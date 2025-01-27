import random
import turtle

window = turtle.Screen()
window.bgcolor("#000000")
spider = turtle.Turtle()
spider.color("#EEEEEE")
spider.speed(0)
spider.pensize(2)

for threads in range(8):
    spider.forward(180)
    spider.back(180)
    spider.left(45)

def drawArc(radius, startingAngle, angle):
    spider.setheading(startingAngle+90)
    spider.circle(radius,angle)

def drawSpiderWeb(layers):
    for threads in range(8):
        spider.forward(12*3*layers+20)
        spider.back(12*3*layers+20)
        spider.left(45)

    for i in range(1,layers+1):
        spider.backward(12*3)
        for j in range(8):
            drawArc(5*3*i, 90+j*45,-135)

    spider.hideturtle()

layers = random.randint(3,5)
drawSpiderWeb(layers)