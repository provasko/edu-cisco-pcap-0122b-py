# Dictionary

'''
The dictionary is another Python data structure. It's not a sequence type (but can be easily adapted 
to sequence processing) and it is mutable.
'''

'''
This means that a dictionary is a set of key-value pairs. Note:

- each key must be unique - it's not possible to have more than one key of the same value;
- a key may be any immutable type of object: it can be a number (integer or float), or even a string, 
but not a list;
- a dictionary is not a list - a list contains a set of numbered values, while a dictionary holds 
pairs of values;
- the len() function works for dictionaries, too - it returns the numbers of key-value elements in 
the dictionary;
- a dictionary is a one-way tool - if you have an English-French dictionary, you can look for 
French equivalents of English terms, but not vice versa.
'''

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary['cat'])
print(phone_numbers['Suzy'])


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)


# modifying and adding values

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)

# Tuples and dictionaries can work together

school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break

    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)


# Key takeaways: tuples

'''
Tuples are ordered and unchangeable (immutable) collections of data. 
They can be thought of as immutable lists. They are written in round brackets:
'''
my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)

'''
You can create an empty tuple like this:
'''
empty_tuple = ()
print(type(empty_tuple))    # outputs: <class 'tuple'>

'''
A one-element tuple may be created as follows:
'''
one_elem_tuple_1 = ("one", )    # Brackets and a comma.
one_elem_tuple_2 = "one",       # No brackets, just a comma.

'''
You can access tuple elements by indexing them:
'''
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3])    # outputs: [3, 4]

'''
Tuples are immutable, which means you cannot change their elements (you cannot append tuples, 
or modify, or remove tuple elements). The following snippet will cause an exception:
However, you can delete a tuple as a whole:
'''
my_tuple = 1, 2, 3,
del my_tuple
print(my_tuple)    # NameError: name 'my_tuple' is not defined

# Example 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)

# Example 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)

# Example 3
tuple_3 = (1, 2, 3, 5)
print(len(tuple_3))

# Example 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2

print(tuple_4)
print(tuple_5)

'''
You can also create a tuple using a Python built-in function called tuple(). 
This is particularly useful when you want to convert a certain iterable (e.g., 
a list, range, string, etc.) to a tuple:
'''

my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>

'''
By the same fashion, when you want to convert an iterable to a list, you can use a Python 
built-in function called list():
'''

tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list))    # outputs: <class 'list'>

# Key takeaways: dictionaries

