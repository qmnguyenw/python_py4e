Python – Summation Matrix columns



Sometimes, we are encountered with such problem in which we need to find the
sum of each column in a matrix i.e sum of each index in list of lists. This
kind of problem is quite common and useful in competitive programming. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Usingsum() + list comprehension + zip()**  
The combination of above methods are required to solve this particular
problem. The sum function is used to get the required sum value and zip
function provides the combination of like indices and then list is created
using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Summation of each column in Matrix

# using sum() + list comprehension + zip()

 

# initializing list

test_list = [[3, 7, 6], [1, 3, 5], [9, 3,
2]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using sum() + list comprehension + zip()

# Summation of each column in Matrix

res = [sum(idx) for idx in zip(*test_list)]

 

# print result

print("The Summation of each index list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 7, 6], [1, 3, 5], [9, 3, 2]]
    The Summation of each index list is : [13, 13, 13]
    

**Method #2 : Usingmap() + sum() + zip()**  
This works in almost similar way as the above method, but the difference is
just that we use map function to build the sum list rather than using list
comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Summation of each column in Matrix

# using map() + sum() + zip()

 

# initializing list

test_list = [[3, 7, 6], [1, 3, 5], [9, 3,
2]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using map() + sum() + zip()

# Summation of each column in Matrix

res = list(map(sum, zip(*test_list)))

 

# print result

print("The Summation of each index list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 7, 6], [1, 3, 5], [9, 3, 2]]
    The Summation of each index list is : [13, 13, 13]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

