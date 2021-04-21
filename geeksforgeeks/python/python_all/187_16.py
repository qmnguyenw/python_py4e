Python Program to print all permutations of a given string



A permutation, also called an “arrangement number” or “order, ” is a
rearrangement of the elements of an ordered list S into a one-to-one
correspondence with S itself. A string of length n has n! permutation.  
Source: Mathword(http://mathworld.wolfram.com/Permutation.html)

Below are the permutations of string ABC.  
ABC ACB BAC BCA CBA CAB

## Recommended: Please solve it on “ ** _ _PRACTICE__** ” first, before moving
on to the solution.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print all permutations with

# duplicates allowed

 

def toString(List):

 return ''.join(List)

 

# Function to print permutations of string

# This function takes three parameters:

# 1. String

# 2. Starting index of the string

# 3. Ending index of the string.

def permute(a, l, r):

 if l == r:

 print toString(a)

 else:

 for i in xrange(l, r + 1):

 a[l], a[i] = a[i], a[l]

 permute(a, l + 1, r)

 a[l], a[i] = a[i], a[l] # backtrack

 

# Driver program to test the above function

string = "ABC"

n = len(string)

a = list(string)

permute(a, 0, n-1)

 

# This code is contributed by Bhavya Jain  
  
---  
  
 __

 __

 **Output:**

    
    
    ABC
    ACB
    BAC
    BCA
    CBA
    CAB
    

## By Using inbuilt Function

For finding the permutation of the given string we use the inbuilt function.
You can use the itertools module which has a useful method called
permutations(iterable[, r]). This method will return successive r length
permutations of elements in the iterable as tuples. you’ll need to iterate
over the function call and join the tuples.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print all permutations

 

from itertools import permutations

print [''.join(p) for p in permutations('ABC')]

# This code is contributed by Vidit Varshney  
  
---  
  
 __

 __

 **Output:**

    
    
    ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
    

Please refer complete article on Write a program to print all permutations of
a given string for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

