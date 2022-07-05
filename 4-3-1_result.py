def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")


happy_new_year()

happy_new_year(False)

value = None
if value is None:
    print("Sorry, you don't carry any value")

print(strange_function(2))
print(strange_function(1))


def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum([5, 4, 3]))

# Effects and results: lists and functions


def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list


print(strange_list_fun(5))


def is_year_leap(year):
    #
    # put your code here
    #


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr, "->", end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


def is_year_leap(year):
    #
    # Your code from LAB 4.3.1.6.
    #


def days_in_month(year, month):
    #
    # Write your new code here.
    #


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


def is_year_leap(year):
    #
    # Your code from LAB 4.3.1.6.
    #


def days_in_month(year, month):
    #
    # Your code from LAB 4.3.1.7.
    #


def day_of_year(year, month, day):
    #
    # Write your new code here.
    #


print(day_of_year(2000, 12, 31))


def is_prime(num):
    #
    # Write your code here.
    #


for i in range(1, 20):
	if is_prime(i + 1):
		print(i + 1, end=" ")
print()


def liters_100km_to_miles_gallon(liters):
    #
    # Write your code here.
    #


def miles_gallon_to_liters_100km(miles):
    #
    # Write your code here
    #


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


# Key takeaways

'''
1. You can use the return keyword to tell a function to return some value. The return statement 
exits the function, e.g.:
'''


def multiply(a, b):
    return a * b


print(multiply(3, 4))    # outputs: 12


def multiply(a, b):
    return


print(multiply(3, 4))    # outputs: None

'''
2. The result of a function can be easily assigned to a variable, e.g.:
'''


def wishes():
    return "Happy Birthday!"


w = wishes()

print(w)    # outputs: Happy Birthday!

# Example 1


def wishes():
    print("My Wishes")
    return "Happy Birthday"


wishes()    # outputs: My Wishes


# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"


print(wishes())

# outputs: My Wishes
#          Happy Birthday

'''
3. You can use a list as a function's argument, e.g.:
'''


def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)


hi_everybody(["Adam", "John", "Lucy"])

'''
4. A list can be a function result, too, e.g.:
'''


def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list


print(create_list(5))
