"""Python Basics reviewer

Run this file to review the examples. Explanations are kept in comments so
this remains a Python code file and can be used as a quick study reference.
"""

# 1. Variables, naming, comments, and printing
# Names start with a letter or underscore, can contain letters/numbers/_ ,
# are case-sensitive, and cannot be Python keywords. Use descriptive snake_case.
name = 'John Doe'
age = 25
print('Name:', name, '| Age:', age)  # print separates arguments with spaces

# Python chooses the type from the assigned value (dynamic typing).
whole_number = 10
decimal_number = 4.5
word = 'hello'
is_ready = True
print(type(whole_number), type(decimal_number), type(word), type(is_ready))
print(isinstance(whole_number, int))
print(isinstance(decimal_number, (int, float)))


# 2. Strings
# Strings use single or double quotes and are immutable: operations return
# new strings. Reassignment changes what a variable refers to.
greeting = 'Hello world'
print(greeting[0], greeting[6], greeting[-1])  # indexing; negative counts from end
print(greeting[0:5], greeting[:5], greeting[6:])  # stop index is excluded
print(greeting[::2], greeting[::-1], greeting[:])  # step, reverse, whole string
print(len(greeting))
print('Hello' in greeting, 'goodbye' in greeting)

# Quote styles, escaping, and multiline strings
quoted = "It's a sunny day"
escaped_quote = 'She said, \'Hello!\''
multiline = '''First line
Second line'''
print(quoted)
print(escaped_quote)
print(multiline)

# Concatenation, repetition, conversion, and f-strings
first_name = 'Jessica'
print('My name is ' + first_name + '.')
print('ha' * 3)
years = 26
print('Age: ' + str(years))  # a string and a number cannot be concatenated directly
print(f'My name is {first_name}. In two years I will be {years + 2}.')

# Common string methods: each returns a new value; the original is unchanged.
messy_text = '  hello world  '
print(messy_text.upper())
print(messy_text.lower())
print(messy_text.strip())
print('hello world'.replace('hello', 'hi'))
print('one-two-three'.split('-'))
print(' '.join(['one', 'two', 'three']))
print('Jessica'.startswith('J'), 'Jessica'.endswith('a'))
print('Los Angeles'.find('Angeles'), 'Los Angeles'.find('New'))  # -1 means not found
print('Los Angeles'.count('e'))
print('chocolate cake'.capitalize(), 'los angeles'.title())
print('HELLO'.isupper(), 'hello'.islower())

# str.maketrans creates a character mapping; translate applies it.
translation_table = str.maketrans('abc', '123')
print('abcabc'.translate(translation_table))


# 3. Integer and float operations
number_a = 56
number_b = 12
float_a = 5.4
float_b = 12.0
print(number_a + number_b, number_a - number_b)
print(number_a * number_b, number_a / number_b)
print(float_a + number_a)  # combining int and float produces a float
print(number_a % number_b)  # remainder
print(number_a // number_b)  # floor division
print(4 ** 2)  # exponentiation
print(float(4), int(4.9), round(3.4), round(7.7), abs(-13), pow(2, 3))

# Augmented assignment updates a variable using its current value.
score = 10
score += 5
score -= 2
score *= 2
score /= 2
score //= 3
score %= 2
score **= 3
print('score:', score)


# 4. Functions, parameters, return values, and built-ins
def get_sum(num_1, num_2):
    """Return the sum of two inputs."""
    return num_1 + num_2


def add_with_default(num_1, num_2=2):
    return num_1 + num_2


def greet():
    print('hello')  # printing displays a value; it does not return it


print(get_sum(3, 4))
print(add_with_default(3), add_with_default(3, 4))
greet_result = greet()
print('A function with no return gives:', greet_result)  # None

# input() waits for a user. Uncomment these lines to try it interactively:
# user_name = input('What is your name? ')
# print('Hello', user_name)

# int() converts supported values to integers (a float is truncated).
print(int(3.14), int('42'), int(True), int(False))


# 5. Scope
# Function parameters and variables created inside a function are local.
tax_rate = 0.70  # global variable


def get_total(subtotal):
    total = subtotal + subtotal * tax_rate
    return total


print(get_total(100))


# 6. Comparisons and conditionals
print(3 == 4, 3 != 4)
print(3 > 4, 3 < 4, 3 >= 3, 3 <= 4)

person_age = 16
if person_age >= 18:
    print('You are an adult')
elif person_age >= 13:
    print('You are a teenager')
else:
    print('You are a child')

# Nested if statements check a second condition only inside the first.
is_citizen = True
voter_age = 25
if is_citizen:
    if voter_age >= 18:
        print('Eligible to vote')
else:
    print('Not a citizen')


# 7. Truthy/falsy values and Boolean operators
# Common falsy values include None, False, 0, 0.0, and ''. Most other values
# (including nonzero numbers and nonempty strings) are truthy.
print(bool(None), bool(False), bool(0), bool(0.0), bool(''))
print(bool(True), bool(1), bool('Hello'))

# `not` inverts truthiness. `and`/`or` short-circuit and return an operand.
print(not '', not 'Hello', not 0, not 1)
print(True and 'both conditions are truthy')
print(0 and 'unreached')  # stops at the first falsy operand: 0
print('first truthy value' or 'fallback')  # stops at the first truthy operand

is_employed = False
is_student = True
discount_age = 19
if discount_age < 18 or is_student:
    print('Eligible for a student discount')
if is_citizen and voter_age >= 18:
    print('Eligible to vote based on both conditions')
if not is_employed:
    print('Currently not employed')

# MY QUIZ RESULT!
result = 100

print(f' My Python Basic Quiz Grade is = {result}')