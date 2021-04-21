Largest substring where all characters appear at least K times | Set 2



Given a string **str** and an integer **K** , the task is to find the length
of the longest sub-string **S** such that every character in **S** appears at
least **K** times.

 **Examples:**

>  **Input:** str = “aabbba”, K = 3  
>  **Output:** 6  
>  **Explanation:**  
>  In substring aabbba, each character repeats at least k times and its length
> is 6.
>
>  **Input:** str = “ababacb”, K = 3  
>  **Output:** 0  
>  **Explanation:**  
>  There is no substring where each character repeats at least k times.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** We have discussed the Naive Approach in the previous
post.

  

  

 **Approach:** In this post, we will discuss the approach using Divide and
Conquer technique and Recursion. Below are the steps:

  1. Store the frequency of each characters of the given string in a frequency array of size **26**.
  2. Initialize two variables _start_ with 0 and _end_ which is the length of the string **str**.
  3. Iterate over the string from **start** to **end** and count the number of times each character repeats and store it in an array.
  4. If any character repeats **less than K times** , then Divide the string into two halves. If i is the index of the string where we found that the **string[i]** repeats less than **K times** , then we divide the string into two halves from **start to i** and **i + 1 to end**.
  5. Recursively call for the two halves in the above steps i.e., from **start to i** and **i + 1 to end** separately and repeat the **Step 2 and 3** and return the maximum of the two values reutnr by the above recursive call.
  6. If all the characters between **start** and **end** is repeated at least **K** times, then the answer is **end – start**.

