Python – Print Heart Pattern



Given an even integer input, the task is to write a Python program to print a
heart using loops and mathematical formulations.

#### Example :

    
    
    For n = 8
    
      *   *   *   *   
    *       *       * 
    *               * 
    *     G F G     * 
      *           *   
        *       *     
          *   *       
            *
    
    For n = 14
    
          * *           * *       
        *     *       *     *     
      *         *   *         *   
    *             *             * 
    *                           * 
    *           G F G           * 
      *                       *   
        *                   *     
          *               *       
            *           *         
              *       *           
                *   *             
                  *       

#### Approach :

The following steps are used :

  * Form the worksheet of n X n+1 using two loops.
  * Apply the if-else conditions for printing stars.
  * Apply the if-else conditions for printing text “GFG”.
  * Apply else condition for rest spaces.

 **Note:** The value of n must be greater than 8

Below is the implementation of the above approach :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# define size n = even only

n = 8

 

# so this heart can be made n//2 part left,

# n//2 part right, and one middle line

# i.e; columns m = n + 1

m = n+1

 

# loops for upper part

for i in range(n//2-1):

 for j in range(m):

 

 # condition for printing stars to GFG upper line

 if i == n//2-2 and (j == 0 or j ==
m-1):

 print("*", end=" ")

 

 # condition for printing stars to left upper

 elif j <= m//2 and ((i+j == n//2-3
and j <= m//4) \

 or (j-i == m//2-n//2+3 and j >
m//4)):

 print("*", end=" ")

 

 # condition for printing stars to right upper

 elif j > m//2 and ((i+j ==
n//2-3+m//2 and j < 3*m//4) \

 or (j-i == m//2-n//2+3+m//2
and j >= 3*m//4)):

 print("*", end=" ")

 

 # condition for printing spaces

 else:

 print(" ", end=" ")

 print()

 

# loops for lower part

for i in range(n//2-1, n):

 for j in range(m):

 

 # condition for printing stars

 if (i-j == n//2-1) or (i+j ==
n-1+m//2):

 print('*', end=" ")

 

 # condition for printing GFG

 elif i == n//2-1:

 

 if j == m//2-1 or j == m//2+1:

 print('G', end=" ")

 elif j == m//2:

 print('F', end=" ")

 else:

 print(' ', end=" ")

 

 # condition for printing spaces

 else:

 print(' ', end=" ")

 

 print()  
  
---  
  
 __

 __

 **Output:**

    
    
                                  
          * *           * *       
        *     *       *     *     
      *         *   *         *   
    *             *             * 
    *                           * 
    *           G F G           * 
      *                       *   
        *                   *     
          *               *       
            *           *         
              *       *           
                *   *             
                  *               

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

