# Import Modules
import random
import turtle
import time

# Name non racing turtles
lines = turtle.Turtle()
winnerLabel = turtle.Turtle()
numberStart = turtle.Turtle()

# Set winner variable to no
winner = "no"

# Creates a playground for turtles
wn = turtle.Screen()

# Adds title and color to playground window
wn.title("The Great Turtle Races")
wn.bgcolor("Light Green")

# Hide turtles not involved in the race
lines.hideturtle()
winnerLabel.hideturtle()
numberStart.hideturtle()

# Create race lines including start and finish
lines.penup()
lines.goto (-400,300)
lines.speed (100)
for step in range(9):
    if step ==0:
        lines.write("Start",align = "center",font = ("Arial", 20, "normal"))
    elif step ==8:
        lines.write("Finish",align = "center",font = ("Arial", 20, "normal"))
    else:
        lines.write(step,align = "center")
    lines.right(90)
    lines.forward (10)
    lines.pendown()
    lines.forward (600)
    lines.penup ()
    lines.backward(610)
    lines.left(90)
    lines.forward(100)

# Create turtles for the race

red = turtle.Turtle ()
blue = turtle.Turtle ()
yellow = turtle.Turtle ()
green = turtle.Turtle ()
red.color("red")
red.shape("turtle")
red.turtlesize (2)
blue.color("blue")
blue.shape("turtle")
blue.turtlesize (2)
yellow.color("yellow")
yellow.shape("turtle")
yellow.turtlesize (2)
green.color("dark green")
green.shape("turtle")
green.turtlesize (2)

#Place turtles at starting line and twirl once
red.penup()
red.goto(-435,150)
red.pendown()
red.right(360)
blue.penup()
blue.goto(-435,50)
blue.pendown()
blue.left(360)
yellow.penup()
yellow.goto(-435,-50)
yellow.pendown()
yellow.right(360)
green.penup()
green.goto(-435,-150)
green.pendown()
green.left(360)

# Count down from 3 to start race
numberStart.pencolor("black")
numberStart.write("3", align= "center", font = ("Arial", 100, "normal"))
time.sleep (1)
numberStart.clear()
numberStart.write("2", align= "center", font = ("Arial", 100, "normal"))
time.sleep (1)
numberStart.clear()
numberStart.write("1", align= "center", font = ("Arial", 100, "normal"))
time.sleep (1)
numberStart.clear()
numberStart.write("GO!", align= "center", font = ("Arial", 100, "normal"))
time.sleep (1)
numberStart.clear()

# The turtle race!
for turn in range (200):
    red.penup()
    blue.penup()
    yellow.penup()
    green.penup()
    if winner == "no":
        red.forward(random.randrange(1, 9))
        blue.forward(random.randrange(1, 9))
        yellow.forward(random.randrange(1, 9))
        green.forward(random.randrange(1, 9))
    # Check for winner
    if red.xcor() > 370:
        winner = "red"
    elif blue.xcor() > 370:
        winner = "blue"
    elif yellow.xcor() > 370:
        winner = "yellow"
    elif green.xcor() > 370:
        winner = "green"
    else:
        winner = "no"

# Display winner label
def displayWinnerLabel():
    winnerLabel.right(90)
    winnerLabel.penup()
    winnerLabel.forward(300)
    winnerLabel.pendown()
    winnerLabel.pencolor("black")
    winnerLabel.write("WINNER!", align="center", font=("Arial", 100, "normal"))

# Anncounce winner
lines.clear()
if winner == "red":
    blue.hideturtle()
    green.hideturtle()
    yellow.hideturtle()
    red.penup()
    red.goto (0,0)
    red.down()
    red.turtlesize(15)
    red.left(450)
    displayWinnerLabel()
elif winner == "blue":
    red.hideturtle()
    green.hideturtle()
    yellow.hideturtle()
    blue.penup()
    blue.goto (0,0)
    blue.down()
    blue.turtlesize(15)
    blue.left(450)
    displayWinnerLabel()
elif winner == "yellow":
    blue.hideturtle()
    green.hideturtle()
    red.hideturtle()
    yellow.penup()
    yellow.goto(0, 0)
    yellow.down()
    yellow.turtlesize(15)
    yellow.left(450)
    displayWinnerLabel()
elif winner == "green":
    blue.hideturtle()
    red.hideturtle()
    yellow.hideturtle()
    green.penup()
    green.goto(0, 0)
    red.down()
    green.turtlesize(15)
    green.left(450)
    displayWinnerLabel()

# Keep window open
turtle.mainloop()