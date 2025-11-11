# main logic (creates folders/files)

import os
from pathlib import Path
from jaminit.utils import write_file, copy_template, init_git_repo

ENGINE_STRUCTURES = {
	"pygame": [
		"src",
		"assets/sprites",
		"assets/sounds",
		"assets/fonts",
	],
	"godot": [
		"scenes",
		"scripts",
		"assets",
	],
	"unity": [
		"Assets",
		"ProjectSettings",
		"Packages",
	],
}

def create_project(name, engine, theme=None, license_type="MIT", git=False):
	project_dir = Path(name.replace(" ", "_").lower())

	if project_dir.exists():
		print(f"Error: directory '{project_dir}' already exists.")
		return

	print(f"Creating new project at {project_dir}/")

	# Pick folder layout for the chosen engine
	folders = ENGINE_STRUCTURES.get(engine.lower())
	if not folders:
		print(f"Unknown engine '{engine}'. Available: {', '.join(ENGINE_STRUCTURES)}")
		return

	for folder in folders:
		os.makedirs(project_dir / folder, exist_ok=True)

	# Common files for all engines
	write_file(project_dir / "README.md", f"# {name}\n\nTheme: {theme or 'N/A'}\nEngine: {engine}\n")
	write_file(project_dir / "requirements.txt", "")
	write_file(project_dir / "LICENSE", f"License: {license_type}\n")

	# Copy engine-specific templates
	copy_template(engine, project_dir)

	if git:
		init_git_repo(project_dir)

	print("Project initialized successfully.")