# استعاء المكتبة الاساسية لصنع اللعبة
import turtle
# عمل الشاشه الرئيسية للعبة
wind = turtle.Screen()
wind.bgcolor("black")
wind.title("BING BONG GAME EIDAT ZAIN")
wind.setup(width=800, height=600)
wind.tracer(0)

#عمل مضرب 1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("red")
madrab1.penup()
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.goto(-350, 0)

#عمل مضرب 2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("blue")
madrab2.penup()
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.goto(350, 0)

#عمال الكورة
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("White")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2
# عمل النتائج
score1 = 0
score2 = 0
score = turtle.Turtle()
score.hideturtle()
score.goto(0, 270)
score.color("white")
score.penup()
score.write("player 1: 0 player 2: 0", align="center", font=("Courier", 16, "normal"))

#دوال تحركي المضارب والكورة
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)
def madrab1_down():
    y = madrab1.ycor()
    y += -20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)
def madrab2_down():
    y = madrab2.ycor()
    y += -20
    madrab2.sety(y)
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")
# الداله التكرارية للعبة الاساسية
while True:
    wind.update()

    #حرك الكرة
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy )
    #الاستضام للاعلى والاسفل
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #الاستضام لليمين واليسار
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))
    #الاستضام مع مضرب 1
    if (340 < ball.xcor() < 360) and (madrab2.ycor() - 60 < ball.ycor() < madrab2.ycor() + 60):
        ball.setx(340)
        ball.dx *= -1
    if (-360 < ball.xcor() < -340) and (madrab1.ycor() - 60 < ball.ycor() < madrab1.ycor() + 60):
        ball.setx(-340)
        ball.dx *= -1



