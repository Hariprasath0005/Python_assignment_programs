#Program to find the number of notes (Sample of notes: 10, 20, 50, 100, 500, and 1000 ) against an given amount
amt=int(input("Enter the amount: "))
notes = [1000,500,100,50,20,10]
for i in notes:
    count = amt//i
    amt = amt%i
    print(i,"-->",count)
    
