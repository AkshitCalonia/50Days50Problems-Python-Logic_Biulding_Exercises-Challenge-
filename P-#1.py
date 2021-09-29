# Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.
# The function should return 0 if a non-integer is passed in.

k = int(input("Enter a num here : "))

def add_it_up(k):
    s = 0
    for num in range(0, k+1):
        s = s + num
    
    print(f"The sum of numbers from 0 to {k} is {s}")

add_it_up(k)

