Smallest index in given range of indices which is not equal to X



Given an integer array **arr[]** of size **N** , and **Q** queries of the form
of **{L, R, X}** , the task is to find the smallest index between **L** and
**R** from the given array such that **arr[i] != X**. If no such index exists
in array, print **-1**.

 **Examples:**

>  **Input:** arr[] = {1, 2, 1, 1, 3, 5}, query[][] = {{0, 3, 1}, {1, 5, 2},
> {2, 3, 1}}  
> **Output:** 1  
> 2  
> -1  
> **Explanation:**  
> The first index from 0 to 3 which does not contain 1 is 1  
> The first index from 1 to 5 which does not contain 2 is 2  
> All the indices from 2 to 3 contain 1. Hence, the answer is -1.
>
>  **Input:** arr[] = { 1, 2, 3, 2, 1, 1, 3, 5}, query[][] = { { 1, 4, 2 }, {
> 4, 5, 1 }, { 2, 3, 1 }, { 4, 6, 1 }}  
> **Output:** 2  
> -1  
> 2  
> 6

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**  
Iterate over the range **[L, R]** for every query and check if any index
exists which does not contain **X**. If such an index is found, print that
index. Otherwise, print **-1**.

  

  

_**Time Complexity:** O (N * Q)_  
_**Auxiliary Space:** O (1)_

 **Efficient Approach:**  
The above approach can be further optimized by precomputing and storing the
index of the next element which is different from the current element, for
every array element, which reduces computational complexity to O(1) for every
query.  
Follow the steps below to solve the problem:

  1. Create an auxiliary array **nextpos[]** to store for every array element, the index of the next element which is different from the current element.
  2. Now to process every query, firstly check if the value at index **L** is not equal to **X**. If so, then the answer will be **L**.
  3. Otherwise, it means that **arr[L] = X**. In this case, we need to find the next index which has a value different from **arr[L]**. This can be obtained from **nextpos[L]**.
  4. If **nextpos[L]** is less than equal to **R** , then print nexpos[L].
  5. If neither of the above conditions are satisfied, then answer will be **-1**.

 **Illustration:**

> arr[] = {1, 2, 1, 1, 3, 5}, query[][] = {{0, 3, 1}, {1, 5, 2}, {2, 3, 1}}  
> For the given arr[], nextpos[] array will be {1, 2, 4, 4, 5, 6}  
> For 1st Query: L = 0, R = 3, X = 1  
> arr[0] = 1 = X  
> nextpos[0] = 1( < 3)  
> Hence, the answer is 1.  
> For the 2nd Query: L = 1, R = 5, X = 2  
> arr[1] = 2( = X)  
> nextpos[1] = 2( < 5)  
> Hence, the answer is 2.  
> For the 3rd Query: L = 2, R = 3, X = 1  
> arr[2] = 1( = X)  
> nextpos[2] = 4( > R)  
> Hence, the answer is -1

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to find the smallest

// index in the array in the range

// [L, R] which does not contain X

#include <bits/stdc++.h>

using namespace std;

// Precompute the index of next

// different element in the array

// for every array element

void precompute(int nextpos[], int arr[],

 int N)

{

 // Default value

 nextpos[N - 1] = N;

 for (int i = N - 2; i >= 0; i--) {

 // Compute nextpos[i] using

 // nextpos[i+1]

 if (arr[i] == arr[i + 1])

 nextpos[i] = nextpos[i + 1];

 else

 nextpos[i] = i + 1;

 }

}

// Function to return the smallest index

void findIndex(int query[][3], int arr[],

 int N, int Q)

{

 // nextpos[i] will store the next

 // position p where arr[p]!=arr[i]

 int nextpos[N];

 precompute(nextpos, arr, N);

 for (int i = 0; i < Q; i++) {

 int l, r, x;

 l = query[i][0];

 r = query[i][1];

 x = query[i][2];

 int ans = -1;

 // If X is not present at l

 if (arr[l] != x)

 ans = l;

 // Otherwise

 else {

 // Find the index which

 // stores a value different

 // from X

 int d = nextpos[l];

 // If that index is within

 // the range

 if (d <= r)

 ans = d;

 }

 cout << ans << "\n";

 }

}

// Driver Code

int main()

