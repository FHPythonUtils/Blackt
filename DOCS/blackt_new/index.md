# blackt_new

> Auto-generated documentation for [blackt_new](../../blackt_new/__init__.py) module.

- [Blackt](../README.md#blackt-index) / [Modules](../README.md#blackt-modules) / blackt_new
    - [Line](#line)
        - [Line().\_\_str\_\_](#line__str__)
    - [LineGenerator](#linegenerator)
        - [LineGenerator().visit_STRING](#linegeneratorvisit_string)
    - [Mode](#mode)
    - [fix_docstring](#fix_docstring)
    - [format_file_in_place](#format_file_in_place)
    - [is_line_short_enough](#is_line_short_enough)
    - [main](#main)
    - [monkey_patch_black](#monkey_patch_black)
    - [test](#test)
    - Modules
        - [\_\_main\_\_](module.md#__main__)

## Line

[[find in source code]](../../blackt_new/__init__.py#L45)

```python
class Line(black.Line):
```

### Line().\_\_str\_\_

[[find in source code]](../../blackt_new/__init__.py#L46)

```python
def __str__() -> str:
```

Render the line.

## LineGenerator

[[find in source code]](../../blackt_new/__init__.py#L61)

```python
class LineGenerator(black.LineGenerator):
```

### LineGenerator().visit_STRING

[[find in source code]](../../blackt_new/__init__.py#L62)

```python
def visit_STRING(leaf: Leaf) -> Iterator[Line]:
```

## Mode

[[find in source code]](../../blackt_new/__init__.py#L18)

```python
class Mode(Enum):
```

## fix_docstring

[[find in source code]](../../blackt_new/__init__.py#L95)

```python
def fix_docstring(docstring: str, prefix: str) -> str:
```

## format_file_in_place

[[find in source code]](../../blackt_new/__init__.py#L119)

```python
def format_file_in_place(*args, **kws):
```

## is_line_short_enough

[[find in source code]](../../blackt_new/__init__.py#L81)

```python
def is_line_short_enough(
    line: black.Line,
    line_length: int,
    line_str: str = '',
) -> bool:
```

Return True if `line` is no longer than `line_length`.

Uses the provided `line_str` rendering, if any, otherwise computes a new one.

## main

[[find in source code]](../../blackt_new/__init__.py#L134)

```python
def main():
```

## monkey_patch_black

[[find in source code]](../../blackt_new/__init__.py#L38)

```python
def monkey_patch_black(mode: Mode) -> None:
```

#### See also

- [Mode](#mode)

## test

[[find in source code]](../../blackt_new/__init__.py#L126)

```python
def test(
    src: Path,
    fast: bool,
    mode: Mode,
    write_back: WriteBack = WriteBack.NO,
    lock: Any = None,
):
```

#### See also

- [Mode](#mode)
