'''Last Digit Ultimate

Your job is to create a function, that takes 3 numbers: a, b, c and returns True if the last digit of a * b = the last digit of c. Check the examples below for an explanation.
'''


def ldu(a, b, c):
    k = a * b
    k1 = str(k)
    k2 = len(k1) - 1
    k3 = k1[k2]

    c1 = str(c)
    c2 = len(c1) - 1
    c3 = c1[c2]

    return k3 == c3


ldu(12, 215, 2142)
