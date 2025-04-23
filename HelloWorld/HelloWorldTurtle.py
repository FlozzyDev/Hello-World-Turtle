import turtle

# Create the window to visualize
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Says Hello World")
screen.setup(width=800, height=500)

# create the pen for drawing, hide the visual so we just see output from "pen"
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

# We need a mascot! This is the actual "turtle"
animated_turtle = turtle.Turtle()
animated_turtle.shape("turtle")
animated_turtle.color("green")
animated_turtle.penup()
animated_turtle.speed(5)

# turtle greeting
pen.goto(0, 150)
pen.color("Green")
pen.write("Hello!", align="center", font=("Arial", 20, "bold"))

fast_turtle = turtle.delay() #We want to turtle to be fast when he's running around!
loops = 3

# Main loop - turtle does a lap and then "Hello World" flashes, and this happens 3 times. 
for i in range(loops):

    turtle.delay(fast_turtle)
    animated_turtle.goto(-350, 200)
    animated_turtle.pendown()
    animated_turtle.pencolor("lime")
    animated_turtle.goto(350, 200)
    animated_turtle.goto(350, -200)
    animated_turtle.goto(-350, -200)
    animated_turtle.goto(-350, 200)
    
    #Flashing "Hello World" in between green/yellow
    colors = [ "yellow", "green", "yellow", "green"]
    for color in colors:
        pen.goto(0, 0)
        pen.color(color)
        pen.clear()
        pen.goto(0, 0)
        pen.color(color)
        pen.write("Hello World!", align="center", font=("Arial", 50, "bold"))
        screen.update()
        turtle.delay(250)

# After the loops, allow user to click on the window and end app
pen.color("Red")
pen.goto(0, -150) 
pen.write("Click to End", align="center", font=("Arial", 25, "bold"))
turtle.exitonclick()