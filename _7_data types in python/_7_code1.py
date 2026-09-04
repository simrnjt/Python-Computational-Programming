#discussing data types in python
#in python, everything is a class, even the primitive data types like integer, string, boolean, etc is a class.
#every value is an instance of a class
#{} in python are used to fetch the value.


#integer data type in python
x = 123
print(f'Type: {type(x)}')
print(f'val: {x}')
print('----------------------------------------------------')
print('\n')


#float data type
y = 1.5
print(f'Type: {type(y)}')
print(f'val: {y}')
print('----------------------------------------------------')
print('\n')


#boolean data type
b1 = True
b2 = False
print(f'Type: {type(b1)}')
print(f'val: {b1}')
#boolean evaluation in boolean mathematics
print(True and False)
print(True and True)
print(False and False)
print(True or False)
print(True or True)
print(False or False)
print(not True)
print(not False)
print('hey' == 'hey')
print('hi' == 'hey')
print('----------------------------------------------------')
print('\n')


#string data type
#string literal can be defined with a single quote(') or a double quote(") or tripe quotes(''' or """)
s1 = 'hello there'
s2 = "hi, I'm here!"
s3 = 'hi, "Sam"'
s4 = "hey, 'rohan'"
s5 = '''hi, i'm python'''
print(f'Type: {type(s1)}')
print(f'Value: {s1}')
print(s2, s3, s4, s5)
print('----------------------------------------------------')
print('\n')


#complex numbers in python
#complex numbers in python use 'j' to denote the imaginary part
num1 = 1 - 3j
print(f'Type: {type(num1)}')
print(f'Vale: {num1}')
print(num1.real, num1.imag)
#explicitly, type convert into integers
print(int(num1.real), int(num1.imag))
print('----------------------------------------------------')
print('\n')


#dynamic typing in python
#in python while the value that a variable points to has a type, the variable itself has no strict type in it's definition. you can re-use the same variable to point to an object of a different type.
w = 11
print(f'Type: {type(w)}')
w = 'Tree'
print(f'Type: {type(w)}')
print('----------------------------------------------------')
print('\n')


#None data type. None represents the absence of a value.
t = None
print(f'Type: {type(t)}')
print(f'Value: {t}')
print('----------------------------------------------------')
print('\n')



#explicit typecast the string to integer
a = '10'
print(f'Type: {type(a)}')
a = int(a)
print(f'Type: {type(a)}')
print('----------------------------------------------------')
print('\n')


#explicit typecast the integer to string
b = 10
b = str(b)
print(f'Type: {type(b)}')
print('----------------------------------------------------')
print('\n')


#convert string to float
st = '12.5'
fNum = float(st)
print(f'Type: {type(fNum)}')
print('----------------------------------------------------')
print('\n')


#convert boolean value to integer value
b1 = True
b2 = False
x = int(b1)
print(x)
y = int(b2)
print(y)