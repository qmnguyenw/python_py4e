How to Create a Single Legend for All Subplots in Matplotlib?



The subplot() function in matplotlib helps to create a grid of subplots within
a single figure. In a figure, subplots are created and ordered row-wise from
the top left. A legend in the Matplotlib library basically describes the graph
elements. The legend() can be customized and adjusted anywhere inside or
outside the graph by placing it at various positions. Sometimes it is
necessary to create a single legend for all subplots. Below are the examples
that show a single legend for all subplots.

 **Syntax of Subplot():**

    
    
    subplot(nrows,ncols,nsubplot)

For example, subplot(2,1,1) is the figure which represents the first subplot
with 2 rows and one column, the first subplot lies in the first row.

The subplot(2,1,2) represents the second subplot which lies in the second row
in the first column.

**The legend command Syntax:**

  

  

    
    
    legend(*args, **kwargs)

If the length of arguments i.e, args is 0 in the legend command then it
automatically generates the legend from label properties by calling
get_legend_handles_labels() method.

For example, ax.legend() is equivalent to:

    
    
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)

The get_legend_handles_labels() method returns a tuple of two lists, i.e.,
list of artists and list of labels.

**Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing required libraries

import matplotlib.pyplot as plt

import numpy as np

 

# 2 subplots in 1 row and 2 columns

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,
5))

 

x1 = ['Telugu', 'Hindi', 'English',

 'Maths', 'Science', 'Social']

y1 = [45, 34, 30, 45, 50, 38]

y2 = [36, 28, 30, 45, 38, 48]

 

# Labels to use in the legend for each line

labels = ["in 2019", "in 2020"]

 

# Title for subplots

fig.suptitle('Number of Students passed in each subject\

from a class in 2019 & 2020', fontsize=20)

 

# Creating the sub-plots.

l1 = ax1.plot(x1, y1, color="green")

l2 = ax2.plot(x1, y2, color="blue")

 

ax1.set_yticks(np.arange(0, 51, 5))

ax2.set_yticks(np.arange(0, 51, 5))

 

ax1.set_ylabel('Number of students', fontsize=25)

 

 

fig.legend([l1, l2], labels=labels,

 loc="upper right")

 

# Adjusting the sub-plots

plt.subplots_adjust(right=0.9)

 

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201210170308/singlelegendforsubplots.png)

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Plotting sub-plots of number of

# students passed in each subject 

# in academic year 2017-20.

import matplotlib.pyplot as plt

import numpy as np

 

plt.style.use('seaborn') # Plot Styles

 

fig = plt.figure()

 

# 4 subplots in 2 rows and 2 columns in a figure

axes = fig.subplots(nrows=2, ncols=2)

 

axes[0, 0].bar(['Telugu', 'Hindi', 'English', 

 'Maths', 'Science', 'Social'],

 [50, 27, 42, 34, 45, 48], 

 color='g', label="Students passed in 2017")

 

axes[0, 0].set_yticks(np.arange(0, 51, 5))

 

axes[0, 1].bar(['Telugu', 'Hindi', 'English', 

 'Maths', 'Science', 'Social'],

 [50, 27, 42, 34, 45, 48], 

 color='y', label="Students passed in 2018")

 

axes[0, 1].set_yticks(np.arange(0, 51, 5))

 

axes[1, 0].bar(['Telugu', 'Hindi', 'English', 

 'Maths', 'Science', 'Social'],

 [40, 27, 22, 44, 35, 38],

 color='r', label="Students passed in 2019")

 

axes[1, 0].set_yticks(np.arange(0, 51, 5))

axes[1, 0].set_xlabel('Subjects', fontsize=25)

 

# rotating third sub-plot x-axis labels

for tick in axes[1, 0].get_xticklabels():

 tick.set_rotation(45)

 

axes[1, 0].set_ylabel(" Number of Students passed in 2017-2020",
fontsize=20)

 

 

axes[1, 1].bar(['Telugu', 'Hindi', 'English',

 'Maths', 'Science', 'Social'],

 [40, 27, 32, 44, 45, 48], 

 color='b', label="Students passed in 2020")

 

axes[1, 1].set_xlabel('Subjects', fontsize=20)

axes[1, 1].set_yticks(np.arange(0, 51, 5))

 

 

lines = []

labels = []

 

for ax in fig.axes:

 Line, Label = ax.get_legend_handles_labels()

 # print(Label)

 lines.extend(Line)

 labels.extend(Label)

 

# rotating x-axis labels of last sub-plot

plt.xticks(rotation=45)

 

fig.legend(lines, labels, loc='upper right')

 

plt.show()  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201209231510/subplots.jpg)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

