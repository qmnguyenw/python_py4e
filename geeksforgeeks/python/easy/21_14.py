Python | Introduction to Matplotlib



Matplotlib is an amazing visualization library in Python for 2D plots of
arrays. Matplotlib is a multi-platform data visualization library built on
NumPy arrays and designed to work with the broader SciPy stack. It was
introduced by John Hunter in the year 2002.

One of the greatest benefits of visualization is that it allows us visual
access to huge amounts of data in easily digestible visuals. Matplotlib
consists of several plots like line, bar, scatter, histogram etc.

 **Installation :**  
Windows, Linux and macOS distributions have matplotlib and most of its
dependencies as wheel packages. Run the following command to install
matplotlib package :

    
    
    python -mpip install -U matplotlib

  
**Importing matplotlib :**

    
    
    from matplotlib import pyplot as plt
    _or_
    import matplotlib.pyplot as plt 

#### Basic plots in Matplotlib :

Matplotlib comes with a wide variety of plots. Plots helps to understand
trends, patterns, and to make correlations. They’re typically instruments for
reasoning about quantitative information. Some of the sample plots are covered
here.

  

  

 **Line plot :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing matplotlib module

from matplotlib import pyplot as plt

 

# x-axis values

x = [5, 2, 9, 4, 7]

 

# Y-axis values

y = [10, 5, 8, 4, 2]

 

# Function to plot

plt.plot(x,y)

 

# function to show the plot

plt.show()  
  
---  
  
 __

 __

Output :

![](https://media.geeksforgeeks.org/wp-content/uploads/line-plot-300x254.png)  
  
**Bar plot :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing matplotlib module

from matplotlib import pyplot as plt

 

# x-axis values

x = [5, 2, 9, 4, 7]

 

# Y-axis values

y = [10, 5, 8, 4, 2]

 

# Function to plot the bar

plt.bar(x,y)

 

# function to show the plot

plt.show()  
  
---  
  
 __

 __

Output :  
![](https://media.geeksforgeeks.org/wp-content/uploads/bar-plot-300x254.png)  
  
**Histogram :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing matplotlib module

from matplotlib import pyplot as plt

 

# Y-axis values

y = [10, 5, 8, 4, 2]

 

# Function to plot histogram

plt.hist(y)

 

# Function to show the plot

plt.show()  
  
---  
  
 __

 __

Output :

![](https://media.geeksforgeeks.org/wp-
content/uploads/histogram-1-300x256.png)

 **Scatter Plot :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing matplotlib module

from matplotlib import pyplot as plt

 

# x-axis values

x = [5, 2, 9, 4, 7]

 

# Y-axis values

y = [10, 5, 8, 4, 2]

 

# Function to plot scatter

plt.scatter(x, y)

 

# function to show the plot

plt.show()  
  
---  
  
 __

 __

Output :

![](https://media.geeksforgeeks.org/wp-content/uploads/scatter-
plot-300x252.png)  
  
Reference : Matplotlib Documentation.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

