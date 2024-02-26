#Program to count the occurence of a specific character in a string

str = input("Enter the string: ")
a =input("Which character: ")
count = 0
for i in str:
    if a==i:
        count+=1
print(count)