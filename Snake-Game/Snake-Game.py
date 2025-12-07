#!/usr/bin/python

from turtle import *
import random
import time

# ----------------- CONFIG -----------------
d = 0.1          # delay
s = 0            # score
hs = 0           # high score

# ============   Playable area   ==============

Half_X = 450          # left/right (width 900)
Half_Y = 350          # up/down (height 700)

Off_Y = -100          # move playable area down

Top = Half_Y + Off_Y
Bot = -Half_Y + Off_Y

Coll_X = Half_X - 10
Food_X = Half_X - 30

# =========== SCREEN ============

sc = Screen()
sc.title("Snake Game - PMU")
sc.bgcolor("gray")
sc.setup(width=1200, height=1200)
sc.tracer(0)

# ----------------- BORDER -----------------

border = Turtle()

border.speed(0)
border.color("white")
border.pensize(3)

border.penup()
border.goto(-Half_X, Bot)    # bottom left corner
border.pendown()

for _ in range(2):
    border.forward(Half_X * 2)     # width (900)
    border.left(90)
    border.forward(Half_Y * 2)     # height (700)
    border.left(90)
    
border.hideturtle()

# ----------------- TITLE -----------------
titleT = Turtle()

titleT.speed(0)

titleT.color("white")
titleT.penup()
titleT.hideturtle()

titleT.goto(0, Top + 100)
titleT.write("Snake Game", align="center", 
	font=("Times New Roman", 30, "normal"))

# ----------------- SCORE (TOP CENTER) -----------------
scoreT = Turtle()

scoreT.speed(0)
scoreT.shape("square")
scoreT.color("white")
scoreT.penup()

scoreT.hideturtle()

scoreT.goto(0, Top + 45)
scoreT.write("Score : 0  High Score : 0", align="center",
	 font=("Times New Roman", 24, "bold"))

# ----------------- SNAKE HEAD -----------------

head = Turtle()

head.shape("square")
head.color("white")
head.penup()

head.goto(0, 0)
head.direction = "Stop"

# ----------------- FOOD -----------------

food = Turtle()

food.speed(0)
food.shape(random.choice(["square", "triangle", "circle"]))
food.color(random.choice(["red", "green", "black"]))
food.penup()

food.goto(0, Top - 50)

seg = []   # Snake body segments


# ----------------- CONTROLS -----------------
def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def left():
    if head.direction != "right":
        head.direction = "left"

def right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


def updateScore():
    scoreT.clear()
    scoreT.write(f"Score : {s}  High Score : {hs}",
                 align="center", font=("Times New Roman", 24, "bold"))

def resetGame():
    global s, d, seg

    head.goto(0, 0)
    head.direction = "Stop"

    food.goto(
        random.randint(-Food_X, Food_X),
        random.randint(Bot + 30, Top - 30)
    )

    for segment in seg:
        segment.goto(1000, 1000)
    seg.clear()

    s = 0
    d = 0.1
    updateScore()


# ----------------- KEY BINDINGS -----------------

sc.listen()
sc.onkeypress(up, "Up")
sc.onkeypress(down, "Down")
sc.onkeypress(left, "Left")
sc.onkeypress(right, "Right")

resetGame()  # start immediately

# ----------------- MAIN LOOP -----------------

try:
    while True:
        sc.update()

        # boundary check
        if (head.xcor() > Coll_X or head.xcor() < -Coll_X or
                head.ycor() > Top - 10 or head.ycor() < Bot + 10):
            time.sleep(1)
            resetGame()

        # food collision
        if head.distance(food) < 20:
            food.goto(
                random.randint(-Food_X, Food_X),
                random.randint(Bot + 30, Top - 30)
            )
            # change food look each time
            food.shape(random.choice(["square", "triangle", "circle"]))
            food.color(random.choice(["red", "green", "black"]))

            # add new segment
            NewSeg = Turtle()
            NewSeg.speed(0)
            NewSeg.shape("square")
            NewSeg.color("orange")
            NewSeg.penup()
            seg.append(NewSeg)

            # increase difficulty
            d = max(0.01, d - 0.001)

            # update score
            s += 10
            if s > hs:
                hs = s
            updateScore()

       
        for i in range(len(seg) - 1, 0, -1):
            x = seg[i - 1].xcor()
            y = seg[i - 1].ycor()
            seg[i].goto(x, y)      # move segments

        if len(seg) > 0:
            seg[0].goto(head.xcor(), head.ycor())

        
        move() # move head

        # self-collision
        for segment in seg:
            if segment.distance(head) < 20:
                time.sleep(1)
                resetGame()

        time.sleep(d)

except Terminator:
    pass  # window closed; exit cleanly
