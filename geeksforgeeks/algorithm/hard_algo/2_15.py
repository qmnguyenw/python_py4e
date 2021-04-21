Maximize sum of all elements which are not a part of the Longest Increasing
Subsequence



Given an array **arr[]** , the task is to find the maximum sum of all the
elements which are not a part of the longest increasing subsequence.  
**Examples:**

> **Input:** arr[] = {4, 6, 1, 2, 3, 8}  
> **Output:** 10  
> **Explanation:**  
> Elements are 4 and 6  
> **Input:** arr[] = {5, 4, 3, 2, 1}  
> **Output:** 14  
> **Explanation:**  
> Elements are 5, 4, 3, 2

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  * The idea is to find the longest increasing subsequence with the minimum sum and then subtract it from the sum of all elements. 
  * To do this we will use the concept of LIS using Dynamic Programming and store the sum along with the length of the subsequences and update the minimum sum accordingly. 

Below is the implementation of the above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the Maximum sum of

// all elements which are not a part of

// longest increasing sub sequence

#include <bits/stdc++.h>

using namespace std;

// Function to find maximum sum

int findSum(int* arr, int n)

{

 int totalSum = 0;

 // Find total sum of array

 for (int i = 0; i < n; i++) {

 totalSum += arr[i];

 }

 // Maintain a 2D array

 int dp[2][n];

 for (int i = 0; i < n; i++) {

 dp[0][i] = 1;

 dp[1][i] = arr[i];

 }

 // Update the dp array along

 // with sum in the second row

 for (int i = 1; i < n; i++) {

 for (int j = 0; j < i; j++) {

 if (arr[i] > arr[j]) {

 // In case of greater length

 // Update the length along

 // with sum

 if (dp[0][i] < dp[0][j] + 1) {

 dp[0][i] = dp[0][j] + 1;

 dp[1][i] = dp[1][j]

 + arr[i];

 }

 // In case of equal length

 // find length update length

 // with minimum sum

 else if (dp[0][i]

 == dp[0][j] + 1) {

 dp[1][i]

 = min(dp[1][i],

 dp[1][j]

 + arr[i]);

 }

 }

 }

 }

 int maxm = 0;

 int subtractSum = 0;

 // Find the sum that need to

 // be subtracted from total sum

 for (int i = 0; i < n; i++) {

 if (dp[0][i] > maxm) {

 maxm = dp[0][i];

 subtractSum = dp[1][i];

 }

 else if (dp[0][i] == maxm) {

 subtractSum = min(subtractSum,

 dp[1][i]);

 }

 }

 // Return the sum

 return totalSum - subtractSum;

}

// Driver code

int main()

