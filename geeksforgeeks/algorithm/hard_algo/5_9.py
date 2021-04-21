Count number of Special Set



An ordered set of integers is said to be a special set if for every element of
the set **X** , the set does not contain the element **X + 1**. Given an
integer **N** , the task is to find the number of special sets whose largest
element is not greater than **N**. Since, the number of special sets can be
very large, print the answer modulo **10 9 + 7**.

 **Example:**

>  **Input:** N = 3  
>  **Output:** 5  
> {1}, {2}, {3}, {1, 3} and {3, 1} are the  
> only special sets possible.
>
>  **Input:** N = 4  
>  **Output:** 10

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can be solved using dynamic programming. Create an
array **dp[][]** where **dp[i][j]** stores the number of special sets of
length **i** ending with **j**. Now, the recurrence relation will be:

  

  

> dp[i][j] = dp[i – 1][1] + dp[i – 1][2] + … + dp[i – 1][j – 2]  
> dp[i][j] can be computed in O(1) by taking the prefix sum of the previous
> dp[i – 1] once.

Now the total special sets of size **i** can be calculated by multiplying
**dp[i][n]** with **factorial(i)**.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <bits/stdc++.h>

using namespace std;

 

typedef long long ll;

 

const int MAX = 2 * 1000 + 10;

const int MOD = 1e9 + 7;

 

// To store the states of the dp

ll dp[MAX][MAX];

 

// Function to return (a + b) % MOD

ll sum(ll a, ll b)

{

 return ((a % MOD) + (b % MOD)) % MOD;

}

 

// Function to return (a * b) % MOD

ll mul(ll a, ll b)

{

 return ((a % MOD) * (b % MOD)) % MOD;

}

 

// Function to return the count

// of special sets

int cntSpecialSet(int n)

{

 

 // Fill the dp[][] array with the answer

 // for the special sets of size 1

 for (int i = 1; i <= n; i++) {

 dp[1][i] = 1;

 

 // Take prefix sum of the current row which

 // will be used to fill the next row

 dp[1][i] += dp[1][i - 1];

 }

 

 // Fill the rest of the dp[][] array

 for (int i = 2; i <= n; i++) {

 

 // Recurrence relation

 for (int j = 2; j <= n; j++) {

 dp[i][j] = dp[i - 1][j - 2];

 }

 

 // Calculate the prefix sum

 for (int j = 1; j <= n; j++) {

 dp[i][j] = sum(dp[i][j], dp[i][j - 1]);

 }

 }

 

 ll ways(1), ans(0);

 

 for (int i = 1; i <= n; i++) {

 

 // To find special set of size i

 ways = mul(ways, i);

 

 // Addition of special sets of all sizes

 ans = sum(ans, mul(ways, dp[i][n]));

 }

 

 return ans;

}

 

// Driver code

int main()

