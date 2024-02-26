#Program to check whether given input is palindrome or not

num = input("Enter the value: ")
str = num[::-1]
if num == str:
    print("palindrome!")
else:
    print("Not a palindrome")