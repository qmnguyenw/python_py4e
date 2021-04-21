XOR of XORs of all sub-matrices



Given a **‘N*N’** matrix, the task is to find the XOR of XORs of all possible
sub-matrices.  
 **Examples:**

    
    
    **Input :** arr =  {{3, 1},
                   {1, 3}}
    **Output :** 0
    **Explanation** : All the elements lie in 4 submatrices each. 
    4 being even, there total contribution towards 
    final answer becomes 0. Thus, ans = 0.
    
    **Input :** arr = {{6, 7, 13},
                   {8, 3, 4},
                   {9, 7, 6}};
    **Output :** 4

A **Simple Approach** is to generate all the possible submatrices, find the
XOR of each submatrice uniquely and then XOR them all up. The time complexity
of this approach will be O(n6).  
 **Better solution:** For each index(R, C), we will try to find the number of
sub-matrices in which that index lies. If the number of sub-matrices is odd,
then the final answer will be updated as **ans = (ans ^ arr[R][C])**. In case
of even, we don’t need to update answer. This works because a number XORed
with itself gives zero and order of operation doesn’t effect final XOR value.  
Assuming 0-based indexing, number of sub-matrices an index (R, C) lies in
equals

    
    
    (R + 1)*(C + 1)*(N - R)*(N - C)

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the XOR of XOR's of

// all submatrices

#include <iostream>

using namespace std;

#define n 3

// Function to find to required

// XOR value

int submatrixXor(int arr[][n])

{

 int ans = 0;

 // Nested loop to find the

 // number of sub-matrix each

 // index belongs to

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < n; j++) {

 // Number of ways to choose

 // from top-left elements

 int top_left = (i + 1) * (j + 1);

 // Number of ways to choose

 // from bottom-right elements

 int bottom_right = (n - i) * (n - j);

 if ((top_left % 2 == 1) && (bottom_right % 2 == 1))

 ans = (ans ^ arr[i][j]);

 }

 }

 return ans;

}

// Driver Code

int main()

{

 int arr[][n] = { { 6, 7, 13 },

 { 8, 3, 4 },

 { 9, 7, 6 } };

 cout << submatrixXor(arr);

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

//Java program to find the XOR of XOR's

// of all submatrices

class GFG

{

 

// Function to find to required

// XOR value

static int submatrixXor(int[][]arr)

{

 int n = 3;

 int ans = 0;

 // Nested loop to find the

 // number of sub-matrix each

 // index belongs to

 for (int i = 0; i < n; i++)

 {

 for (int j = 0; j < n; j++)

 {

 // Number of ways to choose

 // from top-left elements

 int top_left = (i + 1) * (j + 1);

 // Number of ways to choose

 // from bottom-right elements

 int bottom_right = (n - i) * (n - j);

 if ((top_left % 2 == 1) &&

 (bottom_right % 2 == 1))

 ans = (ans ^ arr[i][j]);

 }

 }

 return ans;

}

// Driver Code

public static void main(String[] args)

{

 int[][] arr = {{ 6, 7, 13},

 { 8, 3, 4 },

 { 9, 7, 6 }};

 System.out.println(submatrixXor(arr));

}

}

// This code is contributed

// by Code_Mech.  
  
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

# Python3 program to find the XOR of

# XOR's of all submatrices

# Function to find to required

# XOR value

def submatrixXor(arr, n):

 ans = 0

 # Nested loop to find the

 # number of sub-matrix each

 # index belongs to

 for i in range(0, n):

 for j in range(0, n):

 # Number of ways to choose

 # from top-left elements

 top_left = (i + 1) * (j + 1)

 # Number of ways to choose

 # from bottom-right elements

 bottom_right = (n - i) * (n - j)

 if (top_left % 2 == 1 and

 bottom_right % 2 == 1):

 ans = (ans ^ arr[i][j])

 return ans

# Driver code

n = 3

arr = [[6, 7, 13],

 [8, 3, 4],

 [9, 7, 6]]

print(submatrixXor(arr, n))

# This code is contributed by Shrikant13  
  
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

// C# program to find the XOR of XOR's

// of all submatrices

using System;

class GFG

{

 

// Function to find to required

// XOR value

static int submatrixXor(int [,]arr)

{

 int n = 3;

 int ans = 0;

 // Nested loop to find the

 // number of sub-matrix each

 // index belongs to

 for (int i = 0; i < n; i++)

 {

 for (int j = 0; j < n; j++)

 {

 // Number of ways to choose

 // from top-left elements

 int top_left = (i + 1) * (j + 1);

 // Number of ways to choose

 // from bottom-right elements

 int bottom_right = (n - i) * (n - j);

 if ((top_left % 2 == 1) &&

 (bottom_right % 2 == 1))

 ans = (ans ^ arr[i, j]);

 }

 }

 return ans;

}

// Driver Code

public static void Main()

{

 int [, ]arr = {{ 6, 7, 13},

 { 8, 3, 4 },

 { 9, 7, 6 }};

 Console.Write(submatrixXor(arr));

}

}

// This code is contributed

// by Akanksha Rai  
  
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

// PHP program to find the XOR of

// XOR's of all submatrices

// Function to find to required

// XOR value

function submatrixXor($arr)

{

 $ans = 0;

 $n = 3 ;

 // Nested loop to find the

 // number of sub-matrix each

 // index belongs to

 for ($i = 0; $i < $n; $i++)

 {

 for ($j = 0; $j < $n; $j++)

 {

 // Number of ways to choose

 // from top-left elements

 $top_left = ($i + 1) * ($j + 1);

 // Number of ways to choose

 // from bottom-right elements

 $bottom_right = ($n - $i) * ($n - $j);

 if (($top_left % 2 == 1) &&

 ($bottom_right % 2 == 1))

 $ans = ($ans ^ $arr[$i][$j]);

 }

 }

 return $ans;

}

// Driver Code

$arr = array(array( 6, 7, 13 ),

 array( 8, 3, 4 ),

 array( 9, 7, 6 ));

echo submatrixXor($arr);

# This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    4

**Time Complexity** : O(N2)  
 **Auxiliary Space:** O(1)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

