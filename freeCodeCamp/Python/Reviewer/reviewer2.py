"""Python reviewer: Lists

Lists are ordered, mutable sequences. They can contain values of different
types, including other lists. Python list indexes start at zero.
"""

# 1. Creating a list and reading its elements
cities = ['Los Angeles', 'London', 'Tokyo']
print('Cities:', cities)
print('First city:', cities[0])       # index 0 is the first item
print('Last city:', cities[-1])       # -1 counts from the end
print('Number of cities:', len(cities))

# list() converts an iterable into a list. A string is iterable character by
# character, so each character becomes one list item.
developer_name = 'Jessica'
letters = list(developer_name)
print('Letters:', letters)


# 2. Updating and removing items
# Lists are mutable, so an item at a valid index can be replaced.
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print('After update:', programming_languages)

# del removes an item by index; later items shift left to fill its place.
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print('After deleting item 1:', developer)

# An index outside the list's valid range raises IndexError. This example is
# intentionally commented out so it does not stop the reviewer from running:
# programming_languages[10] = 'JavaScript'  # IndexError


# 3. Checking membership with `in`
languages = ['Python', 'Java', 'C++', 'Rust']
print('Rust is included:', 'Rust' in languages)          # True
print('JavaScript is included:', 'JavaScript' in languages)  # False


# 4. Nested lists
# A list can contain another list. Use one index for the outer list and
# another index for an item inside the nested list.
developer_info = ['Alice', 25, ['Python', 'Rust', 'C++']]
print('Nested language list:', developer_info[2])
print('Second language:', developer_info[2][1])  # Rust


# 5. Unpacking values
# The number of variables on the left must match the list length, unless a
# starred variable is used to collect the remaining values.
developer_details = ['Alice', 34, 'Rust Developer']
name, age, job = developer_details
print('Unpacked:', name, age, job)

name, *rest = developer_details
print('Name:', name)
print('Remaining values:', rest)  # [34, 'Rust Developer']

# A mismatch without a starred target raises ValueError. Example (commented
# out so it will not interrupt this file):
# name, age, job, city = developer_details  # ValueError: only 3 items


# 6. Slicing lists: list[start:stop:step]
# start is included; stop is excluded. Omitting stop means continue to the end.
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print('Middle desserts:', desserts[1:4])  # Cookies, Ice Cream, Pie
print('Copy of the list:', desserts[:])

numbers = [1, 2, 3, 4, 5, 6]
print('Even numbers:', numbers[1::2])  # start at index 1, then step by 2
print('Every other number:', numbers[::2])
print('Reversed:', numbers[::-1])

# Slicing makes a new list; it does not change the original list.
print('Original numbers:', numbers)


# 7. Common list methods
# append(item) adds one item to the end. Appending a list keeps it nested.
append_demo = [1, 2, 3]
append_demo.append(4)
append_demo.append([5, 6])
print('append adds one item:', append_demo)  # [1, 2, 3, 4, [5, 6]]

# extend(iterable) adds each item from the iterable to the end of the list.
extend_demo = [1, 2, 3]
extend_demo.extend([4, 5, 6])
print('extend adds each item:', extend_demo)  # [1, 2, 3, 4, 5, 6]

# insert(index, item) places a value at the requested position.
insert_demo = [1, 2, 3, 4]
insert_demo.insert(2, 'two and a half')
print('After insert:', insert_demo)

# remove(value) removes only the first matching value.
remove_demo = [10, 20, 30, 30]
remove_demo.remove(30)
print('After removing first 30:', remove_demo)  # [10, 20, 30]

# pop(index) removes and returns an item. With no index, it removes the last.
pop_demo = ['a', 'b', 'c']
removed_item = pop_demo.pop(1)
last_item = pop_demo.pop()
print('Popped items:', removed_item, last_item)
print('List after pop:', pop_demo)

# clear() removes every item from the list.
clear_demo = [1, 2, 3]
clear_demo.clear()
print('After clear:', clear_demo)  # []


# 8. Sorting and reversing
# sort() changes the list in place and returns None.
sort_demo = [19, 2, 35, 1, 67, 41]
sort_demo.sort()
print('Sorted in place:', sort_demo)

# sorted(iterable) returns a new sorted list and leaves the original unchanged.
unsorted_numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(unsorted_numbers)
print('Original:', unsorted_numbers)
print('New sorted list:', sorted_numbers)

# Both sort() and sorted() accept reverse=True for descending order.
print('Descending:', sorted(unsorted_numbers, reverse=True))

# reverse() reverses the current order in place; it does not sort the values.
reverse_demo = [6, 5, 4, 3, 2, 1]
reverse_demo.reverse()
print('After reverse:', reverse_demo)


# 9. Finding an item's index
# index(value) returns the position of the first matching item.
programming_languages = ['Rust', 'Java', 'Python', 'C++']
print("Index of Java:", programming_languages.index('Java'))  # 1

# index(value) raises ValueError if the value is not in the list. Example:
# programming_languages.index('JavaScript')  # ValueError
