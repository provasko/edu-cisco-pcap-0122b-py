# Sequence types and mutability

'''
A sequence type is a type of data in Python which is able to store more than one value 
(or less than one, as a sequence may be empty), and these values can be sequentially (hence the name) 
browsed, element by element.

Mutable data can be freely updated at any time
'''

# A tuple is an immutable sequence type.

'''
The first and the clearest distinction between lists and tuples is the syntax used to create them - 
tuples prefer to use parenthesis, whereas lists like to see brackets, although it's also possible 
to create a tuple just from a set of values separated by commas.
'''

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

empty_tuple = ()

one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

