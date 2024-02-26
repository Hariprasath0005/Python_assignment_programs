#Program to sum of first n positive integers

n = int(input("enter the number: "))
a = 0
for i in range(1,n+1):
    a += i
print("Sum of positive integer: ",a)