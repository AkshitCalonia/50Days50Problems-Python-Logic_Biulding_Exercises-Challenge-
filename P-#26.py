# Write a program to take a string from user and return the number of each vowel present in it.
'''
Example - 
vow_c("Hello")  --->   e = 1,  o = 1
'''

inp = input("Enter the string here : ").lower()

vow = ["a", "e", "i", "o", "u"]
c = 0
vowcount = [0, 0, 0, 0, 0]

for i in inp:
    if i in vow:
        c += 1
        for k in range(0, 5):
            if i == vow[k]:
                vowcount[k] += 1

print(f"Total number of vowels are : {c}")
for i in range(5):
    if vowcount[i] != 0:
        print(f"number of vowel -> {vow[i]} is {vowcount[i]}")
