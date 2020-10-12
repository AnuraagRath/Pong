#Pong by Anuraag Rath

import turtle
import os

windowCanvas = turtle.Screen()
windowCanvas.title("Pong")
windowCanvas.bgcolor("black")
windowCanvas.setup(width=800, height=600)
windowCanvas.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
rectUno = turtle.Turtle()
rectUno.speed(0)
rectUno.shape("square")
rectUno.color("white")
rectUno.shapesize(stretch_wid=5,stretch_len=1)
rectUno.drawCanvasup()
rectUno.goto(-350, 0)

# Paddle B
rectDos = turtle.Turtle()
rectDos.speed(0)
rectDos.shape("square")
rectDos.color("white")
rectDos.shapesize(stretch_wid=5,stretch_len=1)
rectDos.drawCanvasup()
rectDos.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.drawCanvasup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# drawCanvas
drawCanvas = turtle.Turtle()
drawCanvas.speed(0)
drawCanvas.shape("square")
drawCanvas.color("white")
drawCanvas.drawCanvasup()
drawCanvas.hideturtle()
drawCanvas.goto(0, 260)
drawCanvas.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def rectUno_up():
    y = rectUno.ycor()
    y += 20
    rectUno.sety(y)

def rectUno_dowindowCanvas():
    y = rectUno.ycor()
    y -= 20
    rectUno.sety(y)

def rectDos_up():
    y = rectDos.ycor()
    y += 20
    rectDos.sety(y)

def rectDos_dowindowCanvas():
    y = rectDos.ycor()
    y -= 20
    rectDos.sety(y)

# Keyboard bindings
windowCanvas.listen()
windowCanvas.onkeypress(rectUno_up, "w")
windowCanvas.onkeypress(rectUno_dowindowCanvas, "s")
windowCanvas.onkeypress(rectDos_up, "Up")
windowCanvas.onkeypress(rectDos_dowindowCanvas, "DowindowCanvas")

# Main game loop
while True:
    windowCanvas.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        drawCanvas.clear()
        drawCanvas.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        drawCanvas.clear()
        drawCanvas.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < rectUno.ycor() + 50 and ball.ycor() > rectUno.ycor() - 50:
        ball.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < rectDos.ycor() + 50 and ball.ycor() > rectDos.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    