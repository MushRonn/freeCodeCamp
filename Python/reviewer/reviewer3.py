"""Loops and Sequences Review

Runnable examples and notes for lists, tuples, loops, and related functions.
Error examples are commented out so they do not stop the file from running.
"""


# 1. Lists: ordered, mutable sequences. Indexes start at zero.
cities = ['Los Angeles', 'London', 'Tokyo']
print('First city:', cities[0])
print('Last city:', cities[-1])  # Negative indexes count from the end.
print('City count:', len(cities))

# list() converts an iterable to a list. A string becomes individual chars.
developer = 'Jessica'
print('Characters:', list(developer))

# Lists are mutable: update an item using a valid index.
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print('Updated list:', programming_languages)

# An invalid index raises IndexError. Kept commented out intentionally.
# programming_languages[10] = 'Go'

# del removes the item at an index; `in` checks for a value.
developer_info = ['Jane Doe', 23, 'Python Developer']
del developer_info[1]
print('After del:', developer_info)
print('Rust is present:', 'Rust' in programming_languages)
print('Go is present:', 'Go' in programming_languages)

# Nested lists: use repeated indexes to access an item inside an inner list.
nested_developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print('Language list:', nested_developer[2])
print('Second language:', nested_developer[2][1])

# Unpacking assigns list values to variables. A starred name collects the rest.
developer_record = ['Alice', 34, 'Rust Developer']
person_name, person_age, person_job = developer_record
print('Unpacked:', person_name, person_age, person_job)
person_name, *other_details = developer_record
print('Name and remaining details:', person_name, other_details)
# Without a starred target, the number of variables must match list length.
# person_name, person_age = developer_record  # ValueError

# Slicing uses [start:stop:step]. Start is included; stop is excluded.
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie']
print('Slice:', desserts[1:3])
sequence_numbers = [1, 2, 3, 4, 5, 6]
print('Every other even-positioned value:', sequence_numbers[1::2])


# 2. Common list methods
method_numbers = [1, 2, 3]
method_numbers.append(4)        # Append one item at the end.
method_numbers.append([5, 6])   # The whole list is appended as one nested item.
print('append():', method_numbers)

extended_numbers = [1, 2, 3]
extended_numbers.extend([4, 5, 6])  # Add each item from another iterable.
print('extend():', extended_numbers)

insert_numbers = [1, 2, 3, 4]
insert_numbers.insert(2, 2.5)   # Insert value at index 2.
print('insert():', insert_numbers)

remove_numbers = [10, 20, 30, 30]
remove_numbers.remove(30)       # Removes only the first matching value.
print('remove():', remove_numbers)

pop_numbers = [1, 2, 3, 4]
removed_value = pop_numbers.pop(1)  # Removes and returns item at index 1.
last_value = pop_numbers.pop()      # With no index, removes the last item.
print('pop() returned:', removed_value, last_value)
print('After pop():', pop_numbers)

clear_numbers = [1, 2, 3]
clear_numbers.clear()
print('clear():', clear_numbers)

# sort() changes a list in place; sorted() makes a new sorted list.
unsorted_numbers = [19, 2, 35, 1, 67, 41]
unsorted_numbers.sort()
print('sort():', unsorted_numbers)
original_numbers = [19, 2, 35, 1, 67, 41]
new_sorted_numbers = sorted(original_numbers)
print('Original after sorted():', original_numbers)
print('New sorted list:', new_sorted_numbers)
print('Reverse sort:', sorted(original_numbers, reverse=True))

reverse_numbers = [6, 5, 4, 3, 2, 1]
reverse_numbers.reverse()      # Reverses current order in place; does not sort.
print('reverse():', reverse_numbers)

language_list = ['Rust', 'Java', 'Python', 'C++']
print('index of Java:', language_list.index('Java'))  # First matching index.
# language_list.index('Go')  # ValueError when value is absent.


# 3. Tuples: ordered sequences that are immutable.
developer_tuple = ('Alice', 34, 'Rust Developer')
language_tuple = ('Python', 'Java', 'C++', 'Rust')
print('Tuple item:', developer_tuple[1])
tuple_numbers = (1, 2, 3, 4, 5)
print('Negative tuple index:', tuple_numbers[-2])

# Tuples cannot have individual items updated or deleted (TypeError).
# language_tuple[0] = 'JavaScript'
# del developer_tuple[1]
# tuple_numbers[7]  # IndexError: index is out of range

# tuple() converts an iterable into a tuple.
print('Tuple from string:', tuple('Jessica'))
print('Tuple from list:', tuple(['Python', 'Rust']))
print('Rust is in tuple:', 'Rust' in language_tuple)

# Tuples support unpacking and slicing, just like lists.
person_name, person_age, person_job = developer_tuple
print('Tuple unpacked:', person_name, person_age, person_job)
person_name, *tuple_rest = developer_tuple
print('Tuple remainder:', tuple_rest)  # The starred result is a list.
tuple_desserts = ('cake', 'pie', 'cookies', 'ice cream')
print('Tuple slice:', tuple_desserts[1:3])

# Choose a list for data that needs to change; choose a tuple for fixed data.


