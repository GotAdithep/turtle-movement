import turtle

def move_forward():
    turtle.setheading(90)
    turtle.forward(100)

def move_right():
    turtle.setheading(0)
    turtle.forward(100)

def move_down():
    turtle.setheading(270)
    turtle.forward(100)

def move_left():
    turtle.setheading(180)
    turtle.forward(100)

turtle.onkey(move_forward, "Up")
turtle.onkey(move_right, "Right")
turtle.onkey(move_down, "Down")
turtle.onkey(move_left, "Left")

turtle.listen()
turtle.done()
