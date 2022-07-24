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

# The default exception and how to use it

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')
except:
    print('Something strange has happened here... Sorry!')

# ZeroDivisionError , they are: /, //, and %.

# ValueError

'''
Expect this exception when you're dealing with values which may be inappropriately used in some context. 
In general, this exception is raised when a function (like int() or float()) receives an argument 
of a proper type, but its value is unacceptable.
'''

# TypeError

'''
This exception shows up when you try to apply a data whose type cannot be accepted in the current context. Look at the example:

short_list = [1]
one_value = short_list[0.5]
'''

# AttributeError

'''
This exception arrives – among other occasions – when you try to activate a method which doesn't exist 
in an item you're dealing with. For example:

short_list = [1]
short_list.append(2)
short_list.depend(3)
'''

# SyntaxError

'''
This exception is raised when the control reaches a line of code which violates Python's grammar. 
It may sound strange, but some errors of this kind cannot be identified without first running the code. 
This kind of behavior is typical of interpreted languages – the interpreter always works in a hurry 
and has no time to scan the whole source code. It is content with checking the code which is 
currently being run. An example of such a category of issues will be presented very soon.

It's a bad idea to handle this exception in your programs. You should produce code that is free of 
\syntax errors, instead of masking the faults you’ve caused.
'''
