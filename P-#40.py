#Get number of rows and columns from user and return the matrix(2D Array) of it

c = int(input("Enter no. of colmns here : ")) 
r = int(input("Enter no. of rows here : ")) 
ls = [] 

for i in range(r):
    recs = []
    for j in range(c):
        inp_ls = int(input(f"Enter the values for the row no. {i+1} : "))
        recs.append(inp_ls)
    ls.append(recs)

print("\nHere's the Matrix - ")
for k in range(len(ls)):
    for l in range(len(ls[k])):
        print(ls[k][l], end=" ")
    print()