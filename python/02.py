#https://www.metshein.com/course/python-turtle-graphics/?action=curriculum // ülesanne 2 // ITS24 Karl-Gustav Kessel

import turtle

aken = turtle.Screen()
aken.setup(width=600,height=400)
aken.title("Olümpiarõngad ja sinu nimi")

turtle.speed(0)

#sinine ring
turtle.penup()
turtle.goto(-150,100)
turtle.pendown()
turtle.color("blue")
turtle.circle(50,360)

#must ring
turtle.penup()
turtle.goto(-90,100)
turtle.pendown()
turtle.color("black")
turtle.circle(50,360)

#punane
turtle.penup()
turtle.goto(-20,100)
turtle.pendown()
turtle.color("blue")
turtle.circle(50,360)

#kollane
turtle.penup()
turtle.goto(-150,50)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50,360)

#roheline
turtle.penup()
turtle.goto(-30,50)
turtle.pendown()
turtle.color("green")
turtle.circle(50,360)


turtle.done()