"""Provides the wrapper methods to black. Requires black to be on the system path."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path

THISDIR = Path(__file__).resolve().parent

EXCLUDED = [
	".env/",
	".venv/",
	"env/",
	"venv/",
	"ENV/",
	"env.bak/",
	"venv.bak/",
	".svn/",
	"CVS/",
	".bzr/",
	".hg/",
	".git/",
	"__pycache__/",
	".tox/",
	".eggs/",
]


def main() -> None:  # pragma: no cover
	"""Establish the main entry point."""
	parser = ArgumentParser(add_help=False)
	parser.add_argument("-h", "--help", action="store_true", default=argparse.SUPPRESS)

	args, unknown = parser.parse_known_args()
	if len(args.__dict__) + len(unknown) == 0 or "help" in args.__dict__:
		print(_doSysExec("black --help")[1])
		sys.exit(0)

	sourceFiles = findSourceFiles()

	convertTabsToSpaces(sourceFiles, "\t", "    ")

	exitCode: int
	out: str
	exitCode, out = runBlack(unknown)

	convertSpacesToTabs(sourceFiles, "    ", "\t")

	printOutput(out)
	sys.exit(exitCode)


def findSourceFiles() -> list[Path]:
	"""Find source files to process."""
	sourceFiles = []
	for root, _, files in os.walk("."):
		for file in files:
			if file.endswith((".py", ".pyi", ".ipynb")) and not any(x in file for x in EXCLUDED):
				sourceFiles.append(Path(root) / file)
	return sourceFiles


def convertTabsToSpaces(files: list[Path], find: str, replace: str) -> None:
	"""Convert tabs to spaces."""
	for file in files:
		convertFile(file, find, replace)


def convertSpacesToTabs(files: list[Path], find: str, replace: str) -> None:
	"""Convert spaces to tabs."""
	for file in files:
		convertFile(file, find, replace)


def convertFile(file: Path, find: str, replace: str) -> None:
	"""Convert spaces to tabs or vice versa.

	Args:
	----
		file (str): file to modify
		find (str): tabs/ spaces to find
		replace (str): tabs/ spaces to replace
	"""

	with file.open(encoding="utf-8", newline="") as fp:
		out_lines = []

		pattern = re.compile(f"^({find})*")

		for line in fp.read().splitlines(keepends=True):
			match = pattern.match(line)
			span = match.span()  # type:ignore[reportOptionalMemberAccess]
			out_lines.append(replace * (span[1] // len(find)) + line[span[1] :])

		file.write_text("".join(out_lines), encoding="utf-8", newline="")


def runBlack(unknown: list[str]) -> tuple[int, str]:
	"""Run black with forwarded args."""
	return _doSysExec("black " + " ".join(unknown))


def printOutput(out: str) -> None:
	"""Print the output."""
	try:
		print(out.encode("utf-8").decode("unicode_escape"))
	except UnicodeError:
		print(out)


def _doSysExec(command: str, *, errorAsOut: bool = True) -> tuple[int, str]:
	"""Execute a command and check for errors.

	Args:
	----
		command (str): commands as a string
		errorAsOut (bool, optional): redirect errors to stdout

	Returns:
	-------
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


if __name__ == "__main__":  # pragma: no cover
	main()
