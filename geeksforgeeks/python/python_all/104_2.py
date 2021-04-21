Python | Dictionary initialization with common dictionary



Sometimes, while working with dictionaries, we might have an utility in which
we need to initialize a dictionary with records values, so that they can be
altered later. This kind of application can occur in cases of memoizations in
general or competitive programming. Let’s discuss certain way in which this
task can be performed.

 **Method : Usingzip() + repeat()**  
The combination of these functions can be used to perform this particular
task. In this, the Dictionary value is attached to the keys repeated using the
repeat() by help of zip()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary initialization with common dictionary

# Using zip() + repeat()

from itertools import repeat

 

# initialization Dictionary 

test_dict = {'gfg' : 1, 'best' : 3}

 

# Using zip() + repeat()

# Dictionary initialization with common dictionary

res = dict(zip(range(4), repeat(test_dict)))

 

# printing result 

print("The dictionary with record values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The dictionary with record values : {0: {'gfg': 1, 'best': 3}, 1: {'gfg': 1, 'best': 3}, 2: {'gfg': 1, 'best': 3}, 3: {'gfg': 1, 'best': 3}}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

