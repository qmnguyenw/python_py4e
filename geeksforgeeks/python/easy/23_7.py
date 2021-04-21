Python List Comprehension | Sort even-placed elements in increasing and odd-
placed in decreasing order



We are given an array of n distinct numbers, the task is to sort all even-
placed numbers in increasing and odd-place numbers in decreasing order. The
modified array should contain all sorted even-placed numbers followed by
reverse sorted odd-placed numbers.

Note that the first element is considered as even because of its index 0.

Examples:

    
    
    Input:  arr[] = {0, 1, 2, 3, 4, 5, 6, 7}
    Output: arr[] = {0, 2, 4, 6, 7, 5, 3, 1}
    Even-place elements : 0, 2, 4, 6
    Odd-place elements : 1, 3, 5, 7
    Even-place elements in increasing order : 
    0, 2, 4, 6
    Odd-Place elements in decreasing order : 
    7, 5, 3, 1
    
    Input: arr[] = {3, 1, 2, 4, 5, 9, 13, 14, 12}
    Output: {2, 3, 5, 12, 13, 14, 9, 4, 1}
    Even-place elements : 3, 2, 5, 13, 12
    Odd-place elements : 1, 4, 9, 14
    Even-place elements in increasing order : 
    2, 3, 5, 12, 13
    Odd-Place elements in decreasing order : 
    14, 9, 4, 1
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Sort even-placed
elements in increasing and odd-placed in decreasing order link. We can solve
this problem in python quickly using List Comprehension. Approach is very
simple,

  

  

  1. Separate original list into two parts, one contains all even indexed elements and one contains all odd indexed elements.
  2. Now sort list containing all even indexed elements in ascending order and list containing all odd indexed elements in descending order. Now concatenate both of them.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to Sort even-placed elements

# in increasing and odd-placed in decreasing

# order

 

def evenOddSort(input):

 

 # separate even odd indexed elements list

 evens = [ input[i] for i in
range(0,len(input)) if i%2==0 ] 

 odds = [ input[i] for i in
range(0,len(input)) if i%2!=0 ] 

 

 # sort evens in ascending and odds in 

 # descending using sorted() method

 print (sorted(evens) + sorted(odds,reverse=True))

 

# Driver program

if __name__ == "__main__":

 input = [0, 1, 2, 3, 4, 5, 6, 7]

 evenOddSort(input)  
  
---  
  
 __

 __

Output:

    
    
    [0, 2, 4, 6, 7, 5, 3, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

