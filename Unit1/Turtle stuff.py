# import turtle as t
# t.speed(0)
# t.screensize(4000,4000)
# def fillc(nice, c):
#     t.fillcolor(c)
#     t.begin_fill()
#     t.circle(nice)
#     t.end_fill()
# #Ears
# ud(-70, 150)
# t.seth(345)
# fillc(40, "grey")
# ud(-67.5, 160)
# fillc(25, "black")
# ud(70, 150)
# t.seth(15)
# fillc(40, "grey")
# ud(67.5, 160)
# fillc(25, "black")
# #Face
# t.seth(0)
# ud(0, 0)
# fillc(100, "grey")
# #Eyes
# ud(-50, 90)
# fillc(20, "black")
# ud(-55, 110)
# fillc(8, "white")
# ud(50, 90)
# fillc(20, "black")
# ud(45, 110)
# fillc(8, "white")
# #Nose
# ud(0, 55)
# fillc(30, "black")
# #Cheeks
# ud(-70, 55)
# fillc(15, "pink")
# ud(70, 55)
# fillc(15, "pink")
#
# t.ht()
# t.Screen().exitonclick()

#Working Fibbonacci sequence
# def fibs(x):
#     a = 0
#     b = 1
#     for i in range(x):
#         print(a)
#         c = a + b
#         a = b
#         b = c
# fibs(14)

# def circleF(nice):
#     t.begin_fill()
#     t.circle(nice)
#     t.end_fill()
# def penM(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
# def fs():
#     a = 0
#     b = 1
#     hx = 0
#     for i in range(14):
#         circleF(a)
#         # penM(hx + a + b, 0)
#         # t.write(a, font=('Courier', a))
#         penM(hx + a + b, -a)
#         c = a + b
#         a = b
#         b = c
#         hx += c
# fs()
# t.ht()
# t.Screen().exitonclick()

n1 = 150
n2 = 345
# t.screensize = (n1, n2)
n3 = 1
while n3 != 10:
    n1 = n2 % n3
    n3 = n2
    n2 = n1

# t.ht()
# t.Screen().exitonclick()
