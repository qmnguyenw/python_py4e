Python | Remove trailing empty elements from given list



Given a list, the task is to remove trailing _None_ values from last of the
list. Let’s discuss a few methods to solve the given task.

 **Examples:**

    
    
     **Input:** [1, 2, 3, 4, None, 76, None, None]
    **Output:** [1, 2, 3, 4, None, 76]
    
    **Input:** [1, 2, None, None, None, None, None, 5]
    **Output:** [1, 2, None, None, None, None, None, 5]

 **Method #1: Using naive method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to remove trailing None

# elements from lists

 

# initialising lists

ini_list = [1, 2, 3, 4, None, 76, None,
None, None]

 

# printing initial dictionary

print ("initial dictionary", str(ini_list))

 

# code toremove trailing None values

# from lists

while not ini_list[-1]:

 ini_list.pop()

 

# printing result

print ("resultant list", str(ini_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial dictionary [1, 2, 3, 4, None, 76, None, None, None]
    resultant list [1, 2, 3, 4, None, 76]
    

  
**Method #2: Usingitertools.dropwhile()**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to remove trailing None

# elements from lists

 

from itertools import dropwhile

# initialising lists

ini_list = [1, 2, 3, 4, None, 76, None,
None, None]

 

# printing initial dictionary

print ("initial dictionary", str(ini_list))

 

# code toremove trailing None values

# from lists

res = list(reversed(tuple(dropwhile(lambda x: x is
None, 

 reversed(ini_list)))))

 

# printing result

print ("resultant list", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial dictionary [1, 2, 3, 4, None, 76, None, None, None]
    resultant list [1, 2, 3, 4, None, 76]
    

**Method #3: Usingitertools.takewhile()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to remove trailing None

# elements from lists

 

from itertools import takewhile

 

# initialising lists

ini_list = [1, 2, 3, 4, None, 76, None,
None, None]

 

# printing initial dictionary

print ("initial dictionary", str(ini_list))

 

# code toremove trailing None values

# from lists

res = ini_list[:-len(list(takewhile(lambda x: x ==
None,

 reversed(ini_list))))]

# printing result

print ("resultant list", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial dictionary [1, 2, 3, 4, None, 76, None, None, None]
    resultant list [1, 2, 3, 4, None, 76]
    

  
**Method #4: Using enumerate and list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to remove trailing None

# elements from lists

 

 

# initialising lists

ini_list = [1, 2, 3, 4, None, 76, None,
None, None]

 

# printing initial dictionary

print ("initial dictionary", str(ini_list))

 

# code toremove trailing None values

# from lists

res = [x for n, x in enumerate(ini_list)

 if any(y is not None for y in ini_list[n:])]

 

# printing result

print ("resultant list", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial dictionary [1, 2, 3, 4, None, 76, None, None, None]
    resultant list [1, 2, 3, 4, None, 76]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

