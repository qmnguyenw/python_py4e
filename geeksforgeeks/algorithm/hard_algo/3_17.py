Maximize the sum of array after multiplying a prefix and suffix by -1



Given an array **arr[]** of length **N** , the task is to maximize the sum of
all the elements of the array by performing the following operations at most
once.

  * Choose a prefix of the array and multiply all the elements by -1.
  * Choose a suffix of the array and multiply all the elements by -1.

 **Examples:**

> **Input:** arr[] = {-1, -2, -3}  
> **Output:** 6  
> **Explanation:**  
> **Operation 1:** Prefix of array – {-1, -2, -3}  
> can be multiplied with -1 to get the maximum sum.  
> Array after Operation: {1, 2, 3}  
> Sum = 1 + 2 + 3 = 6
>
>  **Input:** arr[] = {-4, 2, 0, 5, 0}  
> **Output:** 11  
> **Explanation:**  
> **Operation 1:** Prefix of array – {-4}  
> can be multiplied with -1 to get the maximum sum.  
> Array after operation: {4, 2, 0, 5, 0}  
> Sum = 4 + 2 + 0 + 5 + 0 = 11

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The key observation in the problem is if the chosen range of
the prefix and suffix intersect, then the elements of intersection portion
have same sign. Due to which it is always better to choose non-intersecting
ranges of the prefix and suffix array. Below is the illustration of the steps:

  

  

  * It is easily been observed that there will be a portion/subarray in the array whose sum is the same as the original and the sum of the other elements is reversed. So the new sum of the array will be: 

    
    
    // X - Sum of subarray which is not in
    //     the range of the prefix and suffix
    // S - Sum of the original array
    
    New Sum = X + -1*(S - X) = 2*X - S 

  * Hence, the idea is to maximize the value of X to get the maximum sum because S is the constant value which cannot be changed. This can be achieved with the help of the Kadane’s Algorithm.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// maximum sum of the array by

// multiplying the prefix and suffix

// of the array by -1

#include <bits/stdc++.h>

using namespace std;

// Kadane's algorithm to find

// the maximum subarray sum

int maxSubArraySum(int a[], int size)

{

 int max_so_far = INT_MIN,

 max_ending_here = 0;

 

 // Loop to find the maximum subarray

 // array sum in the given array

 for (int i = 0; i < size; i++) {

 max_ending_here =

 max_ending_here + a[i];

 if (max_ending_here < 0)

 max_ending_here = 0;

 if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 }

 return max_so_far;

}

// Function to find the maximum

// sum of the array by multiplying

// the prefix and suffix by -1

int maxSum(int a[], int n)

{

 

 // Total intital sum

 int S = 0;

 

 // Loop to find the maximum

 // sum of the array

 for (int i = 0; i < n; i++)

 S += a[i];

 int X = maxSubArraySum(a, n);

 

 // Maximum value

 return 2 * X - S;

}

// Driver Code

int main()

