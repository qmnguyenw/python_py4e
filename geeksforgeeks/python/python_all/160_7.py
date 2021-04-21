Python | Ways to Spilt the list by some value



Given a list (may contain either strings or numbers), the task is to split the
list by some value into two lists.

The approach is very simple. Split the first half of list by given value, and
second half from the same value. There are multiple variations possible from
this operation based on the requirement, like dropping the first/some
element(s) in second half after the split value etc. Let’s see the different
ways we can do this task.

 **Method #1: Using list index**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to split the list

# by some value into two lists.

 

# List initialisation

list = ['Geeks', 'forgeeks', 'is a', 'portal', 'for
Geeks']

 

# Splitting list into first half

first_list = list[:list.index('forgeeks')]

 

# Splitting list into second half

second_list = list[list.index('forgeeks')+1:]

 

# Printing first list

print(first_list)

 

# Printing second list

print(second_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Geeks']
    ['is a', 'portal', 'for Geeks']
    

**Method #2: Using dropwhile and set**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to split the list

# by some value into two lists.

 

# Importing

from itertools import dropwhile

 

# List initialisation

lst = ['Geeks', 'forgeeks', 'is a', 'portal', 'for
Geeks']

 

# Using dropwhile to split into second list

second_list = list(dropwhile(lambda x: x != 'forgeeks',
lst))[1:]

 

# Using set to get difference between two lists

first_list = set(lst)-set(second_list)

 

# removing 'split' string

first_list.remove('forgeeks')

 

# converting to list

first_list = list(first_list)

 

# Printing first list

print(first_list)

 

# Printing second list

print(second_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Geeks']
    ['is a', 'portal', 'for Geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

