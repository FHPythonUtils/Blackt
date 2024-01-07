# Blackt

[Blackt Index](../README.md#blackt-index) /
Blackt

> Auto-generated documentation for [blackt](../../../blackt/__init__.py) module.

- [Blackt](#blackt)
  - [convertFile](#convertfile)
  - [convertSpacesToTabs](#convertspacestotabs)
  - [convertTabsToSpaces](#converttabstospaces)
  - [findSourceFiles](#findsourcefiles)
  - [main](#main)
  - [printOutput](#printoutput)
  - [runBlack](#runblack)
  - [Modules](#modules)

## convertFile

[Show source in __init__.py:80](../../../blackt/__init__.py#L80)

Convert spaces to tabs of vice versa

#### Arguments

- `file` *str* - file to modify
- `find` *str* - tabs/ spaces to find
- `replace` *str* - tabs/ spaces to replace

#### Signature

```python
def convertFile(file: str, find: str, replace: str): ...
```



## convertSpacesToTabs

[Show source in __init__.py:74](../../../blackt/__init__.py#L74)

Convert spaces to tabs

#### Signature

```python
def convertSpacesToTabs(files: list[str], find: str, replace: str): ...
```



## convertTabsToSpaces

[Show source in __init__.py:68](../../../blackt/__init__.py#L68)

Convert tabs to spaces

#### Signature

```python
def convertTabsToSpaces(files: list[str], find: str, replace: str): ...
```



## findSourceFiles

[Show source in __init__.py:58](../../../blackt/__init__.py#L58)

Find source files to process

#### Signature

```python
def findSourceFiles() -> list[str]: ...
```



## main

[Show source in __init__.py:34](../../../blackt/__init__.py#L34)

Main entry point

#### Signature

```python
def main(): ...
```



## printOutput

[Show source in __init__.py:102](../../../blackt/__init__.py#L102)

Print the output

#### Signature

```python
def printOutput(out: str): ...
```



## runBlack

[Show source in __init__.py:97](../../../blackt/__init__.py#L97)

Run black with forwarded args

#### Signature

```python
def runBlack(unknown: list[str]) -> tuple[int, str]: ...
```



## Modules

- [Module](./module.md)