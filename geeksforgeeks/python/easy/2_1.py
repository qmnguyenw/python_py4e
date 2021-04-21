How to plot a simple vector field in Matplotlib ?



The quantity incorporating both magnitude and direction **** is known as
Vectors. In simple words, we can say, Vector Field is an engagement or
collaboration of such vectors in a subset of space. Vector fields are the key
aspects of understanding our real-life surrounding.

For more intuition, you can think of a vector field as representing a
multivariable function whose input and output spaces each have the same
dimension. The length of arrows drawn in a vector field is usually not to
scale, but the ratio of the length of one vector to another should be
accurate.

In this article, we are going to discuss how to plot a vector field in python.
In order to perform this task we are going to use the _quiver()_ method and
the _streamplot()_ method in _matplotlib_ module.

 **Syntax:**

To plot a vector field using the _quiver()_ method:

  

  

> matplotlib.pyplot.quiver(X, Y, U, V, **kw)

Where X _, Y_ define the Vector location and U _, V_ are directional arrows
with respect of the Vector location.

To plot a vector field using the _streamplot()_ method:

> matplotlib.pyplot.streamplot(X, Y, U, V, density=1, linewidth=None,
> color=None, **kw)

Where X, Y are evenly spaced grid[1D array] and U and V represent the stream
velocity of each point present on the grid. Density is the no. of vector per
area of the plot. Line width represents the thickness of streamlines.

 **Below are some examples which depict how to plot vector fields using** _
**matplotlib**_ **module:**

 **Example 1:** Plotting a single vector using _quiver()_ method in
_matplotlib_ module.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Import libraries

import numpy as np

import matplotlib.pyplot as plt

 

# Vector origin location

X = [0]

Y = [0]

 

# Directional vectors

U = [2] 

V = [1] 

 

# Creating plot

plt.quiver(X, Y, U, V, color='b', units='xy', scale=1)

plt.title('Single Vector')

 

# x-lim and y-lim

plt.xlim(-2, 5)

plt.ylim(-2, 2.5)

 

# Show plot with gird

plt.grid()

plt.show()  
  
---  
  
 __

 __

