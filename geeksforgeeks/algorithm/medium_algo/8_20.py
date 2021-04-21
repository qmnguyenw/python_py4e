XOR of a submatrix queries



Given an **N * N** matrix and **q** queries, each containing position of top-
left and bottom-right corner of a rectangular sub-matrix, the task is to find
the xor of all the elements from this sub-matrix.

 **Examples:**

>  **Input:** arr[][] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, q[] = {{1, 1, 2,
> 2}, {1, 2, 2, 2}}  
>  **Output:**  
>  2  
> 15  
> Query 1: 5 ^ 6 ^ 8 ^ 9 = 2  
> Query 2: 6 ^ 9 = 15
>
>  **Input:** arr[][] = {{21, 2}, { 14, 5}}, q[] = {{0, 1, 1, 1}, {0, 0, 1,
> 1}}  
>  **Output:**  
>  7  
> 28

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **simple solution** is to find the XOR of the entire sub-matrix for each
query. Thus, the worst case time complexity for each query will be O(n2).

  

  

 **Efficient Approach:** We are all familiar with the idea of prefix XOR on
linear array i.e.

> if arr[] = {1, 2, 3, 4} and we calculate prefixXOR[] = {1, 3, 0, 4} where
> prefixXOR[i] stores the XOR of values from arr[0] to arr[i]  
> Then the XOR of sub-array arr[i] to arr[j] can be found as prefixXOR[j] ^
> prefixXOR[i – 1]  
> For example, the XOR of sub-array {2, 3} will be XOR(0, 1) = 1  
> This is because in the prefixXOR values for {1, 2, 3} and {1}, the value 1
> got repeated twice which will give 0 as the XOR result and will not affect
> the value of the other XOR operations.

We will try to extend the same to the 2-D matrix. We will compute a prefix-XOR
matrix which will help us in solving each query in O(1).  
In this case, our prefix-XOR matrix at position (R, C) will store the XOR of
the rectangular sub-matrix with top-left corner at(0, 0) and bottom-right
corner at (R, C).  
We calculate the prefix-XOR in two steps.

  1. Calculate the prefix-XOR for each row of the original matrix from left to right.
  2. On the above matrix, calculate the prefix XOR for each column from top to bottom.

Once, we have the required prefix XOR-matrix, we can answer the queries with
simplicity. XOR of a sub-matrix from (R1, C1) to (R2, C2) can be computed as
**prefix_xor[R2][C2] ^ prefix_xor[R1 – 1][C2] ^ prefix_xor[R2][C1 – 1] ^
prefix_xor[R1 – 1][C1 – 1]**.

 **Note:** If R1 or C1 equals 0, then R1 – 1 or C1 – 1 should also be 0.

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

#include <iostream>

#define n 3

using namespace std;

 

// Function to pre-compute the xor

void preComputeXor(int arr[][n], int prefix_xor[][n])

{

 // Left to right prefix xor

 // for each row

 for (int i = 0; i < n; i++)

 for (int j = 0; j < n; j++) {

 if (j == 0)

 prefix_xor[i][j] = arr[i][j];

 else

 prefix_xor[i][j]

 = (prefix_xor[i][j - 1] ^ arr[i][j]);

 }

 

 // Top to bottom prefix xor

 // for each column

 for (int i = 0; i < n; i++)

 for (int j = 1; j < n; j++)

 prefix_xor[j][i]

 = (prefix_xor[j - 1][i] ^ prefix_xor[j][i]);

}

 

// Function to process the queries

// x1, x2, y1, y2 represent the

// positions of the top-left

// and bottom right corners

int ansQuerie(int prefix_xor[][n], int x1, int y1, int x2,
int y2)

{

 

 // To store the xor values

 int xor_1 = 0, xor_2 = 0, xor_3 = 0;

 

 // Finding the values we need to xor

 // with value at (x2, y2) in prefix-xor

 // matrix

 if (x1 != 0)

 xor_1 = prefix_xor[x1 - 1][y2];

 if (y1 != 0)

 xor_2 = prefix_xor[x2][y1 - 1];

 if (x1 != 0 and y1 != 0)

 xor_3 = prefix_xor[x1 - 1][y1 - 1];

 

 // Return the required prefix xor

 return ((prefix_xor[x2][y2] ^ xor_1) ^ (xor_2 ^ xor_3));

}

 

// Driver code

int main()

