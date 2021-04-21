Difference between loc() and iloc() in Pandas DataFrame



Pandas library of python is very useful for the manipulation of mathematical
data and is widely used in the field of machine learning. It comprises of many
methods for its proper functioning. **loc()** and **iloc()** are one of
those methods. These are used in slicing of data from the Pandas DataFrame.
They help in the convenient selection of data from the DataFrame. They are
used in filtering the data according to some conditions. Working of both of
these methods is explained in the sample dataset of cars.

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import pandas as pd

 

# creating a sample dataframe

data = pd.DataFrame({'Brand' : ['Maruti', 'Hyundai',
'Tata',

 'Mahindra', 'Maruti', 'Hyundai',

 'Renault', 'Tata', 'Maruti'],

 'Year' : [2012, 2014, 2011, 2015, 2012, 

 2016, 2014, 2018, 2019],

 'Kms Driven' : [50000, 30000, 60000, 

 25000, 10000, 46000, 

 31000, 15000, 12000],

 'City' : ['Gurgaon', 'Delhi', 'Mumbai', 

 'Delhi', 'Mumbai', 'Delhi', 

 'Mumbai','Chennai', 'Ghaziabad'],

 'Mileage' : [28, 27, 25, 26, 28, 

 29, 24, 21, 24]})

 

# displaying the DataFrame

display(data)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805205050/jjupyter1.png)

 **loc()** : loc() is label based data selecting method which means that we
have to pass the name of the row or column which we want to select. This
method includes the last element of the range passed in it, unlike iloc().
loc() can accept the boolean data unlike iloc() . Many operations can be
performed using the loc() method like-

 **1.** Selecting data according to some conditions :

 __

 __  
 __

 __

 __  
 __  
 __

# selecting cars with brand 'Maruti' and Mileage> 25

display(data.loc[(data.Brand == 'Maruti') & (data.Mileage >
25)])  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805205504/jjupyter2.png)

  

  

 **2.** Selecting a range of rows from the DataFrame :

 __

 __  
 __

 __

 __  
 __  
 __

# selecting range of rows from 2 to 5

display(data.loc[2 : 5])  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805205628/jjupyter3.png)

 **3.** Updating the value of any column :

 __

 __  
 __

 __

 __  
 __  
 __

# updating values of Mileage if Year< 2015

data.loc[(data.Year < 2015), ['Mileage']] = 22

display(data)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805205807/jjupyter4.png)

 **iloc() :**iloc() is a indexed based selecting method which means that we
have to pass integer index in the method to select specific row/column. This
method does not include the last element of the range passed in it unlike
loc(). iloc() does not accept the boolean data unlike loc(). Operations
performed using iloc() are:

 **1.** Selecting rows using integer indices:

 __

 __  
 __

 __

 __  
 __  
 __

# selecting 0th, 2th, 4th, and 7th index rows

display(data.iloc[[0, 2, 4, 7]])  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805210049/jjupyter5.png)

 **2.** Selecting a range of columns and rows simultaneously:

 __

 __  
 __

 __

 __  
 __  
 __

# selecting rows from 1 to 4 and columns from 2 to 4

display(data.iloc[1 : 5, 2 : 5])  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805210207/jjupyter6.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

