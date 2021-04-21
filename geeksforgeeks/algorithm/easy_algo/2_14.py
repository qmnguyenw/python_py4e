Count ways to reach end from start stone with at most K jumps at each step



Given **N** stones in a row from left to right. From each stone, you can jump
to at most **K** stones. The task is to find the total number of ways to reach
from **sth** stone to **Nth** stone.

 **Examples:**

>  **Input:** N = 5, s = 2, K = 2  
>  **Output:** Total Ways = 3  
>  **Explanation:**  
>  Assume s1, s2, s3, s4, s5 be the stones. The possible paths from 2nd stone
> to 5th stone:  
> s2 -> s3 -> s4 -> s5  
> s2 -> s4 -> s5  
> s2 -> s3 -> s5  
> Hence total number of ways = 3
>
>  **Input:** N = 8, s = 1, K = 3  
>  **Output:** Total Ways = 44

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  1. Let assume **dp[i]** be the number of ways to reach **ith** stone.
  2. Since there are atmost **K jumps** , So the **ith** stone can be reach by all it’s previous **K** stones.
  3. Iterate for all possible **K jumps** and keep adding this possible combination to the array **dp[]**.
  4. Then the total number of possible ways to reach **Nth** node from **sth** stone will be **dp[N-1]**.
  5. For Example:  

> Let N = 5, s = 2, K = 2, then we have to reach Nth stone from sth stone.  
> Let dp[N+1] is the array that stores the number of paths to reach the Nth
> Node from sth stone.  
> Initially, dp[] = { 0, 0, 0, 0, 0, 0 } and dp[s] = 1, then  
> dp[] = { 0, 0, 1, 0, 0, 0 }  
> To reach the 3rd,  
> There is only 1 way with at most 2 jumps i.e., from stone 2(with jump = 1).
> Update dp[3] = dp[2]  
> dp[] = { 0, 0, 1, 1, 0, 0 }
>
> To reach the 4th stone,  
> The two ways with at most 2 jumps i.e., from stone 2(with jump = 2) and
> stone 3(jump = 1). Update dp[4] = dp[3] + dp[2]  
> dp[] = { 0, 0, 1, 1, 2, 0 }
>
> To reach the 5th stone,  
> The two ways with at most 2 jumps i.e., from stone 3(with jump = 2) and
> stone 4(with jump = 1). Update dp[5] = dp[4] + dp[3]  
> dp[] = { 0, 0, 1, 1, 2, 3 }
>
> Now dp[N] = 3 is the number of ways to reach Nth stone from sth stone.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find total no.of ways

// to reach nth step

#include "bits/stdc++.h"

using namespace std;

 

// Function which returns total no.of ways

// to reach nth step from sth steps

int TotalWays(int n, int s, int k)

{

 // Initialize dp array

 int dp[n];

 

 // filling all the elements with 0

 memset(dp, 0, sizeof(dp));

 

 // Initialize (s-1)th index to 1

 dp[s - 1] = 1;

 

 // Iterate a loop from s to n

 for (int i = s; i < n; i++) {

 

 // starting range for counting ranges

 int idx = max(s - 1, i - k);

 

 // Calculate Maximum moves to

 // Reach ith step

 for (int j = idx; j < i; j++) {

 dp[i] += dp[j];

 }

 }

 

 // For nth step return dp[n-1]

 return dp[n - 1];

}

 

// Driver Code

int main()

{

 // no of steps

 int n = 5;

 

 // Atmost steps allowed

 int k = 2;

 

 // starting range

 int s = 2;

 cout << "Total Ways = "

 << TotalWays(n, s, k);

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

// Java program to find total no.of ways

// to reach nth step

class GFG{

 

// Function which returns total no.of ways

// to reach nth step from sth steps

static int TotalWays(int n, int s, int k)

{

 // Initialize dp array

 int []dp = new int[n];

 

 // Initialize (s-1)th index to 1

 dp[s - 1] = 1;

 

 // Iterate a loop from s to n

 for (int i = s; i < n; i++) {

 

 // starting range for counting ranges

 int idx = Math.max(s - 1, i - k);

 

 // Calculate Maximum moves to

 // Reach ith step

 for (int j = idx; j < i; j++) {

 dp[i] += dp[j];

 }

 }

 

 // For nth step return dp[n-1]

 return dp[n - 1];

}

 

// Driver Code

public static void main(String[] args)

{

 // no of steps

 int n = 5;

 

 // Atmost steps allowed

 int k = 2;

 

 // starting range

 int s = 2;

 System.out.print("Total Ways = "

 + TotalWays(n, s, k));

}

}

 

// This code is contributed by sapnasingh4991  
  
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

# Python 3 program to find total no.of ways

# to reach nth step

 

# Function which returns total no.of ways

# to reach nth step from sth steps

def TotalWays(n, s, k):

 

 # Initialize dp array

 dp = [0]*n

 

 # Initialize (s-1)th index to 1

 dp[s - 1] = 1

 

 # Iterate a loop from s to n

 for i in range(s, n):

 

 # starting range for counting ranges

 idx = max(s - 1, i - k)

 

 # Calculate Maximum moves to

 # Reach ith step

 for j in range( idx, i) :

 dp[i] += dp[j]

 

 # For nth step return dp[n-1]

 return dp[n - 1]

 

# Driver Code

if __name__ == "__main__":

 # no of steps

 n = 5

 

 # Atmost steps allowed

 k = 2

 

 # starting range

 s = 2

 print("Total Ways = ", TotalWays(n, s, k))

 

# This code is contributed by chitranayal  
  
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

// C# program to find total no.of ways

// to reach nth step

using System;

 

class GFG{

 

 // Function which returns total no.of ways

 // to reach nth step from sth steps

 static int TotalWays(int n, int s, int k)

 {

 // Initialize dp array

 int []dp = new int[n];

 

 // Initialize (s-1)th index to 1

 dp[s - 1] = 1;

 

 // Iterate a loop from s to n

 for (int i = s; i < n; i++) {

 

 // starting range for counting ranges

 int idx = Math.Max(s - 1, i - k);

 

 // Calculate Maximum moves to

 // Reach ith step

 for (int j = idx; j < i; j++) {

 dp[i] += dp[j];

 }

 }

 

 // For nth step return dp[n-1]

 return dp[n - 1];

 }

 

 // Driver Code

 public static void Main(string[] args)

 {

 // no of steps

 int n = 5;

 

 // Atmost steps allowed

 int k = 2;

 

 // starting range

 int s = 2;

 Console.Write("Total Ways = "+ TotalWays(n, s, k));

 }

}

 

// This code is contributed by Yash_R  
  
---  
  
 __

 __

 **Output:**

    
    
    Total Ways = 3
    

**Time Complexity:** O(N2), where N is the number of stones.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

