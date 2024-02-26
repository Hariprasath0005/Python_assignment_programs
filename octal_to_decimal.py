#Program - octal to decimal conversion

oct = input("Enter octal :")
oct = oct[::-1]
decimal = 0
for i, bit in enumerate(oct):
    decimal += int(bit) * 8 ** i
print('Decimal :' , decimal)