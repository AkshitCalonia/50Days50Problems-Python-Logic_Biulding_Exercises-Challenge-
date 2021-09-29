# Create a function that takes two lists of numbers sorted in ascending order and returns a list of numbers which are common to both the input lists.

def fce(ls1, ls2):
    fnl = []
    if len(ls1)>len(ls2):
        for i in ls2:
            if i in ls1:
                fnl.append(i)
    else:
        for i in ls1:
            if i in ls2:
                fnl.append(i)
    
    return fnl

fce([1, 2, 3, 4, 6, 5, 9, 8, 7],[5, 6, 7, 8, 9])