"""Dictionaries, Sets, Standard Library, and Regex Review

Run this file to see the examples. Error examples are comments so they do not
interrupt execution.
"""

import datetime
import math
import math as m
import random
import re
from math import cos, radians, sin


# 1. Dictionaries
# Dictionaries store key-value pairs. Keys must be unique and hashable;
# values can repeat and can be any type. Modern dictionaries keep insertion order.
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}
print('Pizza:', pizza)

# dict() can build a dictionary from a sequence of (key, value) tuples.
pizza_from_pairs = dict([
    ('name', 'Margherita Pizza'),
    ('price', 8.9),
    ('calories_per_slice', 250),
    ('toppings', ['mozzarella', 'basil'])
])
print('Built with dict():', pizza_from_pairs)

# Bracket notation reads a value, updates an existing key, or adds a new key.
print('Name:', pizza['name'])
pizza['name'] = 'Margherita'       # Update an existing value.
pizza['total_time'] = 25           # Add a new key-value pair.
print('Updated pizza:', pizza)
# pizza['missing']  # KeyError if a key is absent.

# A dictionary's keys can be strings, numbers, or tuples of hashable values.
# A tuple containing a list cannot be used as a key because lists are mutable.
key_examples = {1: 'number key', ('x', 'y'): 'tuple key'}
print('Valid key examples:', key_examples)
# invalid_keys = {('x', [1, 2]): 'not hashable'}  # TypeError

# ** unpacks a dictionary into keyword arguments. Key names must match params.
def greet(name, age):
    print(f'{name} is {age}')


greeting_data = {'name': 'Jessica', 'age': 30}
greet(**greeting_data)

# all() is True only if every item is truthy. Empty iterables also return True.
print('all truthy:', all([1, 'a', True]))
print('one falsy:', all([1, 0, True]))
print('empty iterable:', all([]))


# 2. Common dictionary methods
# get(key, default) avoids KeyError for a missing key.
print('Toppings:', pizza.get('toppings', []))
print('Missing value:', pizza.get('allergens', 'Not specified'))

# keys(), values(), and items() return views that reflect dictionary contents.
print('Keys:', pizza.keys())
print('Values:', pizza.values())
print('Items:', pizza.items())

# pop(key, default) removes a key and returns its value. Without a default,
# a missing key raises KeyError.
pop_example = {'name': 'Margherita', 'price': 8.9}
print('Popped price:', pop_example.pop('price'))
print('Missing key default:', pop_example.pop('total_price', 10))
# pop_example.pop('total_price')  # KeyError

# popitem() removes and returns the last inserted pair (Python 3.7+).
popitem_example = {'name': 'Margherita', 'price': 8.9, 'total_time': 25}
print('Removed pair:', popitem_example.popitem())

# update() overwrites shared keys and adds new keys.
update_example = {'apple': 10, 'pear': 20}
update_example.update({'apple': 8, 'plum': 12})
print('After update:', update_example)

# clear() removes all pairs.
clear_example = {'name': 'Margherita', 'price': 8.9}
clear_example.clear()
print('After clear:', clear_example)


# 3. Looping over dictionaries
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70
}

# values() visits values; keys() or the dictionary itself visits keys.
for price in products.values():
    print('Price:', price)

for product in products.keys():
    print('Product:', product)

for product in products:
    print('Key from direct loop:', product)

# items() gives key-value tuples. Unpack each tuple into two loop variables.
for product, price in products.items():
    print(product, price)

# Updating existing values while looping over items is fine; don't add or
# remove keys while iterating over the same dictionary.
discounted_products = products.copy()
for product, price in discounted_products.items():
    discounted_products[product] = round(price * 0.8)
print('Discounted products:', discounted_products)

# enumerate() adds a counter (0 by default); its optional start sets another.
for index, product_pair in enumerate(products.items()):
    print(index, product_pair)

for index, product_pair in enumerate(products.items(), 1):
    print(index, product_pair)


# 4. Sets
# Sets are mutable, unordered collections of unique hashable elements.
my_set = {1, 2, 3, 4, 5}
duplicate_set = {1, 2, 2, 3, 3}
print('Set:', my_set)
print('Duplicates removed:', duplicate_set)

# set() creates an empty set; {} creates an empty dictionary.
empty_set = set()
empty_dict = {}
print('Empty set:', empty_set)
print('Empty dictionary:', empty_dict)

