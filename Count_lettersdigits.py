#Program that accepts a string and calculate the number of digits and letters

str = input("Enter a string: ")
d= 0
l= 0
for i in str:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1
print("letters",l," Digits",d)