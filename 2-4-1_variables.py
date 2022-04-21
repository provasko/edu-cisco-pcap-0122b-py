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
