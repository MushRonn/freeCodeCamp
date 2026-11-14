# Reviewer for Error Handling in Python

# COMMON PYTHON ERRORS
# --------------------
# SyntaxError: code does not follow Python's grammar.
# Example: print("Hello"  # Missing closing parenthesis.
#
# NameError: a variable or function name has not been defined.
# Example: print(username)  # No variable named username was created.
#
# TypeError: an operation is used with an incompatible type.
# Example: 5 + "5"  # A number cannot be added directly to a string.
#
# IndexError: an index is outside a sequence's valid range.
# Example: [10, 20][5]
#
# AttributeError: an object does not have the requested method or attribute.
# Example: "hello".append("!")  # Strings do not have append().


# DEBUGGING TECHNIQUES
# --------------------
# print() and f-strings quickly show the values and flow of a program.
def add(a, b):
    result = a + b
    print(f'Debug: a={a}, b={b}, result={result}')
    return result


add(3, 4)

# pdb is Python's built-in interactive debugger. Uncomment to try it in a
# terminal; set_trace() pauses the program and opens a (Pdb) prompt.
# import pdb
# pdb.set_trace()
# Useful commands: help, whatis expression, p expression, n, s, c, q.
#
# IDE debuggers (such as VS Code) support breakpoints and variable inspection.
# F5: continue; F10: step over; F11: step into; Shift+F11: step out.


# EXCEPTION HANDLING
# ------------------
# Put code that might fail in try, then handle a particular error in except.
try:
    result = 22 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Separate except blocks can give different errors useful responses.
user_text = 'not an integer'
try:
    number = int(user_text)
    result = 22 / number
except ZeroDivisionError:
    print('You cannot divide by zero!')
except ValueError:
    print('Please enter a valid integer!')

# One except clause can handle several exception types using a tuple.
user_text = '0'
try:
    number = int(user_text)
    result = 10 / number
except (ValueError, ZeroDivisionError) as error:
    print(f'Error occurred: {error}')

# `as error` gives a name to the exception object and its message.
try:
    value = int('not a number')
except ValueError as error:
    print(f'Caught an error: {error}')

# else runs only when try succeeds; finally always runs.
try:
    result = 100 / 4
except ZeroDivisionError:
    print('You cannot divide by zero!')
else:
    print(f'Result is {result}')
finally:
    print('Execution complete!')


# THE raise STATEMENT
# -------------------
# raise manually triggers an exception when a rule is broken.
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('You cannot divide by zero')
    return a / b


try:
    divide(10, 0)
except ZeroDivisionError as error:
    print(f'Division failed: {error}')

# Bare `raise` inside an except block re-raises the current exception.
def process_data(data):
    try:
        return int(data) * 2
    except ValueError:
        print('Logging: invalid data received')
        raise


try:
    process_data('abc')
except ValueError:
    print('The caller handled the invalid data.')

# ASSERTIONS AND REQUIRED VALIDATION
# assert checks a debugging assumption and raises AssertionError if false.
# Python can remove assertions in optimized mode (-O), so use if/raise for
# input checks that must always run.
def square_root(number):
    if number < 0:
        raise ValueError('Number cannot be negative')
    return number ** 0.5


try:
    square_root(-4)
except ValueError as error:
    print(f'Invalid input: {error}')


# CUSTOM EXCEPTIONS
# -----------------
# Create a domain-specific exception by inheriting from Exception.
class InvalidCredentialsError(Exception):
    pass


def login(username, password):
    if username != 'admin' or password != 'example-password':
        raise InvalidCredentialsError('Invalid username or password')
    return f'Welcome, {username}!'


try:
    login('visitor', 'wrong')
except InvalidCredentialsError as error:
    print(f'Login failed: {error}')


# EXCEPTION CHAINING
# ------------------
# `raise NewError(...) from error` records the original exception as the cause.
# `from None` suppresses the original exception context in the traceback.
def parse_config_text(text):
    try:
        return int(text)
    except ValueError as error:
        raise ValueError('Invalid configuration format') from error


try:
    parse_config_text('not a number')
except ValueError as error:
    print(f'Configuration error: {error}')


def report_missing_config():
    try:
        raise FileNotFoundError('settings file not found')
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None


try:
    report_missing_config()
except ValueError as error:
    print(f'Configuration error: {error}')

# My Score
score = 95
print(f' My score is {score}%')