Remove one element to get maximum XOR



Given an array **arr[]** of **N** elements, the task is to remove one element
from the array such that the XOR value of the array is maximized. Print the
maximized value.

 **Examples:**

>  **Input:** arr[] = {1, 1, 3}  
>  **Output:** 2  
> All possible ways of deleting one element and their  
> corresponding XOR values will be:  
> a) Remove 1 -> (1 XOR 3) = 2  
> b) Remove 1 -> (1 XOR 3) = 2  
> c) Remove 3 -> (1 XOR 1) = 0  
> Thus, the final answer is 2.
>
>  **Input:** arr[] = {3, 3, 3}  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** One way will be to remove each element one by one and
then finding the XOR of the remaining elements. The time complexity of this
approach will be O(N2).

  

  

 **Efficient approach:**

  * Find XOR of all the elements of the array. Let’s call this value **X**.
  * For each element **arr[i]** , perform **Y = (X XOR arr[i])** and update the final answer as **ans = max(Y, ans)**.

The above method works because if **(A XOR B) = C** then (C XOR B) = A

