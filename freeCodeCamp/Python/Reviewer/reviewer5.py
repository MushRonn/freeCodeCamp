"""Python reviewer: Dictionaries

Dictionaries store key-value pairs. Use a key to look up its associated value.
Keys must be unique and hashable; values may be repeated and can be any type.
"""


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
