Python | Consecutive element swapping in String



Sometimes, while working with strings, we can have a problem in which we may
require to perform swapping of consecutive elements in string. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usingjoin() + zip() \+ generator expression**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of joining consecutive characters using zip() and
generator expression is used to provide the swap logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive element swapping in String

# using join() + zip() + generator expression

 

# initializing string 

test_str = "gfgisbesty"

 

# printing original string 

print("The original string is : " + test_str)

 

# Consecutive element swapping in String

# using join() + zip() + generator expression

res = ''.join([char[1] + char[0] for char in
zip(test_str[::2], test_str[1::2])])

 

# printing result

print("String after Consecutive Swapping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : gfgisbesty
    String after Consecutive Swapping : fgigbsseyt
    

**Method #2 : Using regex expression**  
This task can also be performed using regular expression using correctly
framed regex.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive element swapping in String

# using regular expression

import re 

 

# initializing string 

test_str = "gfgisbesty"

 

# printing original string 

print("The original string is : " + test_str)

 

# Consecutive element swapping in String

# using regular expression

res = re.sub(r'(.)(.)', r'\2\1', test_str)

 

# printing result

print("String after Consecutive Swapping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : gfgisbesty
    String after Consecutive Swapping : fgigbsseyt
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

