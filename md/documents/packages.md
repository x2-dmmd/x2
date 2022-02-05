# [x2](../../README.md) / [Documents](../documents.md) / Package

## Table of Contents

- [Home](../../README.md)
- [Tutorials](../tutorials.md)
- [Documents ▾](../documents.md)
    - [About](../documents.md#about)
    - [Documents ▾](../documents.md#documents)
        - [Comments](./comments.md)
        - [Comparators](./comparators.md)
        - [Configurations](./configurations.md)
        - [Data Types](./dataTypes.md)
        - [Operators](./operators.md)
        - **Packages ▾**
            - [About](#about)
        - [Python API](./pythonAPI.md)
        - [Sections](./sections.md)
        - [Variables](./variables.md)
- [Standard Library](../standardLibrary.md)

## About

Packages are x2 files written by other people that can be imported to your x2 project using the `imp` operator:

```
imp "stdlib"
```

All packages are located in the `pkg/` folder. If one is not found, the interpreter will automatically create one. When attempting to import a package, the interpreter will look for the `pkg/<package>/main.xt` file. If one is not found, an error is thrown.