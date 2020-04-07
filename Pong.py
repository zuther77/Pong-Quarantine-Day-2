# Simple pong Works Someties 
import turtle

win = turtle.Screen()
win.title("Pong Quarantine day 3")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# left paddle
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.color("white")
paddle_left.penup()
paddle_left.goto(-350, 0)

# right paddle
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.2

# Score Board 
score_left = 0
score_right = 0

score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("Red")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


def right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)


def right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)


def left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)


def left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)





# Key Bindings
win.listen()
win.onkeypress(right_up, "Up")
win.onkeypress(right_down, "Down")
win.onkeypress(left_up, "w")
win.onkeypress(left_down, "s")

# Main Loop
while True:
    win.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 350: 
        score_left += 1
        score.clear()
        score.write("Player A : {}  PLayer B : {}".format(score_left,score_right) , align="center" ,font= ("Courier", 24, "normal" ))
        ball.dx *= -1
      
    elif ball.xcor() < -350:
        score_right += 1
        score.clear()
        score.write("Player A : {}  PLayer B : {}".format(score_left,score_right) , align="center" ,font= ("Courier", 24, "normal" ))
        ball.dx *= -1
        

# Paddle collision
    if ball.xcor() < -340 and ball.ycor() < paddle_right.ycor() + 50 and ball.ycor() > paddle_right.ycor() - 50:
        ball.dx *= -1 
        
    elif ball.xcor() > 340 and ball.ycor() < paddle_left.ycor() + 50 and ball.ycor() > paddle_left.ycor() - 50:
        ball.dx *= -1
       
    

