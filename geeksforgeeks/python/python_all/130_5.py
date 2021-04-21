Python | Summation of integers in heterogenous list



Sometimes, while working with Python, we can come across a problem in which we
require to find the sum of list. This problem is easier to solve. But this can
get complex in case we have mixture of data types to go along with it. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using Type casting + Exception Handling**  
We can employ a brute force method to type caste each element and catch the
exception if any occurs. This can ensure that only integers are added to sum
and hence can solve the problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of integers in heterogenous list

# using type caste and exception handling

 

# initializing list

test_list = [5, 6, "gfg", 8, (5, 7), 'is',
9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Summation of integers in heterogenous list

# using type caste and exception handling

res = 0

for ele in test_list:

 try:

 res += int(ele)

 except :

 pass

 

# printing result 

print("Summation of integers in list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 'gfg', 8, (5, 7), 'is', 9]
    Summation of integers in list : 28
    

**Method #2 : Usingsum() + isinstance()**  
This problem can also be solved using the inbuilt function of sum() and it
also supports the instance filter using isinstance() which can be feeded
with integer and hence solve the problem.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of integers in heterogenous list

# using sum() + isinstance()

 

# initializing list

test_list = [5, 6, "gfg", 8, (5, 7), 'is',
9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Summation of integers in heterogenous list

# using sum() + isinstance()

res = sum(filter(lambda i: isinstance(i, int),
test_list))

 

# printing result 

print("Summation of integers in list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 'gfg', 8, (5, 7), 'is', 9]
    Summation of integers in list : 28
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

