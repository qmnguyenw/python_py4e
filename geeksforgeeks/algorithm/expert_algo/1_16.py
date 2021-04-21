Number of ways to select equal sized subarrays from two arrays having atleast
K equal pairs of elements



Given two arrays **A[]** and **B[]** , and an integer **K** , the task is to
find the number of ways to select two subarrays of the same size, one from A
and the other one from B such that the subarrays have at least K equal pairs
of elements. (i.e. the number of pairs (A[i], B[j]) in the two selected
subarrays such that A[i] = B[j] >= K).  
 **Examples:**

> **Input:** A[] = {1, 2}, B[] = {1, 2, 3}, K = 1  
> **Output:** 4  
> The ways to select two subarrays are:
>
>   1. [1], [1]
>   2. [2], [2]
>   3. [1, 2], [1, 2]
>   4. [1, 2], [2, 3]
>

>
>  **Input:** A[] = {3, 2, 5, 21, 15, 2, 6}, B[] = {2, 1, 4, 3, 6, 7, 9}, K =
> 2  
> **Output:** 7

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  * Instead of dealing with the two arrays separately, let’s combine them in form of a binary matrix such that: 

    
    
    mat[i][j] = 0, if A[i] != B[j]
              = 1, if A[i] = B[j]
    

  * Now if we consider any submatrix of this matrix, say of size P x Q, it’s basically a combination of a subarray from A of size P and a subarray from B of size Q. Since we only want to check for equal-sized subarrays, we will consider only square submatrices. 
  * Let’s consider a square submatrix with top left corner as (i, j) and bottom right corner as (i + size,, j + size). This is equivalent to considering subarrays A[i: i + size] and B[j: j + size]. It can be observed that if these two subarrays will have x pairs of equal elements then the submatrix will have x 1’s in it. 
  * So traverse over all the elements of the matrix (i, j) and consider them to be the bottom right corner of the square. Now, one way is to traverse all the possible sizes of submatrix and find the sizes which have sum >= k, but this will be less efficient. It can be observed that say if a S x S submatrix with (i, j) as bottom right corner has sum >= k, then all square submatrices with size >= S and (i, j) as bottom right corner will follow the property. 
  * So instead of iterating for all sizes at each (i, j), we will just apply binary search over the size of the square submatrix and find the smallest size S such that it has sum >= K, and then simply add the matrices with greater side lengths.   
This article can be referred to see how submatrix sums are evaluated in
constant time using 2D prefix sums.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to count the

// number of ways to select equal

// sized subarrays such that they

// have atleast K common elements

#include <bits/stdc++.h>

using namespace std;

// 2D prefix sum for submatrix

// sum query for matrix

int prefix_2D[2005][2005];

// Function to find the prefix sum

// of the matrix from i and j

int subMatrixSum(int i, int j, int len)

{

 return prefix_2D[i][j] -

 prefix_2D[i][j - len] -

 prefix_2D[i - len][j] +

 prefix_2D[i - len][j - len];

}

// Function to count the number of ways

// to select equal sized subarrays such

// that they have atleast K common elements

int numberOfWays(int a[], int b[], int n,

 int m, int k)

