Python | Pandas dataframe.keys()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **dataframe.keys()** function returns the ‘info axis’ for the pandas
object. If the pandas object is **series** then it returns index. If the
pandas object is **dataframe** then it returns columns. If the pandas object
is **panel** then it returns major_axis.

>  **Syntax:** DataFrame.keys()

For link to the CSV file, click here

 **Example #1:** Use keys() function to find the columns of a dataframe.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Creating the dataframe 

df = pd.read_csv("nba.csv")

 

# Print the dataframe

df  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/1-548.png)

 __

 __  
 __

 __

 __  
 __  
 __

# find the keys of the dataframe

df.keys()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-549.png)  
  
**Example #2:** Use keys() function to find the index of the pandas
**series** object.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Creating the series 

sr = pd.Series([12, 5, None, 5, None, 11])

 

# Print the series

sr  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/1-546.png)

 __

 __  
 __

 __

 __  
 __  
 __

# to find the index

sr.keys()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-550.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

