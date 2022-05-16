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
