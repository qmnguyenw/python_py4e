Python | Remove duplicates based on Kth element tuple list



Sometimes, while working with records, we may have a problem in which we need
to remove duplicates based on Kth element of tuple in list. This problem has
application in domains which uses records as input. Let’s discuss certain ways
in which this problem can be solved.

 **Method #1 : Using loop**  
This is a brute force method to perform this particular task. In this, we
check for the Kth index of tuple and add to a set to keep record. If that
value is already in the memory set, we discard it from result as it’s
duplicate.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove duplicates based on Kth element tuple list

# Using loop

 

# initialize list 

test_list = [(3, 1, 5), (1, 3, 6), (2, 1,
7),

 (5, 2, 8), (6, 3, 0)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize K 

K = 1

 

# Remove duplicates based on Kth element tuple list

# Using loop

temp = set() 

res = []

for ele in test_list:

 if ele[K] not in temp:

 res.append(ele)

 temp.add(ele[K])

 

# printing result

print("The list after removal of K based duplicates : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [(3, 1, 5), (1, 3, 6), (2, 1, 7), (5, 2, 8), (6, 3,
> 0)]  
> The list after removal of K based duplicates : [(3, 1, 5), (1, 3, 6), (5, 2,
> 8)]

  

  

**Method #2 : Usingreduce() + lambda + keys()**

In this method, we perform the task of filtering using reduce() + lambda,
and decide to append or not using the extracted keys using keys(). If key
has already occurred, its discarded otherwise added.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove duplicates based on Kth element tuple list

# Using reduce() + lambda + keys()

from functools import reduce

 

# initialize list 

test_list = [(3, 1), (1, 3), (3, 2), (5,
2), (5, 3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize K 

K = 0

 

# Remove duplicates based on Kth element tuple list

# Using reduce() + lambda + keys()

res = reduce(lambda sub, ele : ele[K] in dict(sub).keys() 

 and sub or sub + [ele], test_list, [])

 

# printing result

print("The list after removal of K based duplicates : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [(3, 1), (1, 3), (3, 2), (5, 2), (5, 3)]  
> The list after removal of K based duplicates : [(3, 1), (1, 3), (5, 2)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

