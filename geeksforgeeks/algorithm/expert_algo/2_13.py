Median of an unsorted array using Quick Select Algorithm



Given an unsorted array **arr[]** of length **N** , the task is to find the
median of of this array.  
**Median** of a sorted array of size N is defined as the middle element when n
is odd and average of middle two elements when n is even.  
 **Examples:**  

> **Input:** arr[] = {12, 3, 5, 7, 4, 19, 26}  
> **Output:** 7  
> Sorted sequence of given array arr[] = {3, 4, 5, 7, 12, 19, 26}  
> Since the number of elements is odd, the median is 4th element in the sorted
> sequence of given array arr[], which is 7  
>  **Input:** arr[] = {12, 3, 5, 7, 4, 26}  
> **Output:** 6  
> Since number of elements are even, median is average of 3rd and 4th element
> in sorted sequence of given array arr[], which means (5 + 7)/2 = 6  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**  

  * Sort the array arr[] in increasing order.
  * If number of elements in **arr[]** is odd, then median is **arr[n/2]**.
  * If the number of elements in **arr[]** is even, median is **average of arr[n/2] and arr[n/2+1]**.

Please refer to this article for implementation of above approach.  
 **Efficient Approach: using** **Randomized QuickSelect**  

  

  

  * Randomly pick pivot element from **arr[]** and the using the **partition step** from the quick sort algorithm arrange all the elements smaller than the pivot on its left and the elements greater than it on its right.
  * If after the previous step, the position of the chosen pivot is the middle of the array then it is the required median of the given array.
  * If the position is before the middle element then repeat the step for the subarray starting from previous starting index and the chosen pivot as the ending index.
  * If the position is after the middle element then repeat the step for the subarray starting from the chosen pivot and ending at the previous ending index.
  * Note that in case of even number of elements, the middle two elements have to be found and their average will be the median of the array.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to find median of

// an array

#include "bits/stdc++.h"

using namespace std;

// Utility function to swapping of element

void swap(int* a, int* b)

{

 int temp = *a;

 *a = *b;

 *b = temp;

}

// Returns the correct position of

// pivot element

int Partition(int arr[], int l, int r)

{

 int lst = arr[r], i = l, j = l;

 while (j < r) {

 if (arr[j] < lst) {

 swap(&arr;[i], &arr;[j]);

 i++;

 }

 j++;

 }

 swap(&arr;[i], &arr;[r]);

 return i;

}

// Picks a random pivot element between

// l and r and partitions arr[l..r]

// around the randomly picked element

// using partition()

int randomPartition(int arr[], int l,

 int r)

{

 int n = r - l + 1;

 int pivot = rand() % n;

 swap(&arr;[l + pivot], &arr;[r]);

 return Partition(arr, l, r);

}

// Utility function to find median

void MedianUtil(int arr[], int l, int r,

 int k, int& a, int& b)

{

 // if l < r

 if (l <= r) {

 // Find the partition index

 int partitionIndex

 = randomPartition(arr, l, r);

 // If partion index = k, then

 // we found the median of odd

 // number element in arr[]

 if (partitionIndex == k) {

 b = arr[partitionIndex];

 if (a != -1)

 return;

 }

 // If index = k - 1, then we get

 // a & b as middle element of

 // arr[]

 else if (partitionIndex == k - 1) {

 a = arr[partitionIndex];

 if (b != -1)

 return;

 }

 // If partitionIndex >= k then

 // find the index in first half

 // of the arr[]

 if (partitionIndex >= k)

 return MedianUtil(arr, l,

 partitionIndex - 1,

 k, a, b);

 // If partitionIndex <= k then

 // find the index in second half

 // of the arr[]

 else

 return MedianUtil(arr,

 partitionIndex + 1,

 r, k, a, b);

 }

 return;

}

// Function to find Median

void findMedian(int arr[], int n)

{

 int ans, a = -1, b = -1;

 // If n is odd

 if (n % 2 == 1) {

 MedianUtil(arr, 0, n - 1,

 n / 2, a, b);

 ans = b;

 }

 // If n is even

 else {

 MedianUtil(arr, 0, n - 1,

 n / 2, a, b);

 ans = (a + b) / 2;

 }

 // Print the Median of arr[]

 cout << "Median = " << ans;

}

