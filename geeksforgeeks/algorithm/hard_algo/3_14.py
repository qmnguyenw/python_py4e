Maximum size square Sub-Matrix with sum less than or equals to K



Given a Matrix **arr[][]** of size **M x N** having positive integers and a
number **K** , the task is to find the size of the largest square sub-matrix
whose sum of elements is less than or equals to **K**.

**Example:**

    
    
    **Input:** 
    arr[][] = { { 1, 1, 3, 2, 4, 3, 2 },
                { 1, 1, 3, 2, 4, 3, 2 },
                { 1, 1, 3, 2, 4, 3, 2 } },
    K = 4
    **Output:** 
    2
    **Explanation:**
    Maximum size square Sub-Matrix 
    with sum less than or equals to 4
          1 1
          1 1
    Size is 2.
    
    **Input:** 
    arr[][] = { { 1, 1, 3, 2, 4, 3, 2 },
                { 1, 1, 3, 2, 4, 3, 2 },
                { 1, 1, 3, 2, 4, 3, 2 } }, 
    K = 22
    **Output:** 
    3
    **Explanation:**
    Maximum size square Sub-Matrix 
    with sum less than or equals to 22
          1 1 3
          1 1 3
          1 1 3
    Size is 3. 

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  1. For the given matrix **arr[][]** create a prefix sum matrix(say **sum[][]** ) such that **sum[i][j]** stores the sum of all the elements of the matrix of size **i x j**.
  2. For each row in prefix sum matrix **sum[][]** using Binary Search do the following: 
    * Perform Binary search with the lower limit as **0** end the upper limit as to **maximum size of square matrix**.
    * Find the middle index (say **mid** ).
    * If the sum of elements of all possible square matrix of size **mid** is less than or equals to **K** , then update the lower limit as **mid + 1** to find the maximum sum with size greater than mid.
    * Else Update the upper limit as **mid – 1** to find the maximum sum with size less than mid.
  3. Keep updating the maximum size of square matrix in each iteration for the given valid condition above.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h>

using namespace std;

// Function to find the maximum size

// of matrix with sum <= K

void findMaxMatrixSize(vector<vector<int> > arr, int K)

{

 int i, j;

 // N size of rows and M size of cols

 int n = arr.size();

 int m = arr[0].size();

 // To store the prefix sum of matrix

 int sum[n + 1][m + 1];

 // Create Prefix Sum

 for (int i = 0; i <= n; i++) {

 // Traverse each rows

 for (int j = 0; j <= m; j++) {

 if (i == 0 || j == 0) {

 sum[i][j] = 0;

 continue;

 }

 // Update the prefix sum

 // till index i x j

 sum[i][j] = arr[i - 1][j - 1] + sum[i - 1][j]

 + sum[i][j - 1] - sum[i - 1][j - 1];

 }

 }

 // To store the maximum size of

 // matrix with sum <= K

 int ans = 0;

 // Traverse the sum matrix

 for (i = 1; i <= n; i++) {

 for (j = 1; j <= m; j++) {

 // Index out of bound

 if (i + ans - 1 > n || j + ans - 1 > m)

 break;

 int mid, lo = ans;

 // Maximum possible size

 // of matrix

 int hi = min(n - i + 1, m - j + 1);

 // Binary Search

 while (lo < hi) {

 // Find middle index

 mid = (hi + lo + 1) / 2;

 // Check whether sum <= K

 // or not

 // If Yes check for other

 // half of the search

 if (sum[i + mid - 1][j + mid - 1]

 + sum[i - 1][j - 1]

 - sum[i + mid - 1][j - 1]

 - sum[i - 1][j + mid - 1]

 <= K) {

 lo = mid;

 }

 // Else check it in first

 // half

 else {

 hi = mid - 1;

 }

 }

 // Update the maximum size matrix

 ans = max(ans, lo);

 }

 }

 // Print the final answer

 cout << ans << endl;

}

// Driver Code

int main()

