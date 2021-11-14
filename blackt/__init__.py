"""Provides the wrapper methods to black. Requires black to be on the system path"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path

THISDIR = Path(__file__).resolve().parent


def main():
	"""Main entry point"""
	parser = ArgumentParser(add_help=False)
	parser.add_argument("-h", "--help", action="store_true", default=argparse.SUPPRESS)

	args, unknown = parser.parse_known_args()
	if len(args.__dict__) + len(unknown) == 0 or "help" in args.__dict__:
		print((THISDIR / "doc.txt").read_text(encoding="utf-8"))
		sys.exit(0)

	sourceFiles = []
	for root, _dirs, files in os.walk("."):
		for file in files:
			if file.endswith(".py") or file.endswith(".pyi") or file.endswith(".ipynb"):
				sourceFiles.append(os.path.join(root, file))

	# Convert tabs to spaces
	for file in sourceFiles:
		convertFile(file, "\t", "    ")

	# Run black with forwarded args
	exitCode, out = _doSysExec("black " + " ".join(unknown))

	# Convert spaces to tabs
	for file in sourceFiles:
		convertFile(file, "    ", "\t")

	print(out.encode("utf-8").decode("unicode_escape"))  # pylint: disable=no-member
	sys.exit(exitCode)


def convertFile(file: str, find: str, replace: str):
	"""Convert spaces to tabs of vice versa

	Args:
		file (str): file to modify
		find (str): tabs/ spaces to find
		replace (str): tabs/ spaces to replace
	"""
	lines = Path(file).read_text(encoding="utf-8").split("\n")
	outLines = []
	for line in lines:
		match = re.match(f"^({find})*", line)
		span = match.span()
		outLines.append(replace * (span[1] // len(find)) + line[span[1] :])
	Path(file).write_text("\n".join(outLines), encoding="utf-8")


def _doSysExec(command: str, errorAsOut: bool = True) -> tuple[int, str]:
	"""Execute a command and check for errors.

	Args:
		command (str): commands as a string
		errorAsOut (bool, optional): redirect errors to stdout

	Raises:
		RuntimeWarning: throw a warning should there be a non exit code

	Returns:
		tuple[int, str]: tuple of return code (int) and stdout (str)
	"""
	with subprocess.Popen(
		command,
		stdout=subprocess.PIPE,
		stderr=subprocess.STDOUT if errorAsOut else subprocess.PIPE,
		encoding="utf-8",
		errors="ignore",
	) as process:
		out = process.communicate()[0]
		exitCode = process.returncode
		return exitCode, out


if __name__ == "__main__":
	main()
