import turtle
import random

colors  = ["red","green","blue","orange","purple","pink","yellow","dark green","dark red","lime","dark blue","medium violet red",
           "cyan","saddle brown","dark gray","dark orange","medium purple","magenta"]
darkcolors = ["white","red","green","blue","orange","purple","pink","yellow"]
length = 5
turtle.bgpic("28648.gif",)
def tcircles(circle_turtle,color,dis_range,radius):

    circle_turtle.color(color)
    for i in range(dis_range):
        circle_turtle.circle(radius*i)
	
    circle_turtle.up()
    circle_turtle.goto(0,0)
    circle_turtle.down()
	
def ccircles(circle_turtle,dis_range,radius):
    
    for i in range(dis_range):
        color = random.choice(darkcolors)
        circle_turtle.color(color)
        circle_turtle.circle(radius*i)
        circle_turtle.up()
        circle_turtle.sety((radius*i)*(-1))
        circle_turtle.down()

    circle_turtle.up()
    circle_turtle.goto(0,0)
    circle_turtle.down()


if __name__ == "__main__":

    rcircle = turtle.Turtle()
    rcircle_screen = turtle.Screen()
    rcircle_screen.bgcolor('black')
    
    rcircle.width(1)      
    rcircle.speed(0)      
    
    ccircles(rcircle,30,10)

    rcircle.width(2)      

    for j in range(8):
        for i in range (10):
            tcircles(rcircle,darkcolors[j],10,(10 + j))
            rcircle.right(360/10)

    rcircle.width(3)
    ccircles(rcircle,60,3)

    rcircle.width(2)

   
    for count in range(60):
        rcircle.forward(length)
        rcircle.right(135)
        rcircle.color('black')     
        length = length + 5

    
    rcircle.penup()
    rcircle.home()
    rcircle.pendown()

    turtle.Screen().exitonclick()