{

 int N, Q;

 N = 6;

 Q = 3;

 int arr[] = { 1, 2, 1, 1, 3, 5 };

 int query[Q][3] = { { 0, 3, 1 },

 { 1, 5, 2 },

 { 2, 3, 1 } };

 findIndex(query, arr, N, Q);

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

// Java program to find the smallest

// index in the array in the range

// [L, R] which does not contain X

class GFG{

// Precompute the index of next

// different element in the array

// for every array element

static void precompute(int nextpos[], int arr[],

 int N)

{

 

 // Default value

 nextpos[N - 1] = N;

 for(int i = N - 2; i >= 0; i--)

 {

 

 // Compute nextpos[i] using

 // nextpos[i+1]

 if (arr[i] == arr[i + 1])

 nextpos[i] = nextpos[i + 1];

 else

 nextpos[i] = i + 1;

 }

}

// Function to return the smallest index

static void findIndex(int query[][], int arr[],

 int N, int Q)

{

 

 // nextpos[i] will store the next

 // position p where arr[p]!=arr[i]

 int []nextpos = new int[N];

 precompute(nextpos, arr, N);

 for(int i = 0; i < Q; i++)

 {

 int l, r, x;

 l = query[i][0];

 r = query[i][1];

 x = query[i][2];

 

 int ans = -1;

 

 // If X is not present at l

 if (arr[l] != x)

 ans = l;

 

 // Otherwise

 else

 {

 

 // Find the index which

 // stores a value different

 // from X

 int d = nextpos[l];

 

 // If that index is within

 // the range

 if (d <= r)

 ans = d;

 }

 System.out.print(ans + "\n");

 }

}

// Driver Code

public static void main(String[] args)

{

 int N, Q;

 N = 6;

 Q = 3;

 int arr[] = { 1, 2, 1, 1, 3, 5 };

 int query[][] = { { 0, 3, 1 },

 { 1, 5, 2 },

 { 2, 3, 1 } };

 findIndex(query, arr, N, Q);

}

}

// This code is contributed by Amit Katiyar  
  
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

# Python3 program to find the smallest

# index in the array in the range

# [L, R] which does not contain X

# Precompute the index of next

# different element in the array

# for every array element

def precompute(nextpos, arr, N):

 # Default value

 nextpos[N - 1] = N

 

 for i in range(N - 2, -1, -1):

 

 # Compute nextpos[i] using

 # nextpos[i+1]

 if arr[i] == arr[i + 1]:

 nextpos[i] = nextpos[i + 1]

 else:

 nextpos[i] = i + 1

# Function to return the smallest index

def findIndex(query, arr, N, Q):

 # nextpos[i] will store the next

 # position p where arr[p]!=arr[i]

 nextpos = [0] * N

 precompute(nextpos, arr, N)

 

 for i in range(Q):

 l = query[i][0]

 r = query[i][1]

 x = query[i][2]

 

 ans = -1

 

 # If X is not present at l

 if arr[l] != x:

 ans = l

 

 # Otherwise

 else:

 

 # Find the index which

 # stores a value different

 # from X

 d = nextpos[l]

 

 # If that index is within

 # the range

 if d <= r:

 ans = d

 

 print(ans)

 

# Driver code 

N = 6

Q = 3

arr = [ 1, 2, 1, 1, 3, 5 ]

query = [ [ 0, 3, 1 ],

 [ 1, 5, 2 ],

 [ 2, 3, 1 ] ]

findIndex(query, arr, N, Q)

# This code is contributed by divyeshrabadiya07  
  
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

// C# program to find the smallest

// index in the array in the range

// [L, R] which does not contain X

using System;

class GFG{

// Precompute the index of next

// different element in the array

// for every array element

static void precompute(int []nextpos,

 int []arr, int N)

{

 

 // Default value

 nextpos[N - 1] = N;

 for(int i = N - 2; i >= 0; i--)

 {

 

 // Compute nextpos[i] using

 // nextpos[i+1]

 if (arr[i] == arr[i + 1])

 nextpos[i] = nextpos[i + 1];

 else

 nextpos[i] = i + 1;

 }

}

// Function to return the smallest index

static void findIndex(int [,]query, int []arr,

 int N, int Q)

{

 

 // nextpos[i] will store the next

 // position p where arr[p]!=arr[i]

 int []nextpos = new int[N];

 precompute(nextpos, arr, N);

 for(int i = 0; i < Q; i++)

 {

 int l, r, x;

 l = query[i, 0];

 r = query[i, 1];

 x = query[i, 2];

 

 int ans = -1;

 

 // If X is not present at l

 if (arr[l] != x)

 ans = l;

 

 // Otherwise

 else

 {

 

 // Find the index which

 // stores a value different

 // from X

 int d = nextpos[l];

 

 // If that index is within

 // the range

 if (d <= r)

 ans = d;

 }

 Console.Write(ans + "\n");

 }

}

// Driver Code

public static void Main(String[] args)

{

 int N, Q;

 N = 6;

 Q = 3;

 int []arr = { 1, 2, 1, 1, 3, 5 };

 int [,]query = { { 0, 3, 1 },

 { 1, 5, 2 },

 { 2, 3, 1 } };

 findIndex(query, arr, N, Q);

}

}

// This code is contributed by Amit Katiyar  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    2
    -1
    
    

_**Time Complexity:** O(N)_  
_**Auxiliary Space:** O(N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

