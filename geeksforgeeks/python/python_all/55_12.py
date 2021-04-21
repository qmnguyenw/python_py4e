Pandas – Convert the first and last character of each word to upper case in a
series



In python, if we wish to convert only the first character of every word to
uppercase, we can use the capitalize() method. Or we can take just the first
character of the string and change it to uppercase using the upper() method.
So, to convert the first and last character of each word to upper case in a
series we will be using a similar approach. First of all, let’s create a
series in Pandas.  

**Example :** Let’s create a Pandas Series

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

series = pd.Series(['geeks', 'for', 'geeks',

 'pandas', 'series'])

 

# Print the series

print("Series:")

series  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200708110534/series.jpg)

Once we have created a series using Pandas, we will apply a lambda() function
to the entire series using the map() function. The lambda function will take
the first character using slicing, capitalize it and add the rest of the
string as it is until the last character. The last character is again
capitalized and added to the resultant series.

 **Example :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Apply the lambda function to

# capitalize first and last 

# character to each word

newSeries = series.map(lambda x: x[0].upper() +
x[1:-1] + x[-1].upper())

 

# Print the resulting series

print("\nResulting Series :")

newSeries  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200708110532/resultSeries.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

