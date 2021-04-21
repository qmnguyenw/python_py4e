How to Change Legend Font Size in Matplotlib?



Matplotlib is a library for creating interactive visualizations in Python. The
functions in matplotlib make it work like MATLAB software. The legend() method
in matplotlib describes the elements in the plot. In this article, we are
going to Change Legend Font Size in Matplotlib.

 **Syntax:**

    
    
    matplotlib.pyplot.legend(*args, **kwargs)

 **It can be done in different ways:**

  * To use font size as a parameter.
  * To use prop keyword to change the font size in legend.
  * To use rcParams Method.

 **Method 1:**

Example 1 and example 2 clearly differentiate changes between default font
size and changed the font size in legend.

  

  

 **Example 1:** Default font size of the text in the legend

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

 

plt.figure(figsize = (8, 4))

 

x = ['Arjun', 'Bharath', 'Raju', 'Seeta', 'Ram']

y = [5, 7, 8, 4, 6]

 

plt.bar(x, y, color = 'g')

 

plt.xlabel('Students', fontsize = 18)

plt.ylabel('Marks', fontsize = 18)

 

#Default fontsize of text using legend

plt.legend(['Marks scored'])

 

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225225628/fontsizeinlegend.png)

**Example 2:** Changing the font size of the text in legend

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

 

plt.figure(figsize = (8, 4))

 

x = ['Arjun', 'Bharath', 'Raju', 'Seeta', 'Ram']

 

y = [5, 7, 8, 4, 6]

 

plt.bar(x, y, color = 'g')

 

plt.xlabel('Students', fontsize = 18)

plt.ylabel('Marks', fontsize = 18)

 

#Changing text fontsize in legend 

plt.legend(['Marks scored'], fontsize = 17)

 

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225230405/changefontsizeinlegendmatplotlib.png)

  

  

The above example changes the font size of items in legend. The font size
parameter can have integer or float values. It also accepts the string sizes
like: ‘xx-small’, ‘x-small’, ‘small’, ‘medium’, ‘large’, ‘x-large’, ‘xx-
large’.

 **Method 2:** The prop keyword is used to change the font size property. It
is used in matplotlib as:

> matplotlib.pyplot.legend(*args… , prop = {‘size’ : 20})

 **Example 3:** Using a prop keyword for changing the font size in legend.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import matplotlib.pyplot as plt

 

plt.figure(figsize = (8 , 5))

 

plt.plot([1, 2, 4, 8, 30, 1])

plt.plot([1, 6, 13, 20, 38, 1])

plt.plot([1, 4, 8, 14, 20, 1])

plt.plot([1, 3, 4, 5, 10, 1])

 

#Using prop keyword in legend to change font size

plt.legend(['blue', 'orange', 'green', 'red'], 

 prop = {'size' : 20}, 

 loc = 'upper left', shadow = True,

 facecolor = 'yellow')

 

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201226013321/changefontinlegend.png)

 **Method 3:**

The matplotlib.rcparams is a dictionary-like variable that has all the
configuration settings to customize default parameters. The matplotlib.rc()
command is used to change multiple settings with the use of keyword arguments.

 **Syntax:**

> matplotlib.pyplot.rc(group, **kwargs)

For Example,

    
    
    matplotlib.pyplot.rc ('lines', linewidth = 5, color = 'g')

 **Example 4:**

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

from pylab import *

 

x = np.linspace(0, (2*np.pi), endpoint = True)

 

xlim(x.min(), x.max())

 

xticks([0, np.pi/2, np.pi, (3*np.pi/2),
(2*np.pi)], 

 [r'$0$', r'$+\pi/2$', r'$+\pi$', r'$3/2\pi$',
r'$2\pi$'])

 

ylim(-1, 0, 1)

yticks([-1, 0, +1], 

 [r'$-1$', r'$0$', r'$+1$'])

 

plt.plot(x, np.sin(x), label = "sin(x)")

plt.plot(x, np.cos(x), label = "cos(x)")

 

plt.title('Trignometric Functions', fontsize = 22)

 

plt.xlabel('Angles', fontsize = 18)

plt.ylabel('Values', fontsize = 18)

 

plt.legend(loc = 'upper center')

 

plt.rc('legend', fontsize = 16)

 

#plt.grid()

plt.tight_layout()

 

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210101003842/increaselegendfontsize.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

