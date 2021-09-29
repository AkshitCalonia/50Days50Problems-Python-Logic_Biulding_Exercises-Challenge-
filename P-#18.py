'''Create a function that accepts a string, checks if it's a valid email address and returns either True or False, depending on the evaluation.

The string must contain an @ character.
The string must contain a . character.
The @ must have at least one character in front of it.
e.g. "e@edabit.com" is valid while "@edabit.com" is invalid.
The . and the @ must be in the appropriate places.
e.g. "hello.email@com" is invalid while "john.smith@email.com" is valid.
If the string passes these tests, it's considered a valid email address.
'''

def checkemail(st):
    j = 0
    ls=[]
    ls[:0]=st
    indfat = ls.index("@")

    if indfat == 0:
        return False
    
    elif ls.__contains__("@") and (ls[indfat-1].isalpha() == True) and ls.__contains__(".") and ls[len(ls)-4] == ".":
        return True

    else:
        return False

run = checkemail("@gmail.com")
print(run)
