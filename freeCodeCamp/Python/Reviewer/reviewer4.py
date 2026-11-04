"""Python reviewer: Dictionaries

Dictionaries store key-value pairs. Use a key to look up its associated value.
Keys must be unique and hashable; values can be any type and may repeat.
"""


# 1. Creating dictionaries
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}
print('Pizza dictionary:', pizza)

# dict() can create the same dictionary from key-value pairs.
pizza_from_pairs = dict([
    ('name', 'Margherita Pizza'),
    ('price', 8.9),
    ('calories_per_slice', 250),
    ('toppings', ['mozzarella', 'basil'])
])
print('Created with dict():', pizza_from_pairs)

# Keys are commonly strings. Integers and tuples can also be keys; lists
# cannot be keys because they are mutable. Values can be lists or other types.
sample = {1: 'one', ('x', 'y'): 'a tuple key', 'items': [2, 3]}
print('Other valid key types:', sample)


# 2. Accessing, updating, and adding values
print('Pizza name:', pizza['name'])  # Bracket notation retrieves by key.

pizza['name'] = 'Margherita'         # Existing key: replace its value.
pizza['total_time'] = 25             # New key: add a key-value pair.
print('Updated name:', pizza['name'])
print('Added total time:', pizza['total_time'])

# Insertion order is preserved in modern Python dictionaries, so iteration
# follows the order in which keys were added.
print('Keys in insertion order:', list(pizza))


# 3. get(): retrieve a value with an optional fallback
# Bracket notation with a missing key raises KeyError. get() can provide a
# default value instead, so the lookup is safe when the key might be absent.
print('Toppings:', pizza.get('toppings', []))
print('Missing field fallback:', pizza.get('allergens', 'Not specified'))


# 4. Viewing keys, values, and key-value pairs
# keys(), values(), and items() return view objects, which reflect the
# dictionary's contents without making a separate copy.
print('Keys view:', pizza.keys())
print('Values view:', pizza.values())
print('Items view:', pizza.items())

# Views can be converted to lists when a list is useful.
print('Keys as a list:', list(pizza.keys()))


# 5. Removing dictionary entries
pop_demo = {'name': 'Margherita', 'price': 8.9}
removed_price = pop_demo.pop('price')  # Removes the key and returns its value.
print('Popped value:', removed_price)
print('After pop:', pop_demo)

# A default is returned when pop() cannot find the requested key.
print('Missing pop with default:', pop_demo.pop('total_price', 10))

# Without a default, pop() on a missing key raises KeyError. Example:
# pop_demo.pop('total_price')

# popitem() removes and returns the last inserted key-value pair (Python 3.7+).
popitem_demo = {'name': 'Margherita', 'price': 8.9, 'total_time': 25}
last_pair = popitem_demo.popitem()
print('Removed last pair:', last_pair)
print('After popitem:', popitem_demo)

# clear() removes all entries from the dictionary.
clear_demo = {'name': 'Margherita', 'price': 8.9}
clear_demo.clear()
print('After clear:', clear_demo)


# 6. update(): add or replace multiple entries
update_demo = {
    'name': 'Margherita',
    'price': 8.9,
    'calories_per_slice': 250
}
update_demo.update({'price': 15, 'total_time': 25})
print('After update:', update_demo)
# The existing price is overwritten; total_time is added because it was new.