{

 // Combining the two arrays

 for (int i = 1; i <= n; i++) {

 for (int j = 1; j <= m; j++) {

 if (a[i - 1] == b[j - 1])

 prefix_2D[i][j] = 1;

 else

 prefix_2D[i][j] = 0;

 }

 }

 // Calculating the 2D prefix sum

 for (int i = 1; i <= n; i++) {

 for (int j = 1; j <= m; j++) {

 prefix_2D[i][j] += prefix_2D[i][j - 1];

 }

 }

 for (int i = 1; i <= n; i++) {

 for (int j = 1; j <= m; j++) {

 prefix_2D[i][j] += prefix_2D[i - 1][j];

 }

 }

 int answer = 0;

 // iterating through all

 // the elements of matrix

 // and considering them to

 // be the bottom right

 for (int i = 1; i <= n; i++) {

 for (int j = 1; j <= m; j++) {

 

 // applying binary search

 // over side length

 int low = 1;

 int high = min(i, j);

 while (low < high) {

 int mid = (low + high) >> 1;

 // if sum of this submatrix >=k then

 // new search space will be [low, mid]

 if (subMatrixSum(i, j, mid) >= k) {

 high = mid;

 }

 // else new search space

 // will be [mid+1, high]

 else {

 low = mid + 1;

 }

 }

 // Adding the total submatrices

 if (subMatrixSum(i, j, low) >= k) {

 answer += (min(i, j) - low + 1);

 }

 }

 }

 return answer;

}

// Driver Code

int main()

{

 int N = 2, M = 3;

 int A[N] = { 1, 2 };

 int B[M] = { 1, 2, 3 };

 int K = 1;

 cout << numberOfWays(A, B, N, M, K);

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

// Java implementation to count the

// number of ways to select equal

// sized subarrays such that they

// have atleast K common elements

class GFG{

// 2D prefix sum for submatrix

// sum query for matrix

static int [][]prefix_2D = new int[2005][2005];

// Function to find the prefix sum

// of the matrix from i and j

static int subMatrixSum(int i, int j, int len)

{

 return prefix_2D[i][j] -

 prefix_2D[i][j - len] -

 prefix_2D[i - len][j] +

 prefix_2D[i - len][j - len];

}

// Function to count the number of ways

// to select equal sized subarrays such

// that they have atleast K common elements

static int numberOfWays(int a[], int b[], int n,

 int m, int k)

{

 

 // Combining the two arrays

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= m; j++)

 {

 if (a[i - 1] == b[j - 1])

 prefix_2D[i][j] = 1;

 else

 prefix_2D[i][j] = 0;

 }

 }

 // Calculating the 2D prefix sum

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= m; j++)

 {

 prefix_2D[i][j] += prefix_2D[i][j - 1];

 }

 }

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= m; j++)

 {

 prefix_2D[i][j] += prefix_2D[i - 1][j];

 }

 }

 int answer = 0;

 // Iterating through all

 // the elements of matrix

 // and considering them to

 // be the bottom right

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= m; j++)

 {

 

 // Applying binary search

 // over side length

 int low = 1;

 int high = Math.min(i, j);

 

 while (low < high)

 {

 int mid = (low + high) >> 1;

 

 // If sum of this submatrix >=k then

 // new search space will be [low, mid]

 if (subMatrixSum(i, j, mid) >= k)

 {

 high = mid;

 }

 

 // Else new search space

 // will be [mid+1, high]

 else

 {

 low = mid + 1;

 }

 }

 

 // Adding the total submatrices

 if (subMatrixSum(i, j, low) >= k)

 {

 answer += (Math.min(i, j) - low + 1);

 }

 }

 }

 return answer;

}

// Driver Code

public static void main(String[] args)

{

 int N = 2, M = 3;

 int A[] = { 1, 2 };

 int B[] = { 1, 2, 3 };

 int K = 1;

 System.out.print(numberOfWays(A, B, N, M, K));

}

}

// This code is contributed by Princi Singh  
  
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

# Python3 implementation to count the

# number of ways to select equal

# sized subarrays such that they

# have atleast K common element

# 2D prefix sum for submatrix

# sum query for matrix

prefix_2D = [[0 for x in range (2005)]

 for y in range (2005)]

# Function to find the prefix sum

# of the matrix from i and j

def subMatrixSum(i, j, length):

 return (prefix_2D[i][j] -

 prefix_2D[i][j - length] -

 prefix_2D[i - length][j] +

 prefix_2D[i - length][j - length])

# Function to count the number of ways

# to select equal sized subarrays such

# that they have atleast K common elements

