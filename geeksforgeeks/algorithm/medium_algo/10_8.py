Print matrix after applying increment operations in M ranges



Given a 2-D matrix **mat[][]** of size **N * N** , initially all the elements
of the matrix are **0**. A number of queries(M ranges) need to be performed on
the matrix where each query consists of four integers **X1** , **Y1** , **X2**
and **Y2** , the task is to add **1** to all the cells between **mat[X1][Y1]**
and **mat[X2][Y2]** (including both) and print the contents of the updated
matrix in the end.

 **Examples:**

>  **Input:** N = 2, q[][] = { { 0, 0, 1, 1 }, { 0, 0, 0, 1 } }  
>  **Output:**  
>  2 2  
> 1 1  
> After 1st query: mat[][] = { {1, 1}, {1, 1} }  
> After 2nd query: mat[][] = { {2, 2}, {1, 1} }
>
>  **Input:** N = 5, q[][] = { { 0, 0, 1, 2 }, { 1, 2, 3, 4 }, { 1, 4, 3, 4 }
> }  
>  **Output:**  
>  1 1 1 1 1  
> 1 1 2 1 2  
> 2 2 2 2 2  
> 2 2 2 2 2  
> 0 0 0 0 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** For each query **(X1, Y1)** represents the top left cell of the
sub-matrix and **(X2, Y2)** represents the bottom right cell of the sub-
matrix. For each top left cell add **1** to the top left element and subtract
**1** from the element next to bottom right cell (if any).  
Then maintain a running sum of all the elements from the original (now
modified) matrix and at every addition, the current sum is the element
(updated) at the current position.

  

  

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

#include<bits/stdc++.h>

using namespace std;

 

// Function to update and print the 

// matrix after performing queries

void updateMatrix(int n, int q[3][4])

{

 int i, j;

 int mat[n][n];

 for(int i = 0; i < n; i++)

 for(int j = 0; j < n; j++)

 mat[i][j] = 0;

 for (i = 0; i < 3; i++)

 {

 int X1 = q[i][0];

 int Y1 = q[i][1];

 int X2 = q[i][2];

 int Y2 = q[i][3];

 

 // Add 1 to the first element of 

 // the sub-matrix

 mat[X1][Y1]++;

 

 // If there is an element after the 

 // last element of the sub-matrix 

 // then decrement it by 1

 if (Y2 + 1 < n)

 mat[X2][Y2 + 1]--;

 else if (X2 + 1 < n)

 mat[X2 + 1][0]--;

 }

 

 // Calculate the running sum

 int sum = 0;

 for (i = 0; i < n; i++)

 {

 for (j = 0; j < n; j++) 

 {

 sum += mat[i][j];

 

 // Print the updated element

 cout << sum << " ";

 }

 

 // Next line

 cout << endl;

 }

}

 

// Driver code

int main()

{

 

 // Size of the matrix

 int n = 5;

 

 

 // Queries

 int q[3][4] = {{ 0, 0, 1, 2 },

 { 1, 2, 3, 4 },

 { 1, 4, 3, 4 }};

 

 updateMatrix(n, q);

 return 0;

}

 

// This code is contributed by chandan_jnu  
  
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

public class GFG {

 

 // Function to update and print the matrix

 // after performing queries

 static void updateMatrix(int n, int q[][], int mat[][])

 {

 int i, j;

 for (i = 0; i < q.length; i++) {

 int X1 = q[i][0];

 int Y1 = q[i][1];

 int X2 = q[i][2];

 int Y2 = q[i][3];

 

 // Add 1 to the first element of the sub-matrix

 mat[X1][Y1]++;

 

 // If there is an element after the last element

 // of the sub-matrix then decrement it by 1

 if (Y2 + 1 < n)

 mat[X2][Y2 + 1]--;

 else if (X2 + 1 < n)

 mat[X2 + 1][0]--;

 }

 

 // Calculate the running sum

 int sum = 0;

 for (i = 0; i < n; i++) {

 for (j = 0; j < n; j++) {

 sum += mat[i][j];

 

 // Print the updated element

 System.out.print(sum + " ");

 }

 

 // Next line

 System.out.println();

 }

 }

 

 // Driver code

 public static void main(String[] args)

 {

 

 // Size of the matrix

 int n = 5;

 int mat[][] = new int[n][n];

 

 // Queries

 int q[][] = { { 0, 0, 1, 2 },

 { 1, 2, 3, 4 },

 { 1, 4, 3, 4 } };

 

 updateMatrix(n, q, mat);

 }

}  
  
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