{

 int arr[][n] = { { 1, 2, 3 },

 { 4, 5, 6 },

 { 7, 8, 9 } };

 

 // To store pre-computed xor

 int prefix_xor[n][n];

 

 // Pre-computing xor

 preComputeXor(arr, prefix_xor);

 

 // Queries

 cout << ansQuerie(prefix_xor, 1, 1, 2, 2) << endl;

 cout << ansQuerie(prefix_xor, 1, 2, 2, 2) << endl;

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

class GfG

{

 

static int n = 3;

 

// Function to pre-compute the xor 

static void preComputeXor(int arr[][], 

 int prefix_xor[][]) 

{ 

 // Left to right prefix xor 

 // for each row 

 for (int i = 0; i < n; i++) 

 for (int j = 0; j < n; j++) 

 { 

 if (j == 0) 

 prefix_xor[i][j] = arr[i][j]; 

 else

 prefix_xor[i][j] = 

 (prefix_xor[i][j - 1] ^ arr[i][j]); 

 } 

 

 // Top to bottom prefix xor 

 // for each column 

 for (int i = 0; i < n; i++) 

 for (int j = 1; j < n; j++) 

 prefix_xor[j][i] = 

 (prefix_xor[j - 1][i] ^ prefix_xor[j][i]); 

} 

 

// Function to process the queries 

// x1, x2, y1, y2 represent the 

// positions of the top-left 

// and bottom right corners 

static int ansQuerie(int prefix_xor[][], int x1, 

 int y1, int x2, int y2) 

{ 

 

 // To store the xor values 

 int xor_1 = 0, xor_2 = 0, xor_3 = 0; 

 

 // Finding the values we need to xor 

 // with value at (x2, y2) in prefix-xor 

 // matrix 

 if (x1 != 0) 

 xor_1 = prefix_xor[x1 - 1][y2]; 

 if (y1 != 0) 

 xor_2 = prefix_xor[x2][y1 - 1]; 

 if (x1 != 0 && y1 != 0) 

 xor_3 = prefix_xor[x1 - 1][y1 - 1]; 

 

 // Return the required prefix xor 

 return ((prefix_xor[x2][y2] ^ xor_1) ^ (xor_2 ^ xor_3)); 

} 

 

// Driver code 

public static void main(String[] args) 

{ 

 int arr[][] = new int[][]{{ 1, 2, 3 },

 { 4, 5, 6 }, 

 { 7, 8, 9 }}; 

 

 // To store pre-computed xor 

 int prefix_xor[][] = new int[n][n]; 

 

 // Pre-computing xor 

 preComputeXor(arr, prefix_xor); 

 

 // Queries 

 System.out.println(ansQuerie(prefix_xor, 1, 1, 2, 2)); 

 System.out.println(ansQuerie(prefix_xor, 1, 2, 2, 2)); 

} 

} 

 

// This code is contributed by 

// Prerna Saini.  
  
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

n= 3

 

# Function to pre-compute the xor

def preComputeXor(arr, prefix_xor):

 

 # Left to right prefix xor

 # for each row

 for i in range(n):

 for j in range(n):

 if (j == 0):

 prefix_xor[i][j] = arr[i][j]

 else:

 prefix_xor[i][j] = (prefix_xor[i][j - 1] ^ 

 arr[i][j])

 

 # Top to bottom prefix xor

 # for each column

 for i in range(n):

 for j in range(1, n):

 prefix_xor[j][i] = (prefix_xor[j - 1][i] ^ 

 prefix_xor[j][i])

 

# Function to process the queries

# x1, x2, y1, y2 represent the

# positions of the top-left

# and bottom right corners

def ansQuerie(prefix_xor, x1, y1, x2, y2):

 

 # To store the xor values

 xor_1, xor_2, xor_3 = 0, 0, 0

 

 # Finding the values we need to xor

 # with value at (x2, y2) in prefix-xor

 # matrix

 if (x1 != 0):

 xor_1 = prefix_xor[x1 - 1][y2]

 if (y1 != 0):

 xor_2 = prefix_xor[x2][y1 - 1]

 if (x1 != 0 and y1 != 0):

 xor_3 = prefix_xor[x1 - 1][y1 - 1]

 

 # Return the required prefix xor

 return ((prefix_xor[x2][y2] ^ xor_1) ^ 

 (xor_2 ^ xor_3))

 

 

# Driver code

arr = [[ 1, 2, 3 ],

 [ 4, 5, 6 ],

 [ 7, 8, 9 ]]

 

# To store pre-computed xor

prefix_xor = [[0 for i in range(n)]

 for i in range(n)]

 

# Pre-computing xor

preComputeXor(arr, prefix_xor)

 

# Queries

print(ansQuerie(prefix_xor, 1, 1, 2, 2))

print(ansQuerie(prefix_xor, 1, 2, 2, 2))

 

# This code is contributed by Mohit Kumar  
  
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

 

class GfG 

{ 

 static int n = 3; 

 

 // Function to pre-compute the xor 

 static void preComputeXor(int [,]arr, 

 int [,]prefix_xor) 

 { 

 // Left to right prefix xor 

 // for each row 

 for (int i = 0; i < n; i++) 

 for (int j = 0; j < n; j++) 

 { 

 if (j == 0) 

 prefix_xor[i, j] = arr[i, j]; 

 else

 prefix_xor[i, j] = 

 (prefix_xor[i, j - 1] ^ arr[i, j]); 

 } 

 

 // Top to bottom prefix xor 

 // for each column 

 for (int i = 0; i < n; i++) 

 for (int j = 1; j < n; j++) 

 prefix_xor[j, i] = 

 (prefix_xor[j - 1, i] ^ 

 prefix_xor[j, i]); 

 } 

 

 // Function to process the queries 

 // x1, x2, y1, y2 represent the 

 // positions of the top-left 

 // and bottom right corners 

 static int ansQuerie(int [,]prefix_xor, int x1, 

 int y1, int x2, int y2) 

 { 

 

 // To store the xor values 

 int xor_1 = 0, xor_2 = 0, xor_3 = 0; 

 

 // Finding the values we need to xor 

 // with value at (x2, y2) in prefix-xor 

 // matrix 

 if (x1 != 0) 

 xor_1 = prefix_xor[x1 - 1, y2]; 

 if (y1 != 0) 

 xor_2 = prefix_xor[x2, y1 - 1]; 

 if (x1 != 0 && y1 != 0) 

 xor_3 = prefix_xor[x1 - 1, y1 - 1]; 

 

 // Return the required prefix xor 

 return ((prefix_xor[x2,y2] ^ xor_1) ^ 

 (xor_2 ^ xor_3)); 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 int [,]arr = {{ 1, 2, 3 }, 

 { 4, 5, 6 },

 { 7, 8, 9 }}; 

 

 // To store pre-computed xor 

 int [,]prefix_xor = new int[n, n]; 

 

 // Pre-computing xor 

 preComputeXor(arr, prefix_xor); 

 

 // Queries 

 Console.WriteLine(ansQuerie(prefix_xor, 1, 1, 2, 2)); 

 Console.WriteLine(ansQuerie(prefix_xor, 1, 2, 2, 2)); 

 } 

} 

 

// This code is contributed by Ryuga  
  
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

 

$n = 3;

 

// Function to pre-compute the xor

function preComputeXor($arr, &$prefix_xor)

{

 global $n;

 

 // Left to right prefix xor

 // for each row

 for ($i = 0; $i < $n; $i++)

 for ($j = 0; $j < $n; $j++) 

 {

 if ($j == 0)

 $prefix_xor[$i][$j] = $arr[$i][$j];

 else

 $prefix_xor[$i][$j] = ($prefix_xor[$i][$j - 1] ^ 

 $arr[$i][$j]);

 }

 

 // Top to bottom prefix xor

 // for each column

 for ($i = 0; $i < $n; $i++)

 for ($j = 1; $j < $n; $j++)

 $prefix_xor[$j][$i] = ($prefix_xor[$j - 1][$i] ^

 $prefix_xor[$j][$i]);

}

 

// Function to process the queries

// x1, x2, y1, y2 represent the

// positions of the top-left

// and bottom right corners

function ansQuerie($prefix_xor, $x1, 

 $y1, $x2, $y2)

{

 

 // To store the xor values

 $xor_1 = $xor_2 = $xor_3 = 0;

 

 // Finding the values we need to xor

 // with value at (x2, y2) in prefix-xor

 // matrix

 if ($x1 != 0)

 $xor_1 = $prefix_xor[$x1 - 1][$y2];

 if ($y1 != 0)

 $xor_2 = $prefix_xor[$x2][$y1 - 1];

 if ($x1 != 0 and $y1 != 0)

 $xor_3 = $prefix_xor[$x1 - 1][$y1 - 1];

 

 // Return the required prefix xor

 return (($prefix_xor[$x2][$y2] ^ $xor_1) ^ 

 ($xor_2 ^ $xor_3));

}

 

// Driver code

$arr = array(array( 1, 2, 3 ),

 array( 4, 5, 6 ),

 array( 7, 8, 9 ));

 

// To store pre-computed xor

$prefix_xor = array_fill(0, $n, 

 array_fill(0, $n, 0));

 

// Pre-computing xor

preComputeXor($arr, $prefix_xor);

 

// Queries

echo ansQuerie($prefix_xor, 1, 1, 2, 2) . "\n";

echo ansQuerie($prefix_xor, 1, 2, 2, 2);

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    15
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

