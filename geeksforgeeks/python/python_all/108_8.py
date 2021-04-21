Python | Sliced Product in List



Accessing elements in a list has many types and variations. These are an
essential part of Python programming and one must know to perform the same.
This article discusses ways to fetch the initial K elements and do its
multiplication. Let’s discuss a certain solution to perform this task.

 **Method #1 : Using list slicing + loop**  
This problem can be performed in 1 line rather than using a loop using the
list slicing functionality provided by Python and then using a loop to perform
the product.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sliced Product in List

# using list slicing + loop

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initializing list 

test_list = [4, 5, 2, 6, 7, 8, 10] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# initializing K 

K = 5

 

# Sliced Product in List

# using list slicing + loop

res = prod(test_list[:K])

 

# print result 

print("The first K elements product of list is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [4, 5, 2, 6, 7, 8, 10]
    The first K elements product of list is : 1680
    

**Method #2 : Usingislice() \+ loop**  
The inbuilt funtions can also be used to perform this particular task. The
islice function can be used to get the sliced list and then prod() can be
employed to perform product.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sliced Product in List

# using islice() + loop

from itertools import islice 

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initializing list 

test_list = [4, 5, 2, 6, 7, 8, 10] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# initializing K 

K = 5

 

# Sliced Product in List

# using islice() + loop

res = list(islice(test_list, 0, K)) 

res = prod(res)

 

# print result 

print("The first K elements product of list is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [4, 5, 2, 6, 7, 8, 10]
    The first K elements product of list is : 1680
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

