Seaborn – Coloring Boxplots with Palettes



Adding the right set of color with your data visualization makes it more
impressive and readable, _seaborn_ color palettes make it easy to use colors
with your visualization. In this article, we will see how to color _boxplot_
with _seaborn_ color palettes also learn the uses of _seaborn_ color palettes
and it can be applied to other plots as well.

**Step-by-step Approach:**

 **Step 1:** Load the python packages and libraries required to color a
_boxplot_.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import libraries

import seaborn as sns 

import matplotlib.pyplot as plt  
  
---  
  
 __

 __

  

  

 **Step 2:** Load the dataset to generate a _boxplot_.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# loading dataset

ds = sns.load_dataset('iris')  
  
---  
  
 __

 __

 **Step 3:** Generate a _boxplot_ using the _boxplot()_ method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# create boxplot object

ax = sns.boxplot(data=tips, orient="h")  
  
---  
  
 __

 __

 **Step 4:** _Seaborn_ _boxplot()_ function has palette argument, in this
example we have set _palette=”Set1″,_ it uses a qualitative color _paletter
Set3_ to color the boxes in _boxpolot_. So add palette parameter in _boxplot_
method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# use palette method

ax = sns.boxplot(data=ds, orient="h", palette="Set1")  
  
---  
  
 __

 __

 **Below is the complete program based on the above approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import libraries

import seaborn as sns

import matplotlib.pyplot as plt

 

# load datset

ds = sns.load_dataset("tips")

 

plt.figure(figsize=(8, 6))

 

# use palette method

ax = sns.boxplot(data=ds, orient="h", palette="Set1")  
  
---  
  
 __

 __

#### Output:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201031194614/pallete.png)

Coloring Boxplots with Seaborn Palettes

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

