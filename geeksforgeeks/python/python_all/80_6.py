Python | Longest Run of given Character in String



Sometimes, while working with Strings, we can have a problem in which we need
to perform the extraction of length of longest consecution of certain letter.
This can have application in web development and competitive programming. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force method in which we can perform this task. In this, we run
a loop over the String and keep on memorizing the maximum whenever the run
occurs.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Longest Run of Character in String

# Using loop

 

# initializing string

test_str = 'geeksforgeeeks'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = 'e'

 

# Longest Run of Character in String

# Using loop

res = 0

cnt = 0

for chr in test_str:

 if chr == K:

 cnt += 1

 else:

 res = max(res, cnt)

 cnt = 0

res = max(res, cnt)

 

# printing result 

print("Longest Run length of K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeeks
    Longest Run length of K : 3
    

  
**  
Method #2 : Usingmax() + re.findall()**  
This is one liner way in which this problem can be solved. In this, we find
the maximum of all runs found using findall().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Longest Run of Character in String

# Using max() + re.findall()

import re

 

# initializing string

test_str = 'geeksforgeeeks'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = 'e'

 

# Longest Run of Character in String

# Using max() + re.findall()

res = len(max(re.findall(K + '+', test_str), key =
len))

 

# printing result 

print("Longest Run length of K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeeks
    Longest Run length of K : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

