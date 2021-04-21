Python Program to perform cross join in Pandas



In Pandas, there are parameters to perform left, right, inner or outer merge
and join on two DataFrames or Series. However there’s no possibility as of now
to perform a cross join to merge or join two methods using how="cross"
parameter.

 **Cross Join :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200625140356/cross-
joinPd-1.png)  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200625140450/resultCrossJoin.png)

 **Example 1:**

The above example is proven as follows

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd 

 

# Define a dictionary with column A

data1 = {'A': [1, 2]} 

 

# Define another dictionary with column B

data2 = {'B': ['a', 'b', 'c']} 

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data1, index =[0, 1])

 

# Convert the dictionary into DataFrame 

df1 = pd.DataFrame(data2, index =[2, 3, 4]) 

 

# Now to perform cross join, we will create

# a key column in both the DataFrames to 

# merge on that key.

df['key'] = 1

df1['key'] = 1

 

# to obtain the cross join we will merge 

# on the key and drop it.

result = pd.merge(df, df1, on ='key').drop("key", 1)

 

result  
  
---  
  
 __

 __

 **DataFrame 1:** ![](https://media.geeksforgeeks.org/wp-
content/uploads/20200703130307/ex1df.png)  
**DataFrame 2 :**![](https://media.geeksforgeeks.org/wp-
content/uploads/20200703130327/ex1df1.png)  
 **Output :**![](https://media.geeksforgeeks.org/wp-
content/uploads/20200703130342/ex1op.png)

  

  

 **Example 2:**

Cross join on two DataFrames for user and product.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd 

 

# Define a dictionary containing user ID

data1 = {'Name': ["Rebecca", "Maryam", "Anita"],

 'UserID': [1, 2, 3]} 

 

# Define a dictionary containing product ID 

data2 = {'ProductID': ['P1', 'P2', 'P3', 'P4']} 

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data1, index =[0, 1, 2])

 

# Convert the dictionary into DataFrame 

df1 = pd.DataFrame(data2, index =[2, 3, 6, 7]) 

 

# Now to perform cross join, we will create

# a key column in both the DataFrames to 

# merge on that key.

df['key'] = 1

df1['key'] = 1

 

# to obtain the cross join we will merge on 

# the key and drop it.

result = pd.merge(df, df1, on ='key').drop("key", 1)

 

result  
  
---  
  
 __

 __

 **DataFrame 1:** ![](https://media.geeksforgeeks.org/wp-
content/uploads/20200625141748/df13.png)  
**DataFrame 2 :**![](https://media.geeksforgeeks.org/wp-
content/uploads/20200625141806/df21.png)  
 **Output :**![](https://media.geeksforgeeks.org/wp-
content/uploads/20200625141944/crossJoinRes2.png)

 **Example 3:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd 

 

# Define a dictionary with two columns

data1 = {'col 1': [0, 1],

 'col 2': [2, 3]} 

 

# Define another dictionary 

data2 = {'col 3': [5, 6],

 'col 4': [7, 8]} 

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data1, index =[0, 1])

 

# Convert the dictionary into DataFrame 

df1 = pd.DataFrame(data2, index =[2, 3]) 

 

# Now to perform cross join, we will create

# a key column in both the DataFrames to

# merge on that key.

df['key'] = 1

df1['key'] = 1

 

# to obtain the cross join we will merge on 

# the key and drop it.

result = pd.merge(df, df1, on ='key').drop("key", 1)

 

result  
  
---  
  
 __

 __

 **DataFrame 1:** ![](https://media.geeksforgeeks.org/wp-
content/uploads/20200703124927/ex2df.png)  
**DataFrame 2 :**![](https://media.geeksforgeeks.org/wp-
content/uploads/20200703124944/ex2df1.png)  
 **Output :**![](https://media.geeksforgeeks.org/wp-
content/uploads/20200703125001/ex2op.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

