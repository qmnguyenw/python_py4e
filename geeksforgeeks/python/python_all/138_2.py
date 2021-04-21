Python | Ways to find all permutation of a string



Given a string, write a Python program to find out all possible permutations
of a string. Let’s discuss a few methods to solve the problem.

 **Method #1: Using Naive Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find all permutation of

# a given string

 

# Initialising string

ini_str = "abc"

 

# Printing initial string

print("Initial string", ini_str)

 

# Finding all permuatation

result = []

 

def permute(data, i, length): 

 if i == length: 

 result.append(''.join(data) )

 else: 

 for j in range(i, length): 

 # swap

 data[i], data[j] = data[j], data[i] 

 permute(data, i + 1, length) 

 data[i], data[j] = data[j], data[i] 

permute(list(ini_str), 0, len(ini_str))

 

# Printing result

print("Resultant permutations", str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial string abc
    Resultant permutations ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
    

  
**Method #2: Using itertools**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find all permutation of

# a given string

 

from itertools import permutations

 

# Initialising string

ini_str = "abc"

 

# Printing initial string

print("Initial string", ini_str)

 

# Finding all permuatation

permutation = [''.join(p) for p in permutations(ini_str)]

# Printing result

print("Resultant List", str(permutation))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial string abc
    Resultant List ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

