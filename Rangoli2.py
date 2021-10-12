import turtle
import random

colors  = ["red","green","blue","orange","purple","pink","yellow","dark green","dark red","lime","dark blue","medium violet red",
           "cyan","saddle brown","dark gray","dark orange","medium purple","magenta"]
darkcolors = ["white","red","green","blue","orange","purple","pink","yellow"]
length = 5
turtle.bgpic("28648.gif",)
def tcircles(cturtle,color,dis_range,radius):

    cturtle.color(color)
    for i in range(dis_range):
        cturtle.circle(radius*i)
	
    cturtle.up()
    cturtle.goto(0,0)
    cturtle.down()
	
def ccircles(cturtle,dis_range,radius):
    
    for i in range(dis_range):
        color = random.choice(darkcolors)
        cturtle.color(color)
        cturtle.circle(radius*i)
        cturtle.up()
        cturtle.sety((radius*i)*(-1))
        cturtle.down()

    cturtle.up()
    cturtle.goto(0,0)
    cturtle.down()


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