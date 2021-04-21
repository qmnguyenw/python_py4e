Python | Words lengths in String



We sometimes come through the situations where we require to get all the words
lengths present in the string, this can be a tedious task done using naive
method. Hence having shorthands to perform this task is always useful. Let’s
discuss certain ways to achieve this.

 **Method #1 : Usingsplit() + len()**  
Using split function, we can split the string into a list of words and is most
generic and recommended method if one wished to accomplish this particular
task. But drawback is that it fails in the cases in string contains
punctuation marks. The len() is used to compute string length.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Words lengths in String

# using split()

 

# initializing string 

test_string = "Geeksforgeeks is best Computer Science Portal"

 

# printing original string

print ("The original string is : " + test_string)

 

# using split()

# Words lengths in String

res = list(map(len, test_string.split()))

 

# printing result

print ("The list of words lengths is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeksforgeeks is best Computer Science Portal
    The list of words lengths is : [13, 2, 4, 8, 7, 6]
    

**Method #2 : Usingregex( findall() ) + len()**  
In the cases which contain all the special characters and punctuation marks,
as discussed above, the conventional method of finding words in string using
split can fail and hence requires regular expressions to perform this task.
findall function returns the list after filtering the string and extracting
words ignoring punctuation marks. The len() is used to compute string length.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Words lengths in String

# using regex( findall() )

import re

 

# initializing string 

test_string = "Geeksforgeeks, is best @# Computer Science Portal.!!!"

 

# printing original string

print ("The original string is : " + test_string)

 

# using regex( findall() )

# Words lengths in String

res = list(map(len, re.findall(r'\w+', test_string)))

 

# printing result

print ("The list of words lengths is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeksforgeeks is best Computer Science Portal
    The list of words lengths is : [13, 2, 4, 8, 7, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

