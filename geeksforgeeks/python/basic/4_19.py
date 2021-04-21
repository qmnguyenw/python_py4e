Draw Clock Design using Turtle in Python



Turtle is an inbuilt module in Python. It provides drawing using a screen
(cardboard) and turtle (pen). To draw something on the screen, we need to move
the turtle (pen). To move turtle, there are some functions i.e forward(),
backward(), etc.

#### To draw Clock Design :

> Following steps are used :
>
>   * Import turtle.
>   * Create Screen object and set Screen configuration.
>   * Create Turtle object and set its position and speed.
>   * Draw a dashed line and print number in circular shape.
>   * Draw center and fill color black in it
>   * Write “GFG” and “CLOCK” at required postion.
>

Below is the implementation:

Python3

    
    
    # import package
    import turtle
    
    # create a Screen Object
    screen = turtle.Screen()
    
    # Screen configuration
    screen.setup(500, 500)
    
    # Make turtle Object
    clk = turtle.Turtle()
    
    # set a Turtle object color
    clk.color('Green')
    
    # set a Turtle object width
    clk.width(4)
    
    
    def draw_hour_hand():
        clk.penup()
        clk.home()
        clk.right(90)
        clk.pendown()
        clk.forward(100)
    
    
    # value for numbers in clock
    val = 0
    
    # loop for print clock numbers
    for i in range(12):
        # increment value by 1
        val += 1
    
        # move turtle in air
        clk.penup()
    
        # for circular motion
        clk.setheading(-30 * (i + 3) + 75)
    
        # move forward for space
        clk.forward(22)
    
        # move turtle to surface
        clk.pendown()
    
        # move forward for dash line
        clk.forward(15)
    
        # move turtle in air
        clk.penup()
    
        # move forward for space
        clk.forward(20)
    
        # write clock integer
        clk.write(str(val), align="center",
                  font=("Arial",
                        12, "normal"))
    
    # colored centre by setting position
    # sets position of turtle at given position
    clk.setpos(2, -112)
    clk.pendown()
    clk.width(2)
    
    # To fill color green
    clk.fillcolor('Green')
    
    # start filling
    clk.begin_fill()
    
    # make a circle of radius 5
    clk.circle(5)
    
    # end filling
    clk.end_fill()
    
    clk.penup()
    draw_hour_hand()
    clk.setpos(-20, -64)
    clk.pendown()
    clk.penup()
    
    # Write Clock by setting position
    clk.setpos(-30, -170)
    clk.pendown()
    clk.write(' GfG Clock', font=("Arial", 14,
                                  "normal"))
    clk.hideturtle()
    turtle.done()
    

