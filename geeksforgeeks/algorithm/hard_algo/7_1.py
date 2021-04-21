Merge K sorted arrays | Set 3 ( Using Divide and Conquer Approach )



Giving k sorted arrays, each of size **N** , the task is to merge them into a
single sorted array.  
 **Examples:**  

    
    
    **Input:** arr[][] = {{5, 7, 15, 18},
                       {1, 8, 9, 17},
                       {1, 4, 7, 7}}
    **Output:** {1, 1, 4, 5, 7, 7, 7, 8, 9, 15, 17, 18}
    
    **Input:** arr[][] = {{3, 2, 1}
                       {6, 5, 4}}
    **Output:**  {1, 2, 3, 4, 5, 6}

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Prerequisite** : Merge Sort  
 ** _Simple Approach:_** A simple solution is to append all the arrays one
after another and sort them.  

## CPP14

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to merge K

// sorted arrays

#include <bits/stdc++.h>

using namespace std;

#define N 4

// Merge and sort k arrays

void merge_and_sort(

 int* output, int arr[][N],

 int n, int k)

{

 // Put the elments in sorted array.

 for (int i = 0; i < k; i++) {

 for (int j = 0; j < n; j++) {

 output[i * n + j] = arr[i][j];

 }

 }

 // Sort the output array

 sort(output, output + n * k);

}

// Driver Function

int main()

