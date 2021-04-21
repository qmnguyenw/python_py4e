Python | Prefix sum list



Nowadays, especially in the field of competitive programming, the utility of
computing prefix sum is quite popular and features in many problems. Hence,
having a one-liner solution to it would possess a great help. Let’s discuss
certain way in which this problem can be solved.

 **Method #1: Using list comprehension + sum() + list slicing**

This problem can be solved using the combination of above two functions in
which we use list comprehension to extend logic to each element, sum function
to get the sum along, slicing is used to get sum till the particular index.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# prefix sum list

# using list comprehension + sum() + list slicing 

 

# initializing list

test_list = [3, 4, 1, 7, 9, 1]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + sum() + list slicing

# prefix sum list

res = [sum(test_list[ : i + 1]) for i in
range(len(test_list))]

 

# print result

print("The prefix sum list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 4, 1, 7, 9, 1]
    The prefix sum list is : [3, 7, 8, 15, 24, 25]
    

  
**Method #2:** Using accumulate(iterable) method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# function to find cumulative sum of list

from itertools import accumulate 

 

def cumulativeSum(lst): 

 print (list(accumulate(lst))) 

 

# Driver program 

if __name__ == "__main__": 

 lst = [3, 4, 1, 7, 9, 1]

 cumulativeSum(lst)   
  
---  
  
__

__

**Output:**

    
    
    [3, 7, 8, 15, 24, 25]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

