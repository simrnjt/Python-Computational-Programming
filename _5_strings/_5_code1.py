#Strings in python. String is a collection of characters written in single quotes or double quotes
s1 = 'California'
s2 = "Hiroshima"
s3 = '78210149823542002355899'
s4 = '7845iopresfAVCXZWRWR983322'
s5 = '@#%*&8789adfdQWET{]}[/<>'
#this prints all the five strings in a one single line
print(s1,s2,s3,s4,s5)
#this prints all the five strings in a new line
#use the sep='\n' parameter,this tells Python to separate each argument with a line break.
print(s1,s2,s3,s4,s5, sep='\n')
print('---------------------------------------------------')
print('\n')


#string concatenation
s6 = 'rio'
s7 = 'lio'
s8 = 'hio'
#here, the space i.e a white space character is concatenated between the variables, just to have space between their values.
print(s6+' '+s7+' '+s8)
print('---------------------------------------------------')
print('\n')


#another form of string concatenation
s9 = 'Tokyo'
print(s9 + '125')
print('---------------------------------------------------')
print('\n')


#string concatenation by converting a numeric value to a string value
s10 = 'Yokohama'
print(s10 + str(70.123))
s11 = 'Waterfall'
print(s11 + str(-42100))
print('---------------------------------------------------')
print('\n')


#string concatenation by converting the boolean value to string value
s12 = '-...0.12455'
print(s12 + str(True))
s13 = '0....1217899'
print(s13 + str(False))
print('---------------------------------------------------')
print('\n')


#string duplication
s14 = 'yellow/Ice-Cream/0.25'
print(s14 * 5)
#print in a new line
print((s14 + '\n') * 5)
print('---------------------------------------------------')
print('\n')


#print a string five times in a one single line with white space characters
s15 = 'hey'
print((s15 + ' ') * 5)
#find the length of string
s16 = (s15 + ' ') * 5
print(len(s16))
print('---------------------------------------------------')
print('\n')


#print the string
st1 = 'Python'
st2 = 'is very easily'
st3 = 'understandable programming language'
print(st1 + ' ' + st2 + ' ' + st3)