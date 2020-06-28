# M CHADO-CODEINN practice
import turtle
import time

wn = turtle.Screen()
wn.title("A demo traffic light")
wn.bgcolor("black")



#Draw a box round rhe spotlight
pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

#Make red light
red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.goto(0, 40)

#Make yellow light
yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.goto(0, 0)

#Make green light
green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.goto(0, -40)
    


while True:
    yellow_light.color("white")
    red_light.color("red")
    time.sleep(5)

    red_light.color("white")
    green_light.color("green")
    time.sleep(3)

    green_light.color("white")
    yellow_light.color("yellow")
    time.sleep(1)







wn.mainloop()
