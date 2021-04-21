Generating random number list in Python



Sometimes, in making programs for gaming or gambling, we come across the task
of creating the list all with random numbers. This task is to perform in
general using loop and appending the random numbers one by one. But there is
always a requirement to perform this in most concise manner. Let’s discuss
certain ways in which this can be done.

###  **Method #1 : Using list comprehension + randrange()**

The naive method to perform this particular task can be shortened using the
list comprehension. randrange function is used to perform the task of
generating the random numbers.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to generate random number list

# using list comprehension + randrange()

import random

# using list comprehension + randrange()

# to generate random number list

res = [random.randrange(1, 50, 1) for i in
range(7)]

# printing result

print ("Random number list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Random number list is : [21, 27, 23, 20, 21, 25, 15]
    
    
    
    
    
    
    

###  
**Method #2 : Using random.sample()**

This single utility function performs the exact required as asked by the
problem statement, it generated N no. of random numbers in a list in the
specified range and returns the required list.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to generate random number list

# using random.sample()

import random

# using random.sample()

# to generate random number list

res = random.sample(range(1, 50), 7)

# printing result

print ("Random number list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Random number list is : [8, 46, 45, 49, 15, 6, 31]
    
    
    
    
    
    
    

