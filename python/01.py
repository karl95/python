#https://www.metshein.com/course/python-turtle-graphics/?action=curriculum // ülesanne 1 // ITS24 Karl-Gustav Kessel
# impordib kilpkonna mooduli

import turtle

#kolmnurk
turtle.speed(5)
turtle.penup()
turtle.goto(-500,200)
turtle.pendown()
turtle.forward(200) #fd
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
#lõpetab kilpkonna, et ei jookse kokku

#süda
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
turtle.left(120)
turtle.forward(100)
turtle.circle(50,180)
turtle.right(90)
turtle.circle(50,180)
turtle.forward(100)

turtle.done()
