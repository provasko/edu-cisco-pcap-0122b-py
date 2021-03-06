'''
while conditional_expression:
    instruction_one
    instruction_two
    instruction_three
    :
    :
    instruction_n
'''

'''
if you want to execute more than one statement inside one while, you must (as with if) indent 
all the instructions in the same way;
an instruction or set of instructions executed inside the while loop is called the loop's body;
if the condition is False (equal to zero) as early as when it is tested for the first time, the 
body is not executed even once (note the analogy of not having to do anything if there is nothing to do);
the body should be able to change the condition's value, because if the condition is True at 
the beginning, the body might run continuously to infinity - notice that doing a thing usually 
decreases the number of things to do).
'''

# infinite
while True:
    print("I'm stuck inside a loop.")

# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)


counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)


# LOOP

i = 0
while i < 100:
    # do_something()
    i += 1

# same
for i in range(100):
    # do_something()
    pass

for i in range(10):
    print("The value of i is currently", i)

for i in range(2, 8):
    print("The value of i is currently", i)

for i in range(2, 8, 3):
    print("The value of i is currently", i)

'''
These two instructions are:

break - exits the loop immediately, and unconditionally ends the loop's operation; 
the program begins to execute the nearest instruction after the loop's body;

continue - behaves as if the program has suddenly reached the end of the body; 
the next turn is started and the condition expression is tested immediately.
'''

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")


largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


# Loop control

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


# Loops else

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)


'''
1. There are two types of loops in Python: while and for:

the while loop executes a statement or a set of statements as long as a specified boolean 
condition is true, e.g.:
'''
# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1
'''
the for loop executes a set of statements many times; it's used to iterate over a sequence 
(e.g., a list, a dictionary, a tuple, or a set - you will learn about them soon) or other 
objects that are iterable (e.g., strings). You can use the for loop to iterate over a sequence 
of numbers using the built-in range function. Look at the examples below:

'''
# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)


'''
2. You can use the break and continue statements to change the flow of a loop:

You use break to exit a loop, e.g.:
'''
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

'''
You use continue to skip the current iteration, and continue with the next iteration, e.g.:
'''
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")


'''
3. The while and for loops can also have an else clause in Python. The else clause executes after 
the loop finishes its execution as long as it has not been terminated by break, e.g.:
'''
n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

'''
4. The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: range(start, stop, step), where:

start is an optional parameter specifying the starting number of the sequence (0 by default)
stop is an optional parameter specifying the end of the sequence generated (it is not included),
and step is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)
Example code:
'''
for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

# Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. 

for i in range(0, 11):
    if i % 2 != 0:
        print(i)

# Create a while loop that counts from 0 to 10, and prints odd numbers to the screen.

x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

# Create a program with a for loop and a break statement. The program should iterate over characters 
# in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on 
# one line

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# Create a program with a for loop and a continue statement. The program should iterate over a string 
# of digits, replace each 0 with x, and print the modified string to the screen.

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

# What is the output of the following code?

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

# What is the output of the following code?

n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

# What is the output of the following code?

for i in range(0, 6, 3):
    print(i)
