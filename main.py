import turtle
import random

def DrawTriangle():
    turtle.penup()
    turtle.goto(-150,-150)
    turtle.pendown()

    peakList = list()
    turtle.color("white")

    print("A: " + str(turtle.pos()))
    peakList.append(turtle.pos())
    turtle.forward(400)

    print("B: " + str(turtle.pos()))
    peakList.append(turtle.pos())
    turtle.left(120)
    turtle.forward(400)

    print("C: " + str(turtle.pos()))
    peakList.append(turtle.pos())
    turtle.left(120)
    turtle.forward(400)

    return peakList

def DrawPoint(x: int, y:int):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.dot(3,"blue")

def GetRandomTrianglePeak(peakList):
    peakNumber = random.randint(0,2)
    return peakList[peakNumber]

def GetMiddlePoint(currentPos:turtle.Vec2D, peakPos:turtle.Vec2D):
    middlePointX = (currentPos[0] + peakPos[0]) / 2
    middlePointY = (currentPos[1] + peakPos[1]) / 2

    middlePoint = list()
    middlePoint.append(middlePointX)
    middlePoint.append(middlePointY)

    return middlePoint

turtle.hideturtle()
turtle.bgcolor("Black")

turtle.speed(-1)

peakList = DrawTriangle()
currentPoint = turtle.Vec2D(0, 0)
for i in range(1000):
    randomPeak = GetRandomTrianglePeak(peakList)
    middlePoint = GetMiddlePoint(currentPoint,randomPeak)
    #print(middlePoint[0])
    #print(middlePoint[1])
    DrawPoint(middlePoint[0], middlePoint[1])
    currentPoint = turtle.Vec2D(middlePoint[0], middlePoint[1])

print("Done")
turtle.mainloop()
