Seaborn – Bubble Plot



 **Seaborn** is an amazing visualization library for statistical graphics
plotting in Python. It provides beautiful default styles and color palettes to
make statistical plots more attractive. It is built on the top of matplotlib
library and also closely integrated to the data structures from pandas.

 **Scatter plots** are used to observe relationship between variables and uses
dots to represent the relationship between them. **Bubble plots** are scatter
plots with bubbles (color filled circles) rather than information focuses.
Bubbles have various sizes dependent on another variable in the data.
Likewise, Bubbles can be of various color dependent on another variable in the
dataset.

Let us load the required module and the simplified Iris data as a Pandas Data
frame:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import all important libraries

import matplotlib.pyplot as plt

import pandas as pd

import seaborn as sns

 

# load dataset

data=
"https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

 

# convert to dataframe

df = pd.read_csv(data)

 

# display top most rows

df.head()  
  
---  
  
 __

 __

 **Output:**

  

  

###

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201108142623/Screenshot598.png)

### Scatter plot with Seaborn:

As stated earlier than, bubble is a unique form of scatter plot with bubbles
as opposed to easy facts points in scatter plot. Let us first make a simple
scatter plot the usage of _Seaborn_ ’s _scatterplot()_ function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import all important libraries

import matplotlib.pyplot as plt

import pandas as pd

import seaborn as sns

 

# load dataset

data =
"https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

 

# convert to dataframe

df = pd.read_csv(data)

 

# display top most rows

df.head()

 

# depict scatterplot illustration

sns.set_context("talk", font_scale=1.1)

plt.figure(figsize=(8, 6))

sns.scatterplot(x="sepal.length",

 y="sepal.width",

 data=df)

 

# assign labels

plt.xlabel("Sepal.Length")

plt.ylabel("sepal.width")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201107175420/download.png)

### Bubble plot with Seaborn scatterplot():

To make bubble plot in _Seaborn_ , we are able to use _scatterplot()_ function
in _Seaborn_ with a variable specifying _size_ argument in addition to x and
y-axis variables for scatter plot.

In this bubble plot instance, we have _length= ”body_mass_g”_. And this will
create a bubble plot with unique bubble sizes based at the body length
variable.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import all important libraries

import matplotlib.pyplot as plt

import pandas as pd

import seaborn as sns

 

# load dataset

data =
"https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

 

# convert to dataframe

df = pd.read_csv(data)

 

# display top most rows

df.head()

 

# depict scatter plot illustration

sns.set_context("talk", font_scale=1.1)

plt.figure(figsize=(10, 6))

sns.scatterplot(x="petal.length",

 y="petal.width",

 data=df)

# Put the legend out of the figure

plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0)

plt.xlabel("petal.length")

plt.ylabel("petal.width")

plt.tight_layout()

plt.savefig("Bubble_plot_Seaborn_scatterplot.png",

 format='png', dpi=150)  
  
---  
  
 __

 __

