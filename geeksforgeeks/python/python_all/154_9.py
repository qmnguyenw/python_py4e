Python | Check if a list exists in given list of lists



Given a list of lists, the task is to check if a list exists in given list of
lists.

    
    
     **Input :**
    lst = [[1, 1, 1, 2], [2, 3, 4], [1, 2, 3], [4, 5, 6]]
    list_search = [4, 5, 6]
    
    **Output:** True
    
    **Input :**
    lst = [[5, 6, 7], [12, 54, 9], [1, 2, 3]]
    list_search = [4, 12, 54]
    
    **Output:** False
    

Let’s discuss certain ways in which this task is performed.

 **Method #1: Using _Counter_**  
The most concise and readable way to find whether a list exists in list of
lists is using Counter.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code find whether a list

# exists in list of list.

import collections

 

# Input List Initialization

Input = [[1, 1, 1, 2], [2, 3, 4], [1,
2, 3], [4, 5, 6]]

 

# List to be searched

list_search = [2, 3, 4]

 

# Flag initialization

flag = 0

 

# Using Counter

for elem in Input:

 if collections.Counter(elem) == collections.Counter(list_search)
:

 flag = 1

 

# Check whether list exists or not. 

if flag == 0:

 print("False")

else:

 print("True")  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    

  
**Method #2: Using _in_**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code find whether a list

# exists in list of list.

 

# Input List Initialization

Input = [[1, 1, 1, 2], [2, 3, 4], [1,
2, 3], [4, 5, 6]]

 

# List to be searched

list_search = [1, 1, 1, 2]

 

# Using in to find whether 

# list exists or not

if list_search in Input:

 print("True")

else:

 print("False")  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    

  
**Method #3: Usingany**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code find whether a list

# exists in list of list.

 

# Input List Initialization

Input = [[1, 1, 1, 2], [2, 3, 4], [1,
2, 3], [4, 5, 6]]

 

# List to be searched

list_search = [4, 5, 6]

 

# Using any to find whether 

# list exists or not

if any(list == list_search for list in Input):

 print("True")

else:

 print("False")

   
  
---  
  
__

__

**Output:**

    
    
    True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

