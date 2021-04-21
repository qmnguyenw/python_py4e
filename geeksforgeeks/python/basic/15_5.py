Python | Pandas Index.value_counts()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **Index.value_counts()** function returns object containing counts of
unique values. The resulting object will be in descending order so that the
first element is the most frequently-occurring element. Excludes NA values by
default.

>  **Syntax:** Index.value_counts(normalize=False, sort=True, ascending=False,
> bins=None, dropna=True)
>
>  **Parameters :**  
>  **normalize :** If True then the object returned will contain the relative
> frequencies of the unique values.  
>  **sort :** Sort by values  
>  **ascending :** Sort in ascending order  
>  **bins :** Rather than count values, group them into half-open bins, a
> convenience for pd.cut, only works with numeric data  
>  **dropna :** Don’t include counts of NaN.
>
>  **Returns :** counts : Series
>
>  
>
>
>  
>

 **Example #1:** Use Index.value_counts() function to count the number of
unique values in the given Index.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Creating the index

idx = pd.Index(['Harry', 'Mike', 'Arther', 'Nick',

 'Harry', 'Arther'], name ='Student')

 

# Print the Index

print(idx)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-923.png)

Let’s find the count of all unique values in the index.

 __

 __  
 __

 __

 __  
 __  
 __

# find the count of unique values in the index

idx.value_counts()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-927.png)  
The function has returned the count of all unique values in the given index.
Notice the object returned by the function contains the occurrence of the
values in descending order.  
  
**Example #2:** Use Index.value_counts() function to find the count of all
unique values in the given index.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Creating the index

idx = pd.Index([21, 10, 30, 40, 50, 10, 50])

 

# Print the Index

print(idx)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-925.png)

Let’s count the occurrence of all the unique values in the Index.

 __

 __  
 __

 __

 __  
 __  
 __

# for finding the count of all

# unique values in the index.

idx.value_counts()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-928.png)  
The function has returned the count of all unique values in the index.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

