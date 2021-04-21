Count Negative Numbers in a Column-Wise and Row-Wise Sorted Matrix



Find the number of negative numbers in a column-wise / row-wise sorted matrix
M[][]. Suppose M has n rows and m columns.  
Example:

    
    
    Input:  M =  [-3, -2, -1,  1]
                 [-2,  2,  3,  4]
                 [4,   5,  7,  8]
    Output : 4
    We have 4 negative numbers in this matrix

 **We strongly recommend you to minimize your browser and try this yourself
first.**  
 **Naive Solution**  
Here’s a naive, non-optimal solution.  
We start from the top left corner and count the number of negative numbers one
by one, from left to right and top to bottom.  
With the given example:

    
    
    [-3, -2, -1,  1]
    [-2,  2,  3,  4]
    [4,   5,  7,  8]
    
    Evaluation process
    
    [?,  ?,  ?,  1]
    [?,  2,  3,  4]
    [4,  5,  7,  8]

Below is the implementation of above idea:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP implementation of Naive method

// to count of negative numbers in

// M[n][m]

#include <bits/stdc++.h>

using namespace std;

int countNegative(int M[][4], int n, int m)

{

 int count = 0;

 // Follow the path shown using

 // arrows above

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < m; j++) {

 if (M[i][j] < 0)

 count += 1;

 // no more negative numbers

 // in this row

 else

 break;

 }

 }

 return count;

}

// Driver program to test above functions

int main()

{

 int M[3][4] = { { -3, -2, -1, 1 },

 { -2, 2, 3, 4 },

 { 4, 5, 7, 8 } };

 cout << countNegative(M, 3, 4);

 return 0;

}

// This code is contributed by Niteesh Kumar  
  
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

// Java implementation of Naive method

// to count of negative numbers in

// M[n][m]

import java.util.*;

import java.lang.*;

import java.io.*;

class GFG {

 static int countNegative(int M[][], int n,

 int m)

 {

 int count = 0;

 // Follow the path shown using

 // arrows above

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < m; j++) {

 if (M[i][j] < 0)

 count += 1;

 // no more negative numbers

 // in this row

 else

 break;

 }

 }

 return count;

 }

 // Driver program to test above functions

 public static void main(String[] args)

 {

 int M[][] = { { -3, -2, -1, 1 },

 { -2, 2, 3, 4 },

 { 4, 5, 7, 8 } };

 System.out.println(countNegative(M, 3, 4));

 }

}

// This code is contributed by Chhavi  
  
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

# Python implementation of Naive method to count of

# negative numbers in M[n][m]

def countNegative(M, n, m):

 count = 0

 # Follow the path shown using arrows above

 for i in range(n):

 for j in range(m):

 if M[i][j] < 0:

 count += 1

 else:

 # no more negative numbers in this row

 break

 return count

# Driver code

M = [

 [-3, -2, -1, 1],

 [-2, 2, 3, 4],

 [ 4, 5, 7, 8]

 ]

print(countNegative(M, 3, 4))  
  
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

// C# implementation of Naive method

// to count of negative numbers in

// M[n][m]

using System;

class GFG {

 // Function to count

 // negative number

 static int countNegative(int[, ] M, int n,

 int m)

 {

 int count = 0;

 // Follow the path shown

 // using arrows above

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < m; j++) {

 if (M[i, j] < 0)

 count += 1;

 // no more negative numbers

 // in this row

 else

 break;

 }

 }

 return count;

 }

 // Driver Code

 public static void Main()

 {

 int[, ] M = { { -3, -2, -1, 1 },

 { -2, 2, 3, 4 },

 { 4, 5, 7, 8 } };

 Console.WriteLine(countNegative(M, 3, 4));

 }

}

// This code is contributed by Sam007  
  
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

// PHP implementation of Naive method

// to count of negative numbers in

// M[n][m]

function countNegative($M, $n, $m)

