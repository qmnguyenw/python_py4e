Query to count odd and even parity elements in subarray after XOR with K



Given an array **arr[]** consisting of **N** elements and **Q** queries
represented by **L** , **R** , and **K**. The task is to print the count of
odd and even parity elements in the subarray **[L, R]** after Bitwise-XOR with
K.

 **Examples:**

> **Input:** arr[] = {5, 2, 3, 1, 4, 8, 10}  
> query[] = {{0, 5, 3}, {1, 4, 8}, {4, 6, 10}}  
> **Output:**  
> 4 2  
> 1 3  
> 2 1  
> **Explanation:**  
> In query 1, the odd and even parity elements in subarray [0:5] are [2, 1, 4,
> 8] and [5, 3]. Now after XOR with K = 3, the number of odd and even parity
> elements are 4 and 2 respectively.  
> In query 2, the odd and even parity elements in subarray [1:4] are [2, 1, 4]
> and [3]. Now after XOR with K = 8, the number of odd and even parity
> elements are 1 and 3 respectively.  
> In query 3, the odd and even parity elements in subarray [4:6] are [4, 8]
> and [10]. Now after XOR with K = 10, the number of odd and even parity
> elements are 2 and 1 respectively.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to use MO’s algorithm to pre-process all queries so
that result of one query can be used in the next query.

  * Sort all queries in a way that queries with L values from **0 to √n – 1** are put together, followed by queries from **√n to 2 ×√n – 1** , and so on. All queries within a block are sorted in increasing order of R values.
  * Count the **odd parity** elements and then calculate the **even parity** elements as

