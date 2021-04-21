Python | Pandas Index.insert()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **Index.insert()** function make new Index inserting new item at
location. This function also follows Python list.append() semantics for
negative values. If the negative value are passed then it start from the other
end.

>  **Syntax:** Index.insert(loc, item)
>
>  **Parameters :**  
>  **loc :** int  
>  **item :** object
>
>  **Returns :** new_index : Index
>
>  
>
>
>  
>

 **Example #1:** Use Index.insert() function to insert a new value in the
Index.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Creating the Index

idx = pd.Index(['Labrador', 'Beagle', 'Labrador',

 'Lhasa', 'Husky', 'Beagle'])

 

# Print the Index

idx  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-805.png)  
Now insert ‘Great_Dane’ at the 1st index.

 __

 __  
 __

 __

 __  
 __  
 __

# Inserting a value at the first position in the index.

idx.insert(1, 'Great_Dane')  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-827.png)

As we can see in the output, the Index.insert() function has inserted the
passed value at the desired location.  
  
**Example #2:** Use Index.insert() function to insert a value into the Index
at the second position from the last in the Index.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Creating the Index

idx = pd.Index(['Labrador', 'Beagle', 'Labrador',

 'Lhasa', 'Husky', 'Beagle'])

 

# Print the Index

idx  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-805.png)

Now insert ‘Great_Dane’ at the 1st index from the last.

 __

 __  
 __

 __

 __  
 __  
 __

# Inserting a value at the first position in the index.

idx.insert(-1, 'Great_Dane')  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-828.png)  
As we can see in the output, the passed value has been inserted into the Index
at the desired location.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