{

 $count = 0;

 // Follow the path shown using

 // arrows above

 for( $i = 0; $i < $n; $i++)

 {

 for( $j = 0; $j < $m; $j++)

 {

 if( $M[$i][$j] < 0 )

 $count += 1;

 

 // no more negative numbers

 // in this row

 else

 break;

 }

 }

 return $count;

}

 // Driver Code

 $M = array(array(-3, -2, -1, 1),

 array(-2, 2, 3, 4),

 array(4, 5, 7, 8));

 

 echo countNegative($M, 3, 4);

 

// This code is contributed by anuj_67.

?>  
  
---  
  
 __

 __

 **Output :**

    
    
    4

In this approach we are traversing through the all the elements and therefore,
in the worst case scenario (when all numbers are negative in the matrix), this
takes O(n * m) time.  
 **Optimal Solution**  
Here’s a more efficient solution:

  

  

  1. We start from the top right corner and find the position of the last negative number in the first row.
  2. Using this information, we find the position of the last negative number in the second row.
  3. We keep repeating this process until we either run out of negative numbers or we get to the last row.

    
    
    With the given example:
    [-3, -2, -1,  1]
    [-2,  2,  3,  4]
    [4,   5,  7,  8]
    
    Here's the idea:
    [-3, -2,  ?,  ?] -> Found 3 negative numbers in this row
    [ ?,  ?,  ?,  4] -> Found 1 negative number in this row
    [ ?,  5,  7,  8] -> No negative numbers in this row 

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP implementation of Efficient

// method to count of negative numbers

// in M[n][m]

#include <bits/stdc++.h>

using namespace std;

int countNegative(int M[][4], int n, int m)

{

 // initialize result

 int count = 0;

 // Start with top right corner

 int i = 0;

 int j = m - 1;

 // Follow the path shown using

 // arrows above

 while (j >= 0 && i < n) {

 if (M[i][j] < 0) {

 // j is the index of the

 // last negative number

 // in this row. So there

 // must be ( j+1 )

 count += j + 1;

 // negative numbers in

 // this row.

 i += 1;

 }

 // move to the left and see

 // if we can find a negative

 // number there

 else

 j -= 1;

 }

 return count;

}

// Driver program to test above functions

int main()

{

 int M[3][4] = { { -3, -2, -1, 1 },

 { -2, 2, 3, 4 },

 { 4, 5, 7, 8 } };

 cout << countNegative(M, 3, 4);

 return 0;

}

// This code is contributed by Niteesh Kumar  
  
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

// Java implementation of Efficient

// method to count of negative numbers

// in M[n][m]

import java.util.*;

import java.lang.*;

import java.io.*;

class GFG {

 static int countNegative(int M[][], int n,

 int m)

 {

 // initialize result

 int count = 0;

 // Start with top right corner

 int i = 0;

 int j = m - 1;

 // Follow the path shown using

 // arrows above

 while (j >= 0 && i < n) {

 if (M[i][j] < 0) {

 // j is the index of the

 // last negative number

 // in this row. So there

 // must be ( j+1 )

 count += j + 1;

 // negative numbers in

 // this row.

 i += 1;

 }

 // move to the left and see

 // if we can find a negative

 // number there

 else

 j -= 1;

 }

 return count;

 }

 // Driver program to test above functions

 public static void main(String[] args)

 {

 int M[][] = { { -3, -2, -1, 1 },

 { -2, 2, 3, 4 },

 { 4, 5, 7, 8 } };

 System.out.println(countNegative(M, 3, 4));

 }

}

// This code is contributed by Chhavi  
  
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

# Python implementation of Efficient method to count of

# negative numbers in M[n][m]

