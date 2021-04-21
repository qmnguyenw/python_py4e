Python | Average of Float Numbers



While working with Python, we can have a problem in which we need to find mean
of a list cumulative with float elements. This problem is common in Data
Science domain. Let’s discuss certain ways in which this problem can be
solved.

 **Method #1 : Using loop + formula**  
The simpler manner to approach this problem is to employ the formula for
finding mean and perform using loop shorthands. This is the most basic
approach to solve this problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Average of Float Numbers 

# using loop + formula 

import math

 

# initialize list 

test_list = [6.1, 7.2, 3.3, 9.4, 10.6, 15.7] 

 

# printing original list 

print("The original list is : " + str(test_list)) 

 

# Average of Float Numbers

# using loop + formula 

sum = 0

for ele in test_list:

 sum += ele

res = sum / len(test_list)

 

# printing result 

print("The mean of float list elements is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [6.1, 7.2, 3.3, 9.4, 10.6, 15.7]
    The mean of float list elements is : 8.716666666666667
    

**Method #2 : Usingstatistics.fmean()**  
This task can also be performed using inbuilt function of fmean(). This is new
in Python versions >= 3.8.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Average of Float Numbers

# using statistics.fmean() 

import statistics 

 

# initialize list 

test_list = [6.1, 7.2, 3.3, 9.4, 10.6, 15.7] 

 

# printing original list 

print("The original list is : " + str(test_list)) 

 

# Average of Float Numbers

# using statistics.fmean() 

res = statistics.fmean(test_list) 

 

# printing result 

print("The mean of float list elements is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [6.1, 7.2, 3.3, 9.4, 10.6, 15.7]
    The mean of float list elements is : 8.716666666666667
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