# set(iterable) builds a set from an iterable, removing duplicates.
print('From list:', set([1, 2, 2, 3]))
expected_keys = {'name', 'age'}
person_data = {'name': 'Jessica', 'age': 30}
print('Expected keys match:', set(person_data) == expected_keys)

# Add and remove elements. remove() raises KeyError if missing; discard() does not.
mutable_set = {1, 2, 3, 4, 5}
mutable_set.add(6)
mutable_set.add(5)  # Duplicate has no effect.
mutable_set.remove(4)
mutable_set.discard(99)
print('After add/remove:', mutable_set)
# mutable_set.remove(99)  # KeyError
mutable_set.clear()
print('After clear:', mutable_set)

# Set relationships and operations.
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}
print('Subset:', your_set.issubset(my_set))
print('Superset:', my_set.issuperset(your_set))
print('Disjoint:', my_set.isdisjoint(your_set))
print('Union |:', my_set | your_set)
print('Intersection &:', my_set & your_set)
print('Difference -:', my_set - your_set)
print('Symmetric difference ^:', my_set ^ your_set)

# Compound operators update the left-hand set in place.
compound_set = {1, 2, 3}
compound_set |= {3, 4}          # Union
compound_set &= {2, 3, 4, 5}    # Intersection
compound_set -= {4}             # Difference
compound_set ^= {3, 5}          # Symmetric difference
print('After compound operations:', compound_set)
print('2 is in the set:', 2 in compound_set)


# 5. Python standard library and imports
# The standard library provides reusable modules for common tasks, such as
# math, random, regular expressions (re), and dates (datetime).
print('Square root:', math.sqrt(36))
print('Pi:', math.pi)
print('Random die roll:', random.randint(1, 6))

# An alias gives an imported module a shorter or alternative name.
print('Square root using alias:', m.sqrt(49))

# Import selected functions to call them without the module prefix.
angle_radians = radians(40)
print('Sine:', sin(angle_radians))
print('Cosine:', cos(angle_radians))

# Wildcard imports are generally discouraged: they can cause name collisions
# and make it harder to know where a name came from.
# from math import *

# datetime.date creates a date object; its fields are accessed with dot notation.
birthday = datetime.date(1959, 7, 15)
print('Birthday:', birthday)
print('Day, month, year:', birthday.day, birthday.month, birthday.year)


# 6. The __name__ == '__main__' idiom
# When run directly, a module's __name__ is '__main__'. When imported, it is
# set to the module name. Put code you want to run only directly under this guard.
def show_main_message():
    print('This code runs when the file is executed directly.')


if __name__ == '__main__':
    show_main_message()


# 7. Regular expressions (regex)
# Regex patterns describe text to match. Import re to use regex functions.
# search() looks anywhere in the string; it returns a Match object or None.
search_result = re.search('cat', 'The cat sat on the mat.')
print('Search result:', search_result)
print('Matched text:', search_result.group())
print('Match span:', search_result.span())
print('No match:', re.search('dog', 'The cat sat.'))

# By default matching is case-sensitive; IGNORECASE enables case-insensitive matching.
print('Case-insensitive:', re.search('CAT', 'The cat sat.', re.IGNORECASE))

# Raw strings make regex backslashes easy to write. Common sequences:
# \d digit, \w word character, \s whitespace; uppercase versions match opposites.
print('Digits:', re.search(r'\d+', 'Room 42B'))
print('Word characters:', re.findall(r'\w+', 'Hello, Python 3!'))
print('Whitespace:', re.search(r'\s', 'hello world'))

# Quantifiers: + one or more, * zero or more, ? zero or one, {n} exactly n,
# and {n,m} between n and m repetitions.
print('Optional u:', re.search(r'colou?r', 'color'))
print('Four digits:', re.search(r'\d{4}', 'Room 1987'))

# re.match() checks at the start; fullmatch() requires the whole string to match.
print('Match at start:', re.match(r'\d+', '42 apples'))
print('No start match:', re.match(r'\d+', 'apples: 42'))
print('Whole string match:', re.fullmatch(r'\d+:\d+', '10:30'))
print('Whole string fails:', re.fullmatch(r'\d+:\d+', '10:30pm'))

# findall() returns all matches. sub() replaces matches; count is passed by name.
print('All numbers:', re.findall(r'\d+', 'Rooms 12, 7, and 105'))
print('Redacted:', re.sub(r'\d', '*', '555 0123', count=3))

# My Score
score = 100
print(f' My score is {score}%')