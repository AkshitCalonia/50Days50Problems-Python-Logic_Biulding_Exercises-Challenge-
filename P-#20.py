'''Create a function that counts the number of digits in a number. Conversion of the number to a string is not allowed, thus, the approach is either recursive or iterative.

Examples
digits_count(4666) ➞ 4
digits_count(544) ➞ 3
digits_count(121317) ➞ 6
digits_count(0) ➞ 1
digits_count(12345) ➞ 5
digits_count(1289396387328) ➞ 13

Notes
All inputs are integers but some are in exponential form, deal with it accordingly.
A recursive version of this challenge can be found via this link.
'''

def digits_count(num):
    J = 0
    while num>=1:
        num = num/10
        J = J+1
    return J

print(digits_count(5768))