Count all sub-sequences having product <= K – Recursive approach



Given an integer **K** and a non negative array **arr[]** , the task is to
find the number of sub-sequences having product **≤ K**.  
This problem already has a dynamic programming solution. This solution aims to
provide an _optimized recursive strategy_ to the problem.

 **Examples:**

>  **Input:** arr[] = { 1, 2, 3, 4 }, K = 10  
>  **Output:** 11  
> The sub-sequences are {1}, {2}, {3}, {4}, {1, 2}, {1, 3}, {1, 4}, {2, 3},
> {2, 4}, {1, 2, 3}, {1, 2, 4}
>
>  **Input:** arr[] = { 4, 8, 7, 2 }, K = 50  
>  **Output:** 9

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Convert the **product** problem to a **sum** problem by
performing the conversions **arr[i] = log(arr[i])** and **K = log(K)**.
Generate all subsets and store the sum of elements that have been _taken in_
the sub-sequence. If at any point, the sum becomes larger than K, then we know
that if we add another element to the sub-sequence, its sum will also be
**larger than K**. Therefore, we discard all such sub-sequences that have sum
larger than **K** without making a recursive call for them. Also if we
currently have **sum less than K** then we check if there are any chances to
further discard any sub-sequences.

