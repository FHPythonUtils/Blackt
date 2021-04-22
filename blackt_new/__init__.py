import itertools
import sys
from enum import Enum
from typing import Iterator, Any
from copy import deepcopy

import black
from black import Leaf, get_string_prefix, is_docstring, Path, WriteBack
from click.decorators import version_option

# pylint: disable=invalid-name


__version__ = "2021a4"
black_format_file_in_place = lambda: True


class Mode(Enum):
	asynchronous = 1
	synchronous = 2


BLACKT_PATCH = [
	# Synchronous Monkees.
	("format_file_in_place", Mode.synchronous),
	#("Line", Mode.synchronous),
	#("LineGenerator", Mode.synchronous),
	#("is_line_short_enough", Mode.synchronous),
	#("fix_docstring", Mode.synchronous),
	# Asynchronous Monkees.
	#("Line", Mode.asynchronous),
	#("LineGenerator", Mode.asynchronous),
	#("is_line_short_enough", Mode.asynchronous),
	#("fix_docstring", Mode.asynchronous),
]


def monkey_patch_black(mode: Mode) -> None:
	blackt = sys.modules["blackt"]
	for function_name, monkey_mode in BLACKT_PATCH:
		if monkey_mode is mode:
			setattr(black, function_name, getattr(blackt, function_name))


class Line(black.Line):
	def __str__(self) -> str:
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


class LineGenerator(black.LineGenerator):
	def visit_STRING(self, leaf: Leaf) -> Iterator[Line]:
		if is_docstring(leaf) and "\\\n" not in leaf.value:
			# We're ignoring docstrings with backslash newline escapes because changing
			# indentation of those changes the AST representation of the code.
			prefix = get_string_prefix(leaf.value)
			lead_len = len(prefix) + 3
			tail_len = -3
			indent = "\t" * self.current_line.depth
			docstring = fix_docstring(leaf.value[lead_len:tail_len], indent)
			if docstring:
				if leaf.value[lead_len - 1] == docstring[0]:
					docstring = " " + docstring
				if leaf.value[tail_len + 1] == docstring[-1]:
					docstring = docstring + " "
			leaf.value = leaf.value[0:lead_len] + docstring + leaf.value[tail_len:]

		yield from self.visit_default(leaf)


def is_line_short_enough(line: black.Line, *, line_length: int, line_str: str = "") -> bool:
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


def fix_docstring(docstring: str, prefix: str) -> str:
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


def format_file_in_place(*args, **kws):
	# This is a convenient place to monkey patch any function that must be
	# done after black's asynchronous invocation.
	# print(dir(black))
	#monkey_patch_black(Mode.asynchronous)
	return black_format_file_in_place(*args, **kws)

def test(src: Path,
    fast: bool,
    mode: Mode,
    write_back: WriteBack = WriteBack.NO,
    lock: Any = None,):
	return True


def main():
	#monkey_patch_black(Mode.synchronous)
	black.format_file_in_place = test
	# Reach in and monkey patch the Click options. This is tricky based on the
	# way Click works! This is highly fragile because the index into the Click
	# parameters is dependent on the decorator order for Black's main().
	# Change the target version help doc to mention "BlackT", not "Black".
	target_version_param = black.main.params[2]
	assert target_version_param.name == "target_version"
	target_version_param.help = target_version_param.help.replace("Black", "BlackT")
	# Change the version string by adding a redundant Click `version_option`
	# decorator on `black.main`. Fortunately the added `version_option` takes
	# precedence over the existing one.
	version_string = f"{__version__}, based on black {black.__version__}"
	version_option(version_string)(black.main)
	black.main()


main()
