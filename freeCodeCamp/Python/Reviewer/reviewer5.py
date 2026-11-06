"""Python reviewer: Dictionaries

Dictionaries store key-value pairs. Use a key to look up its associated value.
Keys must be unique and hashable; values may be repeated and can be any type.
"""

# The standard library is Python's collection of reusable modules. It includes
# tools for math, randomness, regular expressions, dates, files, the OS, and more.
import datetime
import math
import math as m
import random
import re

# Import only selected names when that is more convenient. These names can
# then be used without writing the module prefix.
from math import cos, radians, sin


# 1. Create a dictionary with curly braces and key: value pairs.
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}
print('Pizza:', pizza)

# dict() can build a dictionary from key-value pairs.
pizza_from_pairs = dict([
    ('name', 'Margherita Pizza'),
    ('price', 8.9),
    ('calories_per_slice', 250),
    ('toppings', ['mozzarella', 'basil'])
])
print('Made with dict():', pizza_from_pairs)

# Strings and numbers can be keys. Tuples can be keys if their contents are
# hashable; a list cannot be a key because it can change.
example = {1: 'number key', ('x', 'y'): 'tuple key', 'items': [2, 3]}
print('Key and value examples:', example)
# invalid = {['x', 'y']: 'list keys are not allowed'}  # TypeError


# 2. Access, update, and add key-value pairs.
print('Pizza name:', pizza['name'])  # Bracket notation retrieves a value.
# pizza['missing_key']  # KeyError if bracket notation uses an absent key.

pizza['name'] = 'Margherita'         # Existing key: update its value.
pizza['total_time'] = 25             # New key: add another pair.
print('Updated name:', pizza['name'])
print('Added total time:', pizza['total_time'])

# Modern Python dictionaries preserve insertion order.
print('Keys in insertion order:', list(pizza))


# 3. get() safely reads a key, with an optional default value.
print('Toppings:', pizza.get('toppings', []))
print('Missing value default:', pizza.get('allergens', 'Not specified'))


# 4. Dictionary views: keys(), values(), and items().
# These show the dictionary's contents without making a separate copy.
print('Keys view:', pizza.keys())
print('Values view:', pizza.values())
print('Key-value pairs:', pizza.items())


# 5. Remove entries with pop(), popitem(), and clear().
pop_demo = {'name': 'Margherita', 'price': 8.9}
removed_value = pop_demo.pop('price')  # Remove key and return its value.
print('pop() returned:', removed_value)
print('After pop():', pop_demo)

# If the key is absent, pop() returns the default instead of raising KeyError.
print('Absent key with default:', pop_demo.pop('total_price', 10))
# pop_demo.pop('total_price')  # KeyError because no default was supplied.

# popitem() removes and returns the last inserted pair (Python 3.7+).
popitem_demo = {'name': 'Margherita', 'price': 8.9, 'total_time': 25}
print('popitem() returned:', popitem_demo.popitem())
print('After popitem():', popitem_demo)

# clear() removes all key-value pairs.
clear_demo = {'name': 'Margherita', 'price': 8.9}
clear_demo.clear()
print('After clear():', clear_demo)


# 6. update() adds pairs and overwrites values for keys that already exist.
update_demo = {
    'name': 'Margherita',
    'price': 8.9,
    'calories_per_slice': 250
}
update_demo.update({'price': 15, 'total_time': 25})
print('After update():', update_demo)
# The price was replaced with 15; total_time was added as a new key.


# 7. Looping over dictionary values, keys, and key-value pairs
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70
}

# values() loops over just the values.
for price in products.values():
    print('Price:', price)

# keys() loops over the keys. Looping over the dictionary itself does this too.
for product in products.keys():
    print('Product key:', product)

for product in products:
    print('Key by looping over dictionary:', product)

# items() gives each key-value pair as a tuple. You can unpack it into two
# loop variables, with the key first and the value second.
for pair in products.items():
    print('Pair tuple:', pair)

for product, price in products.items():
    print(product, price)


# 8. Updating dictionary values while looping over items
# Assigning new values to existing keys is fine while iterating over items.
# Avoid adding or removing keys while iterating over the same dictionary.
discounted_products = products.copy()
for product, price in discounted_products.items():
    discounted_products[product] = round(price * 0.8)
print('Prices after 20% discount:', discounted_products)


# 9. enumerate() with dictionary iteration
# enumerate() pairs each item with a counter that starts at 0 by default.
for index, product in enumerate(products):
    print('Key with index:', index, product)

