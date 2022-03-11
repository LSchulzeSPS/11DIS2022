import turtle as t
#Get inputs before starting turtle gui
length = int(input("Please input the length of your tile perimeter: ")) #345 test
width = int(input("Please input the width of your tile perimeter: ")) #150 test
t.speed(0)
def penM(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
def rectangleCreate(length, width, c):
    for i in range(4):
        t.fillcolor(c)
        t.begin_fill()
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.end_fill()
def euclidalgorithm(length, width):
    holdValue = 1
    while holdValue != 0:
        holdValue = length % width
        length = width
        width = holdValue
    return length
size = euclidalgorithm(length, width)
startX = 0
startY = width-size
acrossSquare = int(length/size)
downSquare = int(width/size)
rectangleCreate(length, width, "white")
for a in range(downSquare):
    for b in range(acrossSquare):
        penM(startX + size * b, startY)
        rectangleCreate(size, size, "green")
    startY -= size
t.ht()
t.Screen().exitonclick()
