# [x2](../../README.md) / [Documents](../documents.md) / Comparators

## Table of Contents

- [Home](../../README.md)
- [Tutorials](../tutorials.md)
-  [Documents](../documents.md)
    - [About](../documents.md#about)
    - [Sections](../documents.md#about)
        - **Comparators ▾**
            - [About](#about)
            - [Expressions](#expressions)
            - [Documentation](#documentation)
        - [Configurations](./documents/configurations.md)
        - [Data Types](./documents/dataTypes.md)
        - [Operators](./documents/operators.md)
        - [Packages](./documents/packages.md)
        - [Python API](./documents/pythonAPI.md)
        - [Sections](./documents/sections.md)
        - [Variables](./documents/variables.md)

## About

Comparators are symbols or keywords that compare two different variables or values and trigger a branch in the x2 thread. Each comparator has their own functionality.


## Expressions

Expressions are segments in the code that creates a branch in the x2 thread. They are always made up of three components: the `source`, the `comparator`, and the `target` are arranged like so:

```
<source> <comparator> <target>
```

For example:

```
5 == 5
```

Or:

```
"hello" in "hello world"
```
 
An expression cannot be used on its own, as it is not considered as an operator and thus not a valid statement. It is always accompanied by operators that take an expression as an argument. A classic example of this is the `cmp` operator:

```
cmp 5 == 5 "out \"yes\""
```

Any operator that uses an expression creates a branch, with `true` being the first branch and `false` being the second. For example, the `cmp` operator creates a branch based on whether or not the expression is true:

```
cmp 5 == 10 "out \"same\"" "out \"different\""
```

## Documentation

### Equal To

```
<source> == <target>
```

Checks if the two variables or values are equal to each other.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | Any | The variable or value that is being compared against |
| Target | Any | The variable or value being compared to |

---

### Not Equal To

```
<source> != <target>
```

Checks if the two variables or values are different from each other.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | Any | The variable or value that is being compared against |
| Target | Any | The variable or value being compared to |

---

### Less Than

```
<source> < <target>
```

Checks if the source is less than the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | [String](./dataTypes.md#string) or [Integer](./dataTypes.md#integer) or [Float](./dataTypes.md#float) | The variable or value that is being compared against |
| Target | [String](./dataTypes.md#string) or [Integer](./dataTypes.md#integer) or [Float](./dataTypes.md#float) | The variable or value being compared to |

---

### Less Than or Equal To

```
<source> <= <target>
```

Checks if the source is less than or equal to the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | [String](./dataTypes.md#string) or [Integer](./dataTypes.md#integer) or [Float](./dataTypes.md#float) | The variable or value that is being compared against |
| Target | [String](./dataTypes.md#string) or [Integer](./dataTypes.md#integer) or [Float](./dataTypes.md#float) | The variable or value being compared to |

---

### Greater Than

```
<source> > <target>
```

Checks if the source is greater than the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | [String](./dataTypes.md#string) or [Integer](./dataTypes.md#integer) or [Float](./dataTypes.md#float) | The variable or value that is being compared against |
| Target | [String](./dataTypes.md#string) or [Integer](./dataTypes.md#integer) or [Float](./dataTypes.md#float) | The variable or value being compared to |

---

### Greater Than or Equal To

```
<source> >= <target>
```

Checks if the source is greater than or equal to the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | [String](./dataTypes.md#string) or [Integer](./dataTypes.md#integer) or [Float](./dataTypes.md#float) | The variable or value that is being compared against |
| Target | [String](./dataTypes.md#string) or [Integer](./dataTypes.md#integer) or [Float](./dataTypes.md#float) | The variable or value being compared to |

---

### In

```
<source> in <target>
```

Checks if the source is in the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | Any | The variable or value that is being compared against |
| Target | Any | The variable or value being compared to |

---

### Not In

```
<source> xin <target>
```

Checks if the source is not in the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | Any | The variable or value that is being compared against |
| Target | Any | The variable or value being compared to |

---

### Is

```
<source> is <target>
```

Checks if the source is a type of the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | Any | The variable or value that is being compared against |
| Target | [String](./dataTypes.md#string) | The variable or value being compared to |

---

### From

```
<source> from <target>
```

Checks if the source is an instance of the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | Any | The variable or value that is being compared against |
| Target | Any | The variable or value being compared to |

---

Last Updated: February 4th, 2022 by Dm123321_31mD

[↑ Go To Top](#x2--documents--comparators)