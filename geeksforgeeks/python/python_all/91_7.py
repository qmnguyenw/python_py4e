Python | Arbitrary List Product



Sometimes, in making programs for gaming or gambling, we come across the task
of creating the list all with arbitrary numbers and perform its product. This
task has to performed in general using loop and appending the arbitrary
numbers one by one and then performing product. But there is always
requirement to perform this in most concise manner. Lets discuss certain ways
in which this can be done.

 **Method #1 : Using list comprehension +randrange() \+ loop**  
The naive method to perform this particular task can be shortened using the
list comprehension. randrange function is used to perform the task of
generating the random numbers. The task of performing product is done using
loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Arbitrary List Product

# using list comprehension + randrange() + loop

import random

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# using list comprehension + randrange() + loop

# Arbitrary List Product

res = prod([random.randrange(1, 50, 1) for i in
range(7)])

 

# printing result

print ("Arbitrary number product list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Arbitrary number product list is : 1182384000
    

**Method #2 : Usingrandom.sample() + loop**  
This single utility function performs the exact required as asked by the
problem statement, it generated N no. of arbitrary numbers in a list in the
specified range and returns the required list. The task of performing product
is done using loop.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Arbitrary List Product

# using random.sample() + loop

import random

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# using random.sample() + loop

# Arbitrary List Product

res = prod(random.sample(range(1, 50), 7))

 

# printing result

print ("Arbitrary number product list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Arbitrary number product list is : 1182384000
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

