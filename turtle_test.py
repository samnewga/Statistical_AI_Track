import turtle
import math
from tkinter import *

#Function that runs all our turtle functionalities
def AI_Track():

    # Creates the robot that will be navigating through the room
    robot = turtle.Turtle()
    robot.color('blue')
    robot.pensize(1)
    robot.shape('square')

    # Creates the room  with three sides only, leaving one side open
    room = turtle.Turtle()
    room.penup()
    room.setposition(300, 300)
    room.pendown()
    room.pensize(5)
    for side in range(3):
        room.right(90)
        room.forward(600)
    room.hideturtle()

    # Creates the exit objective
    exit = turtle.Turtle()
    exit.penup()
    exit.color("red")
    exit.tilt(90)
    exit.shape("arrow")
    exit.shapesize()
    exit.speed(0)
    exit.setposition(0, 300)

    # Movement algorithm the robot will follow
    def movements():
        robot.penup()
        robot.forward(-300)
        robot.left(90)

    # A while true for the boundaries and for when the exit arrow is touched
    while True:
        movements()

        if robot.xcor() > 100 or robot.xcor() < -100:
            robot.right(180)
        if robot.ycor() < -300:
            robot.right(180)
        d = math.sqrt(math.pow(robot.xcor()-exit.xcor(), 2)) + math.pow(robot.ycor()-exit.ycor(), 2)
        if d < 20:
            exit.hideturtle()

# The text that describes the project
description_text = "Assignment: Statistical AI Track" \
                   "\nBy: Samael Newgate" \
                   "\nDescription: Using the Turtle library an environment that simulates a room with one open door to the north is created. " \
                   "\nBoundaries are then created to prevent a robot from passing through them" \
                   "\nAn arrow is placed at the exit that is removed once the robot passes through it to signal a succesful exit."

# Description window that will output the description text
def description_window():
    toplevel = Toplevel()
    label1 = Label(toplevel, text=description_text, height=10, width=90)
    label1.pack()

# Creates a tkinter window
window = Tk()
window.title("Statistical AI Track")
window.configure(background="black")

# Breaks the tkinter window into a top frame and bottom frame
topFrame = LabelFrame(window, background='black')
topFrame.pack()
bottomFrame = Frame(window, background='black')
bottomFrame.pack(side=BOTTOM)

# Displays the tittle of the project on the bottom frame under the buttons
menu_font = Label(bottomFrame, fg= 'white', text='Statistical AI Track', background='black', font=44)
menu_font.pack()

# Description button set to the top frame, description window is bound to this button
button2 = Button(topFrame, text='Description', background = 'white', padx=9, pady=5, command = description_window)
button2.pack(side=LEFT)

# Run button that executes the AI_Track function
button1 = Button(topFrame, text='Run', padx=9, pady=5, background = 'green', command = AI_Track)
button1.pack(side=LEFT)

# Exit button set to the top frame, window.destroy is bound to this button which destroys all active windows
button5 = Button(topFrame, text='Exit', background='red', padx=9, pady=5,command=window.destroy)
button5.pack(side=LEFT)

# Runs the tkinter window in a loop
window.mainloop()