from turtle import*

#building the house
width(4)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#door

forward(80)
left(90)
color("blue")
begin_fill()
forward(80)
right(90)

forward(40)
right(90)

forward(80)
left(90)
end_fill()
#roof
color("red")
penup()
goto(200,200)
pendown()
begin_fill()
left(120)

forward(200)
left(120)

forward(200)
left(30)
end_fill()

#windows
penup()
goto(20,110)
pendown()
color("brown")
begin_fill()
left(90)
forward(45)
left(90)

forward(45)
left(90)

forward(45)
left(90)

forward(45)
left(90)
end_fill()

penup()
goto(135,110)
pendown()
begin_fill()

left(90)
forward(45)
right(90)

forward(45)
right(90)

forward(45)
right(90)

forward(45)
right(90)
end_fill()




penup()
goto(65,155)
pendown()
color("black")
left(90)
forward(45)
left(90)

forward(45)
left(90)

forward(45)
left(90)

forward(45)
left(90)

penup()
goto(180,155)
pendown()

left(90)
forward(45)
right(90)

forward(45)
right(90)

forward(45)
right(90)

forward(45)
right(90)

penup()
goto(180,132)
pendown()
right(90)
forward(45)
left(90)

penup()
goto(157,155)
pendown()
forward(45)

penup()
goto(43,155)
pendown()
forward(45)
right(90)

penup()
goto(65,132)
pendown()
forward(45)


exitonclick()