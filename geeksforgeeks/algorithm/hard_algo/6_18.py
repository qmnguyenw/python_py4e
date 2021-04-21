Search element in a Spirally sorted Matrix



Given a spirally sorted matrix with **N * N** elements and an integer **X** ,
the task is to find the position of this given integer in the matrix if it
exists, else print **-1**. **Note** that all the matrix elements are distinct.

 **Examples:**

>  **Input:** arr[] = {  
> {1, 2, 3, 4},  
> {12, 13, 14, 5},  
> {11, 16, 15, 6},  
> {10, 9, 8, 7}}, X = 9  
>  **Output:** 3 1  
> 9 appears in row number 3 and column number 1 (0-based indexing)  
> Thus, output is (3, 1).
>
>  **Input:** arr[] = {  
> {1, 2, 3},  
> {8, 9, 4},  
> {7, 6, 5}}, X = 9  
>  **Output:** 1 1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **simple solution** is to search through all the elements in the array. The
worst case time complexity of this approach will be **O(n 2)**.

  

  

A **better solution** is to use binary search. We apply binary search in two
phases.  
But before jumping to that, lets define what a ring means in here. A ring is
defined as a set of all the cells in the array such that there minimum of the
distances from all the four sides is equal.

First, we try to determine the ring the number ‘X’ will belong to. We will do
this using binary search. For that, observe the diagonal elements of the
matrix. First ceil(N/2) of the diagonal matrix are guaranteed to be sorted in
increasing order. So, each one of the ceil(N/2) diagonal elements can
represent a ring. By, applying binary on the first ceil(N/2) diagonal
elements, we determine the ring the number ‘X’ belongs to in O(log(n)) time.  
After that, we apply binary search on the elements of the ring. Before that we
determine the side of the ring, the number ‘X’ will belong to. Then, we apply
the binary search correspondingly.

So, the total time complexity becomes **O(log(n))**.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

 

#include <iostream>

#define n 4

using namespace std;

 

// Function to return the ring, the number x

// belongs to.

int findRing(int arr[][n], int x)

{

 // Returns -1 if number x is smaller than

 // least element of arr

 if (arr[0][0] > x)

 return -1;

 

 // l and r represent the diagonal

 // elements to search in

 int l = 0, r = (n + 1) / 2 - 1;

 

 // Returns -1 if number x is greater

 // than the largest element of arr

 if (n % 2 == 1 && arr[r][r] < x)

 return -1;

 if (n % 2 == 0 && arr[r + 1][r] < x)

 return -1;

 

 while (l < r) {

 int mid = (l + r) / 2;

 if (arr[mid][mid] <= x)

 if (mid == (n + 1) / 2 - 1

 || arr[mid + 1][mid + 1] > x)

 return mid;

 else

 l = mid + 1;

 else

 r = mid - 1;

 }

 

 return r;

}

 

// Function to perform binary search 

// on an array sorted in increasing order

// l and r represent the left and right 

// index of the row to be searched

int binarySearchRowInc(int arr[][n], int row,

 int l, int r, int x)

{

 while (l <= r) {

 int mid = (l + r) / 2;

 

 if (arr[row][mid] == x)

 return mid;

 

 if (arr[row][mid] < x)

 l = mid + 1;

 else

 r = mid - 1;

 }

 

 return -1;

}

 

// Function to perform binary search on 

// a particlar column of the 2D array

// t and b represent top and 

// bottom rows

int binarySearchColumnInc(int arr[][n], int col,

 int t, int b, int x)

{

 while (t <= b) {

 

 int mid = (t + b) / 2;

 

 if (arr[mid][col] == x)

 return mid;

 

 if (arr[mid][col] < x)

 t = mid + 1;

 else

 b = mid - 1;

 }

 

 return -1;

}

 

// Function to perform binary search on 

// an array sorted in decreasing order

int binarySearchRowDec(int arr[][n], int row,

 int l, int r, int x)

{

 while (l <= r) {

 

 int mid = (l + r) / 2;

 

 if (arr[row][mid] == x)

 return mid;

 

 if (arr[row][mid] < x)

 r = mid - 1;

 else

 l = mid + 1;

 }

 

 return -1;

}

 

