"""Reviewer: Python in Your Local Environment

This file is Python code with study notes in comments. Run it as a script,
then use the terminal and REPL examples in the comments for practice.
"""

# INSTALLING PYTHON
# Download the installer for Windows, macOS, or Linux from the official site:
# https://www.python.org/
# After installing, open a terminal and check that Python starts with `python`.

# TERMINAL
# A terminal is a text-based interface where you type commands for your
# computer. Examples of terminal apps:
#   Windows: Command Prompt or PowerShell
#   macOS:   Terminal
#   Linux:   a terminal app such as GNOME Terminal or Console

# IDE / CODE EDITOR
# IDE means Integrated Development Environment. It can combine a code editor,
# testing tools, a terminal, and other development features.
# Popular options for Python include VS Code, PyCharm, and Spyder.

# RUNNING A PYTHON FILE
# In VS Code, the Run button (a play icon, usually near the upper-right) can
# run the current Python file in the terminal.
#
# You can also open a terminal and change directory to the folder containing
# your file. For example, if main.py is inside python-projects:
#
#   cd python-projects
#   python main.py
#
# `cd` means change directory. Run `python main.py` from the folder where
# main.py is saved. If Python is installed as `python3` on your system, use:
#
#   python3 main.py


# INTERACTIVE PYTHON SHELL (REPL)
# Start it from a terminal by typing `python` and pressing Enter. The `>>>`
# prompt means Python is ready for one command. Try this at the >>> prompt:
#
#   >>> print('Hello, world!')
#   Hello, world!
#   >>>
#
# REPL means Read, Evaluate, Print, Loop:
#   1. Read the command you typed.
#   2. Evaluate (run) that command.
#   3. Print its result, when there is one.
#   4. Loop back to >>> so you can enter another command.

# Here is a tiny example of Python code that can be saved in a .py file and
# run from a terminal with `python reviewer1.py`:
def greet(name):
    """Return a greeting for the given name."""
    return f'Hello, {name}!'


if __name__ == '__main__':
    print(greet('world'))

score = 100
print(f' My score is {score}%')