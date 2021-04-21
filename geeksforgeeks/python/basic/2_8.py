Use error bars in a Matplotlib scatter plot



 **Prerequisites:**Matplotlib

In this article, we will create a scatter plot with error bars using
Matplotlib. Error bar charts are a great way to represent the variability in
your data. It can be applied to graphs to provide an additional layer of
detailed information on the presented data.

### **Approach**

  * Import required python library.
  * Create data.
  * Pass required values to errorbar() function
  * Plot graph.

>  _ **Syntax:** matplotlib.pyplot.errorbar(x, y, yerr=None, xerr=None, fmt=”,
> ecolor=None, elinewidth=None, capsize=None, barsabove=False, lolims=False,
> uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=None,
> \\*, data=None, \\*\\*kwargs)_
>
>  _ **Parameters:** This method accept the following parameters that are
> described below:_
>
>   *  _ **x, y:** These parameters are the horizontal and vertical
> coordinates of the data points._
>   *  _ **fmt:** This parameter is an optional parameter and it contains the
> string value._
>   *  _ **capsize:** This parameter is also an optional parameter. And it is
> the length of the error bar caps in points with default value NONE._
>

Implementation of the concept discussed above is given below:

 **Example 1:** Adding Some error in a ‘y’ value.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import matplotlib.pyplot as plt

 

a = [1, 3, 5, 7]

b = [11, -2, 4, 19]

plt.scatter(a, b)

 

c = [1, 3, 2, 1]

 

plt.errorbar(a, b, yerr=c, fmt="o")

plt.show()  
  
---  
  
 __

 __

