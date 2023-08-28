# Blackt

> Auto-generated documentation for [blackt](../../../blackt/__init__.py) module.

Provides the wrapper methods to black. Requires black to be on the system path

- [Blackt](../README.md#blackt-index) / [Modules](../MODULES.md#blackt-modules) / Blackt
    - [convertFile](#convertfile)
    - [convertSpacesToTabs](#convertspacestotabs)
    - [convertTabsToSpaces](#converttabstospaces)
    - [findSourceFiles](#findsourcefiles)
    - [main](#main)
    - [printOutput](#printoutput)
    - [runBlack](#runblack)
    - Modules
        - [Module](module.md#module)

## convertFile

[[find in source code]](../../../blackt/__init__.py#L80)

```python
def convertFile(file: str, find: str, replace: str):
```

Convert spaces to tabs of vice versa

#### Arguments

- `file` *str* - file to modify
- `find` *str* - tabs/ spaces to find
- `replace` *str* - tabs/ spaces to replace

## convertSpacesToTabs

[[find in source code]](../../../blackt/__init__.py#L74)

```python
def convertSpacesToTabs(files: list[str], find: str, replace: str):
```

Convert spaces to tabs

## convertTabsToSpaces

[[find in source code]](../../../blackt/__init__.py#L68)

```python
def convertTabsToSpaces(files: list[str], find: str, replace: str):
```

Convert tabs to spaces

## findSourceFiles

[[find in source code]](../../../blackt/__init__.py#L58)

```python
def findSourceFiles() -> list[str]:
```

Find source files to process

## main

[[find in source code]](../../../blackt/__init__.py#L34)

```python
def main():
```

Main entry point

## printOutput

[[find in source code]](../../../blackt/__init__.py#L102)

```python
def printOutput(out: str):
```

Print the output

## runBlack

[[find in source code]](../../../blackt/__init__.py#L97)

```python
def runBlack(unknown: list[str]) -> tuple[int, str]:
```

Run black with forwarded args
