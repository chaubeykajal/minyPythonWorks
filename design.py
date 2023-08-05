import turtle
import colorsys
t= turtle.Turtle()
s=turtle.screen()
s.bgcolor("black")
t.speed(0)
h=0
n=80
for i in range (90):
    c=colorsys.hs_to_rgb(h,1,1)
    h+=1/n
    t.color (c)
    t.left(134)
    t.fd(i)
    
    for j in range (3):
        t.left(5)
        t.fd(i*2)
        t.left(22)
