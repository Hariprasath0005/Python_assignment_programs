#Program to calculate the hypotenuse of a right angled triangle
from math import sqrt
a = float(input("Enter the value a: "))
b = float(input("Enter the value b: "))
hypotenuse = sqrt(a**2+b**2)
print("Hypotenuse: ", hypotenuse)