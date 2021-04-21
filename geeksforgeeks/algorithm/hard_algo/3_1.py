Divide a sorted array in K parts with sum of difference of max and min
minimized in each part



Given an ascendingly sorted array **arr[]** of size **N** and an integer **K**
, the task is to partition the given array into **K** non-empty subarrays such
that the sum of differences of the maximum and the minimum of each subarray is
minimized.

 **Examples:**

> **Input:** arr[] = {4, 8, 15, 16, 23, 42}, K = 3  
> **Output:** 12  
> **Explanation:**  
> The given array can be split into three sub arrays in the following way:  
> {4, 8}, {15, 16, 23}, {42}  
> Here, the sum of difference of the minimum and maximum element in each of
> the subarrays respectively are:  
> 4 + 8 + 0 = 12.
>
>  **Input:** arr[] = {1, 2, 3, 4, 5}, K = 5  
> **Output:** 0

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** One observation that needs to be made is that we clearly know
that the sum of the difference between the maximum and the minimum element of
the subarray is minimum only when we choose the adjacent elements as the
maximum and the minimum element of the subarray. So:

  

  

  * Let’s say we have to split the array into K + 1 parts such that the first part will be arr[0 … i1-1], the second part will be arr[i1… i2-1] and so on.
  * So, the sum of the differences between the K parts will be:   

> sum = arr[i1-1] – arr[0] + arr[i2-1] – arr[i1] + …. + arr[n] – arr[iK]  
>

  * After rearranging the above value, we get:   

> sum = -arr[0] – (arr[i1] – arr[i1 – 1]) – (arr[i2] – arr[i2 – 1]) – …
> -(arr[iK] – arr[iK – 1]) + arr[N – 1]  
>

  * Clearly, the value to be computed is formed from the difference between the adjacent elements of the array. If this difference is maximum, then the sum will be minimum.
  * Therefore, the idea is to iterate over the array and store the difference between the adjacent elements of the array in another array.
  * Now, sort this array in descending order. We know that the maximum values of the difference should be taken to get the minimum difference.
  * Therefore, subtract the first **K – 1** values from the difference of the first and the last element of the array. This gives the sum of the remaining differences of the K subarrays formed from the array.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the minimum

// sum of differences possible for

// the given array when the array

// is divided into K subarrays

#include<bits/stdc++.h>

using namespace std;

// Function to find the minimum

// sum of differences possible for

// the given array when the array

// is divided into K subarrays

int calculate_minimum_split(int n, int a[], int k)

{

 // Array to store the differences

 // between two adjacent elements

 int p[n - 1];

 

 // Iterating through the array

 for(int i = 1; i < n; i++)

 

 // Storing differences to p

 p[i - 1] = a[i] - a[i - 1];

 

 // Sorting p in descending order

 sort(p, p + n - 1, greater<int>());

 

 // Sum of the first k-1 values of p

 int min_sum = 0;

 for(int i = 0; i < k - 1; i++)

 min_sum += p[i];

 

 // Computing the result

 int res = a[n - 1] - a[0] - min_sum;

 

 return res;

}

// Driver code

int main()

{

 int arr[6] = { 4, 8, 15, 16, 23, 42 };

 int k = 3;

 int n = sizeof(arr) / sizeof(int);

 cout << calculate_minimum_split(n, arr, k);

}

// This code is contributed by ishayadav181  
  
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

// Java program to find the minimum

// sum of differences possible for

// the given array when the array

// is divided into K subarrays

import java.util.*;

class GFG{

// Function to find the minimum

// sum of differences possible for

// the given array when the array

// is divided into K subarrays

static int calculate_minimum_split(int n, int a[],

 int k)

{

 

 // Array to store the differences

 // between two adjacent elements

 Integer[] p = new Integer[n - 1];

 // Iterating through the array

 for(int i = 1; i < n; i++)

 // Storing differences to p

 p[i - 1] = a[i] - a[i - 1];

 // Sorting p in descending order

 Arrays.sort(p, new Comparator<Integer>()

 {

 public int compare(Integer a, Integer b)

 {

 return b - a;

 }

 });

 // Sum of the first k-1 values of p

 int min_sum = 0;

 for(int i = 0; i < k - 1; i++)

 min_sum += p[i];

 // Computing the result

 int res = a[n - 1] - a[0] - min_sum;

 return res;

}

// Driver code

public static void main(String[] args)

{

 int arr[] = { 4, 8, 15, 16, 23, 42 };

 int k = 3;

 int n = arr.length;

 System.out.println(calculate_minimum_split(

 n, arr, k));

}

}

// This code is contributed by offbeat  
  
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

# Python3 program to find the minimum

# sum of differences possible for

# the given array when the array

# is divided into K subarrays

# Function to find the minimum

# sum of differences possible for

# the given array when the array

# is divided into K subarrays

def calculate_minimum_split(a, k):

 # Array to store the differences

 # between two adjacent elements

 p =[]

 n = len(a)

 # Iterating through the array

 for i in range(1, n):

 

 # Appending differences to p

 p.append(a[i]-a[i-1])

 # Sorting p in descending order

 p.sort(reverse = True)

 

 # Sum of the first k-1 values of p

 min_sum = sum(p[:k-1])

 

 # Computing the result

 res = a[n-1]-a[0]-min_sum

 

 return res

if __name__ == "__main__":

 arr = [4, 8, 15, 16, 23, 42]

 K = 3

 print(calculate_minimum_split(arr, K))  
  
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

// C# program to find the minimum

// sum of differences possible for 

// the given array when the array 

// is divided into K subarrays 

using System;

class GFG{

 

// Function to find the minimum 

// sum of differences possible for 

// the given array when the array 

// is divided into K subarrays 

static int calculate_minimum_split(int n, int[] a,

 int k) 

{ 

 

 // Array to store the differences 

 // between two adjacent elements 

 int[] p = new int[n - 1]; 

 

 // Iterating through the array 

 for(int i = 1; i < n; i++) 

 

 // Storing differences to p 

 p[i - 1] = a[i] - a[i - 1]; 

 

 // Sorting p in descending order 

 Array.Sort(p);

 Array.Reverse(p);

 

 // Sum of the first k-1 values of p 

 int min_sum = 0; 

 for(int i = 0; i < k - 1; i++) 

 min_sum += p[i]; 

 

 // Computing the result 

 int res = a[n - 1] - a[0] - min_sum; 

 

 return res; 

} 

// Driver code

static void Main()

{

 int[] arr = { 4, 8, 15, 16, 23, 42 }; 

 int k = 3; 

 int n = arr.Length; 

 Console.Write(calculate_minimum_split(

 n, arr, k));

}

}

// This code is contributed by divyeshrabadiya07  
  
---  
  
 __

 __

 **Output:**

    
    
    12
    
    

**Time Complexity:** _O(N * log(N))_ , where N is the size of the array.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

