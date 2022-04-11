from pathlib import Path
from tempfile import NamedTemporaryFile

THISDIR = str(Path(__file__).resolve().parent)

from blackt import _doSysExec, convertFile


def test_convertFile_toTabs():
	with NamedTemporaryFile(suffix=".txt", delete=False) as file:
		Path(file.name).write_text(
			Path(f"{THISDIR}/data/spaces.txt").read_text(encoding="utf-8"), encoding="utf-8"
		)
		convertFile(file.name, find="    ", replace="\t")
		assert Path(file.name).read_text(encoding="utf-8") == Path(
			f"{THISDIR}/data/tabs.txt"
		).read_text(encoding="utf-8")


def test_convertFile_toSpaces():
	with NamedTemporaryFile(suffix=".txt", delete=False) as file:
		Path(file.name).write_text(
			Path(f"{THISDIR}/data/tabs.txt").read_text(encoding="utf-8"), encoding="utf-8"
		)
		convertFile(file.name, find="\t", replace="    ")
		assert Path(file.name).read_text(encoding="utf-8") == Path(
			f"{THISDIR}/data/spaces.txt"
		).read_text(encoding="utf-8")


def test_shell():
	assert _doSysExec("black --help")[0] == 0
