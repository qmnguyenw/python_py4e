Number of subarrays with GCD = 1 | Segment tree



Given an array **arr[]** , the task is to find the count of sub-arrays with
GCD equal to **1**.

 **Examples:**

>  **Input:** arr[] = {1, 1, 1}  
>  **Output:** 6  
> Every single subarray of the given array has GCD  
> of 1 and there are a total of 6 subarrays.
>
>  **Input:** arr[] = {2, 2, 2}  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can be solved in **O(NlogN)** using segment-tree
data structure. The segment that will be built can be used to answer range-gcd
queries.

  

  

Let’s understand the algorithm now. Use the two-pointer technique to solve
this problem. Let’s make a few observations before discussing the algorithm.

  * Let’s say **G** is the GCD of the subarray **arr[l…r]** and **G1** is the GCD of the subarray **arr[l+1…r]**. **G** smaller than or equal to **G1** always.
  * Let’s say for the given **L1** , **R1** is the first index such that GCD of the range **[L, R]** is **1** then for any **L2** greater than or equal to **L1** , **R2** will also be greater than or equal to **R1**.

After the above observation, two-pointer technique makes perfect sense i.e. if
the length  
of the smallest **R** is known for an index **L** then for an index **L + 1**
, the search needs to be started from **R** on-wards.

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

#define maxLen 30

 

// Array to store segment-tree

int seg[3 * maxLen];

 

// Function to build segment-tree to

// answer range GCD queries

int build(int l, int r, int in, int* arr)

{

 // Base-case

 if (l == r)

 return seg[in] = arr[l];

 

 // Mid element of the range

 int mid = (l + r) / 2;

 

 // Merging the result of left and right sub-tree

 return seg[in] = __gcd(build(l, mid, 2 * in + 1, arr),

 build(mid + 1, r, 2 * in + 2, arr));

}

 

// Function to perform range GCD queries

int query(int l, int r, int l1, int r1, int in)

{

 // Base-cases

 if (l1 <= l and r <= r1)

 return seg[in];

 if (l > r1 or r < l1)

 return 0;

 

 // Mid-element

 int mid = (l + r) / 2;

 

 // Calling left and right child

 return __gcd(query(l, mid, l1, r1, 2 * in + 1),

 query(mid + 1, r, l1, r1, 2 * in + 2));

}

 

// Function to find the required count

int findCnt(int* arr, int n)

{

 // Building the segment tree

 build(0, n - 1, 0, arr);

 

 // Two pointer variables

 int i = 0, j = 0;

 

 // To store the final answer

 int ans = 0;

 

 // Looping

 while (i < n) {

 

 // Incrementing j till we don't get

 // a gcd value of 1

 while (j < n and query(0, n - 1, i, j, 0) != 1)

 j++;

 

 // Updating the final answer

 ans += (n - j);

 

 // Increment i

 i++;

 

 // Update j

 j = max(j, i);

 }

 

 // Returning the final answer

 return ans;

}

 

// Driver code

int main()

