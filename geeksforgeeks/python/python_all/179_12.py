Python 3 | Program to print double sided stair-case pattern



Below mentioned is the python 3 program to print the double sided stair case
pattern.

 **Examples:**

    
    
    Input : 10
    Output :
    
                     *   * 
                     *   * 
                 *   *   *   * 
                 *   *   *   * 
             *   *   *   *   *   * 
             *   *   *   *   *   * 
         *   *   *   *   *   *   *   * 
         *   *   *   *   *   *   *   * 
     *   *   *   *   *   *   *   *   *   * 
     *   *   *   *   *   *   *   *   *   * 
    
    

**Note :** This code only works for even values of n.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to demonstrate

# staircase pattern

 

# function definition

def pattern(n):

 

 # for loop for rows

 for i in range(1,n+1):

 

 # conditional operator

 k =i + 1 if(i % 2 != 0) else i

 

 # for loop for printing spaces

 for g in range(k,n):

 if g>=k:

 print(end=" ")

 

 # according to value of k carry

 # out further operation

 for j in range(0,k):

 if j == k - 1:

 print(" * ")

 else:

 print(" * ", end = " ")

 

 

# Driver code

n = 10

pattern(n)  
  
---  
  
 __

 __

Output:

    
    
    
                     *   * 
                     *   * 
                 *   *   *   * 
                 *   *   *   * 
             *   *   *   *   *   * 
             *   *   *   *   *   * 
         *   *   *   *   *   *   *   * 
         *   *   *   *   *   *   *   * 
     *   *   *   *   *   *   *   *   *   * 
     *   *   *   *   *   *   *   *   *   * 
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

