Python Program to print hollow half diamond hash pattern



Give an integer **N** and the task is to print hollow half diamond pattern.

 **Examples:**

    
    
    **Input :** 6
    **Output :**
    # 
    # # 
    #   # 
    #     # 
    #       # 
    #         # 
    #       # 
    #     # 
    #   # 
    # # 
    # 
    
    **Input :** 7
    **Output :**
    # 
    # # 
    #   # 
    #     # 
    #       # 
    #         # 
    #           # 
    #         # 
    #       # 
    #     # 
    #   # 
    # # 
    #  
    

**Approach:**  
The idea is to break the pattern into two parts:

  *  **Upper part:** For the upper half start the for loop with iterator (i) from 1 to n and one more for loop with iterator (j) from 1 to i.
    
    
    # 
    # # 
    #   # 
    #     # 
    #       # 
    #         # 
    #           #  
    

  * **Lower part:** For lower half start the for loop with iterator (n-1) to 1 and loop inside this for will remain same as for the upper half.
    
    
    #         # 
    #       # 
    #     # 
    #   # 
    # # 
    #
    

  * Now we have to check this condition that if (i==j) or (j==1) then we have to print “#”, otherwise we have to print ” “(space).

 **Below is the implementation:**

 __

 __  
 __

 __

 __  
 __  
 __

# python program to print

# hollow half diamond star

 

 

# function to print hollow

# half diamond star

def hollow_half_diamond(N):

 

 # this for loop is for 

 # printing upper half 

 for i in range( 1, N + 1):

 for j in range(1, i + 1):

 

 # this is the condition to 

 # print "#" only on the

 # boundaries

 if i == j or j == 1:

 print("#", end =" ")

 

 # print " "(space) on the rest

 # of the area

 else:

 print(" ", end =" ")

 print()

 

 # this for loop is to print lower half

 for i in range(N - 1, 0, -1):

 

 for j in range(1, i + 1):

 

 if j == 1 or i == j:

 print("#", end =" ")

 

 else:

 print(" ", end =" ")

 

 print()

 

# Driver Code

if __name__ == "__main__":

 N = 7

 hollow_half_diamond( N )

   
  
---  
  
__

__

**Output:**

  

  

    
    
    # 
    # # 
    #   # 
    #     # 
    #       # 
    #         # 
    #           # 
    #         # 
    #       # 
    #     # 
    #   # 
    # # 
    # 
    

**Time Complexity:** O(N^2)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

