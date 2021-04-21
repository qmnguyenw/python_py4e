Color N boxes using M colors such that K boxes have different color from the
box on its left



Given **N** number of boxes arranged in a row and **M** number of colors. The
task is to find the number of ways to paint those **N** boxes using **M**
colors such that there are exactly **K** boxes with a color different from the
color of the box on its left. Print this answer modulo **998244353**.

 **Examples:**

>  **Input:** N = 3, M = 3, K = 0  
>  **Output:** 3  
> Since the value of K is zero, no box can have a different color from color
> of the box on its left. Thus, all boxes should be painted with same color
> and since there are 3 types of colors, so there are total 3 ways.
>
>  **Input:** N = 3, M = 2, K = 1  
>  **Output:** 4  
> Let’s number the colors as 1 and 2. Four possible sequences of painting 3
> boxes with 1 box having different color from color of box on its left are (1
> 2 2), (1 1 2), (2 1 1) (2 2 1)

 **Prerequisites :** Dynamic Programming

  

  

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can be solved using dynamic programming where
**dp[i][j]** will denote the number of ways to paint **i** boxes using **M**
colors such that there are exactly **j** boxes with a color different from the
color of the box on its left. For every current box except **1 st**, either we
can paint the same color as painted on its left box and solve for **dp[i –
1][j]** or we can paint it with remaining **M – 1** colors and solve for
**dp[i – 1][j – 1]** recursively.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP Program to Paint N boxes using M

// colors such that K boxes have color

// different from color of box on its left

#include <bits/stdc++.h>

using namespace std;

 

const int M = 1001;

const int MOD = 998244353;

 

int dp[M][M];

 

// This function returns the required number

// of ways where idx is the current index and

// diff is number of boxes having different

// color from box on its left

int solve(int idx, int diff, int N, int M, int K)

{

 // Base Case

 if (idx > N) {

 if (diff == K)

 return 1;

 return 0;

 }

 

 // If already computed

 if (dp[idx][ diff] != -1)

 return dp[idx][ diff];

 

 // Either paint with same color as

 // previous one

 int ans = solve(idx + 1, diff, N, M, K);

 

 // Or paint with remaining (M - 1)

 // colors

 ans += (M - 1) * solve(idx + 1, diff + 1, N, M, K);

 

 return dp[idx][ diff] = ans % MOD;

}

 

// Driver code

int main()

