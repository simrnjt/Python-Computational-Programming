# Expressions in Python


#Constant expressions - these are the expressions that have constant values only
x = 19 + 1.3
print(f'type: {type(x)}')
print(f'value: {x}')
print('----------------------------------')
print('\n')


#arithmetic expression - an expression is a combination of numeric values, operators and sometimes parathesis.
x = 4
y = 5
add = x + y
sub = x - y
product = x * y
div1 = x / y
div2 = x//y
print(add, sub, product, div1, div2)
print('----------------------------------')
print('\n')


# relational expression - also called as boolean expressoin because it produces a boolean output at the end
a = 8
b = 1
c = 9
d = 10
ans = (a + b) >= (c - d)
print(ans)
print('----------------------------------')
print('\n')


#logical expression - these are kinds of expressions that the result is either True or False. it's basically specifies one or more condition
exp1 = (10 == 9)
print(f'type: {type(exp1)}')
print(f'value:{exp1}')

exp2 = (11 < 9)
print(exp2)

exp3 = (11 == 9 or 4 > 1)
print(exp3)

exp4 = (11 > 9 and 2 > 3)
print(exp4)

exp5 = (11 > 9 or 2 > 3)
print(exp5)

exp6 = not(5 == 5)
print(exp6)

exp7 = not(5 != 7)
print(exp7)
print('----------------------------------')
print('\n')


#bitwise expression - these are the kind of expressions in which computations are performed at bit level.
t = 12
#Right Shift Operator (>>)
#The right shift operator moves all bits to the right and effectively divides the number by powers of two.
z = t >> 2
#Left Shift Operator (<<)
# The left shift operator moves all bits to the left, fills the rightmost vacant positions with zeros, and effectively multiplies the number by powers of two
h = t << 1
print(z)
print(h)