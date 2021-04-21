Length of longest increasing index dividing subsequence



Given an array **arr[]** of size **N** , the task is to find the longest
increasing sub-sequence such that index of any element is divisible by index
of previous element (LIIDS). The following are the necessary conditions for
the LIIDS:

If i, j are two indices in the given array. Then:

  * i < j
  * j % i = 0
  * arr[i] < arr[j]

 **Examples:**

>  **Input:** arr[] = {1, 2, 3, 7, 9, 10}  
>  **Output:** 3  
>  **Explanation:**  
>  The subsequence = {1, 2, 7}  
> Indices of the elements of sub-sequence = {1, 2, 4}  
> Indices condition:  
> 2 is divisible by 1  
> 4 is divisible by 2  
> OR  
> Another possible sub-sequence = {1, 3, 10}  
> Indices of elements of sub-sequence = {1, 3, 6}  
> Indices condition:  
> 3 is divisible by 1  
> 6 is divisible by 3
>
>  **Input:** arr[] = {7, 1, 3, 4, 6}  
>  **Output:** 2  
>  **Explanation:**  
>  The sub-sequence = {1, 4}  
> Indices of elements of sub-sequence = {2, 4}  
> Indices condition:  
> 4 is divisible by 2
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use the concept of Dynamic programming to solve
this problem.

  * Create a dp[] array first and initialize the array with 1. This is because, the minimum length of the dividing subsequence is 1.
  * Now, for every index ‘i’ in the array, increment the count of the values at the indices at all its multiples.
  * Finally, when the above step is performed for all the values, the maximum value present in the array is the required answer.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the length of

// the longest increasing sub-sequence

// such that the index of the element is

// divisible by index of previous element

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the length of

// the longest increasing sub-sequence

// such that the index of the element is

// divisible by index of previous element

int LIIDS(int arr[], int N)

{

 // Initialize the dp[] array with 1 as a

 // single element will be of 1 length

 int dp[N + 1];

 

 int ans = 0;

 for (int i = 1; i <= N; i++) {

 dp[i] = 1;

 }

 

 // Traverse the given array

 for (int i = 1; i <= N; i++) {

 

 // If the index is divisible by

 // the previous index

 for (int j = i + i; j <= N; j += i) {

 

 // if increasing

 // subsequence identified

 if (arr[j] > arr[i]) {

 dp[j] = max(dp[j], dp[i] + 1);

 }

 }

 

 // Longest length is stored

 ans = max(ans, dp[i]);

 }

 return ans;

}

 

// Driver code

int main()

{

 

 int arr[] = { 1, 2, 3, 7, 9, 10 };

 int N = sizeof(arr) / sizeof(arr[0]);

 

 cout << LIIDS(arr, N);

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

// Java program to find the length of

// the longest increasing sub-sequence

// such that the index of the element is

// divisible by index of previous element

import java.util.*;

 

class GFG{

 

// Function to find the length of

// the longest increasing sub-sequence

// such that the index of the element is

// divisible by index of previous element

static int LIIDS(int arr[], int N)

{

 

 // Initialize the dp[] array with 1 as a

 // single element will be of 1 length

 int[] dp = new int[N + 1];

 int ans = 0;

 

 for(int i = 1; i <= N; i++)

 {

 dp[i] = 1;

 }

 

 // Traverse the given array

 for(int i = 1; i <= N; i++)

 {

 

 // If the index is divisible by

 // the previous index

 for(int j = i + i; j <= N; j += i)

 {

 

 // If increasing

 // subsequence identified

 if (j < arr.length && arr[j] > arr[i])

 {

 dp[j] = Math.max(dp[j], dp[i] + 1);

 }

 }

 

 // Longest length is stored

 ans = Math.max(ans, dp[i]);

 }

 return ans;

}

 

// Driver code

public static void main(String args[])

{

 int arr[] = { 1, 2, 3, 7, 9, 10 };

 int N = arr.length;

 

 System.out.println(LIIDS(arr, N));

}

}

 

// This code is contributed by AbhiThakur  
  
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

# Python3 program to find the length of

# the longest increasing sub-sequence 

# such that the index of the element is 

# divisible by index of previous element 

 

# Function to find the length of 

# the longest increasing sub-sequence 

# such that the index of the element is 

# divisible by index of previous element 

def LIIDS(arr, N):

 

 # Initialize the dp[] array with 1 as a 

 # single element will be of 1 length 

 dp = []

 for i in range(1, N + 1):

 dp.append(1)

 

 ans = 0

 

 # Traverse the given array 

 for i in range(1, N + 1):

 

 # If the index is divisible by 

 # the previous index 

 j = i + i

 while j <= N:

 

 # If increasing 

 # subsequence identified 

 if j < N and i < N and arr[j] > arr[i]:

 dp[j] = max(dp[j], dp[i] + 1)

 

 j += i

 

 # Longest length is stored 

 if i < N:

 ans = max(ans, dp[i])

 

 return ans

 

# Driver code 

arr = [ 1, 2, 3, 7, 9, 10 ]

 

N = len(arr)

 

print(LIIDS(arr, N))

 

# This code is contributed by ishayadav181  
  
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

// C# program to find the length of

// the longest increasing sub-sequence

// such that the index of the element is

// divisible by index of previous element

using System; 

 

class GFG{

 

// Function to find the length of

// the longest increasing sub-sequence

// such that the index of the element is

// divisible by index of previous element

static int LIIDS(int[] arr, int N)

{

 

 // Initialize the dp[] array with 1 as a

 // single element will be of 1 length

 int[] dp = new int[N + 1];

 int ans = 0;

 

 for(int i = 1; i <= N; i++)

 {

 dp[i] = 1;

 }

 

 // Traverse the given array

 for(int i = 1; i <= N; i++)

 {

 

 // If the index is divisible by

 // the previous index

 for(int j = i + i; j <= N; j += i)

 {

 

 // If increasing

 // subsequence identified

 if (j < arr.Length && arr[j] > arr[i])

 {

 dp[j] = Math.Max(dp[j], dp[i] + 1);

 }

 }

 

 // Longest length is stored

 ans = Math.Max(ans, dp[i]);

 }

 return ans;

}

 

// Driver code

public static void Main()

{

 int[] arr = new int[] { 1, 2, 3, 7, 9, 10 };

 int N = arr.Length;

 

 Console.WriteLine(LIIDS(arr, N));

}

}

 

// This code is contributed by sanjoy_62  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time Complexity:** _O(N log(N))_ , where N is the length of the array.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

