#Program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure
def number():

    num = input("Enter the number:")
    num1 = num[::-1]
    add = int(num) + int(num1)
    add = str(add)
    rev = add[::-1]
    while True:
        if add != rev:
            print(rev,"Not palindrome")
            number()
            break
        else:
            print(rev,"Palindrom!")
            break
number()
