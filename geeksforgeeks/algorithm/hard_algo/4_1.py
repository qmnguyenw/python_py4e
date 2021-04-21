Maximum size of square such that all submatrices of that size have sum less
than K



Given an **N x M** matrix of integers and an integer **K** , the task is to
find the size of the maximum square sub-matrix **(S x S)** , such that **all
square sub-matrices** of the given matrix of that size have a sum less than
**K**.

 **Examples:**

    
    
    **Input:** K = 30 
    mat[N][M] = {{1, 2, 3, 4, 6}, 
                 {5, 3, 8, 1, 2}, 
                 {4, 6, 7, 5, 5}, 
                 {2, 4, 8, 9, 4} }; 
    **Output:** 2
    **Explanation:**
    All Sub-matrices of size **2 x 2** 
    have sum less than 30
    
    **Input :** K = 100 
    mat[N][M] = { { 1, 2, 3, 4 },
                  { 5, 6, 7, 8 }, 
                  { 9, 10, 11, 12 }, 
                  { 13, 14, 15, 16 } };
    **Output:** 3
    **Explanation:**
    All Sub-matrices of size **3 x 3** 
    have sum less than 100

 **Naive Approach** The basic solution is to choose the size **S** of the
submatrix and find all the submatrices of that size and check that the sum of
all sub-matrices is less than the given sum whereas, this can be improved by
computing the sum of the matrix using this approach. Therefore, the task will
be to choose the maximum size possible and the starting and ending position of
the every possible sub-matrices. Due to which the overall time complexity will
be O(N3).

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// maximum size square submatrix

// such that their sum is less than K

#include <bits/stdc++.h>

using namespace std;

// Size of matrix

#define N 4

#define M 5

// Function to preprocess the matrix

// for computing the sum of every

// possible matrix of the given size

void preProcess(int mat[N][M],

 int aux[N][M])

{

 // Loop to copy the first row

 // of the matrix into the aux matrix

 for (int i = 0; i < M; i++)

 aux[0][i] = mat[0][i];

 

 // Computing the sum column-wise

 for (int i = 1; i < N; i++)

 for (int j = 0; j < M; j++)

 aux[i][j] = mat[i][j] +

 aux[i - 1][j];

 // Computing row wise sum

 for (int i = 0; i < N; i++)

 for (int j = 1; j < M; j++)

 aux[i][j] += aux[i][j - 1];

}

// Function to find the sum of a

// submatrix with the given indices

int sumQuery(int aux[N][M], int tli,

 int tlj, int rbi, int rbj)

{

 // Overall sum from the top to

 // right corner of matrix

 int res = aux[rbi][rbj];

 

 // Removing the sum from the top

 // corer of the matrix

 if (tli > 0)

 res = res - aux[tli - 1][rbj];

 

 // Remove the overlapping sum

 if (tlj > 0)

 res = res - aux[rbi][tlj - 1];

 

 // Add the sum of top corner

 // which is substracted twice

 if (tli > 0 && tlj > 0)

 res = res +

 aux[tli - 1][tlj - 1];

 return res;

}

// Function to find the maximum

// square size possible with the

// such that every submatrix have

// sum less than the given sum

int maximumSquareSize(int mat[N][M], int K)

{

 int aux[N][M];

 preProcess(mat, aux);

 

 // Loop to choose the size of matrix

 for (int i = min(N, M); i >= 1; i--) {

 bool satisfies = true;

 

 // Loop to find the sum of the

 // matrix of every possible submatrix

 for (int x = 0; x < N; x++) {

 for (int y = 0; y < M; y++) {

 if (x + i - 1 <= N - 1 &&

 y + i - 1 <= M - 1) {

 if (sumQuery(aux, x, y,

 x + i - 1, y + i - 1) > K)

 satisfies = false;

 }

 }

 }

 if (satisfies == true)

 return (i);

 }

 return 0;

}

// Driver Code

int main()

