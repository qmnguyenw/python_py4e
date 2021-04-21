Matplotlib.pyplot.colorbar() function in Python



Colorbars are a visualization of the mapping from scalar values to colors. In
Matplotlib they are drawn into a dedicated axis.

 **Note:** Colorbars are typically created through **Figure.colorbar** or its
pyplot wrapper **pyplot.colorbar** , which uses make_axes and Colorbar
internally. As an end-user, you most likely won’t have to call the methods or
instantiate the classes in this module explicitly.

##  **matplotlib.pyplot.colorbar() in python**

The **colorbar() function** in pyplot module of matplotlib adds a colorbar to
a plot indicating the color scale.

>  **Syntax:** matplotlib.pyplot.colorbar(mappable=None, cax=None, ax=None,
> **kwarg)
>
>  **Parameters:**
>
>  
>
>
>  
>
>
>  **ax:** This parameter is an optional parameter and it contains Axes or
> **** list of Axes.
>
>  ****kwarg** (keyword arguments): This parameter is an optional parameter
> and are of two kinds:
>
> **colorbar properties:**
>
>  **extend:** {‘neither’, ‘both’, ‘min’, ‘max’} makes pointed end(s) for out-
> of-range  
> values.
>
> **label:** The label on the colorbar’s long axis.
>
> **ticks** :None or list of ticks or Locator. __
>
> _**Returns:** colorbar which is an instance of the class
> ‘matplotlib.colorbar.Colorbar’. _

Below examples illustrate the matplotlib.pyplot.colorbar() function in
matplotlib.pyplot:

 **Example #1:** To **** Add a horizontal colorbar to a scatterplot.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# pyplot.colorbar() method

import numpy as np

import matplotlib.pyplot as plt

 

# Dataset

# List of total number of items purchased 

# from each products

purchaseCount = [100, 200, 150, 23, 30, 50,

 156, 32, 67, 89]

 

# List of total likes of 10 products

likes = [50, 70, 100, 10, 10, 34, 56, 18,
35, 45]

 

# List of Like/Dislike ratio of 10 products

ratio = [1, 0.53, 2, 0.76, 0.5, 2.125, 0.56,


 1.28, 1.09, 1.02]

 

# scatterplot

plt.scatter(x=purchaseCount, y=likes, c=ratio,
cmap="summer")

 

plt.colorbar(label="Like/Dislike Ratio",
orientation="horizontal")

plt.show()  
  
---  
  
 __

 __

