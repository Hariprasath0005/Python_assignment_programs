#Program to get a new string from a given string where "Is" has been added to the front

str = input("Enter the string: ")
if str.startswith("Is") or str.startswith("is"):
    print(str,"Given string is correct")
else:
    str1 = "Is" + str
    print("Updated string is ",str1)