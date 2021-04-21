Python | Pandas Timestamp.second



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **Timestamp.second** attribute return an integer value which
represents the value of second in the given Timestamp object.

>  **Syntax :** Timestamp.second
>
>  **Parameters :** None
>
>  **Return :** second
>
>  
>
>
>  
>

 **Example #1:** Use Timestamp.second attribute to find second’s value in
the given Timestamp object.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Create the Timestamp object

ts = pd.Timestamp(2016, 1, 1, 12, 25, 16, 28,
32)

 

# Print the Timestamp object

print(ts)  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-content/uploads/1-1464.png)

Now we will use the Timestamp.second attribute to find the second’s value in
the given object.

 __

 __  
 __

 __

 __  
 __  
 __

# return the value of second

ts.second  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-content/uploads/1-1467.png)  
As we can see in the output, the Timestamp.second attribute has returned 16
indicating that the second’s value in the given object is set to 16.  
  
**Example #2:** Use Timestamp.second attribute to find second’s value in the
given Timestamp object.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Create the Timestamp object

ts = pd.Timestamp(year = 2009, month = 5, day = 31,
hour = 4, 

 second = 49, tz = 'Europe/Berlin')

 

# Print the Timestamp object

print(ts)  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-content/uploads/1-1468.png)

Now we will use the Timestamp.second attribute to find the second’s value in
the given object.

 __

 __  
 __

 __

 __  
 __  
 __

# return the value of second

ts.second  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-content/uploads/2-369.png)

As we can see in the output, the Timestamp.second attribute has returned 49
indicating that the second’s value in the given object is set to 49.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