def countNegative(M, n, m):

 count = 0 # initialize result

 # Start with top right corner

 i = 0

 j = m - 1

 # Follow the path shown using arrows above

 while j >= 0 and i < n:

 if M[i][j] < 0:

 # j is the index of the last negative number

 # in this row. So there must be ( j + 1 )

 count += (j + 1)

 # negative numbers in this row.

 i += 1

 else:

 # move to the left and see if we can

 # find a negative number there

 j -= 1

 return count

# Driver code

M = [

 [-3, -2, -1, 1],

 [-2, 2, 3, 4],

 [4, 5, 7, 8]

 ]

print(countNegative(M, 3, 4))  
  
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

// C# implementation of Efficient

// method to count of negative

// numbers in M[n][m]

using System;

class GFG {

 // Function to count

 // negative number

 static int countNegative(int[, ] M, int n,

 int m)

 {

 // initialize result

 int count = 0;

 // Start with top right corner

 int i = 0;

 int j = m - 1;

 // Follow the path shown

 // using arrows above

 while (j >= 0 && i < n) {

 if (M[i, j] < 0) {

 // j is the index of the

 // last negative number

 // in this row. So there

 // must be ( j + 1 )

 count += j + 1;

 // negative numbers in

 // this row.

 i += 1;

 }

 // move to the left and see

 // if we can find a negative

 // number there

 else

 j -= 1;

 }

 return count;

 }

 // Driver Code

 public static void Main()

 {

 int[, ] M = { { -3, -2, -1, 1 },

 { -2, 2, 3, 4 },

 { 4, 5, 7, 8 } };

 Console.WriteLine(countNegative(M, 3, 4));

 }

}

// This code is contributed by Sam007  
  
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

// PHP implementation of Efficient

// method to count of negative numbers

// in M[n][m]

function countNegative( $M, $n, $m)

{

 

 // initialize result

 $count = 0;

 // Start with top right corner

 $i = 0;

 $j = $m - 1;

 // Follow the path shown using

 // arrows above

 while( $j >= 0 and $i < $n )

 {

 if( $M[$i][$j] < 0 )

 {

 // j is the index of the

 // last negative number

 // in this row. So there

 // must be ( j+1 )

 $count += $j + 1;

 // negative numbers in

 // this row.

 $i += 1;

 }

 

 // move to the left and see

 // if we can find a negative

 // number there

 else

 $j -= 1;

 }

 return $count;

}

 // Driver Code

 $M = array(array(-3, -2, -1, 1),

 array(-2, 2, 3, 4),

 array(4, 5, 7, 8));

 

 echo countNegative($M, 3, 4);

 

 return 0;

// This code is contributed by anuj_67.

?>  
  
---  
  
 __

 __

 **Output :**

    
    
    4

With this solution, we can now solve this problem in O(n + m) time.  
 **More Optimal Solution**  
Here’s a more efficient solution using binary search instead of linear search:

  1. We start from the first row and find the position of the last negative number in the first row using binary search.
  2. Using this information, we find the position of the last negative number in the second row by running binary search only until the position of the last negative number in the row above.
  3. We keep repeating this process until we either run out of negative numbers or we get to the last row.

    
    
    With the given example:
    [-3, -2, -1,  1]
    [-2,  2,  3,  4]
    [4,   5,  7,  8]
    
    Here's the idea:
    1. Count is initialized to 0
    2. Binary search on full 1st row returns 2 as the index 
       of last negative integer, and we increase count to 0+(2+1) = 3.
    3. For 2nd row, we run binary search from index 0 to index 2 
       and it returns 0 as the index of last negative integer. 
       We increase the count to 3+(0+1) = 4;
    4. For 3rd row, first element is > 0, so we end the loop here.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of More efficient

// method to count number of negative numbers

// in row-column sorted matrix M[n][m]

#include<bits/stdc++.h>

using namespace std;

// Recursive binary search to get last negative

// value in a row between a start and an end

int getLastNegativeIndex(int array[], int start,

 int end,int n)

