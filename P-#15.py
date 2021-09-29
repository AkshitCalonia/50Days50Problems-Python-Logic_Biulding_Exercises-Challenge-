# Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.
# distance formula = √[(x2 − x1)2 + (y2 − y1)2]
import matplotlib.pyplot
import math
import numpy

x1 = int(input("Enter the x1 : "))
y1 = int(input("Enter the y1 : "))
x2 = int(input("Enter the x2 : "))
y2 = int(input("Enter the y2 : "))

def linemeasure(x1, y1 ,x2, y2):
    return round(math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)), 2)

print(linemeasure(x1, y1 ,x2, y2))

xpoints = numpy.array([x1, x2])
ypoints = numpy.array([y1, y2])

matplotlib.pyplot.plot(xpoints, ypoints)
matplotlib.pyplot.show()
