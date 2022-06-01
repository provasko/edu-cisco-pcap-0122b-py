'''
We'll show you how to declare such multi-value variables. 
We'll do this with the example we just suggested. 
We'll write a program that sorts a sequence of numbers. 
We won't be particularly ambitious - we'll assume that there are exactly five numbers.

Let's create a variable called numbers; it's assigned with not just one number, 
but is filled with a list consisting of five values (note: the list starts with an open square 
bracket and ends with a closed square bracket; the space between the brackets is filled with 
five numbers separated by commas).
'''

numbers = [10, 5, 7, 2, 1]

# Indexing lists

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("New list content: ", numbers)  # Current list content.


numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list content:", numbers)  # Printing current list content.

# Accessing list content

print(numbers[0])  # Accessing the list's first element.

print(numbers)  # Printing the whole list.

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList length:", len(numbers))  # Printing the list's length.

del numbers[1]
print(len(numbers))
print(numbers)

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###


# Negative indices are legal

numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])


# Functions vs. methods

'''
A method is a specific kind of function - it behaves like a function and looks like a function, 
but differs in the way in which it acts, and in its invocation style.

A function doesn't belong to any data - it gets data, it may create new data and it (generally) 
produces a result.

A method does all these things, but is also able to change the state of a selected entity.

A method is owned by the data it works for, while a function is owned by the whole code.


This also means that invoking a method requires some specification of the data from which 
the method is invoked.

It may sound puzzling here, but we'll deal with it in depth when we delve into object-oriented 
programming.

In general, a typical function invocation may look like this:
'''

result = function(arg)


'''
A typical method invocation usually looks like this:
'''

result = data.method(arg)

'''
Note: the name of the method is preceded by the name of the data which owns the method. 
Next, you add a dot, followed by the method name, and a pair of parenthesis enclosing the arguments.

The method will behave like a function, but can do something more - it can change the internal 
state of the data from which it has been invoked.
'''

# Adding elements to a list: append() and insert()

list.append(value)

'''
The insert() method is a bit smarter - it can add a new element at any place in the list, 
not only at the end.
'''

list.insert(location, value)

'''
Add the following snippet after the last line of code in the editor:
'''

numbers.insert(1, 333)

# Adding elements to a list: continued
'''
We've modified the snippet a bit:
'''

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

# Making use of lists

