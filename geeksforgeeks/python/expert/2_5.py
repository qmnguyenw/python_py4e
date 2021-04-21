Change marker border color in Plotly – Python



In this article, we are going to discuss how to change marker border color
using _plotly_ module in Python.

 _Plotly_ is definitely a must-know tool for visualization since it’s
incredibly powerful easily used and has the big benefit of interactivity we
are able to export visualization, being able to run on browsers, build with
DASH which is web-based python interface which removes the need of javascript
in this type of analytical web applications, and we can also run these plot
offline as well. In this article we will use the module of _plotly_ which is
_plotly.express_ , it is the high-level python visualization library, it
exposes simple syntax to complex charts it is the wrapper for plotly.py.

 **Installation:**

This module can be installed using the below command:

    
    
    pip install plotly

In this article, we are going to change the maker border color with the help
of _plotly.express.scatter.update_traces()_ and
_plotly.express.scatter_3d.update_traces()()_ methods.

  

  

 **Step-by-step Approach:**

  * Import the _plotly_ and _pandas_ library.
  * First, we have to load the dataset on which we are plotting our graph with the help of the _pandas_ library.
  * For plotting the graph we will use _plotly.scatter()_ for scatter plot and put it in the variable let name as _fig_
  * Then we use _fig.update_traces_ function which is having marker property from which we can change the borders of the marker.

We are going to use the below _iris_ dataset in various examples:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import plotly.express as px

 

# importing iris dataset from plotly

df = px.data.iris()

 

# display dataset

df  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201216222018/Screenshot195.png)

 **Example 1:** Plotting default scatter plot on _iris_ dataset.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import plotly.express as px

 

# importing iris dataset from plotly

df = px.data.iris()

 

# plotting the scatter plot on sepal_width 

# and sepal_length and giving color with 

# respect to species

fig = px.scatter(df, x='sepal_width', 

 y='sepal_length', 

 color='species')

 

# showing the plot with default settings

fig.show()  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201214002124/default.png)

Plotting scatter plot on iris dataset and changing marker border color.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import plotly.express as px

 

# importing iris dataset from plotly

df = px.data.iris()

 

# plotting the scatter plot on sepal_width

# and sepal_length and giving color 

# with respect to species

fig = px.scatter(df, x='sepal_width', 

 y='sepal_length', 

 color='species')

 

# setting up marker and in line 

# Attribute giving the width and color of border

fig.update_traces(marker=dict(size=10, 

 line=dict(width=3,

 color='blue')))

 

# showing the plot with default settings

fig.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201214004452/color.png)

In the above code, we had used _update_traces()_ function in that we had given
marker attribute for creating the borders in that attribute we had passed the
dictionary in which we had passes size=10 for giving the size to the circles,
whereas in line we had passed the dictionary in which we had passes width and
color, width refers to the width of the border and color refers to the color
of the border.

 **Example 3:** Plotting default _scatter_3d_ plot on _iris_ dataset.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import plotly.express as px

 

# importing iris dataset from plotly

df = px.data.iris()

 

# plotting the scatter 3d plot by giving 

# three axis, petal length, petal width 

# and sepal length 

# giving color with respect to species

fig = px.scatter_3d(df,x='petal_length',

 y='petal_width',

 z='sepal_length',

 color='species')

 

# showing the plot with default settings

fig.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201214010838/Figure1.png)

 **Example 4:** Plotting scatter_3d plot on iris dataset with marker border
color.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing library

import plotly.express as px

 

# importing iris dataset from plotly

df = px.data.iris()

 

# plotting the scatter_3d plot by 

# giving three axis on petal_length, 

# petal_width and sepal_length 

# and giving color with respect to species

fig = px.scatter_3d(df,x='petal_length',

 y='petal_width',

 z='sepal_length',

 color='species')

 

# setting up marker and in line Attribute 

# giving the width and color of border

fig.update_traces(marker=dict(size=10,

 line=dict(width=10,

 color='red')))

 

# showing the plot 

fig.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201214011739/Figure1.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

