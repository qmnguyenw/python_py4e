Find Median of List in Python



Sometimes, while working with Python list we can have a problem in which we
need to find Median of list. This problem is quite common in the mathematical
domains and generic calculations. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Using loop +"~" operator**  
This task can be performed in brute force manner using the combination of
above functionalities. In this, we sort the list and the by using the property
of “~” operator to perform negation, we access the list from front and rear,
performing the required computation required for finding median.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Median of list

# Using loop + "~" operator

 

# initializing list

test_list = [4, 5, 8, 9, 10, 17]

 

# printing list

print("The original list : " + str(test_list))

 

# Median of list

# Using loop + "~" operator

test_list.sort()

mid = len(test_list) // 2

res = (test_list[mid] + test_list[~mid]) / 2

 

# Printing result

print("Median of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10, 17]
    Median of list is : 8.5
    

**

Method #2 : Usingstatistics.median()

**  
This is the most generic method to perform this task. In this we directly use
inbuilt function to perform the median of the list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Median of list

# Using statistics.median()

import statistics

 

# initializing list

test_list = [4, 5, 8, 9, 10, 17]

 

# printing list

print("The original list : " + str(test_list))

 

# Median of list

# Using statistics.median()

res = statistics.median(test_list)

 

# Printing result

print("Median of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10, 17]
    Median of list is : 8.5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

