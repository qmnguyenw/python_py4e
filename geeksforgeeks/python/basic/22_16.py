Python | Permutation of a given string using inbuilt function



A permutation, also called an “arrangement number” or “order”, is a
rearrangement of the elements of an ordered list S into a one-to-one
correspondence with S itself. A string of length n has n! permutation.

Examples:

    
    
    Input :  str = 'ABC'
    Output : ABC 
             ACB 
             BAC 
             BCA 
             CAB 
             CBA

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Permutations of a
given string using STL link. We can also solve this problem in python using
inbuilt function permutations(iterable).

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find permutations of a given string

from itertools import permutations

 

def allPermutations(str):

 

 # Get all permutations of string 'ABC'

 permList = permutations(str)

 

 # print all permutations

 for perm in list(permList):

 print (''.join(perm))

 

# Driver program

if __name__ == "__main__":

 str = 'ABC'

 allPermutations(str)  
  
---  
  
 __

 __

 **Output:**

    
    
    ABC
    ACB
    BAC
    BCA
    CAB
    CBA
    

Permutation and Combination in Python

  

  

 **Permutations of a given string with repeating characters**  
The idea is to use dictionary to avoid printing duplicates.

 __

 __  
 __

 __

 __  
 __  
 __

from itertools import permutations

import string

 

s = "GEEK"

a = string.ascii_letters

p = permutations(s)

 

# Create a dictionary

d = []

for i in list(p):

 

 # Print only if not in dictionary

 if (i not in d):

 d.append(i)

 print(''.join(i))  
  
---  
  
 __

 __

 **Output:**

    
    
    GEEK
    GEKE
    GKEE
    EGEK
    EGKE
    EEGK
    EEKG
    EKGE
    EKEG
    KGEE
    KEGE
    KEEG
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

