# helper functions

import os
import shutil
from pathlib import Path

def write_file(path: Path, content: str):
	path.write_text(content, encoding="utf-8")

def copy_template(engine: str, dest: Path):
	template_dir = Path(__file__).parent / "templates" / engine
	if template_dir.exists():
		shutil.copytree(template_dir, dest / "template", dirs_exist_ok=True)
	else:
		print(f"No template found for engine '{engine}'")

def init_git_repo(path: Path):
	os.system(f"cd {path} && git init && git add . && git commit -m 'Initial commit'")
