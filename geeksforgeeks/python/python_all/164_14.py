Python | Prefix Sum Subarray till False value



The prefix array is quite famous in the programming practice. This article
would discuss a variation of this scheme. This deals with the cumulative list
sum till a False value, and again starts cumulation from the occurrence of
True value. Let’s discuss certain ways in which this can be performed.

 **Method #1 : Using Naive Method**  
In the naive method, we just construct the new list comprising of the
summation of prev. value of list until 0 and restarts the procedure once a
non-zero value is encountered.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Prefix Sum Subarray till False value 

# using naive method 

 

# initializing list of lists

test_list = [1, 3, 4, 0, 4, 5, 0, 7,
8]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Prefix Sum Subarray till False value 

# using naive method

for i in range(1, len(test_list)):

 if test_list[i]: 

 test_list[i] += test_list[i - 1]

 

# printing result

print ("The computed modified new list : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 3, 4, 0, 4, 5, 0, 7, 8]
    The computed modified new list : [1, 4, 8, 0, 4, 9, 0, 7, 15]
    

  
**Method #2 : Usingfrom_iterable() + accumulate() + groupby()**  
The above three functions combine together to perform this particular task. In
this, the accumulate function performs the task of addition of elements,
groupby function groups the non-zero values and the result is combined by the
from_iterable function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Prefix Sum Subarray till False value 

# from_iterable() + accumulate() + groupby()

from itertools import groupby, accumulate, chain

 

# initializing list of lists

test_list = [1, 3, 4, 0, 4, 5, 0, 7,
8]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Prefix Sum Subarray till False value 

# from_iterable() + accumulate() + groupby()

res = list(chain.from_iterable(accumulate(j) 

 for i, j in groupby(test_list, bool)))

 

# printing result

print ("The computed modified new list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 3, 4, 0, 4, 5, 0, 7, 8]
    The computed modified new list : [1, 4, 8, 0, 4, 9, 0, 7, 15]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