{

 int N = 3, M = 3, K = 0;

 memset(dp, -1, sizeof(dp));

 

 // Multiply M since first box can be

 // painted with any of the M colors and

 // start solving from 2nd box

 cout << (M * solve(2, 0, N, M, K)) << endl;

 

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

// Java Program to Paint N boxes using M

// colors such that K boxes have color

// different from color of box on its left

 

class GFG

{

 

 static int M = 1001;

 static int MOD = 998244353;

 

 static int[][] dp = new int[M][M];

 

 // This function returns the required number

 // of ways where idx is the current index and

 // diff is number of boxes having different

 // color from box on its left

 static int solve(int idx, int diff,

 int N, int M, int K)

 {

 // Base Case

 if (idx > N) 

 {

 if (diff == K)

 return 1;

 return 0;

 }

 

 // If already computed

 if (dp[idx][ diff] != -1)

 return dp[idx][ diff];

 

 // Either paint with same color as

 // previous one

 int ans = solve(idx + 1, diff, N, M, K);

 

 // Or paint with remaining (M - 1)

 // colors

 ans += (M - 1) * solve(idx + 1, 

 diff + 1, N, M, K);

 

 return dp[idx][ diff] = ans % MOD;

 }

 

 // Driver code

 public static void main (String[] args) 

 {

 int N = 3, M = 3, K = 0;

 for(int i = 0; i <= M; i++)

 for(int j = 0; j <= M; j++)

 dp[i][j] = -1;

 

 // Multiply M since first box can be

 // painted with any of the M colors and

 // start solving from 2nd box

 System.out.println((M * solve(2, 0, N, M, K)));

 }

}

 

// This code is contributed by mits  
  
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

# Python3 Program to Paint N boxes using M

# colors such that K boxes have color 

# different from color of box on its left 

 

M = 1001; 

MOD = 998244353; 

 

dp = [[-1]* M ] * M

 

# This function returns the required number 

# of ways where idx is the current index and 

# diff is number of boxes having different 

# color from box on its left 

def solve(idx, diff, N, M, K) :

 

 # Base Case 

 if (idx > N) : 

 if (diff == K) :

 return 1

 return 0

 

 # If already computed 

 if (dp[idx][ diff] != -1) :

 return dp[idx]; 

 

 # Either paint with same color as 

 # previous one 

 ans = solve(idx + 1, diff, N, M, K); 

 

 # Or paint with remaining (M - 1) 

 # colors 

 ans += (M - 1) * solve(idx + 1, diff + 1, N,
M, K); 

 

 dp[idx][ diff] = ans % MOD; 

 

 return dp[idx][ diff]

 

# Driver code 

if __name__ == "__main__" : 

 

 N = 3

 M = 3

 K = 0

 

 # Multiply M since first box can be 

 # painted with any of the M colors and 

 # start solving from 2nd box 

 print(M * solve(2, 0, N, M, K)) 

 

# This code is contributed by Ryuga  
  
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

// C# Program to Paint N boxes using M

// colors such that K boxes have color

// different from color of box on its left

using System;

class GFG

{

 

static int M = 1001;

static int MOD = 998244353;

 

static int[,] dp = new int[M, M];

 

// This function returns the required number

// of ways where idx is the current index and

// diff is number of boxes having different

// color from box on its left

static int solve(int idx, int diff,

 int N, int M, int K)

{

 // Base Case

 if (idx > N) 

 {

 if (diff == K)

 return 1;

 return 0;

 }

 

 // If already computed

 if (dp[idx, diff] != -1)

 return dp[idx, diff];

 

 // Either paint with same color as

 // previous one

 int ans = solve(idx + 1, diff, N, M, K);

 

 // Or paint with remaining (M - 1)

 // colors

 ans += (M - 1) * solve(idx + 1, 

 diff + 1, N, M, K);

 

 return dp[idx, diff] = ans % MOD;

}

 

// Driver code

public static void Main () 

{

 int N = 3, M = 3, K = 0;

 for(int i = 0; i <= M; i++)

 for(int j = 0; j <= M; j++)

 dp[i, j] = -1;

 

 // Multiply M since first box can be

 // painted with any of the M colors and

 // start solving from 2nd box

 Console.WriteLine((M * solve(2, 0, N, M, K)));

}

}

 

// This code is contributed by chandan_jnu  
  
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

// PHP Program to Paint N boxes using M

// colors such that K boxes have color

// different from color of box on its left

 

$M = 1001;

$MOD = 998244353;

 

$dp = array_fill(0, $M,

 array_fill(0, $M, -1));

 

// This function returns the required number

// of ways where idx is the current index 

// and diff is number of boxes having 

// different color from box on its left

function solve($idx, $diff, $N, $M, $K)

{

 global $dp, $MOD;

 

 // Base Case

 if ($idx > $N) 

 {

 if ($diff == $K)

 return 1;

 return 0;

 }

 

 // If already computed

 if ($dp[$idx][$diff] != -1)

 return $dp[$idx][$diff];

 

 // Either paint with same color 

 // as previous one

 $ans = solve($idx + 1, $diff, $N, $M, $K);

 

 // Or paint with remaining (M - 1)

 // colors

 $ans += ($M - 1) * solve($idx + 1,

 $diff + 1, $N, $M, $K);

 

 return $dp[$idx][$diff] = $ans % $MOD;

}

 

// Driver code

$N = 3;

$M = 3;

$K = 0;

 

// Multiply M since first box can be

// painted with any of the M colors and

// start solving from 2nd box

echo ($M * solve(2, 0, $N, $M, $K));

 

// This code is contributed by chandan_jnu

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

