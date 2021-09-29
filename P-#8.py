# Write a program that returns a list of all the numbers from 1 to an integer argument. But for multiples of three use “Fizz” instead of the number and for the multiples of five use “Buzz”. For numbers which are multiples of both three and five use “FizzBuzz”.


def FBTest(n):
    nums = []
    for i in range(1, n+1):
        nums.append(i)
        if i%3 == 0 and i%5 == 0:
            nums[i-1] = "FizzBuzz"
        elif i%3 == 0:
            nums[i-1] = "Fizz"
        elif i%5 == 0:
            nums[i-1] = "Buzz"
    return print(nums)

FBTest(15)

