Python | Incremental Records Product



Sometimes, while working with data, we can have a problem in which we need to
find accumulative product of each index in tuples. This problem can have
application in web development and competitive programming domain. Let’s
discuss certain way in which this problem can be solved.

 **Method : Usingaccumulate() \+ loop + lambda + map() + tuple() + zip()**  
The combination of above functions can be used to solve this task. In this, we
pair the elements using zip(), the then we perform the product of them and we
extend this to all elements using map(). The taking forward of product is done
by using accumulate. The binding of all logic is done by lambda function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Incremental Records Product

# Using accumulate() + loop + lambda + map() + tuple() + zip()

from itertools import accumulate

 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res

 

# initialize list

test_list = [(3, 4, 5), (4, 5, 7), (1, 4,
10)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Incremental Records Product

# Using accumulate() + loop + lambda + map() + tuple() + zip()

res = list(accumulate(test_list, lambda i, j:
tuple(map(prod, zip(i, j)))))

 

# printing result

print("Accumulative index product of tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 4, 5), (4, 5, 7), (1, 4, 10)]
    Accumulative index product of tuple list : [(3, 4, 5), (12, 20, 35), (12, 80, 350)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