{

 int n = 3;

 

 cout << cntSpecialSet(n);

 

 return 0;

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

// Java implementation of the approach

import java.util.*;

 

class GFG 

{

static int MAX = 2 * 1000 + 10;

static int MOD = (int) (1e9 + 7);

 

// To store the states of the dp

static long [][]dp = new long[MAX][MAX];

 

// Function to return (a + b) % MOD

static long sum(long a, long b)

{

 return ((a % MOD) + (b % MOD)) % MOD;

}

 

// Function to return (a * b) % MOD

static long mul(long a, long b)

{

 return ((a % MOD) * (b % MOD)) % MOD;

}

 

// Function to return the count

// of special sets

static long cntSpecialSet(int n)

{

 

 // Fill the dp[][] array with the answer

 // for the special sets of size 1

 for (int i = 1; i <= n; i++) 

 {

 dp[1][i] = 1;

 

 // Take prefix sum of the current row which

 // will be used to fill the next row

 dp[1][i] += dp[1][i - 1];

 }

 

 // Fill the rest of the dp[][] array

 for (int i = 2; i <= n; i++) 

 {

 

 // Recurrence relation

 for (int j = 2; j <= n; j++) 

 {

 dp[i][j] = dp[i - 1][j - 2];

 }

 

 // Calculate the prefix sum

 for (int j = 1; j <= n; j++) 

 {

 dp[i][j] = sum(dp[i][j], dp[i][j - 1]);

 }

 }

 

 long ways = 1, ans = 0;

 

 for (int i = 1; i <= n; i++) 

 {

 

 // To find special set of size i

 ways = mul(ways, i);

 

 // Addition of special sets of all sizes

 ans = sum(ans, mul(ways, dp[i][n]));

 }

 

 return ans;

}

 

// Driver code

public static void main(String[] args)

{

 int n = 3;

 

 System.out.println(cntSpecialSet(n));

}

}

 

// This code is contributed by PrinciRaj1992  
  
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

# Python3 implementation of the approach

 

# Function to print the nodes having 

# maximum and minimum degree 

def minMax(edges, leng, n) : 

 

 # Map to store the degrees of every node 

 m = {};

 

 for i in range(leng) :

 m[edges[i][0]] = 0;

 m[edges[i][1]] = 0;

 

 for i in range(leng) :

 

 # Storing the degree for each node

 m[edges[i][0]] += 1;

 m[edges[i][1]] += 1; 

 

 # maxi and mini variables to store 

 # the maximum and minimum degree 

 maxi = 0; 

 mini = n; 

 

 for i in range(1, n + 1) :

 maxi = max(maxi, m[i]); 

 mini = min(mini, m[i]); 

 

 # Printing all the nodes 

 # with maximum degree 

 print("Nodes with maximum degree : ", 

 end = "")

 

 for i in range(1, n + 1) :

 if (m[i] == maxi) :

 print(i, end = " "); 

 

 print()

 

 # Printing all the nodes 

 # with minimum degree 

 print("Nodes with minimum degree : ", 

 end = "")

 

 for i in range(1, n + 1) :

 if (m[i] == mini) :

 print(i, end = " "); 

 

# Driver code 

if __name__ == "__main__" : 

 

 # Count of nodes and edges 

 n = 4; m = 6; 

 

 # The edge list 

 edges = [[ 1, 2 ], [ 1, 3 ], 

 [ 1, 4 ], [ 2, 3 ], 

 [ 2, 4 ], [ 3, 4 ]]; 

 

 minMax(edges, m, 4); 

 

# This code is contributed by AnkitRai01  
  
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

// C# implementation of the approach

using System;

 

class GFG 

{

 

static int MAX = 2 * 1000 + 10;

static int MOD = (int) (1e9 + 7);

 

// To store the states of the dp

static long [,]dp = new long[MAX, MAX];

 

// Function to return (a + b) % MOD

static long sum(long a, long b)

{

 return ((a % MOD) + (b % MOD)) % MOD;

}

 

// Function to return (a * b) % MOD

static long mul(long a, long b)

{

 return ((a % MOD) * (b % MOD)) % MOD;

}

 

// Function to return the count

// of special sets

static long cntSpecialSet(int n)

{

 

 // Fill the dp[,] array with the answer

 // for the special sets of size 1

 for (int i = 1; i <= n; i++) 

 {

 dp[1, i] = 1;

 

 // Take prefix sum of the current row which

 // will be used to fill the next row

 dp[1, i] += dp[1, i - 1];

 }

 

 // Fill the rest of the dp[,] array

 for (int i = 2; i <= n; i++) 

 {

 

 // Recurrence relation

 for (int j = 2; j <= n; j++) 

 {

 dp[i, j] = dp[i - 1, j - 2];

 }

 

 // Calculate the prefix sum

 for (int j = 1; j <= n; j++) 

 {

 dp[i, j] = sum(dp[i, j], dp[i, j - 1]);

 } 

 }

 

 long ways = 1, ans = 0;

 

 for (int i = 1; i <= n; i++) 

 {

 

 // To find special set of size i

 ways = mul(ways, i);

 

 // Addition of special sets of all sizes

 ans = sum(ans, mul(ways, dp[i, n]));

 }

 

 return ans;

}

 

// Driver code

public static void Main(String[] args)

{

 int n = 3;

 

 Console.WriteLine(cntSpecialSet(n));

}

}

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

