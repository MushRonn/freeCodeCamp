# Understanding Functions and Scope

# name = input('What is your name?') 
# print('Hello', name)


# int() converts a number, a boolean, or a string representing an integer into an integer:

print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 

# Defining and Calling Functions
def hello():
    print('Hello World')
    
# Using Parameters and Arguments
def calculate_sum(a, b):
    print(a + b)
    
calculate_sum(3, 1) # 4

# Returning Values From Functions

def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None

# Scope in Python and How Does it Work?

tax_rate = 0.1

def calculate_tax(price):
    tax = price * tax_rate
    return tax

print(calculate_tax(50)) # 5.0
print(tax_rate) # 0.1
# print(tax) # NameError: name 'tax' is not defined