Minimum number of adjacent swaps required to convert a permutation to another
permutation by given condition



Given a **permutation P** of size **N** , having values from **1 to N**. the
task is to find the minimum number of adjacent swaps required such that for
all i in the range **[1, N]** , **P[i] does not equal i**.  
 **Examples:**

> **Input:** P = [1, 4, 3, 5, 2]  
> **Output:** 2  
> **Explanation:**  
> Here P = [1, 4, 3, 5, 2] at index 1, 2, 3, 4, 5. As we can see, P[1] = 1 and
> P[3] = 3. Hence, we need to get rid of this invariant.  
> Swap 1: Swap index 1 and index 2 => [4, 1, 3, 5, 2]  
> Swap 2: Swap index 2 and index 3 => [4, 3, 1, 5, 2]  
> The final array has no i where P[i] = i. Hence, a minimum of 2 swaps is
> required.
>
>  **Input:** P = [1, 2, 4, 9, 5, 8, 7, 3, 6]  
> **Output:** 3  
> **Explanation:**  
> Swap 1: Swap index 1 and index 2 => [2, 1, 4, 9, 5, 8, 7, 3, 6]  
> Swap 2: Swap index 5 and index 6 => [2, 1, 4, 9, 8, 5, 7, 3, 6]  
> Swap 2: Swap index 7 and index 8 => [2, 1, 4, 9, 8, 5, 3, 7, 6]  
> Hence, a minimum of 3 swaps is required.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Let us consider the positions where **P[i] = i** be denoted by
**X** and the other positions by **O**. Below are three basic observation for
the question:

  * If values at any two adjacent index of the permutation is of the form **XO** , we can simply swap the 2 indexes to get ‘OO’.
  * If values at any two adjacent index of the permutation is of the form **XX** , we can simply swap the 2 indexes to get ‘OO’.
  * If values at any two adjacent index of the permutation is of the form **OX** , it is simply **‘XO’** or **‘XX’** once the pointer reaches index at **X**.

Below are the steps:

  

  

  1. Iterate from **1 to N – 1** and check if **P[i] = i** then we simply **swap(P[i], P[i + 1])** , otherwise continue the process for the next adjacent pairs.
  2. The Corner Case for the given question is when **i = N** , if P[i] = i, then we **swap(P[i], P[i – 1])**.

Below is the implementation of above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the minimum

// number of swaps

void solve(vector<int>& P, int n)

{

 

 // New array to convert

 // to 1-based indexing

 vector<int> arr;

 

 arr.push_back(0);

 

 for (auto x : P)

 arr.push_back(x);

 

 // Keeps count of swaps

 int cnt = 0;

 

 for (int i = 1; i < n; i++) {

 

 // Check if it is an 'X' position

 if (arr[i] == i) {

 swap(arr[i], arr[i + 1]);

 cnt++;

 }

 }

 

 // Corner Case

 if (arr[n] == n) {

 

 swap(arr[n - 1], arr[n]);

 cnt++;

 }

 

 // Print the minimum swaps

 cout << cnt << endl;

}

 

// Driver Code

signed main()

{

 // Given Number N

 int N = 9;

 

 // Given Permutation of N numbers

 vector<int> P = { 1, 2, 4, 9, 5,

 8, 7, 3, 6 };

 

 // Function Call

 solve(P, N);

 

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

// Java program for the above approach

import java.io.*; 

 

class GFG{ 

 

// Function to find the minimum

// number of swaps

static void solve(int P[], int n)

{

 

 // New array to convert

 // to 1-based indexing

 int arr[] = new int[n + 1];

 

 arr[0] = 0;

 

 for(int i = 0; i < n; i++)

 arr[i + 1] = P[i];

 

 // Keeps count of swaps

 int cnt = 0;

 

 for(int i = 1; i < n; i++)

 {

 

 // Check if it is an 'X' position

 if (arr[i] == i)

 {

 int t = arr[i + 1];

 arr[i + 1] = arr[i];

 arr[i] = t;

 cnt++;

 }

 }

 

 // Corner Case

 if (arr[n] == n)

 {

 

 // Swap

 int t = arr[n - 1];

 arr[n - 1] = arr[n];

 arr[n] = t;

 cnt++;

 }

 

 // Print the minimum swaps

 System.out.println(cnt);

}

 

// Driver code

public static void main(String[] args) 

{ 

 

 // Given Number N

 int N = 9;

 

 // Given Permutation of N numbers

 int P[] = new int[]{ 1, 2, 4, 9, 5,

 8, 7, 3, 6 };

 

 // Function Call

 solve(P, N);

} 

} 

 

// This code is contributed by Pratima Pandey  
  
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

# Python3 program for the above approach

 

# Function to find the minimum

# number of swaps

def solve(P, n):

 

 # New array to convert

 # to 1-based indexing

 arr = []

 

 arr.append(0)

 

 for x in P:

 arr.append(x)

 

 # Keeps count of swaps

 cnt = 0

 

 for i in range(1, n):

 

 # Check if it is an 'X' position

 if (arr[i] == i):

 arr[i], arr[i + 1] = arr[i + 1], arr[i]

 cnt += 1

 

 # Corner Case

 if (arr[n] == n):

 arr[n - 1], arr[n] = arr[n] , arr[n - 1]

 cnt += 1

 

 # Print the minimum swaps

 print(cnt)

 

# Driver Code

 

# Given number N

N = 9

 

# Given permutation of N numbers

P = [ 1, 2, 4, 9, 5,

 8, 7, 3, 6 ]

 

# Function call

solve(P, N)

 

# This code is contributed by chitranayal  
  
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

// C# program for the above approach

using System;

 

class GFG{ 

 

// Function to find the minimum 

// number of swaps 

static void solve(int []P, int n) 

{ 

 

 // New array to convert 

 // to 1-based indexing 

 int []arr = new int[n + 1]; 

 

 arr[0] = 0; 

 

 for(int i = 0; i < n; i++) 

 arr[i + 1] = P[i]; 

 

 // Keeps count of swaps 

 int cnt = 0; 

 

 for(int i = 1; i < n; i++) 

 { 

 

 // Check if it is an 'X' position 

 if (arr[i] == i) 

 { 

 int t = arr[i + 1]; 

 arr[i + 1] = arr[i]; 

 arr[i] = t; 

 cnt++; 

 } 

 } 

 

 // Corner Case 

 if (arr[n] == n) 

 { 

 

 // Swap 

 int t = arr[n - 1]; 

 arr[n - 1] = arr[n]; 

 arr[n] = t; 

 cnt++; 

 } 

 

 // Print the minimum swaps 

 Console.WriteLine(cnt); 

} 

 

// Driver code 

public static void Main(String[] args) 

{ 

 

 // Given Number N 

 int N = 9; 

 

 // Given Permutation of N numbers 

 int []P = { 1, 2, 4, 9, 5, 

 8, 7, 3, 6 }; 

 

 // Function Call 

 solve(P, N); 

} 

} 

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time Complexity:** _O(N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

