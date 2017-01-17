#speedCam.py
#Shivam Patel
#COMP 150 - Romer

limit = 60

speed = int(input("What speed was the driver driving at? "))

if speed < limit:
            print("No issue")
elif speed <= 65:
            print("Send driver warning")
else:
    print("Send driver ticket")
