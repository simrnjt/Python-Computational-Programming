#for loop
#a for loop purpose is to iterate over a sequence, be it a list,a tuple, a string or range and execute a designated block of code for each item in the sequence.
#range(start, stop, step_size)
#start: default is 0
#stop: iterate upto (stop - 1)
#step_size: jump for each successive number
#for ex: list(range(5, 50, 5)) --> [5,10,15,20,25,30,35,40,45]

#Pb. given a list of voter's age, count the total number of ages greater than or equal to the targetAge
targetAge1 = 20
ageList1 = [10, 21, 20, 18, 20, 16, 22]
count1 = 0
for age in ageList1:
    if age >= targetAge1:
        count1 += 1   #or count1 = count1 + 1
print('total count is: ', count1)
print('--------------------------------------------')
print('\n')




#while loop
# a while loop is used to iteratively execute a block of statements until a specified condition is met.

#Pb. given a list of voter's age, count the total number of ages greater than or equal to the targetAge
targetAge2 = 20
ageList2 = [10, 21, 20, 18, 20, 16, 22]
count2 = 0
index = 0
while index < len(ageList2):
    if ageList2[index] >= targetAge2:
        count2 += 1
    index = index + 1
print('total count is:', count2)
print('--------------------------------------------')
print('\n')