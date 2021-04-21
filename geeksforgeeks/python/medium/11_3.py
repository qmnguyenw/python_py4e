Python – Itertools.chain.from_iterable()



Python’s Itertool is a module that provides various functions that work on
iterators to produce complex iterators. This module works as a fast, memory-
efficient tool that is used either by themselves or in combination to form
iterator algebra.

 **Note:** For more information, refer to Python Itertools

The functions under itertools can be classified into 3 categories

  1. Functions producing Infinite Iterators
  2. Functions producing Iterators terminating on the shortest input sequence
  3. Functions producing Combinatoric generators

## Chain.from_iterable() method

The function chain.from_iterable() comes under the category of terminating
iterators. This function takes a single iterable as an argument and all the
elements of the input iterable should also be iterable and it returns a
flattened iterable containing all the elements of the input iterable.

    
    
    **Syntax :**
    chain.from_iterable(iterable)
    

**Example #1:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Importing chain class from itertools

from itertools import chain

 

 

# Single iterable containing iterable

# elements(strings) is passed as input

from_iterable = chain.from_iterable(['geeks',

 'for', 

 'geeks'])

 

# printing the flattened iterable

print(list(from_iterable))  
  
---  
  
 __

 __

 **Output :**

> [‘g’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’, ‘r’, ‘g’, ‘e’, ‘e’, ‘k’, ‘s’]

 **Example #2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Importing chain class from itertools

from itertools import chain

 

 

# Single iterable containing iterable

# elements(strings and list) is passed

# as input

from_iterable = chain.from_iterable(['geeks', 

 'for',

 'geeks',

 ['w', 'i', 'n', 's']])

 

# printing the flattened iterable

print(list(from_iterable))  
  
---  
  
 __

 __

 **Output :**

> [‘g’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’, ‘r’, ‘g’, ‘e’, ‘e’, ‘k’, ‘s’, ‘w’, ‘i’,
> ‘n’, ‘s’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

