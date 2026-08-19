<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,100:2563EB&height=220&section=header&text=Recipes&fontSize=48&fontColor=FFFFFF&animation=fadeIn&fontAlignY=38&desc=The%20Odin%20Project&descAlignY=58&descSize=20"
    alt="Recipes banner"
  >
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel" />
</p>

<h1 align="center"><a href="https://odin-recipes-gamma.vercel.app" target="_blank">Recipes</a></h1>

<p align="center">A multi-page recipe website demonstrating foundational HTML, relative links, images, lists, and a structured Git workflow.</p>

## Status

- **Status:** Complete
- **Started:** 07-08-2026
- **Completed:** 19-08-2026
- **Portfolio readiness:** Learning project

## Links

- **Assignment:** [The Odin Project — Recipes](https://www.theodinproject.com/lessons/foundations-recipes)
- **Live demo:** [odin-recipes-gamma.vercel.app](https://odin-recipes-gamma.vercel.app)
- **Repository path:** `projects/01-foundations/01-recipes`

## Overview

Recipes is the first formal project in The Odin Project Foundations course. It is a small, HTML-only website with a homepage and three individual recipe pages: Greek Yoghurt Pancakes, One-Pan Spaghetti, and Chocolate Layer Cake.

The project demonstrates how complete HTML documents, semantic content elements, relative paths, local images, and multi-page navigation work together without CSS, JavaScript, a build system, or external dependencies.

## Table of contents

- [Status](#status)
- [Links](#links)
- [Overview](#overview)
- [Assignment requirements](#assignment-requirements)
- [Learning objectives](#learning-objectives)
- [Tech stack](#tech-stack)
- [Project structure](#project-structure)
- [Key features](#key-features)
- [Design and implementation](#design-and-implementation)
- [Local development](#local-development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Accessibility](#accessibility)
- [Challenges and solutions](#challenges-and-solutions)
- [Known limitations](#known-limitations)
- [Retrospective](#retrospective)
- [Attribution](#attribution)
- [License](#license)

## Assignment requirements

- [x] Create a homepage with the standard HTML boilerplate and a site heading.
- [x] Store individual recipe pages in a dedicated `recipes` directory.
- [x] Link the homepage to each recipe using relative paths.
- [x] Add a finished-dish image and descriptive alternative text to every recipe.
- [x] Give every recipe a description, unordered ingredients list, and ordered steps list.
- [x] Create three recipe pages with a consistent overall structure.
- [x] Provide a link from every recipe back to the homepage.
- [x] Use meaningful Git commits throughout development.

## Learning objectives

- Create complete HTML documents using the standard boilerplate.
- Use headings, paragraphs, links, images, and lists for their intended purposes.
- Navigate between pages and load local assets with relative paths.
- Organise related pages and images into a clear directory structure.
- Write useful image alternative text.
- Use ordered and unordered lists to represent different kinds of content.
- Build the project incrementally with small, descriptive Git commits.

## Tech stack

| Technology | Role                                                            |
| ---------- | --------------------------------------------------------------- |
| HTML5      | Structures the homepage, recipe content, navigation, and images |
| Git        | Tracks the project through incremental commits                  |
| GitHub     | Hosts the repository and project source                         |
| Vercel     | Deploys and hosts the production website                        |

The project intentionally has no CSS, JavaScript, package dependencies, or build tooling because its scope is foundational HTML.

## Project structure

```text
01-recipes/
├── index.html                         # Homepage and recipe navigation
├── README.md                          # Project documentation
└── recipes/
    ├── chocolate-layer-cake.html
    ├── greek-yoghurt-pancakes.html
    ├── one-pan-spaghetti.html
    └── images/
        ├── chocolate-layer-cake.jpg
        ├── greek-yoghurt-pancakes.jpg
        └── one-pan-spaghetti.jpg
```

## Key features

- A central homepage linking to all three recipes.
- Dedicated pages for Greek Yoghurt Pancakes, One-Pan Spaghetti, and Chocolate Layer Cake.
- Descriptions, ingredient lists, and ordered cooking instructions for each dish.
- Locally stored dish images with alternative text and explicit display widths.
- Return-home navigation on every recipe page.
- No dependency on JavaScript or third-party runtime services.

## Design and implementation

Each page is a standalone HTML document with its own metadata, page title, and top-level heading. The homepage acts as the navigation hub, while the recipe pages share the same simple content order: title, image, description, ingredients, steps, and return link.

Relative paths keep the site portable. The homepage links down into `recipes/`, each recipe loads its image from `recipes/images/`, and `../index.html` returns to the homepage. Images live beside the recipe pages they support rather than depending on remote URLs.

The deliberately unstyled presentation keeps the work focused on semantic HTML and document organisation, matching the assignment's scope.

## Local development

### Prerequisites

- Git, if cloning the repository
- A modern web browser

### Run

From the repository root:

```bash
cd projects/01-foundations/01-recipes
```

Open `index.html` directly in a browser. Alternatively, serve the directory locally:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`. No installation, environment variables, or build step is required.

## Testing

- **Status:** Manual
- **Automated test command:** Not applicable

The final source review verified that:

- all four pages contain the HTML5 doctype, language declaration, character encoding, viewport metadata, title, and one top-level heading;
- all homepage recipe links resolve to existing pages;
- every recipe image path resolves to a local image;
- every image has non-empty alternative text; and
- every recipe has description, ingredients, steps, and a working relative link back to the homepage.

There is no automated test suite because the project is a small static HTML exercise. Visual rendering and link navigation should also be checked in a browser after future content changes.

## Deployment

- **Provider:** Vercel
- **Production URL:** [https://odin-recipes-gamma.vercel.app](https://odin-recipes-gamma.vercel.app)
- **Root directory:** `projects/01-foundations/01-recipes`
- **Build command:** Not applicable
- **Output directory:** Not applicable
- **Environment variables:** None

Vercel publishes the project directory as a static site. No build step, output directory, or runtime configuration is required.

## Accessibility

- The pages declare English as their document language.
- Heading levels give each recipe a clear content hierarchy.
- Recipe navigation uses native links and lists, so it remains keyboard accessible without custom scripting.
- Each dish image includes concise alternative text.
- Ingredients and cooking steps use semantic unordered and ordered lists.
- The viewport metadata supports browser scaling on smaller screens.

The project has not undergone a formal assistive-technology audit. The fixed image widths can also overflow narrow viewports because responsive CSS is outside this assignment's scope.

## Challenges and solutions

### Managing relative paths

Moving from the homepage into a nested recipe directory changes the path needed for both navigation and images. The project solves this by linking from the homepage with `./recipes/...`, loading images relative to each recipe with `./images/...`, and returning one directory level with `../index.html`.

### Keeping repeated pages consistent

Three standalone documents can easily drift into different structures. Reusing the same section order and heading hierarchy across every recipe makes the pages predictable and makes missing content easier to spot during review.

## Known limitations

- The site is intentionally unstyled and uses the browser's default presentation.
- Fixed image widths are not responsive and may overflow on small screens.
- Navigation is limited to the homepage and a return link; recipe pages do not link directly to one another.
- Recipe content is static and cannot be searched, filtered, scaled, or edited in the browser.
- The site has not been formally audited with accessibility tools.

## Retrospective

### What I learned

I learned how relative paths depend on the current document's directory, how semantic lists make recipe content easier to understand, and how a shared page structure keeps a multi-page site consistent.

### What went well

Building one recipe at a time kept the work manageable. The final directory structure is small and predictable, every page can be opened independently, and the Git history records the site's incremental growth.

### What I would approach differently

I would verify spelling, units, alternative text, and source attribution as each recipe is added instead of leaving the full content review until the end. I would also use a small validation checklist for every repeated page.

### Potential improvements

- Add responsive CSS for typography, spacing, navigation, and images.
- Add direct previous/next navigation between recipes.
- Validate the pages with an HTML validator and test them with accessibility tooling.
- Add automated HTML validation to catch markup regressions.

## Attribution

- Project brief: [The Odin Project — Recipes](https://www.theodinproject.com/lessons/foundations-recipes).
- [Greek Yogurt Pancakes](https://www.allrecipes.com/recipe/244286/greek-yogurt-pancakes/) — recipe source.
- [One-Pan Dirty Spaghetti](https://www.allrecipes.com/one-pan-dirty-spaghetti-recipe-11930383) — recipe source.
- [Moist Chocolate Layer Cake](https://www.allrecipes.com/recipe/232342/moist-chocolate-layer-cake/) — recipe source.

## License

Original code and documentation in this directory are covered by the repository [MIT License](../../../LICENSE). Third-party recipe content and images remain subject to their original terms and are excluded from that licence unless their provenance establishes otherwise.
