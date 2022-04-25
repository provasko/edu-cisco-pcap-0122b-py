'''
- the name of the variable must be composed of upper-case or lower-case letters, digits, 
and the character _ (underscore)
- the name of the variable must begin with a letter;
- the underscore character is a letter;
- upper- and lower-case letters are treated as different (a little differently than in the real 
world - Alice and ALICE are the same first names, but in Python they are two different variable names, 
and consequently, two different variables);
- the name of the variable must not be any of Python's reserved words (the keywords - we'll explain 
more about this soon).
'''

# dont use ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
# 'with', 'yield']

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

var = "3.8.5"
print("Python version: " + var)

var = 100
var = 200 + 300
print(var)

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

'''
- create the variables: john, mary, and adam;
- assign values to the variables. The values must be equal to the numbers of fruit possessed by 
John, Mary, and Adam respectively;
- having stored the numbers in the variables, print the variables on one line, and separate each 
of them with a comma;
- now create a new variable named total_apples equal to addition of the three former variables.
print the value stored in total_apples to the console;
- experiment with your code: create new variables, assign different values to them, and perform 
various arithmetic operations on them (e.g., +, -, *, /, //, etc.). 
Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.
'''
john = 1
mary = 3
adam = 9
total_apples = john + mary + adam
print(john, mary, adam, sep=",")
print("Total: " + str(total_apples))

# Shortcut operators
x = 2
x = x * 2
sheep = 0
sheep = sheep + 1

x *= 2
sheep += 1

'''
ake a look at the examples below. Make sure you understand them all.

i = i + 2 * j ⇒ i += 2 * j

var = var / 2 ⇒ var /= 2

rem = rem % 10 ⇒ rem %= 10

j = j - (i + var + rem) ⇒ j -= (i + var + rem)

x = x ** 2 ⇒ x **= 2
'''

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

'''

1. A variable is a named location reserved to store values in the memory. A variable is created or 
initialized automatically when you assign a value to it for the first time. (2.1.4.1)

2. Each variable must have a unique name - an identifier. A legal identifier name must be a non-empty 
sequence of characters, must begin with the underscore(_), or a letter, and it cannot be a Python 
keyword. The first character may be followed by underscores, letters, and digits. Identifiers in 
Python are case-sensitive. (2.1.4.1)

3. Python is a dynamically-typed language, which means you don't need to declare variables in it. 
(2.1.4.3) To assign values to variables, you can use a simple assignment operator in the form of 
the equal (=) sign, i.e., var = 1.

4. You can also use compound assignment operators (shortcut operators) to modify values assigned 
to variables, e.g., var += 1, or var /= 5 * 2. (2.1.4.8)

5. You can assign new values to already existing variables using the assignment operator or one 
of the compound operators, e.g.: (2.1.4.5)

You can combine text and variables using the + operator, and use the print() function to output 
strings and variables
'''