{

 int K = 30;

 int mat[N][M] = { { 1, 2, 3, 4, 6 },

 { 5, 3, 8, 1, 2 },

 { 4, 6, 7, 5, 5 },

 { 2, 4, 8, 9, 4 } };

 cout << maximumSquareSize(mat, K);

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

// Java implementation to find the

// maximum size square submatrix

// such that their sum is less than K

class GFG{

 

// Size of matrix

static final int N = 4;

static final int M = 5;

 

// Function to preprocess the matrix

// for computing the sum of every

// possible matrix of the given size

static void preProcess(int [][]mat,

 int [][]aux)

{

 // Loop to copy the first row

 // of the matrix into the aux matrix

 for (int i = 0; i < M; i++)

 aux[0][i] = mat[0][i];

 

 // Computing the sum column-wise

 for (int i = 1; i < N; i++)

 for (int j = 0; j < M; j++)

 aux[i][j] = mat[i][j] +

 aux[i - 1][j];

 

 // Computing row wise sum

 for (int i = 0; i < N; i++)

 for (int j = 1; j < M; j++)

 aux[i][j] += aux[i][j - 1];

}

 

// Function to find the sum of a

// submatrix with the given indices

static int sumQuery(int [][]aux, int tli,

 int tlj, int rbi, int rbj)

{

 // Overall sum from the top to

 // right corner of matrix

 int res = aux[rbi][rbj];

 

 // Removing the sum from the top

 // corer of the matrix

 if (tli > 0)

 res = res - aux[tli - 1][rbj];

 

 // Remove the overlapping sum

 if (tlj > 0)

 res = res - aux[rbi][tlj - 1];

 

 // Add the sum of top corner

 // which is substracted twice

 if (tli > 0 && tlj > 0)

 res = res +

 aux[tli - 1][tlj - 1];

 

 return res;

}

 

// Function to find the maximum

// square size possible with the

// such that every submatrix have

// sum less than the given sum

static int maximumSquareSize(int [][]mat, int K)

{

 int [][]aux = new int[N][M];

 preProcess(mat, aux);

 

 // Loop to choose the size of matrix

 for (int i = Math.min(N, M); i >= 1; i--) {

 

 boolean satisfies = true;

 

 // Loop to find the sum of the

 // matrix of every possible submatrix

 for (int x = 0; x < N; x++) {

 for (int y = 0; y < M; y++) {

 if (x + i - 1 <= N - 1 &&

 y + i - 1 <= M - 1) {

 if (sumQuery(aux, x, y,

 x + i - 1, y + i - 1) > K)

 satisfies = false;

 }

 }

 }

 if (satisfies == true)

 return (i);

 }

 return 0;

}

 

// Driver Code

public static void main(String[] args)

{

 int K = 30;

 int mat[][] = { { 1, 2, 3, 4, 6 },

 { 5, 3, 8, 1, 2 },

 { 4, 6, 7, 5, 5 },

 { 2, 4, 8, 9, 4 } };

 

 System.out.print(maximumSquareSize(mat, K));

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

# Python3 implementation to find the

# maximum size square submatrix

# such that their sum is less than K

# Size of matrix

N = 4

M = 5

# Function to preprocess the matrix

# for computing the sum of every

# possible matrix of the given size

def preProcess(mat, aux):

 # Loop to copy the first row

 # of the matrix into the aux matrix

 for i in range (M):

 aux[0][i] = mat[0][i]

 

 # Computing the sum column-wise

 for i in range (1, N):

 for j in range (M):

 aux[i][j] = (mat[i][j] +

 aux[i - 1][j])

 # Computing row wise sum

 for i in range (N):

 for j in range (1, M):

 aux[i][j] += aux[i][j - 1]

# Function to find the sum of a

# submatrix with the given indices

def sumQuery(aux, tli, tlj, rbi, rbj):

 # Overall sum from the top to

 # right corner of matrix

 res = aux[rbi][rbj]

 

 # Removing the sum from the top

 # corer of the matrix

 if (tli > 0):

 res = res - aux[tli - 1][rbj]

 

 # Remove the overlapping sum

 if (tlj > 0):

 res = res - aux[rbi][tlj - 1]

 

 # Add the sum of top corner

 # which is substracted twice

 if (tli > 0 and tlj > 0):

 res = (res +

 aux[tli - 1][tlj - 1])

 return res

# Function to find the maximum

# square size possible with the

# such that every submatrix have

# sum less than the given sum

def maximumSquareSize(mat, K):

 aux = [[0 for x in range (M)]

 for y in range (N)]

 preProcess(mat, aux)

 

 # Loop to choose the size of matrix

 for i in range (min(N, M), 0, -1):

 satisfies = True

 

 # Loop to find the sum of the

 # matrix of every possible submatrix

 for x in range (N):

 for y in range (M) :

 if (x + i - 1 <= N - 1 and

 y + i - 1 <= M - 1):

 if (sumQuery(aux, x, y,

 x + i - 1,

 y + i - 1) > K):

 satisfies = False

 

 if (satisfies == True):

 return (i)

 return 0

# Driver Code

if __name__ == "__main__":

 K = 30

 mat = [[1, 2, 3, 4, 6],

 [5, 3, 8, 1, 2],

 [4, 6, 7, 5, 5],

 [2, 4, 8, 9, 4]]

 print( maximumSquareSize(mat, K))

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

// C# implementation to find the

// maximum size square submatrix

// such that their sum is less than K

using System;

public class GFG{

 

// Size of matrix

static readonly int N = 4;

static readonly int M = 5;

 

// Function to preprocess the matrix

// for computing the sum of every

// possible matrix of the given size

static void preProcess(int [,]mat,

 int [,]aux)

{

 // Loop to copy the first row

 // of the matrix into the aux matrix

 for (int i = 0; i < M; i++)

 aux[0,i] = mat[0,i];

 

 // Computing the sum column-wise

 for (int i = 1; i < N; i++)

 for (int j = 0; j < M; j++)

 aux[i,j] = mat[i,j] +

 aux[i - 1,j];

 

 // Computing row wise sum

 for (int i = 0; i < N; i++)

 for (int j = 1; j < M; j++)

 aux[i,j] += aux[i,j - 1];

}

 

// Function to find the sum of a

// submatrix with the given indices

static int sumQuery(int [,]aux, int tli,

 int tlj, int rbi, int rbj)

{

 // Overall sum from the top to

 // right corner of matrix

 int res = aux[rbi,rbj];

 

 // Removing the sum from the top

 // corer of the matrix

 if (tli > 0)

 res = res - aux[tli - 1,rbj];

 

 // Remove the overlapping sum

 if (tlj > 0)

 res = res - aux[rbi,tlj - 1];

 

 // Add the sum of top corner

 // which is substracted twice

 if (tli > 0 && tlj > 0)

 res = res +

 aux[tli - 1,tlj - 1];

 

 return res;

}

 

// Function to find the maximum

// square size possible with the

// such that every submatrix have

// sum less than the given sum

static int maximumSquareSize(int [,]mat, int K)

{

 int [,]aux = new int[N,M];

 preProcess(mat, aux);

 

 // Loop to choose the size of matrix

 for (int i = Math.Min(N, M); i >= 1; i--) {

 

 bool satisfies = true;

 

 // Loop to find the sum of the

 // matrix of every possible submatrix

 for (int x = 0; x < N; x++) {

 for (int y = 0; y < M; y++) {

 if (x + i - 1 <= N - 1 &&

 y + i - 1 <= M - 1) {

 if (sumQuery(aux, x, y,

 x + i - 1, y + i - 1) > K)

 satisfies = false;

 }

 }

 }

 if (satisfies == true)

 return (i);

 }

 return 0;

}

 

// Driver Code

public static void Main(String[] args)

{

 int K = 30;

 int [,]mat = { { 1, 2, 3, 4, 6 },

 { 5, 3, 8, 1, 2 },

 { 4, 6, 7, 5, 5 },

 { 2, 4, 8, 9, 4 } };

 

 Console.Write(maximumSquareSize(mat, K));

}

}

 

// This code contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    2

