Avoid TLE in Python in Competitive Programming



 ** _Reasons behind getting TLE_ :**

  * It is slower compared to other programming languages.
  * It offers slower Input/Output.
  * It has a lower recursion depth which often gives TLE in recursion and graph problems.

 ** _Tips to avoid TLE with_** ** _Python_** **:**

###  ** _Convert to an Iterative Approach_ :**

  * Any problem of recursion can be converted to an iterative approach, so try to use the iterative approach instead of recursion.
  * Using Stack and while loop may save the execution time of the program.

 **Program 1:**

Given below is the code showing the time required for calculating the
factorial of a number in both approaches:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Program to show the time taken in

# iteration and recursion

 

import time

 

# Recursive function to find factorial

# of the given number N

def factorial(N):

 

 # Base Case

 if N == 0:

 return 1

 

 # Recursive Call

 return N * factorial(N - 1)

 

# Driver Code

if __name__ == '__main__':

 n = 20

 

 # Find the time taken for the

 # recursive approach

 start = time.perf_counter()

 print("Calculated using recursion: ", factorial(n))

 

 end = time.perf_counter()

 print("Time taken in recursion: ",
"{0:.9f}".format(end-start))

 

 # Find time taken for iterative

 # approach

 start = time.perf_counter()

 result = 1

 

 while n > 0:

 result *= n

 n -= 1

 

 print("Calculated using the iterative method: ", result)

 

 end = time.perf_counter()

 print("Time taken in iteration: ",
"{0:.9f}".format(end-start))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Calculated using recursion:  2432902008176640000
    Time taken in recursion:  0.000015925
    Calculated using the iterative method:  2432902008176640000
    Time taken in iteration:  0.000009279
    

