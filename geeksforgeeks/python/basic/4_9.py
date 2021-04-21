Concatenate strings from several rows using Pandas groupby



Pandas **Dataframe.groupby()** method is used to split the data into groups
based on some criteria. The abstract definition of grouping is to provide a
mapping of labels to the group name.

To concatenate string from several rows using **Dataframe.groupby()** ,
perform the following steps:

  1. Group the data using Dataframe.groupby() method whose attributes you need to concatenate.
  2. Concatenate the string by using the join function and transform the value of that column using **lambda** statement.

We will use the CSV file having 2 columns, the content of the file is shown in
the below image:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803222006/content.JPG)

 **Example 1:** We will concatenate the data in the branch column having the
same name.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas library

import pandas as pd

 

# read csv file

df = pd.read_csv("Book2.csv")

 

# concatenate the string

df['branch'] =
df.groupby(['Name'])['branch'].transform(lambda x : '
'.join(x))

 

# drop duplicate data

df = df.drop_duplicates() 

 

# show the dataframe

print(df)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803222154/output-200x83.JPG)

 **Example 2:** We can perform Pandas groupby on multiple columns as well.

We will use the CSV file having 3 columns, the content of the file is shown in
the below image:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803222714/content.JPG)

Apply groupby on Name and year column

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas library

import pandas as pd

 

# read a csv file

df = pd.read_csv("Book1.csv")

 

# concatenate the string

df['branch'] = df.groupby(['Name',
'year'])['branch'].transform(

 lambda x: ' '.join(x))

 

# drop duplicate data

df = df.drop_duplicates() 

 

# show the dataframe

df  
  
---  
  
 __

 __

 **Output:**

![Groupby on multiple columns](https://media.geeksforgeeks.org/wp-
content/uploads/20200803222832/output-300x199.JPG)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

