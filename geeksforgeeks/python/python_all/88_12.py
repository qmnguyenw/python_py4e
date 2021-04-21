Python – Matrix elements Frequencies Counter



Sometimes, while working with python Matrix, we can have a problem in which we
need to find frequencies of all elements in Matrix. This kind of problem can
have application in many domains. Lets discuss certain ways in which this task
can be performed.

 **Method #1 : UsingCounter() + sum() + map()**  
The combination of above methods can be used to perform this task. In this, we
perform task of counting elements using Counter() and extending the logic to
each row is performed using sum() and map().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Matrix elements Frequencies Counter

# using Counter() + sum() + map()

from collections import Counter

 

# Initializing list

test_list = [[4, 5, 6], [2, 4, 5], [6, 7,
5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Matrix elements Frequencies Counter

# using Counter() + sum() + map()

res = dict(sum(map(Counter, test_list), Counter()))

 

# printing result 

print ("The frequencies dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
    The frequencies dictionary is : {2: 1, 4: 2, 5: 3, 6: 2, 7: 1}
    

**Method #2 : Usingchain() + Counter()**  
The combination of above functions can be used to perform this task. In this,
we flatten the matrix using chain() and compute frequency using Counter().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Matrix elements Frequencies Counter

# using Counter() + chain()

from collections import Counter

import itertools

 

# Initializing list

test_list = [[4, 5, 6], [2, 4, 5], [6, 7,
5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Matrix elements Frequencies Counter

# using Counter() + chain()

res = dict(Counter(itertools.chain(*test_list)))

 

# printing result 

print ("The frequencies dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
    The frequencies dictionary is : {2: 1, 4: 2, 5: 3, 6: 2, 7: 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

