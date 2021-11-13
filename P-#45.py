# Length Sort
'''
Write a function which takes a list as argument and sort it according to the length of each element in it. It should be acending order.
Use iterative method
'''

def new_sort(ls=["thisu", "as", "f", "mndc"]):
    recs = []
    for i in ls:
        recs.append((len(i), i))
    ans = []
    for i in sorted(recs):
        ans.append(i[1])
    
    return ans

print(new_sort())