{

 // Input 2D-array

 int arr[][N] = { { 5, 7, 15, 18 },

 { 1, 8, 9, 17 },

 { 1, 4, 7, 7 } };

 int n = N;

 // Number of arrays

 int k = sizeof(arr) / sizeof(arr[0]);

 // Output array

 int* output = new int[n * k];

 merge_and_sort(output, arr, n, k);

 // Print merged array

 for (int i = 0; i < n * k; i++)

 cout << output[i] << " ";

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

// Java program to merge K

// sorted arrays

import java.util.*;

class GFG

{

 static int N = 4; 

 

 // Merge and sort k arrays

 static void merge_and_sort(int output[], int arr[][],

 int n, int k)

 {

 // Put the elments in sorted array.

 for (int i = 0; i < k; i++)

 {

 for (int j = 0; j < n; j++)

 {

 output[i * n + j] = arr[i][j];

 }

 }

 

 // Sort the output array

 Arrays.sort(output);

 }

 // Driver code

 public static void main(String[] args)

 {

 

 // Input 2D-array

 int arr[][] = { { 5, 7, 15, 18 },

 { 1, 8, 9, 17 },

 { 1, 4, 7, 7 } };

 int n = N;

 

 // Number of arrays

 int k = arr.length;

 

 // Output array

 int output[] = new int[n * k]; 

 merge_and_sort(output, arr, n, k);

 

 // Print merged array

 for (int i = 0; i < n * k; i++)

 System.out.print(output[i] + " ");

 }

}

// This code is contributed by divyesh072019  
  
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

# Python3 program to merge K

# sorted arrays

N = 4

# Merge and sort k arrays

def merge_and_sort(output, arr, n, k):

 # Put the elments in sorted array.

 for i in range(k):

 for j in range(n):

 output[i * n + j] = arr[i][j];

 # Sort the output array

 output.sort()

# Driver Function

if __name__=='__main__':

 # Input 2D-array

 arr = [ [ 5, 7, 15, 18 ],

 [ 1, 8, 9, 17 ],

 [ 1, 4, 7, 7 ] ];

 n = N;

 # Number of arrays

 k = len(arr)

 # Output array

 output = [0 for i in range(n * k)]

 merge_and_sort(output, arr, n, k);

 # Print merged array

 for i in range(n * k):

 print(output[i], end = ' ')

 

# This code is contributed by rutvik_56.  
  
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

// C# program to merge K

// sorted arrays

using System;

class GFG

{

 

 static int N = 4; 

 

 // Merge and sort k arrays

 static void merge_and_sort(int[] output, int[,] arr,

 int n, int k)

 {

 // Put the elments in sorted array.

 for (int i = 0; i < k; i++)

 {

 for (int j = 0; j < n; j++)

 {

 output[i * n + j] = arr[i,j];

 }

 }

 

 // Sort the output array

 Array.Sort(output);

 }

 

 // Driver code

 static void Main()

 {

 

 // Input 2D-array

 int[,] arr = { { 5, 7, 15, 18 },

 { 1, 8, 9, 17 },

 { 1, 4, 7, 7 } };

 int n = N;

 

 // Number of arrays

 int k = arr.GetLength(0);

 

 // Output array

 int[] output = new int[n * k]; 

 merge_and_sort(output, arr, n, k);

 

 // Print merged array

 for (int i = 0; i < n * k; i++)

 Console.Write(output[i] + " ");

 }

}

// This code is contributed by divyeshrabadiya07  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

 // Javascript program to merge K

 // sorted arrays

 

 let N = 4;

 

 // Merge and sort k arrays

 function merge_and_sort(output, arr, n, k)

 {

 // Put the elments in sorted array.

 for (let i = 0; i < k; i++)

 {

 for (let j = 0; j < n; j++)

 {

 output[i * n + j] = arr[i][j];

 }

 }

 

 // Sort the output array

 output.sort(function(a, b){return a - b});

 }

 

 // Input 2D-array

 let arr = [ [ 5, 7, 15, 18 ],

 [ 1, 8, 9, 17 ],

 [ 1, 4, 7, 7 ] ];

 let n = N;

 

 // Number of arrays

 let k = 3;

 

 // Output array

 let output = new Array(n * k); 

 merge_and_sort(output, arr, n, k);

 

 // Print merged array

 for (let i = 0; i < n * k; i++)

 document.write(output[i] + " ");

 

 // This code is contributed by mukesh07.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    1 1 4 5 7 7 7 8 9 15 17 18

**Complexity Analysis:**  

  

  

  * **Time Complexity:** O(N*k*log(N*k)).   
The size of all elements is n*k so the time complexity is O(N*k * log(N*k))

  *  **Space Complexity:** O(N*k).   
To store the output array O(N*k) space is required.

 ** _Efficient Solution_** _:_  
**Approach:** The idea becomes clear once we start looking at the **k** arrays
as the intermediate state of the merge sort algorithm.  
Since there are k arrays that are already sorted, merge the k arrays. Create a
recursive function which will take k arrays and divide them into two parts and
call the function recursively with each half. The base cases are when the
value of k is less than 3.  
See this article to merge two arrays in O(n) time.  
 **Algorithm:**  

  1. Initialize the output array with the size **N*k**.
  2. Call the function divide. Let ![l          ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-8231df027087f7933adcad511685ebc9_l3.png)and ![r          ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-57f69c577eb5d4a31b39f01ddccef140_l3.png)represent the range of arrays that are to be merged and thus vary between **0 to k-1**.
  3. At each step, we call the left and right half of the range recursively so that, they will be sorted and stored in the output array.
  4. After that, we merge the left and right half. For merging, we need to determine the range of indexes for the left and right halves in the output array. We can easily find that. 
    1. **Left part** will start from the index **l * n** of the output array.
    2. Similarly, **right part** will start from the index **((l + r) / 2 + 1) * n** of the output array.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to merge K

// sorted arrays

#include <iostream>

#define n 4

using namespace std;

// Function to perform merge operation

void merge(int l, int r, int* output)

{

 // to store the starting point

 // of left and right array

 int l_in = l * n, r_in

 = ((l + r) / 2 + 1) * n;

 // To store the size of left and

 // right array

 int l_c = ((l + r) / 2 - l + 1) * n;

 int r_c = (r - (l + r) / 2) * n;

 // array to temporarily store left

 // and right array

 int l_arr[l_c], r_arr[r_c];

 // storing data in left array

 for (int i = 0; i < l_c; i++)

 l_arr[i] = output[l_in + i];

 // storing data in right array

 for (int i = 0; i < r_c; i++)

 r_arr[i] = output[r_in + i];

 // to store the current index of

 // temporary left and right array

 int l_curr = 0, r_curr = 0;

 // to store the current index

 // for output array

 int in = l_in;

 // two pointer merge for

 // two sorted arrays

 while (

 l_curr + r_curr < l_c + r_c) {

 if (

 r_curr == r_c

 || (l_curr != l_c

 && l_arr[l_curr] < r_arr[r_curr]))

 output[in]

 = l_arr[l_curr],

 l_curr++, in++;

 else

 output[in]

 = r_arr[r_curr],

 r_curr++, in++;

 }

}

// Code to drive merge-sort and

// create recursion tree

void divide(int l, int r, int* output,

 int arr[][n])

{

 if (l == r) {

 /* base step to initialize the output

 array before performing merge

 operation */

 for (int i = 0; i < n; i++)

 output[l * n + i] = arr[l][i];

 return;

 }

 // To sort left half

 divide(l, (l + r) / 2,

 output, arr);

 // To sort right half

 divide((l + r) / 2 + 1, r,

 output, arr);

 // Merge the left and right half

 merge(l, r, output);

}

// Driver Function

int main()

{

 // input 2D-array

 int arr[][n] = { { 5, 7, 15, 18 },

 { 1, 8, 9, 17 },

 { 1, 4, 7, 7 } };

 // Number of arrays

 int k = sizeof(arr) / sizeof(arr[0]);

 // Output array

 int* output = new int[n * k];

 divide(0, k - 1, output, arr);

 // Print merged array

 for (int i = 0; i < n * k; i++)

 cout << output[i] << " ";

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

// Java program to merge

// K sorted arrays

import java.util.*;

class GFG {

 static int n = 4;

 // Function to perform

 // merge operation

 static void merge(

 int l, int r, int[] output)

 {

 // To store the starting point

 // of left and right array

 int l_in = l * n, r_in

 = ((l + r) / 2 + 1) * n;

 // to store the size of left and

 // right array

 int l_c = ((l + r) / 2 - l + 1) * n;

 int r_c = (r - (l + r) / 2) * n;

 // array to temporarily store left

 // and right array

 int l_arr[] = new int[l_c],

 r_arr[] = new int[r_c];

 // storing data in left array

 for (int i = 0; i < l_c; i++)

 l_arr[i] = output[l_in + i];

 // storing data in right array

 for (int i = 0; i < r_c; i++)

 r_arr[i] = output[r_in + i];

 // to store the current index of

 // temporary left and right array

 int l_curr = 0, r_curr = 0;

 // to store the current index

 // for output array

 int in = l_in;

 // two pointer merge for two sorted arrays

 while (l_curr + r_curr < l_c + r_c) {

 if (

 r_curr == r_c

 || (l_curr != l_c

 && l_arr[l_curr] < r_arr[r_curr])) {

 output[in] = l_arr[l_curr];

 l_curr++;

 in++;

 }

 else {

 output[in] = r_arr[r_curr];

 r_curr++;

 in++;

 }

 }

 }

 // Code to drive merge-sort and

 // create recursion tree

 static void divide(int l, int r, int[] output,

 int arr[][])

 {

 if (l == r) {

 /* base step to initialize the output

 array before performing merge

 operation */

 for (int i = 0; i < n; i++)

 output[l * n + i] = arr[l][i];

 return;

 }

 // to sort left half

 divide(l, (l + r) / 2, output, arr);

 // to sort right half

 divide((l + r) / 2 + 1, r, output, arr);

 // merge the left and right half

 merge(l, r, output);

 }

 // Driver Code

 public static void main(String[] args)

 {

 // input 2D-array

 int arr[][] = { { 5, 7, 15, 18 },

 { 1, 8, 9, 17 },

 { 1, 4, 7, 7 } };

 // Number of arrays

 int k = arr.length;

 // Output array

 int[] output = new int[n * k];

 divide(0, k - 1, output, arr);

 // Print merged array

 for (int i = 0; i < n * k; i++)

 System.out.print(output[i] + " ");

 }

}

/* This code contributed by PrinciRaj1992 */  
  
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

# Python3 program to merge K sorted arrays

n = 4 ;

# Function to perform merge operation

def merge(l, r, output) :

 

 # to store the starting point of

 # left and right array

 l_in = l * n ;

 r_in = ((l + r) // 2 + 1) * n;

 # to store the size of left and

 # right array

 l_c = ((l + r) // 2 - l + 1) * n;

 r_c = (r - (l + r) // 2) * n;

 # array to temporarily store left

 # and right array

 l_arr = [0] * l_c; r_arr = [0] * r_c;

 # storing data in left array

 for i in range(l_c) :

 l_arr[i] = output[l_in + i];

 # storing data in right array

 for i in range(r_c) :

 r_arr[i] = output[r_in + i];

 # to store the current index of

 # temporary left and right array

 l_curr = 0 ; r_curr = 0;

 # to store the current index

 # for output array

 in1 = l_in;

 # two pointer merge for two sorted arrays

 while (l_curr + r_curr < l_c + r_c) :

 if (r_curr == r_c or (l_curr != l_c and

 l_arr[l_curr] < r_arr[r_curr])) :

 output[in1] = l_arr[l_curr];

 l_curr += 1; in1 += 1;

 else :

 output[in1] = r_arr[r_curr];

 r_curr += 1; in1 += 1;

# Code to drive merge-sort and

# create recursion tree

def divide(l, r, output, arr) :

 

 if (l == r) :

 # base step to initialize the output

 # array before performing merge

 # operation

 for i in range(n) :

 output[l * n + i] = arr[l][i];

 return;

 

 # to sort left half

 divide(l, (l + r) // 2, output, arr);

 # to sort right half

 divide((l + r) // 2 + 1, r, output, arr);

 # merge the left and right half

 merge(l, r, output);

# Driver code

if __name__ == "__main__" :

 # input 2D-array

 arr = [[ 5, 7, 15, 18 ],

 [ 1, 8, 9, 17 ],

 [ 1, 4, 7, 7 ]];

 

 # Number of arrays

 k = len(arr);

 

 # Output array

 output = [0] * (n * k);

 

 divide(0, k - 1, output, arr);

 

 # Print merged array

 for i in range(n * k) :

 print(output[i], end = " ");

# This code is contributed by Ryuga  
  
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

// C# program to merge K sorted arrays

using System;

class GFG {

 static int n = 4;

 // Function to perform merge operation

 static void merge(int l, int r, int[] output)

 {

 // to store the starting point of left

 // and right array

 int l_in = l * n, r_in = ((l + r) / 2 + 1) * n;

 // to store the size of left and

 // right array

 int l_c = ((l + r) / 2 - l + 1) * n;

 int r_c = (r - (l + r) / 2) * n;

 // array to temporarily store left

 // and right array

 int[] l_arr = new int[l_c];

 int[] r_arr = new int[r_c];

 // storing data in left array

 for (int i = 0; i < l_c; i++)

 l_arr[i] = output[l_in + i];

 // storing data in right array

 for (int i = 0; i < r_c; i++)

 r_arr[i] = output[r_in + i];

 // to store the current index of

 // temporary left and right array

 int l_curr = 0, r_curr = 0;

 // to store the current index

 // for output array

 int index = l_in;

 // two pointer merge for two sorted arrays

 while (l_curr + r_curr < l_c + r_c) {

 if (r_curr == r_c || (l_curr != l_c && l_arr[l_curr] < r_arr[r_curr]))
{

 output[index] = l_arr[l_curr];

 l_curr++;

 index++;

 }

 else {

 output[index] = r_arr[r_curr];

 r_curr++;

 index++;

 }

 }

 }

 // Code to drive merge-sort and

 // create recursion tree

 static void divide(int l, int r, int[] output,

 int[, ] arr)

 {

 if (l == r) {

 /* base step to initialize the output

 array before performing merge

 operation */

 for (int i = 0; i < n; i++)

 output[l * n + i] = arr[l, i];

 return;

 }

 // to sort left half

 divide(l, (l + r) / 2, output, arr);

 // to sort right half

 divide((l + r) / 2 + 1, r, output, arr);

 // merge the left and right half

 merge(l, r, output);

 }

 // Driver Code

 public static void Main(String[] args)

 {

 // input 2D-array

 int[, ] arr = { { 5, 7, 15, 18 },

 { 1, 8, 9, 17 },

 { 1, 4, 7, 7 } };

 // Number of arrays

 int k = arr.GetLength(0);

 // Output array

 int[] output = new int[n * k];

 divide(0, k - 1, output, arr);

 // Print merged array

 for (int i = 0; i < n * k; i++)

 Console.Write(output[i] + " ");

 }

}

// This code has been contributed by 29AjayKumar  
  
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

// PHP program to merge K sorted arrays

$n = 4;

// Function to perform merge operation

function merge($l, $r, &$output)

{

 global $n;

 

 // to store the starting point of left

 // and right array

 $l_in = $l * $n;

 $r_in = ((int)(($l + $r) / 2) + 1) * $n;

 // to store the size of left and

 // right array

 $l_c = (int)(((($l + $r) / 2) - $l + 1) * $n);

 $r_c = ($r - (int)(($l + $r) / 2)) * $n;

 // array to temporarily store left

 // and right array

 $l_arr = array_fill(0, $l_c, 0);

 $r_arr = array_fill(0, $r_c, 0);

 // storing data in left array

 for ($i = 0; $i < $l_c; $i++)

 $l_arr[$i] = $output[$l_in + $i];

 // storing data in right array

 for ($i = 0; $i < $r_c; $i++)

 $r_arr[$i] = $output[$r_in + $i];

 // to store the current index of

 // temporary left and right array

 $l_curr = 0;

 $r_curr = 0;

 // to store the current index

 // for output array

 $in = $l_in;

 // two pointer merge for two sorted arrays

 while ($l_curr + $r_curr < $l_c + $r_c)

 {

 if ($r_curr == $r_c || ($l_curr != $l_c &&

 $l_arr[$l_curr] < $r_arr[$r_curr]))

 {

 $output[$in] = $l_arr[$l_curr];

 $l_curr++; $in++;

 }

 else

 {

 $output[$in] = $r_arr[$r_curr];

 $r_curr++; $in++;

 }

 }

}

// Code to drive merge-sort and

// create recursion tree

function divide($l, $r, &$output, $arr)

{

 global $n;

 if ($l == $r)

 {

 /* base step to initialize the output

 array before performing merge

 operation */

 for ($i = 0; $i < $n; $i++)

 $output[$l * $n + $i] = $arr[$l][$i];

 return;

 }

 // to sort left half

 divide($l, (int)(($l + $r) / 2), $output, $arr);

 // to sort right half

 divide((int)(($l + $r) / 2) + 1, $r, $output, $arr);

 // merge the left and right half

 merge($l, $r, $output);

}

// Driver Code

// input 2D-array

$arr = array(array( 5, 7, 15, 18 ),

 array( 1, 8, 9, 17 ),

 array( 1, 4, 7, 7 ));

// Number of arrays

$k = count($arr);

// Output array

$output = array_fill(0, $n * $k, 0);

divide(0, $k - 1, $output, $arr);

// Print merged array

for ($i = 0; $i < $n * $k; $i++)

 print($output[$i] . " ");

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    1 1 4 5 7 7 7 8 9 15 17 18

**Complexity Analysis:**  

  * **Time Complexity:** O(N*k*log(k)).   
In each level the array of size N*k is traversed once, and the number of
levels are log(k).

  *  **Space Complexity:** O(N*k).   
To store the output array O(N*k) space is required.

We can also solve this problem by using min-heap.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

