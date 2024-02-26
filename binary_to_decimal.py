#Program - binary to decimal conversion

bin = input("Enter the binary number: ")
bin = bin[::-1]
decimal = 0
for i,bit in enumerate(bin):
    decimal+=int(bit)*2**i
print("Decimal: ", decimal)