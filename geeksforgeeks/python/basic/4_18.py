Draw moving object using Turtle in Python



 **Turtle** is an inbuilt module in python. It provides drawing using a screen
(cardboard) and turtle (pen). To draw something on the screen, we need to move
the turtle. To move turtle, there are some functions i.e forward(),
backward(), etc.

#### 1.)Move the Object (ball) :

> Following steps are used:
>
>   * Import Turtle package.
>   * Set screen with dimensions and color.
>   * Form turtle object with color.
>   * Form the object (ball – made of colored circle).
>   * Call the function for making object again and again and clear the
> screen.
>

Below is the implementation :

Python3

    
    
    # import turtle package
    import turtle
    
    
    # function for movement of an object 
    def moving_object(move):
        
        # to fill the color in ball
        move.fillcolor('orange') 
        
        # start color filling
        move.begin_fill() 
        
        # draw circle
        move.circle(20)  
        
        # end color filling
        move.end_fill()             
    
    # Driver Code
    if __name__ == "__main__" :
        
        # create a screen object
        screen = turtle.Screen() 
    
        # set screen size
        screen.setup(600,600)    
    
        # screen background color
        screen.bgcolor('green')   
    
        # screen updaion 
        screen.tracer(0)           
    
        # create a turtle object object
        move = turtle.Turtle() 
    
        # set a turtle object color
        move.color('orange')
    
        # set turtle object speed
        move.speed(0) 
    
        # set turtle object width
        move.width(2)     
    
        # hide turtle object
        move.hideturtle()          
    
        # turtle object in air
        move.penup()               
    
        # set initial position
        move.goto(-250, 0) 
    
        # move turtle object to surface
        move.pendown()             
    
        # infinite loop
        while True :
            
            # clear turtle work
            move.clear()  
            
            # call function to draw ball
            moving_object(move)   
            
            # update screen
            screen.update()    
            
            # forward motion by turtle object
            move.forward(0.5)      
    

