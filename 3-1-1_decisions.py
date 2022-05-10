var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)

'''
Priority	Operator	
1	        +, -	unary
2	        **	
3	        *, /, //, %	
4	        +, -	binary
5	        <, <=, >, >=	
6	        ==, !=
'''

if sheep_counter >= 120:  # Evaluate a test expression
    sleep_and_dream()  # Execute if test expression is True

if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
feed_the_sheepdogs()

if true_or_false_condition:
    perform_if_condition_true
else:
    perform_if_condition_false

if the_weather_is_good:
    go_for_a_walk()
else:
    go_to_a_theater()
have_lunch()

if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()


# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)


# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02

if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")


year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Common year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Common year")


#SUMMARY

# The comparison (or the so-called relational) operators are used to compare values. 
# The table below illustrates how the comparison operators work, assuming that 
x = 0, y = 1, z = 0

x == y  # False
x == z  # True

x != y  # True
x != z  # False

x > y  # False
y > z  # True

x < y  # True
y < z  # False

x >= y  # False
x >= z  # True
y >= z  # True

x <= y  # True
x <= z  # True
y <= z  # False

# When you want to execute some code only if a certain condition is met, you can use a conditional statement:

x = 10

if x == 10:  # condition
    print("x is equal to 10")  # Executed if the condition is True.


x = 10

if x > 5:  # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10:  # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10:  # condition three
    print("x is equal to 10")  # Executed if condition three is True.



x = 10

if x < 10:  # Condition
    print("x is less than 10")  # Executed if the condition is True.

else:
    # Executed if the condition is False.
    print("x is greater than or equal to 10")


x = 10

if x > 5:  # True
    print("x > 5")

if x > 8:  # True
    print("x > 8")

if x > 10:  # False
    print("x > 10")

else:
    print("else will be executed")

# Each if is tested separately. The body of else is executed if the last if is False.

x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("else will not be executed")

# If the condition for if is False, the program checks the conditions of the subsequent elif blocks - 
# the first elif block that is True is executed. If all the conditions are False, the else block 
# will be executed.


# Nested

x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")


