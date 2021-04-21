Path with maximum product in 2-d array



Given a 2D matrix of size **N*M**. The task is to find the maximum product
path from **(0, 0)** to **(N-1, M-1)**. You can only move to right from **(i,
j)** to **(i, j+1)** and down from **(i, j)** to **(i+1, j)**.

 **Examples**

>  **Input:** arr[][] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} }  
>  **Output:** 2016  
> The path with maximum product is : 1->4->7->8->9 = 2016

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
To choose which direction to go from the current position we have to check the
direction that gives the maximum product. We will maintain two 2D arrays:

  1.  **maxPath[i][j]:** It will store the maximum product till **(i, j)**
  2.  **minPath[i][j]:** It will store the minimum product till **(i, j)**

 **Steps:**

  

  

  * Initialise the maxPath[0][0] & minPath[0][0] to arr[0][0].
  * For all the remaining cells in maxPath[i][j] check whether the product of current cell(i, j) and previous cell (i-1, j) is maximum or not by:  

> considering rows:  
>  **maxValue1 = max(arr[i][j]*maxPath[i-1][j], arr[i][j]*minPath[i-1][j])**  
>  considering columns:  
>  **maxValue2 = max(maxPath[i][j – 1] * arr[i][j], minPath[i][j – 1] *
> arr[i][j])**  
>  as arr[i][j] can be negative and if minPath[i][j] is negative. Then,  
> arr[i][j]*minPath[i][j] is positive, which can be maximum product.

  * For all the remaining cells in minPath[i][j] check whether the product of current cell(i, j) and previous cell (i-1, j) is minimum or not by:  

> considering rows:  
>  **minValue1 = min(maxPath[i – 1][j] * arr[i][j], minPath[i – 1][j] *
> arr[i][j])**  
>  considering columns:  
>  **minValue2 = min(maxPath[i][j – 1] * arr[i][j], minPath[i][j – 1] *
> arr[i][j])**

  * Update **minPath[i][j] = min(minValue1, minValue2)** & **maxPath[i][j] = max(maxValue1, maxValue2)**
  * Return **maxPath[n-1][m-1]** for maximum product.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to find maximum

// product path from (0, 0) to

// (N-1, M-1)

#include <bits/stdc++.h>

using namespace std;

#define N 3

#define M 3

 

// Function to find maximum product

int maxProductPath(int arr[N][M])

{

 

 // It will store the maximum

 // product till a given cell.

 vector<vector<int> > maxPath(N, vector<int>(M, INT_MIN));

 

 // It will store the minimum

 // product till a given cell

 // (for -ve elements)

 vector<vector<int> > minPath(N, vector<int>(M, INT_MAX));

 

 for (int i = 0; i < N; i++) {

 for (int j = 0; j < M; j++) {

 

 int minVal = INT_MAX;

 int maxVal = INT_MIN;

 

 // If we are at topmost

 // or leftmost, just

 // copy the elements.

 if (i == 0 && j == 0) {

 maxVal = arr[i][j];

 minVal = arr[i][j];

 }

 

 // If we're not at the

 // above, we can consider

 // the above value.

 if (i > 0) {

 int tempMax = max(maxPath[i - 1][j] * arr[i][j],

 minPath[i - 1][j] * arr[i][j]);

 maxVal = max(maxVal, tempMax);

 

 int tempMin = min(maxPath[i - 1][j] * arr[i][j],

 minPath[i - 1][j] * arr[i][j]);

 minVal = min(minVal, tempMin);

 }

 

 // If we're not on the

 // leftmost, we can consider

 // the left value.

 if (j > 0) {

 int tempMax = max(maxPath[i][j - 1] * arr[i][j],

 minPath[i][j - 1] * arr[i][j]);

 maxVal = max(maxVal, tempMax);

 

 int tempMin = min(maxPath[i][j - 1] * arr[i][j],

 minPath[i][j - 1] * arr[i][j]);

 minVal = min(minVal, tempMin);

 }

 

 // Store max & min product

 // till i, j.

 maxPath[i][j] = maxVal;

 minPath[i][j] = minVal;

 }

 }

 

 // Return the max product path

 // from 0, 0 -> N-1, M-1.

 return maxPath[N - 1][M - 1];

}

 