{

 // Base case

 if (start == end)

 {

 return start;

 }

 // Get the mid for binary search

 int mid = start + (end - start) / 2;

 // If current element is negative

 if (array[mid] < 0)

 {

 // If it is the rightmost negative

 // element in the current row

 if (mid + 1 < n && array[mid + 1] >= 0)

 {

 return mid;

 }

 // Check in the right half of the array

 return getLastNegativeIndex(array,

 mid + 1, end, n);

 }

 else

 {

 // Check in the left half of the array

 return getLastNegativeIndex(array,

 start, mid - 1, n);

 }

}

// Function to return the count of

// negative numbers in the given matrix

int countNegative(int M[][4], int n, int m)

{

 // Initialize result

 int count = 0;

 // To store the index of the rightmost negative

 // element in the row under consideration

 int nextEnd = m - 1;

 // Iterate over all rows of the matrix

 for (int i = 0; i < n; i++)

 {

 // If the first element of the current row

 // is positive then there will be no negatives

 // in the matrix below or after it

 if (M[i][0] >= 0)

 {

 break;

 }

 // Run binary search only until the index of last

 // negative Integer in the above row

 nextEnd = getLastNegativeIndex(M[i], 0, nextEnd, 4);

 count += nextEnd + 1;

 }

 return count;

}

// Driver code

int main()

{

 int M[][4] = { { -3, -2, -1, 1 },

 { -2, 2, 3, 4 },

 { 4, 5, 7, 8 } };

 int r = 3;

 int c = 4;

 cout << (countNegative(M, r, c));

 return 0;

}

// This code is contributed by Arnab Kundu  
  
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

// Java implementation of More efficient

// method to count number of negative numbers

// in row-column sorted matrix M[n][m]

import java.util.*;

import java.lang.*;

import java.io.*;

class GFG {

 // Recursive binary search to get last negative

 // value in a row between a start and an end

 static int getLastNegativeIndex(int array[], int start, int
end)

 {

 // Base case

 if (start == end) {

 return start;

 }

 // Get the mid for binary search

 int mid = start + (end - start) / 2;

 // If current element is negative

 if (array[mid] < 0) {

 // If it is the rightmost negative

 // element in the current row

 if (mid + 1 < array.length && array[mid + 1] >= 0) {

 return mid;

 }

 // Check in the right half of the array

 return getLastNegativeIndex(array, mid + 1, end);

 }

 else {

 // Check in the left half of the array

 return getLastNegativeIndex(array, start, mid - 1);

 }

 }

 // Function to return the count of

 // negative numbers in the given matrix

 static int countNegative(int M[][], int n, int m)

 {

 // Initialize result

 int count = 0;

 // To store the index of the rightmost negative

 // element in the row under consideration

 int nextEnd = m - 1;

 // Iterate over all rows of the matrix

 for (int i = 0; i < n; i++) {

 // If the first element of the current row

 // is positive then there will be no negatives

 // in the matrix below or after it

 if (M[i][0] >= 0) {

 break;

 }

 // Run binary search only until the index of last

 // negative Integer in the above row

 nextEnd = getLastNegativeIndex(M[i], 0, nextEnd);

 count += nextEnd + 1;

 }

 return count;

 }

 // Driver code

 public static void main(String[] args)

 {

 int M[][] = { { -3, -2, -1, 1 },

 { -2, 2, 3, 4 },

 { 4, 5, 7, 8 } };

 int r = M.length;

 int c = M[0].length;

 System.out.println(countNegative(M, r, c));

 }

}

// This code is contributed by Rahul Jain  
  
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

# Python3 implementation of More efficient

# method to count number of negative numbers

# in row-column sorted matrix M[n][m]

# Recursive binary search to get last negative

# value in a row between a start and an end

