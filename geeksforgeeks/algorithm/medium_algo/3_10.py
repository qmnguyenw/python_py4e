Queries for elements having values within the range A to B using MO’s
Algorithm



 **Prerequisites:** MO’s algorithm, SQRT Decomposition

Given an array **arr[]** of **N** elements and two integers **A** to **B** ,
the task is to answer Q queries each having two integers **L** and **R.** For
each query, find the number of elements in the subarray **arr[L, R]** which
lies within the range **A** to **B** (inclusive).

 **Examples:**

>  **Input:** arr[] = {3, 4, 6, 2, 7, 1}, A = 1, B = 6, query = {0, 4}  
>  **Output:** 4  
>  **Explanation:**  
>  All 3, 4, 6, 2 lies within 1 to 6 in the subarray {3, 4, 6, 2}  
> Therefore, the count of such elements is 4.
>
>  **Input:** arr[] = {0, 1, 2, 3, 4, 5, 6, 7}, A = 1, B = 5, query = {3, 5}  
>  **Output:** 3  
>  **Explanation:**  
>  All the elements 3, 4 and 5 lies within the range 1 to 5 in the subarray
> {3, 4, 5}.  
> Therefore, the count of such elements is 3.
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use MO’s algorithm to pre-process all queries so
that result of one query can be used in the next query. Below is the
illustration of the steps:

  1. Group the queries into mutiple chunks where each chunk contains the values of starting range in (0 to √N – 1), (√N to 2x√N – 1) and so on. Sort the queries within a chunk in incresing order of **R**.
  2. Process all queries one by one in a way that every query uses result computed in the previous query.
  3. Maintain the frequency array that will count the frequency of arr[i] as they appear in the range [L, R].

 **For example:**

> arr[] = [3, 4, 6, 2, 7, 1], L = 0, R = 4 and A = 1, B = 6
>
> Initially frequency array is initialized to 0 i.e freq[]=[0….0]  
>  **Step 1:** Add arr[0] and increment its frequency as freq[arr[0]]++  
> i.e freq[3]++ and freq[]=[0, 0, 0, 1, 0, 0, 0, 0]
>
>  **Step 2:** Add arr[1] and increment freq[arr[1]]++  
> i.e freq[4]++ and freq[]=[0, 0, 0, 1, 1, 0, 0, 0]
>
>  **Step 3:** Add arr[2] and increment freq[arr[2]]++  
> i.e freq[6]++ and freq[]=[0, 0, 0, 1, 1, 0, 1, 0]
>
>  **Step 4:** Add arr[3] and increment freq[arr[3]]++  
> i.e freq[2]++ and freq[]=[0, 0, 1, 1, 1, 0, 1, 0]
>
>  **Step 5:** Add arr[4] and increment freq[arr[4]]++  
> i.e freq[7]++ and freq[]=[0, 0, 1, 1, 1, 0, 1, 1]
>
>  
>
>
>  
>
>
>  **Step 6:** Now we need to find the numbers of elements between A and B.
>
>  **Step 7:** The answer is equal to ![ \\sum_{i=A}^B freq\[i\]
> ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-45fe17e8bc5a4767c5de6ad6db752536_l3.png)

To calculate the sum in **Step 7,** we cannot do iteration because that would
lead to **O(N)** time complexity per query. So we will use **square root
decomposition technique** to find the sum, whose time complexity is **O(√N)**
per query.

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

// values in the range A to B

// in a subarray of L to R

 

#include <bits/stdc++.h>

using namespace std;

 

#define MAX 100001

#define SQRSIZE 400

 

// Variable to represent block size.

// This is made global so compare()

// of sort can use it.

int query_blk_sz;

 

// Structure to represent a query range

struct Query {

 int L;

 int R;

};

 

// Frequency array

// to keep count of elements

int frequency[MAX];

 

// Array which contains the frequency

// of a particular block

int blocks[SQRSIZE];

 

// Block size

int blk_sz;

 

// Function used to sort all queries

// so that all queries of the same

// block are arranged together and

// within a block, queries are sorted

// in increasing order of R values.

bool compare(Query x, Query y)

{

 if (x.L / query_blk_sz

 != y.L / query_blk_sz)

 return (x.L / query_blk_sz

 < y.L / query_blk_sz);

 

 return x.R < y.R;

}

 

// Function used to get the block

// number of current a[i] i.e ind

int getblocknumber(int ind)

{

 return (ind) / blk_sz;

}

 

// Function to get the answer

// of range [0, k] which uses the

// sqrt decompostion technique

int getans(int A, int B)

{

 int ans = 0;

 int left_blk, right_blk;

 left_blk = getblocknumber(A);

 right_blk = getblocknumber(B);

 

 // If left block is equal to rigth block

 // then we can traverse that block

 if (left_blk == right_blk) {

 for (int i = A; i <= B; i++)

 ans += frequency[i];

 }

 else {

 // Traversing first block in

 // range

 for (int i = A;

 i < (left_blk + 1) * blk_sz;

 i++)

 ans += frequency[i];

 

 // Traversing completely overlapped

 // blocks in range

 for (int i = left_blk + 1;

 i < right_blk; i++)

 ans += blocks[i];

 

 // Traversing last block in range

 for (int i = right_blk * blk_sz;

 i <= B; i++)

 ans += frequency[i];

 }

 return ans;

}

 

void add(int ind, int a[])

{

 // Increment the frequency of a[ind]

 // in the frequency array

 frequency[a[ind]]++;

 

 // Get the block number of a[ind]

 // to update the result in blocks

 int block_num = getblocknumber(a[ind]);

 

 blocks[block_num]++;

}

 

void remove(int ind, int a[])

{

 // Decrement the frequency of

 // a[ind] in the frequency array

 frequency[a[ind]]--;

 

 // Get the block number of a[ind]

 // to update the result in blocks

 int block_num = getblocknumber(a[ind]);

 

 blocks[block_num]--;

}

void queryResults(int a[], int n,

 Query q[], int m,

 int A, int B)

{

 

 // Initialize the block size

 // for queries

 query_blk_sz = sqrt(m);

 

 // Sort all queries so that queries

 // of same blocks are arranged

 // together.

 sort(q, q + m, compare);

 

 // Initialize current L,

 // current R and current result

 int currL = 0, currR = 0;

 

 for (int i = 0; i < m; i++) {

 

 // L and R values of the

 // current range

 

 int L = q[i].L, R = q[i].R;

 

 // Add Elements of current

 // range

 while (currR <= R) {

 add(currR, a);

 currR++;

 }

 while (currL > L) {

 add(currL - 1, a);

 currL--;

 }

 

 // Remove element of previous

 // range

 while (currR > R + 1)

 

 {

 remove(currR - 1, a);

 currR--;

 }

 while (currL < L) {

 remove(currL, a);

 currL++;

 }

 printf("%d\n", getans(A, B));

 }

}

 

// Driver code

int main()

{

 

 int arr[] = { 3, 4, 6, 2, 7, 1 };

 int N = sizeof(arr) / sizeof(arr[0]);

 

 int A = 1, B = 6;

 blk_sz = sqrt(N);

 Query Q[] = { { 0, 4 } };

 

 int M = sizeof(Q) / sizeof(Q[0]);

 

 // Answer the queries

 queryResults(arr, N, Q, M, A, B);

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

**Time Complexity:** O(Q*√N)  
 **Space Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

