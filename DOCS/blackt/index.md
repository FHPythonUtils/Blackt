# blackt

> Auto-generated documentation for [blackt](../../blackt/__init__.py) module.

- [Blackt](../README.md#blackt-index) / [Modules](../README.md#blackt-modules) / blackt
    - [BaseStringSplitter](#basestringsplitter)
        - [BaseStringSplitter().__get_max_string_length](#basestringsplitter__get_max_string_length)
        - [BaseStringSplitter().__validate](#basestringsplitter__validate)
        - [BaseStringSplitter().do_match](#basestringsplitterdo_match)
        - [BaseStringSplitter().do_splitter_match](#basestringsplitterdo_splitter_match)
    - [BracketMatchError](#bracketmatcherror)
    - [BracketTracker](#brackettracker)
        - [BracketTracker().any_open_brackets](#brackettrackerany_open_brackets)
        - [BracketTracker().delimiter_count_with_priority](#brackettrackerdelimiter_count_with_priority)
        - [BracketTracker().get_open_lsqb](#brackettrackerget_open_lsqb)
        - [BracketTracker().mark](#brackettrackermark)
        - [BracketTracker().max_delimiter_priority](#brackettrackermax_delimiter_priority)
        - [BracketTracker().maybe_decrement_after_for_loop_variable](#brackettrackermaybe_decrement_after_for_loop_variable)
        - [BracketTracker().maybe_decrement_after_lambda_arguments](#brackettrackermaybe_decrement_after_lambda_arguments)
        - [BracketTracker().maybe_increment_for_loop_variable](#brackettrackermaybe_increment_for_loop_variable)
        - [BracketTracker().maybe_increment_lambda_arguments](#brackettrackermaybe_increment_lambda_arguments)
    - [CannotSplit](#cannotsplit)
    - [CannotTransform](#cannottransform)
    - [Changed](#changed)
    - [CustomSplit](#customsplit)
    - [CustomSplitMapMixin](#customsplitmapmixin)
        - [CustomSplitMapMixin().add_custom_splits](#customsplitmapmixinadd_custom_splits)
        - [CustomSplitMapMixin().has_custom_splits](#customsplitmapmixinhas_custom_splits)
        - [CustomSplitMapMixin().pop_custom_splits](#customsplitmapmixinpop_custom_splits)
    - [DebugVisitor](#debugvisitor)
        - [DebugVisitor.show](#debugvisitorshow)
        - [DebugVisitor().visit_default](#debugvisitorvisit_default)
    - [EmptyLineTracker](#emptylinetracker)
        - [EmptyLineTracker().maybe_empty_lines](#emptylinetrackermaybe_empty_lines)
    - [Err](#err)
        - [Err().err](#errerr)
    - [Feature](#feature)
    - [InvalidInput](#invalidinput)
    - [Line](#line)
        - [Line().\_\_bool\_\_](#line__bool__)
        - [Line().\_\_str\_\_](#line__str__)
        - [Line().append](#lineappend)
        - [Line().append_comment](#lineappend_comment)
        - [Line().append_safe](#lineappend_safe)
        - [Line().clone](#lineclone)
        - [Line().comments_after](#linecomments_after)
        - [Line().contains_multiline_strings](#linecontains_multiline_strings)
        - [Line().contains_standalone_comments](#linecontains_standalone_comments)
        - [Line().contains_uncollapsable_type_comments](#linecontains_uncollapsable_type_comments)
        - [Line().contains_unsplittable_type_ignore](#linecontains_unsplittable_type_ignore)
        - [Line().has_magic_trailing_comma](#linehas_magic_trailing_comma)
        - [Line().is_class](#lineis_class)
        - [Line().is_class_paren_empty](#lineis_class_paren_empty)
        - [Line().is_comment](#lineis_comment)
        - [Line().is_complex_subscript](#lineis_complex_subscript)
        - [Line().is_decorator](#lineis_decorator)
        - [Line().is_def](#lineis_def)
        - [Line().is_import](#lineis_import)
        - [Line().is_stub_class](#lineis_stub_class)
        - [Line().is_triple_quoted_string](#lineis_triple_quoted_string)
        - [Line().remove_trailing_comma](#lineremove_trailing_comma)
    - [LineGenerator](#linegenerator)
        - [LineGenerator().\_\_post\_init\_\_](#linegenerator__post_init__)
        - [LineGenerator().line](#linegeneratorline)
        - [LineGenerator().visit_DEDENT](#linegeneratorvisit_dedent)
        - [LineGenerator().visit_ENDMARKER](#linegeneratorvisit_endmarker)
        - [LineGenerator().visit_INDENT](#linegeneratorvisit_indent)
        - [LineGenerator().visit_SEMI](#linegeneratorvisit_semi)
        - [LineGenerator().visit_STANDALONE_COMMENT](#linegeneratorvisit_standalone_comment)
        - [LineGenerator().visit_STRING](#linegeneratorvisit_string)
        - [LineGenerator().visit_async_stmt](#linegeneratorvisit_async_stmt)
        - [LineGenerator().visit_decorators](#linegeneratorvisit_decorators)
        - [LineGenerator().visit_default](#linegeneratorvisit_default)
        - [LineGenerator().visit_factor](#linegeneratorvisit_factor)
        - [LineGenerator().visit_simple_stmt](#linegeneratorvisit_simple_stmt)
        - [LineGenerator().visit_stmt](#linegeneratorvisit_stmt)
        - [LineGenerator().visit_suite](#linegeneratorvisit_suite)
    - [Mode](#mode)
        - [Mode().get_cache_key](#modeget_cache_key)
    - [NothingChanged](#nothingchanged)
    - [Ok](#ok)
        - [Ok().ok](#okok)
    - [ProtoComment](#protocomment)
    - [Report](#report)
        - [Report().\_\_str\_\_](#report__str__)
        - [Report().done](#reportdone)
        - [Report().failed](#reportfailed)
        - [Report().path_ignored](#reportpath_ignored)
        - [Report().return_code](#reportreturn_code)
    - [StringMerger](#stringmerger)
        - [StringMerger().__merge_string_group](#stringmerger__merge_string_group)
        - [StringMerger.__remove_backslash_line_continuation_chars](#stringmerger__remove_backslash_line_continuation_chars)
        - [StringMerger.__validate_msg](#stringmerger__validate_msg)
        - [StringMerger().do_match](#stringmergerdo_match)
        - [StringMerger().do_transform](#stringmergerdo_transform)
    - [StringParenStripper](#stringparenstripper)
        - [StringParenStripper().do_match](#stringparenstripperdo_match)
        - [StringParenStripper().do_transform](#stringparenstripperdo_transform)
    - [StringParenWrapper](#stringparenwrapper)
        - [StringParenWrapper().do_splitter_match](#stringparenwrapperdo_splitter_match)
        - [StringParenWrapper().do_transform](#stringparenwrapperdo_transform)
    - [StringParser](#stringparser)
        - [StringParser().parse](#stringparserparse)
    - [StringSplitter](#stringsplitter)
        - [StringSplitter().__get_break_idx](#stringsplitter__get_break_idx)
        - [StringSplitter().__normalize_f_string](#stringsplitter__normalize_f_string)
        - [StringSplitter().do_splitter_match](#stringsplitterdo_splitter_match)
        - [StringSplitter().do_transform](#stringsplitterdo_transform)
    - [StringTransformer](#stringtransformer)
        - [StringTransformer().\_\_call\_\_](#stringtransformer__call__)
        - [StringTransformer().do_match](#stringtransformerdo_match)
        - [StringTransformer().do_transform](#stringtransformerdo_transform)
    - [TargetVersion](#targetversion)
        - [TargetVersion().is_python2](#targetversionis_python2)
    - [Visitor](#visitor)
        - [Visitor().visit](#visitorvisit)
        - [Visitor().visit_default](#visitorvisit_default)
    - [WriteBack](#writeback)
        - [WriteBack.from_configuration](#writebackfrom_configuration)
    - [TErr](#terr)
    - [append_leaves](#append_leaves)
    - [assert_equivalent](#assert_equivalent)
    - [assert_is_leaf_string](#assert_is_leaf_string)
    - [assert_stable](#assert_stable)
    - [bracket_split_build_line](#bracket_split_build_line)
    - [bracket_split_succeeded_or_raise](#bracket_split_succeeded_or_raise)
    - [can_be_split](#can_be_split)
    - [can_omit_invisible_parens](#can_omit_invisible_parens)
    - [cancel](#cancel)
    - [child_towards](#child_towards)
    - [color_diff](#color_diff)
    - [container_of](#container_of)
    - [contains_fmt_on_at_column](#contains_fmt_on_at_column)
    - [contains_pragma_comment](#contains_pragma_comment)
    - [convert_one_fmt_off_pair](#convert_one_fmt_off_pair)
    - [decode_bytes](#decode_bytes)
    - [delimiter_split](#delimiter_split)
    - [detect_target_versions](#detect_target_versions)
    - [diff](#diff)
    - [dont_increase_indentation](#dont_increase_indentation)
    - [dump_to_file](#dump_to_file)
    - [ensure_visible](#ensure_visible)
    - [enumerate_reversed](#enumerate_reversed)
    - [enumerate_with_length](#enumerate_with_length)
    - [filter_cached](#filter_cached)
    - [find_project_root](#find_project_root)
    - [find_pyproject_toml](#find_pyproject_toml)
    - [find_user_pyproject_toml](#find_user_pyproject_toml)
    - [first_child_is_arith](#first_child_is_arith)
    - [first_leaf_column](#first_leaf_column)
    - [fix_docstring](#fix_docstring)
    - [format_file_contents](#format_file_contents)
    - [format_file_in_place](#format_file_in_place)
    - [format_float_or_int_string](#format_float_or_int_string)
    - [format_hex](#format_hex)
    - [format_long_or_complex_number](#format_long_or_complex_number)
    - [format_scientific_notation](#format_scientific_notation)
    - [format_stdin_to_stdout](#format_stdin_to_stdout)
    - [format_str](#format_str)
    - [gen_python_files](#gen_python_files)
    - [generate_comments](#generate_comments)
    - [generate_ignored_nodes](#generate_ignored_nodes)
    - [generate_trailers_to_omit](#generate_trailers_to_omit)
    - [get_cache_file](#get_cache_file)
    - [get_cache_info](#get_cache_info)
    - [get_features_used](#get_features_used)
    - [get_future_imports](#get_future_imports)
    - [get_gitignore](#get_gitignore)
    - [get_grammars](#get_grammars)
    - [get_sources](#get_sources)
    - [get_string_prefix](#get_string_prefix)
    - [has_triple_quotes](#has_triple_quotes)
    - [insert_str_child_factory](#insert_str_child_factory)
    - [is_atom_with_invisible_parens](#is_atom_with_invisible_parens)
    - [is_docstring](#is_docstring)
    - [is_empty_lpar](#is_empty_lpar)
    - [is_empty_par](#is_empty_par)
    - [is_empty_rpar](#is_empty_rpar)
    - [is_empty_tuple](#is_empty_tuple)
    - [is_fmt_on](#is_fmt_on)
    - [is_import](#is_import)
    - [is_line_short_enough](#is_line_short_enough)
    - [is_multiline_string](#is_multiline_string)
    - [is_one_tuple](#is_one_tuple)
    - [is_one_tuple_between](#is_one_tuple_between)
    - [is_simple_decorator_expression](#is_simple_decorator_expression)
    - [is_simple_decorator_trailer](#is_simple_decorator_trailer)
    - [is_split_after_delimiter](#is_split_after_delimiter)
    - [is_split_before_delimiter](#is_split_before_delimiter)
    - [is_stub_body](#is_stub_body)
    - [is_stub_suite](#is_stub_suite)
    - [is_type_comment](#is_type_comment)
    - [is_valid_index_factory](#is_valid_index_factory)
    - [is_vararg](#is_vararg)
    - [is_walrus_assignment](#is_walrus_assignment)
    - [is_yield](#is_yield)
    - [last_two_except](#last_two_except)
    - [left_hand_split](#left_hand_split)
    - [lib2to3_parse](#lib2to3_parse)
    - [lib2to3_unparse](#lib2to3_unparse)
    - [line_to_string](#line_to_string)
    - [lines_with_leading_tabs_expanded](#lines_with_leading_tabs_expanded)
    - [list_comments](#list_comments)
    - [main](#main)
    - [make_comment](#make_comment)
    - [max_delimiter_priority_in_atom](#max_delimiter_priority_in_atom)
    - [maybe_make_parens_invisible_in_atom](#maybe_make_parens_invisible_in_atom)
    - [normalize_fmt_off](#normalize_fmt_off)
    - [normalize_invisible_parens](#normalize_invisible_parens)
    - [normalize_numeric_literal](#normalize_numeric_literal)
    - [normalize_path_maybe_ignore](#normalize_path_maybe_ignore)
    - [normalize_prefix](#normalize_prefix)
    - [normalize_string_prefix](#normalize_string_prefix)
    - [normalize_string_quotes](#normalize_string_quotes)
    - [nullcontext](#nullcontext)
    - [parent_type](#parent_type)
    - [parse_ast](#parse_ast)
    - [parse_pyproject_toml](#parse_pyproject_toml)
    - [patch_click](#patch_click)
    - [patched_main](#patched_main)
    - [path_empty](#path_empty)
    - [path_is_excluded](#path_is_excluded)
    - [preceding_leaf](#preceding_leaf)
    - [prev_siblings_are](#prev_siblings_are)
    - [re_compile_maybe_verbose](#re_compile_maybe_verbose)
    - [read_cache](#read_cache)
    - [read_pyproject_toml](#read_pyproject_toml)
    - [reformat_many](#reformat_many)
    - [reformat_one](#reformat_one)
    - [replace_child](#replace_child)
    - [right_hand_split](#right_hand_split)
    - [run_transformer](#run_transformer)
    - [schedule_formatting](#schedule_formatting)
    - [should_split_line](#should_split_line)
    - [shutdown](#shutdown)
    - [standalone_comment_split](#standalone_comment_split)
    - [sub_twice](#sub_twice)
    - [supports_feature](#supports_feature)
    - [target_version_option_callback](#target_version_option_callback)
    - [transform_line](#transform_line)
    - [unwrap_singleton_parenthesis](#unwrap_singleton_parenthesis)
    - [validate_regex](#validate_regex)
    - [whitespace](#whitespace)
    - [wrap_in_parentheses](#wrap_in_parentheses)
    - [wrap_stream_for_windows](#wrap_stream_for_windows)
    - [write_cache](#write_cache)
    - Modules
        - [\_\_main\_\_](module.md#__main__)

#### Attributes

- `FileContent` - types: `str`
- `Result` - The 'Result' return type is used to implement an error-handling model heavily
  influenced by that used by the Rust programming language
  (see https://doc.rust-lang.org/book/ch09-00-error-handling.html).: `Union[(Ok[T], Err[E])]`
- `FileMode` - Legacy name, left for integrations.: `Mode`

## BaseStringSplitter

[[find in source code]](../../blackt/__init__.py#L3464)

```python
class BaseStringSplitter(StringTransformer):
```

Abstract class for StringTransformers which transform a Line's strings by splitting
them or placing them on their own lines where necessary to avoid going over
the configured line length.

Requirements:
 * The target string value is responsible for the line going over the
 line length limit. It follows that after all of black's other line
 split methods have been exhausted, this line (or one of the resulting
 lines after all line splits are performed) would still be over the
 line_length limit unless we split this string.
  AND
 * The target string is NOT a "pointless" string (i.e. a string that has
 no parent or siblings).
  AND
 * The target string is not followed by an inline comment that appears
 to be a pragma.
  AND
 * The target string is not a multiline (i.e. triple-quote) string.

#### See also

- [StringTransformer](#stringtransformer)

### BaseStringSplitter().__get_max_string_length

[[find in source code]](../../blackt/__init__.py#L3552)

```python
def __get_max_string_length(line: Line, string_idx: int) -> int:
```

Calculates the max string length used when attempting to determine
whether or not the target string is responsible for causing the line to
go over the line length limit.

WARNING: This method is tightly coupled to both StringSplitter and
(especially) StringParenWrapper. There is probably a better way to
accomplish what is being done here.

#### Returns

- `max_string_length` - such that `line.leaves[string_idx].value >
max_string_length` implies that the target string IS responsible
for causing this line to exceed the line length limit.

#### See also

- [Line](#line)

### BaseStringSplitter().__validate

[[find in source code]](../../blackt/__init__.py#L3509)

```python
def __validate(line: Line, string_idx: int) -> TResult[None]:
```

Checks that @line meets all of the requirements listed in this classes'
docstring. Refer to `help(BaseStringSplitter)` for a detailed
description of those requirements.

#### Returns

* Ok(None), if ALL of the requirements are met.
 OR
* Err(CannotTransform), if ANY of the requirements are NOT met.

#### See also

- [Line](#line)

### BaseStringSplitter().do_match

[[find in source code]](../../blackt/__init__.py#L3497)

```python
def do_match(line: Line) -> TMatchResult:
```

#### See also

- [Line](#line)
- [TMatchResult](#tmatchresult)

### BaseStringSplitter().do_splitter_match

[[find in source code]](../../blackt/__init__.py#L3486)

```python
@abstractmethod
def do_splitter_match(line: Line) -> TMatchResult:
```

BaseStringSplitter asks its clients to override this method instead of
`StringTransformer.do_match(...)`.

Follows the same protocol as `StringTransformer.do_match(...)`.

Refer to `help(StringTransformer.do_match)` for more information.

#### See also

- [Line](#line)
- [TMatchResult](#tmatchresult)

## BracketMatchError

[[find in source code]](../../blackt/__init__.py#L113)

```python
class BracketMatchError(KeyError):
```

Raised when an opening bracket is unable to be matched to a closing bracket.

## BracketTracker

[[find in source code]](../../blackt/__init__.py#L1337)

```python
dataclass
class BracketTracker():
```

Keeps track of brackets on a line.

### BracketTracker().any_open_brackets

[[find in source code]](../../blackt/__init__.py#L1398)

```python
def any_open_brackets() -> bool:
```

Return True if there is an yet unmatched open bracket on the line.

### BracketTracker().delimiter_count_with_priority

[[find in source code]](../../blackt/__init__.py#L1410)

```python
def delimiter_count_with_priority(priority: Priority = 0) -> int:
```

Return the number of delimiters with the given `priority`.

If no `priority` is passed, defaults to max priority on the line.

#### See also

- [Priority](#priority)

### BracketTracker().get_open_lsqb

[[find in source code]](../../blackt/__init__.py#L1474)

```python
def get_open_lsqb() -> Optional[Leaf]:
```

Return the most recent opening square bracket (if any).

### BracketTracker().mark

[[find in source code]](../../blackt/__init__.py#L1348)

```python
def mark(leaf: Leaf) -> None:
```

Mark `leaf` with bracket-related metadata. Keep track of delimiters.

All leaves receive an int `bracket_depth` field that stores how deep
within brackets a given leaf is. 0 means there are no enclosing brackets
that started on this line.

If a leaf is itself a closing bracket, it receives an `opening_bracket`
field that it forms a pair with. This is a one-directional link to
avoid reference cycles.

If a leaf is a delimiter (a token on which Black can split the line if
needed) and it's on depth 0, its `id()` is stored in the tracker's
`delimiters` field.

### BracketTracker().max_delimiter_priority

[[find in source code]](../../blackt/__init__.py#L1402)

```python
def max_delimiter_priority(exclude: Iterable[LeafID] = ()) -> Priority:
```

Return the highest priority of a delimiter found on the line.

Values are consistent with what `is_split_*_delimiter()` return.
Raises ValueError on no delimiters.

#### See also

- [Priority](#priority)

### BracketTracker().maybe_decrement_after_for_loop_variable

[[find in source code]](../../blackt/__init__.py#L1434)

```python
def maybe_decrement_after_for_loop_variable(leaf: Leaf) -> bool:
```

See [BracketTracker().maybe_increment_for_loop_variable](#brackettrackermaybe_increment_for_loop_variable) above for explanation.

### BracketTracker().maybe_decrement_after_lambda_arguments

[[find in source code]](../../blackt/__init__.py#L1461)

```python
def maybe_decrement_after_lambda_arguments(leaf: Leaf) -> bool:
```

See [BracketTracker().maybe_increment_lambda_arguments](#brackettrackermaybe_increment_lambda_arguments) above for explanation.

### BracketTracker().maybe_increment_for_loop_variable

[[find in source code]](../../blackt/__init__.py#L1421)

```python
def maybe_increment_for_loop_variable(leaf: Leaf) -> bool:
```

In a for loop, or comprehension, the variables are often unpacks.

To avoid splitting on the comma in this situation, increase the depth of
tokens between `for` and `in`.

### BracketTracker().maybe_increment_lambda_arguments

[[find in source code]](../../blackt/__init__.py#L1448)

```python
def maybe_increment_lambda_arguments(leaf: Leaf) -> bool:
```

In a lambda expression, there might be more than one argument.

To avoid splitting on the comma in this situation, increase the depth of
tokens between `lambda` and `:`.

## CannotSplit

[[find in source code]](../../blackt/__init__.py#L105)

```python
class CannotSplit(CannotTransform):
```

A readable split that fits the allotted line length is impossible.

#### See also

- [CannotTransform](#cannottransform)

## CannotTransform

[[find in source code]](../../blackt/__init__.py#L101)

```python
class CannotTransform(Exception):
```

Base class for errors raised by Transformers.

## Changed

[[find in source code]](../../blackt/__init__.py#L165)

```python
class Changed(Enum):
```

## CustomSplit

[[find in source code]](../../blackt/__init__.py#L2906)

```python
dataclass
class CustomSplit():
```

A custom (i.e. manual) string split.

A single CustomSplit instance represents a single substring.

#### Examples

Consider the following string:

```
"Hi there friend."
" This is a custom"
f" string {split}."
```

This string will correspond to the following three CustomSplit instances:

```
CustomSplit(False, 16)
CustomSplit(False, 17)
CustomSplit(True, 16)
```

## CustomSplitMapMixin

[[find in source code]](../../blackt/__init__.py#L2931)

```python
class CustomSplitMapMixin():
```

This mixin class is used to map merged strings to a sequence of
CustomSplits, which will then be used to re-split the strings iff none of
the resultant substrings go over the configured max line length.

### CustomSplitMapMixin().add_custom_splits

[[find in source code]](../../blackt/__init__.py#L2950)

```python
def add_custom_splits(
    string: str,
    custom_splits: Iterable[CustomSplit],
) -> None:
```

Custom Split Map Setter Method

Side Effects:
 Adds a mapping from @string to the custom splits @custom_splits.

### CustomSplitMapMixin().has_custom_splits

[[find in source code]](../../blackt/__init__.py#L2981)

```python
def has_custom_splits(string: str) -> bool:
```

#### Returns

True iff @string is associated with a set of custom splits.

### CustomSplitMapMixin().pop_custom_splits

[[find in source code]](../../blackt/__init__.py#L2961)

```python
def pop_custom_splits(string: str) -> List[CustomSplit]:
```

Custom Split Map Getter Method

#### Returns

* A list of the custom splits that are mapped to @string, if any
exist.
 OR
* [], otherwise.

Side Effects:
 Deletes the mapping between @string and its associated custom
 splits (which are returned to the caller).

## DebugVisitor

[[find in source code]](../../blackt/__init__.py#L1189)

```python
dataclass
class DebugVisitor(Visitor[T]):
```

### DebugVisitor.show

[[find in source code]](../../blackt/__init__.py#L1212)

```python
@classmethod
def show(code: Union[(str, Leaf, Node)]) -> None:
```

Pretty-print the lib2to3 AST of a given string of `code`.

Convenience method for debugging.

### DebugVisitor().visit_default

[[find in source code]](../../blackt/__init__.py#L1192)

```python
def visit_default(node: LN) -> Iterator[T]:
```

#### See also

- [LN](#ln)

## EmptyLineTracker

[[find in source code]](../../blackt/__init__.py#L1828)

```python
dataclass
class EmptyLineTracker():
```

Provides a stateful method that returns the number of potential extra
empty lines needed before and after the currently processed line.

Note: this tracker works on lines that haven't been split yet.  It assumes
the prefix of the first leaf consists of optional newlines.  Those newlines
are consumed by `maybe_empty_lines()` and included in the computation.

### EmptyLineTracker().maybe_empty_lines

[[find in source code]](../../blackt/__init__.py#L1842)

```python
def maybe_empty_lines(current_line: Line) -> Tuple[(int, int)]:
```

Return the number of extra empty lines before and after the `current_line`.

This is for separating `def`, `async def` and `class` with extra empty
lines (two on module-level).

#### See also

- [Line](#line)

## Err

[[find in source code]](../../blackt/__init__.py#L129)

```python
class Err(Generic[E]):
    def __init__(e: E) -> None:
```

#### See also

- [E](#e)

### Err().err

[[find in source code]](../../blackt/__init__.py#L133)

```python
def err() -> E:
```

#### See also

- [E](#e)

## Feature

[[find in source code]](../../blackt/__init__.py#L185)

```python
class Feature(Enum):
```

#### Attributes

- `UNICODE_LITERALS` - All string literals are unicode: `1`
- `ASYNC_IDENTIFIERS` - The following two feature-flags are mutually exclusive, and exactly one should be
  set for every version of python.: `6`

## InvalidInput

[[find in source code]](../../blackt/__init__.py#L109)

```python
class InvalidInput(ValueError):
```

Raised when input source code fails all parse attempts.

## Line

[[find in source code]](../../blackt/__init__.py#L1480)

```python
dataclass
class Line():
```

Holds leaves and comments. Can be printed with `str(line)`.

### Line().\_\_bool\_\_

[[find in source code]](../../blackt/__init__.py#L1822)

```python
def __bool__() -> bool:
```

Return True if the line has leaves or comments.

### Line().\_\_str\_\_

[[find in source code]](../../blackt/__init__.py#L1806)

```python
def __str__() -> str:
```

Render the line.

### Line().append

[[find in source code]](../../blackt/__init__.py#L1493)

```python
def append(leaf: Leaf, preformatted: bool = False) -> None:
```

Add a new `leaf` to the end of the line.

Unless `preformatted` is True, the `leaf` will receive a new consistent
whitespace prefix and metadata applied by :class:[BracketTracker](#brackettracker).
Trailing commas are maybe removed, unpacked for loop variables are
demoted from being delimiters.

Inline comments are put aside.

### Line().append_comment

[[find in source code]](../../blackt/__init__.py#L1730)

```python
def append_comment(comment: Leaf) -> bool:
```

Add an inline or standalone comment to the line.

### Line().append_safe

[[find in source code]](../../blackt/__init__.py#L1525)

```python
def append_safe(leaf: Leaf, preformatted: bool = False) -> None:
```

Like :func:`append()` but disallow invalid standalone comment structure.

Raises ValueError when any `leaf` is appended after a standalone comment
or when a standalone comment is not the first leaf on the line.

### Line().clone

[[find in source code]](../../blackt/__init__.py#L1797)

```python
def clone() -> 'Line':
```

### Line().comments_after

[[find in source code]](../../blackt/__init__.py#L1767)

```python
def comments_after(leaf: Leaf) -> List[Leaf]:
```

Generate comments that should appear directly after `leaf`.

### Line().contains_multiline_strings

[[find in source code]](../../blackt/__init__.py#L1694)

```python
def contains_multiline_strings() -> bool:
```

### Line().contains_standalone_comments

[[find in source code]](../../blackt/__init__.py#L1617)

```python
def contains_standalone_comments(depth_limit: int = sys.maxsize) -> bool:
```

If so, needs to be split before emitting.

### Line().contains_uncollapsable_type_comments

[[find in source code]](../../blackt/__init__.py#L1625)

```python
def contains_uncollapsable_type_comments() -> bool:
```

### Line().contains_unsplittable_type_ignore

[[find in source code]](../../blackt/__init__.py#L1661)

```python
def contains_unsplittable_type_ignore() -> bool:
```

### Line().has_magic_trailing_comma

[[find in source code]](../../blackt/__init__.py#L1697)

```python
def has_magic_trailing_comma(
    closing: Leaf,
    ensure_removable: bool = False,
) -> bool:
```

Return True if we have a magic trailing comma, that is when:
- there's a trailing comma here
- it's not a one-tuple
Additionally, if ensure_removable:
- it's not from square bracket indexing

### Line().is_class

[[find in source code]](../../blackt/__init__.py#L1557)

```python
@property
def is_class() -> bool:
```

Is this line a class definition?

### Line().is_class_paren_empty

[[find in source code]](../../blackt/__init__.py#L1592)

```python
@property
def is_class_paren_empty() -> bool:
```

Is this a class with no base classes but using parentheses?

Those are unnecessary and should be removed.

### Line().is_comment

[[find in source code]](../../blackt/__init__.py#L1542)

```python
@property
def is_comment() -> bool:
```

Is this line a standalone comment?

### Line().is_complex_subscript

[[find in source code]](../../blackt/__init__.py#L1779)

```python
def is_complex_subscript(leaf: Leaf) -> bool:
```

Return True iff `leaf` is part of a slice with non-trivial exprs.

### Line().is_decorator

[[find in source code]](../../blackt/__init__.py#L1547)

```python
@property
def is_decorator() -> bool:
```

Is this line a decorator?

### Line().is_def

[[find in source code]](../../blackt/__init__.py#L1573)

```python
@property
def is_def() -> bool:
```

Is this a function definition? (Also returns True for async defs.)

### Line().is_import

[[find in source code]](../../blackt/__init__.py#L1552)

```python
@property
def is_import() -> bool:
```

Is this an import line?

### Line().is_stub_class

[[find in source code]](../../blackt/__init__.py#L1566)

```python
@property
def is_stub_class() -> bool:
```

Is this line a class definition with a body consisting only of "..."?

### Line().is_triple_quoted_string

[[find in source code]](../../blackt/__init__.py#L1608)

```python
@property
def is_triple_quoted_string() -> bool:
```

Is the line a triple quoted string?

### Line().remove_trailing_comma

[[find in source code]](../../blackt/__init__.py#L1771)

```python
def remove_trailing_comma() -> None:
```

Remove the trailing comma and moves the comments attached to it.

## LineGenerator

[[find in source code]](../../blackt/__init__.py#L1952)

```python
dataclass
class LineGenerator(Visitor[Line]):
```

Generates reformatted Line objects.  Empty lines are not emitted.

Note: destroys the tree it's visiting by mutating prefixes of its leaves
in ways that will no longer stringify to valid Python code on the tree.

### LineGenerator().\_\_post\_init\_\_

[[find in source code]](../../blackt/__init__.py#L2149)

```python
def __post_init__() -> None:
```

You are in a twisty little maze of passages.

### LineGenerator().line

[[find in source code]](../../blackt/__init__.py#L1963)

```python
def line(indent: int = 0) -> Iterator[Line]:
```

Generate a line.

If the line is empty, only emit if it makes sense.
If the line is too long, split it first and then generate.

If any lines were generated, set up a new current_line.

### LineGenerator().visit_DEDENT

[[find in source code]](../../blackt/__init__.py#L2015)

```python
def visit_DEDENT(node: Leaf) -> Iterator[Line]:
```

Decrease indentation level, maybe yield a line.

### LineGenerator().visit_ENDMARKER

[[find in source code]](../../blackt/__init__.py#L2104)

```python
def visit_ENDMARKER(leaf: Leaf) -> Iterator[Line]:
```

End of file. Process outstanding comments and end with a newline.

### LineGenerator().visit_INDENT

[[find in source code]](../../blackt/__init__.py#L2009)

```python
def visit_INDENT(node: Leaf) -> Iterator[Line]:
```

Increase indentation level, maybe yield a line.

### LineGenerator().visit_SEMI

[[find in source code]](../../blackt/__init__.py#L2100)

```python
def visit_SEMI(leaf: Leaf) -> Iterator[Line]:
```

Remove a semicolon and put the other statement on a separate line.

### LineGenerator().visit_STANDALONE_COMMENT

[[find in source code]](../../blackt/__init__.py#L2109)

```python
def visit_STANDALONE_COMMENT(leaf: Leaf) -> Iterator[Line]:
```

### LineGenerator().visit_STRING

[[find in source code]](../../blackt/__init__.py#L2131)

```python
def visit_STRING(leaf: Leaf) -> Iterator[Line]:
```

### LineGenerator().visit_async_stmt

[[find in source code]](../../blackt/__init__.py#L2079)

```python
def visit_async_stmt(node: Node) -> Iterator[Line]:
```

Visit `async def`, `async for`, `async with`.

### LineGenerator().visit_decorators

[[find in source code]](../../blackt/__init__.py#L2094)

```python
def visit_decorators(node: Node) -> Iterator[Line]:
```

Visit decorators.

### LineGenerator().visit_default

[[find in source code]](../../blackt/__init__.py#L1979)

```python
def visit_default(node: LN) -> Iterator[Line]:
```

Default `visit_*()` implementation. Recurses to children of `node`.

#### See also

- [LN](#ln)

### LineGenerator().visit_factor

[[find in source code]](../../blackt/__init__.py#L2114)

```python
def visit_factor(node: Node) -> Iterator[Line]:
```

Force parentheses between a unary op and a binary power:

-2 ** 8 -> -(2 ** 8)

### LineGenerator().visit_simple_stmt

[[find in source code]](../../blackt/__init__.py#L2057)

```python
def visit_simple_stmt(node: Node) -> Iterator[Line]:
```

Visit a statement without nested statements.

### LineGenerator().visit_stmt

[[find in source code]](../../blackt/__init__.py#L2029)

```python
def visit_stmt(
    node: Node,
    keywords: Set[str],
    parens: Set[str],
) -> Iterator[Line]:
```

Visit a statement.

This implementation is shared for `if`, `while`, `for`, `try`, `except`,
`def`, `with`, `class`, `assert` and assignments.

The relevant Python language `keywords` for a given statement will be
NAME leaves within it. This methods puts those on a separate line.

`parens` holds a set of string leaf values immediately after which
invisible parens should be put.

### LineGenerator().visit_suite

[[find in source code]](../../blackt/__init__.py#L2050)

```python
def visit_suite(node: Node) -> Iterator[Line]:
```

Visit a suite.

## Mode

[[find in source code]](../../blackt/__init__.py#L252)

```python
dataclass
class Mode():
```

### Mode().get_cache_key

[[find in source code]](../../blackt/__init__.py#L260)

```python
def get_cache_key() -> str:
```

## NothingChanged

[[find in source code]](../../blackt/__init__.py#L97)

```python
class NothingChanged(UserWarning):
```

Raised when reformatted code is the same as source.

## Ok

[[find in source code]](../../blackt/__init__.py#L121)

```python
class Ok(Generic[T]):
    def __init__(value: T) -> None:
```

#### See also

- [T](#t)

### Ok().ok

[[find in source code]](../../blackt/__init__.py#L125)

```python
def ok() -> T:
```

#### See also

- [T](#t)

## ProtoComment

[[find in source code]](../../blackt/__init__.py#L2624)

```python
dataclass
class ProtoComment():
```

Describes a piece of syntax that is a comment.

It's not a class `blib2to3.pytree.Leaf` so that:

* it can be cached (`Leaf` objects should not be reused more than once as
  they store their lineno, column, prefix, and parent information);
* `newlines` and `consumed` fields are kept separate from the `value`. This
  simplifies handling of special marker comments like ``# fmt: off/on``.

## Report

[[find in source code]](../../blackt/__init__.py#L6252)

```python
dataclass
class Report():
```

Provides a reformatting counter. Can be rendered with `str(report)`.

### Report().\_\_str\_\_

[[find in source code]](../../blackt/__init__.py#L6307)

```python
def __str__() -> str:
```

Render a color report of the current state.

Use `click.unstyle` to remove colors.

### Report().done

[[find in source code]](../../blackt/__init__.py#L6263)

```python
def done(src: Path, changed: Changed) -> None:
```

Increment the counter for successful reformatting. Write out a message.

#### See also

- [Changed](#changed)

### Report().failed

[[find in source code]](../../blackt/__init__.py#L6279)

```python
def failed(src: Path, message: str) -> None:
```

Increment the counter for failed reformatting. Write out a message.

### Report().path_ignored

[[find in source code]](../../blackt/__init__.py#L6284)

```python
def path_ignored(path: Path, message: str) -> None:
```

### Report().return_code

[[find in source code]](../../blackt/__init__.py#L6288)

```python
@property
def return_code() -> int:
```

Return the exit code that the app should use.

This considers the current state of changed files and failures:
- if there were any failures, return 123;
- if any files were changed and --check is being used, return 1;
- otherwise return 0.

## StringMerger

[[find in source code]](../../blackt/__init__.py#L2990)

```python
class StringMerger(CustomSplitMapMixin, StringTransformer):
```

StringTransformer that merges strings together.

Requirements:
 (A) The line contains adjacent strings such that ALL of the validation checks
 listed in StringMerger.__validate_msg(...)'s docstring pass.
  OR
 (B) The line contains a string which uses line continuation backslashes.

Transformations:
 Depending on which of the two requirements above where met, either:

(A) The string group associated with the target string is merged.
 OR
(B) All line-continuation backslashes are removed from the target string.

Collaborations:
 StringMerger provides custom split information to StringSplitter.

#### See also

- [CustomSplitMapMixin](#customsplitmapmixin)
- [StringTransformer](#stringtransformer)

### StringMerger().__merge_string_group

[[find in source code]](../../blackt/__init__.py#L3091)

```python
def __merge_string_group(line: Line, string_idx: int) -> TResult[Line]:
```

Merges string group (i.e. set of adjacent strings) where the first
string in the group is `line.leaves[string_idx]`.

#### Returns

Ok(new_line), if ALL of the validation checks found in
__validate_msg(...) pass.
 OR
Err(CannotTransform), otherwise.

#### See also

- [Line](#line)

### StringMerger.__remove_backslash_line_continuation_chars

[[find in source code]](../../blackt/__init__.py#L3055)

```python
@staticmethod
def __remove_backslash_line_continuation_chars(
    line: Line,
    string_idx: int,
) -> TResult[Line]:
```

Merge strings that were split across multiple lines using
line-continuation backslashes.

#### Returns

Ok(new_line), if @line contains backslash line-continuation
characters.
 OR
Err(CannotTransform), otherwise.

#### See also

- [Line](#line)

### StringMerger.__validate_msg

[[find in source code]](../../blackt/__init__.py#L3234)

```python
@staticmethod
def __validate_msg(line: Line, string_idx: int) -> TResult[None]:
```

Validate (M)erge (S)tring (G)roup

Transform-time string validation logic for __merge_string_group(...).

#### Returns

* Ok(None), if ALL validation checks (listed below) pass.
 OR
* Err(CannotTransform), if any of the following are true:
 - The target string group does not contain ANY stand-alone comments.
 - The target string is not in a string group (i.e. it has no
   adjacent strings).
 - The string group has more than one inline comment.
 - The string group has an inline comment that appears to be a pragma.
 - The set of all string prefixes in the string group is of
   length greater than one and is not equal to {"", "f"}.
 - The string group consists of raw strings.

#### See also

- [Line](#line)

### StringMerger().do_match

[[find in source code]](../../blackt/__init__.py#L3010)

```python
def do_match(line: Line) -> TMatchResult:
```

#### See also

- [Line](#line)
- [TMatchResult](#tmatchresult)

### StringMerger().do_transform

[[find in source code]](../../blackt/__init__.py#L3028)

```python
def do_transform(line: Line, string_idx: int) -> Iterator[TResult[Line]]:
```

#### See also

- [Line](#line)

## StringParenStripper

[[find in source code]](../../blackt/__init__.py#L3316)

```python
class StringParenStripper(StringTransformer):
```

StringTransformer that strips surrounding parentheses from strings.

Requirements:
 The line contains a string which is surrounded by parentheses and:
  - The target string is NOT the only argument to a function call.
  - The target string is NOT a "pointless" string.
  - If the target string contains a PERCENT, the brackets are not
    preceeded or followed by an operator with higher precedence than
    PERCENT.

Transformations:
 The parentheses mentioned in the 'Requirements' section are stripped.

Collaborations:
 StringParenStripper has its own inherent usefulness, but it is also
 relied on to clean up the parentheses created by StringParenWrapper (in
 the event that they are no longer needed).

#### See also

- [StringTransformer](#stringtransformer)

### StringParenStripper().do_match

[[find in source code]](../../blackt/__init__.py#L3336)

```python
def do_match(line: Line) -> TMatchResult:
```

#### See also

- [Line](#line)
- [TMatchResult](#tmatchresult)

### StringParenStripper().do_transform

[[find in source code]](../../blackt/__init__.py#L3427)

```python
def do_transform(line: Line, string_idx: int) -> Iterator[TResult[Line]]:
```

#### See also

- [Line](#line)

## StringParenWrapper

[[find in source code]](../../blackt/__init__.py#L4094)

```python
class StringParenWrapper(CustomSplitMapMixin, BaseStringSplitter):
```

StringTransformer that splits non-"atom" strings (i.e. strings that do not
exist on lines by themselves).

Requirements:
 All of the requirements listed in BaseStringSplitter's docstring in
 addition to the requirements listed below:

* The line is a return/yield statement, which returns/yields a string.
 OR
* The line is part of a ternary expression (e.g. `x = y if cond else
z`) such that the line starts with `else <string>`, where <string> is
some string.
 OR
* The line is an assert statement, which ends with a string.
 OR
* The line is an assignment statement (e.g. `x = <string>` or `x +=
<string>`) such that the variable is being assigned the value of some
string.
 OR
* The line is a dictionary key assignment where some valid key is being
assigned the value of some string.

Transformations:
 The chosen string is wrapped in parentheses and then split at the LPAR.

We then have one line which ends with an LPAR and another line that
starts with the chosen string. The latter line is then split again at
the RPAR. This results in the RPAR (and possibly a trailing comma)
being placed on its own line.

NOTE: If any leaves exist to the right of the chosen string (except
for a trailing comma, which would be placed after the RPAR), those
leaves are placed inside the parentheses.  In effect, the chosen
string is not necessarily being "wrapped" by parentheses. We can,
however, count on the LPAR being placed directly before the chosen
string.

In other words, StringParenWrapper creates "atom" strings. These
can then be split again by StringSplitter, if necessary.

Collaborations:
 In the event that a string line split by StringParenWrapper is
 changed such that it no longer needs to be given its own line,
 StringParenWrapper relies on StringParenStripper to clean up the
 parentheses it created.

#### See also

- [BaseStringSplitter](#basestringsplitter)
- [CustomSplitMapMixin](#customsplitmapmixin)

### StringParenWrapper().do_splitter_match

[[find in source code]](../../blackt/__init__.py#L4143)

```python
def do_splitter_match(line: Line) -> TMatchResult:
```

#### See also

- [Line](#line)
- [TMatchResult](#tmatchresult)

### StringParenWrapper().do_transform

[[find in source code]](../../blackt/__init__.py#L4345)

```python
def do_transform(line: Line, string_idx: int) -> Iterator[TResult[Line]]:
```

#### See also

- [Line](#line)

## StringParser

[[find in source code]](../../blackt/__init__.py#L4443)

```python
class StringParser():
    def __init__() -> None:
```

A state machine that aids in parsing a string's "trailer", which can be
either non-existent, an old-style formatting sequence (e.g. `% varX` or `%
(varX, varY)`), or a method-call / attribute access (e.g. `.format(varX,
varY)`).

NOTE: A new StringParser object MUST be instantiated for each string
trailer we need to parse.

#### Examples

We shall assume that `line` equals the [Line](#line) object that corresponds
to the following line of python code:

```
x = "Some {}.".format("String") + some_other_string
```

Furthermore, we will assume that `string_idx` is some index such that:

```
assert line.leaves[string_idx].value == "Some {}."
```

The following code snippet then holds:

```
string_parser = StringParser()
idx = string_parser.parse(line.leaves, string_idx)
assert line.leaves[idx].type == token.PLUS
```

#### Attributes

- `START` - String Parser States: `1`

### StringParser().parse

[[find in source code]](../../blackt/__init__.py#L4515)

```python
def parse(leaves: List[Leaf], string_idx: int) -> int:
```

Pre-conditions:
 * @leaves[@string_idx].type == token.STRING

#### Returns

The index directly after the last leaf which is apart of the string
trailer, if a "trailer" exists.
 OR
@string_idx + 1, if no string "trailer" exists.

## StringSplitter

[[find in source code]](../../blackt/__init__.py#L3662)

```python
class StringSplitter(CustomSplitMapMixin, BaseStringSplitter):
```

StringTransformer that splits "atom" strings (i.e. strings which exist on
lines by themselves).

Requirements:
 * The line consists ONLY of a single string (with the exception of a
 '+' symbol which MAY exist at the start of the line), MAYBE a string
 trailer, and MAYBE a trailing comma.
  AND
 * All of the requirements listed in BaseStringSplitter's docstring.

Transformations:
 The string mentioned in the 'Requirements' section is split into as
 many substrings as necessary to adhere to the configured line length.

In the final set of substrings, no substring should be smaller than
MIN_SUBSTR_SIZE characters.

The string will ONLY be split on spaces (i.e. each new substring should
start with a space). Note that the string will NOT be split on a space
which is escaped with a backslash.

If the string is an f-string, it will NOT be split in the middle of an
f-expression (e.g. in f"FooBar: {foo() if x else bar()}", {foo() if x
else bar()} is an f-expression).

If the string that is being split has an associated set of custom split
records and those custom splits will NOT result in any line going over
the configured line length, those custom splits are used. Otherwise the
string is split as late as possible (from left-to-right) while still
adhering to the transformation rules listed above.

Collaborations:
 StringSplitter relies on StringMerger to construct the appropriate
 CustomSplit objects and add them to the custom split map.

#### Attributes

- `RE_FEXPR` - Matches an "f-expression" (e.g. {var}) that might be found in an f-string.: `'\n\t(?<!\\{) (?:\\{\\{)* \\{ (?!\\{)\n\t\t(?:\...`

#### See also

- [BaseStringSplitter](#basestringsplitter)
- [CustomSplitMapMixin](#customsplitmapmixin)

### StringSplitter().__get_break_idx

[[find in source code]](../../blackt/__init__.py#L3953)

```python
def __get_break_idx(string: str, max_break_idx: int) -> Optional[int]:
```

This method contains the algorithm that StringSplitter uses to
determine which character to split each string at.

#### Arguments

- `@string` - The substring that we are attempting to split.
- `@max_break_idx` - The ideal break index. We will return this value if it
meets all the necessary conditions. In the likely event that it
doesn't we will try to find the closest index BELOW @max_break_idx
that does. If that fails, we will expand our search by also
considering all valid indices ABOVE @max_break_idx.

Pre-Conditions:
 * assert_is_leaf_string(@string)
 * 0 <= @max_break_idx < len(@string)

#### Returns

break_idx, if an index is able to be found that meets all of the
conditions listed in the 'Transformations' section of this classes'
docstring.
 OR
None, otherwise.

### StringSplitter().__normalize_f_string

[[find in source code]](../../blackt/__init__.py#L4066)

```python
def __normalize_f_string(string: str, prefix: str) -> str:
```

Pre-Conditions:
 * assert_is_leaf_string(@string)

#### Returns

* If @string is an f-string that contains no f-expressions, we
return a string identical to @string except that the 'f' prefix
has been stripped and all double braces (i.e. '{{' or '}}') have
been normalized (i.e. turned into '{' or '}').
 OR
* Otherwise, we return @string.

### StringSplitter().do_splitter_match

[[find in source code]](../../blackt/__init__.py#L3713)

```python
def do_splitter_match(line: Line) -> TMatchResult:
```

#### See also

- [Line](#line)
- [TMatchResult](#tmatchresult)

### StringSplitter().do_transform

[[find in source code]](../../blackt/__init__.py#L3752)

```python
def do_transform(line: Line, string_idx: int) -> Iterator[TResult[Line]]:
```

#### See also

- [Line](#line)

## StringTransformer

[[find in source code]](../../blackt/__init__.py#L2810)

```python
dataclass
class StringTransformer(ABC):
```

An implementation of the Transformer protocol that relies on its
subclasses overriding the template methods `do_match(...)` and
`do_transform(...)`.

This Transformer works exclusively on strings (for example, by merging
or splitting them).

The following sections can be found among the docstrings of each concrete
StringTransformer subclass.

Requirements:
 Which requirements must be met of the given Line for this
 StringTransformer to be applied?

Transformations:
 If the given Line meets all of the above requirements, which string
 transformations can you expect to be applied to it by this
 StringTransformer?

Collaborations:
 What contractual agreements does this StringTransformer have with other
 StringTransfomers? Such collaborations should be eliminated/minimized
 as much as possible.

### StringTransformer().\_\_call\_\_

[[find in source code]](../../blackt/__init__.py#L2870)

```python
def __call__(line: Line, _features: Collection[Feature]) -> Iterator[Line]:
```

StringTransformer instances have a call signature that mirrors that of
the Transformer type.

#### Raises

CannotTransform(...) if the concrete StringTransformer class is unable
to transform @line.

#### See also

- [Line](#line)

### StringTransformer().do_match

[[find in source code]](../../blackt/__init__.py#L2841)

```python
@abstractmethod
def do_match(line: Line) -> TMatchResult:
```

#### Returns

* Ok(string_idx) such that `line.leaves[string_idx]` is our target
string, if a match was able to be made.
 OR
* Err(CannotTransform), if a match was not able to be made.

#### See also

- [Line](#line)
- [TMatchResult](#tmatchresult)

### StringTransformer().do_transform

[[find in source code]](../../blackt/__init__.py#L2851)

```python
@abstractmethod
def do_transform(line: Line, string_idx: int) -> Iterator[TResult[Line]]:
```

#### Yields

* Ok(new_line) where new_line is the new transformed line.
 OR
* Err(CannotTransform) if the transformation failed for some reason. The
`do_match(...)` template method should usually be used to reject
the form of the given Line, but in some cases it is difficult to
know whether or not a Line meets the StringTransformer's
requirements until the transformation is already midway.

Side Effects:
 This method should NOT mutate @line directly, but it MAY mutate the
 Line's underlying Node structure. (WARNING: If the underlying Node
 structure IS altered, then this method should NOT be allowed to
 yield an CannotTransform after that point.)

#### See also

- [Line](#line)

## TargetVersion

[[find in source code]](../../blackt/__init__.py#L171)

```python
class TargetVersion(Enum):
```

### TargetVersion().is_python2

[[find in source code]](../../blackt/__init__.py#L181)

```python
def is_python2() -> bool:
```

## Visitor

[[find in source code]](../../blackt/__init__.py#L1154)

```python
class Visitor(Generic[T]):
```

Basic lib2to3 visitor that yields things of type `T` on `visit()`.

### Visitor().visit

[[find in source code]](../../blackt/__init__.py#L1157)

```python
def visit(node: LN) -> Iterator[T]:
```

Main method to visit `node` and its children.

It tries to find a `visit_*()` method for the given `node.type`, like
`visit_simple_stmt` for Node objects or `visit_INDENT` for Leaf objects.
If no dedicated `visit_*()` method is found, chooses `visit_default()`
instead.

Then yields objects of type `T` from the selected visitor.

#### See also

- [LN](#ln)

### Visitor().visit_default

[[find in source code]](../../blackt/__init__.py#L1181)

```python
def visit_default(node: LN) -> Iterator[T]:
```

Default `visit_*()` implementation. Recurses to children of `node`.

#### See also

- [LN](#ln)

## WriteBack

[[find in source code]](../../blackt/__init__.py#L145)

```python
class WriteBack(Enum):
```

### WriteBack.from_configuration

[[find in source code]](../../blackt/__init__.py#L152)

```python
@classmethod
def from_configuration(
    check: bool,
    diff: bool,
    color: bool = False,
) -> 'WriteBack':
```

## TErr

[[find in source code]](../../blackt/__init__.py#L4585)

```python
def TErr(err_msg: str) -> Err[CannotTransform]:
```

(T)ransform Err

Convenience function used when working with the TResult type.

## append_leaves

[[find in source code]](../../blackt/__init__.py#L4738)

```python
def append_leaves(
    new_line: Line,
    old_line: Line,
    leaves: List[Leaf],
    preformatted: bool = False,
) -> None:
```

Append leaves (taken from @old_line) to @new_line, making sure to fix the
underlying Node structure where appropriate.

All of the leaves in @leaves are duplicated. The duplicates are then
appended to @new_line and used to replace their originals in the underlying
Node structure. Any comments attached to the old leaves are reattached to
the new leaves.

Pre-conditions:
 set(@leaves) is a subset of set(@old_line.leaves).

#### See also

- [Line](#line)

## assert_equivalent

[[find in source code]](../../blackt/__init__.py#L6436)

```python
def assert_equivalent(src: str, dst: str) -> None:
```

Raise AssertionError if `src` and `dst` aren't equivalent.

## assert_is_leaf_string

[[find in source code]](../../blackt/__init__.py#L4798)

```python
def assert_is_leaf_string(string: str) -> None:
```

Checks the pre-condition that @string has the format that you would expect
of `leaf.value` where `leaf` is some Leaf such that `leaf.type ==
token.STRING`. A more precise description of the pre-conditions that are
checked are listed below.

Pre-conditions:
 * @string starts with either ', ", <prefix>', or <prefix>" where
 `set(<prefix>)` is some subset of `set(STRING_PREFIX_CHARS)`.
 * @string ends with a quote character (' or ").

#### Raises

AssertionError(...) if the pre-conditions listed above are not
satisfied.

## assert_stable

[[find in source code]](../../blackt/__init__.py#L6467)

```python
def assert_stable(src: str, dst: str, mode: Mode) -> None:
```

Raise AssertionError if `dst` reformats differently the second time.

#### See also

- [Mode](#mode)

## bracket_split_build_line

[[find in source code]](../../blackt/__init__.py#L4983)

```python
def bracket_split_build_line(
    leaves: List[Leaf],
    original: Line,
    opening_bracket: Leaf,
    is_body: bool = False,
) -> Line:
```

Return a new line with given `leaves` and respective comments from `original`.

If `is_body` is True, the result line is one-indented inside brackets and as such
has its first leaf's prefix normalized and a trailing comma added when expected.

#### See also

- [Line](#line)

## bracket_split_succeeded_or_raise

[[find in source code]](../../blackt/__init__.py#L4957)

```python
def bracket_split_succeeded_or_raise(
    head: Line,
    body: Line,
    tail: Line,
) -> None:
```

Raise :exc:[CannotSplit](#cannotsplit) if the last left- or right-hand split failed.

Do nothing otherwise.

A left- or right-hand split is based on a pair of brackets. Content before
(and including) the opening bracket is left on one line, content inside the
brackets is put on a separate line, and finally content starting with and
following the closing bracket is put on a separate line.

Those are called `head`, `body`, and `tail`, respectively. If the split
produced the same line (all content in `head`) or ended up with an empty `body`
and the `tail` is just the closing bracket, then it's considered failed.

#### See also

- [Line](#line)

## can_be_split

[[find in source code]](../../blackt/__init__.py#L6622)

```python
def can_be_split(line: Line) -> bool:
```

Return False if the line cannot be split *for sure*.

This is not an exhaustive search but a cheap heuristic that we can use to
avoid some unfortunate formattings (mostly around wrapping unsplittable code
in unnecessary parentheses).

#### See also

- [Line](#line)

## can_omit_invisible_parens

[[find in source code]](../../blackt/__init__.py#L6658)

```python
def can_omit_invisible_parens(
    line: Line,
    line_length: int,
    omit_on_explode: Collection[LeafID] = (),
) -> bool:
```

Does `line` have a shape safe to reformat without optional parens around it?

Returns True for only a subset of potentially nice looking formattings but
the point is to not return false positives that end up producing lines that
are too long.

#### See also

- [Line](#line)

## cancel

[[find in source code]](../../blackt/__init__.py#L6525)

```python
def cancel(tasks: Iterable['asyncio.Task[Any]']) -> None:
```

asyncio signal handler that cancels all `tasks` and reports to stderr.

## child_towards

[[find in source code]](../../blackt/__init__.py#L2451)

```python
def child_towards(ancestor: Node, descendant: LN) -> Optional[LN]:
```

Return the child of `ancestor` that contains `descendant`.

#### See also

- [LN](#ln)

## color_diff

[[find in source code]](../../blackt/__init__.py#L910)

```python
def color_diff(contents: str) -> str:
```

Inject the ANSI color codes to the diff.

## container_of

[[find in source code]](../../blackt/__init__.py#L2459)

```python
def container_of(leaf: Leaf) -> LN:
```

Return `leaf` or one of its ancestors that is the topmost container of it.

By "container" we mean a node where `leaf` is the very first child.

#### See also

- [LN](#ln)

## contains_fmt_on_at_column

[[find in source code]](../../blackt/__init__.py#L5521)

```python
def contains_fmt_on_at_column(container: LN, column: int) -> bool:
```

Determine if children at a given column have formatting switched on.

#### See also

- [LN](#ln)

## contains_pragma_comment

[[find in source code]](../../blackt/__init__.py#L4594)

```python
def contains_pragma_comment(comment_list: List[Leaf]) -> bool:
```

#### Returns

True iff one of the comments in @comment_list is a pragma used by one
of the more common static analysis tools for python (e.g. mypy, flake8,
pylint).

## convert_one_fmt_off_pair

[[find in source code]](../../blackt/__init__.py#L5411)

```python
def convert_one_fmt_off_pair(node: Node) -> bool:
```

Convert content of a single `# fmt: off`/`# fmt: on` into a standalone comment.

Returns True if a pair was converted.

## decode_bytes

[[find in source code]](../../blackt/__init__.py#L1065)

```python
def decode_bytes(src: bytes) -> Tuple[(FileContent, Encoding, NewLine)]:
```

Return a tuple of (decoded_contents, encoding, newline).

`newline` is either CRLF or LF but `decoded_contents` is decoded with
universal newlines (i.e. only contains LF).

## delimiter_split

[[find in source code]](../../blackt/__init__.py#L5041)

```python
@dont_increase_indentation
def delimiter_split(
    line: Line,
    features: Collection[Feature] = (),
) -> Iterator[Line]:
```

Split according to delimiters of the highest priority.

If the appropriate Features are given, the split will add trailing commas
also in function signatures and calls that contain `*` and `**`.

#### See also

- [Line](#line)
- [dont_increase_indentation](#dont_increase_indentation)

## detect_target_versions

[[find in source code]](../../blackt/__init__.py#L5955)

```python
def detect_target_versions(node: Node) -> Set[TargetVersion]:
```

Detect the version to target based on the nodes used.

## diff

[[find in source code]](../../blackt/__init__.py#L6505)

```python
def diff(a: str, b: str, a_name: str, b_name: str) -> str:
```

Return a unified diff string between strings `a` and `b`.

## dont_increase_indentation

[[find in source code]](../../blackt/__init__.py#L5026)

```python
def dont_increase_indentation(split_func: Transformer) -> Transformer:
```

Normalize prefix of the first leaf in every line returned by `split_func`.

This is a decorator over relevant split functions.

#### See also

- [Transformer](#transformer)

## dump_to_file

[[find in source code]](../../blackt/__init__.py#L6483)

```python
@mypyc_attr(patchable=True)
def dump_to_file(ensure_final_newline: bool = True, *output: str) -> str:
```

Dump `output` to a temporary file. Return path to the file.

## ensure_visible

[[find in source code]](../../blackt/__init__.py#L5827)

```python
def ensure_visible(leaf: Leaf) -> None:
```

Make sure parentheses are visible.

They could be invisible as part of some statements (see
:func:[normalize_invisible_parens](#normalize_invisible_parens) and :func:`visit_import_from`).

## enumerate_reversed

[[find in source code]](../../blackt/__init__.py#L6578)

```python
def enumerate_reversed(sequence: Sequence[T]) -> Iterator[Tuple[(Index, T)]]:
```

Like `reversed(enumerate(sequence))` if that were possible.

## enumerate_with_length

[[find in source code]](../../blackt/__init__.py#L6586)

```python
def enumerate_with_length(
    line: Line,
    reversed: bool = False,
) -> Iterator[Tuple[(Index, Leaf, int)]]:
```

Return an enumeration of leaves with their length.

Stops prematurely on multiline strings and standalone comments.

#### See also

- [Line](#line)

## filter_cached

[[find in source code]](../../blackt/__init__.py#L6868)

```python
def filter_cached(
    cache: Cache,
    sources: Iterable[Path],
) -> Tuple[(Set[Path], Set[Path])]:
```

Split an iterable of paths in `sources` into two sets.

The first contains paths of files that modified on disk or are not in the
cache. The other contains paths to non-modified files.

#### See also

- [Cache](#cache)

## find_project_root

[[find in source code]](../../blackt/__init__.py#L6196)

```python
@lru_cache()
def find_project_root(srcs: Iterable[str]) -> Path:
```

Return a directory containing .git, .hg, or pyproject.toml.

That directory will be a common parent of all files and directories
passed in `srcs`.

If no directory in the tree contains a marker that would specify it's the
project root, the root of the file system is returned.

## find_pyproject_toml

[[find in source code]](../../blackt/__init__.py#L285)

```python
def find_pyproject_toml(path_search_start: Iterable[str]) -> Optional[str]:
```

Find the absolute filepath to a pyproject.toml if it exists

## find_user_pyproject_toml

[[find in source code]](../../blackt/__init__.py#L6235)

```python
@lru_cache()
def find_user_pyproject_toml() -> Path:
```

Return the path to the top-level user configuration for black.

This looks for ~\.black on Windows and ~/.config/black on Linux and other
Unix systems.

## first_child_is_arith

[[find in source code]](../../blackt/__init__.py#L5627)

```python
def first_child_is_arith(node: Node) -> bool:
```

Whether first child is an arithmetic or a binary arithmetic expression

## first_leaf_column

[[find in source code]](../../blackt/__init__.py#L5536)

```python
def first_leaf_column(node: Node) -> Optional[int]:
```

Returns the column of the first leaf child of a node.

## fix_docstring

[[find in source code]](../../blackt/__init__.py#L6970)

```python
def fix_docstring(docstring: str, prefix: str) -> str:
```

## format_file_contents

[[find in source code]](../../blackt/__init__.py#L983)

```python
def format_file_contents(
    src_contents: str,
    fast: bool,
    mode: Mode,
) -> FileContent:
```

Reformat contents of a file and return new contents.

If `fast` is False, additionally confirm that the reformatted code is
valid by calling :func:[assert_equivalent](#assert_equivalent) and :func:[assert_stable](#assert_stable) on it.
`mode` is passed to :func:[format_str](#format_str).

#### See also

- [FileContent](#filecontent)
- [Mode](#mode)

## format_file_in_place

[[find in source code]](../../blackt/__init__.py#L860)

```python
def format_file_in_place(
    src: Path,
    fast: bool,
    mode: Mode,
    write_back: WriteBack = WriteBack.NO,
    lock: Any = None,
) -> bool:
```

Format file under `src` path. Return True if changed.

If `write_back` is DIFF, write a diff to stdout. If it is YES, write reformatted
code to the file.
`mode` and `fast` options are passed to :func:[format_file_contents](#format_file_contents).

#### See also

- [Mode](#mode)
- [WriteBack](#writeback)

## format_float_or_int_string

[[find in source code]](../../blackt/__init__.py#L5342)

```python
def format_float_or_int_string(text: str) -> str:
```

Formats a float string like "1.0".

## format_hex

[[find in source code]](../../blackt/__init__.py#L5306)

```python
def format_hex(text: str) -> str:
```

Formats a hexadecimal string like "0x12b3"

Uses lowercase because of similarity between "B" and "8", which
can cause security issues.
see: https://github.com/psf/black/issues/1692

## format_long_or_complex_number

[[find in source code]](../../blackt/__init__.py#L5332)

```python
def format_long_or_complex_number(text: str) -> str:
```

Formats a long or complex string like `10L` or `10j`

## format_scientific_notation

[[find in source code]](../../blackt/__init__.py#L5319)

```python
def format_scientific_notation(text: str) -> str:
```

Formats a numeric string utilizing scentific notation

## format_stdin_to_stdout

[[find in source code]](../../blackt/__init__.py#L946)

```python
def format_stdin_to_stdout(
    fast: bool,
    write_back: WriteBack = WriteBack.NO,
    mode: Mode,
) -> bool:
```

Format file on stdin. Return True if changed.

If `write_back` is YES, write reformatted code back to stdout. If it is DIFF,
write a diff to stdout. The `mode` argument is passed to
:func:[format_file_contents](#format_file_contents).

#### See also

- [Mode](#mode)
- [WriteBack](#writeback)

## format_str

[[find in source code]](../../blackt/__init__.py#L1003)

```python
def format_str(src_contents: str, mode: Mode) -> FileContent:
```

Reformat a string and return new contents.

`mode` determines formatting options, such as how many characters per line are
allowed.  Example:

```python
>>> import black
>>> print(black.format_str("def f(arg:str='')->None:...", mode=black.Mode()))
def f(arg: str = "") -> None:
 ...
```

A more complex example:

```python
>>> print(
...   black.format_str(
...     "def f(arg:str='')->None: hey",
...     mode=black.Mode(
...       target_versions={black.TargetVersion.PY36},
...       line_length=10,
...       string_normalization=False,
...       is_pyi=False,
...     ),
...   ),
... )
def f(
 arg: str = '',
) -> None:
 hey

#### See also

- [FileContent](#filecontent)
- [Mode](#mode)

## gen_python_files

[[find in source code]](../../blackt/__init__.py#L6130)

```python
def gen_python_files(
    paths: Iterable[Path],
    root: Path,
    include: Optional[Pattern[str]],
    exclude: Pattern[str],
    extend_exclude: Optional[Pattern[str]],
    force_exclude: Optional[Pattern[str]],
    report: 'Report',
    gitignore: PathSpec,
) -> Iterator[Path]:
```

Generate all files under `path` whose paths are not excluded by the
`exclude_regex`, `extend_exclude`, or `force_exclude` regexes,
but are included by the `include` regex.

Symbolic links pointing outside of the `root` directory are ignored.

`report` is where output about exclusions goes.

## generate_comments

[[find in source code]](../../blackt/__init__.py#L2600)

```python
def generate_comments(leaf: LN) -> Iterator[Leaf]:
```

Clean the prefix of the `leaf` and generate comments from it, if any.

Comments in lib2to3 are shoved into the whitespace prefix.  This happens
in `pgen2/driver.py:Driver.parse_tokens()`.  This was a brilliant implementation
move because it does away with modifying the grammar to include all the
possible places in which comments can be placed.

The sad consequence for us though is that comments don't "belong" anywhere.
This is why this function generates simple parentless Leaf objects for
comments.  We simply don't know what the correct parent should be.

No matter though, we can live without this.  We really only need to
differentiate between inline and standalone comments.  The latter don't
share the line with any code.

Inline comments are emitted as regular token.COMMENT leaves.  Standalone
are emitted with a fake STANDALONE_COMMENT token identifier.

#### See also

- [LN](#ln)

## generate_ignored_nodes

[[find in source code]](../../blackt/__init__.py#L5470)

```python
def generate_ignored_nodes(leaf: Leaf, comment: ProtoComment) -> Iterator[LN]:
```

Starting from the container of `leaf`, generate all leaves until `# fmt: on`.

If comment is skip, returns leaf only.
Stops at the end of the block.

#### See also

- [ProtoComment](#protocomment)

## generate_trailers_to_omit

[[find in source code]](../../blackt/__init__.py#L5963)

```python
def generate_trailers_to_omit(
    line: Line,
    line_length: int,
) -> Iterator[Set[LeafID]]:
```

Generate sets of closing bracket IDs that should be omitted in a RHS.

Brackets can be omitted if the entire trailer up to and including
a preceding closing bracket fits in one line.

Yielded sets are cumulative (contain results of previous yields, too).  First
set is empty, unless the line should explode, in which case bracket pairs until
the one that needs to explode are omitted.

#### See also

- [Line](#line)

## get_cache_file

[[find in source code]](../../blackt/__init__.py#L6840)

```python
def get_cache_file(mode: Mode) -> Path:
```

#### See also

- [Mode](#mode)

## get_cache_info

[[find in source code]](../../blackt/__init__.py#L6862)

```python
def get_cache_info(path: Path) -> CacheInfo:
```

Return the information used to check if a file is already formatted or not.

#### See also

- [CacheInfo](#cacheinfo)

## get_features_used

[[find in source code]](../../blackt/__init__.py#L5898)

```python
def get_features_used(node: Node) -> Set[Feature]:
```

Return a set of (relatively) new Python features used in this file.

Currently looking for:
- f-strings;
- underscores in numeric literals;
- trailing commas after * or ** in function signatures and calls;
- positional only arguments in function signatures and lambdas;
- assignment expression;
- relaxed decorator syntax;

## get_future_imports

[[find in source code]](../../blackt/__init__.py#L6037)

```python
def get_future_imports(node: Node) -> Set[str]:
```

Return a set of __future__ imports in the file.

## get_gitignore

[[find in source code]](../../blackt/__init__.py#L6087)

```python
@lru_cache()
def get_gitignore(root: Path) -> PathSpec:
```

Return a PathSpec matching gitignore content if present.

## get_grammars

[[find in source code]](../../blackt/__init__.py#L1082)

```python
def get_grammars(target_versions: Set[TargetVersion]) -> List[Grammar]:
```

## get_sources

[[find in source code]](../../blackt/__init__.py#L627)

```python
def get_sources(
    ctx: click.Context,
    src: Tuple[(str, ...)],
    quiet: bool,
    verbose: bool,
    include: Pattern[str],
    exclude: Pattern[str],
    extend_exclude: Optional[Pattern[str]],
    force_exclude: Optional[Pattern[str]],
    report: 'Report',
    stdin_filename: Optional[str],
) -> Set[Path]:
```

Compute the set of files to be formatted.

## get_string_prefix

[[find in source code]](../../blackt/__init__.py#L4779)

```python
def get_string_prefix(string: str) -> str:
```

Pre-conditions:
 * assert_is_leaf_string(@string)

#### Returns

@string's prefix (e.g. '', 'r', 'f', or 'rf').

## has_triple_quotes

[[find in source code]](../../blackt/__init__.py#L4669)

```python
def has_triple_quotes(string: str) -> bool:
```

#### Returns

True iff @string starts with three quotation characters.

## insert_str_child_factory

[[find in source code]](../../blackt/__init__.py#L4608)

```python
def insert_str_child_factory(string_leaf: Leaf) -> Callable[([LN], None)]:
```

Factory for a convenience function that is used to orphan @string_leaf
and then insert multiple new leaves into the same part of the node
structure that @string_leaf had originally occupied.

#### Examples

Let `string_leaf = Leaf(token.STRING, '"foo"')` and `N =
string_leaf.parent`. Assume the node `N` has the following
original structure:

Node(
 expr_stmt, [
  Leaf(NAME, 'x'),
  Leaf(EQUAL, '='),
  Leaf(STRING, '"foo"'),
 ]
)

We then run the code snippet shown below.

```
insert_str_child = insert_str_child_factory(string_leaf)

lpar = Leaf(token.LPAR, '(')
insert_str_child(lpar)

bar = Leaf(token.STRING, '"bar"')
insert_str_child(bar)

rpar = Leaf(token.RPAR, ')')
insert_str_child(rpar)
```

After which point, it follows that `string_leaf.parent is None` and
the node `N` now has the following structure:

Node(
 expr_stmt, [
  Leaf(NAME, 'x'),
  Leaf(EQUAL, '='),
  Leaf(LPAR, '('),
  Leaf(STRING, '"bar"'),
  Leaf(RPAR, ')'),
 ]
)

## is_atom_with_invisible_parens

[[find in source code]](../../blackt/__init__.py#L5585)

```python
def is_atom_with_invisible_parens(node: LN) -> bool:
```

Given a [LN](#blackt), determines whether it's an atom `node` with invisible
parens. Useful in dedupe-ing and normalizing parens.

#### See also

- [LN](#ln)

## is_docstring

[[find in source code]](../../blackt/__init__.py#L6928)

```python
def is_docstring(leaf: Leaf) -> bool:
```

## is_empty_lpar

[[find in source code]](../../blackt/__init__.py#L4695)

```python
def is_empty_lpar(leaf: Leaf) -> bool:
```

## is_empty_par

[[find in source code]](../../blackt/__init__.py#L4691)

```python
def is_empty_par(leaf: Leaf) -> bool:
```

## is_empty_rpar

[[find in source code]](../../blackt/__init__.py#L4699)

```python
def is_empty_rpar(leaf: Leaf) -> bool:
```

## is_empty_tuple

[[find in source code]](../../blackt/__init__.py#L5603)

```python
def is_empty_tuple(node: LN) -> bool:
```

Return True if `node` holds an empty tuple.

#### See also

- [LN](#ln)

## is_fmt_on

[[find in source code]](../../blackt/__init__.py#L5508)

```python
def is_fmt_on(container: LN) -> bool:
```

Determine whether formatting is switched on within a container.
Determined by whether the last `# fmt:` comment is `on` or `off`.

#### See also

- [LN](#ln)

## is_import

[[find in source code]](../../blackt/__init__.py#L5153)

```python
def is_import(leaf: Leaf) -> bool:
```

Return True if the given leaf starts an import statement.

## is_line_short_enough

[[find in source code]](../../blackt/__init__.py#L6608)

```python
def is_line_short_enough(
    line: Line,
    line_length: int,
    line_str: str = '',
) -> bool:
```

Return True if `line` is no longer than `line_length`.

Uses the provided `line_str` rendering, if any, otherwise computes a new one.

#### See also

- [Line](#line)

## is_multiline_string

[[find in source code]](../../blackt/__init__.py#L5765)

```python
def is_multiline_string(leaf: Leaf) -> bool:
```

Return True if `leaf` is a multiline string that actually spans many lines.

## is_one_tuple

[[find in source code]](../../blackt/__init__.py#L5656)

```python
def is_one_tuple(node: LN) -> bool:
```

Return True if `node` holds a tuple with one element, with or without parens.

#### See also

- [LN](#ln)

## is_one_tuple_between

[[find in source code]](../../blackt/__init__.py#L5866)

```python
def is_one_tuple_between(
    opening: Leaf,
    closing: Leaf,
    leaves: List[Leaf],
) -> bool:
```

Return True if content between `opening` and `closing` looks like a one-tuple.

## is_simple_decorator_expression

[[find in source code]](../../blackt/__init__.py#L5697)

```python
def is_simple_decorator_expression(node: LN) -> bool:
```

Return True iff `node` could be a 'dotted name' decorator

This function takes the node of the 'namedexpr_test' of the new decorator
grammar and test if it would be valid under the old decorator grammar.

The old grammar was: decorator: @ dotted_name [arguments] NEWLINE
The new grammar is : decorator: @ namedexpr_test NEWLINE

#### See also

- [LN](#ln)

## is_simple_decorator_trailer

[[find in source code]](../../blackt/__init__.py#L5678)

```python
def is_simple_decorator_trailer(node: LN, last: bool = False) -> bool:
```

Return True iff `node` is a trailer valid in a simple decorator

#### See also

- [LN](#ln)

## is_split_after_delimiter

[[find in source code]](../../blackt/__init__.py#L2484)

```python
def is_split_after_delimiter(
    leaf: Leaf,
    previous: Optional[Leaf] = None,
) -> Priority:
```

Return the priority of the `leaf` delimiter, given a line break after it.

The delimiter priorities returned here are from those delimiters that would
cause a line break after themselves.

Higher numbers are higher priority.

#### See also

- [Priority](#priority)

## is_split_before_delimiter

[[find in source code]](../../blackt/__init__.py#L2498)

```python
def is_split_before_delimiter(
    leaf: Leaf,
    previous: Optional[Leaf] = None,
) -> Priority:
```

Return the priority of the `leaf` delimiter, given a line break before it.

The delimiter priorities returned here are from those delimiters that would
cause a line break before themselves.

Higher numbers are higher priority.

#### See also

- [Priority](#priority)

## is_stub_body

[[find in source code]](../../blackt/__init__.py#L5783)

```python
def is_stub_body(node: LN) -> bool:
```

Return True if `node` is a simple statement containing an ellipsis.

#### See also

- [LN](#ln)

## is_stub_suite

[[find in source code]](../../blackt/__init__.py#L5770)

```python
def is_stub_suite(node: Node) -> bool:
```

Return True if `node` is a suite with a stub body.

## is_type_comment

[[find in source code]](../../blackt/__init__.py#L5167)

```python
def is_type_comment(leaf: Leaf, suffix: str = '') -> bool:
```

Return True if the given leaf is a special comment.
Only returns true for type comments for now.

## is_valid_index_factory

[[find in source code]](../../blackt/__init__.py#L4703)

```python
def is_valid_index_factory(seq: Sequence[Any]) -> Callable[([int], bool)]:
```

#### Examples

```
my_list = [1, 2, 3]

is_valid_index = is_valid_index_factory(my_list)

assert is_valid_index(0)
assert is_valid_index(2)

assert not is_valid_index(3)
assert not is_valid_index(-1)
```

## is_vararg

[[find in source code]](../../blackt/__init__.py#L5742)

```python
def is_vararg(leaf: Leaf, within: Set[NodeType]) -> bool:
```

Return True if `leaf` is a star or double star in a vararg or kwarg.

If `within` includes VARARGS_PARENTS, this applies to function signatures.
If `within` includes UNPACKING_PARENTS, it applies to right hand-side
extended iterable unpacking (PEP 3132) and additional unpacking
generalizations (PEP 448).

## is_walrus_assignment

[[find in source code]](../../blackt/__init__.py#L5672)

```python
def is_walrus_assignment(node: LN) -> bool:
```

Return True iff `node` is of the shape ( test := test )

#### See also

- [LN](#ln)

## is_yield

[[find in source code]](../../blackt/__init__.py#L5721)

```python
def is_yield(node: LN) -> bool:
```

Return True if `node` holds a `yield` or `yield from` expression.

#### See also

- [LN](#ln)

## last_two_except

[[find in source code]](../../blackt/__init__.py#L6778)

```python
def last_two_except(
    leaves: List[Leaf],
    omit: Collection[LeafID],
) -> Tuple[(Leaf, Leaf)]:
```

Return (penultimate, last) leaves skipping brackets in `omit` and contents.

## left_hand_split

[[find in source code]](../../blackt/__init__.py#L4833)

```python
def left_hand_split(
    line: Line,
    _features: Collection[Feature] = (),
) -> Iterator[Line]:
```

Split line into many lines, starting with the first matching bracket pair.

Note: this usually looks weird, only use this for function definitions.
Prefer RHS otherwise.  This is why this function is not symmetrical with
:func:[right_hand_split](#right_hand_split) which also handles optional parentheses.

#### See also

- [Line](#line)

## lib2to3_parse

[[find in source code]](../../blackt/__init__.py#L1121)

```python
def lib2to3_parse(
    src_txt: str,
    target_versions: Iterable[TargetVersion] = (),
) -> Node:
```

Given a string with source, return the lib2to3 Node.

## lib2to3_unparse

[[find in source code]](../../blackt/__init__.py#L1148)

```python
def lib2to3_unparse(node: Node) -> str:
```

Given a lib2to3 node, return its string representation.

## line_to_string

[[find in source code]](../../blackt/__init__.py#L4730)

```python
def line_to_string(line: Line) -> str:
```

Returns the string representation of @line.

WARNING: This is known to be computationally expensive.

#### See also

- [Line](#line)

## lines_with_leading_tabs_expanded

[[find in source code]](../../blackt/__init__.py#L6948)

```python
def lines_with_leading_tabs_expanded(s: str) -> List[str]:
```

Splits string into lines and expands only leading tabs (following the normal
Python rules)

## list_comments

[[find in source code]](../../blackt/__init__.py#L2641)

```python
@lru_cache(maxsize=4096)
def list_comments(prefix: str, is_endmarker: bool) -> List[ProtoComment]:
```

Return a list of :class:[ProtoComment](#protocomment) objects parsed from the given `prefix`.

## main

[[find in source code]](../../blackt/__init__.py#L374)

```python
@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option(
    '-c',
    '--code',
    type=str,
    help='Format the code passed in as a string.',
)
@click.option(
    '-l',
    '--line-length',
    type=int,
    default=DEFAULT_LINE_LENGTH,
    help='How many characters per line to allow.',
    show_default=True,
)
@click.option(
    '-t',
    '--target-version',
    type=click.Choice([v.name.lower() for v in TargetVersion]),
    callback=target_version_option_callback,
    multiple=True,
    help="Python versions that should be supported by Black's output. [default: per-file auto-detection]",
)
@click.option(
    '--pyi',
    is_flag=True,
    help='Format all input files like typing stubs regardless of file extension (useful when piping source on standard input).',
)
@click.option(
    '-S',
    '--skip-string-normalization',
    is_flag=True,
    help="Don't normalize string quotes or prefixes.",
)
@click.option(
    '-C',
    '--skip-magic-trailing-comma',
    is_flag=True,
    help="Don't use trailing commas as a reason to split lines.",
)
@click.option(
    '--experimental-string-processing',
    is_flag=True,
    hidden=True,
    help='Experimental option that performs more normalization on string literals. Currently disabled because it leads to some crashes.',
)
@click.option(
    '--check',
    is_flag=True,
    help="Don't write the files back, just return the status. Return code 0 means nothing would change. Return code 1 means some files would be reformatted. Return code 123 means there was an internal error.",
)
@click.option(
    '--diff',
    is_flag=True,
    help="Don't write the files back, just output a diff for each file on stdout.",
)
@click.option(
    '--color/--no-color',
    is_flag=True,
    help='Show colored diff. Only applies when `--diff` is given.',
)
@click.option(
    '--fast/--safe',
    is_flag=True,
    help='If --fast given, skip temporary sanity checks. [default: --safe]',
)
@click.option(
    '--include',
    type=str,
    default=DEFAULT_INCLUDES,
    callback=validate_regex,
    help='A regular expression that matches files and directories that should be included on recursive searches. An empty value means all files are included regardless of the name. Use forward slashes for directories on all platforms (Windows, too). Exclusions are calculated first, inclusions later.',
    show_default=True,
)
@click.option(
    '--exclude',
    type=str,
    default=DEFAULT_EXCLUDES,
    callback=validate_regex,
    help='A regular expression that matches files and directories that should be excluded on recursive searches. An empty value means no paths are excluded. Use forward slashes for directories on all platforms (Windows, too). Exclusions are calculated first, inclusions later.',
    show_default=True,
)
@click.option(
    '--extend-exclude',
    type=str,
    callback=validate_regex,
    help='Like --exclude, but adds additional files and directories on top of the excluded ones. (Useful if you simply want to add to the default)',
)
@click.option(
    '--force-exclude',
    type=str,
    callback=validate_regex,
    help='Like --exclude, but files and directories matching this regex will be excluded even when they are passed explicitly as arguments.',
)
@click.option(
    '--stdin-filename',
    type=str,
    help='The name of the file when passing it through stdin. Useful to make sure Black will respect --force-exclude option on some editors that rely on using stdin.',
)
@click.option(
    '-q',
    '--quiet',
    is_flag=True,
    help="Don't emit non-error messages to stderr. Errors are still emitted; silence those with 2>/dev/null.",
)
@click.option(
    '-v',
    '--verbose',
    is_flag=True,
    help='Also emit messages to stderr about files that were not changed or were ignored due to exclusion patterns.',
)
@click.version_option(version=__version__)
@click.argument(
    'src',
    nargs=-1,
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=True,
        readable=True,
        allow_dash=True,
    ),
    is_eager=True,
)
@click.option(
    '--config',
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        allow_dash=False,
        path_type=str,
    ),
    is_eager=True,
    callback=read_pyproject_toml,
    help='Read configuration from FILE path.',
)
@click.pass_context
def main(
    ctx: click.Context,
    code: Optional[str],
    line_length: int,
    target_version: List[TargetVersion],
    check: bool,
    diff: bool,
    color: bool,
    fast: bool,
    pyi: bool,
    skip_string_normalization: bool,
    skip_magic_trailing_comma: bool,
    experimental_string_processing: bool,
    quiet: bool,
    verbose: bool,
    include: Pattern,
    exclude: Pattern,
    extend_exclude: Optional[Pattern],
    force_exclude: Optional[Pattern],
    stdin_filename: Optional[str],
    src: Tuple[(str, ...)],
    config: Optional[str],
) -> None:
```

The uncompromising code formatter.

## make_comment

[[find in source code]](../../blackt/__init__.py#L2678)

```python
def make_comment(content: str) -> str:
```

Return a consistently formatted comment from the given `content` string.

All comments (except for "##", "#!", "#:", '#'", "#%%") should have a single
space between the hash sign and the content.

If `content` didn't start with a hash sign, one is provided.

## max_delimiter_priority_in_atom

[[find in source code]](../../blackt/__init__.py#L5799)

```python
def max_delimiter_priority_in_atom(node: LN) -> Priority:
```

Return maximum delimiter priority inside `node`.

This is specific to atoms with contents contained in a pair of parentheses.
If `node` isn't an atom or there are no enclosing parentheses, returns 0.

#### See also

- [LN](#ln)
- [Priority](#priority)

## maybe_make_parens_invisible_in_atom

[[find in source code]](../../blackt/__init__.py#L5544)

```python
def maybe_make_parens_invisible_in_atom(node: LN, parent: LN) -> bool:
```

If it's safe, make the parens in the atom `node` invisible, recursively.
Additionally, remove repeated, adjacent invisible parens from the atom `node`
as they are redundant.

Returns whether the node should itself be wrapped in invisible parentheses.

#### See also

- [LN](#ln)

## normalize_fmt_off

[[find in source code]](../../blackt/__init__.py#L5404)

```python
def normalize_fmt_off(node: Node) -> None:
```

Convert content between `# fmt: off`/`# fmt: on` into standalone comments.

## normalize_invisible_parens

[[find in source code]](../../blackt/__init__.py#L5351)

```python
def normalize_invisible_parens(node: Node, parens_after: Set[str]) -> None:
```

Make existing optional parentheses invisible or create new ones.

`parens_after` is a set of string leaf values immediately after which parens
should be put.

Standardizes on visible parentheses for single-element tuples, and keeps
existing visible parentheses for other tuples and generator expressions.

## normalize_numeric_literal

[[find in source code]](../../blackt/__init__.py#L5285)

```python
def normalize_numeric_literal(leaf: Leaf) -> None:
```

Normalizes numeric (float, int, and complex) literals.

All letters used in the representation are normalized to lowercase (except
in Python 2 long literals).

## normalize_path_maybe_ignore

[[find in source code]](../../blackt/__init__.py#L6098)

```python
def normalize_path_maybe_ignore(
    path: Path,
    root: Path,
    report: 'Report',
) -> Optional[str]:
```

Normalize `path`. May return `None` if `path` was ignored.

`report` is where "path ignored" output goes.

## normalize_prefix

[[find in source code]](../../blackt/__init__.py#L5175)

```python
def normalize_prefix(leaf: Leaf, inside_brackets: bool) -> None:
```

Leave existing extra newlines if not `inside_brackets`. Remove everything
else.

Note: don't use backslashes for formatting or you'll lose your voting rights.

## normalize_string_prefix

[[find in source code]](../../blackt/__init__.py#L5193)

```python
def normalize_string_prefix(
    leaf: Leaf,
    remove_u_prefix: bool = False,
) -> None:
```

Make all string prefixes lowercase.

If remove_u_prefix is given, also removes any u prefix from the string.

Note: Mutates its argument.

## normalize_string_quotes

[[find in source code]](../../blackt/__init__.py#L5209)

```python
def normalize_string_quotes(leaf: Leaf) -> None:
```

Prefer double quotes but only if it doesn't cause more escaping.

Adds or removes backslashes as appropriate. Doesn't parse and fix
strings nested in f-strings (yet).

Note: Mutates its argument.

## nullcontext

[[find in source code]](../../blackt/__init__.py#L6496)

```python
@contextmanager
def nullcontext() -> Iterator[None]:
```

Return an empty context manager.

To be used like [nullcontext](#nullcontext) in Python 3.7.

## parent_type

[[find in source code]](../../blackt/__init__.py#L4678)

```python
def parent_type(node: Optional[LN]) -> Optional[NodeType]:
```

#### Returns

@node.parent.type, if @node is not None and has a parent.
 OR
None, otherwise.

## parse_ast

[[find in source code]](../../blackt/__init__.py#L6337)

```python
def parse_ast(src: str) -> Union[(ast.AST, ast3.AST, ast27.AST)]:
```

## parse_pyproject_toml

[[find in source code]](../../blackt/__init__.py#L296)

```python
def parse_pyproject_toml(path_config: str) -> Dict[(str, Any)]:
```

Parse a pyproject toml file, pulling out relevant parts for Black

If parsing fails, will raise a toml.TomlDecodeError

## patch_click

[[find in source code]](../../blackt/__init__.py#L6900)

```python
def patch_click() -> None:
```

Make Click not crash.

On certain misconfigured environments, Python 3 selects the ASCII encoding as the
default which restricts paths that it can access during the lifetime of the
application.  Click refuses to work in this scenario by raising a RuntimeError.

In case of Black the likelihood that non-ASCII characters are going to be used in
file paths is minimal since it's Python source code.  Moreover, this crash was
spurious on Python 3.7 thanks to PEP 538 and PEP 540.

## patched_main

[[find in source code]](../../blackt/__init__.py#L6922)

```python
def patched_main() -> None:
```

## path_empty

[[find in source code]](../../blackt/__init__.py#L694)

```python
def path_empty(
    src: Sized,
    msg: str,
    quiet: bool,
    verbose: bool,
    ctx: click.Context,
) -> None:
```

Exit if there is no `src` provided for formatting

## path_is_excluded

[[find in source code]](../../blackt/__init__.py#L6122)

```python
def path_is_excluded(
    normalized_path: str,
    pattern: Optional[Pattern[str]],
) -> bool:
```

## preceding_leaf

[[find in source code]](../../blackt/__init__.py#L2417)

```python
def preceding_leaf(node: Optional[LN]) -> Optional[Leaf]:
```

Return the first leaf that precedes `node`, if any.

## prev_siblings_are

[[find in source code]](../../blackt/__init__.py#L2435)

```python
def prev_siblings_are(
    node: Optional[LN],
    tokens: List[Optional[NodeType]],
) -> bool:
```

Return if the `node` and its previous siblings match types against the provided
list of tokens; the provided `node`has its type matched against the last element in
the list.  `None` can be used as the first element to declare that the start of the
list is anchored at the start of its parent's children.

## re_compile_maybe_verbose

[[find in source code]](../../blackt/__init__.py#L6567)

```python
def re_compile_maybe_verbose(regex: str) -> Pattern[str]:
```

Compile a regular expression string in `regex`.

If it contains newlines, use verbose mode.

## read_cache

[[find in source code]](../../blackt/__init__.py#L6844)

```python
def read_cache(mode: Mode) -> Cache:
```

Read the cache if it exists and is well formed.

If it is not well formed, the call to write_cache later should resolve the issue.

#### See also

- [Cache](#cache)
- [Mode](#mode)

## read_pyproject_toml

[[find in source code]](../../blackt/__init__.py#L306)

```python
def read_pyproject_toml(
    ctx: click.Context,
    param: click.Parameter,
    value: Optional[str],
) -> Optional[str]:
```

Inject Black configuration from "pyproject.toml" into defaults in `ctx`.

Returns the path to a successfully found and read configuration file, None
otherwise.

## reformat_many

[[find in source code]](../../blackt/__init__.py#L752)

```python
def reformat_many(
    sources: Set[Path],
    fast: bool,
    write_back: WriteBack,
    mode: Mode,
    report: 'Report',
) -> None:
```

Reformat multiple files using a ProcessPoolExecutor.

#### See also

- [Mode](#mode)
- [WriteBack](#writeback)

## reformat_one

[[find in source code]](../../blackt/__init__.py#L705)

```python
def reformat_one(
    src: Path,
    fast: bool,
    write_back: WriteBack,
    mode: Mode,
    report: 'Report',
) -> None:
```

Reformat a single file under `src` without spawning child processes.

`fast`, `write_back`, and `mode` options are passed to
:func:[format_file_in_place](#format_file_in_place) or :func:[format_stdin_to_stdout](#format_stdin_to_stdout).

#### See also

- [Mode](#mode)
- [WriteBack](#writeback)

## replace_child

[[find in source code]](../../blackt/__init__.py#L4762)

```python
def replace_child(old_child: LN, new_child: LN) -> None:
```

Side Effects:
 * If @old_child.parent is set, replace @old_child with @new_child in
 @old_child's underlying Node structure.
  OR
 * Otherwise, this function does nothing.

#### See also

- [LN](#ln)

## right_hand_split

[[find in source code]](../../blackt/__init__.py#L4869)

```python
def right_hand_split(
    line: Line,
    line_length: int,
    features: Collection[Feature] = (),
    omit: Collection[LeafID] = (),
) -> Iterator[Line]:
```

Split line into many lines, starting with the last matching bracket pair.

If the split was by optional parentheses, attempt splitting without them, too.
`omit` is a collection of closing bracket IDs that shouldn't be considered for
this split.

Note: running this function modifies `bracket_depth` on the leaves of `line`.

#### See also

- [Line](#line)

## run_transformer

[[find in source code]](../../blackt/__init__.py#L6799)

```python
def run_transformer(
    line: Line,
    transform: Transformer,
    mode: Mode,
    features: Collection[Feature],
    line_str: str = '',
) -> List[Line]:
```

#### See also

- [Line](#line)
- [Mode](#mode)
- [Transformer](#transformer)

## schedule_formatting

[[find in source code]](../../blackt/__init__.py#L789)

```python
async def schedule_formatting(
    sources: Set[Path],
    fast: bool,
    write_back: WriteBack,
    mode: Mode,
    report: 'Report',
    loop: asyncio.AbstractEventLoop,
    executor: Executor,
) -> None:
```

Run formatting of `sources` in parallel using the provided `executor`.

(Use ProcessPoolExecutors for actual parallelism.)

`write_back`, `fast`, and `mode` options are passed to
:func:[format_file_in_place](#format_file_in_place).

#### See also

- [Mode](#mode)
- [WriteBack](#writeback)

## should_split_line

[[find in source code]](../../blackt/__init__.py#L5839)

```python
def should_split_line(line: Line, opening_bracket: Leaf) -> bool:
```

Should `line` be immediately split with `delimiter_split()` after RHS?

#### See also

- [Line](#line)

## shutdown

[[find in source code]](../../blackt/__init__.py#L6532)

```python
def shutdown(loop: asyncio.AbstractEventLoop) -> None:
```

Cancel all pending tasks on `loop`, wait for them, and close the loop.

## standalone_comment_split

[[find in source code]](../../blackt/__init__.py#L5118)

```python
@dont_increase_indentation
def standalone_comment_split(
    line: Line,
    features: Collection[Feature] = (),
) -> Iterator[Line]:
```

Split standalone comments from the rest of the line.

#### See also

- [Line](#line)
- [dont_increase_indentation](#dont_increase_indentation)

## sub_twice

[[find in source code]](../../blackt/__init__.py#L6558)

```python
def sub_twice(regex: Pattern[str], replacement: str, original: str) -> str:
```

Replace `regex` with `replacement` twice on `original`.

This is used by string normalization to perform replaces on
overlapping matches.

## supports_feature

[[find in source code]](../../blackt/__init__.py#L281)

```python
def supports_feature(
    target_versions: Set[TargetVersion],
    feature: Feature,
) -> bool:
```

#### See also

- [Feature](#feature)

## target_version_option_callback

[[find in source code]](../../blackt/__init__.py#L352)

```python
def target_version_option_callback(
    c: click.Context,
    p: Union[(click.Option, click.Parameter)],
    v: Tuple[(str, ...)],
) -> List[TargetVersion]:
```

Compute the target versions from a --target-version flag.

This is its own function because mypy couldn't infer the type correctly
when it was a lambda, causing mypyc trouble.

## transform_line

[[find in source code]](../../blackt/__init__.py#L2697)

```python
def transform_line(
    line: Line,
    mode: Mode,
    features: Collection[Feature] = (),
) -> Iterator[Line]:
```

Transform a `line`, potentially splitting it into many lines.

They should fit in the allotted `line_length` but might not be able to.

`features` are syntactical features that may be used in the output.

#### See also

- [Line](#line)
- [Mode](#mode)

## unwrap_singleton_parenthesis

[[find in source code]](../../blackt/__init__.py#L5613)

```python
def unwrap_singleton_parenthesis(node: LN) -> Optional[LN]:
```

Returns `wrapped` if `node` is of the shape ( wrapped ).

Parenthesis can be optional. Returns None otherwise

#### See also

- [LN](#ln)

## validate_regex

[[find in source code]](../../blackt/__init__.py#L363)

```python
def validate_regex(
    ctx: click.Context,
    param: click.Parameter,
    value: Optional[str],
) -> Optional[Pattern]:
```

## whitespace

[[find in source code]](../../blackt/__init__.py#L2184)

```python
def whitespace(leaf: Leaf, complex_subscript: bool) -> str:
```

Return whitespace prefix if needed for the given `leaf`.

`complex_subscript` signals whether the given leaf is part of a subscription
which has non-trivial arguments, like arithmetic expressions or function calls.

## wrap_in_parentheses

[[find in source code]](../../blackt/__init__.py#L5638)

```python
def wrap_in_parentheses(
    parent: Node,
    child: LN,
    visible: bool = True,
) -> None:
```

Wrap `child` in parentheses.

This replaces `child` with an atom holding the parentheses and the old
child.  That requires moving the prefix.

If `visible` is False, the leaves will be valueless (and thus invisible).

#### See also

- [LN](#ln)

## wrap_stream_for_windows

[[find in source code]](../../blackt/__init__.py#L926)

```python
def wrap_stream_for_windows(
    f: io.TextIOWrapper,
) -> Union[(io.TextIOWrapper, 'colorama.AnsiToWin32')]:
```

Wrap stream with colorama's wrap_stream so colors are shown on Windows.

If `colorama` is unavailable, the original stream is returned unmodified.
Otherwise, the `wrap_stream()` function determines whether the stream needs
to be wrapped for a Windows environment and will accordingly either return
an `AnsiToWin32` wrapper or the original stream.

## write_cache

[[find in source code]](../../blackt/__init__.py#L6884)

```python
def write_cache(cache: Cache, sources: Iterable[Path], mode: Mode) -> None:
```

Update the cache file.

#### See also

- [Cache](#cache)
- [Mode](#mode)
