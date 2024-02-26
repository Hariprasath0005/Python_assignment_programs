#Program to compute the future value of a specified principal amount, rate of interest, and a number of years

amount = float(input("Enter the principal amount: "))
interest = float(input("Enter the rate of interest: "))
years = float(input("Enter the years: "))
value = amount *((1+(0.01*interest))**years)
print("The future value is: ",round(value,2))
