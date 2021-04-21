How To Make Stripplot with Jitter in Altair Python?



 **Prerequisites:** Altair

Altair is a statistical data visualization library in python which is based on
Vega and Vega-Lite visualization grammars. A Stripplot is used for graphical
data analysis. It is a simple plot of response values in a sorted order along
a single axis. The strip plot consists of 2 distinct axes (X, Y). The strip
plots provide an alternative for the histogram and other density-based plots
and are often used with small datasets.

A simple strip plot is used for plotting the data as points, which may not be
very useful to us. To make the simple stripplot more cultivate we add random
jitter. Jitter in simple words is adding a small amount of
variability(horizontal or vertical) to the data to ensure all data points are
visible.

###  **Approach:**

  * Import Libraries
  * Import or create data
  * Create a simple Stripplot using Altair
  * Add jitter variable to the Axis
  * Modify the values of different attributes for better visualization (optional).
  * Display plot

### Function Used

calculate_transform() allows the user to define new fields in the dataset
which are calculated from other fields using an expression.

 **Syntax:**

  

  

    
    
    calculate_transform(<some_expression>)

Various implementation using above approach is given below

 **Example 1:**

In this program, we will use the tip dataset to study the amount of money paid
as tip during Lunch time and Dinner time.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#import libraries

import seaborn

import altair as alt

 

 

# Getting data

tip = seaborn.load_dataset('tips')

 

# plotting the stripplot

stripplot = alt.Chart(tip).mark_circle(size=14).encode(

 # X-axis jitter Vertical

 x=alt.X(

 'jitter:Q',

 title=None,

 axis=alt.Axis(ticks=True, grid=False,
labels=False),

 scale=alt.Scale(),

 ),

 y=alt.Y('tip:Q',

 scale=alt.Scale()),

 color=alt.Color('time:N', legend=None),

 column=alt.Column(

 'time:N',

 ),

).transform_calculate(

 # Generate Gaussian jitter with a Box-Muller transform

 jitter='sqrt(-2*log(random()))*cos(2*PI*random())')

stripplot  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201230193049/strip1-660x282.png)

 **Example 2:**

This program deals with study of maximum temperature during different weather
conditions in the region of Seattle using stripplot.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#import libraries

import altair as alt

from vega_datasets import data

 

# Getting data

weather = data.seattle_weather()

 

# plotting the stripplot

stripplot = alt.Chart(weather).mark_circle(size=14).encode(

 x=alt.X(

 'jitter:Q',

 title=None,

 axis=alt.Axis(ticks=True, grid=False,
labels=False),

 scale=alt.Scale(),

 ),

 y=alt.Y('temp_max:Q',

 scale=alt.Scale(

 domain=(-1, 40))),

 color=alt.Color('weather:N', legend=None),

 column=alt.Column(

 'weather:N',

 header=alt.Header(

 labelFontSize=16,

 labelAngle=0,

 titleOrient='top',

 labelOrient='bottom',

 labelAlign='center',

 labelPadding=25,

 ),

 ),

).transform_calculate(

 # Generate Gaussian jitter with a Box-Muller transform

 jitter='sqrt(-2*log(random()))*cos(2*PI*random())'

).configure_facet(

 spacing=0

).configure_view(

 stroke=None

).configure_axis(

 labelFontSize=16,

 titleFontSize=16

).properties(height=400, width=100)

stripplot  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201230195123/visualization.png)

 **Example 3.**

This plotting depicts the age and gender from a given piece of data.
(Horizontal Plot)

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#import libraries

import seaborn

import altair as alt

import pandas as pd

 

# Creating our own data

data = [['Tom', 10, 'Male'], ['Nick', 25,
'Male'], ['Juli', 14, 'Female'],

 ['Sarah', 30, 'Male'], ['Pulkit', 20, 'Male'],
['Ritika', 20, 'Female'],

 ['Sayantan', 60, 'Male'], ['Pam', 39, 'Female'],
['Peter', 42, 'Male'],

 ['Jenefer', 24, 'Female'], ['Tony', 29, 'Female'],
['Myler', 22, 'Female']]

df = pd.DataFrame(data, columns=['Name', 'Age',
'Gender'])

 

# plotting the stripplot Horizontal

horizontal_stripplot = alt.Chart(df, width=600,
height=100).mark_circle(size=40).encode(

 y=alt.Y(

 'jitter:Q',

 title=None,

 axis=alt.Axis(ticks=True, grid=False,
labels=False),

 scale=alt.Scale(),

 ),

 x=alt.X('Age:Q', scale=alt.Scale()),

 color=alt.Color('Gender:N', legend=None),

 row=alt.Row(

 'Gender:N',

 header=alt.Header(

 labelAngle=0,

 labelFontSize=16,

 titleOrient='top',

 labelOrient='left',

 labelAlign='left',

 ),

 ),

).transform_calculate(

 # Generate Gaussian jitter with a Box-Muller transform

 jitter='sqrt(-2*log(random()))*cos(2*PI*random())'

).configure_facet(

 spacing=0

).configure_view(

 stroke=None

).configure_axis(

 labelFontSize=16,

 titleFontSize=16

)

horizontal_stripplot  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201230201622/visualization1.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

