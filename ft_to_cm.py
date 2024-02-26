#Program to convert height (in feet and inches) to centimetres

while True:
    try:
        height = input("Enter the height in feet,inch format: ").split(",")
        cm = float(height[0])*30.48+float(height[1])*2.54
        print(cm)
        break
    except:
        print("Ivalid format, Enter in feet,inch format")