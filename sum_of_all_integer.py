#Program to calculate sum of the digits in an integer

n = input("enter the number: ")
a = 0
for i in n:
    a += int(i)
print("Sum of positive integer: ",a)