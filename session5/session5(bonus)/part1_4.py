from turtle import *
for i in range (4):
    forward(200)
    left(90)
forward(30)
color ("blue","blue")
begin_fill() 
forward(50)
left(90)
forward(100)
left(90)
forward(50)
left(90)
forward (100)
end_fill()
left(90)
penup()
forward(100)
left(90)
forward(130)
pendown()
color("yellow","yellow")
begin_fill()
right(90)
for a in range (4):
    forward(40)
    left(90)
end_fill()
penup()
forward(70)
left(90)
forward(70)
pendown()
color("black","red")
begin_fill()
left(45)
forward(100*(2**0.5))
left(90)
forward(100*(2**0.5))
end_fill()
mainloop()

