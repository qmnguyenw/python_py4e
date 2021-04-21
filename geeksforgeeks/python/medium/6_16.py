Add column names to dataframe in Pandas



Let us how to add names to DataFrame columns in Pandas.

 **Creating the DataFrame :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing the pandas library

import pandas as pd

 

# creating lists

l1 =["Amar", "Barsha", "Carlos", "Tanmay", "Misbah"]

l2 =["Alpha", "Bravo", "Charlie", "Tango", "Mike"]

l3 =[23, 25, 22, 27, 29]

l4 =[69, 54, 73, 70, 74]

 

# creating the DataFrame

team = pd.DataFrame(list(zip(l1, l2, l3, l4))) 

 

# displaying the DataFrame

print(team)  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200712151207/Data-200x173.jpg)

Here we can see that the columns in the DataFrame are unnamed.

  

  

 **Adding column name to the DataFrame :** We can add columns to an existing
DataFrame using its columns attribute.

 __

 __  
 __

 __

 __  
 __  
 __

# adding column name to the respective columns

team.columns =['Name', 'Code', 'Age', 'Weight']

 

# displaying the DataFrame

print(team)  
  
---  
  
 __

 __

  
**Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200712151004/Data-300x216.jpg)

Now the DataFrame has column names.

 **Renaming column name of a DataFrame :** We can rename the columns of a
DataFrame by using the rename() function.

 __

 __  
 __

 __

 __  
 __  
 __

# reanming the DataFrame columns

team.rename(columns = {'Code':'Code-Name', 

 'Weight':'Weight in kgs'}, 

 inplace = True)

 

# displaying the DataFrame

print(team)  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200712151310/22-300x168.jpg)

We can see the names of the columns have been changed.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

