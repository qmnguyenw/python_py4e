Matplotlib.pyplot.plot() function in Python



 **Matplotlib** is a library in Python and it is numerical – mathematical
extension for NumPy library. **Pyplot** is a state-based interface to a
**Matplotlib** module which provides a MATLAB-like interface. There are
various plots which can be used in Pyplot are Line Plot, Contour, Histogram,
Scatter, 3D Plot, etc.

## matplotlib.pyplot.plot() Function

The **plot() function** in pyplot module of matplotlib library is used to make
a 2D hexagonal binning plot of points x, y.

>  **Syntax:** matplotlib.pyplot.plot(\\*args, scalex=True, scaley=True,
> data=None, \\*\\*kwargs)
>
>  **Parameters:** This method accept the following parameters that are
> described below:
>
>   *  **x, y:** These parameter are the horizontal and vertical coordinates
> of the data points. x values are optional.
>   *  **fmt:** This parameter is an optional parameter and it contains the
> string value.
>   *  **data:** This parameter is an optional parameter and it is an object
> with labelled data.
>

>
>  **Returns:** This returns the following:
>
>  
>
>
>  
>
> *  **lines :** This returns the list of Line2D objects representing the
> plotted data.

Below examples illustrate the matplotlib.pyplot.plot() function in
matplotlib.pyplot:

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

import numpy as np 

 

plt.plot([1, 2, 3]) 

plt.title('matplotlib.pyplot.plot() example 1') 

plt.draw() 

plt.show()   
  
---  
  
__

__

**Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200604112934/plot13.jpg)

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

 

# Fixing random state for reproducibility 

np.random.seed(19680801) 

 

# create random data 

xdata = np.random.random([2, 10]) 

 

# split the data into two parts 

xdata1 = xdata[0, :] 

xdata2 = xdata[1, :] 

 

# sort the data so it makes clean curves 

xdata1.sort() 

xdata2.sort() 

 

# create some y data points 

ydata1 = xdata1 ** 2

ydata2 = 1 - xdata2 ** 3

 

# plot the data 

plt.plot(xdata1, ydata1, color ='tab:blue') 

plt.plot(xdata2, ydata2, color ='tab:orange') 

 

 

# set the limits 

plt.xlim([0, 1]) 

plt.ylim([0, 1]) 

 

plt.title('matplotlib.pyplot.plot() example 2') 

 

# display the plot 

plt.show()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200604113124/plot22.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

