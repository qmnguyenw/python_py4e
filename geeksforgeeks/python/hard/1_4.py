Matplotlib – Cursor Widget



Matplotlib is a Data Visualization library in python. It consists of many
widgets that are designed to work for any of the GUI backends. Some examples
of widgets in matplotlib are Button, CheckButtons, RadioButtons, Cursor, and
TextBox. In this article, the Cursor Widget of Matplotlib library has been
discussed.

A Cursor spans the axes horizontally and/or vertically and moves with the
mouse cursor.

> **Syntax:** Cursor(ax, horizOn=True, vertOn=True, useblit=False,
> **lineprops)
>
>  **Parameters:**
>
>   *  **ax :** Axes to attach the cursor to.
>   *  **Optional Parameters:**
>   *  **horizOn :** To draw the horizontal line(default: True).
>   *  **vertOn :** To draw the vertical line(default: True).
>   *  **useblit :** Use blitting for faster drawing if supported by the
> backend(default: False).
>   *  ****lineprops:** Line properties to control appearance of the
> lines(linewidth, color).
>

 **Example 1:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing cursor widget from matplotlib

from matplotlib.widgets import Cursor

import matplotlib.pyplot as plt

import numpy as np

 

fig = plt.figure()

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

 

num = 100

x = np.random.rand(num)

y = np.random.rand(num)

 

ax.scatter(x, y, c='blue')

ax.set_xlabel('X-axis')

ax.set_ylabel('Y-axis')

 

cursor = Cursor(ax, color='green', linewidth=2)

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210305180202/CursorWidget.jpg)

In the above output, the cursor can be moved horizontally and vertically
throughout the matplotlib axes. We can just drag the cursor wherever
necessary.

###  **MultiCursor**

MultiCursor is used to show cursor on multiple plots at the same time i.e.,
Cursor is shared between multiple axes.

>  **Syntax:**
>
> MultiCursor(canvas, axes, useblit=True, horizOn=False, vertOn=True,
> **lineprops)

 **Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import MultiCursor from matplotlib

from matplotlib.widgets import MultiCursor

import matplotlib.pyplot as plt

import numpy as np

 

fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)

 

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

y = np.sin(x)

z = np.cos(x)

 

ax1.plot(x, y, label="sin function")

ax1.legend(loc="upper right")

ax2.plot(x, z, label="cos function")

 

multi = MultiCursor(fig.canvas, (ax1, ax2), color='g', lw=2,

 horizOn=False, vertOn=True)

 

ax2.legend(loc="upper right")

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210305190737/CursorWidget2.JPG)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from matplotlib.widgets import MultiCursor

import matplotlib.pyplot as plt

import numpy as np

 

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,
5))

 

x1 = ['Telugu', 'Hindi', 'English',

 'Maths', 'Science', 'Social']

y1 = [45, 34, 30, 45, 50, 38]

y2 = [36, 28, 30, 45, 38, 50]

 

labels = ["in 2020", "in 2021"]

 

l1 = ax1.plot(x1, y1, 'o', color="green")

l2 = ax2.plot(x1, y2, 'o', color="blue")

 

ax1.set_yticks(np.arange(0, 51, 5))

ax2.set_yticks(np.arange(0, 51, 5))

 

ax1.set_ylabel('Number of students passed', fontsize=15)

 

fig.legend([l1, l2], labels=labels, loc="upper right")

cursor = MultiCursor(fig.canvas, (ax1, ax2), color='r',

 lw=2, horizOn=True, vertOn=True)

 

plt.subplots_adjust(right=0.9)

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210305194148/cursorwidget3.JPG)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

