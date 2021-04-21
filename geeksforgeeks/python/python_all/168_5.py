Sum of columns of a 2-D Matrix where first element is odd



Given a matrix **mat[][]** , the task is to print the **sum of the columns**
where **the first element is odd**.

 **Examples:**

>  **Input:** mat[][] = {  
> {8, 2, 3, 5},  
> {9, 8, 7, 6},  
> {1, 2, 5, 5} }  
>  **Output:** 31  
> Only the **third** and the **fourth** column start with an odd element.  
> And, sum = 3 + 7 + 5 + 5 + 6 + 5 = 31
>
>  **Input:** mat[][] = {  
> {10, 80, 20, 12, 40},  
> {10, 21, 23, 45, 29},  
> {19, 18, 17, 16, 15},  
> {10, 11, 12, 13, 14} }  
>  **Output:** -1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Initialize **sum = 0** and start traverse the first row, if any
element in the first row is odd then add all the elements of that column to
the sum. Print the **sum** in the end.

  

  

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP implementation of the approach

#include<bits/stdc++.h>

using namespace std;

 

// Function to return the sum of those columns 

// of a given matrix that start with an odd element

int sumColumns(int arr[][4], int r, int c)

{

 

 // Initialize sum to 0

 int sum = 0;

 

 // Traverse through all the elements of the first row

 for (int j = 0; j < c; j++)

 {

 // If the element is odd

 if (arr[0][j] % 2 != 0)

 {

 // Add all the elements of that column

 for (int i = 0; i < r; i++)

 sum += arr[i][j];

 } 

 

 

 }

 

 // Return the sum

 return sum;

 

}

 

// Driver code

int main()

{

int arr[3][4] = {{8, 2, 3, 5},{9, 8, 7, 6}, {1, 2, 5, 5}};

int r = sizeof(arr)/sizeof(arr[0]);

int c = sizeof(arr[0])/sizeof(int);

cout<<(sumColumns(arr, 3, 4));

}

 

// This code is contributed by

// Surendra_Gangwar  
  
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

import java.io.*;

 

class GFG 

{

 

// Function to return the sum of those columns 

// of a given matrix that start with an odd element

static int sumColumns(int arr[][], int r, int c)

{

 

 // Initialize sum to 0

 int sum = 0;

 

 // Traverse through all the 

 // elements of the first row

 for (int j = 0; j < c; j++)

 {

 // If the element is odd

 if (arr[0][j] % 2 != 0)

 {

 // Add all the elements of that column

 for (int i = 0; i < r; i++)

 sum += arr[i][j];

 } 

 }

 

 // Return the sum

 return sum;

}

 

// Driver code

public static void main (String[] args)

{

 int arr[][] = {{8, 2, 3, 5},{9, 8, 7,
6}, {1, 2, 5, 5}};

 System.out.println(sumColumns(arr, 3, 4));

}

}

 

// This code is contributed by

// shs..  
  
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

 

# Function to return the sum of those columns 

# of a given matrix that start with an odd element

def sumColumns(arr, r, c):

 

 # Initialize sum to 0

 sum = 0

 

 # Traverse through all the elements of the first row

 for j in range(c):

 

 # If the element is odd

 if (arr[0][j] % 2 != 0):

 

 # Add all the elements of that column

 for i in range(r):

 sum += arr[i][j]

 

 # Return the sum

 return sum

 

# Driver code

arr = [ [8, 2, 3, 5], [9, 8, 7, 6],
[1, 2, 5, 5] ]

r = len(arr)

c = len(arr[0])

print(sumColumns(arr, r, c))  
  
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

 

 // Function to return the sum of those columns 

 // of a given matrix that start with an odd element 

 static int sumColumns(int [,]arr, int r, int c) 

 { 

 

 // Initialize sum to 0 

 int sum = 0; 

 

 // Traverse through all the 

 // elements of the first row 

 for (int j = 0; j < c; j++) 

 { 

 // If the element is odd 

 if (arr[0, j] % 2 != 0) 

 { 

 // Add all the elements of that column 

 for (int i = 0; i < r; i++) 

 sum += arr[i, j]; 

 } 

 } 

 

 // Return the sum 

 return sum; 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 int [,]arr= {{8, 2, 3, 5}, {9, 8, 7, 6}, {1, 2, 5, 5}}; 

 Console.WriteLine(sumColumns(arr, 3, 4)); 

 } 

} 

 

// This code is contributed by aishwarya.27  
  
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

 

// Function to return the sum of those

// columns of a given matrix that start 

// with an odd element 

function sumColumns($arr, $r, $c) 

{ 

 

 // Initialize sum to 0 

 $sum = 0; 

 

 // Traverse through all the elements 

 // of the first row 

 for ($j = 0; $j < $c; $j++) 

 { 

 // If the element is odd 

 if ($arr[0][$j] % 2 != 0) 

 { 

 // Add all the elements of that column 

 for ($i = 0; $i < $r; $i++) 

 $sum += $arr[$i][$j]; 

 } 

 } 

 

 // Return the sum 

 return $sum; 

} 

 

// Driver code 

$arr = array(array(8, 2, 3, 5),

 array(9, 8, 7, 6), 

 array(1, 2, 5, 5)); 

 

$r = sizeof($arr); 

$c = sizeof($arr[0]); 

 

echo (sumColumns($arr, $r, $c)); 

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    31
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

