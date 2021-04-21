Ways to form an array having integers in given range such that total sum is
divisible by 2



Given three positive integers **N** , **L** and **R**. The task is to find the
number of ways to form an array of size **N** where each element lies in the
range **[L, R]** such that the total sum of all the elements of the array is
divisible by **2**.

 **Examples:**

>  **Input:** N = 2, L = 1, R = 3  
>  **Output:** 5  
> Possible arrays having sum of all elements divisible by 2 are  
> [1, 1], [2, 2], [1, 3], [3, 1] and [3, 3]
>
>  **Input:** N = 3, L = 2, R = 2  
>  **Output:** 1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to find the count of numbers having remainder 0 and
1 modulo 2 separately lying between L and R. This count can be calculated as
follows:

  

  

> We need to count numbers between range having remainder 1 modulo 2  
>  **F** = First number in range of required type  
>  **L** = Last number in range of required type  
>  **Count = (L – F) / 2**  
>  cnt0, and cnt1 represents Count of numbers between range of each type.

Then, using dynamic programming we can solve this problem. Let **dp[i][j]**
denotes the number of ways where the sum of first i numbers modulo 2 is equal
to j. Suppose we need to calculate dp[i][0], then it will have the following
recurrence relation: **dp[i][0] = (cnt0 * dp[i – 1][0] + cnt1 * dp[i –
1][1])**. First term represents the number of ways upto (i – 1) having sum
remainder as 0, so we can place cnt0 numbers in ith position such that sum
remainder still remains 0. Second term represents the number of ways upto (i –
1) having sum remainder as 1, so we can place cnt1 numbers in ith position to
such that sum remainder becomes 0. Similarly, we can calculate for dp[i][1].  
Final answer will be denoted by **dp[N][0]**.

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

 

// Function to return the number of ways to

// form an array of size n such that sum of

// all elements is divisible by 2

int countWays(int n, int l, int r)

{

 int tL = l, tR = r;

 

 // Represents first and last numbers

 // of each type (modulo 0 and 1)

 int L[2] = { 0 }, R[2] = { 0 };

 L[l % 2] = l, R[r % 2] = r;

 

 l++, r--;

 

 if (l <= tR && r >= tL)

 L[l % 2] = l, R[r % 2] = r;

 

 // Count of numbers of each type between range

 int cnt0 = 0, cnt1 = 0;

 if (R[0] && L[0])

 cnt0 = (R[0] - L[0]) / 2 + 1;

 if (R[1] && L[1])

 cnt1 = (R[1] - L[1]) / 2 + 1;

 

 int dp[n][2];

 

 // Base Cases

 dp[1][0] = cnt0;

 dp[1][1] = cnt1;

 for (int i = 2; i <= n; i++) {

 

 // Ways to form array whose sum upto

 // i numbers modulo 2 is 0

 dp[i][0] = (cnt0 * dp[i - 1][0]

 + cnt1 * dp[i - 1][1]);

 

 // Ways to form array whose sum upto

 // i numbers modulo 2 is 1

 dp[i][1] = (cnt0 * dp[i - 1][1]

 + cnt1 * dp[i - 1][0]);

 }

 

 // Return the required count of ways

 return dp[n][0];

}

 

// Driver Code

int main()

