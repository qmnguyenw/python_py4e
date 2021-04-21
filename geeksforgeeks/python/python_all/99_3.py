Python – Multimode of List



Sometimes, while working with Python lists we can have a problem in which we
need to find mode in list i.e most frequently occurring character. But
sometimes, we can have more than 1 modes. This situation is called multimode.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop + formula**  
The simpler manner to approach this problem is to employ the formula for
finding multimode and perform using loop shorthands. This is the most basic
approach to solve this problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multimode of List

# using loop + formula 

import math

from collections import Counter

 

# initialize list 

test_list = [1, 2, 1, 2, 3, 4, 3] 

 

# printing original list 

print("The original list is : " + str(test_list)) 

 

# Multimode of List

# using loop + formula 

res = []

test_list1 = Counter(test_list) 

temp = test_list1.most_common(1)[0][1] 

for ele in test_list:

 if test_list.count(ele) == temp:

 res.append(ele)

res = list(set(res))

 

# printing result 

print("The multimode of list is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [1, 2, 1, 2, 3, 4, 3]
    The multimode of list is : [1, 2, 3]
    

**Method #2 : Usingstatistics.multimode()**  
This task can also be performed using inbuilt function of mulimode(). This is
new in Python versions >= 3.8.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multimode of List

# using statistics.multimode() 

import statistics 

 

# initialize list 

test_list = [1, 2, 1, 2, 3, 4, 3] 

 

# printing original list 

print("The original list is : " + str(test_list)) 

 

# Multimode of List

# using statistics.multimode() 

res = statistics.multimode(test_list) 

 

# printing result 

print("The multimode of list is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [1, 2, 1, 2, 3, 4, 3]
    The multimode of list is : [1, 2, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

