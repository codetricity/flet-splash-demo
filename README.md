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

Output goes to `build/web/`. For a project site on GitHub Pages (served at `/<repo>/`), build with the same base path so assets load correctly:

```bash
uv run fs-build web --base-url /flet-splash-assess/
```

Replace `flet-splash-assess` with your GitHub repo name if different.

## GitHub Pages

- A **GitHub Action** (`.github/workflows/deploy-pages.yml`) builds the web app and deploys to GitHub Pages on push to `main`.
- The build uses `--base-url /<repo-name>/` so assets and the app load correctly at `https://<owner>.github.io/<repo>/` (project site). Without this, you get 404s for `manifest.json`, splash images, etc.
- In the repo **Settings → Pages**, set **Source** to **GitHub Actions** so the workflow can deploy.
- The workflow does not use the `docs/` folder; you can remove the manually copied `docs/` contents from the repo if you no longer need them.

## Links

- [flet-splash](https://github.com/brunobrown/flet-splash) — splash screen injection for Flet
- [Flet](https://flet.dev/) — Python UI framework
