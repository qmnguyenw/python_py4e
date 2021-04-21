Add Text Inside the Plot in Matplotlib



In this article, We are going to see how to add text inside the plot in
Matplotlib. The matplotlib.pyplot.text() function is used to add text inside
the plot. The syntax adds text at an arbitrary location of the axes. It also
supports mathematical expressions.

>  **Syntax:** matplotlib.pyplot.text(x, y, s, fontdict=None, **kwargs)
>
>  **Parameters:**
>
>   * where x, y – coordinates
>   * s – text to be added inside the plot(string)
>   * fontdict – optional parameter. It overrides the default text properties
>   * **kwargs – text properties
>

 **Example 1:** Adding mathematical equations inside the plot.

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

 

x = np.arange(-10, 10, 0.01)

y = x**2

 

#adding text inside the plot

plt.text(-5, 60, 'Parabola $Y = x^2$', fontsize = 22)

 

plt.plot(x, y, c='g')

 

plt.xlabel("X-axis", fontsize = 15)

plt.ylabel("Y-axis",fontsize = 15)

 

plt.show()  
  
---  
  
 __

 __

