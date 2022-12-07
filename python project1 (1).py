a = " "
while len(a) != 5 :
    a = input("Enter the time in the format hh:mm: ")
    if len(a) != 5:
        print("Enter the time in the correct format")

# converting the input into hours and minutes

a = a.split(":")
hours = int(a[0])
minutes = int(a[1])

# calculating the angle between the hour and minute hand

angle = abs((hours*30 + minutes*0.5) - (minutes*6))
if angle>180:
    angle-=180
# printing the angle

print("The angle between the hour and minute hand is: ", angle)
