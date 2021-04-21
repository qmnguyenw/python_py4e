Count of numbers upto N digits formed using digits 0 to K-1 without any
adjacent 0s



Given two integers **N** and **K** , the task is to count the numbers up to
**N** digits such that no two zeros are adjacents and the range of digits are
from 0 to K-1.  
 **Examples:**  

> **Input:** N = 2, K = 3  
> **Output:** 8  
> **Explanation:**  
> There are 8 such numbers such that digits are from 0 to 2 only, without any
> adjacent 0s: {1, 2, 10, 11, 12, 20, 21, 22}  
>  **Input:** N = 3, K = 3  
> **Output:** 22  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to use Dynamic Programming to solve this problem.  
Let **DP[i][j]** be the number of desirable numbers up to **ith** digit of the
number, and its last digit as **j**.  
 **Observations:**

  * The number of ways to fill a place is![\(K-1\) ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-c9a8ed6bbe4d5d21d54360509e96e39d_l3.png)
  * As we know, zero’s can’t be adjacent. So when our last element is 0, means the previous index is filled by 1 way, that is 0. Therefore, current place can only be filled by (K-1) digits.
  * If the last place is filled by (K-1) digits, Then current digit place can be filled by either 0 or (K-1) digits.

 **Base Case:**

  

  

  * If n == 1 and last == K, then we can fill this place by (K-1) digits, return (K-1)
  * Else, return 1

 **Recurrence relation:**  

> When last digit place is not filled by zero then  
>
>
> ![dp\[i\]\[j\] = \(K-1\)*solve\(n-1, K\) + \(K-1\)*solve\(n-1, 1\)
> ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-f132cb8c3694434785698b86b01da12c_l3.png)
>
> When Last digit place is filled by zero then  
>
>
> ![dp\[i\]\[j\] = solve\(n-1, K\) ](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-e2fab56bb35f920f45851f192edc95c4_l3.png)

Below is the implementation of above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to count the

// numbers upto N digits such that

// no two zeros are adjacent

 

#include <bits/stdc++.h>

using namespace std;

 

int dp[15][10];

 

// Function to count the

// numbers upto N digits such that

// no two zeros are adjacent

int solve(int n, int last, int k)

{

 // Condition to check if only

 // one element remains

 if (n == 1) {

 

 // If last element is non

 // zero, return K-1

 if (last == k) {

 return (k - 1);

 }

 // If last element is 0

 else {

 return 1;

 }

 }

 

 // Condition to check if value

 // calculated already

 if (dp[n][last])

 return dp[n][last];

 

 // If last element is non zero,

 // then two cases arise,

 // current element can be either

 // zero or non zero

 if (last == k) {

 

 // Memoize this case

 return dp[n][last]

 = (k - 1)

 * solve(n - 1, k, k)

 + (k - 1)

 * solve(n - 1, 1, k);

 }

 

 // If last is 0, then current

 // can only be non zero

 else {

 

 // Memoize and return

 return dp[n][last]

 = solve(n - 1, k, k);

 }

}

 

// Driver Code

int main()

{

 // Given N and K

 int n = 2, k = 3;

 

 // Function Call

 int x = solve(n, k, k)

 + solve(n, 1, k);

 cout << x;

}  
  
---  
  
 __

 __

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java implementation to count the

// numbers upto N digits such that

// no two zeros are adjacent

