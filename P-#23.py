#Create a function that produces a random number that contains all numbers from one to five, without any duplicates.

import random
ls = []
c=0
while True:
    randno = random.randint(1, 5)
    if randno not in ls:
        ls.append(randno)
        c+=1
    elif c == 5:
        break
    
for nums in ls:
    print(nums, end="")