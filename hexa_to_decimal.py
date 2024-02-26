#Program - hexa-decimal to decimal conversion

hexa = input("Enter the hexa decimal number: ")
hexa = hexa[::-1]
decimal = 0
for i,bit in enumerate(hexa):
    decimal+=int(bit)*16**i
print("Decimal: ", decimal)