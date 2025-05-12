import turtle

# إعداد الشاشة
wind = turtle.Screen()
wind.bgcolor("Black")
wind.title("BING BONG GAME")
wind.setup(width=800, height=600)
wind.tracer(0)  # إيقاف التحديث التلقائي للشاشة (نحن نحدث يدويًا داخل الحلقة)

# إعداد المضرب 1 (اللاعب الأيسر)
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("cyan")
madrab1.penup()
madrab1.shapesize(stretch_wid=6, stretch_len=1.2)
madrab1.goto(-370, 0)

# إعداد المضرب 2 (اللاعب الأيمن)
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.penup()
madrab2.shapesize(stretch_wid=6, stretch_len=1.2)
madrab2.goto(370, 0)

# إعداد الكرة
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.dx = 0.2  # السرعة الأفقية
ball.dy = 0.2  # السرعة الرأسية

# النقاط
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1: 0 player 2: 0", align="center", font=("Courier", 16, "normal"))

# دوال تحريك المضرب 1 (اليسار)
def madrab1_up():
    y = madrab1.ycor()
    if y < 250:  # حد علوي
        madrab1.sety(y + 18)

def madrab1_down():
    y = madrab1.ycor()
    if y > -250:  # حد سفلي
        madrab1.sety(y - 18)

# دوال تحريك المضرب 2 (اليمين)
def madrab2_up():
    y = madrab2.ycor()
    if y < 250:
        madrab2.sety(y + 18)

def madrab2_down():
    y = madrab2.ycor()
    if y > -250:
        madrab2.sety(y - 18)

# ربط المفاتيح
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

# الحلقة الرئيسية للعبة
while True:
    wind.update()

    # تحريك الكرة
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # الاصطدام بالحواف العلوية والسفلية
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # تجاوز الكرة للحدود اليمنى: نقطة للاعب 1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))

    # تجاوز الكرة للحدود اليسرى: نقطة للاعب 2
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))

    # الاصطدام مع madrab2 (اليمين)
    if (340 < ball.xcor() < 360) and (madrab2.ycor() - 60 < ball.ycor() < madrab2.ycor() + 60):
        ball.setx(340)
        ball.dx *= -1
    # الاصطدام مع madrab1 (اليسار)
    if (-360 < ball.xcor() < -340) and (madrab1.ycor() - 60 < ball.ycor() < madrab1.ycor() + 60):
        ball.setx(-340)
        ball.dx *= -1
