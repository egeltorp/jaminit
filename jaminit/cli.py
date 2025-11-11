# command-line interface entrypoint
# jaminit new "Mini Jam 183" --engine pygame --license MIT --git

import argparse
from jaminit.generator import create_project

def main():
	parser = argparse.ArgumentParser(
		prog="jaminit",
        description=(
    "JamInit — Initialize structured game jam projects fast.\n\n"
    "Examples:\n"
    "  jaminit new \"Mini Jam 183\" --engine pygame --license GPL\n"
    "  jaminit new \"Godot Jam\" --engine godot --git"
    ),
	    formatter_class=argparse.RawTextHelpFormatter
	)
	
	subparsers = parser.add_subparsers(dest="command")

	# --- Subcommand: new ---
	new_parser = subparsers.add_parser("new", help="Create a new game jam project.")
	new_parser.add_argument("name", help="Project name, e.g. 'Mini Jam 183'")
	new_parser.add_argument("--engine", choices=["pygame", "godot", "unity"], default="pygame")
	new_parser.add_argument("--license", choices=["MIT", "GPL", "Unlicense"], default="MIT")
	new_parser.add_argument("--git", action="store_true", help="Initialize a Git repository")

	args = parser.parse_args()

	if args.command == "new":
		create_project(args.name, args.engine, args.license, args.git)
	else:
		parser.print_help()

if __name__ == "__main__":
	main()
