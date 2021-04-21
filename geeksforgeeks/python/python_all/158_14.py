Python | Sum two unequal length lists in cyclic manner



Given two unequal length lists, the task is to add elements of two list such
that when elements of smaller list are over, add elements in a circular manner
till all element of the larger list is iterated.

Let’s discuss different ways we can do this task.

 **Method #1 : Using Iteratools and zip**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to add two different

# length lists in cyclic manner

 

# Importing

from itertools import cycle

 

# List initialization

list1 = [150, 177, 454, 126]

list2 = [9, 44, 2, 168, 66, 80, 123, 6,
180, 184]

 

# Using zip

output = [x + y for x, y in zip(cycle(list1), list2)]

 

# Printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [159, 221, 456, 294, 216, 257, 577, 132, 330, 361]
    

  
**Method #2 : Using Iteratools and starmap**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to add two different

# length lists in cyclic manner

 

# Importing

from itertools import starmap, cycle

from operator import add

 

# List initialization

list1 = [150, 177, 454, 126]

list2 = [9, 44, 2, 168, 66, 80, 123, 6,
180, 184]

 

# Using starmap

output = list(starmap(add, zip(cycle(list1), list2)))

 

# Print output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [159, 221, 456, 294, 216, 257, 577, 132, 330, 361]
    

  
**Method #3 : Using List comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to add two different

# length lists in cyclic manner

 

# List initialization

list1 = [150, 177, 454, 126]

list2 = [9, 44, 2, 168, 66, 80, 123, 6,
180, 184]

 

# List comprehension

output = [list1[i % len(list1)]+list2[i]

 for i in range(len(list2))]

 

# Printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [159, 221, 456, 294, 216, 257, 577, 132, 330, 361]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

