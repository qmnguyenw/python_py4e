Find all the numbers in a string using regular expression in Python



Given a string **str** containing numbers and alphabets, the task is to find
all the numbers in **str** using regular expression.

 **Examples:**

>  **Input:** abcd11gdf15hnnn678hh4  
>  **Output:** 11 15 678 4
>
>  **Input:** 1abcd133hhe0  
>  **Output:** 1 133 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use Python re library to extract the sub-strings
from the given string which match the pattern **[0-9]+**. This pattern will
extract all the characters which match from **0** to **9** and the **+** sign
indicates one or more occurrence of the continuous characters.

  

  

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to extract all the numbers from a string

import re

 

# Function to extract all the numbers from the given string

def getNumbers(str):

 array = re.findall(r'[0-9]+', str)

 return array

 

# Driver code

str = "adbv345hj43hvb42"

array = getNumbers(str)

print(*array)  
  
---  
  
 __

 __

 **Output:**

    
    
    345 43 42
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

