#Types of Conditional Statements in Python
# 1. If statement
# 2. If-else statement
# 3. If-elif-else


#write a program which takes age as an input and tells whether the user can vote or not
age = int(input("enter the age: "))

if age >= 18:
    print('yes, you can vote')
elif age <= 0:
    print('age is incorrect, enter the correct age!')
else:
    print("no, you can't vote")