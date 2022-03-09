import turtle as t
t.speed(0)
length = 345
width = 150
def penM(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
def rectangleCreate(length, width):
    for i in range(4):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
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
rectangleCreate(length, width)
for a in range(downSquare):
    for b in range(acrossSquare):
        penM(startX + size * b, startY)
        rectangleCreate(size, size)
    startY -= size
t.ht()
t.Screen().exitonclick()
