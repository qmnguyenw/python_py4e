Data Visualization with Python Seaborn and Pandas



Data Visualization is the presentation of data in pictorial format. It is
extremely important for Data Analysis, primarily because of the fantastic
ecosystem of data-centric Python packages. And it helps to understand the
data, however, complex it is, the significance of data by summarizing and
presenting a huge amount of data in a simple and easy-to-understand format and
helps communicate information clearly and effectively.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201128221945/Capture3-660x176.PNG)

 **Pandas and Seaborn** is one of those packages and makes importing and
analyzing data much easier. In this article, we will use Pandas and Seaborn to
analyze data.

##  **Pandas**

 **Pandas** offer tools for cleaning and process your data. It is the most
popular Python library that is used for data analysis. In pandas, a data table
is called a dataframe.

 **So, let’s start with creating Pandas data frame:**

  

  

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code demonstrate creating

 

import pandas as pd

 

# intialise data of lists.

data = {'Name':[ 'Mohe' , 'Karnal' , 'Yrik' , 'jack'
],

 'Age':[ 30 , 21 , 29 , 28 ]}

 

# Create DataFrame

df = pd.DataFrame( data )

 

# Print the output.

df  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201124203529/Capture.PNG)

 **Example 2:** load the CSV data from the system and display it through
pandas.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import pandas

 

# load the csv

data = pandas.read_csv("nba.csv")

 

# show first 5 column

data.head()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201125173250/Capture-660x169.PNG)

  

  

##  **Seaborn**

Seaborn is an amazing visualization library for statistical graphics plotting
in Python. It is built on the top of matplotlib library and also closely
integrated into the data structures from pandas.

 **Installation**

For python environment :

    
    
    pip install seaborn

For conda environment :

    
    
    conda install seaborn

 **Let’s create Some basic plots using seaborn:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing libraries

import numpy as np 

import seaborn as sns 

 

 

# Selecting style as white, 

# dark, whitegrid, darkgrid 

# or ticks 

sns.set( style = "white" ) 

 

# Generate a random univariate 

# dataset 

rs = np.random.RandomState( 10 ) 

d = rs.normal( size = 50 ) 

 

# Plot a simple histogram and kde 

# with binsize determined automatically 

sns.distplot(d, kde = True, color = "g")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201125093359/Capture.PNG)

## Seaborn: statistical data visualization

Seaborn helps to visualize the statistical relationships, To understand how
variables in a dataset are related to one another and how that relationship is
dependent on other variables, we perform statistical analysis. This
Statistical analysis helps to visualize the trends and identify various
patterns in the dataset.

These are the plot will help to visualize:

  * Line Plot
  * Scatter Plot
  * Box plot
  * Point plot
  * Count plot
  * Violin plot
  * Swarm plot
  * Bar plot
  * KDE Plot

### Line plot:

Lineplot Is the most popular plot to draw a relationship between x and y with
the possibility of several semantic groupings.

>  _ **Syntax :** sns.lineplot(x=None, y=None)_
>
>  _ **Parameters:**_
>
>  _ **x, y:** Input data variables; must be numeric. Can pass data directly
> or reference columns in data._

 **Let’s visualize the data with a line plot and pandas:**

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn as sns

import pandas

 

# loading csv

data = pandas.read_csv("nba.csv")

 

# ploting lineplot

sns.lineplot( data['Age'], data['Weight'])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201125171251/Capture.PNG)

 **Example 2:** Use the hue parameter for plotting the graph.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn as sns

import pandas

 

# read the csv data

data = pandas.read_csv("nba.csv")

 

# plot

sns.lineplot(data['Age'],data['Weight'], hue
=data["Position"])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201125172732/Capture.PNG)

### Scatter Plot:

Scatterplot Can be used with several semantic groupings which can help to
understand well in a graph against continuous/categorical data. It can draw a
two-dimensional graph.

>  _ **Syntax:** seaborn.scatterplot(x=None, y=None)_
>
>  _ **Parameters:**_  
>  _ **x, y:** Input data variables that should be numeric._
>
>  _ **Returns:** This method returns the Axes object with the plot drawn onto
> it._

 **Let’s visualize the data with a scatter plot and pandas:**

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn

import pandas

 

# load csv

data = pandas.read_csv("nba.csv")

 

# plotting

seaborn.scatterplot(data['Age'],data['Weight'])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201125175705/Capture.PNG)

 **Example 2:** Use the hue parameter for plotting the graph.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import seaborn

import pandas

data = pandas.read_csv("nba.csv")

 

seaborn.scatterplot( data['Age'], data['Weight'], hue
=data["Position"])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201125175816/Capture.PNG)

