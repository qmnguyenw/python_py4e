Python program to find the power of a number using recursion



Given a number N and power P. The task is to write a Python program to find
the power of a number using recursion.

 **Definition:** The power of a number can be defined as multiplication of the
number repetitively the number of times of its power.

 **Example:**

    
    
     **Input:** N=2 , P=3
    **Output:** 8
    
    **Input:** N=5 , P=2
    **Output:** 25
    

The idea is to calculate power of a number ‘N’ is to multiply that number ‘P’
times i.e In first example N=2 and P=3, we are getting the result by
multiplying 2 three times repetitively which gives us output 8.

 **Below is the implementation:**

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

def power(N, P):

 

 # if power is 0 or 1 then number is returned

 if(P == 0 or P == 1):

 return N

 else:

 return (N*power(N, P-1))

 

# Driver program

N = 5

P = 2

 

print(power(N, P))  
  
---  
  
 __

 __

 **Output:**

    
    
    25
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

