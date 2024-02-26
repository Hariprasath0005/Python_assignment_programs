#Program to convert the distance (in feet) to inches, yards, and miles. 1 feet = 12 inches, 3 feet = 1 yard, 5280 feet = 1 mile
Distance = float(input("Enter the Distance in feet: "))
inch = Distance*12
yard = Distance/3
mile = Distance/5280
print("Inch:", inch)
print("Yard: ", yard)
print("Mile", mile)