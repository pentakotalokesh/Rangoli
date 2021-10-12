import turtle

t=turtle.Turtle()

s=turtle.Screen()
turtle.Screen().bgcolor('black')
t.pensize(4)
t.pencolor('white')
t.penup()
t.goto(0,200)
t.pendown()
style=('Italic',40)
t.write('Happy Diwali!!',font=style,align='center')
t.penup()
t.goto(-0,-100)
t.pendown()
t.speed(0)
t.hideturtle()
t.begin_fill()
t.fillcolor('violet')
def drawcircle(radius):
    for i in range(2):
        #for colours in ["red","magenta"]:
            # t.color(colours)
             t.circle(radius)
             radius=radius-4  
def drawdesign():
    for i in range(10):
        drawcircle(100)
        t.right(36)
drawdesign()

turtle.done()

