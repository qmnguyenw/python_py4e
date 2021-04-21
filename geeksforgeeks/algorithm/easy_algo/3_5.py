Maximum profit by selling N items at two markets



Given two array **A[]** and **B[]** each of length **N** where **A[i]** and
**B[i]** are the prices of the **i th** item when sold in market **A** and
market **B** respectively. The task is to maximize the profile of selling all
the **N** items but there is a catch if you went to market **B** then you can
not return back. For example, if you sell the first k items in market A then
you have to sell the rest of the items in market B.  
 **Examples:**

> **Input:** A[] = {2, 3, 2}, B[] = {10, 3, 40}  
> **Output:** 53  
> Sell all the items in market B in order to  
> maximize the profit i.e. (10 + 3 + 40) = 53.  
>  **Input:** A[] = {7, 5, 3, 4}, B[] = {2, 3, 1, 3}  
> **Output:** 19

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  * Create a prefix sum array **preA[]** where **preA[i]** will store the profit when the items **A[0…i]** are sold in market **A**.
  * Create a suffix sum array **suffB[]** where **suffB[i]** will store the profit when the items **B[i…n-1]** are sold in market **B**.
  * Now the problem gets reduced to finding an index **i** such that **(preA[i] + suffB[i + 1])** is maximum.

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

// Function to calculate max profit

int maxProfit(int profitA[], int profitB[], int n)

{

 // Prefix sum array for profitA[]

 int preSum[n];

 preSum[0] = profitA[0];

 for (int i = 1; i < n; i++) {

 preSum[i] = preSum[i - 1] + profitA[i];

 }

 // Suffix sum array for profitB[]

 int suffSum[n];

 suffSum[n - 1] = profitB[n - 1];

 for (int i = n - 2; i >= 0; i--) {

 suffSum[i] = suffSum[i + 1] + profitB[i];

 }

 // If all the items are sold in market A

 int res = preSum[n - 1];

 // Find the maximum profit when the first i

 // items are sold in market A and the

 // rest of the items are sold in market

 // B for all possible values of i

 for (int i = 1; i < n - 1; i++) {

 res = max(res, preSum[i] + suffSum[i + 1]);

 }

 // If all the items are sold in market B

 res = max(res, suffSum[0]);

 return res;

}

// Driver code

int main()

{

 int profitA[] = { 2, 3, 2 };

 int profitB[] = { 10, 30, 40 };

 int n = sizeof(profitA) / sizeof(int);

 // Function to calculate max profit

 cout << maxProfit(profitA, profitB, n);

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

 // Function to calculate max profit

 static int maxProfit(int profitA[], int profitB[], int n)

 {

 

 // Prefix sum array for profitA[]

 int preSum[] = new int[n];

 preSum[0] = profitA[0];

 for (int i = 1; i < n; i++)

 {

 preSum[i] = preSum[i - 1] + profitA[i];

 }

 

 // Suffix sum array for profitB[]

 int suffSum[] = new int[n];

 suffSum[n - 1] = profitB[n - 1];

 for (int i = n - 2; i >= 0; i--)

 {

 suffSum[i] = suffSum[i + 1] + profitB[i];

 }

 

 // If all the items are sold in market A

 int res = preSum[n - 1];

 

 // Find the maximum profit when the first i

 // items are sold in market A and the

 // rest of the items are sold in market

 // B for all possible values of i

 for (int i = 1; i < n - 1; i++)

 {

 res = Math.max(res, preSum[i] + suffSum[i + 1]);

 }

 

 // If all the items are sold in market B

 res = Math.max(res, suffSum[0]);

 

 return res;

 }

 

 // Driver code

 public static void main (String[] args)

 {

 int profitA[] = { 2, 3, 2 };

 int profitB[] = { 10, 30, 40 };

 int n = profitA.length;

 

 // Function to calculate max profit

 System.out.println(maxProfit(profitA, profitB, n));

 }

}

// This code is contributed by AnkitRai01  
  
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

# Function to calculate max profit

def maxProfit(profitA, profitB, n) :

 # Prefix sum array for profitA[]

 preSum = [0] * n;

 preSum[0] = profitA[0];

 

 for i in range(1, n) :

 preSum[i] = preSum[i - 1] + profitA[i];

 # Suffix sum array for profitB[]

 suffSum = [0] * n;

 suffSum[n - 1] = profitB[n - 1];

 

 for i in range(n - 2, -1, -1) :

 suffSum[i] = suffSum[i + 1] + profitB[i];

 # If all the items are sold in market A

 res = preSum[n - 1];

 # Find the maximum profit when the first i

 # items are sold in market A and the

 # rest of the items are sold in market

 # B for all possible values of i

 for i in range(1 , n - 1) :

 res = max(res, preSum[i] + suffSum[i + 1]);

 # If all the items are sold in market B

 res = max(res, suffSum[0]);

 return res;

# Driver code

if __name__ == "__main__" :

 profitA = [ 2, 3, 2 ];

 profitB = [ 10, 30, 40 ];

 n = len(profitA);

 # Function to calculate max profit

 print(maxProfit(profitA, profitB, n));

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

 

 // Function to calculate max profit

 static int maxProfit(int []profitA,

 int []profitB, int n)

 {

 

 // Prefix sum array for profitA[]

 int []preSum = new int[n];

 preSum[0] = profitA[0];

 for (int i = 1; i < n; i++)

 {

 preSum[i] = preSum[i - 1] + profitA[i];

 }

 

 // Suffix sum array for profitB[]

 int []suffSum = new int[n];

 suffSum[n - 1] = profitB[n - 1];

 for (int i = n - 2; i >= 0; i--)

 {

 suffSum[i] = suffSum[i + 1] + profitB[i];

 }

 

 // If all the items are sold in market A

 int res = preSum[n - 1];

 

 // Find the maximum profit when the first i

 // items are sold in market A and the

 // rest of the items are sold in market

 // B for all possible values of i

 for (int i = 1; i < n - 1; i++)

 {

 res = Math.Max(res, preSum[i] +

 suffSum[i + 1]);

 }

 

 // If all the items are sold in market B

 res = Math.Max(res, suffSum[0]);

 

 return res;

 }

 

 // Driver code

 public static void Main(String[] args)

 {

 int []profitA = { 2, 3, 2 };

 int []profitB = { 10, 30, 40 };

 int n = profitA.Length;

 

 // Function to calculate max profit

 Console.WriteLine(maxProfit(profitA, profitB, n));

 }

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    80

