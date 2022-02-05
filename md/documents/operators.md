# [x2](../../README.md) / [Documents](../documents.md) / Operators

## Table of Contents

- [Home](../../README.md)
- [Tutorials](../tutorials.md)
-  [Documents ▾](../documents.md)
    - [About](../documents.md#about)
    - [Catalog ▾](../documents.md#catalog)
        - [Comments](./comments.md)
        - [Comparators](./comparators.md)
        - [Configurations](./configurations.md)
        - [Data Types](./dataTypes.md)
        - **Operators ▾**
            - [About](#about)
            - [Documentation](#documentation)
        - [Configurations](./configurations.md)
        - [Packages](./packages.md)
        - [Python API](./pythonAPI.md)
        - [Sections](./sections.md)
        - [Variables](./variables.md)

## About

Operators are keywords that process its arguments.

A statement is a line of code that tells the interpreter what to do. They are always made up of two components: the `operator` and the `arguments`, and they are arranged like so:

```
<operator> [...arguments]
```

For example:

```xt
out "Hello, world!"
```

Or:

```xt
add 1 2 sum
```

A statement can also be wrapped around parentheses (`()`) to group them together.

Some statements return values, which can be stored in a varaible:

```
psh (add 1 2) sum
```

## Documentation

### Add

```xt
add <addend A> <addend B> [sum]
```

Adds two addends together.

| Parameter | Type | Optional | Default | Description |
| :-: | :-: | :-: | :-: | :-: |
| Addend A | [Integer](./dataTypes.md#integer) or [Float](./dataTypes.md#float) or [String](./dataTypes.md#string) | | | The first addend |
| Target | [Integer](./dataTypes.md#integer) or [Float](./dataTypes.md#float) or [String](./dataTypes.md#string) | | | The second addend |
| Sum | [Variable](./variables.md) | ✓ | | The sum of the two addend |

Returns: [Integer](./dataTypes.md#integer) or [Float](./dataTypes.md#float) or [String](./dataTypes.md#string)

Example:

```xt
add 5 10 sum
out sum
```

---

### Call

```xt
call <section> [...arguments] <output>
```

Adds two addends together.

| Parameter | Type | Optional | Default | Description |
| :-: | :-: | :-: | :-: | :-: |
| Section | [Section](./sections.md) | | | The target section |
| ...Arguments | ...Any | ✓ | | The arguments passed to the target section |
| Output | [Variable](./variables.md) | | | The output of the section |

Returns: Any

Example:

```xt
add 5 10 sum
out sum
```