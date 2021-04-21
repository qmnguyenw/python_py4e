Python – Summation in Dual element Records List



Sometimes, while working with Records list, we can have problem in which we
perform the summation of dual tuple records and store it in list. This kind of
application can occur over various domains. Lets discuss certain ways in which
this task can be performed.

 **Method #1 : Using list comprehension**  
This is one of the way to solve this problem. In this we perform summation of
dual tuples in a list and iteration is performed inside comprehended list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Summation in Dual element Records List

# using list comprehension

 

# Initializing list

test_list = [(6, 7), (2, 4), (8, 9), (6,
2)]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# Summation in Dual element Records List

# using list comprehension

res = [ele[0] + ele[1] for ele in test_list]

 

# printing result 

print ("Summation pairs in tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(6, 7), (2, 4), (8, 9), (6, 2)]
    Summation pairs in tuple list : [13, 6, 17, 8]
    

**Method #2 : Usingreduce() + add()**  
This is yet another way to perform this task. In this, we iterate through the
list and perform summation using reduce() and add() respectively.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Summation in Dual element Records List

# using reduce() + add()

from operator import add

from functools import reduce

 

# Initializing list

test_list = [(6, 7), (2, 4), (8, 9), (6,
2)]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# Summation in Dual element Records List

# using reduce() + add()

res = [reduce(add, sub, 0) for sub in test_list]

 

# printing result 

print ("Summation pairs in tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(6, 7), (2, 4), (8, 9), (6, 2)]
    Summation pairs in tuple list : [13, 6, 17, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

