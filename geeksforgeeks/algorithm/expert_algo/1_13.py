Leftmost Column with atleast one 1 in a row-wise sorted binary matrix | Set 2



  
Given a binary matrix **mat[][]** containing 0’s and 1’s. Each row of the
matrix is sorted in the non-decreasing order, the task is to find the left-
most column of the matrix with at least one 1 in it.

 **Note:** If no such column exists return -1.

 **Examples:**

    
    
    **Input:** 
    mat[][] = {{0, 0, 0, 1}
               {0, 1, 1, 1}
               {0, 0, 1, 1}}
    **Output:** 2
    **Explanation:**
    The 2nd column of the
    matrix contains atleast a 1.
    
    **Input:** 
    mat[][] = {{0, 0, 0}
               {0, 1, 1}  
               {1, 1, 1}}
    **Output:** 1
    **Explanation:**
    The 1st column of the
    matrix contains atleast a 1.
    
    **Input:** 
    mat[][] = {{0, 0}
               {0, 0}}
    **Output:** -1
    **Explanation:**
    There is no such column which 
    contains atleast one 1.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  * Here we start our traversal from the last element of the first row. This includes two steps.

  

  

  1. If the current iterating element is 1, we decrement the column index. As we find the leftmost column index with value 1, so we don’t have to check elements with greater column index.
  2. If the current iterating element is 0, we increment row index. As that element is 0, we don’t need to check previous elements of that row.

* We continue until one of the row or column index become invalid.

