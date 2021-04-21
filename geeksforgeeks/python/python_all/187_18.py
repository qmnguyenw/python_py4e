Python Program for Largest Sum Contiguous Subarray



Write an efficient program to find the sum of contiguous subarray within a
one-dimensional array of numbers which has the largest sum.

![kadane-algorithm](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/kadane-Algorithm.png)

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

# Python program to find maximum contiguous subarray

 

# Function to find the maximum contiguous subarray

from sys import maxint

def maxSubArraySum(a, size):

 

 max_so_far = -maxint - 1

 max_ending_here = 0

 

 for i in range(0, size):

 max_ending_here = max_ending_here + a[i]

 if (max_so_far < max_ending_here):

 max_so_far = max_ending_here

 

 if max_ending_here < 0:

 max_ending_here = 0

 return max_so_far

 

# Driver function to check the above function 

a = [-13, -3, -25, -20, -3, -16,
-23, -12, -5, -22, -15, -4, -7]

print "Maximum contiguous sum is", maxSubArraySum(a, len(a))

 

# This code is contributed by _Devesh Agrawal_  
  
---  
  
 __

 __

 **Output:**

    
    
    Maximum contiguous sum is -3
    

Above program can be optimized further, if we compare max_so_far with
max_ending_here only if max_ending_here is greater than 0.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

def maxSubArraySum(a, size):

 

 max_so_far = 0

 max_ending_here = 0

 

 for i in range(0, size):

 max_ending_here = max_ending_here + a[i]

 if max_ending_here < 0:

 max_ending_here = 0

 

 # Do not compare for all elements. Compare only 

 # when max_ending_here > 0

 elif (max_so_far < max_ending_here):

 max_so_far = max_ending_here

 

 return max_so_far  
  
---  
  
 __

 __

Please refer complete article onLargest Sum Contiguous Subarray for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

