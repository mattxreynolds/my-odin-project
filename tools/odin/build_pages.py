#!/usr/bin/env python3
"""Build the curated GitHub Pages artifact for deployed Odin projects."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CANONICAL_PROJECT = re.compile(
    r"projects/\d{2}-[a-z0-9-]+/\d{2}(?:-\d+)?-[a-z0-9-]+"
)
PROJECT_ID = re.compile(r"[a-z]+-p\d{2}-[a-z0-9-]+")


class ManifestError(ValueError):
    """Report an invalid or unsafe Pages publication manifest."""


def canonical_project_path(value: object, field: str) -> str:
    if not isinstance(value, str) or not CANONICAL_PROJECT.fullmatch(value):
        raise ManifestError(f"{field} must be a canonical projects/ path")
    return value


def load_manifest(root: Path, manifest_path: Path) -> dict[str, Any]:
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ManifestError(f"cannot read Pages manifest: {error}") from error

    if not isinstance(data, dict) or not isinstance(data.get("site_title"), str):
        raise ManifestError("manifest must contain a site_title string")
    projects = data.get("projects")
    if not isinstance(projects, list) or not projects:
        raise ManifestError("manifest must contain at least one project")

    seen_ids: set[str] = set()
    seen_destinations: set[str] = set()
    for project in projects:
        if not isinstance(project, dict):
            raise ManifestError("each project entry must be an object")
        project_id = project.get("id")
        if not isinstance(project_id, str) or not PROJECT_ID.fullmatch(project_id):
            raise ManifestError("each project id must use the repository project scope format")
        if project_id in seen_ids:
            raise ManifestError(f"duplicate project id: {project_id}")
        seen_ids.add(project_id)

        if not isinstance(project.get("title"), str) or not project["title"].strip():
            raise ManifestError(f"{project_id} must have a non-empty title")
        source = canonical_project_path(project.get("source"), f"{project_id} source")
        destination = canonical_project_path(project.get("destination"), f"{project_id} destination")
        if source != destination:
            raise ManifestError(f"{project_id} destination must match its repository path")
        if destination in seen_destinations:
            raise ManifestError(f"duplicate destination: {destination}")
        seen_destinations.add(destination)
        if project.get("mode") != "static":
            raise ManifestError(f"{project_id} uses unsupported publication mode")

        source_path = root / source
        if not source_path.is_dir() or not (source_path / "index.html").is_file():
            raise ManifestError(f"{project_id} static source must contain index.html")
        if any(path.is_symlink() for path in source_path.rglob("*")):
            raise ManifestError(f"{project_id} static source must not contain symbolic links")
        excludes = project.get("exclude", [])
        if not isinstance(excludes, list) or not all(
            isinstance(item, str) and item and Path(item).name == item for item in excludes
        ):
            raise ManifestError(f"{project_id} exclude values must be plain file names")

    return data


def write_index(output: Path, title: str, projects: list[dict[str, Any]]) -> None:
    links = "\n".join(
        f'        <li><a href="./{html.escape(project["destination"])}/">'
        f'{html.escape(project["title"])}</a></li>'
        for project in projects
    )
    content = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)}</title>
  </head>
  <body>
    <main>
      <h1>{html.escape(title)}</h1>
      <p>Completed projects from The Odin Project.</p>
      <ul>
{links}
      </ul>
    </main>
  </body>
</html>
"""
    (output / "index.html").write_text(content, encoding="utf-8")


def build(root: Path, manifest_path: Path, output: Path) -> None:
    if output.exists():
        raise ManifestError(f"refusing to overwrite existing output: {output}")
    data = load_manifest(root, manifest_path)
    output.mkdir(parents=True)
    write_index(output, data["site_title"], data["projects"])
    (output / ".nojekyll").touch()

    for project in data["projects"]:
        source = root / project["source"]
        destination = output / project["destination"]
        shutil.copytree(
            source,
            destination,
            ignore=shutil.ignore_patterns(*project.get("exclude", [])),
        )
        print(f"Published {project['id']} to {project['destination']}/")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = args.manifest.resolve() if args.manifest else root / "deploy/pages-projects.json"
    try:
        build(root, manifest, args.output.resolve())
        return 0
    except ManifestError as error:
        parser.error(str(error))


if __name__ == "__main__":
    raise SystemExit(main())
