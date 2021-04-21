Count no. of columns that are not sorted in increasing order



Given an array A of N lowercase letter strings of the same length. The task is
to find the count of columns that are not sorted in increasing order.

 **Examples:**

    
    
    **Input:** A = ["cba", "dah", "ghi"]
    **Output:** 1
    2nd Column ["b", "a", "h"] is not sorted in increasing order.
    
    **Input:** A = ["zyx", "wvu", "tsr"]
    **Output:** 3
    All columns are not sorted in increasing order.
    
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Traverse each column one by one and check if the next element
is greater than the previous element in the same column. If not the increment
the **countOfCol** by 1 and keep traversing till all the columns get
traversed. Print the value of **countOfCol**.

 __

 __  
 __

 __

 __  
 __  
 __

# function to count the unsorted columns

def countUnsorted(A):

 

 countOfCol = 0

 

 for col in zip(*A):

 if any(col[i] > col[i + 1] for i in range(len(col)
- 1)):

 countOfCol += 1

 

 return countOfCol

 

# Driver code

A = ["cba", "daf", "ghi"]

print(countUnsorted(A))  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