{

 int a[] = { -1, -2, -3 };

 int n = sizeof(a) / sizeof(a[0]);

 int max_sum = maxSum(a, n);

 cout << max_sum;

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

// Java implementation to find the

// maximum sum of the array by

// multiplying the prefix and suffix

// of the array by -1

class GFG

{

 

 // Kadane's algorithm to find

 // the maximum subarray sum

 static int maxSubArraySum(int a[], int size)

 {

 int max_so_far = Integer.MIN_VALUE,

 max_ending_here = 0;

 

 // Loop to find the maximum subarray

 // array sum in the given array

 for (int i = 0; i < size; i++) {

 max_ending_here =

 max_ending_here + a[i];

 if (max_ending_here < 0)

 max_ending_here = 0;

 if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 }

 return max_so_far;

 }

 

 // Function to find the maximum

 // sum of the array by multiplying

 // the prefix and suffix by -1

 static int maxSum(int a[], int n)

 {

 

 // Total intital sum

 int S = 0;

 int i;

 // Loop to find the maximum

 // sum of the array

 for (i = 0; i < n; i++)

 S += a[i];

 int X = maxSubArraySum(a, n);

 

 // Maximum value

 return 2 * X - S;

 }

 

 // Driver Code

 public static void main(String []args)

 {

 int a[] = { -1, -2, -3 };

 int n = a.length;

 int max_sum = maxSum(a, n);

 System.out.print(max_sum);

 }

}

// This code is contributed by chitranayal  
  
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

# Python3 implementation to find the

# maximum sum of the array by

# multiplying the prefix and suffix

# of the array by -1

# Kadane's algorithm to find

# the maximum subarray sum

def maxSubArraySum(a, size):

 max_so_far = -10**9

 max_ending_here = 0

 # Loop to find the maximum subarray

 # array sum in the given array

 for i in range(size):

 max_ending_here = max_ending_here + a[i]

 if (max_ending_here < 0):

 max_ending_here = 0

 if (max_so_far < max_ending_here):

 max_so_far = max_ending_here

 return max_so_far

# Function to find the maximum

# sum of the array by multiplying

# the prefix and suffix by -1

def maxSum(a, n):

 # Total intital sum

 S = 0

 # Loop to find the maximum

 # sum of the array

 for i in range(n):

 S += a[i]

 X = maxSubArraySum(a, n)

 # Maximum value

 return 2 * X - S

# Driver Code

if __name__ == '__main__':

 a=[-1, -2, -3]

 n= len(a)

 max_sum = maxSum(a, n)

 print(max_sum)

# This code is contributed by mohit kumar 29  
  
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

// C# implementation to find the

// maximum sum of the array by

// multiplying the prefix and suffix

// of the array by -1

using System;

class GFG

{

 

 // Kadane's algorithm to find

 // the maximum subarray sum

 static int maxSubArraySum(int []a, int size)

 {

 int max_so_far = int.MinValue,

 max_ending_here = 0;

 

 // Loop to find the maximum subarray

 // array sum in the given array

 for (int i = 0; i < size; i++) {

 max_ending_here =

 max_ending_here + a[i];

 if (max_ending_here < 0)

 max_ending_here = 0;

 if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 }

 return max_so_far;

 }

 

 // Function to find the maximum

 // sum of the array by multiplying

 // the prefix and suffix by -1

 static int maxSum(int []a, int n)

 {

 

 // Total intital sum

 int S = 0;

 int i;

 

 // Loop to find the maximum

 // sum of the array

 for (i = 0; i < n; i++)

 S += a[i];

 int X = maxSubArraySum(a, n);

 

 // Maximum value

 return 2 * X - S;

 }

 

 // Driver Code

 public static void Main(String []args)

 {

 int []a = { -1, -2, -3 };

 int n = a.Length;

 int max_sum = maxSum(a, n);

 Console.Write(max_sum);

 }

}

// This code is contributed by sapnasingh4991  
  
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

// Javascript implementation to find the

// maximum sum of the array by

// multiplying the prefix and suffix

// of the array by -1 

// Kadane's algorithm to find

// the maximum subarray sum

function maxSubArraySum(a, size)

{

 var max_so_far = Number.MIN_VALUE,

 max_ending_here = 0;

 // Loop to find the maximum subarray

 // array sum in the given array

 for(i = 0; i < size; i++)

 {

 max_ending_here = max_ending_here + a[i];

 

 if (max_ending_here < 0)

 max_ending_here = 0;

 

 if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 }

 return max_so_far;

}

// Function to find the maximum

// sum of the array by multiplying

// the prefix and suffix by -1

function maxSum(a, n)

{

 

 // Total intital sum

 var S = 0;

 var i;

 // Loop to find the maximum

 // sum of the array

 for(i = 0; i < n; i++)

 S += a[i];

 

 var X = maxSubArraySum(a, n);

 // Maximum value

 return 2 * X - S;

}

// Driver Code

var a = [ -1, -2, -3 ];

var n = a.length;

var max_sum = maxSum(a, n);

document.write(max_sum);

// This code is contributed by aashish1995

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    6

**Time Complexity:** O(N)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

