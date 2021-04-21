Python | Remove unwanted spaces from string



Sometimes, while working with strings, we may have situations in which we
might have more than 1 spaces between intermediate words in strings that are
mostly unwanted. This type of situations can occur in web development and
often needs rectification. Let’s discuss certain ways in which this task can
be performed.

 **Method #1 : Usingre.sub()**  
This problem can be performed using the regex in which we can restrict the
separation between the words to be just a single space using the appropriate
regex string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# remove additional space from string

# Using re.sub()

import re

 

# initializing string 

test_str = "GfG is good website"

 

# printing original string 

print("The original string is : " + test_str)

 

# using re.sub()

# remove additional space from string 

res = re.sub(' +', ' ', test_str)

 

# printing result 

print("The strings after extra space removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GfG  is   good           website
    The strings after extra space removal : GfG is good website
    

**Method #2 : Usingsplit() and join()**  
This task can also be performed using the split and join function. This is
performed in two steps. In first step, we convert the string into list of
words and then join with a single space using the join function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# remove additional space from string

# Using split() + join()

 

# initializing string 

test_str = "GfG is good website"

 

# printing original string 

print("The original string is : " + test_str)

 

# using split() + join()

# remove additional space from string 

res = " ".join(test_str.split())

 

# printing result 

print("The strings after extra space removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GfG  is   good           website
    The strings after extra space removal : GfG is good website
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

