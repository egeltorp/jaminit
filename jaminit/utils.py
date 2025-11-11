# helper functions

import os
import shutil
from pathlib import Path

def write_file(path: Path, content: str):
	path.write_text(content, encoding="utf-8")

def copy_template(engine: str, dest: Path):
	template_dir = Path(__file__).parent / "templates" / engine
	if not template_dir.exists():
		print(f"No template found for engine '{engine}'")
		return

	for item in template_dir.iterdir():
		target = dest / item.name
		if item.is_dir():
			shutil.copytree(item, target, dirs_exist_ok=True)
		else:
			shutil.copy2(item, target)

def init_git_repo(path: Path):
	os.system(f"cd {path} && git init && git add . && git commit -m 'Initial commit'")
