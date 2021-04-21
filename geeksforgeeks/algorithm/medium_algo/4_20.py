Find all Factors of Large Perfect Square Natural Number in O(sqrt(sqrt(N))



Given a **perfect square** natural number **N**. The task is to find all the
factors of **N**.

 **Examples**

>  **Input:** N = 100  
>  **Output:** 1 2 4 5 10 20 25 50 100
>
>  **Input:** N = 900  
>  **Output:** 1 2 4 3 6 12 9 18 36 5 10 20 15 30 60 45 90 180 25 50 100 75
> 150 300 225 450 900

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  1. Find the square root of **N** in temp.
  2. Find all the prime factors of temp in **O(sqrt(temp))** using the approach discussed in this article.
  3. Initialise an array **factor[]** with element 1 in it.
  4. Store all the prime factors of **temp** obtained in above step twice in an array **factor[]**.
  5. Initialise a matrix **M** such that for every element in **factor[]** starting from index 1:
    * If **factor[i]** is equals to **factor[i-1]** , then store **factor[i]*factor[i-1]** in matrix **M** in row **i – 1**.
    * Else **factor[i]** is not equals to **factor[i-1]** , then store **factor[i]*factor[i-1]** in matrix **M** in row **i**.
  6. Initialise two arrays **arr1[]** and **arr2[]** with the element 1 in both the array.
  7. Iterate over every row of matrix **M** such that the product of every element in **arr1[]** with every element of current row must be stored in **arr2[]**.
  8. After above step, copy every element of **arr2[]** in 

