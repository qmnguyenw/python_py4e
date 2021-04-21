Python | Pandas DatetimeIndex.second



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **DatetimeIndex.second** attribute outputs an Index object containing
the second values present in each of the entries of the DatetimeIndex object.

>  **Syntax:** DatetimeIndex.second
>
>  **Return:** Index containing seconds.

 **Example #1:** Use DatetimeIndex.second attribute to find the seconds
value present in the DatetimeIndex object.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Create the DatetimeIndex

didx = pd.DatetimeIndex(['2000-01-10 06:30:05', '2000-01-10
07:30:10',

 '2000-01-10 08:30:15'])

 

# Print the DatetimeIndex

print(didx)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-1011.png)

Now we want to find all the seconds value present in the DatetimeIndex object.

 __

 __  
 __

 __

 __  
 __  
 __

<div class="noIdeBtnDiv">

# find all the second values present in the object

didx.second  
  
---  
  
 __

 __

