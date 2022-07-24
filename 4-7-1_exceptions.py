# When data is not what it should be

'''
Traceback (most recent call last):
  File "code.py", line 1, in 
    value = int(input('Enter a natural number: '))
ValueError: invalid literal for int() with base 10: ''
'''
value = int(input('Enter a natural number: '))
print('The reciprocal of', value, 'is', 1/value)

# The try-except branch

'''
try:
	# It's a place where
	# you can do something
    # without asking for permission.
except:
	# It's a spot dedicated to
    # solemnly begging for forgiveness.
'''

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except:
    print('I do not know what to do.')

# How to deal with more than one exception

'''
Look at the code in the editor. As you can see, we've just introduced the second except branch. 
This is not the only difference – note that both branches have exception names specified. 
In this variant, each of the expected exceptions has its own way of handling the error, 
but it must be emphasized that only one of all branches can intercept the control – 
if one of the branches is executed, all the other branches remain idle.

Additionally, the number of except branches is not limited – you can specify as many or as few 
of them as you need, but don't forget that none of the exceptions can be specified more than once.
'''

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')

