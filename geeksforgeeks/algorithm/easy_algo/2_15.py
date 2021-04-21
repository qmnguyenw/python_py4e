Longest common subarray in the given two arrays



Given two arrays **A[] and B[]** of **N and M** integers respectively, the
task is to find the maximum length of equal subarray or the longest common
subarray between the two given array.

 **Examples:**

> **Input:** A[] = {1, 2, 8, 2, 1}, B[] = {8, 2, 1, 4, 7}  
> **Output:** 3  
> **Explanation:**  
> The subarray that is common to both arrays are {8, 2, 1} and the length of
> the subarray is 3.  
>  **Input:** A[] = {1, 2, 3, 2, 1}, B[] = {8, 7, 6, 4, 7}  
> **Output:** 0  
> **Explanation:**  
> There is no such subarrays which are equal in the array A[] and B[].

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The idea is to generate all the subarrays of the two
given array **A[]** and **B[]** and find the longest matching subarray. This
solution is exponential in terms of time complexity.  
 **Time Complexity:** O(2N+M), where N is the length of the array **A[]** and
M is the length of the **array** **B[]**.

 **Efficient Approach:**  
The efficient approach is to use Dynamic Programming(DP). This problem is the
variation of the Longest Common Subsequence(LCS).  
Let the input sequences are **A[0..n-1]** and **B[0..m-1]** of lengths **m &
n** respectively. Following is the recursive implementation of the equal
subarrays:

  

  

  1. Since common subarray of **A[]** and **B[]** must start at some index **i** and **j** such that **A[i]** is equals to **B[j]**. Let **dp[i][j]** be the longest common subarray of **A[i…] and B[j…]**.
  2. Therefore, for any index i and j, if A[i] is equals to B[j], then **dp[i][j] = dp[i+1][j+1] + 1**.
  3. The maximum of all the element in the array **dp[][]** will give the maximum length of equal subarrays.

 **For Example:**  
If the given array **A[]** = {1, 2, 8, 2, 1} and **B[]** = {8, 2, 1, 4, 7}. If
the characters match at index **i** and **j** for the array **A[]** and
**B[]** respectively, then **dp[i][j]** will be updated as **1 +
dp[i+1][j+1]**.  
Below is the updated **dp[][]** table for the given array **A[]** and **B[]**.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200324151540/LCSA.jpg)

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to DP approach

// to above solution

#include <bits/stdc++.h>

using namespace std;

// Function to find the maximum

// length of equal subarray

int FindMaxLength(int A[], int B[], int n, int m)

{

 // Auxillary dp[][] array

 int dp[n + 1][m + 1];

 for (int i = 0; i <= n; i++)

 for (int j = 0; j <= m; j++)

 dp[i][j] = 0;

 // Updating the dp[][] table

 // in Bottom Up approach

 for (int i = n - 1; i >= 0; i--)

 {

 for (int j = m - 1; j >= 0; j--)

 {

 // If A[i] is equal to B[i]

 // then dp[j][i] = dp[j + 1][i + 1] + 1

 if (A[i] == B[j])

 dp[j][i] = dp[j + 1][i + 1] + 1;

 }

 }

 int maxm = 0;

 // Find maximum of all the values

 // in dp[][] array to get the

 // maximum length

 for (int i = 0; i < n; i++)

 {

 for (int j = 0; j < m; j++)

 {

 // Update the length

 maxm = max(maxm, dp[i][j]);

 }

 }

 // Return the maximum length

 return maxm;

}

// Driver Code

int main()

{

 int A[] = { 1, 2, 8, 2, 1 };

 int B[] = { 8, 2, 1, 4, 7 };

 int n = sizeof(A) / sizeof(A[0]);

 int m = sizeof(B) / sizeof(B[0]);

 // Function call to find

 // maximum length of subarray

 cout << (FindMaxLength(A, B, n, m));

}

// This code is contributed by chitranayal  
  
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

// Java program to DP approach

// to above solution

class GFG

{

 // Function to find the maximum

 // length of equal subarray

 static int FindMaxLength(int A[], int B[], int n, int
m)