def numberOfWays(a, b, n, m, k):

 # Combining the two arrays

 for i in range (1, n + 1):

 for j in range (1, m + 1):

 if (a[i - 1] == b[j - 1]):

 prefix_2D[i][j] = 1

 else:

 prefix_2D[i][j] = 0

 

 # Calculating the 2D prefix sum

 for i in range (1, n + 1):

 for j in range (1, m + 1):

 prefix_2D[i][j] += prefix_2D[i][j - 1]

 

 for i in range (1, n + 1):

 for j in range (1, m + 1):

 prefix_2D[i][j] += prefix_2D[i - 1][j]

 answer = 0

 # iterating through all

 # the elements of matrix

 # and considering them to

 # be the bottom right

 for i in range (1, n +1):

 for j in range (1, m + 1):

 

 # applying binary search

 # over side length

 low = 1

 high = min(i, j)

 while (low < high):

 mid = (low + high) >> 1

 # if sum of this submatrix >=k then

 # new search space will be [low, mid]

 if (subMatrixSum(i, j, mid) >= k):

 high = mid

 

 # else new search space

 # will be [mid+1, high]

 else:

 low = mid + 1

 # Adding the total submatrices

 if (subMatrixSum(i, j, low) >= k):

 answer += (min(i, j) - low + 1)

 

 return answer

# Driver Code

if __name__ == "__main__":

 

 N = 2

 M = 3

 A = [1, 2]

 B = [1, 2, 3]

 K = 1

 print (numberOfWays(A, B, N, M, K))

# This code is contributed by Chitranayal  
  
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

// C# implementation to count the

// number of ways to select equal

// sized subarrays such that they

// have atleast K common elements

using System;

class GFG{

// 2D prefix sum for submatrix

// sum query for matrix

static int [,]prefix_2D = new int[2005, 2005];

// Function to find the prefix sum

// of the matrix from i and j

static int subMatrixSum(int i, int j, int len)

{

 return prefix_2D[i, j] -

 prefix_2D[i, j - len] -

 prefix_2D[i - len, j] +

 prefix_2D[i - len, j - len];

}

// Function to count the number of ways

// to select equal sized subarrays such

// that they have atleast K common elements

static int numberOfWays(int []a, int []b, int n,

 int m, int k)

{

 

 // Combining the two arrays

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= m; j++)

 {

 if (a[i - 1] == b[j - 1])

 prefix_2D[i, j] = 1;

 else

 prefix_2D[i, j] = 0;

 }

 }

 // Calculating the 2D prefix sum

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= m; j++)

 {

 prefix_2D[i, j] += prefix_2D[i, j - 1];

 

 }

 }

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= m; j++)

 {

 prefix_2D[i, j] += prefix_2D[i - 1, j];

 }

 }

 int answer = 0;

 // Iterating through all

 // the elements of matrix

 // and considering them to

 // be the bottom right

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= m; j++)

 {

 

 // Applying binary search

 // over side length

 int low = 1;

 int high = Math.Min(i, j);

 while (low < high)

 {

 int mid = (low + high) >> 1;

 

 // If sum of this submatrix >=k then

 // new search space will be [low, mid]

 if (subMatrixSum(i, j, mid) >= k)

 {

 high = mid;

 }

 

 // Else new search space

 // will be [mid+1, high]

 else

 {

 low = mid + 1;

 }

 }

 

 // Adding the total submatrices

 if (subMatrixSum(i, j, low) >= k)

 {

 answer += (Math.Min(i, j) - low + 1);

 }

 }

 }

 return answer;

}

// Driver Code

public static void Main(String[] args)

{

 int N = 2, M = 3;

 int []A = { 1, 2 };

 int []B = { 1, 2, 3 };

 int K = 1;

 Console.Write(numberOfWays(A, B, N, M, K));

}

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    
    
    

**Time Complexity:** _O(N * M * log(max(N, M)))_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

