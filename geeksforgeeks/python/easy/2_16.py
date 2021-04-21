Hide Axis, Borders and White Spaces in Matplotlib



When we draw plots using Matplotlib, the ticks and labels along x-axis &
y-axis are drawn too. For drawing creative graphs, many times we hide x-axis &
y-axis.

##  **How to hide axis in** **matplotlib** **figure?**

The **matplotlib.pyplot.axis(‘off’)** command us used to hide the axis(both
x-axis & y-axis) in the matplotlib figure.

 **Example:**

Let us consider the following figure in which we have to hide the axis.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# code

import numpy as np

import matplotlib.pyplot as plt

 

# Marks of RAM in different subjects out of 100.

x = ['Science', 'Maths', 'English', 'History',
'Geography']

y = [75, 85, 88, 78, 74]

 

plt.bar(x, y)

plt.xlabel("Subject")

plt.ylabel("Ram's marks out of 100")

plt.show()  
  
---  
  
 __

 __

