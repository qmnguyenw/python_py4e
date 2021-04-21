Change the error bar thickness in Matplotlib



Matplotlib is a Python library which is widely used by data analytics.
_Matplotlib.pyplot.errorbar() is a pyplot module_ consisting of a function
which provides a MATLAB like interface.

##  **Changing Error Bar Thickness**

Before changing the thickness of error bar let us see what error bar is and
how we can plot and use them.

 **Error Bar:** Error bars are bars that we incorporate within our data
conveying the unpredictabilty in reported measurements. In layman terms it
displays graphical representations of the variableness of data and used on
graphs to show the error measurement.

>  **Syntax:** _matplotlib.pyplot.errorbar(x, y, yerr=None, xerr=None, fmt=”,
> ecolor=None, elinewidth=None, capsize=None, barsabove=False, lolims=False,
> uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=None, *,
> data=None, **kwargs)_

 **Example 1:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing necessary libraries

import matplotlib.pyplot as plt

 

# example data

x = np.arange(3, 5, 0.5)

y = np.arange(9, 11, 0.5)

 

# ploting with default thickness of bar

plt.title("1. Without changing thickness")

plt.errorbar(x, y, xerr=0.2, yerr=0.6, fmt='o')

plt.show()

 

# ploting with changed thickness of bar

plt.title("1. With changed thickness of bar")

 

# change elinwidth to change the thickness of bar

plt.errorbar(x, y, xerr=0.2, yerr=0.6, fmt='o',
elinewidth=4)

plt.show()  
  
---  
  
 __

 __

