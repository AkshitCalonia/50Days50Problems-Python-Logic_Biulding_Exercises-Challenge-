'''In mathematics, primorial, denoted by “#”, is a function from natural numbers to natural numbers similar to the factorial function, but rather than successively multiplying positive integers, the function only multiplies prime numbers.

Create a function that takes an integer n and returns its primorial.

Examples
primorial(1) ➞ 2
# First prime number = 2

primorial(2) ➞ 6
# Product of first two prime numbers = 2*3 = 6

primorial(6) ➞ 30030
'''

def primorial(n):
    c = 1
    for i in range(1, n+1):
        if i >1:
            for k in range(2, i):
                if i%k == 0:
                    break
            else:
                c = c*i
    return c

print(primorial(9))