# 4. Common tuple methods and sorting tuples
repeated_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print('Rust count:', repeated_languages.count('Rust'))
print('JavaScript count:', repeated_languages.count('JavaScript'))  # 0
print('First Java index:', repeated_languages.index('Java'))
print('Python index from position 3:', repeated_languages.index('Python', 3))

bounded_languages = (
    'Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python'
)
print('Python index from 2 up to (not including) 5:',
      bounded_languages.index('Python', 2, 5))
# tuple.index() raises ValueError if the item is not present.
# repeated_languages.index('Go')

tuple_values = (13, 2, 78, 3, 45, 67, 18, 7)
print('Sorted tuple values:', sorted(tuple_values))  # sorted() returns a list.
print('Sorted by length:', sorted(repeated_languages, key=len))
print('Descending:', sorted(repeated_languages, reverse=True))


# 5. for loops and nested loops
# A for loop visits each item in an iterable. Indentation is part of the syntax.
for language in ['Rust', 'Java', 'Python', 'C++']:
    print('Loop item:', language)

# Strings are iterable too.
for character in 'code':
    print('Character:', character)

# A nested loop runs the inner loop for each item in the outer loop.
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']
for category in categories:
    for food in foods:
        print(category, food)

# 6. while loops
# A while loop continues while its condition is True. Update the condition so
# the loop can eventually stop.
countdown = 3
while countdown > 0:
    print('Countdown:', countdown)
    countdown -= 1

# Interactive guessing game pattern (commented so the reviewer doesn't pause):
# secret_number = 3
# guess = 0
# while guess != secret_number:
#     guess = int(input('Guess the number (1-5): '))
#     if guess != secret_number:
#         print('Wrong! Try again.')
# print('You got it!')

# break exits the loop; continue skips to the next iteration.
developer_names = ['Jess', 'Naomi', 'Tom']
for developer in developer_names:
    if developer == 'Naomi':
        break
    print('Before break:', developer)  # Jess only

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print('Not skipped:', developer)  # Jess and Tom

# Loop else runs only when the loop finishes without a break.
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']
for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")


# 7. range(start, stop, step)
# stop is required and excluded. Defaults: start=0 and step=1.
for number in range(3):
    print('range(3):', number)  # 0, 1, 2

for number in range(1, 5):
    print('range(1, 5):', number)  # 1, 2, 3, 4

for number in range(2, 11, 2):
    print('Even number:', number)  # 2, 4, 6, 8, 10

for number in range(40, 0, -10):
    print('Counting down:', number)  # 40, 30, 20, 10

# range() requires integer arguments; these examples would raise TypeError.
# range()
# range(3.4)
print('List from range:', list(range(2, 11, 2)))


# 8. enumerate() tracks an item's index while looping.
languages = ['Spanish', 'English', 'Russian', 'Chinese']
for index, language in enumerate(languages):
    print(f'Index {index}, language {language}')

print('Enumerated pairs:', list(enumerate(languages)))
for number, language in enumerate(languages, 1):  # Optional starting count.
    print(f'Number {number}: {language}')

# 9. zip() iterates over matching positions in multiple iterables.
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
developer_ids = [1, 2, 3, 4]
print('Zipped pairs:', list(zip(developers, developer_ids)))
for developer_name, developer_id in zip(developers, developer_ids):
    print(f'{developer_name}: {developer_id}')

# zip() stops when the shortest iterable runs out.
print('Uneven zip:', list(zip(['A', 'B'], [10, 20, 30])))


# 10. List comprehensions
# Shape: [expression for item in iterable if optional_condition]
even_numbers = [number for number in range(21) if number % 2 == 0]
print('Even numbers 0-20:', even_numbers)

# Conditional expression shape: value_if_true if condition else value_if_false
values = [1, 2, 3, 4, 5]
labels = [
    (value, 'Even') if value % 2 == 0 else (value, 'Odd')
    for value in values
]
print('Number labels:', labels)


# 11. filter(), map(), and sum()
words_to_filter = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']


def is_long_word(word):
    return len(word) > 4


# filter(function, iterable) keeps items for which the function returns True.
print('Long words:', list(filter(is_long_word, words_to_filter)))

celsius = [0, 10, 20, 30, 40]


def to_fahrenheit(temperature):
    return (temperature * 9 / 5) + 32


# map(function, iterable) applies the function to every item.
print('Fahrenheit:', list(map(to_fahrenheit, celsius)))

sum_values = [5, 10, 15, 20]
print('Sum:', sum(sum_values))
print('Sum with start value:', sum(sum_values, 10))
print('Sum with named start:', sum(sum_values, start=10))


# 12. Lambda functions
# lambda parameters: single_expression creates a short anonymous function.
# A lambda is useful inline; use def for reusable or complicated functions.
lambda_numbers = [1, 2, 3, 4, 5]
print('Even values with lambda:',
      list(filter(lambda value: value % 2 == 0, lambda_numbers)))
print('Doubled with lambda:',
      list(map(lambda value: value * 2, lambda_numbers)))


def square(number):
    return number ** 2


print('Squares with named function:', list(map(square, lambda_numbers)))


#My SCORE

Score = 100
print(f'My score is: {Score}%')