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