// C# implementation of the above approach

 

using System;

 

public class GFG { 

 

 // Function to update and print the matrix 

 // after performing queries 

 static void updateMatrix(int n, int [,]q, int [,]mat) 

 { 

 int i, j; 

 for (i = 0; i < q.GetLength(0); i++) { 

 int X1 = q[i,0]; 

 int Y1 = q[i,1]; 

 int X2 = q[i,2]; 

 int Y2 = q[i,3]; 

 

 // Add 1 to the first element of the sub-matrix 

 mat[X1,Y1]++; 

 

 // If there is an element after the last element 

 // of the sub-matrix then decrement it by 1 

 if (Y2 + 1 < n) 

 mat[X2,Y2 + 1]--; 

 else if (X2 + 1 < n) 

 mat[X2 + 1,0]--; 

 } 

 

 // Calculate the running sum 

 int sum = 0; 

 for (i = 0; i < n; i++) { 

 for (j = 0; j < n; j++) { 

 sum += mat[i,j]; 

 

 // Print the updated element 

 Console.Write(sum + " "); 

 } 

 

 // Next line 

 Console.WriteLine(); 

 } 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 

 // Size of the matrix 

 int n = 5; 

 int [,]mat = new int[n,n]; 

 

 // Queries 

 int [,]q = { { 0, 0, 1, 2 }, 

 { 1, 2, 3, 4 }, 

 { 1, 4, 3, 4 } }; 

 

 updateMatrix(n, q, mat); 

 } 

 // This code is contributed by Ryuga

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

# Python 3 implementation of the approach

 

# Function to update and print the matrix

# after performing queries

def updateMatrix(n, q, mat):

 

 for i in range(0, len(q)):

 X1 = q[i][0];

 Y1 = q[i][1];

 X2 = q[i][2];

 Y2 = q[i][3];

 

 # Add 1 to the first element of

 # the sub-matrix

 mat[X1][Y1] = mat[X1][Y1] + 1;

 

 # If there is an element after the 

 # last element of the sub-matrix

 # then decrement it by 1

 if (Y2 + 1 < n):

 mat[X2][Y2 + 1] = mat[X2][Y2 + 1] - 1;

 elif (X2 + 1 < n):

 mat[X2 + 1][0] = mat[X2 + 1][0] - 1;

 

 # Calculate the running sum

 sum = 0;

 for i in range(0, n):

 for j in range(0, n): 

 sum =sum + mat[i][j];

 

 # Print the updated element

 print(sum, end = ' ');

 

 # Next line

 print(" ");

 

# Driver code

 

# Size of the matrix

n = 5;

mat = [[0 for i in range(n)] 

 for i in range(n)];

 

# Queries

q = [[ 0, 0, 1, 2 ],

 [ 1, 2, 3, 4 ],

 [ 1, 4, 3, 4 ]];

 

updateMatrix(n, q, mat);

 

# This code is contributed 

# by Shivi_Aggarwal  
  
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

 

// Function to update and print the 

// matrix after performing queries

function updateMatrix($n, $q, $mat)

{

 for ($i = 0; $i < sizeof($q); $i++) 

 {

 $X1 = $q[$i][0];

 $Y1 = $q[$i][1];

 $X2 = $q[$i][2];

 $Y2 = $q[$i][3];

 

 // Add 1 to the first element of 

 // the sub-matrix

 $mat[$X1][$Y1]++;

 

 // If there is an element after the last 

 // element of the sub-matrix then decrement 

 // it by 1

 if ($Y2 + 1 < $n)

 $mat[$X2][$Y2 + 1]--;

 else if ($X2 + 1 < $n)

 $mat[$X2 + 1][0]--;

 }

 

 // Calculate the running sum

 $sum = 0;

 for ($i = 0; $i < $n; $i++) 

 {

 for ($j = 0; $j < $n; $j++) 

 {

 $sum += $mat[$i][$j];

 

 // Print the updated element

 echo($sum . " ");

 }

 

 // Next line

 echo("\n");

 }

}

 

// Driver code

 

// Size of the matrix

$n = 5;

$mat = array_fill(0, $n,

 array_fill(0, $n, 0));

 

// Queries

$q = array(array( 0, 0, 1, 2 ),

 array( 1, 2, 3, 4 ),

 array( 1, 4, 3, 4 ));

 

updateMatrix($n, $q, $mat);

 

// This code is contributed by chandan_jnu

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    1 1 1 1 1 
    1 1 2 1 2 
    2 2 2 2 2 
    2 2 2 2 2 
    0 0 0 0 0
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

