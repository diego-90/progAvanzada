import turtle
ventana = turtle.Screen()
ventana.bgcolor("red")
ventana.title("mi ventana")

rafael = turtle.Turtle()
rafael.shape("turtle")
rafael.color("blue")
rafael.pensize(2)
rafael.speed(1)

rafael.pendown()
rafael.setpos(0,-100)
rafael.penup()
rafael.setpos(100,-100)
rafael.pendown()
rafael.setpos(0,0)

ventana.mainloop()

