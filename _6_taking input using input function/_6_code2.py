#take multiple inputs in a single line using split function
#always give a space between every input value
#split() → by default, splits the string wherever it finds whitespace characters (spaces, tabs, or newlines).
name, gender, age = input('enter your data: ').split()
print(name, gender, age)
print('---------------------------------------------------')
print('\n')


#split the input using comma character
course, university = input('enter your data: ').split(',')
print(course, university)
print('---------------------------------------------------')
print('\n')


#split the input using hyphen character
color, umbrellaSize = input('enter your data: ').split('-')
print(color, umbrellaSize)
print('---------------------------------------------------')
print('\n')