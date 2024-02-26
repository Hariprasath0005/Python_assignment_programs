#Program to convert all units of time into seconds

while True:
    try:
        time = input("Enter the time in dd/hh/mm/ss format: ").split("/")
        seconds = float(time[0])*86400 + float(time[1])*3600 + float(time[2])*60 + float (time[3])
        print("Total seconds: ", seconds)
        break
    except:
        print("Invalid format")
        