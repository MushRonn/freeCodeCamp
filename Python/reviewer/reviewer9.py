# OBJECT-ORIENTED PROGRAMMING REVIEW
# ================================
#
# 1. What is Object-Oriented Programming (OOP)?
# --------------------------------------------
# OOP organizes code around objects. A class is a blueprint; an object is an
# instance created from it. Objects have attributes (data) and methods
# (behavior).
#
# Four key OOP principles:
#   1. Encapsulation
#   2. Inheritance
#   3. Polymorphism
#   4. Abstraction
#
# 2. Encapsulation
# ----------------
# Encapsulation bundles an object's data and methods together. It can protect
# internal state by providing methods or properties to control access.
#
# Naming conventions:
#   name       Public; intended for normal external use.
#   _name      Internal-use convention; Python still allows outside access.
#   __name     Triggers name mangling, usually becoming _ClassName__name.
#              This helps avoid accidental name collisions in subclasses; it
#              does not make the value impossible to access.
#
# Example: controlled access to a wallet balance
#
# class Wallet:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#
# wallet = Wallet(500)
# wallet.deposit(25)
# # wallet.__balance raises AttributeError because its name is mangled.
# # wallet._Wallet__balance can access it, but usually should not be used.
#
# 3. Getters, Setters, Properties, and Decorators
# ------------------------------------------------
# A getter retrieves a value; a setter controls how a value is changed.
# @property makes a method usable like an attribute, with dot notation.
# A decorator modifies or wraps a function or class. It appears directly above
# the definition it decorates.
#
# Example with validation:
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius       # Calls the setter.
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         if value <= 0:
#             raise ValueError('Radius must be positive')
#         self._radius = value       # Use a backing attribute.
#
#     @property
#     def area(self):
#         return 3.14 * self._radius ** 2
#
# circle = Circle(3)
# print(circle.radius)  # 3; the getter runs
# circle.radius = 8     # The setter runs
# print(circle.area)    # 200.96
#
# Do not assign to a property inside its own setter (for example,
# self.radius = value). That calls the setter again and causes recursion.
# Store the value in a backing attribute such as self._radius.
#
# A deleter controls what happens when del is used on a property:
#
#     @radius.deleter
#     def radius(self):
#         del self._radius
#
# 4. Inheritance and super()
# -------------------------
# Inheritance lets a child class reuse or customize a parent's attributes and
# methods. It supports code reuse and clear class hierarchies.
#
# class Parent:
#     pass
#
# class Child(Parent):
#     pass
#
# Single inheritance uses one parent. Multiple inheritance uses more than one:
#
# class GrandChild(Parent, Child):
#     pass
#
# super() calls a parent method without naming the parent class explicitly:
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
# class Developer(Person):
#     def __init__(self, name, language):
#         super().__init__(name)
#         self.language = language
#
# 5. Polymorphism
# ----------------
# Polymorphism means different classes can use the same method name while
# implementing its behavior differently.
#
# class Cat:
#     def speak(self):
#         return 'Meow'
#
# class Dog:
#     def speak(self):
#         return 'Woof'
#
# for animal in (Cat(), Dog()):
#     print(animal.speak())
#
# In inheritance-based polymorphism, child classes override or extend a
# parent's method to provide class-specific behavior.
#
# 6. Name Mangling
# -----------------
# Python changes a double-underscore attribute name by adding the class name:
#     __data becomes _ClassName__data
#
# This mainly prevents accidental name collisions when subclasses define
# similarly named attributes. It is not strict privacy.
#
# class Parent:
#     def __init__(self):
#         self.__data = 'Parent data'
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__data = 'Child data'
#
# child = Child()
# # child.__dict__ contains '_Parent__data' and '_Child__data'.
#
# 7. Abstraction and Abstract Base Classes
# ----------------------------------------
# Abstraction hides implementation details and exposes essential operations.
# The abc module provides ABC and @abstractmethod for formal interfaces. A
# concrete subclass must implement every inherited abstract method before it
# can be instantiated.
#
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side * self.side
#
# # Shape() raises TypeError because area() is abstract.
# print(Square(4).area())  # 16
#
# Inheriting from ABC alone does not prevent instantiation; an unimplemented
# abstract method is what makes the class abstract.
#
# 8. Object Representations: __repr__, repr(), and !r
# ---------------------------------------------------
# __repr__ returns a useful, preferably unambiguous representation. Ideally,
# it resembles the expression that could recreate the object.
# repr(obj) calls obj.__repr__() under the hood. For strings, repr() adds
# quotes and escapes special characters.
#
# repr('Charlie')   # 'Charlie'
# repr("O'Reilly")  # "O'Reilly"
#
# In an f-string, !r applies repr() to the value:
#
# class Employee:
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level
#
#     def __repr__(self):
#         return f'Employee({self.name!r}, {self.level!r})'
#
# print(repr(Employee("O'Reilly", 'junior')))
# # Employee("O'Reilly", 'junior')
#
# 9. Docstrings
# --------------
# A docstring documents a module, class, or function. It is the first
# statement in the body and is commonly written with triple quotes.
#
# class Movie:
#     """Parent class representing a movie."""
#
# print(Movie.__doc__)
#
# 10. Type Checks: isinstance() and type()
# ----------------------------------------
# isinstance(obj, Class) is True when obj is an instance of Class or one of
# its subclasses. Use it when subclass instances should count as that type.
# type(obj) is Class checks for that exact class, excluding subclasses.
#
# class Movie:
#     pass
#
# class TVSeries(Movie):
#     pass
#
# series = TVSeries()
# # isinstance(series, Movie) is True
# # type(series) is Movie is False
# # type(series) is TVSeries is True
#
# 11. Custom Exceptions with Extra Context
# -----------------------------------------
# A custom exception can carry extra data along with its message. Call
# super().__init__(message) so the base Exception stores the message.
#
# class MediaError(Exception):
#     """Custom exception for media-related errors."""
#
#     def __init__(self, message, obj):
#         super().__init__(message)
#         self.obj = obj
#
# try:
#     raise MediaError('Unsupported item', 42)
# except MediaError as error:
#     print(f'Media Error: {error}')
#     print(f'Unable to add {error.obj}: {type(error.obj)}')
#
# 12. Type Hints
# ---------------
# Type hints communicate expected types for parameters, attributes, and
# return values. Python generally does not enforce them at runtime.
#
# def greet(name: str) -> str:
#     return 'Hello, ' + name
#
# def __init__(self, name: str, price: float) -> None:
#     ...
#
# Custom classes can be used as type hints. list[ClassName] describes a list
# expected to contain instances of that class:
#
# class DiscountStrategy:
#     pass
#
# class DiscountEngine:
#     def __init__(self, strategies: list[DiscountStrategy]) -> None:
#         self.strategies = strategies
#
# QUICK REVIEW
# ------------
# - Class = blueprint; object = instance.
# - Encapsulation controls access to object state.
# - @property creates attribute-style getters; @name.setter defines setters.
# - Inheritance reuses and extends parent behavior; super() calls parent logic.
# - Polymorphism lets different classes respond to the same method call.
# - Abstraction defines essential interfaces and hides implementation details.
# - __repr__ describes an object; repr() calls it; !r formats values safely.
# - Docstrings document code; __doc__ exposes a docstring.
# - isinstance includes subclasses; type checks the exact class.
# - Custom exceptions can preserve a message and attach useful context.
# - Type hints document expected types but do not normally validate values.
