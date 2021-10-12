#Geometry 3: Perimeter of a Triangle

'''
Write a function that takes the coordinates of three points in the form of a 2d array and returns the perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.

Examples
perimeter([[15, 7], [5, 22], [11, 1]]) ➞ 47.08

perimeter([[0, 0], [0, 1], [1, 0]]) ➞ 3.42

perimeter([[-10, -10], [10, 10 ], [-10, 10]]) ➞ 68.28
Notes
The given points always create a triangle.
The numbers in the argument array can be positive or negative.
Output should have 2 decimal places
This challenge is easier than it looks.
'''

def perifinder(ls):

    a = ls[0]
    b = ls[1]
    c = ls[2]

    ab = round((((b[0]-a[0])**2) + ((b[1]-a[1])**2)) ** (1/2), 2)
    bc = round((((c[0]-b[0])**2) + ((c[1]-b[1])**2)) ** (1/2), 2)
    ca = round((((a[0]-c[0])**2) + ((a[1]-c[1])**2)) ** (1/2), 2)

    return round(ab+bc+ca, 2)

print(perifinder([[-10, -10], [10, 10 ], [-10, 10]]))
        
