#Program to get the difference between a given number and 17, difference cannot be negative

num = int(input("Enter the number less than 17: "))
if num > 17:
    print("The number should be less than 17, the difference cannot be negative",17-num)
else:
    n = 17 - num
    print("The difference is :", n)
