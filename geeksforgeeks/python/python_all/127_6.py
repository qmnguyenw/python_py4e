Python | Remove random element from list



Sometimes, while working with Python lists, we can have a problem or part of
it, in which we desire to convert a list after deletion of some random
element. This can have it’s application in gaming domain or personal projects.
Let’s discuss certain way in which this task can be done.

 **Method : Usingrandrange() + pop()**  
In this, we just combine the functionality of above functions into one and
achieve this task. The random element is chosen by randrange() and then is
accessed and removed from the list using pop()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove random element from list

# Using randrange() + pop()

import random

 

# initializing list 

test_list = [6, 4, 8, 9, 10]

 

# printing list 

print("The original list : " + str(test_list))

 

# Remove random element from list

# Using randrange() + pop()

test_list.pop(random.randrange(len(test_list)))

 

# Printing result

print("List after removal of random number : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [6, 4, 8, 9, 10]
    List after removal of random number : [6, 4, 8, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

