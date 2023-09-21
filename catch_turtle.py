import random
import time
import turtle

window = turtle.Screen()
window.title("Catch Turtle")

jack = turtle.Turtle()
jack.penup()
jack.shape("turtle")
jack.speed("fastest")
jack.turtlesize(2.5)
colorlist = ["red", "blue", "pink", "purple"]
secondTurtle = turtle.Turtle()
secondTurtle.penup()

score = 0
counter = 30


def mb1(x, y):
    global score
    global counter
    secondTurtle.clear()
    score += 10
    counter -= 1
    jack.color("green")


jack.onclick(fun=mb1, btn=1)


def writerturtle():
    secondTurtle.hideturtle()
    secondTurtle.goto(0, 370)
    secondTurtle.write(f"Score : {score}", move=False, align="center", font=("cooper black", 20, "normal"))


def counterturtle():
    secondTurtle.hideturtle()
    secondTurtle.goto(400, 380)
    secondTurtle.write(f"Counter : {counter}", move=False, align="center", font=("cooper black", 12, "normal"))


for a in range(30):
    writerturtle()
    counterturtle()
    randomnumber = random.randint(-250, 250)
    jack.hideturtle()
    jack.color(random.choice(colorlist))
    time.sleep(0.1)
    jack.hideturtle()
    time.sleep(0.1)
    jack.goto(randomnumber, randomnumber)
    jack.showturtle()
    time.sleep(0.1)

window.clear()


def writerturtle():
    secondTurtle.hideturtle()
    secondTurtle.goto(0, 0)
    secondTurtle.write(f"Score : {score}", move=False, align="center", font=("cooper black", 50, "normal",))


writerturtle()

jack.hideturtle()
window.mainloop()
