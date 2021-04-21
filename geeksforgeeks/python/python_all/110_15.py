Python – Find Minimum Pair Sum in list



Sometimes, we need to find the specific problem of getting the pair which
yields the minimum sum, this can be computed by getting initial two elements
after sorting. But in some case, we don’t with to change the ordering of list
and perform some operation in the similar list without using extra space.
Let’s discuss certain ways in which this can be performed.

 **Method #1 : Using list comprehension +min() + combination() \+ lambda**  
This particular task can be performed using the combination of above functions
in which we use list comprehension to bind all the functionalities and min
function to get the minimum sum, combination function finds all sums
internally and lambda function is used to compute the sum.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Minimum Pair Sum 

# using list comprehension + min() + combinations() + lambda

from itertools import combinations

 

# initializing list

test_list = [3, 4, 1, 7, 9, 1]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + min() + combinations() + lambda

# Minimum Pair Sum 

res = min(combinations(test_list, 2), key = lambda sub:
abs(sub[0]-sub[1]))

 

# print result

print("The minimum sum pair is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 4, 1, 7, 9, 1]
    The minimum sum pair is : (1, 1)
    

**Method #2 : Using list comprehension +nsmallest() + combination() \+
lambda**  
This method has potential of not only finding a single minimum but also k
minimum sum pairs if required and uses nsmallest function instead of min
function to achieve this functionality.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Minimum Pair Sum 

# using list comprehension + nsmallest() + combinations() + lambda

from itertools import combinations

from heapq import nsmallest

 

# initializing list

test_list = [3, 4, 1, 7, 9, 8]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + nsmallest() + combinations() + lambda

# Minimum Pair Sum 

# computes 2 min sum pair

res = nsmallest(2, combinations(test_list, 2), key = lambda
sub: abs(sub[0] + sub[1]))

 

# print result

print("The minimum sum pair is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 4, 1, 7, 9, 8]
    The minimum sum pair is : [(3, 1), (4, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

