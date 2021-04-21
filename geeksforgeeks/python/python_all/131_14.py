Python | Get random dictionary pair



Sometimes, while working with dictionaries, we can have a situation in which
we need to find a random pair from dictionary. This type of problem can come
in games such as lotteries etc. Let’s discuss certain ways in which this task
can be performed.

 **Method #1 : Usingrandom.choice() + list() + items()**

The combination of above methods can be used to perform this task. The
choice function performs the task of random value selection and list
method is used to convert the pairs accessed using items() into a list over
which choice function can work.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get random dictionary pair in dictionary

# Using random.choice() + list() + items()

import random

 

# Initialize dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Get random dictionary pair in dictionary

# Using random.choice() + list() + items()

res = key, val = random.choice(list(test_dict.items()))

 

# printing result

print("The random pair is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Gfg': 1, 'best': 3, 'is': 2}
    The random pair is : ('is', 2)
    

  

  

**Method #2 : Usingpopitem()**  
This function is generally used to remove an item from dictionary and remove
it. The logic why this function can be used to perform this task is that as
ordering in dictionary is random, any pair can be popped hence random.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get random dictionary pair in dictionary

# Using popitem()

 

# Initialize dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Get random dictionary pair in dictionary

# Using popitem()

res = test_dict.popitem()

 

# printing result

print("The random pair is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Gfg': 1, 'best': 3, 'is': 2}
    The random pair is : ('is', 2)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