 {

 // Auxillary dp[][] array

 int[][] dp = new int[n + 1][m + 1];

 for (int i = 0; i <= n; i++)

 for (int j = 0; j <= m; j++)

 dp[i][j] = 0;

 // Updating the dp[][] table

 // in Bottom Up approach

 for (int i = n - 1; i >= 0; i--)

 {

 for (int j = m - 1; j >= 0; j--)

 {

 // If A[i] is equal to B[i]

 // then dp[j][i] = dp[j + 1][i + 1] + 1

 if (A[i] == B[j])

 dp[j][i] = dp[j + 1][i + 1] + 1;

 }

 }

 int maxm = 0;

 // Find maximum of all the values

 // in dp[][] array to get the

 // maximum length

 for (int i = 0; i < n; i++)

 {

 for (int j = 0; j < m; j++)

 {

 // Update the length

 maxm = Math.max(maxm, dp[i][j]);

 }

 }

 // Return the maximum length

 return maxm;

 }

 // Driver Code

 public static void main(String[] args)

 {

 int A[] = { 1, 2, 8, 2, 1 };

 int B[] = { 8, 2, 1, 4, 7 };

 int n = A.length;

 int m = B.length;

 // Function call to find

 // maximum length of subarray

 System.out.print(FindMaxLength(A, B, n, m));

 }

}

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to DP approach

# to above solution

# Function to find the maximum

# length of equal subarray

def FindMaxLength(A, B):

 n = len(A)

 m = len(B)

 # Auxillary dp[][] array

 dp = [[0 for i in range(n + 1)] for i in
range(m + 1)]

 # Updating the dp[][] table

 # in Bottom Up approach

 for i in range(n - 1, -1, -1):

 for j in range(m - 1, -1, -1):

 # If A[i] is equal to B[i]

 # then dp[j][i] = dp[j + 1][i + 1] + 1

 if A[i] == B[j]:

 dp[j][i] = dp[j + 1][i + 1] + 1

 maxm = 0

 # Find maximum of all the values

 # in dp[][] array to get the

 # maximum length

 for i in dp:

 for j in i:

 # Update the length

 maxm = max(maxm, j)

 # Return the maximum length

 return maxm

# Driver Code

if __name__ == '__main__':

 A = [1, 2, 8, 2, 1]

 B = [8, 2, 1, 4, 7]

 # Function call to find

 # maximum length of subarray

 print(FindMaxLength(A, B))  
  
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

// C# program to DP approach

// to above solution

using System;

class GFG

{

 // Function to find the maximum

 // length of equal subarray

 static int FindMaxLength(int[] A, int[] B, int n, int
m)

 {

 // Auxillary [,]dp array

 int[, ] dp = new int[n + 1, m + 1];

 for (int i = 0; i <= n; i++)

 for (int j = 0; j <= m; j++)

 dp[i, j] = 0;

 // Updating the [,]dp table

 // in Bottom Up approach

 for (int i = n - 1; i >= 0; i--)

 {

 for (int j = m - 1; j >= 0; j--)

 {

 // If A[i] is equal to B[i]

 // then dp[j, i] = dp[j + 1, i + 1] + 1

 if (A[i] == B[j])

 dp[j, i] = dp[j + 1, i + 1] + 1;

 }

 }

 int maxm = 0;

 // Find maximum of all the values

 // in [,]dp array to get the

 // maximum length

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < m; j++) {

 // Update the length

 maxm = Math.Max(maxm, dp[i, j]);

 }

 }

 // Return the maximum length

 return maxm;

 }

 // Driver Code

 public static void Main(String[] args)

 {

 int[] A = { 1, 2, 8, 2, 1 };

 int[] B = { 8, 2, 1, 4, 7 };

 int n = A.Length;

 int m = B.Length;

 // Function call to find

 // maximum length of subarray

 Console.Write(FindMaxLength(A, B, n, m));

 }

}

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output**

    
    
    3

 **Time Complexity:** O(N*M), where N is the length of array A[] and M is the
length of array B[].

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

