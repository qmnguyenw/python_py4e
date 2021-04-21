Number of elements less than or equal to a number in a subarray : MO’s
Algorithm



  
Given an array **arr** of size **N** and **Q** queries of the form L, R and X,
the task is to print the number of elements less than or equal to X in the
subarray represented by L to R.

 **Prerequisites:** MO’s Algorithm, Sqrt Decomposition

 **Examples:**

    
    
    **Input:** 
    arr[] = {2, 3, 4, 5}
    Q = {{0, 3, 5}, {0, 2, 2}}
    **Output:**
     4
     1
    **Explanation:**
    Number of elements less than or equal to 5
    in arr[0..3] is 4 (all elements)
    
    Number of elements less than or equal to 2 
    in arr[0..2] is 1 (only 2)
    
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
The idea of MO’s algorithm is to pre-process all queries so that result of one
query can be used in the next query.  
Let **arr[0…n-1]** be input array and **Q[0..m-1]** be an array of queries.

  1. Sort all queries in a way that queries with L values from **0 to √n – 1** are put together, then all queries from **√n to 2×√n – 1** , and so on. All queries within a block are sorted in increasing order of R values.
  2. Process all queries one by one in a way that every query uses result computed in the previous query.
  3. We will maintain the **frequency array** that will count the frequency of arr[i] as they appear in the range [L, R].
  4.  **For example:** arr[]=[3, 4, 6, 2, 7, 1], L=0, R=4 and X=5

  

  

> Initially frequency array is initialized to 0 i.e freq[]=[0….0]  
>  **Step 1** – add arr[0] and increment its frequency as freq[arr[0]]++ i.e
> freq[3]++  
> and freq[]=[0, 0, 0, 1, 0, 0, 0, 0]
>
>  **Step 2** – Add arr[1] and increment freq[arr[1]]++ i.e freq[4]++  
> and freq[]=[0, 0, 0, 1, 1, 0, 0, 0]
>
>  **Step 3** – Add arr[2] and increment freq[arr[2]]++ i.e freq[6]++  
> and freq[]=[0, 0, 0, 1, 1, 0, 1, 0]
>
>  **Step 4** – Add arr[3] and increment freq[arr[3]]++ i.e freq[2]++  
> and freq[]=[0, 0, 1, 1, 1, 0, 1, 0]
>
>  **Step 5** – Add arr[4] and increment freq[arr[4]]++ i.e freq[7]++  
> and freq[]=[0, 0, 1, 1, 1, 0, 1, 1]
>
>  **Step 6** – Now we need to find the numbers of elements less than or equal
> to X(here X=5).
>
>  **Step 7** – The answer is equal to ![\\sum_{i=0}^{X}
> freq\[i\]](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-77f056b293cb4c1f44872614e558a01e_l3.png)
>
> To calculate the **sum in step 7** , we cannot do iteration because that
> would lead to O(N) time complexity per query so we will use **sqrt
> decomposition technique** to find the sum whose **time complexity is O(√n)
> per query**.

