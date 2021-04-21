Sum of all N digit palindromic numbers divisible by 9 formed using digits 1 to
9



Given a number **N** , the task is to find the sum of all N digits palindromic
numbers (formed by digits from 1 to 9) that are divisible by 9.

 **Examples:**

>  **Input:** N = 1  
>  **Output:** 9  
>  **Explanation:**  
>  Only 9 is a palindromic number of 1 digit divisible by 9
>
>  **Input:** N = 3  
>  **Output:** 4995  
>  **Explanation:**  
>  Three-digit Palindromic Numbers divisible by 9 are –  
> 171, 252, 333, 414, 585, 666, 747, 828, 999

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The key observation in the problem is that if a number is
divisible by 9, then the sum of digits of that number is also divisible by 9.
Another observation is if we count the number of N-digit palindromic numbers
using the digits from 1 to 9, then it can be observed that

  

  

> Occurrence of each digit = (count of N-digit numbers / 9)

Therefore,

  1. First find the count of N-digit Palindromic numbers divisible by 9, as:  
![\\text{Count of N-digit Palindromic numbers divisible by 9} = \\begin{cases}
9^{\\frac{N-1}{2}} & \\text{ if N is odd} \\\\ 9^{\\frac{N-2}{2}} & \\text{ if
N is even} \\end{cases}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-6a73663fd142acc380382aab86ebc9c9_l3.png)

  2. Then if N is 1 or 2, the sum will be simply 9 and 99 respectively, as they are the only palindromic numbers of 1 and 2 digits.
  3. If N > 2, then the sum for Nth digit palindromic numbers divisible by 9 is  
![\\text{Sum of Nth digit palindromic numbers divisible by 9 }= \(\\text{sum
of }\(N-1\)^{th}\\text{ digit } * 10\) + \(5*\\text{ count of N digit
palindromic numbers divisible by 9}\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-e939822ef72c60484946b1c5f0b514a5_l3.png)

