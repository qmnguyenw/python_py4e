Python – Constant Multiplication over List



While working with the python lists, we can come over a situation in which we
require to multiply constant to each element in the list. We possibly need to
iterate and multiply constant to each element but that would increase the line
of code. Let’s discuss certain shorthands to perform this task.

 **Method #1 : Using List Comprehension**  
List comprehension is just the short way to perform the task we perform using
the naive method. This is mainly useful to save time and also is best among
others when it comes to readability of the code.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Constant Multiplication over List

# using list comprehension

 

# initializing list 

test_list = [4, 5, 6, 3, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# using list comprehension

# Constant Multiplication over List

res = [x * K for x in test_list]

 

# printing result 

print ("The list after constant multiplcation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 3, 9]
    The list after constant multiplcation : [16, 20, 24, 12, 36]
    

**Method #2 : Usingmap() \+ operator.mul**  
This is similar to the above function but uses the operator.mul to multiply
each element to other element from the other list of K formed before applying
the map function. It multiplies the similar index elements of list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Constant Multiplication over List

# using map() + operator.mul

import operator

 

# initializing list 

test_list = [4, 5, 6, 3, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K list

K_list = [4] * len(test_list)

 

# using map() + operator.mul

# Constant Multiplication over List

res = list(map(operator.mul, test_list, K_list))

 

# printing result 

print ("The list after constant multiplication : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 3, 9]
    The list after constant multiplcation : [16, 20, 24, 12, 36]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

