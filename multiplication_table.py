#Program to create the multiplication table (from 1 to 10) of a number

num = int(input("Enter a table number: "))
a = int(input("Enter the number of times: "))
for i in range(1,a+1):
    x = num*i
    print(num,"*",i,"=",x)