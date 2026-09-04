#TypeCasting in Python


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