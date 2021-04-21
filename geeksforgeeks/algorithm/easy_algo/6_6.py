Count numbers < = N whose difference with the count of primes upto them is > =
K



Given two positive integers **N** and **K** , the task is to count all the
numbers that satisfy the following conditions:  
If the number is **num** ,

  *  **num ≤ N**.
  *  **abs(num – count) ≥ K** where **count** is the count of primes upto **num**.

 **Examples:**

>  **Input:** N = 10, K = 3  
>  **Output:** 5  
> 6, 7, 8, 9 and 10 are the valid numbers. For 6, the difference between 6 and
> prime numbers upto 6 (2, 3, 5) is 3 i.e. 6 – 3 = 3. For 7, 8, 9 and 10 the
> differences are 3, 4, 5 and 6 respectively which are ≥ K.
>
>  **Input:** N = 30, K = 13  
>  **Output:** 10

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Prerequisite:** Binary Search

  

  

 **Approach:** Observe that the function which is the difference of the number
and count of prime numbers upto that number is a monotonically increasing
function for a particular **K**. Also, if a number **X** is a valid number
then **X + 1** will also be a valid number.  
 **Proof :**

> Let the function Ci denotes the count of prime numbers upto number i. Now,  
> for the number X + 1 the difference is X + 1 – CX + 1 which is greater than  
> or equal to the difference X – CX for the number X, i.e. (X + 1 – CX + 1) ≥
> (X – CX).  
> Thus, if (X – CX) ≥ S, then (X + 1 – CX + 1

