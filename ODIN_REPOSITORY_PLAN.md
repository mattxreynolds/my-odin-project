# The Odin Project Repository Plan

**Repository:** `mattxreynolds/my-odin-project`  
**Research baseline:** 30 July 2026  
**Environment:** Windows with WSL2  
**Package manager:** npm  
**Preferred frontend host:** Vercel

## Table of contents

1. [Goals](#1-goals)
2. [Repository structure](#2-repository-structure)
3. [Directory policy](#3-directory-policy)
4. [Standalone projects](#4-standalone-projects)
5. [Git workflow](#5-git-workflow)
6. [Documentation and progress](#6-documentation-and-progress)
7. [Deployment](#7-deployment)
8. [GitHub and automation](#8-github-and-automation)
9. [Initial setup](#9-initial-setup)
10. [Ongoing routine](#10-ongoing-routine)
11. [Supporting documents](#11-supporting-documents)

## 1. Goals

Use one Git repository for all work completed during The Odin Project Foundations course and Full Stack JavaScript path.

The repository should work as:

- a personal learning archive;
- a public progress record;
- a recruiter-friendly portfolio.

Keep repository management lightweight. Do not create nested Git repositories, separate project repositories, a JavaScript workspace, or automation that provides little practical value.

## 2. Repository structure

The primary content directories are:

```text
courses/
projects/
```

- `courses/` contains lesson notes, knowledge-check answers, SQL queries, exercises, and small demonstrations.
- `projects/` contains formal Odin projects as standalone applications.

```text
my-odin-project/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── work-item.md
│   └── pull_request_template.md
├── courses/
│   ├── 01-foundations/
│   ├── 02-intermediate-html-and-css/
│   ├── 03-javascript/
│   ├── 04-advanced-html-and-css/
│   ├── 05-react/
│   ├── 06-databases/
│   ├── 07-nodejs/
│   └── 08-getting-hired/
├── projects/
│   ├── 01-foundations/
│   ├── 02-intermediate-html-and-css/
│   ├── 03-javascript/
│   ├── 04-advanced-html-and-css/
│   ├── 05-react/
│   ├── 06-databases/
│   ├── 07-nodejs/
│   └── 08-getting-hired/
├── docs/
│   ├── curriculum-map.md
│   ├── project-readme-template.md
│   └── repository-conventions.md
├── .editorconfig
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
└── THIRD_PARTY_NOTICES.md
```

This is the intended final shape, not a list of directories to create immediately. The complete course and project order is in [docs/curriculum-map.md](docs/curriculum-map.md).

## 3. Directory policy

### Course material

Organize `courses/` by course and official section:

```text
courses/03-javascript/
├── 01-introduction/
│   └── notes.md
├── 02-organizing-javascript-code/
│   ├── notes.md
│   └── modules/
└── 03-javascript-in-the-real-world/
    ├── notes.md
    └── form-validation/
```

Use one `notes.md` per official section.

| Lesson output                                  | Store it as                              |
| ---------------------------------------------- | ---------------------------------------- |
| Conceptual material or knowledge checks        | A heading in section `notes.md`          |
| One focused example                            | An individual file                       |
| Several related files, assets, or dependencies | A topic directory                        |
| Formal Odin assignment                         | A standalone directory under `projects/` |

Do not create one directory per lesson automatically.

Keep personal notes, knowledge-check answers, SQL queries, meaningful exercises, and reusable debugging examples. Do not store copied lesson text, raw logs, secrets, application tracking, employer research, or private résumé information.

### Projects

Number projects within each course:

```text
projects/03-javascript/04-todo-list/
```

Do not create `-v2`, `-new`, or `-final` directories. Use Git history and branches for revisions.

## 4. Standalone projects

Each project must be independently installable, runnable, testable, and deployable.

An npm-based project owns its own:

```text
README.md
package.json
package-lock.json
src/
tests/
assets/ or public/
project-specific configuration
.env.example when required
deployment configuration when required
```

Rules:

- no root `package.json`;
- no npm workspaces;
- no root runtime dependencies;
- no shared `node_modules`;
- commit each project's lockfile;
- follow Odin's tooling instructions for each assignment;
- keep shared standards limited to documentation and naming.

Run commands from the project directory:

```bash
cd projects/03-javascript/04-todo-list
npm ci
npm run dev
```

## 5. Git workflow

### Course notes and small examples

Commit directly to `main`.

```text
notes(fnd-s04-html-foundations): answer links knowledge checks
example(fnd-dom-manipulation): add event listener exercise
```

### Formal projects

Use one branch, Issue, and pull request per project.

```bash
git switch main
git pull --ff-only
git switch -c project/fnd-p01-recipes
```

Project workflow:

1. Create the Issue and branch.
2. Create the project directory and README.
3. Implement the assignment in focused commits.
4. Test and deploy it.
5. Complete the README and retrospective.
6. Update the root README.
7. Merge the pull request and delete the branch.

Use Conventional Commit syntax with Odin-specific scopes:

```text
<type>(<scope>): <imperative summary>
```

```text
project(fnd-p01-recipes): add recipe navigation
build(js-p03-restaurant-page): configure webpack
test(js-p06-testing-practice): cover capitalize function
fix(react-p03-shopping-cart): preserve cart state
```

See [docs/repository-conventions.md](docs/repository-conventions.md) for the complete naming, scope, branch, label, status, and tag rules.

## 6. Documentation and progress

### Root README

Use the root README as the permanent progress index. Include:

- current course, section, and active project;
- course statuses and completion dates;
- a concise project table;
- links to course material, project code, and deployments;
- a short repository guide;
- license information.

Recommended project table:

| ID  | Project | Course | Status | Code | Live | Completed | Portfolio |
| --- | ------- | ------ | ------ | ---- | ---- | --------- | --------- |

Track actual completion dates and current status. Do not track target dates or estimated effort.

### Project README

Every formal project receives a detailed README based on [docs/project-readme-template.md](docs/project-readme-template.md).

It should cover the assignment, setup, functionality, technology, design decisions, testing, deployment, accessibility where relevant, challenges, limitations, retrospective, attribution, and licensing.

Screenshots are optional and not required.

### Issues

Create Issues for formal projects, unresolved bugs, blockers, substantial documentation tasks, and portfolio improvements. Do not create Issues for individual lessons or minor edits.

## 7. Deployment

Publish every runnable project.

### Frontend

Prefer Vercel for static sites, Vite applications, React applications, and frontend portions of full-stack projects.

Create a separate Vercel project for each deployable directory and set its Root Directory.

```text
Deployment name: odin-<course>-<project>
Root Directory: projects/05-react/03-shopping-cart
Build Command: npm run build
Output Directory: dist
```

Add routing configuration only when the project requires it.

### Node and PostgreSQL

Do not force persistent Express/PostgreSQL applications onto Vercel. Follow the current Odin assignment and use an appropriate Node PaaS and managed database provider.

Document the provider, build command, start command, migrations, database setup, and environment-variable names in the project README. Never commit credentials.

## 8. GitHub and automation

| Timing         | Features                                                                                                                                                                                     |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use now        | Issues, lightweight labels, branches, pull requests, templates, license, repository topics, secret protection                                                                                |
| Add later      | Course milestones, project-specific CI, Dependabot security updates, selected CodeQL workflows, documentation validation                                                                     |
| Skip initially | GitHub Projects, one Issue per lesson, root JavaScript tooling, scaffolding generators, root lint/test commands, Codespaces, dev containers, Wiki, Discussions, CODEOWNERS, complex rulesets |

Automation should be added only after repetition proves it useful. Project-specific GitHub Actions should use path filters so unrelated projects are not installed or tested.

## 9. Initial setup

Create only:

```text
.github/
docs/
README.md
LICENSE
THIRD_PARTY_NOTICES.md
.editorconfig
.gitattributes
.gitignore
```

Then:

1. Replace the root README with a progress-oriented version.
2. Add the supporting documents below.
3. Add one Issue template and one pull-request template.
4. Add the MIT License and third-party notice.
5. Retain the existing editor-neutral configuration.
6. Update `.gitignore` for dependencies, builds, deployment files, databases, environment files, and editors.
7. Verify secret scanning and push protection where available.
8. Create `courses/01-foundations/` only when Foundations begins.
9. Create the first project directory only when Recipes begins.

Suggested commits:

```text
docs(readme): add curriculum progress structure
docs(repo): add repository planning documents
docs(license): add license and third-party notice
chore(github): add issue and pull request templates
```

## 10. Ongoing routine

### Lesson work

Pull `main`, update the current section, commit one coherent change, and push.

### Section completion

Review the notes and examples, remove unused placeholders, verify source links, record the completion date, and update the root README.

### Project completion

Run available tests, linting, and builds; verify the deployment; complete the README and retrospective; update the project table; merge the pull request; delete the branch; and close the Issue.

### Course completion

Confirm required projects and deployments, record the completion date, and create an annotated tag:

```bash
git tag -a course/01-foundations -m "Complete Foundations"
git push origin course/01-foundations
```

### Portfolio maintenance

Periodically review selected projects for deployment health, responsiveness, accessibility, console errors, dependency alerts, tests, and documentation. Only active portfolio projects require ongoing dependency maintenance.

## 11. Supporting documents

- [Complete curriculum map](docs/curriculum-map.md)
- [Repository conventions](docs/repository-conventions.md)
- [Project README template](docs/project-readme-template.md)
