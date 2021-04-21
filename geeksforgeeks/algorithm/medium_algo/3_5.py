Count of Binary strings of length N having atmost M consecutive 1s or 0s
alternatively exactly K times



Given three integers, **N, K** and **M.** The task is to find out the number
of **binary strings** of length **N** which always starts with **1** , in
which there can be at most **M** consecutive 1’s or 0’s and they alternate
exactly **K** times.

 **Examples:**

>  **Input:** N = 5, K = 3, M = 2  
>  **Output:** 3  
> The 3 configurations are:  
> 11001  
> 10011  
> 11011  
>  **Explanation:**  
>  Notice that the groups of 1’s and 0’s alternate exactly K times
>
>  **Input:** N = 7, K = 4, M = 3  
>  **Output:** 16

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Since this problem involves both overlapping sub-problem and
optimal substructure. So, this problem can be solved using dynamic
programming.

  

  

  *  **Sub-problem** : **DP[i][j]** represents the number of binary strings upto length **i** having **j** alternating groups till now. So, to calculate dp[N][K] if we know the value of dp[n-j][k-1], then we can easily get the result by summing up the sub-problem value over j = 1 to m (DP[N][K] represents the final answer).

As shown below in the recursion tree diagram, it is observed many sub-problem
overlaps. So, the result needs to be cached to avoid redundant calculations.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200511212349/recursion-tree-GFG-DP-1.png)

  *  **Optimal substructure:**  
![     $dp\[i\]\[j\]=$$\\sum_{j=1}^{M} f\(N-j, K-1\)
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-82f50b7780ce69c6fffb54bf5b2617dd_l3.png)

  *  **By following the top-down DP approach:**  
As we can have a group which can be atmost of the length **M** , so we iterate
on every possible length and recur with new **N** and decreasing **K** by 1,
as a new group is formed. Solution to sub-problem is cached and summed up to
give final result dp[N][K].

  *  **Base Case:**
    1. When N is 0 and K is 0, then return 1
    2. When N is 0 but K is not 0, then return 0
    3. When N is not 0 but K is 0, then return 0
    4. When both are negative, return 0

Below is the implementation of above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the count

// of Binary strings of length N

// having atmost M consecutive 1s or 0s

// alternatively exactly K times

 

#include <bits/stdc++.h>

using namespace std;

 

// Array to contain the final result

int dp[1000][1000];

 

// Function to get the number

// of desirable binary strings

int solve(int n, int k, int m)

{

 

 // if we reach end of string

 // and groups are exhausted,

 // return 1

 if (n == 0 && k == 0)

 return 1;

 

 // if length is exhausted but

 // groups are still to be made,

 // return 0

 if (n == 0 && k != 0)

 return 0;

 

 // if length is not exhausted

 // but groups are exhausted,

 // return 0

 if (n != 0 && k == 0)

 return 0;

 

 // if both are negative

 // just return 0

 if (n < 0 || k < 0)

 return 0;

 

 // if already calculated,

 // return it

 if (dp[n][k])

 return dp[n][k];

 

 // initialise answer

 // for each state

 int ans = 0;

 

 // loop through every

 // possible m

 for (int j = 1; j <= m; j++) {

 ans += solve(n - j, k - 1, m);

 }

 return dp[n][k] = ans;

}

 

// Driver code

int main()

{

 

 int N = 7, K = 4, M = 3;

 cout << solve(N, K, M);

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

// Java program to find the count of

// Binary Strings of length N having

// atmost M consecutive 1s or 0s

// alternatively exactly K times

import java.util.*;

 

class GFG{

 

// Array to contain the final result

static int [][]dp = new int[1000][1000];

 

// Function to get the number

// of desirable binary strings

static int solve(int n, int k, int m)

{

 

 // If we reach end of string

 // and groups are exhausted,

 // return 1

 if (n == 0 && k == 0)

 return 1;

 

 // If length is exhausted but

 // groups are still to be made,

 // return 0

 if (n == 0 && k != 0)

 return 0;

 

 // If length is not exhausted

 // but groups are exhausted,

 // return 0

 if (n != 0 && k == 0)

 return 0;

 

 // If both are negative

 // just return 0

 if (n < 0 || k < 0)

 return 0;

 

 // If already calculated,

 // return it

 if (dp[n][k] > 0)

 return dp[n][k];

 

 // Initialise answer

 // for each state

 int ans = 0;

 

 // Loop through every

 // possible m

 for(int j = 1; j <= m; j++)

 {

 ans += solve(n - j, k - 1, m);

 }

 return dp[n][k] = ans;

}

 

// Driver code

public static void main(String[] args)

{

 int N = 7, K = 4, M = 3;

 System.out.print(solve(N, K, M));

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find the count

# of Binary strings of length N 

# having atmost M consecutive 1s or 

# 0s alternatively exactly K times 

 

# List to contain the final result 

rows, cols = (1000, 1000) 

dp = [[0 for i in range(cols)] 

 for j in range(rows)]

 

# Function to get the number 

# of desirable binary strings 

def solve(n, k, m):

 

 # If we reach end of string 

 # and groups are exhausted, 

 # return 1

 if n == 0 and k == 0:

 return 1

 

 # If length is exhausted but 

 # groups are still to be made, 

 # return 0 

 if n == 0 and k != 0: 

 return 0

 

 # If length is not exhausted 

 # but groups are exhausted, 

 # return 0 

 if n != 0 and k == 0: 

 return 0

 

 # If both are negative 

 # just return 0 

 if n < 0 or k < 0: 

 return 0

 

 # If already calculated, 

 # return it 

 if dp[n][k]:

 return dp[n][k]

 

 # Initialise answer 

 # for each state 

 ans = 0

 

 # Loop through every 

 # possible m 

 for j in range(1, m + 1):

 ans = ans + solve(n - j,

 k - 1, m)

 dp[n][k] = ans

 

 return dp[n][k]

 

# Driver code 

N = 7

K = 4

M = 3

 

print(solve(N, K, M))

 

# This code is contributed by ishayadav181  
  
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

// C# program to find the count of

// binary strings of length N having

// atmost M consecutive 1s or 0s

// alternatively exactly K times

using System;

 

class GFG{

 

// Array to contain the readonly result

static int [,]dp = new int[1000, 1000];

 

// Function to get the number

// of desirable binary strings

static int solve(int n, int k, int m)

{

 

 // If we reach end of string

 // and groups are exhausted,

 // return 1

 if (n == 0 && k == 0)

 return 1;

 

 // If length is exhausted but

 // groups are still to be made,

 // return 0

 if (n == 0 && k != 0)

 return 0;

 

 // If length is not exhausted

 // but groups are exhausted,

 // return 0

 if (n != 0 && k == 0)

 return 0;

 

 // If both are negative

 // just return 0

 if (n < 0 || k < 0)

 return 0;

 

 // If already calculated,

 // return it

 if (dp[n, k] > 0)

 return dp[n, k];

 

 // Initialise answer

 // for each state

 int ans = 0;

 

 // Loop through every

 // possible m

 for(int j = 1; j <= m; j++)

 {

 ans += solve(n - j, k - 1, m);

 }

 return dp[n, k] = ans;

}

 

// Driver code

public static void Main(String[] args)

{

 int N = 7, K = 4, M = 3;

 

 Console.Write(solve(N, K, M));

}

}

 

// This code is contributed by gauravrajput1  
  
---  
  
 __

 __

 **Output:**

    
    
    16
    

_**Time complexity:** O(N*K*M)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

