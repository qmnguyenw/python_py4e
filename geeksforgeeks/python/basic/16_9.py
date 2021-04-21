Python | Pandas dataframe.groupby()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **dataframe.groupby()** function is used to split the data into
groups based on some criteria. pandas objects can be split on any of their
axes. The abstract definition of grouping is to provide a mapping of labels to
group names.

>  **Syntax:** DataFrame.groupby(by=None, axis=0, level=None, as_index=True,
> sort=True, group_keys=True, squeeze=False, **kwargs)
>
>  **Parameters :**  
>  **by :** mapping, function, str, or iterable  
>  **axis :** int, default 0  
>  **level :** If the axis is a MultiIndex (hierarchical), group by a
> particular level or levels  
>  **as_index :** For aggregated output, return object with group labels as
> the index. Only relevant for DataFrame input. as_index=False is effectively
> “SQL-style” grouped output  
>  **sort :** Sort group keys. Get better performance by turning this off.
> Note this does not influence the order of observations within each group.
> groupby preserves the order of rows within each group.  
>  **group_keys :** When calling apply, add group keys to index to identify
> pieces  
>  **squeeze :** Reduce the dimensionality of the return type if possible,
> otherwise return a consistent type
>
>  **Returns :** GroupBy object
>
>  
>
>
>  
>

For link to CSV file Used in Code, click here

 **Example #1:** Use groupby() function to group the data based on the
“Team”.

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

![](https://media.geeksforgeeks.org/wp-content/uploads/1-506.png)

Now apply thegroupby() function.

 __

 __  
 __

 __

 __  
 __  
 __

# applying groupby() function to

# group the data on team value.

gk = df.groupby('Team')

 

# Let's print the first entries

# in all the groups formed.

gk.first()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-519.png)

Let’s print the value contained any one of group. For that use the name of the
team. We use the function get_group() to find the entries contained in any
of the groups.

 __

 __  
 __

 __

 __  
 __  
 __

# Finding the values contained in the "Boston Celtics" group

gk.get_group('Boston Celtics')  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-520.png)  
  
**Example #2:** Use groupby() function to form groups based on more than one
category (i.e. Use more than one column to perform the splitting).

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

 

# First grouping based on "Team"

# Within each team we are grouping based on "Position"

gkk = df.groupby(['Team', 'Position'])

 

# Print the first value in each group

gkk.first()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-521.png)

groupby() is a very powerful function with a lot of variations. It makes the
task of splitting the dataframe over some criteria really easy and efficient.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

