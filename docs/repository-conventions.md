# Repository Conventions

## Table of contents

1. [Directory naming](#directory-naming)
2. [Commit convention](#commit-convention)
3. [Scopes](#scopes)
4. [Branches](#branches)
5. [Pull requests](#pull-requests)
6. [Issues and labels](#issues-and-labels)
7. [Statuses](#statuses)
8. [Tags](#tags)
9. [Deployment names](#deployment-names)
10. [Environment variables](#environment-variables)

## Directory naming

Use numbered kebab-case names.

### Courses

```text
01-foundations
02-intermediate-html-and-css
03-javascript
04-advanced-html-and-css
05-react
06-databases
07-nodejs
08-getting-hired
```

### Sections and projects

Use two-digit numbering in increments of one:

```text
01-introduction
02-prerequisites
03-git-basics
```

Later insertions can be made as follows:

```text
02-existing-section
02-1-new-section
03-next-section
```

Avoid renaming completed directories unless a curriculum change makes navigation seriously misleading.

## Commit convention

Use:

```text
<type>(<scope>): <imperative summary>
```

Do not place quotation marks around the summary.

### Types

| Type       | Use                                         |
| ---------- | ------------------------------------------- |
| `project`  | Formal-project functionality                |
| `example`  | Lesson examples and exercises               |
| `notes`    | Section notes and knowledge-check answers   |
| `docs`     | READMEs and other documentation             |
| `fix`      | Broken behavior                             |
| `test`     | Automated tests                             |
| `refactor` | Structural changes without behavior changes |
| `style`    | Formatting or visual-only changes           |
| `build`    | Dependencies and build tooling              |
| `ci`       | GitHub Actions and CI                       |
| `chore`    | Repository maintenance                      |
| `perf`     | Performance improvements                    |
| `revert`   | Reverted changes                            |

Examples:

```text
project(fnd-p01-recipes): add recipe navigation
notes(fnd-s04-html-foundations): answer links knowledge checks
example(js-promises): add promise chaining exercise
build(js-p03-restaurant-page): configure webpack
test(js-p06-testing-practice): cover capitalize function
fix(react-p03-shopping-cart): preserve cart state
docs(readme): mark Calculator as complete
```

## Scopes

### Course abbreviations

| Course                    | Abbreviation |
| ------------------------- | ------------ |
| Foundations               | `fnd`        |
| Intermediate HTML and CSS | `ihc`        |
| JavaScript                | `js`         |
| Advanced HTML and CSS     | `ahc`        |
| React                     | `react`      |
| Databases                 | `db`         |
| NodeJS                    | `node`       |
| Getting Hired             | `hire`       |
| Repository-wide work      | `repo`       |

### Projects

```text
<course>-p<number>-<project-slug>
```

Examples:

```text
fnd-p01-recipes
js-p04-todo-list
react-p03-shopping-cart
node-p09-odin-book
```

### Sections

```text
<course>-s<number>-<section-slug>
```

Examples:

```text
fnd-s04-html-foundations
js-s05-testing-javascript
```

### Individual lessons or topics

Use the course abbreviation and a concise lesson slug:

```text
fnd-dom-manipulation
js-promises
react-context
db-joins
```

### Repository-wide scopes

```text
repo
readme
github
license
```

## Branches

Formal project:

```text
project/fnd-p01-recipes
project/js-p04-todo-list
```

Large project milestone:

```text
milestone/node-p09-odin-book-authentication
```

Bug fix:

```text
fix/react-p03-shopping-cart-routing
```

Portfolio improvement:

```text
portfolio/js-p04-todo-list-accessibility
```

Delete merged branches.

## Pull requests

Use pull requests for formal projects and substantial portfolio improvements.

Use the Conventional Commit format for titles:

```text
project(fnd-p01-recipes): complete Recipes
```

Prefer merge commits for formal projects so the project history remains visible. Squash only trivial pull requests.

## Issues and labels

### Issue titles

```text
[Project] Foundations — Recipes
[Bug] Shopping Cart — route refresh returns 404
[Docs] Odin-Book — expand deployment instructions
[Portfolio] Todo List — complete accessibility audit
```

### Base labels

```text
type:project
type:bug
type:docs
type:portfolio
status:blocked
```

### Course labels

Create one course label for every course represented in the project backlog:

    course:foundations
    course:intermediate-html-and-css
    course:javascript
    course:advanced-html-and-css
    course:react
    course:databases
    course:nodejs
    course:getting-hired

Apply the corresponding course label to each formal project Issue.

Formal project Issues may be created in advance as backlog items. An open project Issue does not indicate that the project is in progress. Work begins only when the project branch and directory are created.

Do not create one Issue per lesson.

### Project Issue lifecycle

Formal project Issues are pre-created for the complete curriculum and remain open while they are waiting in the backlog.

When a project begins:

1. Use the existing project Issue.
2. Create the project branch.
3. Create the project directory and README.
4. Complete the project through its normal pull-request workflow.
5. Close the Issue when the project pull request is merged.

Do not create a second Issue when starting a project that already has a backlog Issue.

## Statuses

Use only:

```text
Not started
In progress
Paused
Complete
Portfolio ready
Archived
```

### Testing status

```text
N/A
Manual
Automated
```

### Portfolio status

```text
Learning project
Portfolio candidate
Portfolio ready
Not applicable
```

## Tags

Create annotated tags for completed courses:

```bash
git tag -a course/01-foundations -m "Complete Foundations"
git push origin course/01-foundations
```

Use a project tag only for a substantial polished portfolio milestone:

```text
project/js-p04-todo-list-v1.0.0
```

Do not create GitHub Releases for normal course completion.

## Deployment names

Use:

```text
odin-<project>
```

Examples:

```text
odin-recipes
odin-todo-list
odin-shopping-cart
odin-odin-book
```

## Environment variables

Use uppercase snake case:

```text
DATABASE_URL
SESSION_SECRET
API_KEY
NODE_ENV
PORT
```

Client-exposed Vite variables must use the `VITE_` prefix:

```text
VITE_API_BASE_URL
```

Never place a secret in a `VITE_` variable.

Every project using environment variables must include `.env.example` with empty values.