// Driver program to test above methods

int main()

{

 int arr[] = { 12, 3, 5, 7, 4, 19, 26 };

 int n = sizeof(arr) / sizeof(arr[0]);

 findMedian(arr, n);

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

// JAVA program to find median of

// an array

class GFG

{

 static int a, b;

 // Utility function to swapping of element

 static int[] swap(int[] arr, int i, int j)

 {

 int temp = arr[i];

 arr[i] = arr[j];

 arr[j] = temp;

 return arr;

 }

 // Returns the correct position of

 // pivot element

 static int Partition(int arr[], int l, int r)

 {

 int lst = arr[r], i = l, j = l;

 while (j < r)

 {

 if (arr[j] < lst)

 {

 arr = swap(arr, i, j);

 i++;

 }

 j++;

 }

 arr = swap(arr, i, r);

 return i;

 }

 // Picks a random pivot element between

 // l and r and partitions arr[l..r]

 // around the randomly picked element

 // using partition()

 static int randomPartition(int arr[], int l, int r)

 {

 int n = r - l + 1;

 int pivot = (int) (Math.random() % n);

 arr = swap(arr, l + pivot, r);

 return Partition(arr, l, r);

 }

 // Utility function to find median

 static int MedianUtil(int arr[], int l, int r, int k)

 {

 // if l < r

 if (l <= r)

 {

 // Find the partition index

 int partitionIndex = randomPartition(arr, l, r);

 // If partion index = k, then

 // we found the median of odd

 // number element in arr[]

 if (partitionIndex == k)

 {

 b = arr[partitionIndex];

 if (a != -1)

 return Integer.MIN_VALUE;

 }

 // If index = k - 1, then we get

 // a & b as middle element of

 // arr[]

 else if (partitionIndex == k - 1)

 {

 a = arr[partitionIndex];

 if (b != -1)

 return Integer.MIN_VALUE;

 }

 // If partitionIndex >= k then

 // find the index in first half

 // of the arr[]

 if (partitionIndex >= k)

 return MedianUtil(arr, l, partitionIndex - 1, k);

 // If partitionIndex <= k then

 // find the index in second half

 // of the arr[]

 else

 return MedianUtil(arr, partitionIndex + 1, r, k);

 }

 return Integer.MIN_VALUE;

 }

 // Function to find Median

 static void findMedian(int arr[], int n)

 {

 int ans;

 a = -1;

 b = -1;

 // If n is odd

 if (n % 2 == 1)

 {

 MedianUtil(arr, 0, n - 1, n / 2);

 ans = b;

 }

 // If n is even

 else

 {

 MedianUtil(arr, 0, n - 1, n / 2);

 ans = (a + b) / 2;

 }

 // Print the Median of arr[]

 System.out.print("Median = " + ans);

 }

 // Driver code

 public static void main(String[] args)

 {

 int arr[] = { 12, 3, 5, 7, 4, 19, 26 };

 int n = arr.length;

 findMedian(arr, n);

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

# Python3 program to find median of

# an array

import random

a, b = None, None;

# Returns the correct position of

# pivot element

def Partition(arr, l, r) :

 lst = arr[r]; i = l; j = l;

 while (j < r) :

 if (arr[j] < lst) :

 arr[i], arr[j] = arr[j],arr[i];

 i += 1;

 

 j += 1;

 arr[i], arr[r] = arr[r],arr[i];

 return i;

# Picks a random pivot element between

# l and r and partitions arr[l..r]

# around the randomly picked element

# using partition()

def randomPartition(arr, l, r) :

 n = r - l + 1;

 pivot = random.randrange(1, 100) % n;

 arr[l + pivot], arr[r] = arr[r], arr[l + pivot];

 return Partition(arr, l, r);

# Utility function to find median

def MedianUtil(arr, l, r,

 k, a1, b1) :

 global a, b;

 

 # if l < r

 if (l <= r) :

 

 # Find the partition index

 partitionIndex = randomPartition(arr, l, r);

 

 # If partion index = k, then

 # we found the median of odd

 # number element in arr[]

 if (partitionIndex == k) :

 b = arr[partitionIndex];

 if (a1 != -1) :

 return;

 

 # If index = k - 1, then we get

 # a & b as middle element of

 # arr[]

 elif (partitionIndex == k - 1) :

 a = arr[partitionIndex];

 if (b1 != -1) :

 return;

 

 # If partitionIndex >= k then

 # find the index in first half

 # of the arr[]

 if (partitionIndex >= k) :

 return MedianUtil(arr, l, partitionIndex - 1, k, a, b);

 

 # If partitionIndex <= k then

 # find the index in second half

 # of the arr[]

 else :

 return MedianUtil(arr, partitionIndex + 1, r, k, a, b);

 

 return;

# Function to find Median

def findMedian(arr, n) :

 global a;

 global b;

 a = -1;

 b = -1;

 

 # If n is odd

 if (n % 2 == 1) :

 MedianUtil(arr, 0, n - 1, n // 2, a, b);

 ans = b;

 

 # If n is even

 else :

 MedianUtil(arr, 0, n - 1, n // 2, a, b);

 ans = (a + b) // 2;

 

 # Print the Median of arr[]

 print("Median = " ,ans);

# Driver code

arr = [ 12, 3, 5, 7, 4, 19, 26 ];

n = len(arr);

findMedian(arr, n);

# This code is contributed by AnkitRai01  
  
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

// C# program to find median of

// an array

using System;

class GFG

{

 static int a, b;

 // Utility function to swapping of element

 static int[] swap(int[] arr, int i, int j)

 {

 int temp = arr[i];

 arr[i] = arr[j];

 arr[j] = temp;

 return arr;

 }

 // Returns the correct position of

 // pivot element

 static int Partition(int []arr, int l, int r)

 {

 int lst = arr[r], i = l, j = l;

 while (j < r)

 {

 if (arr[j] < lst)

 {

 arr = swap(arr, i, j);

 i++;

 }

 j++;

 }

 arr = swap(arr, i, r);

 return i;

 }

 // Picks a random pivot element between

 // l and r and partitions arr[l..r]

 // around the randomly picked element

 // using partition()

 static int randomPartition(int []arr, int l, int r)

 {

 int n = r - l + 1;

 int pivot = (int) (new Random().Next() % n);

 arr = swap(arr, l + pivot, r);

 return Partition(arr, l, r);

 }

 // Utility function to find median

 static int MedianUtil(int []arr, int l, int r, int k)

 {

 // if l < r

 if (l <= r)

 {

 // Find the partition index

 int partitionIndex = randomPartition(arr, l, r);

 // If partion index = k, then

 // we found the median of odd

 // number element in []arr

 if (partitionIndex == k)

 {

 b = arr[partitionIndex];

 if (a != -1)

 return int.MinValue;

 }

 // If index = k - 1, then we get

 // a & b as middle element of

 // []arr

 else if (partitionIndex == k - 1)

 {

 a = arr[partitionIndex];

 if (b != -1)

 return int.MinValue;

 }

 // If partitionIndex >= k then

 // find the index in first half

 // of the []arr

 if (partitionIndex >= k)

 return MedianUtil(arr, l, partitionIndex - 1, k);

 // If partitionIndex <= k then

 // find the index in second half

 // of the []arr

 else

 return MedianUtil(arr, partitionIndex + 1, r, k);

 }

 return int.MinValue;

 }

 // Function to find Median

 static void findMedian(int []arr, int n)

 {

 int ans;

 a = -1;

 b = -1;

 // If n is odd

 if (n % 2 == 1)

 {

 MedianUtil(arr, 0, n - 1, n / 2);

 ans = b;

 }

 // If n is even

 else

 {

 MedianUtil(arr, 0, n - 1, n / 2);

 ans = (a + b) / 2;

 }

 // Print the Median of []arr

 Console.Write("Median = " + ans);

 }

 // Driver code

 public static void Main(String[] args)

 {

 int []arr = { 12, 3, 5, 7, 4, 19, 26 };

 int n = arr.Length;

 findMedian(arr, n);

 }

}

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    Median = 7
    
    

**Time Complexity:**  

  1. Best case analysis: O(1)
  2. Average case analysis: O(N)
  3. Worst case analysis: O(N2)

Wonder how?  
Reference: ByStanfordUniversity  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

