Python List Equality | Program to check if two given matrices are identical



We are given two square matrices of same order. Check if two given matrices
are identical.

Examples:

    
    
    Input :     A = [ [1, 1, 1, 1],
                      [2, 2, 2, 2],
                      [3, 3, 3, 3],
                      [4, 4, 4, 4]]
     
                B = [ [1, 1, 1, 1],
                      [2, 2, 2, 2],
                      [3, 3, 3, 3],
                      [4, 4, 4, 4]]
    
    Output:    Matrices are identical
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer C Program to check if
two given matrices are identical link. In python any iterable object is
comparable so we can solve this problem quickly in python with the help of
**List Equality**.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to check if two given matrices are identical

 

def identicalMatrices(A,B):

 

 if A==B:

 print ('Matrices are identical')

 else:

 print ('Matrices are not identical')

 

# Driver program

if __name__ == "__main__":

 A = [ [1, 1, 1, 1],

 [2, 2, 2, 2],

 [3, 3, 3, 3],

 [4, 4, 4, 4]]

 

 B = [ [1, 1, 1, 1],

 [2, 2, 2, 2],

 [3, 3, 3, 3],

 [4, 4, 4, 4]]

 identicalMatrices(A,B)  
  
---  
  
 __

 __

Output:

    
    
    Matrices are identical
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

