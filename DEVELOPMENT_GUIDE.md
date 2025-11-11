# JamInit Development Guide

This document serves as an internal reference for developing, maintaining, and releasing JamInit.  
It outlines the versioning strategy, release process, file roles, and best practices for consistent development.

## Project Overview

**JamInit** is a Python command-line tool that initializes structured game jam projects.  
It provides standardized folder templates, automation for README and license files, and optional Git setup.

The project is developed using **Python ≥3.12**, packaged with **setuptools**, and distributed via **PyPI** (eventually).

### File Roles

| File / Folder | Purpose |
|----------------|----------|
| `jaminit/__init__.py` | Marks main package and stores version metadata. |
| `jaminit/cli.py` | CLI entry point. Parses user commands and dispatches logic. |
| `jaminit/generator.py` | Main logic: creates directories, files, and templates. |
| `jaminit/utils.py` | Helper functions (filesystem, string formatting, Git). |
| `jaminit/templates/` | Folder templates per engine and common shared files. |
| `tests/` | Unit tests for CLI and core logic. |
| `scripts/build_release.py` | Automates building, tagging, and releasing. |
| `pyproject.toml` | Project configuration, metadata, dependencies, and CLI entry point. |
| `requirements.txt` | Runtime dependencies for installation. |
| `README.md` | Public documentation for users. |
| `LICENSE` | Defines project license (MIT). |

---

## Versioning Convention

JamInit uses **Semantic Versioning (SemVer)** in the format:

```
MAJOR.MINOR.PATCH
```

### Meaning

| Component | Example | Increment When... |
|------------|----------|-------------------|
| **MAJOR** | `1` in `1.2.3` | Breaking changes or redesigns. |
| **MINOR** | `2` in `1.2.3` | New features added, backward compatible. |
| **PATCH** | `3` in `1.2.3` | Bug fixes or small improvements. |

### Version Lifecycle Example

| Version | Purpose |
|----------|----------|
| `0.1.0` | First functional CLI prototype. |
| `0.2.0` | Multi-engine support added. |
| `0.3.0` | Git integration and more options. |
| `0.4.0` | Custom templates introduced. |
| `1.0.0` | Stable release with full documentation. |

### Rules
All version strings must appear in `jaminit/__init__.py` as:
```python
__version__ = "X.Y.Z"
```

Every release is tagged in Git as:
```
vX.Y.Z
```

Never reuse or retroactively change existing version numbers.

## Git Tagging and Releases

Each release should be associated with a matching Git tag.

**Tag Format:**

```
vMAJOR.MINOR.PATCH
```

**Example Commands:**

```bash
git tag v0.1.0
git push --tags
```

**Guidelines:**

* Use `scripts/build_release.py` for automated version bumping and tagging.
* Tag and push every release after successful build and test.
* Avoid tagging manually unless you’re debugging.


## Build and Release Workflow

**Script:** `scripts/build_release.py`

| Command                                   | Action                                    |
| ----------------------------------------- | ----------------------------------------- |
| `python scripts/build_release.py current` | Show current version.                     |
| `python scripts/build_release.py patch`   | Bump patch version, build, tag, and push. |
| `python scripts/build_release.py minor`   | Bump minor version, build, tag, and push. |
| `python scripts/build_release.py major`   | Bump major version, build, tag, and push. |
| `python scripts/build_release.py build`   | Build package without tagging.            |
| `python scripts/build_release.py upload`  | Upload built files to PyPI.               |

**Requirements:**

```
build
twine
```

**Build Output:**

```
dist/
├── jaminit-X.Y.Z.tar.gz
└── jaminit-X.Y.Z-py3-none-any.whl
```

## Testing

Tests are stored in `/tests/` and use **pytest**.

Run all tests:

```bash
pytest
```

Optional flags:

```bash
pytest -v   # verbose
pytest -x   # stop on first failure
```

---

## Code Style and Quality

JamInit follows **PEP 8** and uses **Black** for consistent formatting.

### Tools

* `black` — automatic code formatting
* `flake8` — static code style checker
* `pytest` — testing framework

### Commands

```bash
black jaminit tests
flake8 jaminit
pytest
```

Configuration for all tools is stored in `pyproject.toml`.

---

## Version Development Stages

| Stage             | Version Example | Description                              |
| ----------------- | --------------- | ---------------------------------------- |
| **Alpha**         | `0.1.0`         | Early development, unstable.             |
| **Beta**          | `0.9.0`         | Feature complete, testing in progress.   |
| **Stable**        | `1.0.0`         | Public release, stable API and CLI.      |
| **Patch Updates** | `1.0.1`         | Maintenance fixes or small improvements. |

---

## Best Practices

* Always test before tagging a release.
* Keep `__init__.py` and `pyproject.toml` versions synchronized.
* Use semantic commit messages (e.g., `feat: add godot template support`, `fix: resolve path error`).
* Document every new feature or option in `README.md`.
* Don’t tag or release from unclean Git states.

---

## Quick Reference

| Task                 | Command                                 |
| -------------------- | --------------------------------------- |
| Install dependencies | `pip install -r requirements.txt`       |
| Install in dev mode  | `pip install -e .`                      |
| Run CLI locally      | `jaminit --help`                        |
| Run tests            | `pytest`                                |
| Format code          | `black jaminit tests`                   |
| Build package        | `python scripts/build_release.py build` |
| Bump patch version   | `python scripts/build_release.py patch` |

---

*Last updated: v0.1.0*