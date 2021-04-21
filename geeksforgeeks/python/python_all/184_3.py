Python Program to Count number of binary strings without consecutive 1’s



Given a positive integer N, count all possible distinct binary strings of
length N such that there are no consecutive 1’s.

Examples:

    
    
    Input:  N = 2
    Output: 3
    // The 3 strings are 00, 01, 10
    
    Input: N = 3
    Output: 5
    // The 5 strings are 000, 001, 010, 100, 101

## Recommended: Please solve it on “ ** _ _PRACTICE__** ” first, before moving
on to the solution.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count

# all distinct binary strings

# without two consecutive 1's

 

def countStrings(n):

 

 a =[0 for i in range(n)]

 b =[0 for i in range(n)]

 a[0] = b[0] = 1

 for i in range(1, n):

 a[i] = a[i-1] + b[i-1]

 b[i] = a[i-1]

 

 return a[n-1] + b[n-1]

 

# Driver program to test

# above functions

 

print(countStrings(3))

 

# This code is contributed

# by Anant Agarwal.  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

Please refer complete article on Count number of binary strings without
consecutive 1’s for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

