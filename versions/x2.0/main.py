"""
X2 - A minimalistic, lightweight, function-based programming language
Inspired by Assembly, Batch, and Bash.

Copyright (c) 2022 iiPython
"""

# Modules
import os
import re
import sys
from typing import Any

# Exceptions
class UnknownCommand(Exception):
    pass

class MissingArguments(Exception):
    pass

class UnreferencedSection(Exception):
    pass

class PackageNotFound(Exception):
    pass

# Executor
class XCommands:
    def out(mem, args: list) -> None:
        print(*args)

    def jmp(mem, args: list) -> None:
        if not args:
            raise MissingArguments("missing section to jump to")

        mem.xps.jump_section(args[0])

    def psh(mem, args: list) -> None:
        if not len(args) > 1:
            args.append("-")

        mem.vars[args[-1]] = args[0]

    def pop(mem, args: list) -> Any:
        return mem.vars[(args or ["-"])[0]]

    def add(mem, args: list) -> int:
        args += ["-" * (3 - len(args))]
        n1, n2 = args[0], args[1]
        if n1 in mem.vars:
            n1 = mem.vars[n1]

        if n2 in mem.vars:
            n2 = mem.vars[n2]
        mem.vars[args[2]] = n1 + n2
        return mem.vars[args[2]]

    def sub(mem, args: list) -> int:
        args += ["-" * (3 - len(args))]
        n1 = args[0]
        n2 = args[1]
        if n1 in mem.vars:
            n1 = mem.vars[n1]

        if n2 in mem.vars:
            n2 = mem.vars[n2]

        mem.vars[args[2]] = n1 - n2
        return mem.vars[args[2]]

    def mult(mem, args: list) -> int:
        args += ["-" * (3 - len(args))]
        n1 = args[0]
        n2 = args[1]
        if n1 in mem.vars:
            n1 = mem.vars[n1]

        if n2 in mem.vars:
            n2 = mem.vars[n2]

        mem.vars[args[2]] = n1 * n2
        return mem.vars[args[2]]

    def div(mem, args: list) -> int:
        args += ["-" * (3 - len(args))]
        n1 = args[0]
        n2 = args[1]
        if n1 in mem.vars:
            n1 = mem.vars[n1]

        if n2 in mem.vars:
            n2 = mem.vars[n2]

        mem.vars[args[2]] = n1 / n2
        return mem.vars[args[2]]

    def evl(mem, args: list) -> None:
        v1, v2, op, cmd = args[0], args[2], args[1], args[3]
        if v1 in mem.vars:
            v1 = mem.vars[v1]

        if v2 in mem.vars:
            v2 = mem.vars[v2]

        cmdelse = None
        if len(args) > 4:
            cmdelse = args[4]

        if {
            "==": lambda v1, v2: v1 == v2,
            "!=": lambda v1, v2: v1 != v2,
            ">": lambda v1, v2: v1 > v2,
            "<": lambda v1, v2: v1 < v2,
            "<=": lambda v1, v2: v1 <= v2,
            ">=": lambda v1, v2: v1 >= v2
        }[op](v1, v2):
            mem.xin.runline(mem.xps.parse_line(cmd))

        elif cmdelse is not None:
            mem.xin.runline(mem.xps.parse_line(cmdelse))

    def read(mem, args: list) -> str:
        var = args[1] if len(args) > 1 else None
        val = input(args[0] if args else "")
        if var is not None:
            mem.vars[var] = val

        return val

    def num(mem, args: list) -> int:
        for arg in args:
            mem.vars[arg] = int(mem.vars[arg])
        
        return mem.vars[arg]

    def imp(mem, args: list) -> None:
        if not args:
            raise MissingArguments("missing package path")

        fp = args[0] if "." in args[0] else args[0] + ".xt"
        parser = XParser()
        parser.parse_file(fp)
        del parser._sections["global"]
        mem.xps._sections = {**mem.xps._sections, **parser._sections}

    def cls(mem, args: list) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def lwr(mem, args: list) -> None:
        mem.vars[args[0]] = mem.vars[args[0]].lower()

    def brk(mem, args: list) -> None:
        sys.exit((args or [0])[0])

class XMemory(object):
    def __init__(self) -> None:
        self.vars = {}

class XInterpreter(object):
    def __init__(self, parser) -> None:
        self.parser = parser
        self.commands = {k: getattr(XCommands, k) for k in dir(XCommands) if callable(getattr(XCommands, k)) and not k[0] == "_"}

        # Memory initialization
        self.memory = XMemory()
        self.memory.xin = self
        self.memory.xps = self.parser

    def runlines(self, lines: list) -> None:
        [self.runline(ln) for ln in lines]

    def runline(self, line: tuple) -> Any:
        cmd, args = line
        if cmd not in self.commands:
            raise UnknownCommand(cmd)

        nargs = []
        for arg in args:
            if isinstance(arg, str):
                for item in self.parser.expr_rgx.findall(arg):
                    arg = arg.replace(item, str(self.runline(self.parser.parse_line(item[2:][:-1])))).replace("\\'", "\"")

            nargs.append(arg)

        return self.commands[cmd](self.memory, nargs)

# Parser
class XParser(object):
    def __init__(self) -> None:
        self._sections = {"global": []}

        self.executor = XInterpreter(self)
        self.expr_rgx = re.compile(r"\$\([^)]*\)")

    def parse_file(self, filepath: str) -> None:
        if not os.path.isfile(filepath):
            raise PackageNotFound(filepath)

        with open(filepath, "r") as file:
            rawlines = [ln.strip() for ln in file.read().splitlines() if ln.strip()]

        active_section = "global"
        for line in rawlines:
            cmd, args = self.parse_line(line)
            if cmd[0] == ":":
                section = cmd[1:]
                active_section = section
                self._sections[section] = []

            elif cmd == "cmnt":
                continue

            elif active_section:
                self._sections[active_section].append((cmd, args))

        self.jump_section("global")

    def parse_line(self, line: str) -> tuple:
        if line[:2] == "::":
            return ("cmnt", "")

        dt = {"quote": False, "str": "", "args": [], "expr": False}
        for char in line:
            if dt["quote"]:
                if char == "\"":
                    dt["args"].append(dt["str"])
                    dt["quote"] = False
                    dt["str"] = ""

                else:
                    dt["str"] += char

            elif char == "\"":
                dt["quote"] = True

            else:
                if char == " ":
                    if dt["str"]:
                        dt["args"].append(dt["str"])

                    dt["str"] = ""

                else:
                    dt["str"] += char

        if dt["str"]:
            dt["args"].append(dt["str"])

        return (dt["args"][0], self.format_args(dt["args"][1:]))

    def jump_section(self, section: str) -> list:
        if section not in self._sections:
            raise UnreferencedSection(section)

        self.executor.runlines(self._sections[section])

    def format_args(self, args: list) -> list:
        newargs = []
        for a in args:
            try:
                a = int(a)

            except ValueError:
                pass

            # Argument reconstructor
            newargs.append(a)

        return newargs

# Execution handler
parser = XParser()
parser.parse_file(sys.argv[1] if len(sys.argv) > 1 else "main.xt")
parser.jump_section("main")