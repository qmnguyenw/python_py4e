How to select multiple columns in a pandas dataframe



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric Python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Let’s discuss all different ways of selecting multiple columns in a pandas
DataFrame.

 **Method #1:** Basic Method

Given a dictionary which contains Employee entity as keys and list of those
entity as values.

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

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],

 'Age':[27, 24, 22, 32],

 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],

 'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data)

 

# select two columns

df[['Name', 'Qualification']]  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/df_col1.png)

  

  

Select Second to fourth column.

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

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],

 'Age':[27, 24, 22, 32],

 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],

 'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data)

 

# select all rows 

# and second to fourth column

df[df.columns[1:4]]  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/df_col12.png)

**Method #2:** Using loc[]

 **Example 1:** Select two columns

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

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],

 'Age':[27, 24, 22, 32],

 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],

 'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data)

 

# select three rows and two columns

df.loc[1:3, ['Name', 'Qualification']]  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/df_col3.png)

 **Example 2:** Select one to another columns. In our case we select column
name “Name” to “Address”.

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

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],

 'Age':[27, 24, 22, 32],

 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],

 'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data)

 

# select two rows and 

# column "name" to "Address"

# Means total three columns

df.loc[0:1, 'Name':'Address']  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/df_col4.png)

  

  

 **Example 3:** First filtering rows and selecting columns by label format and
then Select all columns.

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

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],

 'Age':[27, 24, 22, 32],

 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],

 'Qualification':['Msc', 'MA', 'MCA', 'Phd']

 }

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data)

 

# .loc DataFrame method

# filtering rows and selecting columns by label

# format

# df.loc[rows, columns]

# row 1, all columns

df.loc[0, :]  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/df_col5.png)

**Method #3:** Using iloc[]

 **Example 1:** Select first two column.

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

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],

 'Age':[27, 24, 22, 32],

 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],

 'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data)

 

# Remember that Python does not

# slice inclusive of the ending index.

# select all rows 

# select first two column

df.iloc[:, 0:2]   
  
---  
  
__

__

**Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/df_col6.png)

 **Example 2:** Select all or some columns, one to another using .iloc.

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

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],

 'Age':[27, 24, 22, 32],

 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],

 'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data)

 

# iloc[row slicing, column slicing]

df.iloc [0:2, 1:3]  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/df_col7.png)

**Method #4:** Using .ix

Select all or some columns, one to another using .ix.

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

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],

 'Age':[27, 24, 22, 32],

 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],

 'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data)

 

# select all rows and 0 to 2 columns 

print(df.ix[:, 0:2])  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/df_col8.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

