#!/usr/bin/env python3
"""Report normalized, read-only facts about this Odin repository."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
COURSE_ABBREVIATIONS = {
    "01-foundations": "fnd",
    "02-intermediate-html-and-css": "ihc",
    "03-javascript": "js",
    "04-advanced-html-and-css": "ahc",
    "05-react": "react",
    "06-databases": "db",
    "07-nodejs": "node",
    "08-getting-hired": "hire",
}


def title_from_slug(value: str) -> str:
    return re.sub(r"^\d+(?:-\d+)?-", "", value).replace("-", " ").title()


def read_progress(root: Path) -> dict[str, str | None]:
    text = (root / "README.md").read_text(encoding="utf-8")
    progress: dict[str, str | None] = {}
    for key in ("Course", "Section", "Active project", "Last updated"):
        match = re.search(rf"^- \*\*{re.escape(key)}:\*\*\s+(.+)$", text, re.M)
        progress[key.lower().replace(" ", "_")] = match.group(1).strip() if match else None
    return progress


def parse_curriculum(root: Path) -> dict[str, list[dict[str, str]]]:
    text = (root / "docs/curriculum-map.md").read_text(encoding="utf-8")
    result: dict[str, list[dict[str, str]]] = {"sections": [], "projects": []}
    course: str | None = None
    kind: str | None = None
    for line in text.splitlines():
        course_match = re.match(r"^## (\d{2}) (.+)$", line)
        if course_match:
            slug = f"{course_match.group(1)}-{course_match.group(2).lower().replace(' ', '-')}"
            course = slug.replace("node-js", "nodejs")
            kind = None
        elif line == "### Course sections":
            kind = "sections"
        elif line == "### Projects":
            kind = "projects"
        elif course and kind:
            path_match = re.search(r"(?:courses|projects)/[^/]+/(\d{2}(?:-\d+)?-[a-z0-9-]+)/?", line)
            tree_match = re.match(r"^[├└]── (\d{2}(?:-\d+)?-[a-z0-9-]+)/?$", line.strip())
            item = path_match.group(1) if path_match else tree_match.group(1) if tree_match else None
            if item and not any(entry["slug"] == item and entry["course"] == course for entry in result[kind]):
                base = "courses" if kind == "sections" else "projects"
                result[kind].append({
                    "course": course,
                    "slug": item,
                    "name": title_from_slug(item),
                    "path": f"{base}/{course}/{item}",
                })
    return result


def git_output(root: Path, *args: str) -> str | None:
    try:
        return subprocess.run(
            ["git", *args], cwd=root, check=True, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def load_issues(path: Path | None) -> list[dict[str, Any]]:
    if path:
        return json.loads(path.read_text(encoding="utf-8"))
    try:
        completed = subprocess.run(
            ["gh", "issue", "list", "--repo", "mattxreynolds/my-odin-project",
             "--state", "all", "--limit", "100", "--json", "number,title,state,body,url"],
            check=True, text=True, timeout=15, stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
        return json.loads(completed.stdout)
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired, json.JSONDecodeError):
        return []


def normalized_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def find_by_name(items: list[dict[str, str]], name: str | None) -> dict[str, str] | None:
    if not name or name.lower() == "none":
        return None
    normalized = normalized_name(name)
    return next((item for item in items if normalized_name(item["name"]) == normalized), None)


def derive_state(
    root: Path = ROOT,
    issues_file: Path | None = None,
    section_name: str | None = None,
    project_name: str | None = None,
) -> dict[str, Any]:
    progress = read_progress(root)
    curriculum = parse_curriculum(root)
    section = find_by_name(curriculum["sections"], section_name or progress["section"])
    active_project = find_by_name(curriculum["projects"], progress["active_project"])
    project = find_by_name(curriculum["projects"], project_name) if project_name else active_project
    issues = load_issues(issues_file) if project else []
    relevant_issue = None
    if project:
        expected_path = f"`{project['path']}`"
        relevant_issue = next((issue for issue in issues if expected_path in issue.get("body", "")), None)

    for item in curriculum["sections"] + curriculum["projects"]:
        item["exists"] = (root / item["path"]).is_dir()
        expected = "notes.md" if item in curriculum["sections"] else "README.md"
        item["expected_file"] = f"{item['path']}/{expected}"
        item["expected_file_exists"] = (root / item["expected_file"]).is_file()
        abbreviation = COURSE_ABBREVIATIONS.get(item["course"], item["course"])
        number = re.match(r"^(\d+)", item["slug"]).group(1)
        prefix = "s" if item in curriculum["sections"] else "p"
        item["scope"] = f"{abbreviation}-{prefix}{number}-{re.sub(r'^\d+(?:-\d+)?-', '', item['slug'])}"
        if prefix == "p":
            item["branch"] = f"project/{item['scope']}"

    inconsistencies: list[str] = []
    if progress["section"] and not section:
        inconsistencies.append("README current section is not present in the curriculum map")
    if section and not section["expected_file_exists"]:
        inconsistencies.append(f"Active section is missing {section['expected_file']}")
    if progress["active_project"] and progress["active_project"].lower() != "none" and not active_project:
        inconsistencies.append("README active project is not present in the curriculum map")
    if active_project and not active_project["expected_file_exists"]:
        inconsistencies.append(f"Active project is missing {active_project['expected_file']}")

    return {
        "repository_root": str(root),
        "branch": git_output(root, "branch", "--show-current"),
        "head": git_output(root, "rev-parse", "HEAD"),
        "working_tree": git_output(root, "status", "--short"),
        "progress": progress,
        "current_section": section,
        "active_project": active_project,
        "selected_project": project if project_name else None,
        "relevant_project_issue": relevant_issue,
        "issue_lookup": "not_needed" if not project else "available" if issues else "unavailable",
        "curriculum": curriculum,
        "inconsistencies": inconsistencies,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--issues-file", type=Path, help="JSON fixture instead of GitHub lookup")
    parser.add_argument("--section", help="Resolve a named section instead of README current section")
    parser.add_argument("--project", help="Resolve a named project instead of README active project")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    print(json.dumps(
        derive_state(args.root.resolve(), args.issues_file, args.section, args.project),
        indent=2 if args.pretty else None,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
