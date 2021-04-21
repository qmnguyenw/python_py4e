Python – Itertools.Permutations()



Itertool is a module provided by Python for creating iterators for efficient
looping. It also provides various features or functions that work with
iterators to produce complex iterators and help us to solve problems easily
and efficiently in terms of time as well as memory. Itertools module provides
us various ways to manipulate the sequence that we are traversing through.

 **Different types of iterators provided by this module are:**

  * Infinite Iterators
  * Iterators terminating on the shortest input sequence
  * Combinatoric Iterators

 **Note:** For more information, refer to Python Itertools

## Itertools.permutation()

Itertools.permutation() function falls under the Combinatoric Generators.
The recursive generators that are used to simplify combinatorial constructs
such as permutations, combinations, and Cartesian products are called
combinatoric iterators.

As understood by the word “Permutation” it refers to all the possible
combinations in which a set or string can be ordered or arranged. Similarly
here itertool.permutations() method provides us with all the possible
arrangements that can be there for an iterator and all elements are assumed to
be unique on the basis of there position and not by there value or category.
All these permutations are provided in lexicographical order. The function
itertool.permutations() takes an iterator and ‘r’ (length of permutation
needed) as input and assumes ‘r’ as default length of iterator if not
mentioned and returns all possible permutations of length ‘r’ each.

  

  

 **Syntax:**

    
    
    Permutations(iterator, r)
    

**Example 1:-**

 __

 __  
 __

 __

 __  
 __  
 __

from itertools import permutations 

 

 

a = "GeEK"

 

# no length entered so default length

# taken as 4(the length of string GeEK)

p = permutations(a) 

 

# Print the obtained permutations 

for j in list(p): 

 print(j)   
  
---  
  
__

__

**Output :-**

    
    
    ('G', 'e', 'E', 'K')
    ('G', 'e', 'K', 'E')
    ('G', 'E', 'e', 'K')
    ('G', 'E', 'K', 'e')
    ('G', 'K', 'e', 'E')
    ('G', 'K', 'E', 'e')
    ('e', 'G', 'E', 'K')
    ('e', 'G', 'K', 'E')
    ('e', 'E', 'G', 'K')
    ('e', 'E', 'K', 'G')
    ('e', 'K', 'G', 'E')
    ('e', 'K', 'E', 'G')
    ('E', 'G', 'e', 'K')
    ('E', 'G', 'K', 'e')
    ('E', 'e', 'G', 'K')
    ('E', 'e', 'K', 'G')
    ('E', 'K', 'G', 'e')
    ('E', 'K', 'e', 'G')
    ('K', 'G', 'e', 'E')
    ('K', 'G', 'E', 'e')
    ('K', 'e', 'G', 'E')
    ('K', 'e', 'E', 'G')
    ('K', 'E', 'G', 'e')
    ('K', 'E', 'e', 'G')
    

**Example 2:-**

 __

 __  
 __

 __

 __  
 __  
 __

from itertools import permutations 

 

print ("All the permutations of the given list is:") 

print (list(permutations([1, 'geeks'], 2))) 

print() 

 

print ("All the permutations of the given string is:") 

print (list(permutations('AB'))) 

print() 

 

print ("All the permutations of the given container is:") 

print(list(permutations(range(3), 2)))   
  
---  
  
__

__

**Output:-**

    
    
    All the permutations of the given list is:
    [(1, 'geeks'), ('geeks', 1)]
    
    All the permutations of the given string is:
    [('A', 'B'), ('B', 'A')]
    
    All the permutations of the given container is:
    [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

