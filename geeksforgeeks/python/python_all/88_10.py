Python – Generate random number except K in list



Sometimes, while working with python, we can have a problem in which we need
to generate random number. This seems quite easy but sometimes we require a
slight variation of it. That is, we require to generate random number from a
list except K. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingchoice() \+ list comprehension**  
The combination of above functions can be used to perform this task. In this,
we first filter out the numbers except K using list comprehension and then
feed that list to choice() for random number generation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Generate random number except K in list

# using choice() + list comprehension

import random

 

# Initializing list 

test_list = [4, 7, 8, 4, 6, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 4

 

# Generate random number except K in list

# using choice() + list comprehension

res = random.choice([ele for ele in test_list if ele !=
K])

 

# printing result 

print ("The random number except K is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 7, 8, 4, 6, 10]
    The random number except K is : 8
    

**Method #2 : Usingfilter() + lambda + choice()**  
This is yet another way in which this task can be performed. In this, we
perform method of creating new list using filter and lambda.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Generate random number except K in list

# using choice() + filter() + lambda

import random

 

# Initializing list 

test_list = [4, 7, 8, 4, 6, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 4

 

# Generate random number except K in list

# using choice() + filter() + lambda

res = random.choice(list(filter(lambda ele: ele != K,
test_list)))

 

# printing result 

print ("The random number except K is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 7, 8, 4, 6, 10]
    The random number except K is : 8
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

