# "Hello, World!" Example

[**← Back**](tutorials.md#tutorials) | [**← Return To Home Page**](../../README.md#x2)

## Table of Contents
- [**Introduction**](#introduction)
- [**The Basics**](#the-basics)
- [**First Program**](#first-program)

## Introduction

Welcome to the "Hello, World!" tutorial! In this lesson, you will learn how to use the `out` operator and how to output a value into the terminal. You will also learn how to manipulate `strings` and `numbers`, as well as learning how to define `variables`.

## The Basics

First, we will learn how an x2 program is structred. Below is the most basics x2 program:

```xt
:main
    out "Hello, World!"
```

This simple program simply outputs `"Hello, World!"` into the terminal. Let's break it down and see how it works.

The first line of our program defines a section in which our code is executed. You will learn about `sections` in a later lesson.

The second line our program then tells the program to output a `string` with the value `"Hello, World!` into the terminal.

The instruction consists of two parts, the operator and the arguments. The operator is an action which the program will execute. In this case, the `out` operator outputs everything after it into the terminal. The arguments are information that the operator then uses to do certain tasks. In this example `"Hello, World!"` is the argument for this instruction. It tells the `out` operator that this is the content that needs to be outputted.

You can output more than just `"Hello, World!"`. By changing the contents within the double quotes (`"`), you can output anything that you want into the terminal:

```
:main
    out "My name is Bob"
```

Of course, we can output numbers as well. By removing the double quotes (`"`) and replacing it with a number, you can output any numbers you want into the terminal:

```
:main
    out 5
```

## Variables

You can also store values inside variables. Variables are labels that represent a value. 

You can define a variable by typing the following below:

```
psh 5 myVariable
```

Like-wise, this instruction also consists of two parts, the operator and the arguments. The `psh` operator defines a variable within the program memory. The first argument is the actual `value` that the variable represents. The second argument is the `label` or the `name` of the variable.

A variable name in x2 can have contain any character besides double quotes and spaces. However, it can only start with an English letter (`a-z` or `A-Z`) or a hyphon (`-`).

You can then reference a variable by simply rewriting the variable name:

```
out myVariable
```

> Note: When referencing a variable, do not surround it with double quotes (`"`).

A variable can also be used multiple times, which can be helpful when a certain value is used over and over throughout the program.

Let's see how we can incorporate variables into our program!

```
:main
    psh 5 a
    out a
```

The first line of our program defines a section. The second line of our program defines the variable `a` with the value `5`. The third line then outputs the variable into the terminal.

## Footer

Last Updated: `Jan. 22nd, 2022` <br>
Document Written by `Dm123321_31mD`

[**↑ Go To Top**](#"hello,-world!"-example)