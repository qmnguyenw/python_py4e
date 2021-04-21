Python – Ways to find Geometric Mean in List



While working with Python, we can have a problem in which we need to find
geometric mean of a list cumulative. This problem is common in Data Science
domain. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using loop + formula**  
The simpler manner to approach this problem is to employ the formula for
finding geometric mean and perform using loop shorthands. This is the most
basic approach to solve this problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Geometric Mean of List 

# using loop + formula 

import math

 

# initialize list 

test_list = [6, 7, 3, 9, 10, 15] 

 

# printing original list 

print("The original list is : " + str(test_list)) 

 

# Geometric Mean of List 

# using loop + formula 

temp = 1

for i in range(0, len(test_list)) : 

 temp = temp * test_list[i] 

temp2 = (float)(math.pow(temp, (1 / len(test_list)))) 

res = (float)(temp2) 

 

# printing result 

print("The geometric mean of list is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [6, 7, 3, 9, 10, 15]
    The geometric mean of list is : 7.443617568993922
    

**Method #2 : Usingstatistics.geometric_mean()**  
This task can also be performed using inbuilt function of geometric_mean().
This is new in Python versions >= 3.8.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Geometric Mean of List 

# using statistics.geometric_mean()

import statistics 

 

# initialize list 

test_list = [6, 7, 3, 9, 10, 15] 

 

# printing original list 

print("The original list is : " + str(test_list)) 

 

# Geometric Mean of List 

# using statistics.geometric_mean() 

res = statistics.geometric_mean(test_list, 1) 

 

# printing result 

print("The geometric mean of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [6, 7, 3, 9, 10, 15]
    The geometric mean of list is : 7.443617568993922
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