// Function to perform binary search on a

// particlar column of the 2D array

int binarySearchColumnDec(int arr[][n], int col,

 int t, int b, int x)

{

 while (t <= b) {

 int mid = (t + b) / 2;

 

 if (arr[mid][col] == x)

 return mid;

 

 if (arr[mid][col] < x)

 b = mid - 1;

 else

 t = mid + 1;

 }

 

 return -1;

}

 

// Function to find the position of the number x

void spiralBinary(int arr[][n], int x)

{

 

 // Finding the ring

 int f1 = findRing(arr, x);

 

 // To store row and column

 int r, c;

 

 if (f1 == -1) {

 cout << "-1";

 return;

 }

 

 // Edge case if n is odd

 if (n % 2 == 1 && f1 == (n + 1) / 2 - 1) {

 cout << f1 << " " << f1 << endl;

 return;

 }

 

 // Check which of the 4 sides, the number x

 // lies in

 if (x < arr[f1][n - f1 - 1]) {

 c = binarySearchRowInc(arr, f1, f1,

 n - f1 - 2, x);

 r = f1;

 }

 else if (x < arr[n - f1 - 1][n - f1 - 1]) {

 c = n - f1 - 1;

 

 r = binarySearchColumnInc(arr, n - f1 - 1, f1,

 n - f1 - 2, x);

 }

 else if (x < arr[n - f1 - 1][f1]) {

 

 c = binarySearchRowDec(arr, n - f1 - 1, f1 + 1,

 n - f1 - 1, x);

 r = n - f1 - 1;

 }

 else {

 

 r = binarySearchColumnDec(arr, f1, f1 + 1,

 n - f1 - 1, x);

 c = f1;

 }

 

 // Printing the position

 if (c == -1 || r == -1)

 cout << "-1";

 else

 cout << r << " " << c;

 

 return;

}

 

// Driver code

int main()

