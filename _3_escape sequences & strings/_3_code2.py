#treating escape sequences as a normal text
#i.e.print the new line escape sequence (\n) as a normal text only
print('King-1 \\n King-2')
#now, print the backslash and the second text part on a new line
#here, \\ will become ---> \, so \ will get printed
    #and \n denotes ---> new line escape sequence
print('yellow1 \\\n yellow2')
print('------------------------------------------------')
print('\n')


#print single apostrophe symbol i.e. single quote
#here, we have first print the single quote using single quotes at the end points.
print('\'')
#here, we have first print the single quote using double quotes at the end points.
print("\'")
print('------------------------------------------------')
print('\n')


#print double apostrophe symbol i.e. double quotes
#here, we have first print the double quote using single quotes at the end points.
print('\"')
#here, we have first print the double quote using double quotes at the end points.
print("\"")
print('------------------------------------------------')
print('\n')


#print single quote and double quote together
print('\" \'')
print("\" \'")
print('------------------------------------------------')
print('\n')


#print backslash with double apostrophe & backslash with single apostrohpe
print('\\\" \\\'')
print('------------------------------------------------')
print('\n')


#print backslash with double apostrophe & backslash with single apostrohpe using Raw Strings Concept
print(r'\" \'')
print('------------------------------------------------')
print('\n')


#usage of new line(\n) escape sequences to print a full sentence
print("Hi, My name is 'Roy'\nI'm 19 years old\nI'm 'Chinese'")
print('------------------------------------------------')
print('\n')


#just print these sentences
print("hi, i'm from USA\n")
print("hello, i'm from japan\n")