#!/usr/bin/env python3
"""Run deterministic, read-only checks for this Odin repository."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from repo_state import ROOT, derive_state

APPROVED_STATUSES = {"Not started", "In progress", "Paused", "Complete", "Portfolio ready", "Archived"}
PLACEHOLDERS = re.compile(
    r"PROJECT_NAME|LIVE_OR_REPOSITORY_URL|OFFICIAL_ASSIGNMENT_URL|DD-MM-YYYY|"
    r"projects/<course>/<project>|Requirement (?:one|two|three)|Objective (?:one|two|three)|"
    r"Explain what the project is|To be completed|To be documented",
    re.I,
)


def finding(severity: str, area: str, message: str, evidence: str) -> dict[str, str]:
    return {"severity": severity, "area": area, "finding": message, "evidence": evidence}


def validate(root: Path) -> list[dict[str, str]]:
    state = derive_state(root)
    findings: list[dict[str, str]] = []
    if (root / "package.json").exists():
        findings.append(finding("error", "architecture", "Root package.json is forbidden", "package.json"))

    for message in state["inconsistencies"]:
        findings.append(finding("warning", "progress", message, "README.md and docs/curriculum-map.md"))

    mapped_paths = {item["path"] for group in state["curriculum"].values() for item in group}
    for base in (root / "courses", root / "projects"):
        if not base.exists():
            findings.append(finding("error", "structure", f"Missing {base.name} directory", base.name))
            continue
        for course in base.iterdir():
            if not course.is_dir():
                continue
            for item in course.iterdir():
                if not item.is_dir():
                    continue
                relative = item.relative_to(root).as_posix()
                if relative not in mapped_paths:
                    findings.append(finding("warning", "curriculum", "Created directory is not mapped", relative))
                if not any(child.is_file() for child in item.rglob("*")):
                    findings.append(finding("warning", "structure", "Premature empty directory", relative))

    for section in state["curriculum"]["sections"]:
        if section["exists"] and not section["expected_file_exists"]:
            findings.append(finding("error", "notes", "Created section is missing notes.md", section["path"]))

    for project in state["curriculum"]["projects"]:
        project_dir = root / project["path"]
        if not project_dir.exists():
            continue
        readme = project_dir / "README.md"
        if not readme.exists():
            findings.append(finding("error", "project", "Created project is missing README.md", project["path"]))
            continue
        text = readme.read_text(encoding="utf-8")
        path_match = re.search(r"\*\*Repository path:\*\*\s*`([^`]+)`", text)
        if path_match and path_match.group(1) != project["path"]:
            findings.append(finding("error", "project", "Project README path does not match curriculum map", str(readme.relative_to(root))))
        status_match = re.search(r"\*\*Status:\*\*\s*(.+)", text)
        if status_match and status_match.group(1).strip() not in APPROVED_STATUSES:
            findings.append(finding("error", "status", "Project uses an unapproved status", status_match.group(0)))
        placeholder = PLACEHOLDERS.search(text)
        if placeholder:
            findings.append(finding("warning", "documentation", "Project README contains unresolved template material", f"{readme.relative_to(root)}: {placeholder.group(0)}"))

    readme = (root / "README.md").read_text(encoding="utf-8")
    for link in re.findall(r"\[[^]]+\]\((?!https?://|#)([^)]+)\)", readme):
        if not (root / link).exists():
            findings.append(finding("error", "links", "README local link target is missing", link))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings = validate(args.root.resolve())
    if args.json:
        print(json.dumps(findings, indent=2))
    elif findings:
        for item in findings:
            print(f"{item['severity'].upper()} [{item['area']}] {item['finding']} — {item['evidence']}")
    else:
        print("No deterministic repository inconsistencies found.")
    return 1 if any(item["severity"] == "error" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
