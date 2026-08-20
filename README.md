# My Odin Project

A public learning archive containing the notes, exercises, and standalone projects I create while completing [The Odin Project](https://www.theodinproject.com/) Foundations course and Full Stack JavaScript path.

## Table of contents

- [Current progress](#current-progress)
- [Course progress](#course-progress)
- [Projects](#projects)
- [Repository structure](#repository-structure)
- [Working with the repository](#working-with-the-repository)
- [Documentation](#documentation)
- [License](#license)

## Current progress

- **Course:** Foundations
- **Section:** CSS Foundations
- **Active project:** None
- **Last updated:** 19 August 2026

## Course progress

| Course                    | Status      | Completed |
| ------------------------- | ----------- | --------- |
| Foundations               | In progress | —         |
| Intermediate HTML and CSS | Not started | —         |
| JavaScript                | Not started | —         |
| Advanced HTML and CSS     | Not started | —         |
| React                     | Not started | —         |
| Databases                 | Not started | —         |
| NodeJS                    | Not started | —         |
| Getting Hired             | Not started | —         |

## Projects

Formal Odin projects are added to this table when work begins. Each project directory contains its own detailed README with setup instructions, requirements, design decisions, testing, deployment information, and a retrospective.

| ID      | Project | Course      | Status   | Code                                        | Live                                          | Completed  | Portfolio        |
| ------- | ------- | ----------- | -------- | ------------------------------------------- | --------------------------------------------- | ---------- | ---------------- |
| FND-P01 | Recipes | Foundations | Complete | [Code](projects/01-foundations/01-recipes/) | [Live](https://mattxreynolds.github.io/my-odin-project/projects/01-foundations/01-recipes/) | 19-08-2026 | Learning project |

The complete planned project order is available in the [curriculum map](docs/curriculum-map.md).

Formal project Issues are pre-created as the curriculum backlog. An open Issue does not indicate that a project has started; projects appear in the table above only when implementation begins.

## Repository structure

```text
.
├── courses/     # Notes, knowledge-check answers, SQL queries, and exercises
├── projects/    # Standalone Odin projects
├── docs/        # Curriculum map, conventions, and documentation templates
└── .github/     # Issue and pull-request templates
```

Course material is organized by official course and section. Formal assignments are stored as standalone applications under `projects/`.

The full structure is documented in [The Odin Project Repository Plan](ODIN_REPOSITORY_PLAN.md).

## Working with the repository

### Course notes and examples

Small lesson updates are committed directly to `main`.

```text
notes(fnd-s04-html-foundations): answer links knowledge checks
example(fnd-dom-manipulation): add event listener exercise
```

### Formal projects

Each formal project uses its own branch, Issue, and pull request.

```bash
git switch main
git pull --ff-only
git switch -c project/fnd-p01-recipes
```

For npm-based projects, run commands from the individual project directory:

```bash
cd projects/<course>/<project>
npm ci
npm run dev
```

This repository does not use a root `package.json`, npm workspaces, or shared runtime dependencies.

## Documentation

- [Repository plan](ODIN_REPOSITORY_PLAN.md)
- [Curriculum map](docs/curriculum-map.md)
- [Repository conventions](docs/repository-conventions.md)
- [Project README template](docs/project-readme-template.md)

## License

Original code and documentation are licensed under the [MIT License](LICENSE) unless a file states otherwise.

The Odin Project material, supplied starter files, third-party assets, libraries, APIs, and other external resources remain subject to their original terms. See [Third-Party Notices](THIRD_PARTY_NOTICES.md).