{

 int arr[][n] = { { 1, 2, 3, 4 },

 { 12, 13, 14, 5 },

 { 11, 16, 15, 6 },

 { 10, 9, 8, 7 } };

 

 spiralBinary(arr, 7);

 

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

// Java implementation of the above approach

class GFG 

{

 

final static int n =4; 

 

// Function to return the ring, 

// the number x belongs to. 

static int findRing(int arr[][], int x) 

{ 

 // Returns -1 if number x is 

 // smaller than least element of arr 

 if (arr[0][0] > x) 

 return -1; 

 

 // l and r represent the diagonal 

 // elements to search in 

 int l = 0, r = (n + 1) / 2 - 1; 

 

 // Returns -1 if number x is greater 

 // than the largest element of arr 

 if (n % 2 == 1 && arr[r][r] < x) 

 return -1; 

 if (n % 2 == 0 && arr[r + 1][r] < x) 

 return -1; 

 

 while (l < r) 

 { 

 int mid = (l + r) / 2; 

 if (arr[mid][mid] <= x) 

 if (mid == (n + 1) / 2 - 1

 || arr[mid + 1][mid + 1] > x) 

 return mid; 

 else

 l = mid + 1; 

 else

 r = mid - 1; 

 } 

 return r; 

} 

 

// Function to perform binary search 

// on an array sorted in increasing order 

// l and r represent the left and right 

// index of the row to be searched 

static int binarySearchRowInc(int arr[][], int row, 

 int l, int r, int x) 

{ 

 while (l <= r) 

 { 

 int mid = (l + r) / 2; 

 

 if (arr[row][mid] == x) 

 return mid; 

 

 if (arr[row][mid] < x) 

 l = mid + 1; 

 else

 r = mid - 1; 

 } 

 return -1; 

} 

 

// Function to perform binary search on 

// a particlar column of the 2D array 

// t and b represent top and 

// bottom rows 

static int binarySearchColumnInc(int arr[][], int col, 

 int t, int b, int x) 

{ 

 while (t <= b)

 { 

 int mid = (t + b) / 2; 

 

 if (arr[mid][col] == x) 

 return mid; 

 

 if (arr[mid][col] < x) 

 t = mid + 1; 

 else

 b = mid - 1; 

 } 

 return -1; 

} 

 

// Function to perform binary search on 

// an array sorted in decreasing order 

static int binarySearchRowDec(int arr[][], int row, 

 int l, int r, int x) 

{ 

 while (l <= r) { 

 

 int mid = (l + r) / 2; 

 

 if (arr[row][mid] == x) 

 return mid; 

 

 if (arr[row][mid] < x) 

 r = mid - 1; 

 else

 l = mid + 1; 

 } 

 return -1; 

} 

 

// Function to perform binary search on a 

// particlar column of the 2D array 

static int binarySearchColumnDec(int arr[][], int col, 

 int t, int b, int x) 

{ 

 while (t <= b) 

 { 

 int mid = (t + b) / 2; 

 

 if (arr[mid][col] == x) 

 return mid; 

 

 if (arr[mid][col] < x) 

 b = mid - 1; 

 else

 t = mid + 1; 

 } 

 return -1; 

} 

 

// Function to find the position of the number x 

static void spiralBinary(int arr[][], int x) 

{ 

 

 // Finding the ring 

 int f1 = findRing(arr, x); 

 

 // To store row and column 

 int r, c; 

 

 if (f1 == -1) 

 { 

 System.out.print("-1");

 return; 

 } 

 

 // Edge case if n is odd 

 if (n % 2 == 1 && f1 == (n + 1) / 2 - 1)

 { 

 System.out.println(f1+" "+f1);

 return; 

 } 

 

 // Check which of the 4 sides, the number x 

 // lies in 

 if (x < arr[f1][n - f1 - 1])

 { 

 c = binarySearchRowInc(arr, f1, f1, 

 n - f1 - 2, x); 

 r = f1; 

 } 

 else if (x < arr[n - f1 - 1][n - f1 - 1]) 

 { 

 c = n - f1 - 1; 

 

 r = binarySearchColumnInc(arr, n - f1 - 1, f1, 

 n - f1 - 2, x); 

 } 

 else if (x < arr[n - f1 - 1][f1])

 { 

 c = binarySearchRowDec(arr, n - f1 - 1, f1 + 1, 

 n - f1 - 1, x); 

 r = n - f1 - 1; 

 } 

 else

 { 

 r = binarySearchColumnDec(arr, f1, f1 + 1, 

 n - f1 - 1, x); 

 c = f1; 

 } 

 

 // Printing the position 

 if (c == -1 || r == -1) 

 System.out.print("-1"); 

 else

 System.out.print(r+" "+c);

 

 return; 

} 

 

// Driver code 

public static void main(String[] args) 

{

 int arr[][] = { { 1, 2, 3, 4 }, 

 { 12, 13, 14, 5 }, 

 { 11, 16, 15, 6 }, 

 { 10, 9, 8, 7 } }; 

 

 spiralBinary(arr, 7); 

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

# Python3 implementation of the above approach

 

# Function to return the ring, 

# the number x belongs to. 

def findRing(arr, x): 

 

 # Returns -1 if number x is smaller 

 # than least element of arr 

 if arr[0][0] > x:

 return -1

 

 # l and r represent the diagonal 

 # elements to search in 

 l, r = 0, (n + 1) // 2 - 1

 

 # Returns -1 if number x is greater 

 # than the largest element of arr 

 if n % 2 == 1 and arr[r][r] < x: 

 return -1

 if n % 2 == 0 and arr[r + 1][r] < x: 

 return -1

 

 while l < r:

 mid = (l + r) // 2

 if arr[mid][mid] <= x: 

 

 if (mid == (n + 1) // 2 - 1 or

 arr[mid + 1][mid + 1] > x): 

 return mid 

 else:

 l = mid + 1

 

 else:

 r = mid - 1

 

 return r 

 

# Function to perform binary search 

# on an array sorted in increasing order 

# l and r represent the left and right 

# index of the row to be searched 

def binarySearchRowInc(arr, row, l, r, x): 

 

 while l <= r: 

 mid = (l + r) // 2

 

 if arr[row][mid] == x: 

 return mid 

 elif arr[row][mid] < x: 

 l = mid + 1

 else:

 r = mid - 1

 

 return -1

 

# Function to perform binary search on 

# a particlar column of the 2D array 

# t and b represent top and 

# bottom rows 

def binarySearchColumnInc(arr, col, t, b, x): 

 

 while t <= b:

 

 mid = (t + b) // 2

 

 if arr[mid][col] == x: 

 return mid 

 elif arr[mid][col] < x: 

 t = mid + 1

 else:

 b = mid - 1

 

 return -1

 

# Function to perform binary search on 

# an array sorted in decreasing order 

def binarySearchRowDec(arr, row, l, r, x): 

 

 while l <= r:

 

 mid = (l + r) // 2

 

 if arr[row][mid] == x: 

 return mid 

 elif arr[row][mid] < x: 

 r = mid - 1

 else:

 l = mid + 1

 

 return -1

 

# Function to perform binary search on a 

# particlar column of the 2D array 

def binarySearchColumnDec(arr, col, t, b, x): 

 

 while t <= b:

 mid = (t + b) // 2

 

 if arr[mid][col] == x: 

 return mid 

 elif arr[mid][col] < x: 

 b = mid - 1

 else:

 t = mid + 1

 

 return -1

 

# Function to find the position of the number x 

def spiralBinary(arr, x): 

 

 # Finding the ring 

 f1 = findRing(arr, x) 

 

 # To store row and column 

 r, c = None, None

 

 if f1 == -1: 

 print("-1") 

 return

 

 # Edge case if n is odd 

 if n % 2 == 1 and f1 == (n + 1) // 2
- 1: 

 print(f1, f1) 

 return

 

 # Check which of the 4 sides, 

 # the number x lies in 

 if x < arr[f1][n - f1 - 1]: 

 c = binarySearchRowInc(arr, f1, f1, 

 n - f1 - 2, x) 

 r = f1 

 

 elif x < arr[n - f1 - 1][n - f1 - 1]: 

 c = n - f1 - 1

 

 r = binarySearchColumnInc(arr, n - f1 - 1, f1, 

 n - f1 - 2, x) 

 

 elif x < arr[n - f1 - 1][f1]: 

 

 c = binarySearchRowDec(arr, n - f1 - 1, f1 + 1, 

 n - f1 - 1, x) 

 r = n - f1 - 1

 

 else:

 

 r = binarySearchColumnDec(arr, f1, f1 + 1, 

 n - f1 - 1, x) 

 c = f1 

 

 # Printing the position 

 if c == -1 or r == -1:

 print("-1") 

 else:

 print("{0} {1}".format(r, c)) 

 

# Driver code 

if __name__ == "__main__": 

 

 n = 4

 arr = [[1, 2, 3, 4], 

 [12, 13, 14, 5], 

 [11, 16, 15, 6], 

 [10, 9, 8, 7]] 

 

 spiralBinary(arr, 7) 

 

# This code is contributed by Rituraj Jain  
  
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

class GFG 

{ 

 

 static int n =4; 

 

// Function to return the ring, 

// the number x belongs to. 

static int findRing(int [,]arr, int x) 

{ 

 // Returns -1 if number x is 

 // smaller than least element of arr 

 if (arr[0,0] > x) 

 return -1; 

 

 // l and r represent the diagonal 

 // elements to search in 

 int l = 0, r = (n + 1) / 2 - 1; 

 

 // Returns -1 if number x is greater 

 // than the largest element of arr 

 if (n % 2 == 1 && arr[r,r] < x) 

 return -1; 

 if (n % 2 == 0 && arr[r + 1,r] < x) 

 return -1; 

 

 while (l < r) 

 { 

 int mid = (l + r) / 2; 

 if (arr[mid,mid] <= x) 

 if (mid == (n + 1) / 2 - 1

 || arr[mid + 1,mid + 1] > x) 

 return mid; 

 else

 l = mid + 1; 

 else

 r = mid - 1; 

 } 

 return r; 

} 

 

// Function to perform binary search 

// on an array sorted in increasing order 

// l and r represent the left and right 

// index of the row to be searched 

static int binarySearchRowInc(int [,]arr, int row, 

 int l, int r, int x) 

{ 

 while (l <= r) 

 { 

 int mid = (l + r) / 2; 

 

 if (arr[row,mid] == x) 

 return mid; 

 

 if (arr[row,mid] < x) 

 l = mid + 1; 

 else

 r = mid - 1; 

 } 

 return -1; 

} 

 

// Function to perform binary search on 

// a particlar column of the 2D array 

// t and b represent top and 

// bottom rows 

static int binarySearchColumnInc(int [,]arr, int col, 

 int t, int b, int x) 

{ 

 while (t <= b) 

 { 

 int mid = (t + b) / 2; 

 

 if (arr[mid,col] == x) 

 return mid; 

 

 if (arr[mid,col] < x) 

 t = mid + 1; 

 else

 b = mid - 1; 

 } 

 return -1; 

} 

 

// Function to perform binary search on 

// an array sorted in decreasing order 

static int binarySearchRowDec(int [,]arr, int row, 

 int l, int r, int x) 

{ 

 while (l <= r) { 

 

 int mid = (l + r) / 2; 

 

 if (arr[row,mid] == x) 

 return mid; 

 

 if (arr[row,mid] < x) 

 r = mid - 1; 

 else

 l = mid + 1; 

 } 

 return -1; 

} 

 

// Function to perform binary search on a 

// particlar column of the 2D array 

static int binarySearchColumnDec(int [,]arr, int col, 

 int t, int b, int x) 

{ 

 while (t <= b) 

 { 

 int mid = (t + b) / 2; 

 

 if (arr[mid,col] == x) 

 return mid; 

 

 if (arr[mid,col] < x) 

 b = mid - 1; 

 else

 t = mid + 1; 

 } 

 return -1; 

} 

 

// Function to find the position of the number x 

static void spiralBinary(int [,]arr, int x) 

{ 

 

 // Finding the ring 

 int f1 = findRing(arr, x); 

 

 // To store row and column 

 int r, c; 

 

 if (f1 == -1) 

 { 

 Console.Write("-1"); 

 return; 

 } 

 

 // Edge case if n is odd 

 if (n % 2 == 1 && f1 == (n + 1) / 2 - 1) 

 { 

 Console.WriteLine(f1+" "+f1); 

 return; 

 } 

 

 // Check which of the 4 sides, the number x 

 // lies in 

 if (x < arr[f1,n - f1 - 1]) 

 { 

 c = binarySearchRowInc(arr, f1, f1, 

 n - f1 - 2, x); 

 r = f1; 

 } 

 else if (x < arr[n - f1 - 1,n - f1 - 1]) 

 { 

 c = n - f1 - 1; 

 

 r = binarySearchColumnInc(arr, n - f1 - 1, f1, 

 n - f1 - 2, x); 

 } 

 else if (x < arr[n - f1 - 1,f1]) 

 { 

 c = binarySearchRowDec(arr, n - f1 - 1, f1 + 1, 

 n - f1 - 1, x); 

 r = n - f1 - 1; 

 } 

 else

 { 

 r = binarySearchColumnDec(arr, f1, f1 + 1, 

 n - f1 - 1, x); 

 c = f1; 

 } 

 

 // Printing the position 

 if (c == -1 || r == -1) 

 Console.Write("-1"); 

 else

 Console.Write(r+" "+c); 

 

 return; 

} 

 

// Driver code 

public static void Main(String []args) 

{ 

 int [,]arr = { { 1, 2, 3, 4 }, 

 { 12, 13, 14, 5 }, 

 { 11, 16, 15, 6 }, 

 { 10, 9, 8, 7 } }; 

 

 spiralBinary(arr, 7); 

} 

} 

 

// This code is contributed by Arnab Kundu  
  
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

// PHP implementation of the above approach

$n = 4;

 

// Function to return the ring, the number x

// belongs to.

function findRing($arr, $x)

{

 global $n;

 

 // Returns -1 if number x is smaller than

 // least element of arr

 if ($arr[0][0] > $x)

 return -1;

 

 // l and r represent the diagonal

 // elements to search in

 $l = 0;

 $r = (int)(($n + 1) / 2 - 1);

 

 // Returns -1 if number x is greater

 // than the largest element of arr

 if ($n % 2 == 1 && $arr[$r][$r] < $x)

 return -1;

 if ($n % 2 == 0 && $arr[$r + 1][$r] < $x)

 return -1;

 

 while ($l < $r) 

 {

 $mid = (int)(($l + $r) / 2);

 if ($arr[$mid][$mid] <= $x)

 if ($mid == (int)(($n + 1) / 2 - 1) || 

 $arr[$mid + 1][$mid + 1] > $x)

 return $mid;

 else

 $l = $mid + 1;

 else

 $r = $mid - 1;

 }

 

 return $r;

}

 

// Function to perform binary search 

// on an array sorted in increasing order

// l and r represent the left and right 

// index of the row to be searched

function binarySearchRowInc($arr, $row, 

 $l, $r, $x)

{

 while ($l <= $r)

 {

 $mid = (int)(($l + $r) / 2);

 

 if ($arr[$row][$mid] == $x)

 return $mid;

 

 if ($arr[$row][$mid] < $x)

 $l = $mid + 1;

 else

 $r = $mid - 1;

 }

 

 return -1;

}

 

// Function to perform binary search on 

// a particlar column of the 2D array

// t and b represent top and 

// bottom rows

function binarySearchColumnInc($arr, $col,

 $t, $b, $x)

{

 while ($t <= $b) 

 {

 $mid = (int)(($t + b) / 2);

 

 if ($arr[$mid][$col] == $x)

 return $mid;

 

 if ($arr[$mid][$col] < $x)

 $t = $mid + 1;

 else

 $b = $mid - 1;

 }

 

 return -1;

}

 

// Function to perform binary search on 

// an array sorted in decreasing order

function binarySearchRowDec($arr, $row, $l, $r, $x)

{

 while ($l <= $r)

 {

 

 $mid = (int)(($l + $r) / 2);

 

 if ($arr[$row][$mid] == $x)

 return $mid;

 

 if ($arr[$row][$mid] < $x)

 $r = $mid - 1;

 else

 $l = $mid + 1;

 }

 

 return -1;

}

 

// Function to perform binary search on a

// particlar column of the 2D array

function binarySearchColumnDec($arr, $col, 

 $t, $b, $x)

{

 while ($t <= $b) 

 {

 $mid = (int)(($t + $b) / 2);

 

 if ($arr[$mid][$col] == $x)

 return $mid;

 

 if ($arr[$mid][$col] < $x)

 $b = $mid - 1;

 else

 $t = $mid + 1;

 }

 

 return -1;

}

 

// Function to find the position of the number x

function spiralBinary($arr, $x)

{

 global $n;

 

 // Finding the ring

 $f1 = findRing($arr, $x);

 

 // To store row and column

 $r = -1;

 $c = -1;

 

 if ($f1 == -1) 

 {

 echo "-1";

 return;

 }

 

 // Edge case if n is odd

 if ($n % 2 == 1 && 

 $f1 == (int)(($n + 1) / 2 - 1)) 

 {

 echo $f1 . " " . $f1 . "\n";

 return;

 }

 

 // Check which of the 4 sides, the number x

 // lies in

 if ($x < $arr[$f1][$n - $f1 - 1]) 

 {

 $c = binarySearchRowInc($arr, $f1, $f1,

 $n - $f1 - 2, $x);

 $r = $f1;

 }

 else if ($x < $arr[$n - $f1 - 1][$n - $f1 -
1])

 {

 $c = $n - $f1 - 1;

 

 $r = binarySearchColumnInc($arr, $n - $f1 - 1, 

 $f1, $n - $f1 - 2, $x);

 }

 else if ($x < $arr[$n - $f1 - 1][$f1])

 {

 

 $c = binarySearchRowDec($arr, $n - $f1 - 1, 

 $f1 + 1, $n - $f1 - 1, $x);

 $r = $n - $f1 - 1;

 }

 else

 {

 $r = binarySearchColumnDec($arr, $f1, $f1 + 1,

 $n - $f1 - 1, $x);

 $c = $f1;

 }

 

 // Printing the position

 if ($c == -1 || $r == -1)

 echo "-1";

 else

 echo $r . " " . $c;

 

 return;

}

 

// Driver code

$arr = array(array( 1, 2, 3, 4 ),

 array( 12, 13, 14, 5 ),

 array( 11, 16, 15, 6 ),

 array( 10, 9, 8, 7 ));

 

spiralBinary($arr, 7);

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    3 3
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

