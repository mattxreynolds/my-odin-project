#!/usr/bin/env python3
"""Safely scaffold supplied Odin section or project documentation."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def safe_target(root: Path, relative: str, filename: str) -> Path:
    target = (root / relative / filename).resolve()
    if root not in target.parents or not re.fullmatch(r"(?:courses|projects)/\d{2}-[a-z0-9-]+/\d{2}(?:-\d+)?-[a-z0-9-]+", relative):
        raise ValueError("target must be a canonical courses/ or projects/ path")
    if target.exists():
        raise FileExistsError(f"refusing to overwrite authored material: {target}")
    return target


def emit(target: Path, content: str, dry_run: bool) -> None:
    if dry_run:
        print(f"Would create {target}\n\n{content}")
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    print(f"Created {target}")


def section(args: argparse.Namespace) -> None:
    target = safe_target(args.root, args.path, "notes.md")
    lines = [f"# {args.title}", ""]
    if args.started:
        lines.extend([f"Started: {args.started}  ", "Completed:", ""])
    for lesson in args.lesson:
        lines.extend([f"## {lesson}", ""])
    emit(target, "\n".join(lines).rstrip() + "\n", args.dry_run)


def project_readme(args: argparse.Namespace) -> None:
    target = safe_target(args.root, args.path, "README.md")
    template = (args.root / "docs/project-readme-template.md").read_text(encoding="utf-8")
    repository_url = args.repository_url.rstrip("/")
    replacements = {
        "Project%20Name": args.name.replace(" ", "%20"),
        "Project Name": args.name,
        "LIVE_OR_REPOSITORY_URL": repository_url,
        "DD-MM-YYYY": args.started,
        "OFFICIAL_ASSIGNMENT_URL": args.assignment_url,
        "projects/<course>/<project>": args.path,
        "Explain what the project is and what it demonstrates.": args.overview,
    }
    for old, new in replacements.items():
        template = template.replace(old, new)
    emit(target, template, args.dry_run)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    subparsers = parser.add_subparsers(required=True)

    section_parser = subparsers.add_parser("section")
    section_parser.add_argument("--path", required=True)
    section_parser.add_argument("--title", required=True)
    section_parser.add_argument("--lesson", action="append", default=[], required=True)
    section_parser.add_argument("--started")
    section_parser.add_argument("--dry-run", action="store_true")
    section_parser.set_defaults(handler=section)

    project_parser = subparsers.add_parser("project-readme")
    project_parser.add_argument("--path", required=True)
    project_parser.add_argument("--name", required=True)
    project_parser.add_argument("--started", required=True)
    project_parser.add_argument("--assignment-url", required=True)
    project_parser.add_argument("--repository-url", required=True)
    project_parser.add_argument("--overview", required=True)
    project_parser.add_argument("--dry-run", action="store_true")
    project_parser.set_defaults(handler=project_readme)

    args = parser.parse_args()
    args.root = args.root.resolve()
    try:
        args.handler(args)
        return 0
    except (FileExistsError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    raise SystemExit(main())
