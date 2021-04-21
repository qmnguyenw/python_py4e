Matplotlib.figure.Figure.add_subplot() in Python



 **Matplotlib** is a library in Python and it is numerical – mathematical
extension for NumPy library. The **figure module** provides the top-level
Artist, the Figure, which contains all the plot elements. This module is used
to control the default spacing of the subplots and top level container for all
plot elements.

## matplotlib.figure.Figure.add_subplot() function

 **The add_subplot() method** figure module of matplotlib library is used to
add an Axes to the figure as part of a subplot arrangement.

>  **Syntax:** add_subplot(self, *args, **kwargs)
>
>  **Parameters:** This accept the following parameters that are described
> below:
>
>   *  **projection :** This parameter is the projection type of the Axes.
>   *  **sharex, sharey :** These parameters share the x or y axis with sharex
> and/or sharey.
>   *  **label :** This parameter is the label for the returned axes.
>

>
>  **Returns:** This method return the axes of the subplot.
>
>  
>
>
>  
>

Below examples illustrate the matplotlib.figure.Figure.add_subplot() function
in matplotlib.figure:

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Implementation of matplotlib function

import matplotlib.pyplot as plt

from mpl_toolkits.axisartist.axislines import Subplot

 

 

fig = plt.figure(figsize =(4, 4))

 

ax = Subplot(fig, 111)

fig.add_subplot(ax)

 

ax.axis["left"].set_visible(False)

ax.axis["bottom"].set_visible(False)

 

fig.suptitle('matplotlib.figure.Figure.add_subplot() \

function Example\n\n', fontweight ="bold")

 

plt.show()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200428232435/sub.jpg)

 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Implementation of matplotlib function

import matplotlib.pyplot as plt

import numpy as np

 

 

np.random.seed(19680801)

 

xdata = np.random.random([2, 10])

 

xdata1 = xdata[0, :]

xdata2 = xdata[1, :]

 

ydata1 = xdata1 ** 2

ydata2 = 1 - xdata2 ** 3

 

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

ax.plot(xdata1, ydata1, color ='tab:blue')

ax.plot(xdata2, ydata2, color ='tab:orange')

 

ax.set_xlim([0, 1])

ax.set_ylim([0, 1])

fig.suptitle('matplotlib.figure.Figure.add_subplot() \

function Example\n\n', fontweight ="bold")

 

plt.show()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428232437/sub11.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

