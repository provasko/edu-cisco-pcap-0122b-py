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