{

 int arr[] = { 4, 6, 1, 2, 3, 8 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << findSum(arr, n);

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

// Java program to find the Maximum sum of

// all elements which are not a part of

// longest increasing sub sequence

class GFG{

// Function to find maximum sum

static int findSum(int []arr, int n)

{

 int totalSum = 0;

 // Find total sum of array

 for(int i = 0; i < n; i++)

 {

 totalSum += arr[i];

 }

 // Maintain a 2D array

 int [][]dp = new int[2][n];

 for(int i = 0; i < n; i++)

 {

 dp[0][i] = 1;

 dp[1][i] = arr[i];

 }

 // Update the dp array along

 // with sum in the second row

 for(int i = 1; i < n; i++)

 {

 for(int j = 0; j < i; j++)

 {

 if (arr[i] > arr[j])

 {

 

 // In case of greater length

 // Update the length along

 // with sum

 if (dp[0][i] < dp[0][j] + 1)

 {

 dp[0][i] = dp[0][j] + 1;

 dp[1][i] = dp[1][j] + arr[i];

 }

 

 // In case of equal length

 // find length update length

 // with minimum sum

 else if (dp[0][i] == dp[0][j] + 1)

 {

 dp[1][i] = Math.min(dp[1][i],

 dp[1][j] + arr[i]);

 }

 }

 }

 }

 int maxm = 0;

 int subtractSum = 0;

 // Find the sum that need to

 // be subtracted from total sum

 for(int i = 0; i < n; i++)

 {

 if (dp[0][i] > maxm)

 {

 maxm = dp[0][i];

 subtractSum = dp[1][i];

 }

 else if (dp[0][i] == maxm)

 {

 subtractSum = Math.min(subtractSum, dp[1][i]);

 }

 }

 // Return the sum

 return totalSum - subtractSum;

}

// Driver code

public static void main(String[] args)

{

 int arr[] = { 4, 6, 1, 2, 3, 8 };

 int n = arr.length;

 System.out.print(findSum(arr, n));

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

# Python3 program to find the maximum sum

# of all elements which are not a part of

# longest increasing sub sequence

# Function to find maximum sum

def findSum(arr, n):

 totalSum = 0

 # Find total sum of array

 for i in range(n):

 totalSum += arr[i]

 # Maintain a 2D array

 dp = [[0] * n for i in range(2)]

 for i in range(n):

 dp[0][i] = 1

 dp[1][i] = arr[i]

 # Update the dp array along

 # with sum in the second row

 for i in range(1, n):

 for j in range(i):

 if (arr[i] > arr[j]):

 # In case of greaer length

 # update the length along

 # with sum

 if (dp[0][i] < dp[0][j] + 1):

 dp[0][i] = dp[0][j] + 1

 dp[1][i] = dp[1][j] + arr[i]

 # In case of equal length

 # find length update length

 # with minimum sum

 elif (dp[0][i] == dp[0][j] + 1):

 dp[1][i] = min(dp[1][i],

 dp[1][j] +

 arr[i])

 maxm = 0

 subtractSum = 0

 # Find the sum that need to

 # be subtracted from total sum

 for i in range(n):

 if (dp[0][i] > maxm):

 maxm = dp[0][i]

 subtractSum = dp[1][i]

 elif (dp[0][i] == maxm):

 subtractSum = min(subtractSum,

 dp[1][i])

 # Return the sum

 return totalSum - subtractSum

# Driver code

arr = [ 4, 6, 1, 2, 3, 8 ]

n = len(arr)

print(findSum(arr, n))

# This code is contributed by himanshu77  
  
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

// C# program to find the Maximum sum of

// all elements which are not a part of

// longest increasing sub sequence

using System;

class GFG{

// Function to find maximum sum

static int findSum(int []arr, int n)

{

 int totalSum = 0;

 // Find total sum of array

 for(int i = 0; i < n; i++)

 {

 totalSum += arr[i];

 }

 // Maintain a 2D array

 int [,]dp = new int[2, n];

 for(int i = 0; i < n; i++)

 {

 dp[0, i] = 1;

 dp[1, i] = arr[i];

 }

 // Update the dp array along

 // with sum in the second row

 for(int i = 1; i < n; i++)

 {

 for(int j = 0; j < i; j++)

 {

 if (arr[i] > arr[j])

 {

 

 // In case of greater length

 // Update the length along

 // with sum

 if (dp[0, i] < dp[0, j] + 1)

 {

 dp[0, i] = dp[0, j] + 1;

 dp[1, i] = dp[1, j] + arr[i];

 }

 

 // In case of equal length

 // find length update length

 // with minimum sum

 else if (dp[0, i] == dp[0, j] + 1)

 {

 dp[1, i] = Math.Min(dp[1, i],

 dp[1, j] + arr[i]);

 }

 }

 }

 }

 int maxm = 0;

 int subtractSum = 0;

 // Find the sum that need to

 // be subtracted from total sum

 for(int i = 0; i < n; i++)

 {

 if (dp[0, i] > maxm)

 {

 maxm = dp[0, i];

 subtractSum = dp[1, i];

 }

 else if (dp[0, i] == maxm)

 {

 subtractSum = Math.Min(subtractSum, dp[1, i]);

 }

 }

 // Return the sum

 return totalSum - subtractSum;

}

// Driver code

public static void Main(String[] args)

{

 int []arr = { 4, 6, 1, 2, 3, 8 };

 int n = arr.Length;

 Console.Write(findSum(arr, n));

}

}

// This code is contributed by sapnasingh4991  
  
---  
  
 __

 __

 **Output:**

    
    
    10

_**Time Complexity:** O(N2) where N is the length of the array arr[]_  
 _ **Auxiliary Space:** O(N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

