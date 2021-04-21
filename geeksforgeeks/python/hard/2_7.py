Align columns to Left in Pandas – Python



Pandas library is useful for performing exploratory data analysis in Python. A
pandas dataframe represents data in a tabular format. We can perform
operations on the data and display it. In this article, we are going to align
columns to the Left in Pandas. When we display the dataframe, we can align the
data in the columns as left, right, or center.

**The default is right alignment as we can see in the below example.**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code demonstrate creating

# DataFrame from dict and left aligning

import pandas as pd 

 

# intialise data of lists. 

data = {'Name' : ['Tania', 'Ravi', 

 'Surbhi', 'Ganesh'], 

 

 'Articles' : [50, 30, 45, 33], 

 

 'Location' : ['Kanpur', 'Kolkata',

 'Kolkata', 'Bombay']} 

 

# Create DataFrame 

df = pd.DataFrame(data) 

display(df)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201222152522/gfg1py-300x164.png)

  

  

In order to align columns to left in pandas dataframe, we use the
**dataframe.style.set_properties()** function.

>  **Syntax:** Styler.set_properties( _subset=None_ , _**kwargs_ )
>
>  **Parameters:**
>
>   *  **subsetIndexSlice:** A valid slice for data to limit the style
> application to.
>   *  ****kwargsdict:** A dictionary of property, value pairs to be set for
> each cell.
>

>
>  **Returns:** selfStyler

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

# DataFrame from dict and left aligning

import pandas as pd 

 

# intialise data of lists. 

data = {'Name' : ['Tania', 'Ravi', 

 'Surbhi', 'Ganesh'], 

 

 'Articles' : [50, 30, 45, 33], 

 

 'Location' : ['Kanpur', 'Kolkata',

 'Kolkata', 'Bombay']} 

 

# Create DataFrame 

df = pd.DataFrame(data) 

 

left_aligned_df = df.style.set_properties(**{'text-align':
'left'})

display(left_aligned_df)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201226182300/Capture.JPG)

  

  

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd 

 

# intialise data of lists. 

data = [['Raghav', 'Jeeva', 'Imon', 'Sandeep'], 

 ['Deloitte', 'Apple', 'Amazon', 'Flipkart'], 

 [2,3,7,8]]

 

# Create DataFrame 

df = pd.DataFrame(data) 

left_aligned_df = df.style.set_properties(**{'text-align':
'left'})

display(left_aligned_df)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201226182316/Capture1.JPG)

In the above example, the content of all columns are left-aligned, except the
column headers. The column headers are center-aligned.

 **Example 3:**

If we want the column headers aligned left, we use the **set_table_styles()
function**.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd 

 

# intialise data of lists. 

data = [['Raghav', 'Jeeva', 'Imon', 'Sandeep'],

 ['Deloitte', 'Apple', 'Amazon', 'Flipkart'],

 [2,3,7,8]]

 

# Create DataFrame 

df = pd.DataFrame(data) 

left_aligned_df = df.style.set_properties(**{'text-align':
'left'})

 

left_aligned_df = left_aligned_df.set_table_styles(

[dict(selector = 'th', props=[('text-align',
'left')])])

 

display(left_aligned_df)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201226182316/Capture2.JPG)

In the above example, both the column headers and the content of all the
columns are left-aligned.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

