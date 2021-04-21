Python | Splitting Text and Number in string



Sometimes, we have a string, which is composed of text and number (or vice-
versa), without any specific distinction between the two. There might be a
requirement in which we require to separate the text from the number. Let’s
discuss certain ways in which this can be performed.

 **Method #1 : Usingre.compile() + re.match() + re.groups()**  
The combination of all the above regex functions can be used to perform this
particular task. In this we compile a regex and match it to group text and
numbers separately into a tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Splitting text and number in string 

# Using re.compile() + re.match() + re.groups()

import re

 

# initializing string 

test_str = "Geeks4321"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using re.compile() + re.match() + re.groups()

# Splitting text and number in string 

temp = re.compile("([a-zA-Z]+)([0-9]+)")

res = temp.match(test_str).groups()

 

# printing result 

print("The tuple after the split of string and number : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks4321
    The tuple after the split of string and number : ('Geeks', '4321')
    

**Method #2 : Usingre.findall()**  
The slight modification of regex can provide the flexibility to reduce the
number of regex functions required to perform this particular task. The
findall function is alone enough for this task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Splitting text and number in string 

# Using re.findall()

import re

 

# initializing string 

test_str = "Geeks4321"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using re.findall()

# Splitting text and number in string 

res = [re.findall(r'(\w+?)(\d+)', test_str)[0] ]

 

# printing result 

print("The tuple after the split of string and number : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks4321
    The tuple after the split of string and number : ('Geeks', '4321')
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

