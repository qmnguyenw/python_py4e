Python | Variance of List



While working with Python, we can have a problem in which we need to find
variance of a list cumulative. This problem is common in Data Science domain.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using loop + formula**  
The simpler manner to approach this problem is to employ the formula for
finding variance and perform using loop shorthands. This is the most basic
approach to solve this problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Variance of List

# using loop + formula

 

# initialize list

test_list = [6, 7, 3, 9, 10, 15]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Variance of List

# using loop + formula

mean = sum(test_list) / len(test_list)

res = sum((i - mean) ** 2 for i in test_list) /
len(test_list)

 

# printing result

print("The variance of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [6, 7, 3, 9, 10, 15]
    The variance of list is : 13.888888888888891
    

**Method #2 : Usingstatistics.variance()**  
This task can also be performed using inbuilt function of variance().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Variance of List

# using statistics.variance

import statistics 

 

# initialize list

test_list = [6, 7, 3, 9, 10, 15]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Variance of List

# using statistics.variance

res = statistics.variance(test_list)

 

# printing result

print("The variance of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [6, 7, 3, 9, 10, 15]
    The variance of list is : 13.888888888888891
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

