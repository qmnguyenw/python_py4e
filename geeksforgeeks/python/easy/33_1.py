Permutation and Combination in Python



Python provides direct methods to find permutations and combinations of a
sequence. These methods are present in itertools package.

 **Permutation**  
First import itertools package to implement the permutations method in python.
This method takes a list as an input and returns an object list of tuples that
contain all permutation in a list form.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to print all

# permutations using library function 

from itertools import permutations 

 

# Get all permutations of [1, 2, 3] 

perm = permutations([1, 2, 3]) 

 

# Print the obtained permutations 

for i in list(perm): 

 print (i)   
  
---  
  
__

__

**Output:**

    
    
    (1, 2, 3)
    (1, 3, 2)
    (2, 1, 3)
    (2, 3, 1)
    (3, 1, 2)
    (3, 2, 1)

It generates n! permutations if the length of the input sequence is n.

If want want to get permutations of length L then implement it in this way.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to print all

# permutations of given length 

from itertools import permutations 

 

# Get all permutations of length 2 

# and length 2 

perm = permutations([1, 2, 3], 2) 

 

# Print the obtained permutations 

for i in list(perm): 

 print (i)   
  
---  
  
__

__

**Output:**

    
    
    (1, 2)
    (1, 3)
    (2, 1)
    (2, 3)
    (3, 1)
    (3, 2)
    

It generate nCr * r! permutations if length of input sequence is n and input
parameter is r.

 **Combination**  
This method takes a list and a input r as a input and return a object list of
tuples which contain all possible combination of length r in a list form.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to print all

# combinations of given length

from itertools import combinations

 

# Get all combinations of [1, 2, 3]

# and length 2

comb = combinations([1, 2, 3], 2)

 

# Print the obtained combinations

for i in list(comb):

 print (i)  
  
---  
  
 __

 __

 **Output:**

    
    
    (1, 2)
    (1, 3)
    (2, 3)
    

  1. Combinations are emitted in lexicographic sort order of input. So, if the input list is sorted, the combination tuples will be produced in sorted order.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to print all

# combinations of a given length 

from itertools import combinations 

 

# Get all combinations of [1, 2, 3] 

# and length 2 

comb = combinations([1, 2, 3], 2) 

 

# Print the obtained combinations 

for i in list(comb): 

 print (i)  
  
---  
  
 __

 __

 **Output:**

    
    
    (2, 1)
    (2, 3)
    (1, 3)
    

  2. Elements are treated as unique based on their position, not on their value. So if the input elements are unique, there will be no repeat values in each combination.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to print all combinations

# of given length with unsorted input. 

from itertools import combinations 

 

# Get all combinations of [2, 1, 3] 

# and length 2 

comb = combinations([2, 1, 3], 2) 

 

# Print the obtained combinations 

for i in list(comb): 

 print (i)  
  
---  
  
 __

 __

 **Output:**

    
    
    (1, 1)
    (1, 3)
    (1, 3)
    

  3. If we want to make combination of same element to same element then we use combinations_with_replacement.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to print all combinations

# with an element-to-itself combination is 

# also included 

from itertools import combinations_with_replacement 

 

# Get all combinations of [1, 2, 3] and length 2 

comb = combinations_with_replacement([1, 2, 3], 2) 

 

# Print the obtained combinations 

for i in list(comb): 

 print (i)   
  
---  
  
__

__

**Output:**

    
    
    (1, 1)
    (1, 2)
    (1, 3)
    (2, 2)
    (2, 3)
    (3, 3) 

This article is contributed by **Raju Varshney**. Please write comments if you
find anything incorrect, or you want to share more information about the topic
discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

