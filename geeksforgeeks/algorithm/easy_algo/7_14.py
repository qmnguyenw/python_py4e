Minimum cost to reach the top of the floor by climbing stairs



Given N non-negative integers which signifies the cost of the moving from each
stair. Paying the cost at i-th step, you can either climb one or two steps.
Given that one can start from the 0-the step or 1-the step, the task is to
find the minimum cost to reach the top of the floor(N+1) by climbing N stairs.

**Examples:**

    
    
    Input: a[] = { 16, 19, 10, 12, 18 }
    Output: 31
    Start from 19 and then move to 12. 
    
    Input: a[] = {2, 5, 3, 1, 7, 3, 4}
    Output: 9 
    2->3->1->3

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Let dp[i] be the cost to climb the i-th staircase to from 0-th
or 1-th step. Hence _**dp[i] = cost[i] + min(dp[i-1], dp[i-2])**_. Since
dp[i-1] and dp[i-2] is needed to compute the cost of traveling from i-th step,
a bottom-up approach can be used to solve the problem. The answer will be the
minimum of cost of reaching n-1th stair and n-2th stair. Compute the dp[]
array in bottom-up manner.

Below is the implementation of the above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the minimum

// cost required to reach the n-th floor

#include <bits/stdc++.h>

using namespace std;

// function to find the minimum cost

// to reach N-th floor

int minimumCost(int cost[], int n)

{

 // declare an array

 int dp[n];

 // base case

 if (n == 1)

 return cost[0];

 // initially to climb till 0-th

 // or 1th stair

 dp[0] = cost[0];

 dp[1] = cost[1];

 // iterate for finding the cost

 for (int i = 2; i < n; i++) {

 dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i];

 }

 // return the minimum

 return min(dp[n - 2], dp[n - 1]);

}

// Driver Code

int main()

{

 int a[] = { 16, 19, 10, 12, 18 };

 int n = sizeof(a) / sizeof(a[0]);

 cout << minimumCost(a, n);

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

// Java program to find the

// minimum cost required to

// reach the n-th floor

import java.io.*;

import java.util.*;

class GFG

{

// function to find

// the minimum cost

// to reach N-th floor

static int minimumCost(int cost[],

 int n)

{

 // declare an array

 int dp[] = new int[n];

 // base case

 if (n == 1)

 return cost[0];

 // initially to

 // climb till 0-th

 // or 1th stair

 dp[0] = cost[0];

 dp[1] = cost[1];

 // iterate for finding the cost

 for (int i = 2; i < n; i++)

 {

 dp[i] = Math.min(dp[i - 1],

 dp[i - 2]) + cost[i];

 }

 // return the minimum

 return Math.min(dp[n - 2],

 dp[n - 1]);

}

// Driver Code

public static void main(String args[])

{

 int a[] = { 16, 19, 10, 12, 18 };

 int n = a.length;

 System.out.print(minimumCost(a, n));

}

}  
  
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

# Python3 program to find

# the minimum cost required

# to reach the n-th floor

# function to find the minimum

# cost to reach N-th floor

def minimumCost(cost, n):

 # declare an array

 dp = [None]*n

 # base case

 if n == 1:

 return cost[0]

 # initially to climb

 # till 0-th or 1th stair

 dp[0] = cost[0]

 dp[1] = cost[1]

 # iterate for finding the cost

 for i in range(2, n):

 dp[i] = min(dp[i - 1],

 dp[i - 2]) + cost[i]

 # return the minimum

 return min(dp[n - 2], dp[n - 1])

# Driver Code

if __name__ == "__main__":

 a = [16, 19, 10, 12, 18 ]

 n = len(a)

 print(minimumCost(a, n))

# This code is contributed

# by ChitraNayal  
  
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

// C# program to find the

// minimum cost required to

// reach the n-th floor

using System;

class GFG

{

// function to find

// the minimum cost

// to reach N-th floor

static int minimumCost(int[] cost,

 int n)

{

 // declare an array

 int []dp = new int[n];

 // base case

 if (n == 1)

 return cost[0];

 // initially to

 // climb till 0-th

 // or 1th stair

 dp[0] = cost[0];

 dp[1] = cost[1];

 // iterate for finding the cost

 for (int i = 2; i < n; i++)

 {

 dp[i] = Math.Min(dp[i - 1],

 dp[i - 2]) + cost[i];

 }

 // return the minimum

 return Math.Min(dp[n - 2],

 dp[n - 1]);

}

// Driver Code

public static void Main()

{

 int []a = { 16, 19, 10, 12, 18 };

 int n = a.Length;

 Console.WriteLine(minimumCost(a, n));

}

}

// This code is contributed

// by Subhadeep  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP program to find the

// minimum cost required

// to reach the n-th floor

// function to find the minimum

// cost to reach N-th floor

function minimumCost(&$cost, $n)

{

 // declare an array

 // base case

 if ($n == 1)

 return $cost[0];

 // initially to climb

 // till 0-th or 1th stair

 $dp[0] = $cost[0];

 $dp[1] = $cost[1];

 // iterate for finding

 // the cost

 for ($i = 2; $i < $n; $i++)

 {

 $dp[$i] = min($dp[$i - 1],

 $dp[$i - 2]) +

 $cost[$i];

 }

 // return the minimum

 return min($dp[$n - 2],

 $dp[$n - 1]);

}

// Driver Code

$a = array(16, 19, 10, 12, 18);

$n = sizeof($a);

echo(minimumCost($a, $n));

 

// This code is contributed

// by Shivi_Aggarwal

?>  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    31

