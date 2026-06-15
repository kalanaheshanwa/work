# Repository Guidelines

## Project Structure & Module Organization
This repository is a static site for a Squarespace portfolio. The source of truth is `build.py`, which generates `index.html` and the `projects/*.html` case-study pages. Shared client-side code lives in `assets/app.js` and `assets/styles.css`. Root-level files such as `styles.css`, `favicon*.png`, and `apple-touch-icon.png` support the public site. Treat generated HTML as build output unless you are intentionally patching the published pages.

## Build, Test, and Development Commands
- `python3 build.py` regenerates `index.html` and every `projects/*.html` page.
- `python3 -m http.server 8000` serves the repository locally for browser checks.
- Open `http://localhost:8000/index.html` to verify layout, links, filtering, and project navigation.

## Coding Style & Naming Conventions
Use ASCII unless a file already contains Unicode content. Follow the existing style: 2-space indentation in HTML/CSS/JS, semicolons in JavaScript, lowercase class names, and kebab-case filenames such as `complete-health-collective.html`. Keep edits aligned with the current visual system in `assets/styles.css`; prefer small, targeted changes over broad restyling. If you update project data or page structure, change `build.py` and regenerate output rather than hand-editing every generated page.

## Testing Guidelines
There is no automated test suite in this repository. Validate changes manually in a browser:
- homepage filters and deep links
- project card navigation
- responsive layout on mobile widths
- image loading and outbound links

If you touch generated pages, rebuild and check that the output still matches the source data in `build.py`.

## Commit & Pull Request Guidelines
Commit history is brief and informal, with messages like `Update styles.css` or `Add files via upload`. Use short, imperative messages that describe the actual change. For pull requests, include a concise summary, the files or sections changed, and screenshots for visible UI updates. Note any regenerated pages so reviewers know whether the change came from `build.py` or a direct HTML edit.

## Agent-Specific Instructions
Before editing, inspect `build.py` first. Prefer updating the generator and rerunning it instead of making repeated manual edits to generated HTML.
