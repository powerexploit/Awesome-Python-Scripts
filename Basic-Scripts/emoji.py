import turtle

root=turtle.Turtle()
root.up()
root.goto(0,-100)
root.down

root.begin_fill()
root.fillcolor("yellow")
root.circle(100)
root.end_fill()


root.up()
root.goto(-67,-40)
root.setheading(-60)
root.width(5)
root.down()
root.circle(80,120)
root.fillcolor("black")

for i in range(-35,105,70):
    root.up()
    root.goto(i,35)
    root.setheading(0)
    root.down()
    root.begin_fill()
    root.circle(10)
    root.end_fill()

root.mainloop()
    
