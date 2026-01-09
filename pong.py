from turtle import Turtle, Screen




screen = Screen()

screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title('Pong')





score = Turtle()

left_score = 0
right_score = 0
score.color('white')
score.hideturtle()

score.teleport(-100,200)
score.write(left_score,align='center',font=('Courier',80,'normal'))


score.teleport(100,200)
score.write(right_score,align='center',font=('Courier',80,'normal'))



left_tim = Turtle()
left_tim.shape('square')
left_tim.color('white')
left_tim.speed('fastest')
left_tim.setheading(90)
left_tim.shapesize(stretch_wid=1, stretch_len=5)
left_tim.teleport(x=-350, y=0)

right_tim = Turtle()
right_tim.shape('square')
right_tim.color('white')
right_tim.speed('fastest')
right_tim.shapesize(stretch_wid=1, stretch_len=5)
right_tim.teleport(x=350, y=0)
right_tim.setheading(90)

def up():
    left_tim.penup()
    if left_tim.ycor() > 230:
        return
    left_tim.forward(20)

def down():
    left_tim.penup()
    if left_tim.ycor() < -230:
        return
    left_tim.backward(20)

def other_up():
    right_tim.penup()
    if right_tim.ycor() > 230:
        return

    right_tim.forward(20)

def other_down():
    right_tim.penup()
    if right_tim.ycor() < -230:
        return

    right_tim.backward(20)



ball = Turtle()
ball.shape('turtle')
ball.color('turquoise')
ball.speed('slowest')
ball.penup()
ball.setheading(30)
keep_moving = True



screen.listen()

#for left side
screen.onkeypress(fun = up, key= 'w')
screen.onkeypress(fun = down, key= 's')

#for right side
screen.onkeypress(fun = other_up, key= 'Up')
screen.onkeypress(fun = other_down, key= 'Down')




def move():
    right_score = 0
    left_score = 0
    while keep_moving:

        ball.forward(10)
        if ball.xcor() > 330 and abs(ball.ycor() - right_tim.ycor()) < 50:
            ball.speed('fastest')
            ball.setheading(180 - ball.heading())
            ball.speed('slowest')
        if ball.xcor() < -330 and abs(ball.ycor() - left_tim.ycor()) < 50:
            ball.speed('fastest')
            ball.setheading(180 - ball.heading())
            ball.speed('slowest')

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.speed('fastest')
            ball.setheading(-ball.heading())
            ball.speed('slowest')

        if ball.xcor() > 390:
            print('Round over for Player 2')
            score.clear()
            left_tim.teleport(x=-350, y=0)
            right_tim.teleport(x=350, y=0)
            left_score += 1
            score.teleport(-100, 200)
            score.write(left_score, align='center', font=('Courier', 80, 'normal'))
            score.teleport(100, 200)
            score.write(right_score, align='center', font=('Courier', 80, 'normal'))
            ball.speed('fastest')
            ball.teleport(0,0)
            ball.setheading(210)
            ball.speed('slowest')

        if ball.xcor() < -380:
            print('Round over for Player 1')
            score.clear()
            left_tim.teleport(x=-350, y=0)
            right_tim.teleport(x=350, y=0)
            right_score += 1
            score.teleport(100, 200)
            score.write(right_score, align='center', font=('Courier', 80, 'normal'))
            score.teleport(-100, 200)
            score.write(left_score, align='center', font=('Courier', 80, 'normal'))
            ball.speed('fastest')
            ball.teleport(0, 0)
            ball.setheading(30)
            ball.speed('slowest')
move()





screen.exitonclick()
