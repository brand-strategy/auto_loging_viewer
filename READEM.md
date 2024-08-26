# Auto Log Viewer

This repository generates an HTML file containing the change log based on Git commit history and serves it via GitHub Pages.

## Setup

1. Create the `generate_log.py` script to generate the `change_log.html` file from Git logs.
2. Configure GitHub Actions in the `.github/workflows/generate-log.yml` to automate log generation.

## View the Change Log

You can view the generated change log at `https://username.github.io/auto_loging_viewer/change_log.html`.
