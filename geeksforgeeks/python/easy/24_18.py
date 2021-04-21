Python Set difference to find lost element from a duplicated array



Given two arrays which are duplicates of each other except one element, that
is one element from one of the array is missing, we need to find that missing
element.

Examples:

    
    
    Input:  A = [1, 4, 5, 7, 9]
            B = [4, 5, 7, 9]
    Output: [1]
    1 is missing from second array.
    
    Input: A = [2, 3, 4, 5
           B = 2, 3, 4, 5, 6]
    Output: [6]
    6 is missing from first array.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Find lost element from
a duplicated array. We can solve this problem quickly in python using Set
difference logic. Approach is very simple, simply convert both lists in
**Set** and perform **A-B** operation where len(A)>len(B).

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find lost element from a duplicate

# array

 

def lostElement(A,B):

 

 # convert lists into set

 A = set(A)

 B = set(B)

 

 # take difference of greater set with smaller

 if len(A) > len(B):

 print (list(A-B))

 else:

 print (list(B-A))

 

# Driver program

if __name__ == "__main__":

 A = [1, 4, 5, 7, 9]

 B = [4, 5, 7, 9]

 lostElement(A,B)  
  
---  
  
 __

 __

Output:

    
    
    [1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

