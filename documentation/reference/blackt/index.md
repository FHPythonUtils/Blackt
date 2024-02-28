# Blackt

[Blackt Index](../README.md#blackt-index) / Blackt

> Auto-generated documentation for [blackt](../../../blackt/__init__.py) module.

- [Blackt](#blackt)
  - [_doSysExec](#_dosysexec)
  - [convertFile](#convertfile)
  - [convertSpacesToTabs](#convertspacestotabs)
  - [convertTabsToSpaces](#converttabstospaces)
  - [findSourceFiles](#findsourcefiles)
  - [main](#main)
  - [printOutput](#printoutput)
  - [runBlack](#runblack)
  - [Modules](#modules)

## _doSysExec

[Show source in __init__.py:117](../../../blackt/__init__.py#L117)

Execute a command and check for errors.

#### Arguments

----
 - `command` *str* - commands as a string
 - `errorAsOut` *bool, optional* - redirect errors to stdout

#### Returns

-------
 - `tuple[int,` *str]* - tuple of return code (int) and stdout (str)

#### Signature

```python
def _doSysExec(command: str, errorAsOut: bool = True) -> tuple[int, str]: ...
```



## convertFile

[Show source in __init__.py:80](../../../blackt/__init__.py#L80)

Convert spaces to tabs or vice versa.

#### Arguments

----
 - `file` *str* - file to modify
 - `find` *str* - tabs/ spaces to find
 - `replace` *str* - tabs/ spaces to replace

#### Signature

```python
def convertFile(file: Path, find: str, replace: str) -> None: ...
```



## convertSpacesToTabs

[Show source in __init__.py:74](../../../blackt/__init__.py#L74)

Convert spaces to tabs.

#### Signature

```python
def convertSpacesToTabs(files: list[Path], find: str, replace: str) -> None: ...
```



## convertTabsToSpaces

[Show source in __init__.py:68](../../../blackt/__init__.py#L68)

Convert tabs to spaces.

#### Signature

```python
def convertTabsToSpaces(files: list[Path], find: str, replace: str) -> None: ...
```



## findSourceFiles

[Show source in __init__.py:58](../../../blackt/__init__.py#L58)

Find source files to process.

#### Signature

```python
def findSourceFiles() -> list[Path]: ...
```



## main

[Show source in __init__.py:34](../../../blackt/__init__.py#L34)

Establish the main entry point.

#### Signature

```python
def main() -> None: ...
```



## printOutput

[Show source in __init__.py:109](../../../blackt/__init__.py#L109)

Print the output.

#### Signature

```python
def printOutput(out: str) -> None: ...
```



## runBlack

[Show source in __init__.py:104](../../../blackt/__init__.py#L104)

Run black with forwarded args.

#### Signature

```python
def runBlack(unknown: list[str]) -> tuple[int, str]: ...
```



## Modules

- [Module](./module.md)