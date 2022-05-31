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

