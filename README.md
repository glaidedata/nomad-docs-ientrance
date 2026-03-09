# AK Feldhoff Oasis Documentation

This repository contains the source and generated static site for the AK Feldhoff NOMAD Oasis documentation, built with MkDocs + Material.

## Structure

- `docs/` - Markdown source content, assets, and theme overrides
- `mkdocs.yml` - MkDocs configuration (navigation, theme, footer, plugins)
- `site/` - Generated static site output
- `LICENSE` - Apache License 2.0
- `LICENSE_GLAIDE` - Project-specific attribution notice

## Local Development

```bash
pip install -r requirements_docs.txt
mkdocs serve
```

Open the local URL shown in terminal (usually `http://127.0.0.1:8000`).

## Build Static Site

```bash
mkdocs build --clean
```

This regenerates the static output in `site/`.

## Deployment

Deploy the contents of `site/` to the Oasis web root (or your configured static hosting target).

## License

Licensed under the Apache License, Version 2.0.  
See `LICENSE` and `LICENSE_GLAIDE` for details.
