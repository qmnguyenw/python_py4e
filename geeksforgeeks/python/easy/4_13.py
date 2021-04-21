Set Pandas dataframe background Color and font color in Python



As we know, the basic idea behind styling is to make more impactful for the
end-user readability. We can make changes like the color and format of the
data visualized in order to communicate insight more efficiently. For the more
impactful visualization on the pandas DataFrame, generally, we DataFrame.style
property, which returns styler object having a number of useful methods for
formatting and visualizing the data frames.

##  **Using DataFrame.style property**

  *  **df.style.set_properties :** By using this, we can use inbuilt functionality to manipulate data frame styling from font color to background color.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing the necessary libraries -->

import pandas as pd

import numpy as np

 

# Seeding random data from numpy

np.random.seed(24)

 

# Making the DatFrame

df = pd.DataFrame({'A': np.linspace(1, 10, 10)})

df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), 

 columns=list('BCDE'))], axis=1)

 

# DataFrame without any styling

print("Original DataFrame:\n")

print(df)

print("\nModified Stlying DataFrame:")

df.style.set_properties(**{'background-color': 'black',

 'color': 'green'})  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200729122720/style1.png)

 **df.style.set_properties**

  *  **df.style.highlight_null :** With the help of this, we can highlight the missing or null values inside the data frame.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Replacing the locating value by NaN (Not a Nummber)

df.iloc[0, 3] = np.nan

df.iloc[2, 3] = np.nan

df.iloc[4, 2] = np.nan

df.iloc[7, 4] = np.nan

 

# Highlight the NaN values in DataFrame

print("\nModified Stlying DataFrame:")

df.style.highlight_null(null_color='red')  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200729125227/style2.png)

 **df.style.highlight_null**

  *  **df.style.highlight_min :** For highlighting the minimum value in each column throughout the data frame.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Highlight the Min values in each column

print("\nModified Stlying DataFrame:")

df.style.highlight_min(axis=0)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200729125923/style3.png)

 **df.style.highlight_min**

  *  **df.style.highlight_max :** For highlighting the maximum value in each column throughout the data frame.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Highlight the Max values in each column

print("\nModified Stlying DataFrame:")

df.style.highlight_max(axis=0)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200729130054/style4.png)

 **df.style.highlight_max**

## Using User-defined Function

  *  **We can modify DataFrame using a user-defined function:** With the help of this function, we can customizing the font color of positive data values inside the data frame.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function for set text color of positive

# values in Dataframes

def color_positive_green(val):

 """

 Takes a scalar and returns a string with

 the css property 'color: green' for positive

 strings, black otherwise.

 """

 if val > 0:

 color = 'green'

 else:

 color = 'black'

 return 'color: %s' % color

 

df.style.applymap(color_positive_green)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200729130745/style5.png)

 **User-Defined Function**

## Using Seaborn Library

  *  **Using color palette for gradient fill in DataFrame:** By importing the light palette of colors from the seaborn library, we can map the color gradient for the background of the data frame.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import seaborn library

import seaborn as sns

 

# Declaring the cm variable by the 

# color palette from seaborn

cm = sns.light_palette("green", as_cmap=True)

 

# Visualizing the DataFrame with set precision

print("\nModified Stlying DataFrame:")

df.style.background_gradient(cmap=cm).set_precision(2)  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200729130918/style6.png)

 **Seaborn Color Palette**

  *  **Using color palette with highlight null or missing values:** Here, we highlight the NaN values in red color with gradient color palette of seaborn.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Highlight the NaN values in DataFrame

# using seaborn color palette

print("\nModified Stlying DataFrame:")

df.style.background_gradient(cmap=cm).set_precision(2).highlight_null('red')  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200729131038/style7.png)

 **Seaborn Color Palette with highlight_null**

  *  **Assemble Seaborn properties with DataFrame.style property:** Customizing the seaborn color palette with highlight properties of a data frame for more impactful data visualization.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Highlight the NaN values in DataFrame

# using seaborn color palette as well as

# min('lighblue') and max('blue') values 

# in each column

print("\nModified Stlying DataFrame:")

df.style.background_gradient(cmap=cm).set_precision(2).highlight_null('red').highlight_min(axis=0,
color='lightblue').highlight_max(axis=0, color='blue')  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200729131233/style8.png)

 **Seaborn Color Palette with diff. highlight properties**

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

