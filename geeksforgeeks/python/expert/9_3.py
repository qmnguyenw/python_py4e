Python | Pandas dataframe.sub()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **dataframe.sub()** function is used for finding the subtraction of
dataframe and other, element-wise. This function is essentially same as doing
dataframe - other but with a support to substitute for missing data in one
of the inputs.

>  **Syntax:** DataFrame.sub(other, axis=’columns’, level=None,
> fill_value=None)
>
>  **Parameters :**  
>  **other :** Series, DataFrame, or constant  
>  **axis :** For Series input, axis to match Series index on  
>  **level :** Broadcast across a level, matching Index values on the passed
> MultiIndex leve  
>  **fill_value :** Fill existing missing (NaN) values, and any new element
> needed for successful DataFrame alignment, with this value before
> computation. If data in both corresponding DataFrame locations is missing
> the result will be missing.
>
>  **Returns :** result : DataFrame
>
>  
>
>
>  
>

 **Example #1:** Use sub() function to subtract each element of a dataframe
with a corresponding element in a series.

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

df = pd.DataFrame({"A":[1, 5, 3, 4, 2],

 "B":[3, 2, 4, 3, 4], 

 "C":[2, 2, 7, 3, 4], 

 "D":[4, 3, 6, 12, 7]}, 

 index =["A1", "A2", "A3", "A4", "A5"])

 

# Print the dataframe

df  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/1-645.png)

Let’s create the series

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Create the series

sr = pd.Series([12, 25, 64, 18], index =["A",
"B", "C", "D"])

 

# Print the series

sr  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/1-661.png)

Let’s use thedataframe.sub() function for subtraction.

 __

 __  
 __

 __

 __  
 __  
 __

# equivalent to df - sr

df.sub(sr, axis = 1)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-704.png)  
  
**Example #2:** Use sub() function to subtract each element in a dataframe
with the corresponding element in other dataframe

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Creating the first dataframe 

df1 = pd.DataFrame({"A":[1, 5, 3, 4, 2],

 "B":[3, 2, 4, 3, 4],

 "C":[2, 2, 7, 3, 4],

 "D":[4, 3, 6, 12, 7]}, 

 index =["A1", "A2", "A3", "A4", "A5"])

 

# Creating the second dataframe

df2 = pd.DataFrame({"A":[10, 11, 7, 8, 5],

 "B":[21, 5, 32, 4, 6], 

 "C":[11, 21, 23, 7, 9],

 "D":[1, 5, 3, 8, 6]},

 index =["A1", "A2", "A3", "A4", "A5"])

 

# subtract df2 from df1

df1.sub(df2)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-705.png)  
Notice, each element of the dataframe df1 has been subtracted with the
corresponding element in the df2.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