// Driver Code

int main()

{

 int arr[N][M] = { { 1, -2, 3 },

 { 4, -5, 6 },

 { -7, -8, 9 } };

 

 // Print maximum product from

 // (0, 0) to (N-1, M-1)

 cout << maxProductPath(arr) << endl;

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

// Java Program to find maximum

// product path from (0, 0) to

// (N-1, M-1)

class GFG

{

 

static final int N = 3;

static final int M = 3;

 

// Function to find maximum product

static int maxProductPath(int arr[][])

{

 

 // It will store the maximum

 // product till a given cell.

 int [][]maxPath = new int[N][M];

 

 // It will store the minimum

 // product till a given cell

 // (for -ve elements)

 int [][]minPath = new int[N][M];

 

 for (int i = 0; i < N; i++) 

 {

 for (int j = 0; j < M; j++) 

 {

 

 int minVal = Integer.MAX_VALUE;

 int maxVal = Integer.MIN_VALUE;

 

 // If we are at topmost

 // or leftmost, just

 // copy the elements.

 if (i == 0 && j == 0)

 {

 maxVal = arr[i][j];

 minVal = arr[i][j];

 }

 

 // If we're not at the

 // above, we can consider

 // the above value.

 if (i > 0) 

 {

 int tempMax = Math.max(maxPath[i - 1][j] * arr[i][j],

 minPath[i - 1][j] * arr[i][j]);

 maxVal = Math.max(maxVal, tempMax);

 

 int tempMin = Math.min(maxPath[i - 1][j] * arr[i][j],

 minPath[i - 1][j] * arr[i][j]);

 minVal = Math.min(minVal, tempMin);

 }

 

 // If we're not on the

 // leftmost, we can consider

 // the left value.

 if (j > 0) {

 int tempMax = Math.max(maxPath[i][j - 1] * arr[i][j],

 minPath[i][j - 1] * arr[i][j]);

 maxVal = Math.max(maxVal, tempMax);

 

 int tempMin = Math.min(maxPath[i][j - 1] * arr[i][j],

 minPath[i][j - 1] * arr[i][j]);

 minVal = Math.min(minVal, tempMin);

 }

 

 // Store max & min product

 // till i, j.

 maxPath[i][j] = maxVal;

 minPath[i][j] = minVal;

 }

 }

 

 // Return the max product path

 // from 0, 0.N-1, M-1.

 return maxPath[N - 1][M - 1];

}

 

// Driver Code

public static void main(String[] args)

{

 int arr[][] = { { 1, -2, 3 },

 { 4, -5, 6 },

 { -7, -8, 9 } };

 

 // Print maximum product from

 // (0, 0) to (N-1, M-1)

 System.out.print(maxProductPath(arr) +"\n");

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

# Python Program to find maximum

# product path from (0, 0) to

# (N-1, M-1)

import sys

N = 3;

M = 3;

 

# Function to find maximum product

def maxProductPath(arr):

 

 # It will store the maximum

 # product till a given cell.

 maxPath = [[0 for i in range(M)] for j in
range(N)];

 

 # It will store the minimum

 # product till a given cell

 # (for -ve elements)

 minPath = [[0 for i in range(M)] for j in
range(N)];

 

 for i in range(N):

 for j in range(M):

 

 minVal = sys.maxsize;

 maxVal = -sys.maxsize;

 

 # If we are at topmost

 # or leftmost, just

 # copy the elements.

 if (i == 0 and j == 0):

 maxVal = arr[i][j];

 minVal = arr[i][j];

 

 # If we're not at the

 # above, we can consider

 # the above value.

 if (i > 0):

 tempMax = max(maxPath[i - 1][j] * arr[i][j],\

 minPath[i - 1][j] * arr[i][j]);

 maxVal = max(maxVal, tempMax);

 

 tempMin = min(maxPath[i - 1][j] * arr[i][j],\

 minPath[i - 1][j] * arr[i][j]);

 minVal = min(minVal, tempMin);

 

 # If we're not on the

 # leftmost, we can consider

 # the left value.

 if (j > 0):

 tempMax = max(maxPath[i][j - 1] * arr[i][j],\

 minPath[i][j - 1] * arr[i][j]);

 maxVal = max(maxVal, tempMax);

 

 tempMin = min(maxPath[i][j - 1] * arr[i][j],\

 minPath[i][j - 1] * arr[i][j]);

 minVal = min(minVal, tempMin);

 

 # Store max & min product

 # till i, j.

 maxPath[i][j] = maxVal;

 minPath[i][j] = minVal;

 

 # Return the max product path

 # from 0, 0.N-1, M-1.

 return maxPath[N - 1][M - 1];

 

# Driver Code

if __name__ == '__main__':

 arr = [[ 1, -2, 3 ],[ 4, -5, 6 ],[
-7, -8, 9]];

 

 # Prmaximum product from

 # (0, 0) to (N-1, M-1)

 print(maxProductPath(arr));

 

# This code is contributed by 29AjayKumar  
  
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

// C# Program to find maximum

// product path from (0, 0) to

// (N-1, M-1)

using System;

 

class GFG

{

 

static readonly int N = 3;

static readonly int M = 3;

 

// Function to find maximum product

static int maxProductPath(int [,]arr)

{

 

 // It will store the maximum

 // product till a given cell.

 int [,]maxPath = new int[N, M];

 

 // It will store the minimum

 // product till a given cell

 // (for -ve elements)

 int [,]minPath = new int[N, M];

 

 for (int i = 0; i < N; i++) 

 {

 for (int j = 0; j < M; j++) 

 {

 

 int minVal = int.MaxValue;

 int maxVal = int.MinValue;

 

 // If we are at topmost

 // or leftmost, just

 // copy the elements.

 if (i == 0 && j == 0)

 {

 maxVal = arr[i, j];

 minVal = arr[i, j];

 }

 

 // If we're not at the

 // above, we can consider

 // the above value.

 if (i > 0) 

 {

 int tempMax = Math.Max(maxPath[i - 1,j] * arr[i,j],

 minPath[i - 1,j] * arr[i,j]);

 maxVal = Math.Max(maxVal, tempMax);

 

 int tempMin = Math.Min(maxPath[i - 1,j] * arr[i,j],

 minPath[i - 1,j] * arr[i,j]);

 minVal = Math.Min(minVal, tempMin);

 }

 

 // If we're not on the

 // leftmost, we can consider

 // the left value.

 if (j > 0) {

 int tempMax = Math.Max(maxPath[i,j - 1] * arr[i,j],

 minPath[i,j - 1] * arr[i,j]);

 maxVal = Math.Max(maxVal, tempMax);

 

 int tempMin = Math.Min(maxPath[i,j - 1] * arr[i,j],

 minPath[i,j - 1] * arr[i,j]);

 minVal = Math.Min(minVal, tempMin);

 }

 

 // Store max & min product

 // till i, j.

 maxPath[i, j] = maxVal;

 minPath[i, j] = minVal;

 }

 }

 

 // Return the max product path

 // from 0, 0.N - 1, M - 1.

 return maxPath[N - 1, M - 1];

}

 

// Driver Code

public static void Main(String[] args)

{

 int [,]arr = { { 1, -2, 3 },

 { 4, -5, 6 },

 { -7, -8, 9 } };

 

 // Print maximum product from

 // (0, 0) to (N - 1, M - 1)

 Console.Write(maxProductPath(arr) +"\n");

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    2016
    

**Time Complexity:** O(N*M)  
 **Auxillary Space:** O(N*M)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

