Python | Pandas Series.str.rindex()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric Python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **str.rindex()** method is used to search and return highest
index(First from right side) of a substring in particular section (Between
start and end) of every string in a series. This method works in a similar way
to str.find() but on not found case, instead of returning -1, str.rindex()
gives a ValueError.

 **Note:** This method is differernt from str.index(). str.rindex() is for
reverse searching. Output of both str.index() and str.rindex() is same if the
substring exists only once in string.

>  **Syntax:** Series.str.rindex(sub, start=0, end=None)
>
>  **Parameters:**  
>  **sub:** String or character to be searched in the text value in series  
>  **start:** String or character to be searched in the text value in series  
>  **end:** String or character to be searched in the text value in series
>
>  
>
>
>  
>
>
>  **Return type:** Series with highest index of substring if found.

To download the data set used in following example, click here.  
In the following examples, the data frame used contains data of some NBA
players. The image of data frame before any operations is attached below.  
![](https://media.geeksforgeeks.org/wp-content/uploads/nba-1-1.png)

 **Example #1:** Finding highest index when substring exists in every string

In this example, ‘e’ is passed as substring. Since ‘e’ exists in all 5
strings, highest index of it’s occurrence is returned. Both index and rindex
methods are applied and output is stored in different columns to compare them.
Before applying any operations, null rows were removed using .dropna() method.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd

 

# reading csv file from url 

data = pd.read_csv("https://media.geeksforgeeks.org/wp-
content/uploads/nba.csv")

 

# dropping null value columns to avoid errors

data.dropna(inplace = True)

 

# extracting 5 rows

short_data = data.head().copy()

 

# calling str.index() method

short_data["Index Name"]=
short_data["Name"].str.index("e")

 

# calling str.rindex() method

short_data["Reverse Index Name"]=
short_data["Name"].str.rindex("e")

 

# display

short_data  
  
---  
  
 __

 __

 **Output:**  
As shown in the output image, It can be compared that .index() method returned
the least index while the str.rindex() method returned highest index.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2018-09-30-01-44-53.png)  
  
**Example #2:**  
In this example, ‘a’ is searched in top 5 rows. Since ‘a’ doesn’t exist in
every string, value error will be returned. To handle error, try and except is
used.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd

 

# reading csv file from url 

data = pd.read_csv("https://media.geeksforgeeks.org/wp-
content/uploads/nba.csv")

 

# dropping null value columns to avoid errors

data.dropna(inplace = True)

 

# extracting 5 rows

short_data = data.head().copy()

 

# calling str.rindex() method

try:

 short_data["Index Name"]=
short_data["Name"].str.rindex("a")

except Exception as err:

 print(err)

 

 

# display

short_data  
  
---  
  
 __

 __

 **Output:**  
As shown in output image, the output data frame is not having the Index Name
column and the error “substring not found” was printed. That is because
str.rindex() returns ValueError on not found and hence it must have gone to
except case and printed the error.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2018-09-29-15-21-16.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

