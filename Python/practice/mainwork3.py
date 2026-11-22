# Understanding Error Handling in Python
#This file contains only lessons and not actual codes, most of the code is commented out. The lessons are in the comments.


# Common Python Errors
# These examples deliberately cause errors inside try/except blocks, so the
# whole file can continue running and show each error message.


def show_error(error_name, example):
    try:
        example()
    except Exception as error:
        print(f'{error_name}: {type(error).__name__}: {error}')


# SyntaxError: Python cannot parse code with invalid syntax. exec() lets this
# example be caught at runtime instead of stopping this file while it loads.
def syntax_error_example():
    exec('print("Hello, world!"')  # Missing closing parenthesis.


show_error('Syntax example', syntax_error_example)

# NameError: the name has not been defined.
def name_error_example():
    exec('print(variable_that_does_not_exist)')


show_error('Name example', name_error_example)

# TypeError: the operation does not support these different types.
show_error('Type example', lambda: 5 + '5')

# IndexError: the requested list index is outside its valid range.
my_list = [1, 2, 3]
show_error('Index example', lambda: my_list[5])

# AttributeError: this type does not have the requested method.
show_error('Attribute example', lambda: (42).append(5))

# Debugging tip: read the exception type and message, then check the line
# named in the traceback. It often points to the kind of mistake to fix.


# Debugging Techniques
# Debugging means finding and fixing errors by examining code flow and values.

# 1. Print statements and f-strings
# Print variable values at useful points to check whether the code is behaving
# as expected. Remove or reduce temporary debug prints when they are no longer
# needed.
def add_with_debug(a, b):
    result = a + b
    print(f'Adding {a} and {b} gives {result}')
    return result


sum_result = add_with_debug(3, 4)
print('Returned sum:', sum_result)


# 2. Interactive debugging with pdb
# pdb.set_trace() pauses execution and opens a (Pdb) prompt. From there, inspect
# values, step through the function, or continue execution.
# Uncomment this example and run it in a terminal to try pdb interactively:
# import pdb
#
# def divide_with_pdb(a, b):
#     pdb.set_trace()
#     return a / b
#
# print(divide_with_pdb(10, 2))
#
# Useful pdb commands:
#   help       Show available commands.
#   whatis a   Show the type of a.
#   p a        Print the value of a.
#   n          Run the next line without entering called functions.
#   s          Step into a called function.
#   c          Continue until the next breakpoint or program end.
#   q          Quit the debugger.


# 3. IDE debugging tools
# In VS Code, click the gutter beside a line number to set a breakpoint, then
# press F5 and choose Python File if asked. The program pauses at the breakpoint.
# Inspect values in the Variables panel or evaluate expressions in Debug Console.
#
# Common VS Code debugger keys:
#   F5          Continue until the next breakpoint.
#   F10         Step over the current line.
#   F11         Step into a function call.
#   Shift + F11 Step out of the current function.


# Choosing a debugging technique:
#   print()     Quick checks of values and program flow.
#   pdb         Interactive debugging in the terminal.
#   IDE tools   Visual breakpoints, stepping, and variable inspection.


# Exception Handling
# Exception handling lets a program respond to runtime errors instead of
# stopping unexpectedly.

# try contains code that might raise an exception; except handles a matching
# exception type.
try:
    division_result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# else runs only if the try block finishes without an exception. finally runs
# whether or not an exception occurred, so it is useful for cleanup.
try:
    division_result = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('Division successful:', division_result)
finally:
    print('This block always runs.')

# Separate except blocks allow different responses for different errors.
try:
    number = int('abc')
    division_result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")

# Use `as` to bind the exception object to a variable and inspect its message.
try:
    division_result = 1 / 0
except ZeroDivisionError as error:
    print(f'Error occurred: {error}')

# One except clause can handle several exception types by listing them in a tuple.
# A fixed string is used instead of input() so this example runs without prompts.
user_entry = '0'
try:
    number = int(user_entry)
    division_result = 10 / number
except (ValueError, ZeroDivisionError) as error:
    print(f'Input or calculation error: {error}')


# The raise statement
# Use raise to trigger an exception when a condition violates a rule.
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age


# Catch the ValueError so this reviewer can continue running.
try:
    check_age(-5)
except ValueError as error:
    print(f'Age check failed: {error}')


# Bare `raise` inside an except block re-raises the same exception. This lets
# you log or handle something locally while allowing a caller to catch it too.
def process_data(data):
    try:
        return int(data) * 2
    except ValueError:
        print('Logging: invalid data received')
        raise


try:
    process_data('abc')
except ValueError:
    print('The caller handled the ValueError.')


# A custom exception can give a specific error a meaningful name and message.
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f'Insufficient funds: ${balance} available, ${amount} requested'
        )


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


try:
    remaining_balance = withdraw(100, 150)
except InsufficientFundsError as error:
    print(f'Transaction failed: {error}')


# Exception chaining preserves the original error as context. `from error`
# says the new error was caused by the caught one; `from None` hides that
# context when it is not useful to show.
def parse_config_text(config_text):
    try:
        return int(config_text)
    except ValueError as error:
        raise ValueError('Invalid configuration format') from error


try:
    parse_config_text('not a number')
except ValueError as error:
    print(f'Configuration error: {error}')


def missing_config():
    try:
        raise FileNotFoundError('settings file not found')
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None


try:
    missing_config()
except ValueError as error:
    print(f'Configuration error: {error}')


# For required input validation, use an explicit condition and raise. An
# assert raises AssertionError when false, but Python may remove asserts with
# optimization enabled, so do not rely on assert for essential validation.
def calculate_square_root(number):
    if number < 0:
        raise ValueError('Cannot calculate square root of a negative number')
    return number ** 0.5


try:
    square_root = calculate_square_root(-4)
except ValueError as error:
    print(f'Invalid input: {error}')
