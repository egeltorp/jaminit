<p align="center">
	<img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white">
	<img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-magenta?&logoColor=white">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen">
  <img src="https://img.shields.io/badge/Contributions-Welcome-yellow">
	<img src="https://img.shields.io/badge/Platforms-macOS%20%7C%20Linux%20%7C%20Windows%20(Bash)-lightgrey?logo=linux&logoColor=white">
	<img src="https://img.shields.io/badge/License-MIT-green">
</p>

# JamInit
JamInit is a command-line tool for creating standardized project structures for game jams.  
It aims to reduce setup time and promote consistency across multiple game jam projects.  

## Features
- Initializes new game jam projects with predefined folder structures.
- Supports multiple engines (Pygame, Godot, Unity).
- Generates template files including README, LICENSE, and .gitignore.
- Optionally initializes a Git repository.
- Configurable templates for custom workflows.


## Installation
JamInit requires Python 3.10 or higher.

```bash
git clone https://github.com/egeltorp/jaminit.git
cd jaminit
pip install -e .
```

## Usage
Create a new game jam project:

```bash
jaminit new "Mini Jam 183" --engine pygame --theme "Dreams" --license MIT --git
```

Example output:

```yaml
mini_jam_183_dreams/
├── src/
│   └── main.py
├── assets/
│   ├── sprites/
│   ├── sounds/
│   └── fonts/
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

Command help:

```bash
jaminit --help
```

## Roadmap

| Version | Milestone | Description |
|:--------:|:-----------|:-------------|
| **v0.1.0** | Core functionality | Implement base CLI using `argparse`. Add support for initializing Godot projects with predefined folder structure and template files. Include auto-generated README, LICENSE, and `.gitignore`. |
| **v0.2.0** | Multi-engine support | Add templates for Pygame and Unity projects. Introduce a shared configuration file defining default directory layout and file templates per engine. |
| **v0.3.0** | Git and license automation | Add optional `--git` flag to automatically run `git init` and create a `.gitignore`. Include `--license` option for MIT, GPL, CC-BY, and Unlicense. |
| **v0.4.0** | Template customization | Allow users to define and store custom templates under `~/.jaminit/templates/`. Add `jaminit template create` and `jaminit template list` commands. |
| **v0.5.0** | Metadata and config files | Introduce a `.jaminit.json` configuration file per project to store metadata (jam name, engine, theme, version). Add command to regenerate project README from metadata. |
| **v0.6.0** | Project regeneration | Add `jaminit refresh` to reapply template updates to an existing project without overwriting code. |
| **v0.7.0** | Cross-platform polish | Add full Windows/macOS/Linux support testing, path normalization, and graceful error handling for filesystem issues. |
| **v0.8.0** | Interactive mode | Add optional interactive wizard (`jaminit new` without args) that prompts the user for engine, theme, and license step-by-step. |
| **v1.0.0** | Stable release | Comprehensive documentation, unit tests, and CI integration (GitHub Actions). Command autocompletion for Bash, Zsh, and PowerShell. |


## Repository Structure

```yaml
jaminit/
├── jaminit/
│ ├── init.py
│ ├── cli.py # Handles command-line parsing and entrypoint
│ ├── generator.py # Core logic for creating folders and files
│ ├── templates/
│ │ ├── pygame/ # Engine-specific templates
│ │ ├── godot/
│ │ ├── unity/
│ │ └── common/ # Shared templates like README, LICENSE, etc.
│ └── utils.py # Helper functions
│
├── tests/
│ ├── init.py
│ ├── test_cli.py
│ ├── test_generator.py
│ └── test_templates.py
│
├── scripts/
│ └── build_release.py # Optional automation for packaging
│
├── LICENSE
├── README.md
├── pyproject.toml # For modern packaging
├── setup.cfg # Metadata and configuration
├── requirements.txt
└── .gitignore
```

## Contributing
Contributions are welcome.
Open an issue before submitting major changes.
Use conventional commit messages where possible.

## License
Licensed under the MIT License.  
See LICENSE for details.
