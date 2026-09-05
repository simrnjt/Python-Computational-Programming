#Containers in Python

#list - a mutuable ordered container
fruits = ['apple', 'mango', 'grapes']
fruits.append('banana')
print(f'Type: {type(fruits)}')
print(f'Value: {fruits}')
print('----------------------------------------------')
print('\n')


#tuple - an immutable ordered container
marks = (11, 17, 13)
print(f'Type: {type(marks)}')
print(f'Value: {marks}')
print(marks[0], marks[1])
#this will give error because tuple is immutable
#marks[2] = 15
print('----------------------------------------------')
print('\n')


#dictionary - a key-value pair container
#mutable, ordered, duplicates(only value, not key)
student1 = {'name': 'Aron', 'age': 20}
student1['gender'] = 'Male'
print(f'type: {type(student1)}')
print(f'value: {student1}')
print(student1)
#data changes in student1 dictionary
#key is a string type and value is a list container
student1 = {'name': 'Aron', 'age': 20, 'courseMarks': [12, 15, 19]}
print(student1)
print('----------------------------------------------')
print('\n')


#set - a collection of unique elements
# set is mutuable, unordered, duplicates not allowed
st1 = {1, 3, 5, 1, 8, 9}
print(f'type: {type(st1)}')
print(f'value: {st1}')
print('----------------------------------------------')
print('\n')


#frozenset - immutable set
#frozenset is immutable
fst1 = frozenset([1,2,4])
print(f'type: {type(fst1)}')
print(f'value: {fst1}')
print('----------------------------------------------')
print('\n')


#string - a container of characters
message = "yellow icecream"
print(f'type: {type(message)}')
print(f'value: {message}')
print(message[4], message[1], message[0], message[9])
print('----------------------------------------------')
print('\n')