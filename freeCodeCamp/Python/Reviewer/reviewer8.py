# PYTHON CLASSES AND OBJECTS REVIEWER
# =================================
# A class is a reusable blueprint that defines data (attributes) and actions
# (methods). An object is one specific instance created from a class.
# Think: Dog is the class; a dog named Jack is an object.


# 1. DEFINING A CLASS, __init__, AND self
# --------------------------------------
# Class names conventionally use PascalCase: Dog, ShoppingCart.
# __init__ runs automatically when an object is created. `self` refers to
# the particular object being initialized and is the first method parameter.
# Python supplies self automatically in a call such as Dog('Jack', 3).
class Dog:
    species = 'Canis familiaris'  # Class attribute, shared by all Dog objects.

    def __init__(self, name, age):
        self.name = name           # Instance attributes; each dog has its own.
        self.age = age

    def bark(self):                # Instance method: an action using this dog.
        print(f'{self.name.upper()} says woof woof!')


dog1 = Dog('Jack', 3)
dog2 = Dog('Thatcher', 5)

dog1.bark()  # JACK says woof woof!
dog2.bark()  # THATCHER says woof woof!
print(dog1.name)       # Jack
dog1.name = 'Max'      # Attributes can be read or updated with dot notation.
print(dog1.name)       # Max
print(Dog.species)     # Can access a class attribute from the class.
print(dog2.species)    # Or from an instance.

# Class vs. object:
# - Dog is the class (the reusable template).
# - dog1 and dog2 are separate objects (instances) with their own data.
# - `self.name` is per object; `species` is shared as a class attribute.


# 2. METHODS AND RETURN VALUES
# ----------------------------
# A method is a function defined inside a class. Use dot notation to call it.
# Methods can print a message or return a value for the caller to use.
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def describe(self):
        return f'This car is a {self.color} {self.model}'


my_car_1 = Car('red', 'Tesla Model S')
my_car_2 = Car('green', 'Lamborghini Revuelto')
print(my_car_1.describe())  # This car is a red Tesla Model S
print(my_car_2.describe())  # This car is a green Lamborghini Revuelto


# 3. DYNAMIC ATTRIBUTE FUNCTIONS
# ------------------------------
# Use these when the attribute name is stored in a string or chosen at runtime.
class Pet:
    def __init__(self, name):
        self.name = name


pet = Pet('Jack')
print(getattr(pet, 'name'))                 # Jack
print(getattr(pet, 'age', 'unknown'))       # unknown (default if missing)
# getattr(pet, 'age')                       # Raises AttributeError: no default.
setattr(pet, 'age', 3)                      # Creates or updates an attribute.
print(hasattr(pet, 'age'))                  # True
print(getattr(pet, 'age'))                  # 3
delattr(pet, 'age')                         # Deletes the attribute.
print(hasattr(pet, 'age'))                  # False

# dir(object) lists attribute and method names. callable(value) tells whether
# a value can be called, which can help separate methods from data attributes.
pet_names = [name for name in dir(pet) if not name.startswith('__')]
print([name for name in pet_names if callable(getattr(pet, name))])
print([name for name in pet_names if not callable(getattr(pet, name))])


# 4. DUNDER (MAGIC) METHODS
# -------------------------
# Dunder methods have double underscores around their names. Python calls them
# behind the scenes for built-in operations such as str(), len(), and ==.
# Without custom methods, a class uses default behavior where available.
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages == other.pages


book1 = Book('Built Wealth Like a Boss', 420)
book2 = Book('Another Book', 420)
print(len(book1))       # 420, from __len__
print(str(book1))       # 'Built Wealth Like a Boss' has 420 pages, from __str__
print(book1)            # print() uses the readable __str__ result.
print(book1 == book2)  # True, because __eq__ compares page counts.

# Common dunder method connections:
# __str__     -> str(object), print(object)
# __len__     -> len(object)
# __eq__      -> object1 == object2
# __add__     -> object1 + object2
# __sub__     -> object1 - object2
# __mul__     -> object1 * object2
# __truediv__ -> object1 / object2
# __lt__      -> object1 < object2
# __gt__      -> object1 > object2
# __iter__    -> iterating over an object
# __next__    -> getting the next item from an iterator
# Calling dunder methods indirectly (len(book1)) is the usual style.


# 5. REAL-WORLD EXAMPLE: A SHOPPING CART
# --------------------------------------
# __len__, __getitem__, __contains__, and __iter__ let a Cart work with
# familiar built-in operations and loops.
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)


cart = Cart()
cart.add('Laptop')
cart.add('Mouse')
print(len(cart))                # 2
print('Laptop' in cart)         # True
print(cart[0])                  # Laptop
print(cart.list_items())        # ['Laptop', 'Mouse']
for item in cart:
    print(item)


# 6. OBJECTS WORKING TOGETHER
# ---------------------------
# Objects can be passed as arguments and stored in other objects' attributes.
# Here Email stores User objects, and each User owns an Inbox object.
class Email:
    def __init__(self, sender, receiver, body):
        self.sender = sender        # A User object.
        self.receiver = receiver    # Another User object.
        self.body = body


class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)


class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()        # Each user gets a separate Inbox object.


sender = User('Ada')
receiver = User('Grace')
email = Email(sender, receiver, 'Hello!')
receiver.inbox.receive_email(email)
print(receiver.inbox.emails[0].body)         # Hello!
print(receiver.inbox.emails[0].sender.name)  # Ada
# Chained dot notation follows object attributes: receiver.inbox.emails.


# 7. WORKING WITH DATES AND TIMES
# -------------------------------
# datetime.datetime.now() returns a datetime object for the current local time.
# Store it on an instance to remember when that object was created.
import datetime


class TimestampedMessage:
    def __init__(self, body):
        self.body = body
        self.timestamp = datetime.datetime.now()


message = TimestampedMessage('Hello!')
# strftime() formats a datetime object as text. Common codes:
# %Y = four-digit year    %m = month       %d = day
# %H = 24-hour hour       %M = minute      %S = second
print(message.timestamp.strftime('%Y-%m-%d %H:%M:%S'))
print(message.timestamp.strftime('%d/%m/%Y'))
# Separators such as -, /, :, and spaces are written literally in the format.

# MY SCORE = 100%
# Means I got all 10 questions right