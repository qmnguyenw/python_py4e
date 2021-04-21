Python | How to get unique elements in nested tuple



Sometimes, while working with tuples, we can have a problem in which we have
nested tuples and we need to extract elements that occur singly, i.e are
elementary. This kind of problem can have applications in many domains. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Using nested loop +set()**  
The above 2 functionalities can be used to solve this particular problem. In
this, we iterate each nested tuple and add to set if element has occurred for
first time and check for each element before adding.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique elements in nested tuple

# Using nested loop + set()

 

# initialize list

test_list = [(3, 4, 5), (4, 5, 7), (1,
4)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Unique elements in nested tuple

# Using nested loop + set()

res = []

temp = set()

for inner in test_list:

 for ele in inner:

 if not ele in temp:

 temp.add(ele)

 res.append(ele)

 

# printing result

print("Unique elements in nested tuples are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 4, 5), (4, 5, 7), (1, 4)]
    Unique elements in nested tuples are : [3, 4, 5, 7, 1]
    

**Method #2 : Usingset() + from_iterable()**  
The combo of above functionalities can be used to solve this. This is done is
2 steps, first, we flatten the nested list and then find distincts using
set().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique elements in nested tuple

# Using from_iterable() + set()

from itertools import chain

 

# initialize list

test_list = [(3, 4, 5), (4, 5, 7), (1,
4)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Unique elements in nested tuple

# Using from_iterable() + set()

res = list(set(chain.from_iterable(test_list)))

 

# printing result

print("Unique elements in nested tuples are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 4, 5), (4, 5, 7), (1, 4)]
    Unique elements in nested tuples are : [1, 3, 4, 5, 7]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

