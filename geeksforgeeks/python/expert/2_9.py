How to Set Plot Background Color in Matplotlib?



 **Prerequisites:**

  * Matplotlib
  * Numpy

From the below figure one can infer that a plot consists of X-axis, Y-axis,
plot title and the axes. By default, the color of the plot is white. If we
have to set the background color of the plot so that our plot looks beautiful,
we have to make the axes object, by using axes() attribute after plotting the
graph.

![](https://media.geeksforgeeks.org/wp-content/uploads/20201208161506/fig.png)

 **Approach:**

  * Import module
  * Load or create data
  * Plot a regular graph
  * Create axes object
  * Set attribute set_facecolor() to the required color. This attribute accepts both name or color code of the color

Follow the given examples to understand better.

  

  

 **Example:** Default color plot

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import matplotlib.pyplot as plt

 

# giving values for x and y to plot

student_marks = [50, 60, 70, 80, 90]

student_grade = ['B', 'B', 'B+', 'B+', 'A']

 

plt.plot(student_marks, student_grade)

 

# Giving x label using xlabel() method

# with bold setting

plt.xlabel("student_marks", fontweight='bold')

 

# Giving y label using xlabel() method

# with bold setting

plt.ylabel("student_grade", fontweight='bold')

 

# Giving title to the plot

plt.title("Student Marks v/s Student Grade")

 

# Showing the plot using plt.show()

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201208173754/Capture.PNG)

 **Example 2 :** Setting background color to yellow

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import matplotlib.pyplot as plt

 

# giving values for x and y to plot

student_marks = [50, 60, 70, 80, 90]

student_grade = ['B', 'B', 'B+', 'B+', 'A']

plt.plot(student_marks, student_grade)

 

# Giving x label using xlabel() method

# with bold setting

plt.xlabel("student_marks", fontweight='bold')

ax = plt.axes()

 

# Setting the background color of the plot 

# using set_facecolor() method

ax.set_facecolor("yellow")

 

# Giving y label using xlabel() method 

# with bold setting

plt.ylabel("student_grade", fontweight='bold')

 

# Giving title to the plot

plt.title("Student Marks v/s Student Grade")

 

# Showing the plot using plt.show()

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201208175947/Figure1.png)

  

  

 **Example 3:** Setting background color to violet

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import matplotlib.pyplot as plt

import numpy as np

 

# giving values for x and y to plot

x = np.arange(0, 10, .1)

y = np.sin(x)

plt.plot(x, y)

 

# Giving x label using xlabel() method 

# with bold setting

plt.xlabel("X")

ax = plt.axes()

 

# Setting the background color of the

# plot using set_facecolor() method

ax.set_facecolor("violet")

 

# Giving y label using xlabel() method 

# with bold setting

plt.ylabel('sin(x)')

 

# Showing the plot using plt.show()

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201208181647/Figure1.png)

###  **Setting Outer and Inner color of plot**

We can also set the color of the outer portion of the plot. To set both the
color for plot background and for outer portion of the plot the only change we
have to do in our code is that we have to add _plt.figure(faceccolor=’color’)_
before plotting the graph.

 **Example 1:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import matplotlib.pyplot as plt

import numpy as np

 

# giving values for x and y to plot

x = np.arange(0, 10, .1)

y = np.sin(x)

 

# Set background color of the outer 

# area of the plt

plt.figure(facecolor='yellow')

 

# Plotting the graph between x and y

plt.plot(x, y)

 

# Giving x label using xlabel() method

# with bold setting

plt.xlabel("X")

ax = plt.axes()

 

# Setting the background color of the plot 

# using set_facecolor() method

ax.set_facecolor("violet")

 

# Giving y label using xlabel() method with

# bold setting

plt.ylabel('sin(x)')

 

# Showing the plot using plt.show()

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201208193057/Figure12.png)

 **Example 2:** Setting plot color using html color codes

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import matplotlib.pyplot as plt

import numpy as np

 

# giving values for x and y to plot

x = np.arange(0, 10, .1)

y = np.sin(x)

 

# Set background color of the outer

# area of the plt

plt.figure(facecolor='#94F008')

 

# Plotting the graph between x and y

plt.plot(x, y)

 

# Giving x label using xlabel() method

# with bold setting

plt.xlabel("X")

ax = plt.axes()

 

# Setting the background color of the plot 

# using set_facecolor() method

ax.set_facecolor("#1CC4AF")

 

# Giving y label using xlabel() method with

# bold setting

plt.ylabel('sin(x)')

 

# Showing the plot using plt.show()

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201208195641/Figure12.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

