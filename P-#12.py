'''Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers.

Vowel	Number
A	4
E	3
I	1
O	0
U	0
'''

def sumofvows(strin):
    vowdict = {
    "A":4,
    "E":3,
    "I":1,
    "O":0, 
    "U":0
    }  
    incl = []
    for i in strin.upper():
        if i in vowdict.keys():
            incl.append(i)

    sum = 0
    for k in incl:
        sum = sum + vowdict[k]
    
    return print(sum)

sumofvows("akshit")

