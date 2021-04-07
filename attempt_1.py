"""Monkeypatch black to use tabs.
"""
import itertools
import sys

import black

# pylint: disable=invalid-name


def Line__str__patch(self) -> str:
	"""Render the line."""
	if not self:
		return "\n"
	indent = "\t" * self.depth
	leaves = iter(self.leaves)
	first = next(leaves)
	res = f"{first.prefix}{indent}{first.value}"
	for leaf in leaves:
		res += str(leaf)
	for comment in itertools.chain.from_iterable(self.comments.values()):
		res += str(comment)

	return res + "\n"


def is_line_short_enough_patch(
	line: black.Line, *, line_length: int, line_str: str = ""
) -> bool:
	"""Return True if `line` is no longer than `line_length`.

	Uses the provided `line_str` rendering, if any, otherwise computes a new one.
	"""
	if not line_str:
		line_str = black.line_to_string(line)
	return (
		len(line_str) + line_str.count("\t") * 3 <= line_length  # "\t" len = 4
		and "\n" not in line_str  # multiline strings
		and not line.contains_standalone_comments()
	)


def fix_docstring_patch(docstring: str, prefix: str) -> str:
	# https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation
	if not docstring:
		return ""
	lines = docstring.splitlines()
	# Determine minimum indentation (first line doesn't count):
	indent = sys.maxsize
	for line in lines[1:]:
		stripped = line.lstrip()
		if stripped:
			indent = min(indent, len(line) - len(stripped))
	# Remove indentation (first line is special):
	trimmed = [lines[0].strip()]
	if indent < sys.maxsize:
		last_line_idx = len(lines) - 2
		for i, line in enumerate(lines[1:]):
			stripped_line = line[indent:].rstrip()
			if stripped_line or i == last_line_idx:
				trimmed.append(prefix + stripped_line)
			else:
				trimmed.append("")
	return "\n".join(trimmed)


black.Line.__str__ = Line__str__patch
black.is_line_short_enough = is_line_short_enough_patch
black.fix_docstring = fix_docstring_patch

main = black.patched_main

main()