for index, price in enumerate(products.values()):
    print('Price with index:', index, price)

# items() provides a pair for each dictionary entry; enumerate() adds the
# counter alongside that pair.
for index, product_pair in enumerate(products.items()):
    print('Indexed pair:', index, product_pair)

# The optional second argument sets a different starting count.
for index, product_pair in enumerate(products.items(), 1):
    print('Count from one:', index, product_pair)


# 10. Sets
# Sets are mutable collections of unique, unordered elements. They have no
# indexes, so access or test elements by value. Elements must be hashable.
number_set = {1, 2, 3, 4, 5}
duplicate_set = {1, 2, 2, 3, 3, 3}
print('Set:', number_set)
print('Duplicates are removed:', duplicate_set)  # Contains 1, 2, and 3 once.

# Use set() to create an empty set. {} creates an empty dictionary instead.
empty_set = set()
empty_dictionary = {}
print('Empty set:', empty_set)
print('Type of {}:', type(empty_dictionary))

# Sets can contain numbers, strings, and tuples of hashable values.
mixed_set = {42, 'Python', ('x', 'y')}
print('Mixed set:', mixed_set)
# {('x', [1, 2])}  # TypeError: a tuple with a list is not hashable.


# 11. Add and remove set elements
mutable_set = {1, 2, 3, 4, 5}
mutable_set.add(6)
mutable_set.add(5)  # Adding a duplicate does not add another copy.
print('After add():', mutable_set)

mutable_set.remove(4)  # remove() raises KeyError if the value is absent.
mutable_set.discard(99)  # discard() does nothing if the value is absent.
print('After remove() and discard():', mutable_set)
# mutable_set.remove(99)  # KeyError because 99 is not in the set.

clear_set = {1, 2, 3}
clear_set.clear()
print('After clear():', clear_set)


# 12. Compare sets
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print('your_set is a subset of my_set:', your_set.issubset(my_set))
print('my_set is a superset of your_set:', my_set.issuperset(your_set))
print('Sets are disjoint:', my_set.isdisjoint(your_set))

# A subset has every element contained in the other set. A superset contains
# every element of the other set. Disjoint sets have no values in common.


# 13. Set math operators
# Each operator below creates a new set.
print('Union |:', my_set | your_set)  # Values in either set.
print('Intersection &:', my_set & your_set)  # Values shared by both.
print('Difference -:', my_set - your_set)  # Values in the left set only.
print('Symmetric difference ^:', my_set ^ your_set)  # Values in either, not both.

# Compound assignment updates the set on the left in place.
union_set = my_set.copy()
union_set |= your_set
print('After |=:', union_set)

intersection_set = my_set.copy()
intersection_set &= your_set
print('After &=:', intersection_set)

difference_set = my_set.copy()
difference_set -= your_set
print('After -=:', difference_set)

symmetric_set = my_set.copy()
symmetric_set ^= your_set
print('After ^=:', symmetric_set)

# The `in` operator checks whether a value is a set member.
print('5 is in my_set:', 5 in my_set)
print('6 is in my_set:', 6 in my_set)


# 14. Standard library modules and imports
# A module is a file of reusable Python names such as functions and constants.
# Import statements are usually placed at the top of the file.

# Import a module, then access its names with dot notation.
print('Square root of 36:', math.sqrt(36))
print('Pi:', math.pi)

# Importing with `as` gives the module a shorter alias.
print('Square root via alias:', m.sqrt(49))

# Import selected functions to use them without a module prefix.
angle_degrees = 40
angle_radians = radians(angle_degrees)
print('Sine:', sin(angle_radians))
print('Cosine:', cos(angle_radians))

# Other common standard library modules:
# random: random numbers or choices
# re: regular expressions (pattern matching)
# datetime: dates and times
print('Random die roll:', random.randint(1, 6))
print('Pattern found:', re.search(r'\d+', 'Room 42').group())

birthday = datetime.date(1959, 7, 15)
print('Birthday:', birthday)
print('Day / month / year:', birthday.day, birthday.month, birthday.year)

# Avoid `from module import *` in normal code: it can cause name collisions
# and makes it harder to tell where imported names came from.
# from math import *


# 15. The __name__ == '__main__' guard
# Python sets __name__ to '__main__' when a file is run directly. When another
# file imports it, __name__ is set to the module name instead. Put code that
# should run only when this file is executed directly inside this condition.
def show_direct_run_message():
    print('This example is running as the main program.')


if __name__ == '__main__':
    show_direct_run_message()
