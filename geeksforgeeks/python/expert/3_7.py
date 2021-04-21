Establishing an Arcade window in Python



The arcade library is a high-tech Python Package with an advanced set of tools
for making 2D games with gripping graphics and sound. It is Object-oriented
and is specially built for Python 3.6 and above versions.

There are five mandatory functions needed to do arcade programming.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201001140912/Arcade-300x147.JPG)

 **1\. arcade.open_window():** In arcade, everything will be done in the
window itself, with the help of open_window(). At present, arcade only
supports a single display window but, you can resize it according to your
requirement.

This command opens a window with a given size i.e width and height along with
screen title. It takes three arguments and the position of each argument is
fixed. It is a built-in function in arcade. Syntax is as follows:

  

  

>  **Syntax:** arcade.open_window(Screen_width, Screen_Height, “Screen_title”
> , resizeable, antialiasing)
>
>  **Parameters:**
>
>   *  **Screen_width:** – Width of the window.
>   *  **Screen_Height** :- Height of the window.
>   *  **Screen_title:** – Title of the window.
>   *  **resizeable:** – Whether the window can be user resizeable or not.
>   *  **antialiasing** :- It tells whether graphics are smooth or not.
>

 **Implementation of the above syntax:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import arcade

 

arcade.open_window(500, 500, "Welcome to GFG " , False,
False)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201007130212/arcade1.PNG)

 _ **2.**_ **arcade.set_background_color():** Arcade makes it really easy to
set the background color, let’s start how to set the background color. In the
arcade module, we have an inbuilt function arcade.set_background_color( )
function, that is used to set the background colour. Its syntax is as follows:

>  **Syntax:** arcade.set_background_color(color)
>
>  
>
>
>  
>
>
>  **Parameter:**
>
>   *  **color:** specifies the color of the background
>

 **Implementation of the above syntax:**

To generate a blue background we will run the following command:

    
    
    arcade.set_background_color(arcade.color.BLUE)

 **3\. arcade.start_render( _):_** It is an inbuilt function in the arcade
module of Python which actually informs the arcade module to start
functioning. To tell Arcade that you start sending drawing commands, you need
to use the arcade.start.render(). It takes no argument. The syntax is as
follows:-

>  **Syntax:** arcade.start_render()
>
>  **Parameters:** None

 **4\. arcade.finish_render():** It is an inbuilt function in the arcade
module of Python which actually displays what we have drawn. It takes no
argument. The syntax is as follows:-

>  **Syntax:** arcade.finish_render()
>
>  **Parameters:** None

 **5\. arcade.run(): __** It basically runs the main program. It is usually
the last command of the program. It also helps to hold the output on the
screen until the user doesn’t exist. The syntax is as follows:

>  **Syntax:** arcade.run()
>
>  **Parameters:** None

Since now we have understood the functions and their use. So let’s take an
example of implementing all the above mentioned functions together.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import arcade module

import arcade

 

# open the window

arcade.open_window(500, 500, "Welcome to GFG", False,
False)

 

# set background colour

arcade.set_background_color(arcade.color.PINK)

 

# start drawing

arcade.start_render()

 

# finish drawing

arcade.finish_render()

 

# to keep output

# window open

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201001173043/Pink-300x148.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

