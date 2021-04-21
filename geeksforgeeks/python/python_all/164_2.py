Python | Print the common elements in all sublists



Given a list of lists, the task is to find the elements which are common in
all sublist.

There are various approaches to do this task. Let’s discuss the approaches one
by one.

 **Method #1:** Using set

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find duplicate element in all

# sublist from list of list

 

# List of list initialization

Input = [ [10, 20, 30, 40],

 [30, 40, 60, 70],

 [20, 30, 40, 60, 70],

 [30, 40, 80, 90], ]

 

Output = set(Input[0])

for l in Input[1:]:

 Output &= set(l)

 

# Converting to list

Output = list(Output)

 

# Printing answer

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [40, 30]
    

  
**Method #2:** Using reduce and map

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find duplicate element in all

# sublist from list of list

import operator

from functools import reduce

 

# List of list initialization

Input = [ [10, 20, 30, 40],

 [30, 40, 60, 70],

 [20, 30, 40, 60, 70], 

 [30, 40, 80, 90], ]

 

# using reduce and map

out = reduce(operator.iand, map(set, Input))

 

# Converting into list

out = list(out)

 

# Printing output

print(out)  
  
---  
  
 __

 __

 **Output:**

    
    
    [40, 30]
    

  
**Method #3:** Using set.intersection

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find duplicate element in all

# sublist from list of list

 

# importing reduce 

from functools import reduce

 

# function for set intersection

def func(a, b):

 return list(set(a).intersection(set(b)))

 

# List of list initialization

Input = [ [10, 20, 30, 40],

 [30, 40, 60, 70],

 [20, 30, 40, 60, 70], 

 [30, 40, 80, 90], ]

 

# using reduce and set.intersection

out = reduce(func, Input)

 

# Printing output

print(out)  
  
---  
  
 __

 __

 **Output:**

    
    
    [40, 30]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

