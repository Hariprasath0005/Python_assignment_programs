#Program that count vowels / consonants

str = input("Enter the string: ")
vowel =0
cons = 0
for i in str:
    if i == "a" or i =="e" or i =="i" or i =="o" or i =="u" or i =="A" or i =="E" or i =="I" or i =="O" or i =="U":
        vowel+=1
    else:
        cons+=1
print("Total vowels:",vowel)
print("Total consonants",cons)