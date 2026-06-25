#PRINT A COUNTDOWN BEFORE SOMETHING EXCITING HAPPENS


import time
event=input("Please tell about your event: ")
count= int(input("Enter the counter number: "))
print("\nCountdown starts now: ")

for i in range (count, 0, -1):
    print(i)
    time.sleep(1)

print("\nWOHOOOO! HAPPY", event.upper())