### Box plot:

A box plot (or box-and-whisker plot) s is the visual representation of the
depicting groups of numerical data through their quartiles against
continuous/categorical data.

A box plot consists of 5 things.

  * Minimum
  * First Quartile or 25%
  * Median (Second Quartile) or 50%
  * Third Quartile or 75%
  * Maximum

>  **Syntax:**
>
> seaborn.boxplot(x=None, y=None, hue=None, data=None)
>
>  **Parameters:**
>
>   * **x, y, hue:** Inputs for plotting long-form data.
>   *  **data:** Dataset for plotting. If x and y are absent, this is
> interpreted as wide-form.
>

>
>  **Returns:** It returns the Axes object with the plot drawn onto it.

**Draw the box plot with Pandas:**

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn as sns

import pandas

 

# read csv and ploting

data = pandas.read_csv( "nba.csv" )

sns.boxplot( data['Age'] )  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126165053/Capture.PNG)

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn as sns

import pandas

 

# read csv and ploting

data = pandas.read_csv( "nba.csv" )

sns.boxplot( data['Age'], data['Weight'])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126164904/Capture.PNG)

### Voilin Plot:

A voilin plot is similar to a boxplot. It shows several quantitative data
across one or more categorical variables such that those distributions can be
compared.

> _**Syntax:** seaborn.violinplot(x=None, y=None, hue=None, data=None)_
>
>  _ **Parameters:** _
>
>   * _**x, y, hue:** Inputs for plotting long-form data. _
>   * _**data:** Dataset for plotting. _  
>
>

**Draw the violin plot with Pandas:**

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn as sns

import pandas

 

# read csv and plot

data = pandas.read_csv("nba.csv")

sns.violinplot(data['Age'])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126170017/Capture.PNG)

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn 

 

seaborn.set(style = 'whitegrid') 

 

# read csv and plot

data = pandas.read_csv("nba.csv")

seaborn.violinplot(x ="Age", y ="Weight",data = data)   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126170406/Capture.PNG)

### Swarm plot:

A swarm plot is similar to a strip plot, We can draw a swarm plot with non-
overlapping points against categorical data.

>  _ **Syntax:** seaborn.swarmplot(x=None, y=None, hue=None, data=None)_  
>  __
>
> _**Parameters:** _
>
>   * _**x, y, hue:** Inputs for plotting long-form data. _
>   * _**data:** Dataset for plotting. _  
> __
>

**Draw the swarm plot with Pandas:**

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn 

 

seaborn.set(style = 'whitegrid') 

 

# read csv and plot

data = pandas.read_csv( "nba.csv" )

seaborn.swarmplot(x = data["Age"])   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126170953/Capture.PNG)

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn 

 

seaborn.set(style = 'whitegrid') 

 

# read csv and plot

data = pandas.read_csv("nba.csv")

seaborn.swarmplot(x ="Age", y ="Weight",data = data)   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126170731/Capture.PNG)

### Bar plot:

Barplot represents an estimate of central tendency for a numeric variable with
the height of each rectangle and provides some indication of the uncertainty
around that estimate using error bars.

> **Syntax :** seaborn.barplot(x=None, y=None, hue=None, data=None)
>
>  **Parameters :**
>
>   *  **x, y :** This parameter take names of variables in data or vector
> data, Inputs for plotting long-form data.
>   *  **hue :** (optional) This parameter take column name for colour
> encoding.
>   *  **data :** (optional) This parameter take DataFrame, array, or list of
> arrays, Dataset for plotting. If x and y are absent, this is interpreted as
> wide-form. Otherwise it is expected to be long-form.
>

>
>  **Returns :** Returns the Axes object with the plot drawn onto it.

**Draw the bar plot with Pandas:**

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn 

 

seaborn.set(style = 'whitegrid') 

 

# read csv and plot

data = pandas.read_csv("nba.csv")

seaborn.barplot(x =data["Age"])   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126171436/Capture.PNG)

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn 

 

seaborn.set(style = 'whitegrid') 

 

# read csv and plot

data = pandas.read_csv("nba.csv")

seaborn.barplot(x ="Age", y ="Weight", data = data)   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126171743/Capture.PNG)

###  **Point plot:**

 **Point plot** used to show point estimates and confidence intervals using
scatter plot glyphs. A point plot represents an estimate of central tendency
for a numeric variable by the position of scatter plot points and provides
some indication of the uncertainty around that estimate using error bars.

