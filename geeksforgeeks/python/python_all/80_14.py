Python | Word location in String



Sometimes, while working with Python strings, we can have problem in which we
need to find location of a particular word. This can have application in
domains such as day-day programming. Lets discuss certain ways in which this
task can be done.

 **Method #1 : Usingre.findall() + index()**  
This is one of the way in which we can find the location where word exists. In
this we look for substring pattern using findall() and its position using
index().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Word location in String

# Using findall() + index()

import re

 

# initializing string

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing word 

wrd = 'best'

 

# Word location in String

# Using findall() + index()

test_str = test_str.split()

res = -1

for idx in test_str:

 if len(re.findall(wrd, idx)) > 0:

 res = test_str.index(idx) + 1

 

# printing result 

print("The location of word is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best for geeks
    The location of word is : 3
    

**Method #2 : Usingre.sub() + index()**  
This performs this task in similar way as above method. In this also regex is
employed. We use different regex function in this method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Word location in String

# Using re.sub() + index()

import re

 

# initializing string

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing word 

wrd = 'best'

 

# Word location in String

# Using re.sub() + index()

res = re.sub("[^\w]", " ", test_str).split()

res = res.index(wrd) + 1

 

# printing result 

print("The location of word is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best for geeks
    The location of word is : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

