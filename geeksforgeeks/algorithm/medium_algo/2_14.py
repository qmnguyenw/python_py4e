Extended Knapsack Problem



Given **N** items, each item having a given weight **C i** and a profit value
**P i**, the task is to maximize the profit by selecting a maximum of **K**
items adding up to a maximum weight **W**.

 **Examples:**

> **Input:** N = 5, P[] = {2, 7, 1, 5, 3}, C[] = {2, 5, 2, 3, 4}, W = 8, K =
> 2.  
> **Output:** 12  
> **Explanation:**  
> Here, the maximum possible profit is when we take 2 items: item2 (P[1] = 7
> and C[1] = 5) and item4 (P[3] = 5 and C[3] = 3).  
> Hence, maximum profit = 7 + 5 = 12  
>  **Input:** N = 5, P[] = {2, 7, 1, 5, 3}, C[] = {2, 5, 2, 3, 4}, W = 1, K =
> 2  
> **Output:** 0  
> **Explanation:** All weights are greater than 1. Hence, no item can be
> picked.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The dynamic programming approach is preferred over the general
recursion approach. Let us first verify that the conditions of DP are still
satisfied.

  1. **Overlapping sub-problems:** When the recursive solution is tried, 1 item is added first and the solution set is (1), (2), …(n). In the second iteration we have (1, 2) and so on where (1) and (2) are recalculated. Hence there will be overlapping solutions.
  2.  **Optimal substructure:** Overall, each item has only two choices, either it can be included in the solution or denied. For a particular subset of z elements, the solution for (z+1)th element can either have a solution corresponding to the z elements or the (z+1)th element can be added if it doesn’t exceed the knapsack constraints. Either way, the optimal substructure property is satisfied.

Let’s derive the recurrence. Let us consider a 3-dimensional table
**dp[N][W][K]** , where **N** is the number of elements, **W** is the maximum
weight capacity and **K** is the maximum number of items allowed in the
knapsack. Let’s define a state **dp[i][j][k]** where **i** denotes that we are
considering the **i th** element, **j** denotes the current weight filled, and
**k** denotes the number of items filled until now.  
For every state **dp[i][j][k]** , the profit is either that of the previous
state (when the current state is not included) or the profit of the current
item added to that of the previous state (when the current item is selected).
Hence, the recurrence relation is:  

  

  

> dp[i][j][k] = max( dp[i-1][j][k], dp[i-1][j-W[i-1]][k-1] + P[i])  
>

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code for the extended

// Knapsack Approach

#include <bits/stdc++.h>

using namespace std;

// To store the dp values

int dp[100][100][100];

int maxProfit(int profit[],

 int weight[],

 int n, int max_W,

 int max_E)

{

 // for each element given

 for (int i = 1; i <= n; i++)

 {

 // For each possible

 // weight value

 for (int j = 1; j <= max_W; j++)

 {

 // For each case where

 // the total elements are

 // less than the constraint

 for (int k = 1; k <= max_E; k++)

 {

 // To ensure that we dont

 // go out of the array

 if (j >= weight[i-1])

 {

 dp[i][j][k]

 = max(dp[i - 1][j][k],

 dp[i - 1][j -

 weight[i-1]][k - 1]+

 profit[i-1]);

 }

 else

 {

 dp[i][j][k]

 = dp[i - 1][j][k];

 }

 }

 }

 }

 return dp[n][max_W][max_E];

}

// Driver Code

int main()

{

 memset(dp, 0, sizeof(dp));

 int n = 5;

 int profit[] = { 2, 7, 1, 5, 3 };

 int weight[] = { 2, 5, 2, 3, 4 };

 int max_weight = 8;

 int max_element = 2;

 cout << maxProfit(profit,

 weight, n,

 max_weight,

 max_element)

 << "\n";

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

// Java code for the extended

// Knapsack Approach

import java.util.*;

import java.lang.*;

import java.io.*;

class GFG{

// To store the dp values

static int[][][] dp = new int[100][100][100];

static int maxProfit(int profit[],

 int weight[],

 int n, int max_W,

 int max_E)

{

 

 // for each element given

 for(int i = 1; i <= n; i++)

 {

 

 // For each possible

 // weight value

 for(int j = 1; j <= max_W; j++)

 {

 

 // For each case where

 // the total elements are

 // less than the constraint

 for(int k = 1; k <= max_E; k++)

 {

 

 // To ensure that we dont

 // go out of the array

 if (j >= weight[i - 1])

 {

 dp[i][j][k] = Math.max(dp[i - 1][j][k],

 dp[i - 1][j -

 weight[i - 1]][k - 1] +

 profit[i - 1]);

 }

 else

 {

 dp[i][j][k] = dp[i - 1][j][k];

 }

 }

 }

 }

 return dp[n][max_W][max_E];

}

 

// Driver code

public static void main(String[] args)

{

 int n = 5;

 int profit[] = { 2, 7, 1, 5, 3 };

 int weight[] = { 2, 5, 2, 3, 4 };

 int max_weight = 8;

 int max_element = 2;

 

 System.out.println(maxProfit(profit,

 weight, n,

 max_weight,

 max_element)); 

}

}

// This code is contributed by offbeat  
  
---  
  
 __

 __

 **Output:**

    
    
    12
    
    
    
    
    
    
    
    

**Time Complexity:** _O(N * W * K)_  
**Auxiliary Space:** _O(N * W * K)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

