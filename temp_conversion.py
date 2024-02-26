#Program to convert temperatures to and from Celsius, Fahrenheit

print("Enter 1 to convert celsius to fahrenheit")
print("Enter 2 to convert fahrenheit to celsius")
n = int(input("Enter: "))
if n == 1:
    c = float(input("Enter the celsius: "))
    f = c*9/5+32
    print("Fahrenheit :",f)
elif n == 2:
    f = float(input("Enter the Fahrenheit: "))
    c = (f-32)*5/9
    print("Celsius",c)
else:
    print("Invalid entry, Enter a valid entry")