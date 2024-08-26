# initialization
import turtle # allows us to use turtles
wn=turtle.Screen() # opens up a playground
alex=turtle.Turtle() # creates a turtle, assigns to alex
alex.speed(1000) # makes the turtle faster

# inputs
currentHour=int(input("Enter an hour:")) # asks for an hour
while currentHour>12:
    currentHour=int(input("Enter an hour:")) # if the user enters an invalid hour, it will ask the user again.
currentMinute=int(input("Enter an minute:")) # asks for a minute
while currentMinute>59:
    currentMinute=int(input("Enter an minute:")) # if the user enters an invalid minute, it will ask the user again.

# decorative purposes
color=str(input("Type the color you want: "))
alex.color(color)
print("The time is " + str(currentHour) + ": " + str(currentMinute))

# drawing tick marks
alex.penup()
for i in range(12):
    alex.forward(100)
    alex.stamp() # draws a tick mark
    alex.back(100)
    alex.left(30) # turns for the next mark
alex.pendown() # we can start drawing the hands now!
alex.left(90) # aligns the turtle to the 12 o'clock tick mark.

# hour hand
degreesToMoveforHours=30*currentHour
degreesToMoveforExtraMinutes=currentMinute/2 
hourHand=degreesToMoveforHours + degreesToMoveforExtraMinutes
alex.right(hourHand) # moves into position for the hour hand
alex.forward(50) # draws the hour hand
alex.back(50) # resets to the middle
alex.left(hourHand) # returns to 12'o clock

# minute hand
minuteHand=currentMinute*6
alex.right(minuteHand) # moves into position for the minute hand
alex.forward(75) # draws the minute hand

alex.hideturtle()
wn.mainloop()