Python | Merge elements of sublists



Given two lists containing sublists, the task is to merge elements of sublist
of two lists in a single list.

 **Examples:**

    
    
     **Input:**
    list1 = [[1, 20, 30],
             [40, 29, 72], 
             [119, 123, 115]]
    
    list2 = [[29, 57, 64, 22],
             [33, 66, 88, 15], 
             [121, 100, 15, 117]]
    
    **Output:** [[1, 20, 30, 29, 57, 64, 22],
             [40, 29, 72, 33, 66, 88, 15],
             [119, 123, 115, 121, 100, 15, 117]]
    

  
**Method #1: UsingMap + lambda**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to merge elements of sublists

 

# Initialisation of first list

list1 = [[1, 20, 30],

 [40, 29, 72],

 [119, 123, 115]]

 

# Initialisation of second list

list2 = [[29, 57, 64, 22],

 [33, 66, 88, 15],

 [121, 100, 15, 117]]

 

# Using map + lambda to merge lists

Output = list(map(lambda x, y:x + y, list1, list2))

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1, 20, 30, 29, 57, 64, 22],
     [40, 29, 72, 33, 66, 88, 15], 
     [119, 123, 115, 121, 100, 15, 117]]
    

  
**Method #2: UsingZip()**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to merge elements of sublists

 

# Initialisation of first list

list1 = [[1, 20, 30],

 [40, 29, 72],

 [119, 123, 115]]

 

# Initialisation of second list

list2 = [[29, 57, 64, 22],

 [33, 66, 88, 15],

 [121, 100, 15, 117]]

 

# Using zip to merge lists

Output = [x + y for x, y in zip(list1, list2)]

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1, 20, 30, 29, 57, 64, 22],
     [40, 29, 72, 33, 66, 88, 15],
     [119, 123, 115, 121, 100, 15, 117]]
    

  
**Method #3: Usingstarmap() and concat()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to merge elements of sublists

 

from operator import concat

from itertools import starmap

 

# Initialisation of first list

list1 = [[1, 20, 30],

 [40, 29, 72],

 [119, 123, 115]]

 

# Initialisation of second list

list2 = [[29, 57, 64, 22],

 [33, 66, 88, 15], 

 [121, 100, 15, 117]]

 

# Using starmap() and concat to merge list

Output = list(starmap(concat, zip(list1, list2)))

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1, 20, 30, 29, 57, 64, 22],
     [40, 29, 72, 33, 66, 88, 15],
     [119, 123, 115, 121, 100, 15, 117]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

