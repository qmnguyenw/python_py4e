Python – Sum of different length Lists of list



Getting the sum of list is quite common problem and has been dealt with and
discussed many times, but sometimes, we require to better it and total sum,
i.e. including those of nested list as well. Let’s try and get the total sum
and solve this particular problem.

 **Method #1 : Using list comprehension +sum()**  
We can solve this problem using the list comprehension as a potential
shorthand to the conventional loops that we may use to perform this particular
task. We just iterate and sum the nested list and at end return the cumulative
sum using sum function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sum of Uneven Lists of list

# Using list comprehension + sum()

 

# initializing list

test_list = [[1, 4, 5], [7, 3], [4], [46,
7, 3]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + sum()

# Sum of Uneven Lists of list

res = sum([ele for sub in test_list for ele in sub])

 

# print result

print("The total element sum in lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
    The total element sum in lists is : 80
    

**Method #2 : Usingchain() + sum()**  
This particular problem can also be solved using the chain function instead of
list comprehension in which we use the conventional sum function to check the
sum.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sum of Uneven Lists of list

# Using chain() + sum()

from itertools import chain

 

# initializing list

test_list = [[1, 4, 5], [7, 3], [4], [46,
7, 3]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using chain() + sum()

# Sum of Uneven Lists of list

res = sum(list(chain(*test_list)))

 

# print result

print("The total element sum in lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
    The total element sum in lists is : 80
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

