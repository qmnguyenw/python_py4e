Python – Minimum Product Pair in List



Sometimes, we need to find the specific problem of getting the pair which
yields the minimum product, this can be solved by sorting and getting the
first and second elements of the list. But in some case, we don’t with to
change the ordering of list and perform some operation in the similar list
without using extra space. Let’s discuss certain ways in which this can be
performed.

 **Method #1 : Using list comprehension + min() + combination() \+ lambda**  
This particular task can be performed using the combination of above functions
in which we use list comprehension to bind all the functionalities and min
function to get the minimum product, combination function finds all product
internally and lambda function is used to compute the product.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Minimum Product Pair in List

# using list comprehension + min() + combinations() + lambda

from itertools import combinations

 

# initializing list

test_list = [3, 4, 1, 7, 9, 1]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + min() + combinations() + lambda

# Minimum Product Pair in List

res = min(combinations(test_list, 2), key = lambda sub:
sub[0] * sub[1])

 

# print result

print("The minimum product pair is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 4, 1, 7, 9, 1]
    The minimum product pair is : (1, 1)
    

**Method #2 : Using list comprehension +nsmallest() + combination() \+
lambda**  
This method has potential of not only finding a single minimum but also k
minimum product pairs if required and uses nsmallest function instead of min
function to achieve this functionality.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Minimum Product Pair in List

# using list comprehension + nsmallest() + combinations() + lambda

from itertools import combinations

from heapq import nsmallest

 

# initializing list

test_list = [3, 4, 1, 7, 9, 8]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + nsmallest() + combinations() + lambda

# Minimum Product Pair in List

res = nsmallest(2, combinations(test_list, 2), key = lambda
sub: sub[0] * sub[1])

 

# print result

print("The minimum product pair is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 4, 1, 7, 9, 8]
    The minimum product pair is : [(3, 1), (4, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

