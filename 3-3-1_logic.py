# Computer logic
'''
We've used the conjunction and, which means that going for a walk depends on the simultaneous 
fulfilment of these two conditions. In the language of logic, such a connection of conditions 
is called a conjunction. And now another example:

If you are in the mall or I am in the mall, one of us will buy a gift for Mom.
'''

counter > 0 and value == 100


'''
The appearance of the word or means that the purchase depends on at least one of these conditions. 
In logic, such a compound is called a disjunction.

It's clear that Python must have operators to build conjunctions and disjunctions. 
Without them, the expressive power of the language would be substantially weakened. 
They're called logical operators.
'''

'''
One logical conjunction operator in Python is the word and. It's a binary operator with a priority that is lower than the one expressed by the comparison operators. It allows us to code complex conditions without the use of parentheses like this one:
'''
