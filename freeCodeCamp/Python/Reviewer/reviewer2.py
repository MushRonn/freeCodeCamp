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


# 10. Tuples
# A tuple is an ordered sequence. It can hold mixed types, like a list, but
# it is immutable: its elements cannot be replaced or removed after creation.
developer_tuple = ('Alice', 34, 'Rust Developer')
programming_tuple = ('Python', 'Java', 'C++', 'Rust')
print('Developer tuple:', developer_tuple)

# Access tuple items with indexes. Indexing starts at 0; negative indexes
# count backward from the end.
print('Age:', developer_tuple[1])
tuple_numbers = (1, 2, 3, 4, 5)
print('Second to last:', tuple_numbers[-2])

# Out-of-range indexing raises IndexError. Example (commented out):
# tuple_numbers[7]  # IndexError

# Tuples cannot be updated or have individual items deleted. These examples
# would raise TypeError, so they stay commented out:
# programming_tuple[0] = 'JavaScript'  # TypeError: tuples are immutable
# del developer_tuple[1]  # TypeError: tuple items cannot be deleted

# tuple(iterable) converts an iterable, such as a string or list, into a tuple.
developer_name = 'Jessica'
tuple_from_string = tuple(developer_name)
tuple_from_list = tuple(['Python', 'Rust'])
print('Tuple from string:', tuple_from_string)
print('Tuple from list:', tuple_from_list)

# Use `in` to check whether an item is present.
print('Rust is included:', 'Rust' in programming_tuple)
print('JavaScript is included:', 'JavaScript' in programming_tuple)

# Unpacking assigns tuple items to variables. A starred target collects the
# remaining items into a list.
person = ('Alice', 34, 'Rust Developer')
person_name, person_age, person_job = person
print('Unpacked tuple:', person_name, person_age, person_job)

person_name, *person_rest = person
print('Name:', person_name)
print('Other values (a list):', person_rest)

# Slicing returns a tuple. The start is included and the stop is excluded.
dessert_tuple = ('cake', 'pie', 'cookies', 'ice cream')
print('Pie and cookies:', dessert_tuple[1:3])
print('Every other dessert:', dessert_tuple[::2])

# Choosing a sequence:
# Use a list for a collection you expect to add to, remove from, or update.
# Use a tuple for an ordered collection that should stay fixed and immutable.


# 11. Common tuple methods: count() and index()
language_tuple = ('Rust', 'Java', 'Python', 'C++', 'Rust')

# count(value) tells how many times a value appears. It returns 0 if absent.
print('Rust count:', language_tuple.count('Rust'))
print('JavaScript count:', language_tuple.count('JavaScript'))

# count() requires a value. This example would raise TypeError:
# language_tuple.count()

# index(value) returns the index of the first matching item.
print('Java index:', language_tuple.index('Java'))

# index() raises ValueError if the value is absent. Example:
# language_tuple.index('JavaScript')

# Optional start and stop positions limit where index() searches. The stop
# position is excluded, just like the stop in a slice.
repeated_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print('Python at or after index 3:', repeated_languages.index('Python', 3))

more_languages = (
    'Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python'
)
print('Python from index 2 up to (not including) 5:',
      more_languages.index('Python', 2, 5))


# 12. Sorting tuples with sorted()
# sorted() accepts iterables, including tuples, and returns a NEW list.
number_tuple = (13, 2, 78, 3, 45, 67, 18, 7)
sorted_numbers = sorted(number_tuple)
print('Original tuple:', number_tuple)
print('Sorted list:', sorted_numbers)

# Use reverse=True to sort in descending order.
language_tuple = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print('Descending:', sorted(language_tuple, reverse=True))

# Use key=len to sort strings by their length. When lengths are equal, their
# original relative order is kept (stable sorting).
print('Sorted by word length:', sorted(language_tuple, key=len))

# Difference to remember:
#   tuple: immutable, so it has no sort() method
#   list.sort(): sorts that list in place and returns None
#   sorted(iterable): works with tuples and other iterables, returns a new list


# 13. Loops
# Loops repeat an indented block of code. Indentation shows which statements
# belong to the loop.

# A for loop visits each item in an iterable, such as a list.
for language in ['Rust', 'Java', 'Python', 'C++']:
    print('Language:', language)

# Strings are iterable too, so a for loop can visit each character.
for character in 'code':
    print('Character:', character)

# Nested loops: for every category, visit every food.
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']
for category in categories:
    for food in foods:
        print(category, food)

# A while loop repeats as long as its condition is True. Make sure something
# in the loop changes the condition, or the loop may never stop.
countdown = 3
while countdown > 0:
    print('Countdown:', countdown)
    countdown -= 1
print('Done!')

# Interactive guessing-game pattern from the lesson (commented out so
# running this reviewer does not wait for keyboard input):
# secret_number = 3
# guess = 0
# while guess != secret_number:
#     guess = int(input('Guess the number (1-5): '))
#     if guess != secret_number:
#         print('Wrong! Try again.')
# print('You got it!')

# break exits the current loop immediately.
developer_names = ['Jess', 'Naomi', 'Tom']
for developer in developer_names:
    if developer == 'Naomi':
        break
    print('Before break:', developer)  # prints Jess only

# continue skips the rest of this iteration and starts the next one.
for developer in developer_names:
    if developer == 'Naomi':
        continue
    print('Not skipped:', developer)  # prints Jess and Tom

# A loop's else clause runs only if the loop finishes without break.
# In nested loops, indentation determines which loop the else belongs to.
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']
for current_word in words:
    for letter in current_word:
        if letter.lower() in 'aeiou':
            print(f"'{current_word}' contains the vowel '{letter}'")
            break
    else:
        # This else belongs to the inner for loop. It runs when that loop
        # checks every letter without finding a vowel (no break occurred).
        print(f"'{current_word}' has no vowels")
