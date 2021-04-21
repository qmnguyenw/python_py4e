Plotting multiple bar charts using Matplotlib in Python



A multiple bar chart is also called a **Grouped Bar chart**. A Bar plot or a
Bar Chart has many customizations such as Multiple bar plots, stacked bar
plots, horizontal bar charts. Multiple bar charts are generally used for
comparing different entities. In this article, plotting multiple bar charts
are discussed.

 **Example 1:** Simple multiple bar chart

In this example we will see how to plot multiple bar charts using matplotlib,
here we are plotting multiple bar charts to visualize the number of boys and
girls in each Group.

 **Approach:**

  1. Importing required libraries such as numpy for performing numerical calculations with arrays and matplotlib for visualization of data.
  2. The data for plotting multiple bar charts are taken into the list.
  3. The np.arange( ) function from numpy library is used to create a range of values. We are creating the X-axis values depending on the number of groups in our example.
  4. Plotting the multiple bars using plt.bar( ) function.
  5. To avoid overlapping of bars in each group, the bars are shifted -0.2 units and +0.2 units from the X-axis.
  6. The width of the bars of each group is taken as 0.4 units.
  7. Finally, the multiple bar charts for both boys and girls are plotted in each group.

 **Code:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np 

import matplotlib.pyplot as plt 

 

X = ['Group A','Group B','Group C','Group D']

Ygirls = [10,20,20,40]

Zboys = [20,30,25,30]

 

X_axis = np.arange(len(X))

 

plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Girls')

plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Boys')

 

plt.xticks(X_axis, X)

plt.xlabel("Groups")

plt.ylabel("Number of Students")

plt.title("Number of Students in each group")

plt.legend()

plt.show()  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210216005002/Multiplebarcharts1.png)

 **Example 2:** Number of Men and Women voted from 2018-2021

 **Approach :**

  1. Importing required libraries such as numpy for performing numerical calculations with arrays and matplotlib for visualization of data.
  2. The Men and Women data for multiple bar charts are taken into a list for easy plotting.
  3. The np.arange( ) function from numpy library is used to create a range of values.
  4. Plotting the multiple bars using plt.bar( ) function in matplotlib library.
  5. To avoid overlapping of bars in each group, the bars are shifted 0.25 units from the X-axis in this example.
  6. The width of the bars of each group is taken as 0.25 units.
  7. The X-axis labels(Years) and x-ticks are plotted as required in our visualization.
  8. Finally, the multiple bar chart for the number of men and women who voted every year is plotted.

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

import matplotlib.pyplot as plt

 

Women = [115, 215, 250, 200]

Men = [114, 230, 510, 370]

 

n=4

r = np.arange(n)

width = 0.25

 

 

plt.bar(r, Women, color = 'b',

 width = width, edgecolor = 'black',

 label='Women')

plt.bar(r + width, Men, color = 'g',

 width = width, edgecolor = 'black',

 label='Men')

 

plt.xlabel("Year")

plt.ylabel("Number of people voted")

plt.title("Number of people voted in each year")

 

# plt.grid(linestyle='--')

plt.xticks(r +
width/2,['2018','2019','2020','2021'])

plt.legend()

 

plt.show()  
  
---  
  
 __

 __

 **Output :**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210216125126/MultipleBarchart2.png)

 **Example3: Scores of different players on different dates**

 **Approach:**

  1. Importing required libraries such as numpy for performing numerical calculations with arrays and matplotlib for visualization of data.
  2. The np.arange( ) function from numpy library is used to create a range of values(Here, 3 values).
  3. Plotting the multiple bars using plt.bar( ) function in matplotlib library. In this Example, Dates are plotted on X-axis and Players Scores on Y-axis.
  4. To avoid overlapping of bars in each group, the bars are shifted 0.25 units from the previous bar.
  5. The width of the bars of each group is taken as 0.25 units with different colors.
  6. The X-axis labels and x-ticks are plotted as required in our visualization.
  7. Finally, the multiple bar chart for the Scores of different players on different dates is plotted.

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

import matplotlib.pyplot as plt

 

N = 3

ind = np.arange(N) 

width = 0.25

 

xvals = [8, 9, 2]

bar1 = plt.bar(ind, xvals, width, color = 'r')

 

yvals = [10, 20, 30]

bar2 = plt.bar(ind+width, yvals, width, color='g')

 

zvals = [11, 12, 13]

bar3 = plt.bar(ind+width*2, zvals, width, color = 'b')

 

plt.xlabel("Dates")

plt.ylabel('Scores')

plt.title("Players Score")

 

plt.xticks(ind+width,['2021Feb01', '2021Feb02',
'2021Feb03'])

plt.legend( (bar1, bar2, bar3), ('Player1', 'Player2', 'Player3')
)

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210216145547/Multiplebarchart3.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