>  _ **Syntax:** seaborn.pointplot(x=None, y=None, hue=None, data=None)_
>
>  _ **Parameters:**_
>
>   *  _ **x, y:** Inputs for plotting long-form data._
>   *  _ **hue:** (optional) column name for color encoding._
>   *  _ **data:** dataframe as a Dataset for plotting._
>

>
>  _ **Return:** The Axes object with the plot drawn onto it._

 **Draw the point plot with Pandas:**

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn 

 

seaborn.set(style = 'whitegrid') 

 

# read csv and plot

data = pandas.read_csv("nba.csv")

seaborn.pointplot(x = "Age", y = "Weight", data = data)   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201128195200/Capture.PNG)

### Count plot:

Count plot used to Show the counts of observations in each categorical bin
using bars.

>  _ **Syntax :** seaborn.countplot(x=None, y=None, hue=None, data=None)_
>
>  _ **Parameters :**_
>
>   *  _ **x, y:** This parameter take names of variables in data or vector
> data, optional, Inputs for plotting long-form data._
>   *  _ **hue :** (optional) This parameter take column name for color
> encoding._
>   *  _ **data :** (optional) This parameter take DataFrame, array, or list
> of arrays, Dataset for plotting. If x and y are absent, this is interpreted
> as wide-form. Otherwise, it is expected to be long-form._
>

>
>  _ **Returns:** Returns the Axes object with the plot drawn onto it._  
>

**Draw the count plot with Pandas:**

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn 

 

seaborn.set(style = 'whitegrid') 

 

# read csv and plot

data = pandas.read_csv("nba.csv")

seaborn.countplot(data["Age"])   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201128195305/Capture.PNG)

### KDE Plot:

KDE Plot described as **Kernel Density Estimate** is used for visualizing the
Probability Density of a continuous variable. It depicts the probability
density at different values in a continuous variable. We can also plot a
single graph for multiple samples which helps in more efficient data
visualization.

>  **Syntax:** seaborn.kdeplot(x=None, *, y=None, vertical=False,
> palette=None, **kwargs)
>
>  **Parameters:**
>
>  **x, y :** vectors or keys in data
>
>  **vertical :** boolean (True or False)
>
>  **data :** pandas.DataFrame, numpy.ndarray, mapping, or sequence

 **Draw the KDE plot with Pandas:**

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the required libraries

from sklearn import datasets 

import pandas as pd 

import seaborn as sns 

 

# Setting up the Data Frame 

iris = datasets.load_iris() 

 

iris_df = pd.DataFrame(iris.data, columns=['Sepal_Length', 

 'Sepal_Width', 'Patal_Length', 'Petal_Width']) 

 

iris_df['Target'] = iris.target 

 

iris_df['Target'].replace([0], 'Iris_Setosa', inplace=True)


iris_df['Target'].replace([1], 'Iris_Vercicolor',
inplace=True) 

iris_df['Target'].replace([2], 'Iris_Virginica',
inplace=True) 

 

# Plotting the KDE Plot 

sns.kdeplot(iris_df.loc[(iris_df['Target'] =='Iris_Virginica'), 

 'Sepal_Length'], color = 'b', shade = True, Label
='Iris_Virginica')   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126182437/Capture.PNG)

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn as sns

import pandas

 

# read top 5 column

data = pandas.read_csv("nba.csv").head()

 

sns.kdeplot( data['Age'], data['Number'])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126182845/Capture.PNG)

### Bivariate and Univariate data using seaborn and pandas:

Before starting let’s have a small intro of bivariate and univariate data:

 **Bivariate data:** This type of data involves **two different variables**.
The analysis of this type of data deals with causes and relationships and the
analysis is done to find out the relationship between the two variables.

 **Univariate data:** This type of data consists of **only one variable**. The
analysis of univariate data is thus the simplest form of analysis since the
information deals with only one quantity that changes. It does not deal with
causes or relationships and the main purpose of the analysis is to describe
the data and find patterns that exist within it.

#### Let’s see an example of **Bivariate data disturbation:**

 **Example 1:** Using the box plot.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn as sns

import pandas

 

# read csv and ploting

data = pandas.read_csv( "nba.csv" )

sns.boxplot( data['Age'], data['Height'])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201128215352/Capture.PNG)

 **Example 2:** using KDE plot.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn as sns

import pandas

 

# read top 5 column

data = pandas.read_csv("nba.csv").head()

 

sns.kdeplot( data['Age'], data['Weight'])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201128215619/Capture.PNG)

#### Let’s see an example of uni **variate data distribution:**

 **Example:** Using the dist plot

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import seaborn as sns

import pandas

 

# read top 5 column

data = pandas.read_csv("nba.csv").head()

 

sns.distplot( data['Age'])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201128215943/Capture.PNG)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

