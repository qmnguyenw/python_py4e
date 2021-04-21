Python | Consecutive chunks Product



Some of the classical problems in programming domain comes from different
categories and one among them is finding the product of subsets. This
particular problem is also common when we need to compute the product and
store consecutive group product value. Let’s try different approaches to this
problem in python language.

 **Method #1 : Using list comprehension + loop**  
The list comprehension can be used to perform the this particular task to
filter out successive groups and product explicit function can be used to get
the product of the filtered solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive chunks Product

# using list comprehension + loop

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initializing list

test_list = [4, 7, 8, 10, 12, 15, 13, 17,
14]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + loop

# Consecutive chunks Product

res = [ prod(test_list[x : x + 3]) for x in range(0,
len(test_list), 3)]

 

# printing result

print("The chunked product list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 7, 8, 10, 12, 15, 13, 17, 14]
    The chunked product list is : [224, 1800, 3094]
    

**Method #2 : Using loop + itertools.islice()**  
The task of slicing the list into chunks is done by islice method here and the
conventional task of getting the product is done by the explicit product
function as the above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive chunks Product

# using itertools.islice() + loop

import itertools

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initializing list

test_list = [4, 7, 8, 10, 12, 15, 13, 17,
14]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using itertools.islice() + loop

# Consecutive chunks Product

res = [prod(list(itertools.islice(test_list, i, i + 3))) for
i in range(0, len(test_list), 3)]

 

# printing result

print("The chunked product list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 7, 8, 10, 12, 15, 13, 17, 14]
    The chunked product list is : [224, 1800, 3094]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

