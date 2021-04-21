Get the absolute values in Pandas



Let us see how to get the absolute value of an element in Python Pandas. We
can perform this task by using the **abs()** function. The abs() function is
used to get a Series/DataFrame with absolute numeric value of each element.

>  **Syntax :** Series.abs() or DataFrame.abs()  
>  **Parameters** : None  
>  **Returns :** Series/DataFrame containing the absolute value of each
> element.

 **Example 1 :** Absolute numeric values in a Series.

 __

 __  
 __

 __

 __  
 __  
 __

# import the library

import pandas as pd

 

# create the Series

s = pd.Series([-2.8, 3, -4.44, 5])

print(s)

 

# fetching the absolute values

print("\nThe absolute values are :")

print(s.abs())  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200730133037/jupyterr10.png)

 **Example 2 :** Absolute numeric values in a Series with complex numbers.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import the library

import pandas as pd

 

# create the Series

s = pd.Series([2.2 + 1j])

print(s)

 

# fetching the absolute values

print("\nThe absolute values are :")

print(s.abs())  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200730132956/jupyterr9.png)

 **Example 3 :** Absolute numeric values in a Series with a Timedelta element.

 __

 __  
 __

 __

 __  
 __  
 __

# import the library

import pandas as pd

 

# create the Series

s = pd.Series([pd.Timedelta('2 days')])

print(s)

 

# fetching the absolute values

print("\nThe absolute values are :")

print(s.abs())  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200730133211/jupyterr11.png)

 **Example 4 :** Fetching the absolute values from a DataFrame column.

 __

 __  
 __

 __

 __  
 __  
 __

# import the library

import pandas as pd

 

# create the DataFrame

df = pd.DataFrame({'p' : [2, 3, 4, 5],

 'q' : [10, 20, 30, 40],

 'r' : [200, 60, -40, -60]})

display(df)

 

# fetching the absolute values

print("\nThe absolute values are :")

display(df.r.abs())  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200730134157/jupyterr12.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

