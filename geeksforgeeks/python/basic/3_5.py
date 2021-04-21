Replacing missing values using Pandas in Python



Dataset is a collection of attributes and rows. Data set can have missing data
that are represented by NA in Python and in this article, we are going to
replace missing values in this article

We consider this data set: Dataset

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201030092137/1-300x154.PNG)

data set

In our data contains missing values in quantity, price, bought, forenoon and
afternoon columns,

So, We can replace missing values in the quantity column with mean, price
column with a median, Bought column with standard deviation. Forenoon column
with the minimum value in that column. Afternoon column with maximum value in
that column.

 **Approach:**

  

  

  * Import the module
  * Load data set
  * Fill in the missing values
  * Verify data set

 **Syntax:**

>  **Mean:** data=data.fillna(data.mean())
>
>  **Median:** data=data.fillna(data.median())
>
>  **Standard Deviation:** data=data.fillna(data.std())
>
>  **Min:** data=data.fillna(data.min())
>
>  **Max:** data=data.fillna(data.max())

Below is the Implementation:

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd

 

# loading data set

data = pd.read_csv('item.csv')

 

# display the data

print(data)  
  
---  
  
 __

 __

