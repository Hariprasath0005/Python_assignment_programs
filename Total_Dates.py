#Program to calculate number of days between two dates

first = input("Enter the first date: ").split("/")
second =input("Enter the second date:").split("/")
diff = (int(second[2])*365 + int(second[1])*30 + int(second[0])) - (int(first[2])*365 + int(first[1])*30 + int(first[0]))
print("Number of days between",first,"and",second,"is",diff)