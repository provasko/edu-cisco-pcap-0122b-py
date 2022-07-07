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

# How the function interacts with its arguments


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

'''
if the argument is a list, then changing the value of the corresponding parameter doesn't affect 
the list (remember: variables containing lists are stored in a different way than scalars),

but if you change a list identified by the parameter (note: the list, not the parameter!), 
the list will reflect the change.
'''


def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)

