Python | Catching the ball game



Python is a multipurpose language and can be used in almost every field of
development. Python can also be used to develop different type of game. Let’s
try to develop a simple _Catching the ball game_ using Python and TKinter.

Game is very simple. There is one bar at the bottom of game window which can
be moved left or right using the buttons that are in the game window. Red ball
will continuously fall from top to bottom and can start from any random x-axis
distance. The task is to bring that bar to a suitable location by moving left
or right so that the red ball will fall on that bar(catch the ball onto the
bar) not on the ground. If player catches the ball onto the bar then score
will get increase and that ball will disappear and again a new red ball will
start falling from top to bottom starting from random x-axis distance. If
player miss the ball from catching it on the bar then you will lose the game
and then finally scorecard will appear on the game window.

 **Approach:**

  1. Use Tkinter package in python for building GUI(Graphical user interface).
  2. Use Canvas for drawing objects in Python – Canvas is a rectangular area intended for drawing pictures or other complex layouts. We can place graphics, text, widgets or frames on Canvas.
    
         **Syntax:** w = Canvas ( master, option=value, ... )
    
    **Parameters:**
    master - This represents the parent window.
    options - List of most commonly used options for this widget. 
    These options can be used as key-value pairs separated by commas. 
    Example- width, height etc. 

  3. Use canvas.create_oval for creating the ball.  
 **create_oval** creates a circle or an ellipse at the given coordinates. It
takes two pairs of coordinates; the top left and bottom right corners of the
bounding rectangle for the oval.

    
         **Syntax:** oval = canvas.create_oval(x0, y0, x1, y1, options)

  4. Use canvas.create_rectangle for creating the bar.  
 **create_rectangle** creates a rectangle at the given coordinates. It takes
two pairs of coordinates; the top left and bottom right coordinates.

  

  

    
    
     **Syntax:** oval = canvas.create_rectangle(x0, y0, x1, y1, options)

* Use canvas.move for moving the ball or bar.  
 **canvas.move** enables the object to move with the specified (x, y)
coordinates.

    
    
     **Syntax:** move=canvas.move(name of object, x, y) 

**Note:** ***** Take x=0 for moving the ball in vertical direction only and
take y=0 for moving the bar in horizontal direction only. ***** Dissapear the
ball when it touches the ground or the bar using canvas.delete(object).

