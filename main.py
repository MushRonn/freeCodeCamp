#testing code only 

my_int_1 = 56
my_int_2 = 12
print(type(my_int_1))
print(type(my_int_2))

#addition
sum_ints = my_int_1 + my_int_2
print('Integer Addition: ', sum_ints)

#subtraction
diff_ints = my_int_1 - my_int_2
print('Integer Subtraction: ', diff_ints)

#multiplication
prod_ints = my_int_1 * my_int_2
print('Integer Multiplication: ', prod_ints)

#division
div_ints = my_int_1 / my_int_2
print('Integer Division: ', div_ints)

#working with floats
my_float_1 = 5.4
my_float_2 = 12.0

print(type(my_float_1))
print(type(my_float_2))

#addition
sum_floats = my_float_1 + my_float_2
print('Float Addition: ', sum_floats)

#subtraction
diff_floats = my_float_1 - my_float_2
print('Float Subtraction: ', diff_floats)

#multiplication
prod_floats = my_float_1 * my_float_2
print('Float Multiplication: ', prod_floats)

#division
div_floats = my_float_1 / my_float_2
print('Float Division: ', div_floats)

#mixing integers and floats
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float
print('Sum of Integer and Float: ', sum_int_and_float)
print(type(sum_int_and_float))

#performing complex arithmetic operations
#using modulo operator (%)
mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo: ', mod_ints)
print('Float Modulo: ', mod_floats)

#using floor division operator (//)
floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division: ', floor_div_ints)
print('Float Floor Division: ', floor_div_floats)

#using exponentiation operator (**)
exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation: ', exp_ints)
print('Float Exponentiation: ', exp_floats)

#converting data into integers or floats
#converting int to float
my_new_int = 56
my_new_float = float(my_new_int)

print(my_new_float)
print(type(my_new_float))

#converting float to int
my_new_float_1 = 12.92563
my_new_int_1 = int(my_new_float_1)

print(my_new_int_1)
print(type(my_new_int_1))

#converting string to int or float
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))
print(converted_float, type(converted_float))

#rounding numbers
my_new_int_2 = 4.798
my_new_int_3 = 4.253

rounded_int_2 = round(my_new_int_2)
rounded_int_3 = round(my_new_int_3)

print(rounded_int_2)
print(rounded_int_3)

#AUGMENTED ASSIGNMENT OPERATORS
print('AUGMENTED ASSIGNMENT OPERATORS')
my_var = 10
my_var += 5 
print(f'Sum Example: {my_var}')

my_var = 10
my_var -= 5
print(f'Subtraction Example: {my_var}')

my_var = 10
my_var *= 5
print(f'Multiplication Example: {my_var}')

my_var = 10
my_var /= 5
print(f'Division Example: {my_var}')

#using floor division
total_pages = 23
total_pages //= 5
print(total_pages)

#using modulo operator
bits = 35
bits %= 2
print(bits)

#using exponentiation operator
my_var = 2
my_var **= 3
print(my_var)

#using augmented assignment operators with strings
greet = 'Hello'
greet += ', World!'
print(greet)

#using augmented assignment operators with strings multiplication
greet = 'Hello'
greet *= 3
print(greet)

greet = 'Hello'
greet -= 3
print(greet)  #this is TypeError because strings do not support subtraction

greet = 'Hello'
greet /= 3
print(greet)  #this is TypeError because strings do not support division