def getLastNegativeIndex(array, start, end, n):

 

 # Base case

 if (start == end):

 return start

 

 # Get the mid for binary search

 mid = start + (end - start) // 2

 

 # If current element is negative

 if (array[mid] < 0):

 

 # If it is the rightmost negative

 # element in the current row

 if (mid + 1 < n and array[mid + 1] >= 0):

 

 return mid

 

 # Check in the right half of the array

 return getLastNegativeIndex(array, mid + 1, end, n)

 

 else:

 

 # Check in the left half of the array

 return getLastNegativeIndex(array, start, mid - 1, n)

# Function to return the count of

# negative numbers in the given matrix

def countNegative(M, n, m):

 

 # Initialize result

 count = 0

 

 # To store the index of the rightmost negative

 # element in the row under consideration

 nextEnd = m - 1

 

 # Iterate over all rows of the matrix

 for i in range(n):

 

 # If the first element of the current row

 # is positive then there will be no negatives

 # in the matrix below or after it

 if (M[i][0] >= 0):

 break

 

 # Run binary search only until the index of last

 # negative Integer in the above row

 nextEnd = getLastNegativeIndex(M[i], 0, nextEnd, 4)

 count += nextEnd + 1

 return count

# Driver code

M = [[-3, -2, -1, 1],[-2, 2, 3,
4],[ 4, 5, 7, 8]]

r = 3

c = 4

print(countNegative(M, r, c))

# This code is contributed by shubhamsingh10  
  
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

// C# implementation of More efficient

// method to count number of negative numbers

// in row-column sorted matrix M[n,m]

using System;

using System.Collections.Generic;

class GFG

{

 // Recursive binary search to get last negative

 // value in a row between a start and an end

 static int getLastNegativeIndex(int []array, int start, int
end)

 {

 // Base case

 if (start == end)

 {

 return start;

 }

 // Get the mid for binary search

 int mid = start + (end - start) / 2;

 // If current element is negative

 if (array[mid] < 0)

 {

 // If it is the rightmost negative

 // element in the current row

 if (mid + 1 < array.GetLength(0) && array[mid + 1] >= 0)

 {

 return mid;

 }

 // Check in the right half of the array

 return getLastNegativeIndex(array, mid + 1, end);

 }

 else

 {

 // Check in the left half of the array

 return getLastNegativeIndex(array, start, mid - 1);

 }

 }

 // Function to return the count of

 // negative numbers in the given matrix

 static int countNegative(int [,]M, int n, int m)

 {

 // Initialize result

 int count = 0;

 // To store the index of the rightmost negative

 // element in the row under consideration

 int nextEnd = m - 1;

 // Iterate over all rows of the matrix

 for (int i = 0; i < n; i++)

 {

 // If the first element of the current row

 // is positive then there will be no negatives

 // in the matrix below or after it

 if (M[i, 0] >= 0)

 {

 break;

 }

 // Run binary search only until the index of last

 // negative int in the above row

 nextEnd = getLastNegativeIndex(GetRow(M, i), 0, nextEnd);

 count += nextEnd + 1;

 }

 return count;

 }

 public static int[] GetRow(int[,] matrix, int row)

 {

 var rowLength = matrix.GetLength(1);

 var rowVector = new int[rowLength];

 for (var i = 0; i < rowLength; i++)

 rowVector[i] = matrix[row, i];

 return rowVector;

 }

 

 // Driver code

 public static void Main(String[] args)

 {

 int [,]M = { { -3, -2, -1, 1 },

 { -2, 2, 3, 4 },

 { 4, 5, 7, 8 } };

 int r = M.GetLength(0);

 int c = M.GetLength(1);

 Console.WriteLine(countNegative(M, r, c));

 }

}

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output :**

    
    
    4

Here we have replaced the linear search for last negative number with binary
search. This should improve the worst case scenario keeping the Worst case to
O(nlog(m)).  
This article is contributed by **YK Sugishita** and **Rahul Jain**. If you
like GeeksforGeeks and would like to contribute, you can also write an article
and mail your article to contribute@geeksforgeeks.org. See your article
appearing on the GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