{

 int arr[] = { 1, 1, 1, 1 };

 int n = sizeof(arr) / sizeof(int);

 

 cout << findCnt(arr, n);

 

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

// Java implementation of the above approach

class GFG

{

static int maxLen = 30;

 

// Array to store segment-tree

static int []seg = new int[3 * maxLen];

 

// Function to build segment-tree to

// answer range GCD queries

static int build(int l, int r, 

 int in, int[] arr)

{

 // Base-case

 if (l == r)

 return seg[in] = arr[l];

 

 // Mid element of the range

 int mid = (l + r) / 2;

 

 // Merging the result of left and right sub-tree

 return seg[in] = __gcd(build(l, mid, 2 * in + 1, arr),

 build(mid + 1, r, 2 * in + 2, arr));

}

 

// Function to perform range GCD queries

static int query(int l, int r, int l1, 

 int r1, int in)

{

 // Base-cases

 if (l1 <= l && r <= r1)

 return seg[in];

 if (l > r1 || r < l1)

 return 0;

 

 // Mid-element

 int mid = (l + r) / 2;

 

 // Calling left and right child

 return __gcd(query(l, mid, l1, r1, 2 * in + 1),

 query(mid + 1, r, l1, r1, 2 * in + 2));

}

 

// Function to find the required count

static int findCnt(int[] arr, int n)

{

 // Building the segment tree

 build(0, n - 1, 0, arr);

 

 // Two pointer variables

 int i = 0, j = 0;

 

 // To store the final answer

 int ans = 0;

 

 // Looping

 while (i < n)

 {

 

 // Incrementing j till we don't get

 // a gcd value of 1

 while (j < n && query(0, n - 1, 

 i, j, 0) != 1)

 j++;

 

 // Updating the final answer

 ans += (n - j);

 

 // Increment i

 i++;

 

 // Update j

 j = Math.max(j, i);

 }

 

 // Returning the final answer

 return ans;

}

 

static int __gcd(int a, int b) 

{ 

 return b == 0 ? a : __gcd(b, a % b); 

}

 

// Driver code

public static void main(String []args) 

{

 int arr[] = { 1, 1, 1, 1 };

 int n = arr.length;

 

 System.out.println(findCnt(arr, n));

}

}

 

// This code is contributed by PrinciRaj1992  
  
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

# Python3 implementation of the above approach

from math import gcd

 

maxLen = 30;

 

# Array to store segment-tree 

seg = [0] * (3 * maxLen); 

 

# Function to build segment-tree to 

# answer range GCD queries 

def build(l, r, i, arr) :

 

 # Base-case 

 if (l == r) :

 seg[i] = arr[l]; 

 return seg[i];

 

 # Mid element of the range 

 mid = (l + r) // 2; 

 

 # Merging the result of left and right sub-tree 

 seg[i] = gcd(build(l, mid, 2 * i + 1, arr),

 build(mid + 1, r, 2 * i + 2, arr)); 

 return seg[i];

 

# Function to perform range GCD queries 

def query(l, r, l1, r1, i) :

 

 # Base-cases 

 if (l1 <= l and r <= r1) :

 return seg[i]; 

 

 if (l > r1 or r < l1) :

 return 0; 

 

 # Mid-element 

 mid = (l + r) // 2; 

 

 # Calling left and right child 

 return gcd(query(l, mid, l1, r1, 2 * i + 1), 

 query(mid + 1, r, l1, r1, 2 * i + 2)); 

 

# Function to find the required count 

def findCnt(arr, n) : 

 

 # Building the segment tree 

 build(0, n - 1, 0, arr); 

 

 # Two pointer variables 

 i = 0; j = 0; 

 

 # To store the final answer 

 ans = 0; 

 

 # Looping 

 while (i < n) :

 

 # Incrementing j till we don't get 

 # a gcd value of 1 

 while (j < n and

 query(0, n - 1, i, j, 0) != 1) :

 j += 1; 

 

 # Updating the final answer 

 ans += (n - j); 

 

 # Increment i 

 i += 1; 

 

 # Update j 

 j = max(j, i); 

 

 # Returning the final answer 

 return ans; 

 

# Driver code 

if __name__ == "__main__" :

 

 arr = [ 1, 1, 1, 1 ]; 

 n = len(arr); 

 

 print(findCnt(arr, n)); 

 

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

// C# implementation of the above approach

using System;

 

class GFG

{

static int maxLen = 30;

 

// Array to store segment-tree

static int []seg = new int[3 * maxLen];

 

// Function to build segment-tree to

// answer range GCD queries

static int build(int l, int r, 

 int iN, int[] arr)

{

 // Base-case

 if (l == r)

 return seg[iN] = arr[l];

 

 // Mid element of the range

 int mid = (l + r) / 2;

 

 // Merging the result of left and right sub-tree

 return seg[iN] = __gcd(build(l, mid, 2 * iN + 1, arr),

 build(mid + 1, r, 2 * iN + 2, arr));

}

 

// Function to perform range GCD queries

static int query(int l, int r, int l1, 

 int r1, int iN)

{

 // Base-cases

 if (l1 <= l && r <= r1)

 return seg[iN];

 if (l > r1 || r < l1)

 return 0;

 

 // Mid-element

 int mid = (l + r) / 2;

 

 // Calling left and right child

 return __gcd(query(l, mid, l1, r1, 2 * iN + 1),

 query(mid + 1, r, l1, r1, 2 * iN + 2));

}

 

// Function to find the required count

static int findCnt(int[] arr, int n)

{

 // Building the segment tree

 build(0, n - 1, 0, arr);

 

 // Two pointer variables

 int i = 0, j = 0;

 

 // To store the final answer

 int ans = 0;

 

 // Looping

 while (i < n)

 {

 

 // Incrementing j till we don't get

 // a gcd value of 1

 while (j < n && query(0, n - 1, 

 i, j, 0) != 1)

 j++;

 

 // Updating the final answer

 ans += (n - j);

 

 // Increment i

 i++;

 

 // Update j

 j = Math.Max(j, i);

 }

 

 // Returning the final answer

 return ans;

}

 

static int __gcd(int a, int b) 

{ 

 return b == 0 ? a : __gcd(b, a % b); 

}

 

// Driver code

public static void Main(String []args) 

{

 int []arr = { 1, 1, 1, 1 };

 int n = arr.Length;

 

 Console.WriteLine(findCnt(arr, n));

}

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    10
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

