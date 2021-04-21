Get list of column headers from a Pandas DataFrame



Let us see how to get all the column headers of a Pandas DataFrame as a list.
The df.columns.values attribute will return a list of column headers.

 **Example 1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# creating the dataframe

df = pd.DataFrame({'PassengerId': [892, 893, 894,
895, 

 896, 897, 898, 899],

 'PassengerClass': [1, 1, 2, 1, 3, 3, 2,
2],

 'PassengerName': ['John', 'Prity', 'Harry', 

 'Smith', 'James', 'Amora', 

 'Kiara', 'Joseph'], 

 'Age': [32, 54, 71, 21, 37, 9, 11,
54]})

 

display("The DataFrame :")

display(df)

 

# print the list of all the column headers

display("The column headers :")

display(list(df.columns.values))  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200723164503/jupyter_25.png)

 **Example 2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# creating the dataframe

my_df = {'Students': ['A', 'B', 'C', 'D'], 

 'BMI': [22.7, 18.0, 21.4, 24.1], 

 'Religion': ['Hindu', 'Islam', 

 'Christian', 'Sikh']}

df = pd.DataFrame(my_df)

display("The DataFrame :")

display(df)

 

# print the list of all the column headers

display("The column headers :")

display(list(df.columns.values))  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200723164558/jupyter_26.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

