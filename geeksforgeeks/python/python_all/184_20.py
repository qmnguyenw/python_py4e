Python Program for Selection Sort



The selection sort algorithm sorts an array by repeatedly finding the minimum
element (considering ascending order) from unsorted part and putting it at the
beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.  
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering
ascending order) from the unsorted subarray is picked and moved to the sorted
subarray.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for implementation of Selection

# Sort

import sys

A = [64, 25, 12, 22, 11]

 

# Traverse through all array elements

for i in range(len(A)):

 

 # Find the minimum element in remaining 

 # unsorted array

 min_idx = i

 for j in range(i+1, len(A)):

 if A[min_idx] > A[j]:

 min_idx = j

 

 # Swap the found minimum element with 

 # the first element 

 A[i], A[min_idx] = A[min_idx], A[i]

 

# Driver code to test above

print ("Sorted array")

for i in range(len(A)):

 print("%d" %A[i]),   
  
---  
  
__

__

  
Please refer complete article onSelection Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

