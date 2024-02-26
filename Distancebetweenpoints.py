#Program to compute the distance between the points (x1, y1) and (x2, y2)
from math import sqrt
x1y1 = input("Enter x1 y1: ").split(",")
x2y2 = input("Enter x2 y2: ").split(",")
x = (int(x2y2[0]))**2 - (int(x1y1[0]))**2
y = (int(x2y2[1]))**2 - (int(x1y1[1]))**2
z = sqrt(x+y)
print("The distance between points (x1, y1) and (x2, y2) is ",z)