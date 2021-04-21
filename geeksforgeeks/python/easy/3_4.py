Matplotlib.pyplot.text() function in Python



This function is used to add a text to the axes at location x, y in data
coordinates.

    
    
     **Syntax:** matplotlib.pyplot.text(x, y, s, fontdict=None, **kwargs)

 **parameters** |  **Description**|  x, y:float| The position to place the
text. By default, this is in data coordinates. The coordinate system can be
changed using the transform parameter.| s :str| The text.| fontdict : dict
default none| A dictionary to override the default text properties. If
fontdict is None, the defaults are determined by rcParams.| **kwargs| Text
properties.  
---|---  
  
 **Example #1:** Text on plot sheet

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import matplotlib.pyplot

 

matplotlib.pyplot.text(0.5, 0.5, "Hello World!")

matplotlib.pyplot.savefig("out.png")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201111155123/out-300x225.png)

  

  

 **Example #2:** Add text to a plot

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import matplotlib.pyplot as plt

 

 

w = 4

h = 3

d = 70

 

plt.figure(figsize=(w, h), dpi=d)

 

x = [1, 2, 4]

x_pos = 0.5

y_pos = 3

 

plt.text(x_pos, y_pos, "text on plot")

plt.plot(x)

plt.savefig("out.png")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201111153951/out.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

