Python Program for Find the closest pair from two sorted arrays



Given two sorted arrays and a number x, find the pair whose sum is closest to
x and **the pair has an element from each array**.

We are given two arrays ar1[0…m-1] and ar2[0..n-1] and a number x, we need to
find the pair ar1[i] + ar2[j] such that absolute value of (ar1[i] + ar2[j] –
x) is minimum.

Example:

    
    
    Input:  ar1[] = {1, 4, 5, 7};
            ar2[] = {10, 20, 30, 40};
            x = 32      
    Output:  1 and 30
    
    Input:  ar1[] = {1, 4, 5, 7};
            ar2[] = {10, 20, 30, 40};
            x = 50      
    Output:  7 and 40
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find the pair from

# two sorted arays such that the sum 

# of pair is closest to a given number x

import sys

 

# ar1[0..m-1] and ar2[0..n-1] are two 

# given sorted arrays and x is given 

# number. This function prints the pair 

# from both arrays such that the sum 

# of the pair is closest to x.

def printClosest(ar1, ar2, m, n, x):

 

 # Initialize the diff between 

 # pair sum and x.

 diff = sys.maxsize

 

 # res_l and res_r are result 

 # indexes from ar1[] and ar2[]

 # respectively. Start from left

 # side of ar1[] and right side of ar2[]

 l = 0

 r = n-1

 while(l < m and r >= 0):

 

 # If this pair is closer to x than 

 # the previously found closest,

 # then update res_l, res_r and diff

 if abs(ar1[l] + ar2[r] - x) < diff:

 res_l = l

 res_r = r

 diff = abs(ar1[l] + ar2[r] - x)

 

 

 # If sum of this pair is more than x,

 # move to smaller side

 if ar1[l] + ar2[r] > x:

 r = r-1

 else: # move to the greater side

 l = l + 1

 

 

 # Print the result

 print("The closest pair is [",

 ar1[res_l], ", ", ar2[res_r], "]")

 

# Driver program to test above functions

ar1 = [1, 4, 5, 7]

ar2 = [10, 20, 30, 40]

m = len(ar1)

n = len(ar2)

x = 38

printClosest(ar1, ar2, m, n, x)

 

# This code is contributed by Smitha Dinesh Semwal   
  
---  
  
__

__

**Output:**

    
    
    The closest pair is [ 7 ,  30 ]
    

Please refer complete article on Find the closest pair from two sorted arrays
for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

