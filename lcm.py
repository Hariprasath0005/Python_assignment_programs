#Program to find LCM (Least Common Multiple)

x = int(input("Enter the value x: "))
y = int(input("enter the value y: "))
if x>y:
    greater = x
else:
    greater = y
while True:
    if ((greater%x==0)and(greater%y==0)):
        lcm = greater
        break
    greater+=1
print("LCM:",lcm)