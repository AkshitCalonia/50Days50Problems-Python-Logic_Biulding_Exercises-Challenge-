#Father and Son Ages
'''Create a function that takes two arguments: a father's current age f_age and his son's current age s_age. Сalculate in how many years he will be twice as old.

Examples
age_difference(36, 7) ➞ 22
# 22 years from now, the father will be 58 years old and his son will be 29 years old.

age_difference(42, 21) ➞ 0
'''

def age_difference(fage, sage):
    c = 0
    while True:
        if fage/sage == 2.0 and fage%sage == 0:
            break
        else:
            fage+=1
            sage+=1
        c+=1
    return c

print(age_difference(36, 7))