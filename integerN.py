#Program that accepts an integer (n) and computes the value of (n+nn+nnn)

n = int(input("Enter the number: "))
n1 = str(n) + str(n)
n2 = str(n)+str(n) + str(n)
comp = n+int(n1)+int(n2)
print(comp)