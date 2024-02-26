#Program that prints user's name in reverse order
str = input("Enter a string: ")
str1 = ""
for i in str:
    str1=i+str1
print("Reverse: ",str1)

str2 = input("Enter: ")
print(str2[::-1])
