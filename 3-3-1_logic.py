# Computer logic
'''
We've used the conjunction and, which means that going for a walk depends on the simultaneous 
fulfilment of these two conditions. In the language of logic, such a connection of conditions 
is called a conjunction. And now another example:

If you are in the mall or I am in the mall, one of us will buy a gift for Mom.
'''

# counter > 0 and value == 100


'''
The appearance of the word or means that the purchase depends on at least one of these conditions. 
In logic, such a compound is called a disjunction.

It's clear that Python must have operators to build conjunctions and disjunctions. 
Without them, the expressive power of the language would be substantially weakened. 
They're called logical operators.
'''

'''
One logical conjunction operator in Python is the word and. 
It's a binary operator with a priority that is lower than the one expressed by the comparison operators. 
It allows us to code complex conditions without the use of parentheses like this one:
'''

'''
A disjunction operator is the word or. It's a binary operator with a lower priority than and 
(just like + compared to *). Its truth table is as follows:

'''

'''
In addition, there's another operator that can be applied for constructing conditions. 
It's a unary operator performing a logical negation. Its operation is simple: 
it turns truth into falsehood and falsehood into truth.

This operator is written as the word not, and its priority is very high: 
the same as the unary + and -.
'''

# Logical expressions
'''
Let's create a variable named var and assign 1 to it.
The following conditions are pairwise equivalent:
'''
var = 1
# Example 1:
print(var > 0)
print(not (var <= 0))


# Example 2:
print(var != 0)
print(not (var == 0))

'''
The negation of a conjunction is the disjunction of the negations.

The negation of a disjunction is the conjunction of the negations.
'''

# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q)

# Logical values vs. single bits

'''
Logical operators take their arguments as a whole regardless of how many bits they contain. 
The operators are aware only of the value: zero (when all the bits are reset) means False; 
not zero (when at least one bit is set) means True.

The result of their operations is one of these values: False or True. 
This means that this snippet will assign the value True to the j variable if i is not zero; 
otherwise, it will be False.
'''

i = 1
j = not not i


# Bitwise operators
'''
However, there are four operators that allow you to manipulate single bits of data. 
They are called bitwise operators.

They cover all the operations we mentioned before in the logical context, and one additional operator. 
This is the xor (as in exclusive or) operator, and is denoted as ^ (caret).
'''

# Bitwise operations (&, |, and ^)

'''
& (ampersand) - bitwise conjunction;
| (bar) - bitwise disjunction;
~ (tilde) - bitwise negation;
^ (caret) - bitwise exclusive or (xor).
'''
print("*" * 10)
a = False
b = True
print(a & b)
print(a | b)
print(~ a)
print(a ^ b)

# Logical vs. bit operations: continued

'''
i: 00000000000000000000000000001111
j: 00000000000000000000000000010110
'''
# bit = i & j	00000000000000000000000000000110

'''
i	00000000000000000000000000001111
bitneg = ~i	11111111111111111111111111110000
'''

'''
Each of these two-argument operators can be used in abbreviated form. These are the examples of their equivalent notations:

x = x & y	x &= y
x = x | y	x |= y
x = x ^ y	x ^= y
'''

# SUMMARY

'''
1. Python supports the following logical operators:

and → if both operands are true, the condition is true, e.g., (True and True) is True,
or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
not → returns false if the result is true, and returns true if the result is false, e.g., 
not True is False.
'''

'''
x = 15, which is 0000 1111 in binary,
y = 16, which is 0001 0000 in binary.
will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

& does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
| does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
>> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
<< does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary,

* -16 (decimal from signed 2's complement) -- read more about the Two's complement operation.
'''

