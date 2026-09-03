#input function is used to take input from the user
#By default, the input function python takes values in the form of string. python automatically converts that value(of any datatype) into a string format.
#input function waits for you until you input some value
input('hey, how are you doing?')
print('---------------------------------------------------')
print('\n')


#the value given by the user as an input gets stored in the ans variable
ans = input('how are you doing?')
print(ans)
print(f'Wilson is doing {ans}')
print('---------------------------------------------------')
print('\n')


#python takes value in the form of a string
num = input('enter a number')
print(type(num))
#here, no need to explicitly type convert the num value into string type because num is already of a string because of input function
print('my umbrella has'+' '+num+' '+'colors')
print('---------------------------------------------------')
print('\n')


#explicitly typeconversion of string into integer type
num1 = input('enter number 1: ')
num2 = input('enter number 2: ')
sum1 = int(num1) + int(num2)
print(sum)
#another way
num3 = int(input('enter number 3: '))
num4 = int(input('enter number 4: '))
sum2 = num3 + num4
print(sum2)
print('---------------------------------------------------')
print('\n')