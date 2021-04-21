How to Make Boxplots with Data Points using Seaborn in Python?



Box Plot or a Whisker Plot is a statistical plot to visualize graphically,
depicting group of numerical data through their quartiles. This plot displays
the summary of set of data containing the five values known as minimum,
quartile 1, quartile 2 or median, quartile 3 and maximum, where the box is
drawn from first quartile to third quartile.

![](https://media.geeksforgeeks.org/wp-content/uploads/20201223024124/img.jpg)

A generic box plot mainly focuses on the five elements mentioned above to give
the user a quartile based interpretation of the data, but it is possible to
show data points on the box plot itself, making it more informative. For this
seaborn is equipped with stripplot() function, all we have to do is call it
just after boxplot() function with appropriate parameters to generate a
boxplot with data points.

A strip plot is drawn on its own. It is a good complement to a boxplot or
violinplot in cases where all observations are shown along with some
representation of the underlying distribution. It is used to draw a scatter
plot based on the category.

>  _ **Syntax:** seaborn.stripplot(*, x=None, y=None, hue=None, data=None,
> order=None, hue_order=None, jitter=True, dodge=False, orient=None,
> color=None, palette=None, size=5, edgecolor=’gray’, linewidth=0, ax=None,
> **kwargs)_
>
>  _ **Parameters:**_
>
>   *  _ **x, y, hue:** Inputs for plotting long-form data._
>   *  _ **data:** Dataset for plotting._
>   *  _ **order:** It is the order to plot the categorical levels in._
>   *  _ **color:** It is the color for all of the elements, or seed for a
> gradient palette_
>

>
>  _ **Returns:** This method returns the Axes object with the plot drawn onto
> it._

### Approach:

  * Import the library
  * Create or load the dataset.
  * Plot a boxplot using boxplot().
  * Add data points using stripplot().
  * Display plot.

Given below are few implementations to help you understand better

  

  

**Example 1:** Regular box plot for comparison

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import seaborn as sns

import matplotlib.pyplot as plt

 

# loading seaborn dataset tips

tdata = sns.load_dataset('tips')

 

# creating boxplot

sns.boxplot(x='size', y='tip', data=tdata)

 

# display plot

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201219023227/op.png)

 **Example 2:** Creating box plot with data points

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import seaborn as sns

import matplotlib.pyplot as plt

# loading seaborn dataset tips

tdata = sns.load_dataset('tips')

 

# creating boxplot

sns.boxplot(x='size', y='tip', data=tdata)

 

# adding data points

sns.stripplot(x='size', y='tip', data=tdata)

# display plot

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201219023503/op.png)

  

  

 **Example 3:** Boxplot with data points with non-default color

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import seaborn as sns

import matplotlib.pyplot as plt

# loading seaborn dataset tips

tdata = sns.load_dataset('tips')

 

# creating boxplot

sns.boxplot(x='size', y='tip', data=tdata)

 

# adding data points

sns.stripplot(x='size', y='tip', data=tdata,
color="grey")

# display plot

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201219023838/op.png)

 **Example 4:** Changing size of the data points

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import seaborn as sns

import matplotlib.pyplot as plt

# loading seaborn dataset tips

tdata = sns.load_dataset('tips')

 

tdata = tdata.head(10)

# creating boxplot

sns.boxplot(x='size', y='tip', data=tdata)

 

# adding data points

sns.stripplot(x='size', y='tip', data=tdata,
color="grey", size=8)

# display plot

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201219024139/op.png)

 **Example 5:** Plotting transparent data points

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import seaborn as sns

import matplotlib.pyplot as plt

# loading seaborn dataset tips

tdata = sns.load_dataset('tips')

 

tdata = tdata.head(20)

# creating boxplot

sns.boxplot(x='size', y='tip', data=tdata)

 

# adding data points

sns.stripplot(x='size', y='tip', data=tdata,
color="black", size=8, alpha=0.5)

# display plot

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201219024602/op.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

