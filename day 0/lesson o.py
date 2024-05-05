from turtle import *

#we want to paint a house 

#step 1: draw a square
shape("turtle")
speed(2)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()


#end of squeare

#drawing a door


forward(70)
color("brown")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)

forward(100)
end_fill()
#draw roof

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#draw a window

color("purple")
left(30)
forward(70)
color("pink")
left(90)
forward(60)
left(90)
forward(70)
left(90)
forward(60)
left(90)
forward(70)
left(90)
forward(30)
left(90)
forward(70)
left(90)
forward(30)
left(90)
forward(35)
left(90)
forward(60)

#second one

penup()
goto(140, 200)
pendown()
forward(60)
right(90)
forward(70)
right(90)
forward(60)
right(90)
forward(70)
right(90)
forward(30)
right(90)
forward(70)
right(90)
forward(30)
right(90)
forward(35)
right(90)
forward(60)




exitonclick()