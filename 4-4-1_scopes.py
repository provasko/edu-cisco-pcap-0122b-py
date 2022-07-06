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
