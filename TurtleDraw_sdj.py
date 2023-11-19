# Turtle Draw
# Author:
# Sebastian Jaculbe
# Credits to ChatGPT for calculating the distance, closing the application through a key,
# and closing the input file.

import turtle
import math

# Variables
distance = float()
totalDistance = float(distance)

# Functions
def calculateDistance(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

def exitApplication():
    turtle.bye()
    
print("Turtle Draw - Sebastian Jaculbe Starting")
print("File name:")

# Extract File
fileName = input()

# Turtle Setup
turtle.setup(width=450, height=400)
turtle.speed(10)
turtle.penup()

# The 'q" is the key to exit the application
turtle.onkey(exitApplication, "g")
turtle.listen()

# Read File
turtleDrawTextFile = open(fileName, "r")
readLine = turtleDrawTextFile.readline()

# Drawing
while readLine:
    print(readLine, end="")
    section = readLine.split(" ")
    
    if (len(section) == 3):
        color = section[0]
        x = int(section[1])
        y = int(section[2])
        # Calculates the Distance
        distance = calculateDistance(turtle.xcor(), turtle.ycor(), x, y)
        totalDistance += distance
        # Turtle's Color and Coordinates
        turtle.color(color)
        turtle.goto (x,y)
        turtle.pendown()
    if(len(section) == 1):
        turtle.penup()    
    readLine = turtleDrawTextFile.readline()

# Display the Total Distance Marked
print(totalDistance)
turtle.penup()
turtle.goto(100,-100)
turtle.write(f"Total Distance Marked: {totalDistance}", align="right", font=("Arial", 8))

#End Application
turtle.done()
print("\nEnd")