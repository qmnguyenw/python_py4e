Python Program to Sort an array of 0s, 1s and 2s



Given an array A[] consisting 0s, 1s and 2s. The task is to write a function
that sorts the given array. The functions should put all 0s first, then all 1s
and all 2s in last.

 **Examples:**

    
    
    **Input :** {0, 1, 2, 0, 1, 2, 2, 2, 2, 1}
    **Output :** {0, 0, 1, 1, 1, 2, 2, 2, 2, 2}
    
    **Input :**  {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
    **Output :**  {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Simple Solution :** We create three empty lists. We add all 0s to first
list, 1s to second list and 2s to third list. Finally we append all lists and
return

 __

 __  
 __

 __

 __  
 __  
 __

# Function for sort

def SortWithoutSorting(arr):

# 3 Empty list for initialize 0 1 and 2

 

 l1 =[]

 l2 =[]

 l3 =[]

 for i in range(len(arr)):

 if arr[i] == 0:

 l1.append(arr[i])

 elif arr[i] == 1:

 l2.append(arr[i])

 else:

 l3.append(arr[i])

 return (l1 + l2 + l3)

 

# Driver Code

arr = array.array('i', [0, 1, 0, 1, 2, 2,
0, 1])

print(SortWithoutSorting(arr))   
  
---  
  
__

__

**Efficient Solution** The above solution requires extra space. How to do it
without extra space (in-place) in the same given list and using only one
traversal. Please refer Sort an array of 0s, 1s and 2s for implementation of
the efficient solution.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

