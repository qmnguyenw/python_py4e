How to Reverse Axes in Matplotlib?



In Matplotlib we can reverse axes of a graph using multiple methods. Most
common method is by using invert_xaxis() and invert_yaxis() for the axes
objects. Other than that we can also use xlim() and ylim(), and axis() methods
for the pyplot object.

 **Method 1:** Using invert_xaxis() and invert_yaxis() method

To invert X-axis and Y-axis, we can use invert_xaxis() and invert_yaxis()
function. We can invert either any one of the axes or both axes using the
above methods.

 **Code:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing numpy and matplotlib

import numpy as np

import matplotlib.pyplot as plt

 

# creating an x sequence

x = np.linspace(5, 15, 35)

 

# equation of a straigt line

y = 3*x+4

 

# creating graph space for two graphs

graph, (plot1, plot2) = plt.subplots(1, 2)

 

# plot1 graph for normal axes

plot1.plot(x, y)

plot1.set_title("Normal Plot")

 

# plot2 graph for inverted axes

plot2.plot(x, y)

plot2.set_title("Inverted Plot")

plot2.invert_xaxis()

plot2.invert_yaxis()

 

# display the graph

graph.tight_layout()

plt.show()  
  
---  
  
 __

 __