{

 int n = 2, l = 1, r = 3;

 cout << countWays(n, l, r);

 

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

class GFG

{

 

// Function to return the number of ways to

// form an array of size n such that sum of

// all elements is divisible by 2

static int countWays(int n, int l, int r)

{

 int tL = l, tR = r;

 

 // Represents first and last numbers

 // of each type (modulo 0 and 1)

 int[] L = new int[3];

 int[] R = new int[3];

 L[l % 2] = l;

 R[r % 2] = r;

 

 l++;

 r--;

 

 if (l <= tR && r >= tL)

 {

 L[l % 2] = l;

 R[r % 2] = r;

 }

 

 // Count of numbers of each type between range

 int cnt0 = 0, cnt1 = 0;

 if (R[0] > 0 && L[0] > 0)

 cnt0 = (R[0] - L[0]) / 2 + 1;

 if (R[1] > 0 && L[1] > 0)

 cnt1 = (R[1] - L[1]) / 2 + 1;

 

 int[][] dp = new int[n + 1][3];

 

 // Base Cases

 dp[1][0] = cnt0;

 dp[1][1] = cnt1;

 for (int i = 2; i <= n; i++) 

 {

 

 // Ways to form array whose sum upto

 // i numbers modulo 2 is 0

 dp[i][0] = (cnt0 * dp[i - 1] [0]

 + cnt1 * dp[i - 1][1]);

 

 // Ways to form array whose sum upto

 // i numbers modulo 2 is 1

 dp[i][1] = (cnt0 * dp[i - 1][1]

 + cnt1 * dp[i - 1][0]);

 }

 

 // Return the required count of ways

 return dp[n][0];

}

 

// Driver Code

public static void main(String[] args)

{

 int n = 2, l = 1, r = 3;

 System.out.println(countWays(n, l, r));

}

}

 

// This code is contributed by Code_Mech.  
  
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

 

# Function to return the number of ways to

# form an array of size n such that sum of

# all elements is divisible by 2

def countWays(n, l, r):

 

 tL, tR = l, r

 

 # Represents first and last numbers

 # of each type (modulo 0 and 1)

 L = [0 for i in range(2)]

 R = [0 for i in range(2)]

 

 L[l % 2] = l

 R[r % 2] = r

 

 l += 1

 r -= 1

 

 if (l <= tR and r >= tL):

 L[l % 2], R[r % 2] = l, r

 

 # Count of numbers of each type 

 # between range

 cnt0, cnt1 = 0, 0

 if (R[0] and L[0]):

 cnt0 = (R[0] - L[0]) // 2 + 1

 if (R[1] and L[1]):

 cnt1 = (R[1] - L[1]) // 2 + 1

 

 dp = [[0 for i in range(2)] 

 for i in range(n + 1)]

 

 # Base Cases

 dp[1][0] = cnt0

 dp[1][1] = cnt1

 for i in range(2, n + 1):

 

 # Ways to form array whose sum 

 # upto i numbers modulo 2 is 0

 dp[i][0] = (cnt0 * dp[i - 1][0] +

 cnt1 * dp[i - 1][1])

 

 # Ways to form array whose sum upto

 # i numbers modulo 2 is 1

 dp[i][1] = (cnt0 * dp[i - 1][1] +

 cnt1 * dp[i - 1][0])

 

 # Return the required count of ways

 return dp[n][0]

 

# Driver Code

n, l, r = 2, 1, 3

print(countWays(n, l, r))

 

# This code is contributed 

# by Mohit Kumar  
  
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

 

// Function to return the number of ways to

// form an array of size n such that sum of

// all elements is divisible by 2

static int countWays(int n, int l, int r)

{

 int tL = l, tR = r;

 

 // Represents first and last numbers

 // of each type (modulo 0 and 1)

 int[] L = new int[3];

 int[] R = new int[3];

 L[l % 2] = l;

 R[r % 2] = r;

 

 l++;

 r--;

 

 if (l <= tR && r >= tL)

 {

 L[l % 2] = l;

 R[r % 2] = r;

 }

 

 // Count of numbers of each type between range

 int cnt0 = 0, cnt1 = 0;

 if (R[0] > 0 && L[0] > 0)

 cnt0 = (R[0] - L[0]) / 2 + 1;

 if (R[1] > 0 && L[1] > 0)

 cnt1 = (R[1] - L[1]) / 2 + 1;

 

 int[,] dp=new int[n + 1, 3];

 

 // Base Cases

 dp[1, 0] = cnt0;

 dp[1, 1] = cnt1;

 for (int i = 2; i <= n; i++) 

 {

 

 // Ways to form array whose sum upto

 // i numbers modulo 2 is 0

 dp[i, 0] = (cnt0 * dp[i - 1, 0]

 + cnt1 * dp[i - 1, 1]);

 

 // Ways to form array whose sum upto

 // i numbers modulo 2 is 1

 dp[i, 1] = (cnt0 * dp[i - 1, 1]

 + cnt1 * dp[i - 1, 0]);

 }

 

 // Return the required count of ways

 return dp[n, 0];

}

 

// Driver Code

static void Main()

{

 int n = 2, l = 1, r = 3;

 Console.WriteLine(countWays(n, l, r));

}

}

 

// This code is contributed by mits  
  
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

// PHP implementation of the approach 

 

// Function to return the number of ways to 

// form an array of size n such that sum of 

// all elements is divisible by 2 

function countWays($n, $l, $r) 

{ 

 $tL = $l;

 $tR = $r; 

 

 $L = array_fill(0, 2, 0);

 $R = array_fill(0, 2, 0);

 

 // Represents first and last numbers 

 // of each type (modulo 0 and 1) 

 $L[$l % 2] = $l;

 $R[$r % 2] = $r; 

 

 $l++;

 $r--; 

 

 if ($l <= $tR && $r >= $tL) 

 {

 $L[$l % 2] = $l;

 $R[$r % 2] = $r; 

 }

 

 // Count of numbers of each type

 // between range 

 $cnt0 = 0;

 $cnt1 = 0; 

 if ($R[0] && $L[0]) 

 $cnt0 = ($R[0] - $L[0]) / 2 + 1;

 

 if ($R[1] && $L[1]) 

 $cnt1 = ($R[1] - $L[1]) / 2 + 1; 

 

 $dp = array();

 

 // Base Cases 

 $dp[1][0] = $cnt0; 

 $dp[1][1] = $cnt1; 

 for ($i = 2; $i <= $n; $i++) 

 { 

 

 // Ways to form array whose sum upto 

 // i numbers modulo 2 is 0 

 $dp[$i][0] = ($cnt0 * $dp[$i - 1][0] + 

 $cnt1 * $dp[$i - 1][1]); 

 

 // Ways to form array whose sum upto 

 // i numbers modulo 2 is 1 

 $dp[$i][1] = ($cnt0 * $dp[$i - 1][1] + 

 $cnt1 * $dp[$i - 1][0]); 

 } 

 

 // Return the required count of ways 

 return $dp[$n][0]; 

} 

 

// Driver Code 

$n = 2;

$l = 1;

$r = 3; 

 

echo countWays($n, $l, $r); 

 

// This code is contributed by Ryuga

?>  
  
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

