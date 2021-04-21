Pick maximum sum M elements such that contiguous repetitions do not exceed K



Given an array **arr[]** of distinct elements and two integers **M** and **K**
, the task is to generate an array from the given array elements (elements can
repeat in the generated array) such that the size of the generated array is
**M** and the length of any sub-array with all same elements must not exceed
**K**. Print the maximum sum of the elements among all the possible arrays
that can be generated.

 **Examples:**

>  **Input:** arr[] = {1, 3, 6, 7, 4, 5}, M = 9, K = 2  
>  **Output:** 60  
> The maxim sum arrangement is 7 7 6 7 7 6 7 7 6. Note that there is no
> subarray of size more than 2 with all same elements.
>
>  **Input:** arr[] = {8, 13, 9, 17, 4, 12}, M = 5, K = 1  
>  **Output:** 77  
> The maxim sum arrangement is 17, 13, 17, 13, 17

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** If we want the maximum sum we have to take **maximum** value
from the array but we can repeat this maximum value at most K times so we have
to separate it by **second maximum** value only once and after that we again
take first maximum value up to K times and this cycle goes on until we take
total **M** values.

  

  

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

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the maximum required sum

long int maxSum(int arr[], int n, int m, int k)

{

 

 int max1 = -1, max2 = -1;

 

 // All the elements in the array are distinct

 // Finding the maximum and the second maximum

 // element from the array

 for (int i = 0; i < n; i++) {

 if (arr[i] > max1) {

 max2 = max1;

 max1 = arr[i];

 }

 else if (arr[i] > max2)

 max2 = arr[i];

 }

 

 // Total times the second maximum element

 // will appear in the generated array

 int counter = m / (k + 1);

 

 long int sum = counter * max2 + (m - counter) * max1;

 

 // Return the required sum

 return sum;

}

 

// Driver code

int main()

{

 int arr[] = { 1, 3, 6, 7, 4, 5 };

 int n = sizeof(arr) / sizeof(arr[0]);

 int m = 9, k = 2;

 cout << maxSum(arr, n, m, k);

 

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

import java.util.*;

 

class GFG

{

 

// Function to return the maximum required sum

static int maxSum(int arr[], int n, int m, int k)

{

 

 int max1 = -1, max2 = -1;

 

 // All the elements in the array are distinct

 // Finding the maximum and the second maximum

 // element from the array

 for (int i = 0; i < n; i++) 

 {

 if (arr[i] > max1) 

 {

 max2 = max1;

 max1 = arr[i];

 }

 else if (arr[i] > max2)

 max2 = arr[i];

 }

 

 // Total times the second maximum element

 // will appear in the generated array

 int counter = m / (k + 1);

 

 int sum = counter * max2 + (m - counter) * max1;

 

 // Return the required sum

 return sum;

}

 

// Driver code

public static void main(String args[])

{

 int arr[] = { 1, 3, 6, 7, 4, 5 };

 int n = arr.length;

 int m = 9, k = 2;

 System.out.println(maxSum(arr, n, m, k));

}

}

 

// This code is contributed by

// Surendra Gangwar  
  
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

def maxSum(arr, n, m, k):

 

 max1 = -1

 max2 = -1

 

 # All the elements in the array are distinct

 # Finding the maximum and the second maximum 

 # element from the array

 for i in range(0, n):

 if(arr[i] > max1):

 max2 = max1

 max1 = arr[i]

 elif(arr[i] > max2):

 max2 = arr[i]

 

 # Total times the second maximum element 

 # will appear in the generated array

 counter = int(m / (k + 1))

 

 sum = counter * max2 + (m - counter) * max1

 

 # Return the required sum

 return int(sum)

 

# Driver code

arr = [1, 3, 6, 7, 4, 5] 

n = len(arr)

m = 9

k = 2

 

print(maxSum(arr, n, m, k))  
  
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

 

// Function to return the maximum required sum

static int maxSum(int []arr, int n, int m, int k)

{

 

 int max1 = -1, max2 = -1;

 

 // All the elements in the array are distinct

 // Finding the maximum and the second maximum

 // element from the array

 for (int i = 0; i < n; i++) 

 {

 if (arr[i] > max1) 

 {

 max2 = max1;

 max1 = arr[i];

 }

 else if (arr[i] > max2)

 max2 = arr[i];

 }

 

 // Total times the second maximum element

 // will appear in the generated array

 int counter = m / (k + 1);

 

 int sum = counter * max2 + (m - counter) * max1;

 

 // Return the required sum

 return sum;

}

 

// Driver code

public static void Main(String []args)

{

 int []arr = { 1, 3, 6, 7, 4, 5 };

 int n = arr.Length;

 int m = 9, k = 2;

 Console.WriteLine(maxSum(arr, n, m, k));

}

}

 

/* This code contributed by PrinciRaj1992 */  
  
---  
  
 __

 __

 **Output:**

    
    
    60
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

