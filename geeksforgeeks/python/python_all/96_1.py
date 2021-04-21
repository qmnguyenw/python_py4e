Python – Random Numbers Summation



Sometimes, in making programs for gaming or gambling, we come across the task
of creating the list all with random numbers and perform its summation. This
task has to performed in general using loop and appending the random numbers
one by one and then performing sum. But there is always requirement to perform
this in most concise manner. Lets discuss certain ways in which this can be
done.

 **Method #1 : Using list comprehension +randrange() + sum()**  
The naive method to perform this particular task can be shortened using the
list comprehension. randrange function is used to perform the task of
generating the random numbers. The task of performing sum is done using sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Random Numbers Summation

# using list comprehension + randrange() + sum()

import random

 

# using list comprehension + randrange() + sum()

# Random Numbers Summation

res = sum([random.randrange(1, 50, 1) for i in
range(7)])

 

# printing result

print ("Random number summation list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Random number summation list is : 187
    

**Method #2 : Usingrandom.sample() + sum()**  
This single utility function performs the exact required as asked by the
problem statement, it generated N no. of random numbers in a list in the
specified range and returns the required list. The task of performing sum is
done using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Random Numbers Summation

# using random.sample() + sum()

import random

 

# using random.sample() + sum()

# Random Numbers Summation

res = sum(random.sample(range(1, 50), 7))

 

# printing result

print ("Random number summation list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Random number summation list is : 187
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

