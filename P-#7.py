# Create a function that subtracts 1 from n (unless it ends in 0) k number of times. If n ends in 0, remove the 0.


def fund(n, k):
    for i in range(k):
        n = n - 1
        if str(n)[-1] == "0":
            k = ""
            print(f"You reached the number ending with 0 and the answer is {str(n).replace(str(n)[-1], k)}")
            break
        else:
            print(n)

fund(42023110, 10) 