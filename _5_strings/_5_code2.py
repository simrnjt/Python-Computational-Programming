#string
s1 = 'oskar is my new dog.'
s2 = 'Its weight in Kg is'
weight = 35
#explicitly type convert the integer type value to string type
print(s1+' '+s2+' '+str(weight))
print('---------------------------------------------------')
print('\n')


#string formatting using f-string syntax
age = 10
weight = 50
print(f'yesterday, I saw a one boy with age {age} and weight {weight}.')
print(f'yesterday, I saw a one boy with age {age-3} and weight {weight+20}.')
print('---------------------------------------------------')
print('\n')


#string concatenation
s1 = '5'
s2 = '4'
print(s1+s2)
print('---------------------------------------------------')
print('\n')


#string duplication
#the string literal '7' gets repeated here 5 times.
s3 = '7'
print(s3*5)