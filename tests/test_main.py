from pathlib import Path
from tempfile import NamedTemporaryFile

THISDIR = str(Path(__file__).resolve().parent)

from blackt import _doSysExec, convertFile


def aux_testConvertFile(sourceFile: str, destFile: str, find: str, replace: str) -> None:
	with (
		NamedTemporaryFile(mode="w", suffix=".txt", delete=False, newline="") as tmp,\
		Path(sourceFile).open(encoding="utf-8", newline="") as src,\
		Path(destFile).open(encoding="utf-8", newline="") as dst,
	):
		tempFile = Path(tmp.name)
		tempFile.write_text(src.read(), encoding="utf-8")
		convertFile(tempFile, find, replace)
		tempFileContents = tempFile.open(encoding="utf-8").read()
		assert "\r" not in tempFileContents
		assert tempFileContents == dst.read()


def test_convertFile_toTabs() -> None:
	aux_testConvertFile(
		f"{THISDIR}/data/spaces.txt", f"{THISDIR}/data/tabs.txt", find="    ", replace="\t"
	)


def test_convertFile_toSpaces() -> None:
	aux_testConvertFile(
		f"{THISDIR}/data/tabs.txt", f"{THISDIR}/data/spaces.txt", find="\t", replace="    "
	)


def test_shell() -> None:
	assert _doSysExec("black --help")[0] == 0
