import turtle
a=turtle.Turtle()
a= turtle.getscreen().bgcolor("black")
a.penup()
a.goto(-200,100)
a.pendown()
a.clor("yellow")
a.speed(25)
def star(turtle,size):       #   install tkinter  #
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range (5):
            turtle.pensize(2)
            turtle.forward(size)
            star(turtle ,size/3)
            turtle.left(216)
            turtle.end_fill()
star(a,360)
turtle.done()
