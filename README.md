[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/blackt.svg?style=for-the-badge&cacheSeconds=28800)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/blackt.svg?style=for-the-badge&cacheSeconds=28800)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/blackt.svg?style=for-the-badge&cacheSeconds=28800)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/blackt.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/blackt.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/blackt.svg?style=for-the-badge&cacheSeconds=28800)](https://pypistats.org/packages/blackt)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi%2Epepy%2Etech%2Fapi%2Fv2%2Fprojects%2Fblackt)](https://pepy.tech/project/blackt)
[![PyPI Version](https://img.shields.io/pypi/v/blackt.svg?style=for-the-badge&cacheSeconds=28800)](https://pypi.org/project/blackt)

<!-- omit in toc -->
# BlackT

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Black (https://github.com/psf/black/) but with tabs

**Note:** you may wish to consider https://github.com/jsh9/cercis

Here are the configuration options to fall back to Blackt's behavior. Put them in
`pyproject.toml`:

```toml
[tool.cercis]
line-length = 88
single-quote = false
use-tabs = true
function-definition-extra-indent = false
other-line-continuation-extra-indent = false
closing-bracket-extra-indent = false
wrap-line-with-long-string = true
collapse-nested-brackets = false
wrap-comments = true
wrap-pragma-comments = true
```

Here is a more opinionated example

```toml
[tool.cercis]
line-length = 120
single-quote = false
use-tabs = true
target-version = ["py38"]
```

- [Using (snippet from upstream)](#using-snippet-from-upstream)
	- [Command line options](#command-line-options)
- [Documentation](#documentation)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Windows - Python.org](#windows---pythonorg)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
	- [Dnf](#dnf)
- [Install Python on MacOS](#install-python-on-macos)
	- [Homebrew](#homebrew)
	- [MacOS - Python.org](#macos---pythonorg)
- [How to run](#how-to-run)
	- [Windows](#windows)
	- [Linux/ MacOS](#linux-macos)
- [Download Project](#download-project)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)

## Using (snippet from upstream)

To get started right away with sensible defaults:

```sh
black {source_file_or_directory}
```

You can run _Black_ as a package if running it as a script doesn't work:

```sh
python -m black {source_file_or_directory}
```

### Command line options

_Black_ doesn't provide many options. You can list them by running `black --help`:

```text
Usage: black [OPTIONS] SRC ...

  The uncompromising code formatter.

Options:
  -c, --code TEXT                 Format the code passed in as a string.
  -l, --line-length INTEGER       How many characters per line to allow.
                                  [default: 100]
  -t, --target-version [py27|py33|py34|py35|py36|py37|py38|py39]
                                  Python versions that should be supported by
                                  Black's output. [default: per-file auto-
                                  detection]
  --pyi                           Format all input files like typing stubs
                                  regardless of file extension (useful when
                                  piping source on standard input).
  --ipynb                         Format all input files like Jupyter
                                  Notebooks regardless of file extension
                                  (useful when piping source on standard
                                  input).
  -S, --skip-string-normalization
                                  Don't normalize string quotes or prefixes.
  -C, --skip-magic-trailing-comma
                                  Don't use trailing commas as a reason to
                                  split lines.
  --check                         Don't write the files back, just return the
                                  status. Return code 0 means nothing would
                                  change. Return code 1 means some files would
                                  be reformatted. Return code 123 means there
                                  was an internal error.
  --diff                          Don't write the files back, just output a
                                  diff for each file on stdout.
  --color / --no-color            Show colored diff. Only applies when
                                  `--diff` is given.
  --fast / --safe                 If --fast given, skip temporary sanity
                                  checks. [default: --safe]
  --required-version TEXT         Require a specific version of Black to be
                                  running (useful for unifying results across
                                  many environments e.g. with a pyproject.toml
                                  file).
  --include TEXT                  A regular expression that matches files and
                                  directories that should be included on
                                  recursive searches. An empty value means all
                                  files are included regardless of the name.
                                  Use forward slashes for directories on all
                                  platforms (Windows, too). Exclusions are
                                  calculated first, inclusions later.
                                  [default: (\.pyi?|\.ipynb)$]
  --exclude TEXT                  A regular expression that matches files and
                                  directories that should be excluded on
                                  recursive searches. An empty value means no
                                  paths are excluded. Use forward slashes for
                                  directories on all platforms (Windows, too).
                                  Exclusions are calculated first, inclusions
                                  later. [default: /(\.direnv|\.eggs|\.git|\.h
                                  g|\.mypy_cache|\.nox|\.tox|\.venv|venv|\.svn
                                  |_build|buck-out|build|dist)/]
  --extend-exclude TEXT           Like --exclude, but adds additional files
                                  and directories on top of the excluded ones.
                                  (Useful if you simply want to add to the
                                  default)
  --force-exclude TEXT            Like --exclude, but files and directories
                                  matching this regex will be excluded even
                                  when they are passed explicitly as
                                  arguments.
  --stdin-filename TEXT           The name of the file when passing it through
                                  stdin. Useful to make sure Black will
                                  respect --force-exclude option on some
                                  editors that rely on using stdin.
  -q, --quiet                     Don't emit non-error messages to stderr.
                                  Errors are still emitted; silence those with
                                  2>/dev/null.
  -v, --verbose                   Also emit messages to stderr about files
                                  that were not changed or were ignored due to
                                  exclusion patterns.
  --version                       Show the version and exit.
  --config FILE                   Read configuration from FILE path.
  -h, --help                      Show this message and exit.
```

_Black_ is a well-behaved Unix-style command-line tool:

- it does nothing if no sources are passed to it;
- it will read from standard input and write to standard output if `-` is used as the
  filename;
- it only outputs messages to users on standard error;
- exits with code 0 unless an internal error occurred (or `--check` was used).

For more info see https://github.com/psf/black/blob/master/README.md

## Documentation

A high-level overview of how the documentation is organized organized will help you know
where to look for certain things:

<!--
- [Tutorials](/documentation/tutorials) take you by the hand through a series of steps to get
  started using the software. Start here if you’re new.
-->
- The [Technical Reference](/documentation/reference) documents APIs and other aspects of the
  machinery. This documentation describes how to use the classes and functions at a lower level
  and assume that you have a good high-level understanding of the software.
<!--
- The [Help](/documentation/help) guide provides a starting point and outlines common issues that you
  may have.
-->

## Install With PIP

```python
pip install blackt
```

Head to https://pypi.org/project/blackt/ for more info

## Language information

### Built for

This program has been written for Python versions 3.8 - 3.11 and has been tested with both 3.8 and
3.11

## Install Python on Windows

### Chocolatey

```powershell
choco install python
```

### Windows - Python.org

To install Python, go to https://www.python.org/downloads/windows/ and download the latest
version.

## Install Python on Linux

### Apt

```bash
sudo apt install python3.x
```

### Dnf

```bash
sudo dnf install python3.x
```

## Install Python on MacOS

### Homebrew

```bash
brew install python@3.x
```

### MacOS - Python.org

To install Python, go to https://www.python.org/downloads/macos/ and download the latest
version.

## How to run

### Windows

- Module
	`py -3.x -m [module]` or `[module]` (if module installs a script)

- File
	`py -3.x [file]` or `./[file]`

### Linux/ MacOS

- Module
	`python3.x -m [module]` or `[module]` (if module installs a script)

- File
	`python3.x [file]` or `./[file]`

## Building

This project uses https://github.com/FHPythonUtils/FHMake to automate most of the building. This
command generates the documentation, updates the requirements.txt and builds the library artefacts

Note the functionality provided by fhmake can be approximated by the following

```sh
handsdown  --cleanup -o documentation/reference
poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --with dev --output requirements_optional.txt
poetry build
```

`fhmake audit` can be run to perform additional checks

## Testing

For testing with the version of python used by poetry use

```sh
poetry run pytest
```

Alternatively use `tox` to run tests over python 3.8 - 3.11

```sh
tox
```

## Download Project

### Clone

#### Using The Command Line

1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2

	```bash
	git clone https://github.com/FHPythonUtils/blackt
	```

More information can be found at
https://help.github.com/en/articles/cloning-a-repository

#### Using GitHub Desktop

1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files

### Licence

MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog

See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct

Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing

Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security

Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support

Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale

The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.
