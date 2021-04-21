How to Union Pandas DataFrames using Concat?



 **concat()** function does all of the heavy liftings of performing
concatenation operations along an axis while performing optional set logic
(union or intersection) of the indexes (if any) on the other axes.

The concat() function combines data frames in one of two ways:

  *  **Stacked: Axis = 0 (This is the default option).**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200627181638/ConcatUpdated-218x300.png)

Axis=0

  *  **Side by Side: Axis = 1**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200627184719/ConcatAxis1-300x128.png)

Axis=1

 **Steps to Union Pandas DataFrames using Concat:**

  *  **Create the first DataFrame**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

students1 = {'Class': ['10','10','10'],

 'Name': ['Hari','Ravi','Aditi'],

 'Marks': [80,85,93]

 }

 

df1 = pd.DataFrame(students1, columns=
['Class','Name','Marks'])

 

df1  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200703182928/pandasconcatenate1.png)

  * **Create the second DataFrame**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

students2 = {'Class': ['10','10','10'],

 'Name': ['Tanmay','Akshita','Rashi'],

 'Marks': [89,91,87]

 }

 

df2 = pd.DataFrame(students2, 

 columns= ['Class','Name','Marks'])

 

df2  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200703183123/pandasconcatenate2.png)

  *  **Union Pandas DataFrames using Concat**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

pd.concat([df1,df2])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200703183301/pandasconcatenate3.png)

**Note:** You’ll need to keep the same column names across all the DataFrames
to avoid any ‘NaN’ values.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

