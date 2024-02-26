#Program to find GCD (Greatest Common Divisor)

x = int(input("Enter the value x: "))
y = int(input("Enter the value y: "))
if x<y:
    small = x
else:
    small = y
for i in range(1,small+1):
    if ((x%i==0)and (y%i==0)):
        gcd = i
print(gcd)