class GFG{

 

static int[][] dp = new int[15][10];

 

// Function to count the numbers 

// upto N digits such that

// no two zeros are adjacent

static int solve(int n, int last, int k)

{

 

 // Condition to check if only

 // one element remains

 if (n == 1)

 {

 

 // If last element is non

 // zero, return K-1

 if (last == k)

 {

 return (k - 1);

 }

 

 // If last element is 0

 else

 {

 return 1;

 }

 }

 

 // Condition to check if 

 // value calculated already

 if (dp[n][last] == 1)

 return dp[n][last];

 

 // If last element is non zero,

 // then two cases arise, current 

 // element can be either zero 

 // or non zero

 if (last == k)

 {

 

 // Memoize this case

 return dp[n][last] = (k - 1) *

 solve(n - 1, k, k) + 

 (k - 1) * 

 solve(n - 1, 1, k);

 }

 

 // If last is 0, then current

 // can only be non zero

 else

 {

 

 // Memoize and return

 return dp[n][last] = solve(n - 1, k, k);

 }

}

 

// Driver Code

public static void main(String[] args)

{

 

 // Given N and K

 int n = 2, k = 3;

 

 // Function Call

 int x = solve(n, k, k) + 

 solve(n, 1, k);

 

 System.out.print(x);

}

}

 

// This code is contributed by Ritik Bansal  
  
---  
  
 __

 __

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 implementation to count the

# numbers upto N digits such that 

# no two zeros are adjacent 

dp = [[0] * 10 for j in range(15)]

 

# Function to count the numbers

# upto N digits such that no two

# zeros are adjacent 

def solve(n, last, k):

 

 # Condition to check if only 

 # one element remains 

 if (n == 1):

 

 # If last element is non 

 # zero, return K-1 

 if (last == k):

 return (k - 1)

 

 # If last element is 0 

 else:

 return 1

 

 # Condition to check if value 

 # calculated already 

 if (dp[n][last]):

 return dp[n][last]

 

 # If last element is non zero, 

 # then two cases arise, current

 # element can be either zero or

 # non zero

 if (last == k):

 

 # Memoize this case

 dp[n][last] = ((k - 1) *

 solve(n - 1, k, k) +

 (k - 1) *

 solve(n - 1, 1, k))

 

 return dp[n][last]

 

 # If last is 0, then current 

 # can only be non zero

 else:

 

 # Memoize and return

 dp[n][last] = solve(n - 1, k, k)

 return dp[n][last]

 

# Driver code

 

# Given N and K

n = 2

k = 3

 

# Function call

x = solve(n, k, k) + solve(n, 1, k)

 

print(x)

 

# This code is contributed by himanshu77  
  
---  
  
 __

 __

## C#

 __

 __  
 __

 __

 __  
 __  
 __

// C# implementation to count the

// numbers upto N digits such that

// no two zeros are adjacent

using System;

 

class GFG{

 

public static int [,]dp = new int[15, 10];

 

// Function to count the numbers 

// upto N digits such that

// no two zeros are adjacent

public static int solve(int n, int last, int k)

{

 

 // Condition to check if only

 // one element remains

 if (n == 1)

 {

 

 // If last element is non

 // zero, return K-1

 if (last == k)

 {

 return (k - 1);

 }

 

 // If last element is 0

 else

 {

 return 1;

 }

 }

 

 // Condition to check if 

 // value calculated already

 if (dp[n, last] == 1)

 return dp[n, last];

 

 // If last element is non zero,

 // then two cases arise, current 

 // element can be either zero 

 // or non zero

 if (last == k)

 {

 

 // Memoize this case

 return dp[n, last] = (k - 1) *

 solve(n - 1, k, k) + 

 (k - 1) * 

 solve(n - 1, 1, k);

 }

 

 // If last is 0, then current

 // can only be non zero

 else

 {

 

 // Memoize and return

 return dp[n, last] = solve(n - 1, k, k);

 }

}

 

// Driver Code

public static void Main(string[] args)

{

 

 // Given N and K

 int n = 2, k = 3;

 

 // Function Call

 int x = solve(n, k, k) + 

 solve(n, 1, k);

 

 Console.WriteLine(x);

}

}

 

// This code is contributed by SoumikMondal  
  
---  
  
 __

 __

 **Output:**

    
    
    8
    

**Time Complexity:** _O(N)_  
**Auxiliary Space:** _O(N*10)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

