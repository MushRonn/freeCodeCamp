# ALGORITHMS AND BIG O NOTATION REVIEW
# ===================================
#
# 1. Algorithms
# -------------
# An algorithm is a precise, unambiguous set of instructions for solving a
# problem or completing a task. It must finish after a finite number of steps.
#
# A practical problem-solving process:
#   1. Understand the task: identify the inputs, expected output, and required
#      transformation from input to output.
#   2. Choose an algorithm and data structure by comparing their time and
#      memory requirements.
#   3. Write pseudocode to outline the logic without committing to syntax.
#   4. Implement clean, readable, modular code, using built-in tools where
#      appropriate.
#   5. Check normal examples and edge cases (valid boundary inputs).
#   6. Debug and refine the code for clarity and efficiency.
#
# Pseudocode example: reverse a string
# GET original_string
# SET reversed_string = ""
# FOR EACH character IN original_string:
#     ADD character TO THE BEGINNING OF reversed_string
# DISPLAY reversed_string
#
# 2. Big O Notation
# -----------------
# Big O describes an asymptotic upper bound on how an algorithm's resource
# usage (usually runtime or memory) grows as input size n increases. It
# describes the growth trend, ignoring constant factors and smaller terms.
# Big O can describe different cases, such as worst-case or average-case
# behavior; it does not by itself specify which case is being discussed.
#
# Common time complexities, from slower growth to faster growth:
#
# O(1) - Constant: bounded time regardless of input size.
# Example: checking whether one number is even or odd.
#
# def check_even_or_odd(number):
#     return 'Even' if number % 2 == 0 else 'Odd'
#
# O(log n) - Logarithmic: the problem size is repeatedly reduced by a constant
# fraction. Binary search is a common example; its bound is O(log n).
#
# O(n) - Linear: work grows at most in proportion to the number of inputs.
# Example: visiting every item in a list once.
#
# for grade in grades:
#     print(grade)
#
# O(n log n) - Log-linear: common in efficient divide-and-conquer sorting.
# Merge sort has O(n log n) worst-case time. Quicksort has O(n log n) average
# time, but O(n^2) worst-case time.
#
# O(n^2) - Quadratic: often caused by two nested loops that each run n times.
#
# for i in range(n):
#     for j in range(n):
#         print(i, j)
#
# O(2^n) - Exponential: when tight, the work approximately doubles each time
# n increases by one.
#
# O(n!) - Factorial: when tight, work grows like the number of permutations of
# n distinct items. This becomes impractical very quickly.
#
# 3. Space Complexity
# -------------------
# Space complexity describes how memory usage grows with input size.
# Auxiliary space is the extra memory an algorithm needs beyond its input and
# required output.
#
# O(1) space: extra memory stays bounded as input grows.
# O(n) space: extra memory grows proportionally to input size.
# O(n^2) space: extra memory grows proportionally to the square of input size.
# O(2^n) space: extra memory grows exponentially.
# O(n!) space: extra memory grows factorially.
#
# 4. Arrays and Python Lists
# --------------------------
# A static array has a fixed size and stores items in contiguous memory.
# Indexed access is O(1). It is useful when the maximum size is known.
#
# A dynamic array can grow or shrink. When it runs out of capacity, it may
# allocate a larger block and copy its elements. Python's built-in list is a
# dynamic array; Python does not provide a traditional built-in static array.
#
# numbers = [3, 4, 5, 6]
# first = numbers[0]       # Indexed access: O(1)
# numbers[2] = 16          # Update by index: O(1)
# numbers.append(7)        # Add at end: O(1) average, O(n) on resize
# numbers.insert(1, 10)    # Insert in middle: O(n), elements shift
# numbers.pop(2)           # Remove by index: O(n) in middle
# numbers.pop()            # Remove last: O(1)
#
# Dynamic array operation summary:
#   Access by index: O(1)
#   Append at end: O(1) average; O(n) when resizing
#   Insert in middle: O(n)
#   Delete in middle: O(n); delete at end: O(1)
#
# 5. Stacks
# ----------
# A stack is a Last-In, First-Out (LIFO) structure. Add and remove elements
# from the top. Python lists can implement stacks with append() and pop().
#
# stack = []
# stack.append(1)  # push: add to top
# stack.append(2)
# stack.append(3)
# top_element = stack.pop()  # pop: returns 3
#
# Ordinary push: O(1) time and O(1) additional space; a resize may take O(n)
# time and temporary O(n) additional space. Pop from the top is typically
# O(1) time and O(1) additional space.
#
# Common uses: undo actions, expression evaluation, and backtracking.
#
# 6. Queues
# ---------
# A queue is a First-In, First-Out (FIFO) structure. Add elements at the back
# (enqueue) and remove them from the front (dequeue).
#
# Enqueue: O(1) time and O(1) additional space in a suitable queue.
# Dequeue: O(1) time and O(1) additional space in a suitable queue.
# Common uses: task scheduling and breadth-first search.
#
# 7. Linked Lists
# ---------------
# A linked list is a sequence of nodes. Each node stores data and a reference
# to another node. A singly linked list node points to its next node.
#
#   head -> [data | next] -> [data | next] -> [data | None]
#
# The head refers to the first node. The last node's next is None. In a singly
# linked list, traversal moves forward, one node at a time. There is no fast
# random access by index; finding an item generally takes O(n).
#
# A nested Node class and a simple append implementation:
#
# class LinkedList:
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.next = None
#
#     def __init__(self):
#         self.head = None
#         self.length = 0
#
#     def is_empty(self):
#         return self.head is None
#
#     def append(self, data):
#         new_node = self.Node(data)
#         if self.is_empty():
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#         self.length += 1
#
# Insertion and deletion logic:
#   Beginning insertion: new_node.next = head, then head = new_node.
#   End insertion: traverse to the last node, then link its next to new_node.
#   Middle insertion: find the previous node; link new_node to the following
#       node, then link the previous node to new_node.
#   Beginning deletion: move head to the second node.
#   End deletion: find the second-to-last node and set its next to None.
#   Middle deletion: link the previous node around the target node.
#   Remove by value: track previous and current nodes while traversing. If the
#       target is not found, do not change the list or its length. Decrease the
#       length only after a successful removal.
#
# Singly linked list operation complexities:
#   Insert at beginning: O(1) time, O(1) auxiliary space
#   Insert at end: O(n) time without a tail reference, O(1) auxiliary space
#   Insert in middle: O(n) time to find position, O(1) auxiliary space
#   Delete at beginning: O(1) time and auxiliary space
#   Delete at end or middle: O(n) time to find node, O(1) auxiliary space
#
# A doubly linked list stores both next and previous references. It can be
# traversed in both directions but uses more memory per node. A tail reference
# makes it possible to start reverse traversal from the last node.
#
# 8. Maps, Hash Maps, and Python Dictionaries
# -------------------------------------------
# An Abstract Data Type (ADT) describes what operations are available and how
# they behave logically, without specifying implementation details.
#
# A map ADT represents unique keys associated with values. A hash map is a
# concrete implementation that uses a hash function to find storage locations
# in an underlying array. Python dictionaries are hash maps.
#
# record = {'A': 1, 'B': 2, 'C': 3}
# other = dict(A=1, B=2, C=3)
# value = record['A']       # retrieve by key
# record['A'] = 4           # update value
# del record['A']           # remove key/value pair
# 'C' in record             # key membership test
# record.keys()             # keys view
# record.values()           # values view
# record.items()            # key/value pairs view
#
# Hash map time complexity:
#   Average insert, lookup, delete: O(1)
#   Worst case: O(n), for example when many keys collide
#
# Hash map auxiliary space:
#   Ordinary insertion: O(1) additional space; resizing may need O(n)
#   Lookup and deletion: O(1) auxiliary space
#
# 9. Sets
# --------
# A set stores unique elements with no guaranteed order or index access.
# Elements must be hashable. Common valid elements include numbers, strings,
# and tuples of hashable values. Lists, dictionaries, and sets cannot be set
# elements. A tuple containing a list is not hashable, so it cannot be an
# element either.
#
# numbers = {1, 2, 3, 4}
# empty_set = set()  # {} creates an empty dictionary, not a set
# numbers.add(5)
# numbers.remove(4)   # KeyError if 4 is absent
# numbers.discard(4)  # no error if 4 is absent
# numbers.pop()       # removes and returns an arbitrary element
# numbers.clear()     # removes all elements
# len(numbers)
#
# Set operations:
#
# set_a = {1, 2, 3, 4}
# set_b = {2, 3, 4, 5, 6}
# set_a.union(set_b)                 # or set_a | set_b
# set_a.intersection(set_b)          # or set_a & set_b
# set_a.difference(set_b)            # or set_a - set_b
# set_a.symmetric_difference(set_b)  # or set_a ^ set_b
# set_a.issubset(set_b)
# set_a.issuperset(set_b)
# set_a.isdisjoint(set_b)
# 5 in set_a                         # membership test
#
# Set time complexity:
#   Average add, remove, membership: O(1)
#   Worst case: O(n) due to hash collisions
#   Length lookup: O(1)
# Auxiliary space is O(1) for ordinary add, lookup, and delete operations;
# resizing during insertion may require O(n) additional space.
#
# 10. Hash Collisions
# -------------------
# A hash collision occurs when different keys produce the same hash value, or
# when their hash values map to the same index in the underlying table. The
# implementation must resolve collisions.
#
# Chaining: Each array bucket points to a collection, often a linked list, of
# entries that map to that bucket.
#
# Open addressing: If a bucket is occupied, probe other array positions in a
# defined sequence until an available location is found.
#
# 11. Choosing a Data Structure
# ------------------------------
# Lists: ordered, indexed access; good when the collection can change size.
# Stacks: LIFO behavior, such as undo, parsing, and backtracking.
# Queues: FIFO behavior, such as scheduling and breadth-first search.
# Linked lists: frequent insertions/deletions near the beginning, unknown size,
#               and no need for random access.
# Hash maps/dictionaries: fast average key/value lookup, counting, and caching.
# Sets: uniqueness checks, membership tests, and mathematical set operations.
#
# QUICK REVIEW
# ------------
# - Big O describes how time or memory grows as input size grows.
# - O(1) is constant; O(log n) logarithmic; O(n) linear; O(n log n) log-linear.
# - Nested loops often yield O(n^2); O(2^n) and O(n!) grow very quickly.
# - Python lists are dynamic arrays; indexed access is O(1), middle insertion
#   and deletion are O(n).
# - A stack is LIFO; a queue is FIFO.
# - Linked lists chain nodes through references; traversal is sequential.
# - Dictionaries and sets use hashing for average O(1) operations.
# - Hash collisions are handled with strategies such as chaining or probing.
# - Choose the structure whose operations fit the task.

# My score is 100% / 20 over 20