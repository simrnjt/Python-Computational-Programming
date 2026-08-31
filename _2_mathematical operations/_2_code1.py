#here we have imported the entire 'math module', inorder to use the mathematical functions like sqrt, floor, ceil, round, trunc, pi
import math

#Import Specific Functions from math module
#from math import sqrt, pi
from math import pi

#integer addition
print(3+7)
print(5 + (-3))
print('\n')

#complex numbers addition
print( (2 + 6j) + (9 + 4j))
print('\n')

#integer subtraction
print(5-9)
print('\n')

#complex numbes subtraction
print((4 + 7j) - (6 + 11j))
print('\n')

#float division(/), keeps the decimal part
print(7/2)
print('\n')

#integer division(//), eliminates the decimal part
print(9//3)
print('\n')

#integer multiplication
print(5 * 3)
print('\n')

#exponent operator i.e. power
print(5 ** 2)
print('\n')

#square root using exponent function
a = 2 ** 0.5
print(a)
c = 81 ** (1/4)
print(c)
print('\n')

#square root using math function
x = math.sqrt(2)
print(x)
f = math.sqrt(36)
print(f)
print('\n')

#ceil function
#ceil function is also called as the Least Integer Function(LIF)
#LIF or ceil gives the nearest right integer value
y = math.ceil(5.1)
print(y)
w = math.ceil(-2.2)
print(w)
print('\n')

#floor function
#floor function is also known as Greatest Integer Function(GIF)
#GIF or floor gives the nearest left integer value
t = math.floor(4.9)
print(t)
h = math.floor(-2.1)
print(h)
print('\n')

#truncate function
#trunc just drops the fractional part
u = math.trunc(2.34)
print(u)
r = math.trunc(-8.9)
print(r)
print('\n')

#printing the value of PI
print(pi)
print('\n')

#power function
b = math.pow(3, 4)
print(b)
g = math.pow(2, -2)
print(g)
j = math.pow(9, 0.5)
print(j)
print('\n')

#factorial function, factorial is always computed for the postive numbers
k = math.factorial(4)
print(k)
print('\n')

#cube root function
s = math.cbrt(27)
print(s)
p = math.cbrt(-64)
print(p)
print('\n')

#using exponent operator to compute the cube root
#but this only works for the positive numbers
#for negative numbes it returns a complex number
ans = 8 ** (1/3)
print(ans)
print('\n')

#round function
#round function syntax: round(a ** b, j)
#where 'j' denotes upto how many decimal places we want the answer
k = round(2 ** 0.5, 5)
print(k)
e = round(pi, 3)
print(e)
v = round(22/7, 7)
print(v)
print('\n')

#modulo operator, it is used to find the remainder
h = 22 % 5
print(h)
r = -22 % 5
print(r)
print('\n')