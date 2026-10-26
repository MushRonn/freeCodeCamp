# Using Comparison Operators

# ==	Equal	Checks if two values are equal
# !=	Not equal	Checks if two values are not equal
# >	    Greater than	Checks if the value on the left is greater than the value on the right
# < 	Less than	Checks if the value on the left is less than the value on the right
# >=	Greater than or equal	Checks if the value on the left is greater than or equal to the value on the right
# <=	Less than or equal	Checks if the value on the left is less than or equal to the value on the right
 
print(3 > 4) 
print(3 == 4) 
print(4 == 4) 
print(3 != 4) 
print(3 >= 4) 
print(3 <= 4) 

# Using If conditions

#if condition: 
#      pass # Code to execute if met the condition or True

age = 12

if age >= 18:
    print('You are adult')
else:
    print('Not old Enough')

# Can also experience IndentionError

# if condition1:
#    pass # Code to execute if condition1 is True
# elif condition2:
    #pass # Code to execute if condition1 is False and condition2 is True
# else:
#    pass # Code to execute if all conditions are False

age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant')
    

# Using more examples with more complex and conditional statements
# starting to understand how True and elif (If else) condition is used

is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote')
    else:
        print('You are not eligible to vote')
else:
    print('You are not eligible to vote')
    
# More examples
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True

# Using "And" Operator 

is_citizen = True
age = 25

print(is_citizen and age) 

# Using more "AND"
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
    
# Using "OR" Operator

age = 19
is_employed = False

print(age or is_employed) # 19

# If you need to check if one or more expressions is True, then you can use the or operator in a conditional like this:

age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')
    
# Using "NOT" Operator

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')
    

# The not Operator
# The last operator we will look at is the not operator which takes a single operand and 
# inverts its boolean value. It converts truthy values to False and falsy values to True. 
# Unlike the previous operators we looked at, not always returns True or False.

print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy