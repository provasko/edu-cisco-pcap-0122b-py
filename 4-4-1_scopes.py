# Functions and scopes
'''
def scope_test():
    x = 123


scope_test()
print(x)

NameError: name 'x' is not defined
'''


def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

'''
A variable existing outside a function has a scope inside the functions' bodies, 
excluding those of them which define a variable of the same name.

It also means that the scope of a variable existing outside a function is supported 
only when getting its value (reading). Assigning a value forces the creation of the function's 
own variable.
'''

# Functions and scopes: the global keyword

'''
There's a special Python method which can extend a variable's scope in a way which includes 
the functions' bodies (even if you want not only to read the values, but also to modify them).
'''


def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

