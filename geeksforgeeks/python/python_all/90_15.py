Python – Maximum Aggregation Pair in List



Sometimes, we need to find the specific problem of getting the pair which
yields the maximum sum, this can be computed by getting initial two elements
after sorting. But in some case, we don’t with to change the ordering of list
and perform some operation in the similar list without using extra space.
Let’s discuss certain ways in which this can be performed.

 **Method #1 : Using list comprehension +max() + combination() \+ lambda**  
This particular task can be performed using the combination of above functions
in which we use list comprehension to bind all the functionalities and max
function to get the maximum sum, combination function finds all sums
internally and lambda function is used to compute the sum.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximum Aggretation Pair in List

# using list comprehension + max() + combinations() + lambda 

from itertools import combinations 

 

# initializing list 

test_list = [3, 4, 1, 7, 9, 1] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# using list comprehension + max() + combinations() + lambda 

# Maximum Aggretation Pair in List

res = max(combinations(test_list, 2), key = lambda sub:
sub[0] + sub[1]) 

 

# print result 

print("The maximum sum pair is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [3, 4, 1, 7, 9, 1]
    The maximum sum pair is : (7, 9)
    

**Method #2 : Using list comprehension +nlargest() + combination() \+
lambda**  
This method has potential of not only finding a single maximum but also k
maximum sum pairs if required and uses nlargest function instead of max
function to achieve this functionality.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximum Aggretation Pair in List

# using list comprehension + nlargest() + combinations() + lambda 

from itertools import combinations 

from heapq import nlargest

 

# initializing list 

test_list = [3, 4, 1, 7, 9, 8] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# using list comprehension + nsmallest() + combinations() + lambda 

# Maximum Aggretation Pair in List

# computes 2 max sum pair 

res = nlargest(2, combinations(test_list, 2), key = lambda
sub: sub[0] + sub[1]) 

 

# print result 

print("The maximum sum pair is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 4, 1, 7, 9, 8]
    The maximum sum pair is : [(9, 8), (7, 9)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

