from pathlib import Path
from tempfile import NamedTemporaryFile

THISDIR = str(Path(__file__).resolve().parent)

from blackt import _doSysExec, convertFile  # noqa: E402


def aux_testConvertFile(sourceFile: str, destFile: str, find: str, replace: str):
	with NamedTemporaryFile(mode="w", suffix=".txt", delete=False, newline="") as file:
		src = Path(sourceFile).open(encoding="utf-8", newline="").read()
		Path(file.name).write_text(src, encoding="utf-8", newline="")
		convertFile(file.name, find, replace)
		tempFileContents = Path(file.name).open(encoding="utf-8", newline="").read()
		assert "\r" not in tempFileContents
		assert tempFileContents == Path(destFile).open(encoding="utf-8", newline="").read()


def test_convertFile_toTabs():
	aux_testConvertFile(
		f"{THISDIR}/data/spaces.txt", f"{THISDIR}/data/tabs.txt", find="    ", replace="\t"
	)


def test_convertFile_toSpaces():
	aux_testConvertFile(
		f"{THISDIR}/data/tabs.txt", f"{THISDIR}/data/spaces.txt", find="\t", replace="    "
	)


def test_shell():
	assert _doSysExec("black --help")[0] == 0
