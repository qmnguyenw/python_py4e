Find K elements whose absolute difference with median of array is maximum



Given an array **arr[]** and an integer **K** , the task is to find the K
elements of the array whose absolute difference with median of array is
maximum.  
**Note:** If two elements have equal difference then the maximum element is
taken into consideration.  
 **Examples:**  

> **Input :** arr[] = {1, 2, 3, 4, 5}, k = 3  
> **Output :** {5, 1, 4}  
> **Explanation :**  
> Median m = 3,  
> Difference of each array elements from median,  
> 1 ==> diff(1-3) = 2  
> 2 ==> diff(2-3) = 1  
> 3 ==> diff(3-3) = 0  
> 4 ==> diff(4-3) = 1  
> 5 ==> diff(5-3) = 2  
> First K elements are 5, 1, 4 in this array.  
>  **Input:** arr[] = {1, 2, 3}, K = 2  
> **Output:** {3, 1}  
>
>
> ##

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  

  * Sort the array and find the median of the array
  * Create a difference array to store the difference of each element with the median of the sorted array.
  * Highest difference elements will be the corner elements of the array. Therefore, intialize the two pointers as both the corner elements of the array that is 0 and N – 1.
  * Finally include the elements of the array one by one with the maximum difference with the median.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find first K

// elements whose difference with the 

// median of array is maximum

 

#include <bits/stdc++.h>

using namespace std;

 

// Function for calculating median 

double findMedian(int a[], int n) 

{

 // check for even case 

 if (n % 2 != 0) 

 return (double)a[n/2]; 

 

 return (double)(a[(n-1)/2] + a[n/2])/2.0; 

} 

 

// Function to find the K maximum absolute

// difference with the median of the array

void kStrongest(int arr[], int n, int k)

{

 // Sort the array.

 sort(arr, arr + n);

 

 // Store median

 double median = findMedian(arr, n);

 int diff[n];

 

 // Find and store difference

 for (int i = 0; i < n; i++) {

 diff[i] = abs(median - arr[i]);

 }

 

 int i = 0, j = n - 1;

 while (k > 0) {

 

 // If diff[i] is greater print it

 // Else print diff[j]

 if (diff[i] > diff[j]) {

 cout << arr[i] << " ";

 i++;

 }

 else {

 cout << arr[j] << " ";

 j--;

 }

 k--;

 }

}

 

// Driver Code

int main()

{

 int arr[] = { 1, 2, 3, 4, 5 };

 int k = 3;

 int n = sizeof(arr) / sizeof(arr[0]);

 

 kStrongest(arr, n, k);

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

// Java implementation to find first K

// elements whose difference with the 

// median of array is maximum

import java.util.*;

class GFG{

 

// Function for calculating median 

static double findMedian(int a[], int n) 

{

 // check for even case 

 if (n % 2 != 0) 

 return (double)a[n / 2]; 

 

 return (double)(a[(n - 1) / 2] + 

 a[n / 2]) / 2.0; 

} 

 

// Function to find the K maximum absolute

// difference with the median of the array

static void kStrongest(int arr[], int n, int k)

{

 // Sort the array.

 Arrays.sort(arr);

 

 // Store median

 double median = findMedian(arr, n);

 int []diff = new int[n];

 

 // Find and store difference

 for (int i = 0; i < n; i++) 

 {

 diff[i] = (int)Math.abs(median - arr[i]);

 }

 

 int i = 0, j = n - 1;

 while (k > 0) 

 {

 

 // If diff[i] is greater print it

 // Else print diff[j]

 if (diff[i] > diff[j])

 {

 System.out.print(arr[i] + " ");

 i++;

 }

 else

 {

 System.out.print(arr[j] + " ");

 j--;

 }

 k--;

 }

}

 

// Driver Code

public static void main(String[] args)

{

 int arr[] = { 1, 2, 3, 4, 5 };

 int k = 3;

 int n = arr.length;

 

 kStrongest(arr, n, k);

}

}

// This code is contributed by sapnasingh4991  
  
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

# Python3 program to find first K

# elements whose difference with the

# median of array is maximum

 

# Function for calculating median

def findMedian(a, n):

 

 # Check for even case

 if (n % 2 != 0):

 return a[int(n / 2)]

 

 return (a[int((n - 1) / 2)] +

 a[int(n / 2)]) / 2.0

 

# Function to find the K maximum 

# absolute difference with the 

# median of the array

def kStrongest(arr, n, k):

 

 # Sort the array

 arr.sort()

 

 # Store median

 median = findMedian(arr, n)

 diff = [0] * (n)

 

 # Find and store difference

 for i in range(n):

 diff[i] = abs(median - arr[i])

 

 i = 0

 j = n - 1

 

 while (k > 0):

 

 # If diff[i] is greater print 

 # it. Else print diff[j]

 if (diff[i] > diff[j]):

 print(arr[i], end = " ")

 i += 1

 else:

 print(arr[j], end = " ")

 j -= 1

 

 k -= 1

 

# Driver code

arr = [ 1, 2, 3, 4, 5 ]

k = 3

n = len(arr)

 

kStrongest(arr, n, k)

 

# This code is contributed by sanjoy_62  
  
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

// C# implementation to find first K

// elements whose difference with the 

// median of array is maximum

using System;

 

class GFG{

 

// Function for calculating median 

static double findMedian(int []a, int n) 

{

 // Check for even case 

 if (n % 2 != 0) 

 return (double)a[n / 2]; 

 

 return (double)(a[(n - 1) / 2] + 

 a[n / 2]) / 2.0; 

} 

 

// Function to find the K maximum absolute

// difference with the median of the array

static void kStrongest(int []arr, int n,

 int k)

{

 

 // Sort the array.

 Array.Sort(arr);

 

 int i = 0;

 

 // Store median

 double median = findMedian(arr, n);

 int []diff = new int[n];

 

 // Find and store difference

 for(i = 0; i < n; i++) 

 {

 diff[i] = (int)Math.Abs(median - arr[i]);

 }

 

 int j = n - 1;

 i = 0;

 while (k > 0) 

 {

 

 // If diff[i] is greater print it

 // Else print diff[j]

 if (diff[i] > diff[j])

 {

 Console.Write(arr[i] + " ");

 i++;

 }

 else

 {

 Console.Write(arr[j] + " ");

 j--;

 }

 k--;

 }

}

 

// Driver Code

public static void Main(String[] args)

{

 int []arr = { 1, 2, 3, 4, 5 };

 int k = 3;

 int n = arr.Length;

 

 kStrongest(arr, n, k);

}

}

 

// This code is contributed by Rohit_ranjan  
  
---  
  
 __

 __

 **Output:**

    
    
    5 1 4

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

