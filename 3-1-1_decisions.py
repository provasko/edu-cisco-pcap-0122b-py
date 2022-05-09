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

if year % 400 = 0:
    print("Leap year")
elif year % 100 = 0:
    print("Common year")
elif year % 4 = 0:
    print("Leap year")
else:
    print("Common year")


