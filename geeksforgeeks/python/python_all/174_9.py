Python Program to check if given array is Monotonic



Given an array **A** containing **n** integers. The task is to check whether
the array is **Monotonic** or not. An array is monotonic if it is either
**monotone increasing** or **monotone decreasing**.  
An array A is monotone increasing if for all i <= j, **A[i] <= A[j]**. An
array A is monotone decreasing if for all i <= j, **A[i] >= A[j]**.  
Return “ **True** ” if the given array A is monotonic else return “ **False**
” (without quotes).

Examples:

    
    
    Input : 6 5 4 4
    Output : true
    
    Input : 5 15 20 10
    Output : false
    

**Approach:**  
An array is **monotonic** if and only if it is **monotone increasing** , or
**monotone decreasing**. Since **p <= q** and **q <= r** implies **p <= r**.
So we only need to check adjacent elements to determine if the array is
monotone increasing (or decreasing), respectively. We can check each of these
properties in one pass.  
To check whether an array A is **monotone increasing** , we’ll check **A[i] <=
A[i+1]** for all i indexing from 0 to len(A)-2. Similarly we can check for
**monotone decreasing** where **A[i] >= A[i+1]** for all i indexing from 0 to
len(A)-2.  
 **Note:** Array with **single element** can be considered to be both
**monotonic increasing or decreasing** , hence returns “ **True** “.

 **Below is the implementation of above approach:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find sum in Nth group

 

# Check if given array is Monotonic

def isMonotonic(A):

 

 return (all(A[i] <= A[i + 1] for i in
range(len(A) - 1)) or

 all(A[i] >= A[i + 1] for i in range(len(A) -
1)))

 

# Driver program

A = [6, 5, 4, 4]

 

# Print required result

print(isMonotonic(A))

 

# This code is written by

# Sanjit_Prasad  
  
---  
  
 __

 __

  
Output:

    
    
    True

 **Time Complexity:** O(N), where N is the length of array.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

