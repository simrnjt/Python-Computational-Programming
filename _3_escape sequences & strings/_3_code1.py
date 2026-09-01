#single quotes and double quotes strings
print('hello china')
print("hello china")
print("hello 'japan'")
print('hello "singapore"')
print("--------------------------------------------------------")
print('\n')

# \' escape sequences is used in the case of single quotes
# \'' escape sequences is used in the case of double quotes
print('hi, I\'m Rohan')
print("hi, I\'m Alice")
print('yellow \'car\'')
print("Hi, \"Switzerland\"")
print("----------------------------------------------------------")
print('\n')

#escape sequences for a new line('\n')
#this creates a new line between the two words Milkeyway and Galaxy
print('Milkeyway\nGalaxy')
print('tokyo \nuniversity')
print('osaka \n university')
print('okinawa\n institute')
print("-----------------------------------------------------------")
print('\n')

#tab escape sequence(\t)
print('name:\tSamarth')
print('course:\toperating system')
print('age:\t19')
print("----------------------------------------------------------")
print('\n')

#backspace escape sequence (\b)
# The cursor moves back over the 'o', and 'o' is overwritten by 'W'
print("Hello\bWorld")
# Output in most terminals: HellWorld
print("------------------------------------------------------------")
print('\n')

#double backslash escape sequences
#to print a single backslash, use two backslashes
print('\\')
#to print two backslashes, use four backslashes
print('\\\\')
print('\\\\\\')
#using raw string i.e. r, to treat the backslashes not as a backslash but only as a string
print(r'\\')
print(r"\\")
#here, we are combining the raw strig with the normal backslash printing
print(r"\\" + "\\")