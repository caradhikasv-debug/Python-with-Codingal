import turtle

turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)
p=turtle.Turtle()

n=10
l=70
angle=360/n
for i in range(n):
    p.forward(l)
    p.right(angle)

turtle.done()
