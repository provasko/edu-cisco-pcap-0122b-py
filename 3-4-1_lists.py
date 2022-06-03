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

'''
the list is assigned a sequence of five integer values;
the i variable takes the values 0, 1, 2, 3, and 4, and then it indexes the list, 
selecting the subsequent elements: the first, second, third, fourth and fifth;
each of these elements is added together by the += operator to the total variable, 
giving the final result at the end of the loop;
note the way in which the len() function has been employed - it makes the code 
independent of any possible changes in the list's content.
'''

# The second face of the for loop

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

'''
the for instruction specifies the variable used to browse the list (i here) followed 
by the in keyword and the name of the list being processed (my_list here)
the i variable is assigned the values of all the subsequent list's elements, 
and the process occurs as many times as there are elements in the list;
this means that you use the i variable as a copy of the elements' values, 
and you don't need to use indices;
the len() function is not needed here, either.
'''

# Lists in action

variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2

'''
If you do something like this, you would lose the value previously stored in variable_2. 
Changing the order of the assignments will not help. You need a third variable that serves 
as an auxiliary storage.
'''

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

# Python offers a more convenient way of doing the swap - take a look:

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

# Now you can easily swap the list's elements to reverse their order:

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)


'''
we've assigned the length variable with the current list's length (this makes our code 
a bit clearer and shorter)
we've launched the for loop to run through its body length // 2 times (this works well 
for lists with both even and odd lengths, because when the list contains an odd number of elements, 
the middle one remains untouched)
we've swapped the ith element (from the beginning of the list) with the one with an index equal to 
(length - i - 1) (from the end of the list); in our example, for i equal to 0 the (lenght - i - 1) 
gives 4; for i equal to 1, it gives 3 - this is exactly what we needed.
'''


# Key takeaways

'''
1. The list is a type of data in Python used to store multiple objects. It is an ordered and mutable 
collection of comma-separated items between square brackets, e.g.:
'''

my_list = [1, None, True, "I am a string", 256, 0]

'''
2. Lists can be indexed and updated, e.g.:
'''

my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0

my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

my_list.insert(0, "first")
my_list.append("last")
# outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']
print(my_list)

'''
3. Lists can be nested, e.g.:
'''

my_list = [1, 'a', ["list", 64, [0, 1], False]]

'''
4. List elements and lists can be deleted, e.g.:
'''

my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]

del my_list  # deletes the whole list

'''
5. Lists can be iterated through using the for loop, e.g.:
'''

my_list = ["white", "purple", "blue", "yellow", "green"]

for color in my_list:
    print(color)

'''
6. The len() function may be used to check the list's length, e.g.:
'''

my_list = ["white", "purple", "blue", "yellow", "green"]
print(len(my_list))  # outputs 5

del my_list[2]
print(len(my_list))  # outputs 4

'''
7. A typical function invocation looks as follows: result = function(arg), while a typical 
method invocation looks like this:result = data.method(arg).
'''
