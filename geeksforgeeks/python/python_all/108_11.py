Python | Matrix Product



Getting the product of list is quite common problem and has been dealt with
and discussed many times, but sometimes, we require to better it and total
product, i.e. including those of nested list as well. Let’s try and get the
total product and solve this particular problem.

 **Method #1 : Using list comprehension + loop**  
We can solve this problem using the list comprehension as a potential
shorthand to the conventional loops that we may use to perform this particular
task. We just iterate and product the nested list and at end return the
cumulative product using function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Matrix Product

# Using list comprehension + loop

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initializing list

test_list = [[1, 4, 5], [7, 3], [4], [46,
7, 3]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + loop

# Matrix Product

res = prod([ele for sub in test_list for ele in sub])

 

# print result

print("The total element product in lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
    The total element product in lists is : 1622880
    

**Method #2 : Usingchain() \+ loop**  
This particular problem can also be solved using the chain function instead of
list comprehension in which we use the conventional function to perform
product.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Matrix Product

# Using chain() + loop

from itertools import chain

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initializing list

test_list = [[1, 4, 5], [7, 3], [4], [46,
7, 3]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using chain() + loop

# Matrix Product

res = prod(list(chain(*test_list)))

 

# print result

print("The total element product in lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
    The total element product in lists is : 1622880
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

