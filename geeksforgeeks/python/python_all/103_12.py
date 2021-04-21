Python | Mathematical Median of Cumulative Records



Sometimes, while working with Python tuple list, we can have a problem in
which we need to find the median of tuple values in the list. This problem has
the possible application in many domains including mathematics. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Using loops +"~" operator**  
This task can be performed in brute force manner using the combination of
above functionalities. In this, we sort the list and the by using the property
of “~” operator to perform negation, we access the list from front and rear
after flattening, performing the required computation required for finding
median.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mathematical Median of Cumulative Records

# Using loop + "~" operator 

 

# initializing list 

test_list = [(1, 4, 5), (7, 8), (2, 4,
10)]

 

# printing list 

print("The original list : " + str(test_list)) 

 

# Mathematical Median of Cumulative Records 

# Using loop + "~" operator 

res = []

for sub in test_list :

 for ele in sub :

 res.append(ele)

res.sort() 

mid = len(res) // 2

res = (res[mid] + res[~mid]) / 2

 

# Printing result 

print("Median of Records is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [(1, 4, 5), (7, 8), (2, 4, 10)]
    Median of Records is : 4.5
    

**Method #2 : Usingchain() + statistics.median()**  
This is the most generic method to perform this task. In this we directly use
inbuilt function after flattening using chain() to perform the median of the
flattened list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mathematical Median of Cumulative Records

# Using chain() + statistics.median()

import statistics 

from itertools import chain

 

# initializing list 

test_list = [(1, 4, 5), (7, 8), (2, 4,
10)] 

 

# printing list 

print("The original list : " + str(test_list)) 

 

# Mathematical Median of Cumulative Records

# Using chain() + statistics.median()

temp = list(chain(*test_list)) 

res = statistics.median(temp) 

 

# Printing result 

print("Median of Records is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [(1, 4, 5), (7, 8), (2, 4, 10)]
    Median of Records is : 4.5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

