Maximum sum subarray of even length



Given an array **arr[]** of **N** elements, the task is to find the maximum
sum of any subarray of length **X** such that **X > 0** and **X % 2 = 0**.

 **Examples:**

>  **Input:** arr[] = {1, 2, 3}  
>  **Output:** 5  
> {2, 3} is the required subarray.
>
>  **Input:** arr[] = {8, 9, -8, 9, 10}  
>  **Output:** 20  
> {9, -8, 9, 10} is the required subarray.  
> Even though {8, 9, -8, 9, 10} has the maximum sum  
> but it is not of even length.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem is a variation of maximum subarray sum problem and
can be solved using dynamic programming approach. Create an array **dp[]**
where **dp[i]** will store the maximum sum of an even length subarray whose
first element is **arr[i]**. Now the recurrence relation will be:

  

  

> dp[i] = max((arr[i] + arr[i + 1]), (arr[i] + arr[i + 1] + dp[i + 2]))

This is because the maximum sum even length subarray starting with the element
**arr[i]** can either be the sum of **arr[i]** and **arr[i + 1]** or it can be
**arr[i] + arr[i + 1]** added with the maximum sum of even length subarray
starting with **arr[i + 2]** i.e. **dp[i + 2]**. Take the maximum of these
two.  
In the end, the maximum value from the **dp[]** array will be the required
answer.

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

 

// Function to return the maximum

// subarray sum of even length

int maxEvenLenSum(int arr[], int n)

{

 

 // There has to be at

 // least 2 elements

 if (n < 2)

 return 0;

 

 // dp[i] will store the maximum

 // subarray sum of even length

 // starting at arr[i]

 int dp[n] = { 0 };

 

 // Valid subarray cannot start from

 // the last element as its

 // length has to be even

 dp[n - 1] = 0;

 dp[n - 2] = arr[n - 2] + arr[n - 1];

 

 for (int i = n - 3; i >= 0; i--) {

 

 // arr[i] and arr[i + 1] can be added

 // to get an even length subarray

 // starting at arr[i]

 dp[i] = arr[i] + arr[i + 1];

 

 // If the sum of the valid subarray starting

 // from arr[i + 2] is greater than 0 then it

 // can be added with arr[i] and arr[i + 1]

 // to maximize the sum of the subarray

 // starting from arr[i]

 if (dp[i + 2] > 0)

 dp[i] += dp[i + 2];

 }

 

 // Get the sum of the even length

 // subarray with maximum sum

 int maxSum = *max_element(dp, dp + n);

 return maxSum;

}

 

// Driver code

int main()

{

 

 int arr[] = { 8, 9, -8, 9, 10 };

 int n = sizeof(arr) / sizeof(int);

 

 cout << maxEvenLenSum(arr, n);

 

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

import java.util.Arrays;

 

class GFG 

{

 

// Function to return the maximum

// subarray sum of even length

static int maxEvenLenSum(int arr[], int n)

{

 

 // There has to be at

 // least 2 elements

 if (n < 2)

 return 0;

 

 // dp[i] will store the maximum

 // subarray sum of even length

 // starting at arr[i]

 int []dp = new int[n];

 

 // Valid subarray cannot start from

 // the last element as its

 // length has to be even

 dp[n - 1] = 0;

 dp[n - 2] = arr[n - 2] + arr[n - 1];

 

 for (int i = n - 3; i >= 0; i--) 

 {

 

 // arr[i] and arr[i + 1] can be added

 // to get an even length subarray

 // starting at arr[i]

 dp[i] = arr[i] + arr[i + 1];

 

 // If the sum of the valid subarray starting

 // from arr[i + 2] is greater than 0 then it

 // can be added with arr[i] and arr[i + 1]

 // to maximize the sum of the subarray

 // starting from arr[i]

 if (dp[i + 2] > 0)

 dp[i] += dp[i + 2];

 }

 

 // Get the sum of the even length

 // subarray with maximum sum

 int maxSum = Arrays.stream(dp).max().getAsInt();

 return maxSum;

}

 

// Driver code

public static void main(String[] args) 

{

 int arr[] = { 8, 9, -8, 9, 10 };

 int n = arr.length;

 

 System.out.println(maxEvenLenSum(arr, n));

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

# Python3 implementation of the approach

 

# Function to return the maximum

# subarray sum of even length

def maxEvenLenSum(arr, n):

 

 # There has to be at

 # least 2 elements

 if (n < 2):

 return 0

 

 # dp[i] will store the maximum

 # subarray sum of even length

 # starting at arr[i]

 dp = [0 for i in range(n)]

 

 # Valid subarray cannot start from

 # the last element as its

 # length has to be even

 dp[n - 1] = 0

 dp[n - 2] = arr[n - 2] + arr[n - 1]

 

 for i in range(n - 3, -1, -1):

 

 # arr[i] and arr[i + 1] can be added

 # to get an even length subarray

 # starting at arr[i]

 dp[i] = arr[i] + arr[i + 1]

 

 # If the sum of the valid subarray 

 # starting from arr[i + 2] is 

 # greater than 0 then it can be added 

 # with arr[i] and arr[i + 1]

 # to maximize the sum of the 

 # subarray starting from arr[i]

 if (dp[i + 2] > 0):

 dp[i] += dp[i + 2]

 

 # Get the sum of the even length

 # subarray with maximum sum

 maxSum = max(dp)

 return maxSum

 

# Driver code

arr = [8, 9, -8, 9, 10]

n = len(arr)

 

print(maxEvenLenSum(arr, n))

 

# This code is contributed by Mohit Kumar  
  
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

 static int MaxSum(int []arr)

 { 

 

 // assigning first element to the array

 int large = arr[0];

 

 // loop to compare value of large

 // with other elements

 for (int i = 1; i < arr.Length; i++)

 {

 // if large is smaller than other element

 // assig that element to the large

 if (large < arr[i])

 large = arr[i];

 }

 return large;

 }

 

 // Function to return the maximum 

 // subarray sum of even length 

 static int maxEvenLenSum(int []arr, int n) 

 { 

 

 // There has to be at 

 // least 2 elements 

 if (n < 2) 

 return 0; 

 

 // dp[i] will store the maximum 

 // subarray sum of even length 

 // starting at arr[i] 

 int []dp = new int[n]; 

 

 // Valid subarray cannot start from 

 // the last element as its 

 // length has to be even 

 dp[n - 1] = 0; 

 dp[n - 2] = arr[n - 2] + arr[n - 1]; 

 

 for (int i = n - 3; i >= 0; i--) 

 { 

 

 // arr[i] and arr[i + 1] can be added 

 // to get an even length subarray 

 // starting at arr[i] 

 dp[i] = arr[i] + arr[i + 1]; 

 

 // If the sum of the valid subarray starting 

 // from arr[i + 2] is greater than 0 then it 

 // can be added with arr[i] and arr[i + 1] 

 // to maximize the sum of the subarray 

 // starting from arr[i] 

 if (dp[i + 2] > 0) 

 dp[i] += dp[i + 2]; 

 } 

 

 // Get the sum of the even length 

 // subarray with maximum sum 

 int maxSum = MaxSum(dp);

 return maxSum; 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 int []arr = { 8, 9, -8, 9, 10 }; 

 int n = arr.Length; 

 

 Console.WriteLine(maxEvenLenSum(arr, n)); 

 } 

}

 

// This code is contributed by kanugargng  
  
---  
  
 __

 __

 **Output:**

    
    
    20
    

**Time complexity:** O(n)  
 **Space complexity:** O(n)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

