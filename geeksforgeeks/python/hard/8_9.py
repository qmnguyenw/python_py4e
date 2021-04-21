Python | pandas.map()



pandas.map() is used to map values from two series having one column same. For
mapping two series, the last column of the first series should be same as
index column of the second series, also the values should be unique.

 **Syntax:**

    
    
    Series.map(arg, na_action=None)

>  **Parameters:**
>
>  **arg :** function, dict, or Series
>
>  **na_action :** _{None, ‘ignore’}_ If ‘ **ignore** ’, propagate NA values,
> without passing them to the mapping correspondence. **na_action** checks the
> NA value and ignores it while mapping in case of ‘ignore’
>
>  
>
>
>  
>

 **Return type:**

    
    
    Pandas Series with same as index as caller

 **Example #1:**  
In the following example, two series are made from same data. pokemon_names
column and pokemon_types index column are same and hence Pandas.map() matches
the rest of two columns and returns a new series.

>  **Note:**  
>  **- >** 2nd column of caller of map function must be same as index column
> of passed series.  
>  **- > **The values of common column must be unique too.

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

#reading csv files

pokemon_names = pd.read_csv("pokemon.csv", usecols =
["Pokemon"],

 squeeze = True)

 

#usecol is used to use selected columns

#index_col is used to make passed column as index

pokemon_types = pd.read_csv("pokemon.csv", index_col =
"Pokemon",

 squeeze = True)

 

#using pandas map function

new=pokemon_names.map(pokemon_types)

 

print (new)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/pandas-map.jpg)  
 **Example #2:**

This function works only with Series. Passing a data frame would give an
Attribute error. Passing series with different length will give the output
series of length same as the caller.

![](https://media.geeksforgeeks.org/wp-content/uploads/datamap.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

