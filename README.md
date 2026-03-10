# flet-splash-assess

A small test project for [flet-splash](https://github.com/brunobrown/flet-splash): unified, customizable splash screens for Flet apps. This repo checks that flet-splash works with a minimal Flet app and that the web build can be deployed to GitHub Pages.

## What this does

- Runs a minimal Flet app with flet-splash (color type, dark background, 5s minimum) configured in `pyproject.toml`.
- Builds for web with `fs-build web` so flet-splash injects the splash screen into the Flutter build.
- Serves the built site from the `docs/` folder for GitHub Pages.

## Local setup

```bash
uv sync
```

## Run locally (desktop)

```bash
uv run flet run main.py
```

## Build for web (with flet-splash)

```bash
uv run fs-build web
```

Output goes to `build/web/`. To publish on GitHub Pages from `docs/`, copy the contents of `build/web/` into `docs/` (or configure your repo to serve from another branch/folder).

## GitHub Pages

- The live site is served from the **`docs/`** directory.
- At this stage the web build has been added to `docs/` **manually** (e.g. by copying from `build/web/` after `fs-build web`).
- If this approach works well, the next step is to automate deployment with **GitHub Actions** (build and update `docs/` or push to a `gh-pages` branch).

## Links

- [flet-splash](https://github.com/brunobrown/flet-splash) — splash screen injection for Flet
- [Flet](https://flet.dev/) — Python UI framework
