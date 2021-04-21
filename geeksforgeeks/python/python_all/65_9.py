Python – N Random Tuples list



Sometimes, while working with Python records, we can have a problem in which
we need to construct random tuple list. This can have application in many
domains using gaming and day-day programming. Let’s discuss certain ways in
which this task can be performed.

>  **Input** :  
> N = 4  
> R = 6  
>  **Output** : [(5, 6), (1, 0), (1, 3), (2, 3)]  
>  **Input** :  
> N = 8  
> R = 4  
>  **Output** : [(2, 3), (4, 1), (2, 0), (4, 3), (4, 2), (0, 2), (1, 4), (0,
> 1)]

 **Method #1 : Using list comprehension +sample()**  
This is one of the ways in which this task can be performed. In this, random
number generation takes place using sample() which, when given pool of numbers
extracts random numbers for forming pairs, which are paired using list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# N Random Tuples list

# Using list comprehension + sample()

import random

 

# initializing N

N = 5

 

# initializing Tuple element range 

R = 10

 

# N Random Tuples list

# Using list comprehension + sample()

res = [divmod(ele, R + 1) for ele in
random.sample(range((R + 1) * (R + 1)), N)]

 

# printing result 

print("The N random tuples : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The N random tuples : [(2, 5), (6, 10), (4, 7), (10, 2), (2, 2)]
    

  

  

**Method #2 : Usingproduct() + sample()**  
The combination of above functions can be used to solve this problem. In this,
we perform task of producing numbers in a range using product() and sample()
is used to extract N random numbers from them.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# N Random Tuples list

# Using product() + sample()

import random

import itertools

 

# initializing N

N = 5

 

# initializing Tuple element range 

R = 10

 

# N Random Tuples list

# Using product() + sample()

res = random.sample(list(itertools.product(range(R + 1),
repeat = 2)), N)

 

# printing result 

print("The N random tuples : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The N random tuples : [(2, 5), (6, 10), (4, 7), (10, 2), (2, 2)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

