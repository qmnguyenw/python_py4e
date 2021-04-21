How to Set a Single Main Title for All the Subplots in Matplotlib?



 **Prerequisites:** Matplotlib

A title in matplotlib library describes the main subject of plotting the
graphs. Setting a title for just one plot is easy using the title() method. By
using this function only the individual title plots can be set but not a
single title for all subplots. Hence, to set a single main title for all
subplots, suptitle() method is used.

>  _ **Syntax:** suptitle(self, t, **kwargs)_
>
>  _ **Parameters:** This method accept the following parameters that are
> discussed below:_
>
>   *  _ **t :** This parameter is the title text._
>   *  _ **x:** This parameter is the x location of the text in figure
> coordinates._
>   *  _ **y:** This parameter is the y location of the text in figure
> coordinates._
>   *  _ **horizontalalignment, ha :** This parameter is the horizontal
> alignment of the text relative to (x, y)._
>   *  _ **verticalalignment, va :** This parameter is the vertical alignment
> of the text relative to (x, y)._
>   *  _ **fontsize, size :** This parameter is the font size of the text._
>   *  _ **fontweight, weight :** This parameter is the font weight of the
> text._
>

>
>  _ **Returns:** This method returns the **Text** instance of the title._

### Approach

  * Import module
  * Create data to be plotted
  * Set figure title using suptitle()
  * Plot the graph
  * Display plot

Implementation using approach given is given below:

 **Example 1:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import matplotlib.pyplot as plt

import numpy as np

 

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,
5))

 

x1 = [1, 2, 3, 4, 5, 6]

y1 = [45, 34, 30, 45, 50, 38]

y2 = [36, 28, 30, 40, 38, 48]

 

labels = ["student 1", "student 2"]

 

fig.suptitle(' Student marks in different subjects ', fontsize=30)

 

# Creating the sub-plots.

l1 = ax1.plot(x1, y1, 'o-', color='g')

l2 = ax2.plot(x1, y2, 'o-')

 

fig.legend([l1, l2], labels=labels,

 loc="upper right")

plt.subplots_adjust(right=0.9)

 

plt.show()  
  
---  
  
 __

 __

