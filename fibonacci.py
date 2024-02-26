#Program to get the Fibonacci series between 0 to 50

num = int(input("Enter the series:"))
a = 0
b = 1
for i in range(0,num):
    print(a,end=" ")
    c = a+b
    a = b
    b = c