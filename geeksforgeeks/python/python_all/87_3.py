Python – Closest Sum Pair in List



Sometimes, we desire to get the elements that sum to a particular element. But
in cases we are not able to find that, our aim changes to be one to find the
closest one. This can have application in many domains. Lets discuss certain
ways in which this task can be performed.

 **Method #1 : Using dictionary comprehension +max()**  
The combination of above functionalities can be used to perform this task. In
this, we perform the logic part in dictionary comprehension and closest pair
is extracted using max(). The list should be sorted to perform this method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Closest Sum Pair in List

# using dictionary comprehension + max()

 

# Initializing list

test_list = [7, 8, 10, 3, 18, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 12

 

# Closest Sum Pair in List

# using dictionary comprehension + max()

test_list.sort()

res = { i + j :(i, j) for i in test_list for j in
test_list if i != j and i + j < K}

res = max(res)

 

# printing result 

print ("The closest sum pair is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [7, 8, 10, 3, 18, 1]
    The closest sum pair is : 11
    

**Method #2 : Using loop +combinations()**  
This is yet another way in which this task can be performed. In this, we
iterate through the list, compute all possible pairs and return the closest
possible sum generated using min(). This return actual pairs.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Closest Sum Pair in List

# using loop + combinations

from itertools import combinations

 

# Initializing list

test_list = [7, 8, 10, 3, 18, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 12

 

# Closest Sum Pair in List

# using dictionary comprehension + max()

res = {}

for ele in combinations(test_list, 2):

 ele_sum = sum(ele)

 try:

 res[ele_sum].append(ele)

 except KeyError:

 res[ele_sum] = [ele]

res = res[min(res, key = lambda ele: abs(ele - K))]

 

# printing result 

print ("The closest sum pair is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [7, 8, 10, 3, 18, 1]
    The closest sum pair is : [(8, 3), (10, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

