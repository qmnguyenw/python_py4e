Box plot visualization with Pandas and Seaborn



 _ **Box Plot**_ is the visual representation of the depicting groups of
numerical data through their quartiles. Boxplot is also used for detect the
outlier in data set. It captures the summary of the data efficiently with a
simple box and whiskers and allows us to compare easily across groups. Boxplot
summarizes a sample data using 25th, 50th and 75th percentiles. These
percentiles are also known as the lower quartile, median and upper quartile.

A box plot consist of 5 things.

  * Minimum
  * First Quartile or 25%
  * Median (Second Quartile) or 50%
  * Third Quartile or 75%
  * Maximum

To download the dataset used, click here.

 **Draw the box plot with Pandas:**

One way to plot boxplot using pandas dataframe is to use boxplot() function
that is part of pandas library.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import the required library

import numpy as np 

import pandas as pd 

import matplotlib.pyplot as plt 

% matplotlib inline

 

 

# load the dataset

df = pd.read_csv("tips.csv")

 

# display 5 rows of dataset

df.head()   
  
---  
  
__

__

![](https://media.geeksforgeeks.org/wp-content/uploads/123-7.png)

Boxplot ofdays with respect total_bill.

 __

 __  
 __

 __

 __  
 __  
 __

df.boxplot(by='day', column =['total_bill'], grid =
False)  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/124-2-300x203.png)  
  
Boxplot of size with respect tip.

 __

 __  
 __

 __

 __  
 __  
 __

df.boxplot(by='size', column =['tip'], grid = False)  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/125-3-300x223.png)  
  
**Draw the boxplot using seaborn library:**

>  **Syntax :**  
> seaborn.boxplot(x=None, y=None, hue=None, data=None, order=None,
> hue_order=None, orient=None, color=None, palette=None, saturation=0.75,
> width=0.8, dodge=True, fliersize=5, linewidth=None, whis=1.5, notch=False,
> ax=None, **kwargs)
>
>  **Parameters:**  
>  **x =** feature of dataset  
>  **y =** feature of dataset  
>  **hue =** feature of dataset  
>  **data =** datafram or full dataset  
>  **color =** color name

Let’s see how to create the box plot through seaborn library.

Information about “tips” dataset.

 __

 __  
 __

 __

 __  
 __  
 __

# load the dataset

tips = sns.load_dataset('tips')

 

tips.head()  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/data-3-300x136.png)

Boxplot ofdays with respect total_bill.

 __

 __  
 __

 __

 __  
 __  
 __

# Draw a vertical boxplot grouped

# by a categorical variable:

sns.set_style("whitegrid")

 

sns.boxplot(x = 'day', y = 'total_bill', data = tips)  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/box-plot-300x196.png)

Let’s take the first box plot i.e, _blue box plot_ of the figure and
understand these statistical things:

  *  _Bottom black_ horizontal line of blue box plot is minimum value
  *  _First black_ horizontal line of rectangle shape of blue box plot is First quartile or 25%
  *  _Second black_ horizontal line of rectangle shape of blue box plot is Second quartile or 50% or median.
  *  _Third black_ horizontal line of rectangle shape of blue box plot is third quartile or 75%
  *  _Top black_ horizontal line of rectangle shape of blue box plot is maximum value.
  *  _Small diamond shape_ of blue box plot is outlier data or erroneous data.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

