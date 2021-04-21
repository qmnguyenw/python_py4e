Python | Accumulative index summation in tuple list



Sometimes, while working with data, we can have a problem in which we need to
find accumulative summation of each index in tuples. This problem can have
application in web development and competitive programming domain. Let’s
discuss certain way in which this problem can be solved.

 **Method : Usingaccumulate() + sum() + lambda + map() + tuple() + zip()**  
The combination of above functions can be used to solve this task. In this, we
pair the elements using zip(), the then we perform the sum of them and we
extend this to all elements using map(). The taking forward of sum is done
by using accumulate. The binding of all logic is done by lambda function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Accumulative index summation in tuple list

# Using accumulate() + sum() + lambda + map() + tuple() + zip()

from itertools import accumulate

 

# initialize list

test_list = [(3, 4, 5), (4, 5, 7), (1, 4,
10)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Accumulative index summation in tuple list

# Using accumulate() + sum() + lambda + map() + tuple() + zip()

res = list(accumulate(test_list, lambda i, j:
tuple(map(sum, zip(i, j)))))

 

# printing result

print("Accumulative index summation of tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 4, 5), (4, 5, 7), (1, 4, 10)]
    Accumulative index summation of tuple list : [(3, 4, 5), (7, 9, 12), (8, 13, 22)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

