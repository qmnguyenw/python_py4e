How to randomly select rows from Pandas DataFrame



Let’s discuss how to randomly select rows from Pandas DataFrame. A random
selection of rows from a DataFrame can be achieved in different ways.

Create a simple dataframe with dictionary of lists.

 __

 __  
 __

 __

 __  
 __  
 __

# Import pandas package

import pandas as pd

 

# Define a dictionary containing employee data

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj',
'Geeku'],

 'Age':[27, 24, 22, 32, 15],

 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj',
'Noida'],

 'Qualification':['Msc', 'MA', 'MCA', 'Phd',
'10th']}

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data)

 

# select all columns

df  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/random_dataframe1.png)

 **Mathod #1:** **Usingsample() method**

> Sample method returns a random sample of items from an axis of object and
> this object of same type as your caller.
>
>  
>
>
>  
>

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Selects one row randomaly using sample()

# without give any parameters.

 

# Import pandas package

import pandas as pd

 

# Define a dictionary containing employee data

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj',
'Geeku'],

 'Age':[27, 24, 22, 32, 15],

 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj',
'Noida'],

 'Qualification':['Msc', 'MA', 'MCA', 'Phd',
'10th']}

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data)

 

# Select one row randomaly using sample()

# without give any parameters

df.sample()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/random_dataframe2.png)

 **Example 2:** Using parameter _n_ , which selects _n_ numbers of rows
randomly.

Select _n_ numbers of rows randomly using sample(n) or sample(n=n). Each
time you run this, you get n different rows.

 __

 __  
 __

 __

 __  
 __  
 __

# To get 3 random rows

# each time it gives 3 different rows

 

# df.sample(3) or

df.sample(n = 3)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/random_dataframe3.png)

 **Example 3:** Using frac parameter.

One can do fraction of axis items and get rows. For example, if frac= .5
then sample method return 50% of rows.

 __

 __  
 __

 __

 __  
 __  
 __

# Fraction of rows

 

# here you get .50 % of the rows

df.sample(frac = 0.5)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/random_dataframe4.png)

  

  

 **Example 4:**  
First selects 70% rows of whole _df_ dataframe and put in another dataframe
_df1_ after that we select 50% frac from _df1_.

 __

 __  
 __

 __

 __  
 __  
 __

# fraction of rows

 

# here you get 70 % row from the df

# make put into another dataframe df1

df1 = df.sample(frac =.7)

 

# Now select 50 % rows from df1

df1.sample(frac =.50)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/random_dataframe5.png)

 **Example 5:** Select some rows randomly with replace = false

Parameter _replace_ give permission to select one rows many time(like).
Default value of replace parameter of sample() method is False so you never
select more than total number of rows.

 __

 __  
 __

 __

 __  
 __  
 __

# Dataframe df has only 4 rows

 

# if we try to select more than 4 row then will come error 

# Cannot take a larger sample than population when 'replace = False'

df1.sample(n = 3, replace = False)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/random_dataframe6.png)

 **Example 6:** Select more than _n_ rows where _n_ is total number of rows
with the help of replace.

 __

 __  
 __

 __

 __  
 __  
 __

# Select more than rows with using replace

# default it is False 

df1.sample(n = 6, replace = True)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/random_dataframe7.png)

 **Example 7:** Using weights

 __

 __  
 __

 __

 __  
 __  
 __

# Weights will be re-normalized automatically

test_weights = [0.2, 0.2, 0.2, 0.4]

 

df1.sample(n = 3, weights = test_weights)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/random_dataframe8.png)

 **Example 8:** Using axis

The axis accepts number or name. sample() method also allows users to sample
columns instead of rows using the axis argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Accepts axis number or name.

 

# sample also allows users to sample columns

# instead of rows using the axis argument.

df1.sample(axis = 0)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/random_dataframe9.png)

 **Example 9:** Using random_state

With a given DataFrame, the sample will always fetch same rows. If
random_state is None or np.random, then a randomly-initialized RandomState
object is returned.

 __

 __  
 __

 __

 __  
 __  
 __

# With a given seed, the sample will always draw the same rows.

 

# If random_state is None or np.random,

# then a randomly-initialized

# RandomState object is returned.

df1.sample(n = 2, random_state = 2)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/random_dataframe10.png)  
  
**Method #2:** **Using NumPy**

Numpy chose how many index include for random selection and we can allow
replacement.

 __

 __  
 __

 __

 __  
 __  
 __

# Import pandas& Numpy package

import numpy as np

import pandas as pd

 

# Define a dictionary containing employee data

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj',
'Geeku'],

 'Age':[27, 24, 22, 32, 15],

 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj',
'Noida'],

 'Qualification':['Msc', 'MA', 'MCA', 'Phd',
'10th']}

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data)

 

# Chose how many index include for random selection

chosen_idx = np.random.choice(4, replace = True, size =
6)

 

df2 = df.iloc[chosen_idx]

 

df2  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/random_dataframe11.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

