Python Tkinter | Moving objects using Canvas.move() method



 **Canvas class** of Tkinter supports a functions which is used to move
objects from one position to another in any canvas or tkinter toplevel.

>  **Syntax:** Canvas.move(canvas_object, x, y)
>
>  **Parameters:**  
>  **canvas_object** is any valid image or drawing created with the help of
> Canvas class. To know how to create object using Canvas class take reference
> of this.  
>  **x** is horizontal distance from upper-left corner.  
>  **y** is vertical distance from upper-left corner.

We will use class to see the working of move() method.

 **Class parameters-**

  

  

>  **Data members used:**  
>  master  
> x  
> y  
> canvas  
> rectangle
>
>  **Member functions used:**  
>  movement()  
> left()  
> right()  
> up()  
> down()
>
>  **Widgets used:** Canvas
>
>  **Tkinter method used:**  
>  Canvas.create_rectangle()  
> pack()  
> Canvas.move()  
> after()  
> bind()

Below is the Python implementation:

 __

 __  
 __

 __

 __  
 __  
 __

# imports every file form tkinter and tkinter.ttk

from tkinter import *

from tkinter.ttk import *

 

class GFG:

 def __init__(self, master = None):

 self.master = master

 

 # to take care movement in x direction

 self.x = 1

 # to take care movement in y direction

 self.y = 0

 

 # canvas object to create shape

 self.canvas = Canvas(master)

 # creating rectangle

 self.rectangle = self.canvas.create_rectangle(

 5, 5, 25, 25, fill = "black")

 self.canvas.pack()

 

 # calling class's movement method to 

 # move the rectangle

 self.movement()

 

 def movement(self):

 

 # This is where the move() method is called

 # This moves the rectangle to x, y coordinates

 self.canvas.move(self.rectangle, self.x, self.y)

 

 self.canvas.after(100, self.movement)

 

 # for motion in negative x direction

 def left(self, event):

 print(event.keysym)

 self.x = -5

 self.y = 0

 

 # for motion in positive x direction

 def right(self, event):

 print(event.keysym)

 self.x = 5

 self.y = 0

 

 # for motion in positive y direction

 def up(self, event):

 print(event.keysym)

 self.x = 0

 self.y = -5

 

 # for motion in negative y direction

 def down(self, event):

 print(event.keysym)

 self.x = 0

 self.y = 5

 

if __name__ == "__main__":

 

 # object of class Tk, resposible for creating

 # a tkinter toplevel window

 master = Tk()

 gfg = GFG(master)

 

 # This will bind arrow keys to the tkinter

 # toplevel which will navigate the image or drawing

 master.bind("<KeyPress-Left>", lambda e: gfg.left(e))

 master.bind("<KeyPress-Right>", lambda e: gfg.right(e))

 master.bind("<KeyPress-Up>", lambda e: gfg.up(e))

 master.bind("<KeyPress-Down>", lambda e: gfg.down(e))

 

 # Infnite loop breaks only by interrupt

 mainloop()  
  
---  
  
 __

 __

 **Output:**  

https://media.geeksforgeeks.org/wp-
content/uploads/20190616234019/Canvas.move_.mp4

Extra print statements are used in above code to show the proper working of
**move()** method. **keysym** keyword (Tkinter reserved) is used to print
which keyboard key is pressed.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

