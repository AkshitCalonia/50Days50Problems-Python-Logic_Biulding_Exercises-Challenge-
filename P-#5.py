# write a function to print factorial of a number

def fact(n):
    k = 1
    for i in range(1, n+1):
        k *= i 
    print(k)

fact(5)