{

 vector<vector<int> > arr;

 arr = { { 1, 1, 3, 2, 4, 3, 2 },

 { 1, 1, 3, 2, 4, 3, 2 },

 { 1, 1, 3, 2, 4, 3, 2 } };

 // Given target sum

 int K = 4;

 // Function Call

 findMaxMatrixSize(arr, K);

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

// Java program for the above approach

import java.util.*;

class GFG {

 // Function to find the maximum size

 // of matrix with sum <= K

 static void findMaxMatrixSize(int[][] arr, int K)

 {

 int i, j;

 // N size of rows and M size of cols

 int n = arr.length;

 int m = arr[0].length;

 // To store the prefix sum of matrix

 int[][] sum = new int[n + 1][m + 1];

 // Create prefix sum

 for (i = 0; i <= n; i++) {

 // Traverse each rows

 for (j = 0; j <= m; j++) {

 if (i == 0 || j == 0) {

 sum[i][j] = 0;

 continue;

 }

 // Update the prefix sum

 // till index i x j

 sum[i][j] = arr[i - 1][j - 1]

 + sum[i - 1][j] + sum[i][j - 1]

 - sum[i - 1][j - 1];

 }

 }

 // To store the maximum size of

 // matrix with sum <= K

 int ans = 0;

 // Traverse the sum matrix

 for (i = 1; i <= n; i++) {

 for (j = 1; j <= m; j++) {

 // Index out of bound

 if (i + ans - 1 > n || j + ans - 1 > m)

 break;

 int mid, lo = ans;

 // Maximum possible size

 // of matrix

 int hi = Math.min(n - i + 1, m - j + 1);

 // Binary Search

 while (lo < hi) {

 // Find middle index

 mid = (hi + lo + 1) / 2;

 // Check whether sum <= K

 // or not

 // If Yes check for other

 // half of the search

 if (sum[i + mid - 1][j + mid - 1]

 + sum[i - 1][j - 1]

 - sum[i + mid - 1][j - 1]

 - sum[i - 1][j + mid - 1]

 <= K) {

 lo = mid;

 }

 // Else check it in first

 // half

 else {

 hi = mid - 1;

 }

 }

 // Update the maximum size matrix

 ans = Math.max(ans, lo);

 }

 }

 // Print the final answer

 System.out.print(ans + "\n");

 }

 // Driver Code

 public static void main(String[] args)

 {

 int[][] arr = { { 1, 1, 3, 2, 4, 3, 2 },

 { 1, 1, 3, 2, 4, 3, 2 },

 { 1, 1, 3, 2, 4, 3, 2 } };

 // Given target sum

 int K = 4;

 // Function Call

 findMaxMatrixSize(arr, K);

 }

}

// This code is contributed by 29AjayKumar  
  
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

# Python3 program for the above approach

# Function to find the maximum size

# of matrix with sum <= K

def findMaxMatrixSize(arr, K):

 # N size of rows and M size of cols

 n = len(arr)

 m = len(arr[0])

 # To store the prefix sum of matrix

 sum = [[0 for i in range(m + 1)] for j in
range(n + 1)]

 # Create Prefix Sum

 for i in range(n + 1):

 # Traverse each rows

 for j in range(m+1):

 if (i == 0 or j == 0):

 sum[i][j] = 0

 continue

 # Update the prefix sum

 # till index i x j

 sum[i][j] = arr[i - 1][j - 1] + sum[i -
1][j] + \

 sum[i][j - 1]-sum[i - 1][j - 1]

 # To store the maximum size of

 # matrix with sum <= K

 ans = 0

 # Traverse the sum matrix

 for i in range(1, n + 1):

 for j in range(1, m + 1):

 # Index out of bound

 if (i + ans - 1 > n or j + ans - 1 > m):

 break

 mid = ans

 lo = ans

 # Maximum possible size

 # of matrix

 hi = min(n - i + 1, m - j + 1)

 # Binary Search

 while (lo < hi):

 # Find middle index

 mid = (hi + lo + 1) // 2

 # Check whether sum <= K

 # or not

 # If Yes check for other

 # half of the search

 if (sum[i + mid - 1][j + mid - 1] +

 sum[i - 1][j - 1] -

 sum[i + mid - 1][j - 1] -

 sum[i - 1][j + mid - 1] <= K):

 lo = mid

 # Else check it in first

 # half

 else:

 hi = mid - 1

 # Update the maximum size matrix

 ans = max(ans, lo)

 # Print the final answer

 print(ans - 1)

# Driver Code

if __name__ == '__main__':

 arr = [[1, 1, 3, 2, 4, 3, 2],

 [1, 1, 3, 2, 4, 3, 2],

 [1, 1, 3, 2, 4, 3, 2]]

 # Given target sum

 K = 4

 # Function Call

 findMaxMatrixSize(arr, K)

# This code is contributed by Surendra_Gangwar  
  
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

// C# program for the above approach

using System;

class GFG {

 // Function to find the maximum size

 // of matrix with sum <= K

 static void findMaxMatrixSize(int[, ] arr, int K)

 {

 int i, j;

 // N size of rows and M size of cols

 int n = arr.GetLength(0);

 int m = arr.GetLength(1);

 // To store the prefix sum of matrix

 int[, ] sum = new int[n + 1, m + 1];

 // Create prefix sum

 for (i = 0; i <= n; i++) {

 // Traverse each rows

 for (j = 0; j <= m; j++) {

 if (i == 0 || j == 0) {

 sum[i, j] = 0;

 continue;

 }

 // Update the prefix sum

 // till index i x j

 sum[i, j] = arr[i - 1, j - 1]

 + sum[i - 1, j] + sum[i, j - 1]

 - sum[i - 1, j - 1];

 }

 }

 // To store the maximum size

 // of matrix with sum <= K

 int ans = 0;

 // Traverse the sum matrix

 for (i = 1; i <= n; i++) {

 for (j = 1; j <= m; j++) {

 // Index out of bound

 if (i + ans - 1 > n || j + ans - 1 > m)

 break;

 int mid, lo = ans;

 // Maximum possible size

 // of matrix

 int hi = Math.Min(n - i + 1, m - j + 1);

 // Binary Search

 while (lo < hi) {

 // Find middle index

 mid = (hi + lo + 1) / 2;

 // Check whether sum <= K

 // or not

 // If Yes check for other

 // half of the search

 if (sum[i + mid - 1, j + mid - 1]

 + sum[i - 1, j - 1]

 - sum[i + mid - 1, j - 1]

 - sum[i - 1, j + mid - 1]

 <= K) {

 lo = mid;

 }

 // Else check it in first

 // half

 else {

 hi = mid - 1;

 }

 }

 // Update the maximum size matrix

 ans = Math.Max(ans, lo);

 }

 }

 // Print the readonly answer

 Console.Write(ans + "\n");

 }

 // Driver Code

 public static void Main(String[] args)

 {

 int[, ] arr = { { 1, 1, 3, 2, 4, 3, 2 },

 { 1, 1, 3, 2, 4, 3, 2 },

 { 1, 1, 3, 2, 4, 3, 2 } };

 // Given target sum

 int K = 4;

 // Function Call

 findMaxMatrixSize(arr, K);

 }

}

// This code is contributed by Amit Katiyar  
  
---  
  
 __

 __

 **Output**

    
    
    2

 **Time Complexity:** O(N*N*log(N))  
**Auxiliary Space:** O(M*N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

