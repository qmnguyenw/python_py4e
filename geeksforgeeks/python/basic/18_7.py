Python | Pandas Dataframe/Series.head() method



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric Python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **head()** method is used to return top n (5 by default) rows of a
data frame or series.

>  **Syntax:** Dataframe.head(n=5)
>
>  **Parameters:**  
>  **n:** integer value, number of rows to be returned
>
>  **Return type:** Dataframe with top n rows
>
>  
>
>
>  
>

To download the data set used in following example, click here.  
In the following examples, the data frame used contains data of some NBA
players. The image of data frame before any operations is attached below.  
![](https://media.geeksforgeeks.org/wp-content/uploads/nba-1-1.png)

 **Example #1:**

In this example, top 5 rows of data frame are returned and stored in a new
variable. No parameter is passed to .head() method since by default it is 5.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

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

 **Output:**  
As shown in the output image, it can be seen that the index of returned rows
is ranging from 0 to 4. Hence, top 5 rows were returned.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2018-09-30-03-47-29.png)

  
**Example #2:** Calling on Series with n parameter()

In this example, the .head() method is called on series with custom input of n
parameter to return top 9 rows of the series.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd

 

# making data frame

data = pd.read_csv("https://media.geeksforgeeks.org/wp-
content/uploads/nba.csv")

 

# number of rows to return

n = 9

 

# creating series

series = data["Name"]

 

# returning top n rows

top = series.head(n = n)

 

# display

top  
  
---  
  
 __

 __

 **Output:**  
As shown in the output image, top 9 rows ranging from 0 to 8th index position
were returned.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2018-09-30-03-57-39.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

