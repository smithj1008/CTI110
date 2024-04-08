    #Jaylen Smith
    #4/7/2024
    #P4LAB1
    #Write a turtle graphics programs that draws a triangle and a square using loops.
import turtle


t = turtle.Turtle()


side_length = 100
angle = 90
count = 0
while count < 4:
    t.forward(side_length)
    t.right(angle)
    count += 1


t.penup()
t.goto(150, 0)
t.pendown()


side_length = 100
angle = 120
count = 0
while count < 3:
    t.forward(side_length)
    t.left(angle)
    count += 1


t.hideturtle()


turtle.done()



