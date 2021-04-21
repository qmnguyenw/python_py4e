How to get column names in Pandas dataframe



While analyzing the real datasets which are often very huge in size, we might
need to get the column names in order to perform some certain operations.

Let’s discuss how to get column names in Pandas dataframe.

First, let’s create a simple dataframe with nba.csv file.

 __

 __  
 __

 __

 __  
 __  
 __

# Import pandas package

import pandas as pd 

 

# making data frame 

data = pd.read_csv("https://media.geeksforgeeks.org/wp-
content/uploads/nba.csv") 

 

# calling head() method 

# storing in new variable 

data_top = data.head() 

 

# display 

data_top   
  
---  
  
__

__

![](https://media.geeksforgeeks.org/wp-content/uploads/col_names1.png)  
Now let’s try to get the columns name from above dataset.

 **Method #1:** Simply iterating over columns

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Import pandas package

import pandas as pd 

 

# making data frame 

data = pd.read_csv("nba.csv") 

 

# iterating the columns

for col in data.columns:

 print(col)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/col_names2.png)  
  
**Method #2:** Using columns with dataframe object

 __

 __  
 __

 __

 __  
 __  
 __

# Import pandas package

import pandas as pd 

 

# making data frame 

data = pd.read_csv("nba.csv") 

 

# list(data) or

list(data.columns)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/col_names3.png)  
  
**Method #3:** column.values method returs an array of index.

 __

 __  
 __

 __

 __  
 __  
 __

# Import pandas package

import pandas as pd 

 

# making data frame 

data = pd.read_csv("nba.csv") 

 

list(data.columns.values)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/col_names3.png)  
  
**Method #4:** Using tolist() method with values with given the list of
columns.

 __

 __  
 __

 __

 __  
 __  
 __

# Import pandas package

import pandas as pd 

 

# making data frame 

data = pd.read_csv("nba.csv") 

 

list(data.columns.values.tolist())  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/col_names3.png)  
  
**Method #5:** Using sorted() method

Sorted() method will return the list of columns sorted in alphabetical order.

 __

 __  
 __

 __

 __  
 __  
 __

# Import pandas package

import pandas as pd 

 

# making data frame 

data = pd.read_csv("nba.csv") 

 

# using sorted() method

sorted(data)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/col_names4.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

