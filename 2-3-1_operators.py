print(2+2)

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)

print(14 % 4)
print(12 % 4.5)

print(-4 + 4)
print(-4. + 8)

# Operators and their priorities
print(2 + 3 * 5)
print(9 % 6 % 2)
print(2 ** 2 ** 3)

'''

Priority	Operator	
1	**	
2	+, - (note: unary operators located next to the right of the power operator bind more strongly)	unary
3	*, /, //, %	
4	+, -	binary
'''

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

# Key takeaways

'''
1. An expression is a combination of values (or variables, operators, calls to functions ‒ 
you will learn about them soon) which evaluates to a certain value, e.g., 1 + 2.

2. Operators are special symbols or keywords which are able to operate on the values and perform 
(mathematical) operations, e.g., the * operator multiplies two values: x * y.

3. Arithmetic operators in Python: + (addition), - (subtraction), * (multiplication), / (classic 
division ‒ always returns a float), % (modulus ‒ divides left operand by right operand and returns 
the remainder of the operation, e.g., 5 % 2 = 1), ** (exponentiation ‒ left operand raised to the 
power of right operand, e.g., 2 ** 3 = 2 * 2 * 2 = 8), // (floor/integer division ‒ returns a number 
resulting from division, but rounded down to the nearest whole number, e.g., 3 // 2.0 = 1.0)

4. A unary operator is an operator with only one operand, e.g., -1, or +3.

5. A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.

6. Some operators act before others – the hierarchy of priorities:

the ** operator (exponentiation) has the highest priority;
then the unary + and - (note: a unary operator to the right of the exponentiation operator binds more 
strongly, for example: 4 ** -1 equals 0.25)
then *, /, //, and %;
and, finally, the lowest priority: the binary + and -.
7. Subexpressions in parentheses are always calculated first, e.g., 15 - 1 * (5 * (1 + 2)) = 0.

8. The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.

'''

print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
