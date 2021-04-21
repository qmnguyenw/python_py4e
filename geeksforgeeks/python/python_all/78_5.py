Python – Non-overlapping Random Ranges



Sometimes, while working with Python, we can have problem in which we need to
extract N random ranges which are non-overlapping in nature and with given
range size. This can have applications in which we work with data. Lets
discuss certain way in which this task can be performed.

 **Method : Usingany() + randint() \+ loop**  
This is brute force way in which this task can be performed. In this we
extract random ranges using randint(), and check for non-repetition of number
ranges using any() and loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Non-overlapping Random Ranges

# Using loop + any() + randint()

import random

 

# initializing N 

N = 7

 

# initializing K 

K = 5

 

# Non-overlapping Random Ranges

# Using loop + any() + randint()

tot = 10000

res = set()

for _ in range(N):

 temp = random.randint(0, tot - K) 

 while any(temp >= idx and temp <= idx + K for idx
in res):

 temp = random.randint(0, tot - K) 

 res.add(temp)

res = [(idx, idx + K) for idx in res]

 

# printing result 

print("The N Non-overlapping Random ranges are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The N Non-overlapping Random ranges are : [(5347, 5352), (7108, 7113), (5479, 5484), (1906, 1911), (2228, 2233), (5206, 5211), (3260, 3265)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

