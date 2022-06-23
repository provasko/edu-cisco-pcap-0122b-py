# Parameterized functions

'''
parameters exist only inside functions in which they have been defined, and the only place where 
the parameter can be defined is a space between a pair of parentheses in the def statement;

assigning a value to the parameter is done at the time of the function's invocation, by specifying 
the corresponding argument.
'''


def message(number):
    print("Enter a number:", number)


message(1)

number = 1234
message(1)
print(number)


def message(what, number):
    print("Enter", what, "number", number)


def message(what, number):
    print("Enter", what, "number", number)


message("telephone", 11)
message("price", 5)
message("number", "number")

# Positional parameter passing

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

# Keyword argument passing

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction(first_name="James", last_name="Bond")
introduction(last_name="Skywalker", first_name="Luke")


# Mixing positional and keyword arguments

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)


adding(1, 2, 3)

# Parametrized functions - more details


def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


introduction("James", "Doe")

introduction("Henry")

introduction(first_name="William")


def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


introduction()

introduction(last_name="Hopkins")


# Key takeaways

'''
1. You can pass information to functions by using parameters. 
Your functions can have as many parameters as you need.
'''


def hi(name):
    print("Hi,", name)

hi("Greg")


def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")

'''
2. You can pass arguments to a function using the following techniques:

positional argument passing in which the order of arguments passed matters (Ex. 1),
keyword (named) argument passing in which the order of arguments passed doesn't matter (Ex. 2),
a mix of positional and keyword argument passing (Ex. 3).
'''

#Ex. 1

def subtra(a, b):
    print(a - b)


subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


#Ex. 2

def subtra(a, b):
    print(a - b)


subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

#Ex. 3

def subtra(a, b):
    print(a - b)


subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3

