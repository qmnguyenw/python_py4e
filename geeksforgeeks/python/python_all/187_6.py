Python Program to Count Inversions in an array | Set 1 (Using Merge Sort)



 _Inversion Count_ for an array indicates – how far (or close) the array is
from being sorted. If array is already sorted then inversion count is 0. If
array is sorted in reverse order that inversion count is the maximum.  
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j]
and i < j.

 **Example:**  
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

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

# Python3 program to count

# inversions in an array

 

def getInvCount(arr, n):

 

 inv_count = 0

 for i in range(n):

 for j in range(i + 1, n):

 if (arr[i] > arr[j]):

 inv_count += 1

 

 return inv_count

 

# Driver Code

arr = [1, 20, 6, 4, 5]

n = len(arr)

print("Number of inversions are",

 getInvCount(arr, n))

 

# This code is contributed by Smitha Dinesh Semwal  
  
---  
  
 __

 __

 **Output:**

    
    
    Number of inversions are 5
    

**METHOD 2(Enhance Merge Sort)** : Suppose we know the number of inversions in
the left half and right half of the array (let be inv1 and inv2), what kinds
of inversions are not accounted for in Inv1 + Inv2? The answer is – the
inversions we have to count during the merge step. Therefore, to get number of
inversions, we need to add number of inversions in left subarray, right
subarray and merge().  
  
Please refer complete article on Count Inversions in an array | Set 1 (Using
Merge Sort) for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

