#Program to check whether a number is completely divisible by another number

num1 = int(input("Enter the divisor: "))
num2 = int(input("Enter the divident: "))
if num1 % num2 ==0:
    print("The number is divisible")
else:
    print("The number is not divisible")
    