Python – Replace multiple words with K



Sometimes, while working with Python strings, we can have a problem in which
we need to perform a replace of multiple words with a single word. This can
have application in many domains including day-day programming and school
programming. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingjoin() + split() \+ list comprehension**  
The combination of above functions can be used to perform this task. In this,
we split the string into words, check and replace the list words using join
and list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace multiple words with K

# Using join() + split() + list comprehension

 

# initializing string

test_str = 'Geeksforgeeks is best for geeks and CS'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing word list 

word_list = ["best", 'CS', 'for']

 

# initializing replace word 

repl_wrd = 'gfg'

 

# Replace multiple words with K

# Using join() + split() + list comprehension

res = ' '.join([repl_wrd if idx in word_list else idx
for idx in test_str.split()])

 

# printing result 

print("String after multiple replace : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Geeksforgeeks is best for geeks and CS
    String after multiple replace : Geeksforgeeks is gfg gfg geeks and gfg
    

**Method #2 : Using regex +join()**  
The combination of above functions can be used to perform this task. In this,
we find the words using regex and perform the replace using join() and list
comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace multiple words with K

# Using regex + join()

import re

 

# initializing string

test_str = 'Geeksforgeeks is best for geeks and CS'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing word list 

word_list = ["best", 'CS', 'for']

 

# initializing replace word 

repl_wrd = 'gfg'

 

# Replace multiple words with K

# Using regex + join()

res = re.sub("|".join(sorted(word_list, key = len, reverse
= True)), repl_wrd, test_str)

 

# printing result 

print("String after multiple replace : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Geeksforgeeks is best for geeks and CS
    String after multiple replace : Geeksforgeeks is gfg gfg geeks and gfg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

