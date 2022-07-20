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
