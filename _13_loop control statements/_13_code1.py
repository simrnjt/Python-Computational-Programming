# loop control statements in python are:
#     1. break
#     2. continue
#     3. pass


#break statement
message = 'i got the value 5'
for a in range (1, 11):
    print('current value of a: ', a)
    if a == 5:
        print(message)
        break
print('-----------------------------------------------')
print('\n')    




#continue statement
message = '5 value is missing!'
for a in range (1, 11):
    if a == 5:
        print(message)
        continue
    print('current value of a: ', a)
print('-----------------------------------------------')
print('\n')

#Pb. find the average age of all the eligible voters from the list of applicants
age_list = [15,23,35,23,70,15]

# avg_age = sum_of_all_eligible_voter / no_of_eligible_voters
sum_of_all_eligible_voter = 0
no_of_eligible_voters = 0

for age in age_list:
    if age < 18:
        continue
    sum_of_all_eligible_voter += age
    no_of_eligible_voters += 1

avgAge = 0

if no_of_eligible_voters > 0:
    avgAge = sum_of_all_eligible_voter / no_of_eligible_voters

print(f'avg age is {avgAge} years')
print('-----------------------------------------------')
print('\n')




#pass statement
# `pass`
#   - A do-nothing placeholder.
#   - Keeps code blocks syntactically valid.
#   - Execution continues normally after `pass`.
#   - Best for: future logic placeholders, empty loops, or when you want to “do nothing” for a condition.

# `continue`
#   - Skips the rest of the current iteration.
#   - Immediately jumps to the next loop iteration.
#   - Best for: skipping invalid or unwanted data during iteration.
  
scores = [85, 90, None, 70, -1, 95]

for score in scores:
    if score is None:
        pass   # placeholder for handling missing data later
    elif score < 0:
        continue   # skip invalid negative scores
    else:
        print("Valid score:", score)
print('-----------------------------------------------')
print('\n')