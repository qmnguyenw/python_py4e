How to Make a Square Plot With Equal Axes in Matplotlib?



In this article, we are going to discuss how to illustrate a square plot with
equal axis using _matplotlib_ module. We can depict a Square plot using
_matplotlib.axes.Axes.set_aspect()_ and _matplotlib.pyplot.axis()_ methods.

###  **Using** _ **set_aspect()**_ **method**

>  **Syntax:** matplotlib.axes.Axes.set_aspect()
>
>  **Parameters:**
>
>   * **aspect :** This parameter accepts the following value {‘auto’,
> ‘equal’} or num.
>   *  **adjustable :** This defines which parameter will be adjusted to meet
> the required aspect.
>   *  **anchor :** This parameter is used to define where the Axes will be
> drawn if there is extra space due to aspect constraints.
>   *  **share:** This parameter is used to apply the settings to all shared
> Axes.
>

 **Example 1:**

We can generate a square plot using _matplotlib.axes.Axes.set_aspect()_
method. We will assign _equal_ as an _aspect_ argument and _box_ as
_adjustable_ argument.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required module

# import required modules

import numpy as np

import matplotlib.pyplot as plt

 

# adjust coordinates

x = y = [i for i in range(0, 6)]

 

# depict illustartion

fig = plt.figure()

ax = fig.add_subplot()

plt.plot(x, y)

 

# square plot

ax.set_aspect('equal', adjustable='box')

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201217152021/Screenshot201-300x292.png)

 **Example 2** :

The above example possibly yields a square plot when ranges for the two
tomahawks are set to be the equivalent. To produce a square plot in the
overall case, we need to physically set the viewpoint proportion utilizing the
accompanying order:

    
    
    axes.set_aspect(1./axes.get_data_ratio())

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required modules

import numpy as np

import matplotlib.pyplot as plt

 

# adjust coordinates

x = y = [i for i in range(0, 6)]

 

# depict illustartion

fig = plt.figure()

ax = fig.add_subplot()

plt.plot(x, y)

 

# square plot

ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201217152021/Screenshot201-300x292.png)

  

  

###  **Using** _ **axis()**_ **method**

>  **Syntax:** matplotlib.pyplot.axis()
>
>  **Parameters:**
>
>   * **xmin, xmax, ymin, ymax** :These parameters can be used to set the axis
> limits on the graph.
>   * **emit:** Its a bool value used to notify observers of the axis limit
> change.
>

**Example 1:**

In this example, we pass _square_ as an argument to _matplotlib.pyplot.axis()_
, it illustrates a square plot.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required module

# import required modules

import numpy as np

import matplotlib.pyplot as plt

 

# adjust coordinates

x=y=[i for i in range(0,6)]

 

# plot coordinates

plt.plot(x,y)

 

# square plot

plt.axis('square')

 

# depict illustration

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201217152021/Screenshot201-300x292.png)

 **Example 2:**

Here is another example to illustrate a square plot using _axis()_ method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing module

import matplotlib.pyplot as plt

 

# assigning x and y coordinates

x = [-5, -4, -3, -2, -1, 0, 1,
2, 3, 4, 5]

y = []

 

for i in range(len(x)):

 y.append(max(0, x[i]))

 

# depicting the visualization

plt.plot(x, y, color='green')

plt.xlabel('X')

plt.ylabel('Y')

 

# square plot

plt.axis('square')

 

# displaying the title

plt.title('ReLU Function')  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201217151805/Screenshot200-292x300.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