![\(R - L + 1- odd parity elements\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-5d75aba2805c18ab6d3b47322dc0236a_l3.png)

  

  

  * Observation after XOR with odd and even parity elements: 
    * XOR of **two odd parity** elements is an **even parity** element.
    * XOR of **two even parity** elements is an **even parity** element.
    * XOR of **one even parity** element and **another odd parity** element is an **odd parity** element and vice-versa.
  * Process all queries one by one and increase the count of odd parity elements and now we will **check the parity of K**. If **K** has an **even parity** then the count of **odd** and **even parity** remains the **same** else we **swap** them. 
    * Let **count_oddP** store the count of odd parity elements in previous query.
    * Remove extra elements of previous query and add new elements for the current query. For example, if previous query was [0, 8] and the current query is [3, 9], then remove the elements arr[0], arr[1] and arr[2] and add arr[9].
  * In order to display the results, sort the queries in the order they were provided.

 **Adding elements**

  * If the current element has odd parity then increase the count of odd parity.

 **Removing elements**

  * If the current element has odd parity then decrease the count of odd parity.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count odd and

// even parity elements in subarray

// after XOR with K

#include <bits/stdc++.h>

using namespace std;

#define MAX 100000

// Variable to represent block size.

// This is made global so compare()

// of sort can use it

int block;

// Structure to represent

// a query range

struct Query {

 // Starting index

 int L, R, K, index;

 // Count of odd

 // parity elements

 int odd;

 // Count of even

 // parity elements

 int even;

};

// To store the count of

// odd parity elements

int count_oddP;

// Function used to sort all queries so that

// all queries of the same block are arranged

// together and within a block, queries are

// sorted in increasing order of R values.

bool compare(Query x, Query y)

{

 // Different blocks, sort by block.

 if (x.L / block != y.L / block)

 return x.L / block < y.L / block;

 // Same block, sort by R value

 return x.R < y.R;

}

// Function used to sort all queries

// in order of their index value so

// that results of queries can be

// printed in same order as of input

bool compare1(Query x, Query y)

{

 return x.index < y.index;

}

// Function to Add elements

// of current range

void add(int currL, int a[])

{

 // _builtin_parity(x)returns true(1)

 // if the number has odd parity else

 // it returns false(0) for even parity.

 if (__builtin_parity(a[currL]))

 count_oddP++;

}

// Function to remove elements

// of previous range

void remove(int currR, int a[])

{

 // _builtin_parity(x)returns true(1)

 // if the number has odd parity else

 // it returns false(0) for even parity.

 if (__builtin_parity(a[currR]))

 count_oddP--;

}

// Function to generate the result of queries

void queryResults(int a[], int n, Query q[],

 int m)

{

 // Initialize number of odd parity

 // elements to 0

 count_oddP = 0;

 // Find block size

 block = (int)sqrt(n);

 // Sort all queries so that queries of

 // same blocks are arranged together.

 sort(q, q + m, compare);

 // Initialize current L, current R and

 // current result

 int currL = 0, currR = 0;

 for (int i = 0; i < m; i++) {

 // L and R values of current range

 int L = q[i].L,

 R = q[i].R,

 k = q[i].K;

 // Add Elements of current range

 while (currR <= R) {

 add(currR, a);

 currR++;

 }

 while (currL > L) {

 add(currL - 1, a);

 currL--;

 }

 // Remove element of previous range

 while (currR > R + 1)

 {

 remove(currR - 1, a);

 currR--;

 }

 while (currL < L) {

 remove(currL, a);

 currL++;

 }

 // If parity of K is even

 // then the count of odd

 // and even parity remains

 // the same

 if (!__builtin_parity(k)) {

 q[i].odd = count_oddP;

 q[i].even

 = R - L + 1 - count_oddP;

 }

 // If parity of K is odd

 // we swap the count of

 // odd and even parity

 // elements

 else {

 q[i].odd

 = R - L + 1 - count_oddP;

 q[i].even = count_oddP;

 }

 }

}

// Function to display the results of

// queries in their initial order

void printResults(Query q[], int m)

{

 sort(q, q + m, compare1);

 for (int i = 0; i < m; i++) {

 cout << q[i].odd << " "

 << q[i].even << endl;

 }

}

// Driver Code

int main()

{

 int arr[] = { 5, 2, 3, 1, 4, 8, 10 };

 int n = sizeof(arr) / sizeof(arr[0]);

 Query q[] = { { 0, 5, 3, 0, 0, 0 },

 { 1, 4, 8, 1, 0, 0 },

 { 4, 6, 10, 2, 0, 0 } };

 int m = sizeof(q) / sizeof(q[0]);

 queryResults(arr, n, q, m);

 printResults(q, m);

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

// Java program to count odd and

// even parity elements in subarray

// after XOR with K

import java.io.*;

import java.util.*;

// Class to represent

// a query range

class Query

{

 int L, R, K, index;

 // Count of odd

 // parity elements

 int odd;

 // Count of even

 // parity elements

 int even;

 Query(int L, int R, int K,

 int index, int odd, int even)

 {

 this.L = L;

 this.R = R;

 this.K = K;

 this.index = index;

 this.odd = odd;

 this.even = even;

 }

}

class GFG{

// Variable to represent block size.

static int block;

// To store the count of

// odd parity elements

static int count_oddP;

// Function to Add elements

// of current range

static void add(int currL, int a[])

{

 

 // _builtin_parity(x)returns true

 // if the number has odd parity else

 // it returns false for even parity.

 if (__builtin_parity(a[currL]))

 count_oddP++;

}

// Function to remove elements

// of previous range

static void remove(int currR, int a[])

{

 

 // _builtin_parity(x)returns true

 // if the number has odd parity else

 // it returns false for even parity.

 if (__builtin_parity(a[currR]))

 count_oddP--;

}

// Function to generate the result of queries

static void queryResults(int a[], int n, Query q[],

 int m)

{

 

 // Initialize number of odd parity

 // elements to 0

 count_oddP = 0;

 // Find block size

 block = (int)(Math.sqrt(n));

 // sort all queries so that all queries

 // of the same block are arranged together

 // and within a block, queries are sorted

 // in increasing order of R values.

 Arrays.sort(q, (Query x, Query y) ->

 {

 

 // Different blocks, sort by block.

 if (x.L / block != y.L / block)

 return x.L / block - y.L / block;

 // Same block, sort by R value

 return x.R - y.R;

 });

 // Initialize current L, current R and

 // current result

 int currL = 0, currR = 0;

 for(int i = 0; i < m; i++)

 {

 

 // L and R values of current range

 int L = q[i].L, R = q[i].R, k = q[i].K;

 // Add Elements of current range

 while (currR <= R)

 {

 add(currR, a);

 currR++;

 }

 while (currL > L)

 {

 add(currL - 1, a);

 currL--;

 }

 // Remove element of previous range

 while (currR > R + 1)

 {

 remove(currR - 1, a);

 currR--;

 }

 while (currL < L)

 {

 remove(currL, a);

 currL++;

 }

 // If parity of K is even

 // then the count of odd

 // and even parity remains

 // the same

 if (!__builtin_parity(k))

 {

 q[i].odd = count_oddP;

 q[i].even = R - L + 1 - count_oddP;

 }

 

 // If parity of K is odd

 // we swap the count of

 // odd and even parity

 // elements

 else

 {

 q[i].odd = R - L + 1 - count_oddP;

 q[i].even = count_oddP;

 }

 }

}

static boolean __builtin_parity(int K)

{

 return (Integer.bitCount(K) % 2) == 1;

}

// Function to display the results of

// queries in their initial order

static void printResults(Query q[], int m)

{

 Arrays.sort(q, (Query x, Query y) ->

 // sort all queries

 // in order of their

 // index value so that results

 // of queries can be printed

 // in same order as of input);

 x.index - y.index);

 for(int i = 0; i < m; i++)

 {

 System.out.println(q[i].odd + " " +

 q[i].even);

 }

}

// Driver Code

public static void main(String[] args)

{

 int arr[] = { 5, 2, 3, 1, 4, 8, 10 };

 int n = arr.length;

 Query q[] = new Query[3];

 q[0] = new Query(0, 5, 3, 0, 0, 0);

 q[1] = new Query(1, 4, 8, 1, 0, 0);

 q[2] = new Query(4, 6, 10, 2, 0, 0);

 int m = q.length;

 queryResults(arr, n, q, m);

 printResults(q, m);

}

}

// This code is contributed by jithin  
  
---  
  
 __

 __

 **Output:**

    
    
    4 2
    1 3
    2 1

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

