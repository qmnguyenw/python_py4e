Queries for number of array elements in a range with Kth Bit Set



Given an array of **N** positive (32-bit)integers, the task is to answer **Q**
queries of the following form:

    
    
    Query(L, R, K): Print the number of elements of the array in the 
                    range **L** to **R** , which have their **K** th bit as set

 **Note** : Consider **LSB** to be indexed at **1**.

 **Examples:**

> **Input** : arr[] = { 8, 9, 1, 3 }  
> Query 1: L = 1, R = 3, K = 4  
> Query 2: L = 2, R = 4, K = 1  
> **Output** :  
> 2  
> 3  
>  **Explanation** :  
> For the 1st query, the range (1, 3) represents elements, {8, 9, 1}. Among
> these elements only **8 and 9** have their 4th bit set. Thus, the answer for
> this query is **2**.  
> For the 2nd query, the range (2, 4) represents elements, {9, 1, 3}. **All**
> of these elements have their 1st bit set. Thus, the answer for this query is
> **3**.

**Prerequisites** : Bit Manipulation | Prefix Sum Arrays

  

  

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Method 1 (Brute Force)** : For each query, traverse the array from L to R,
and at every index check if the array element at that index has its Kth bit as
set. If it does increment the counter variable.

Below is the implementation of above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

/* C++ Program to find the number of elements

 in a range L to R having the Kth bit as set */

#include <bits/stdc++.h>

using namespace std;

// Maximum bits required in binary represention

// of an array element

#define MAX_BITS 32

/* Returns true if n has its kth bit as set, 

 else returns false */

bool isKthBitSet(int n, int k)

{

 if (n & (1 << (k - 1)))

 return true;

 return false;

}

/* Returns the answer for each query with range L

 to R querying for the number of elements with

 the Kth bit set in the range */

int answerQuery(int L, int R, int K, int arr[])

{

 // counter stores the number of element in

 // the range with the kth bit set

 int counter = 0;

 for (int i = L; i <= R; i++) {

 if (isKthBitSet(arr[i], K)) {

 counter++;

 }

 }

 return counter;

}

// Print the answer for all queries

void answerQueries(int queries[][3], int Q,

 int arr[], int N)

{

 int query_L, query_R, query_K;

 for (int i = 0; i < Q; i++) {

 query_L = queries[i][0] - 1;

 query_R = queries[i][1] - 1;

 query_K = queries[i][2];

 cout << "Result for Query " << i + 1 << " = "

 << answerQuery(query_L, query_R, query_K, arr)

 << endl;

 }

}

// Driver Code

int main()

{

 int arr[] = { 8, 9, 1, 3 };

 int N = sizeof(arr) / sizeof(arr[0]);

 /* queries[][] denotes the array of queries

 where each query has three integers

 query[i][0] -> Value of L for ith query

 query[i][0] -> Value of R for ith query

 query[i][0] -> Value of K for ith query */

 int queries[][3] = {

 { 1, 3, 4 },

 { 2, 4, 1 }

 };

 int Q = sizeof(queries) / sizeof(queries[0]);

 answerQueries(queries, Q, arr, N);

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

// Java Program to find the

// number of elements in a

// range L to R having the

// Kth bit as set

import java.util.*;

import java.lang.*;

import java.io.*;

// Maximum bits required

// in binary represention

// of an array element

class GFG

{

static final int MAX_BITS = 32;

/* Returns true if n

has its kth bit as set,

else returns false */

static boolean isKthBitSet(int n,

 int k)

{

 if ((n & (1 << (k - 1))) != 0)

 return true;

 return false;

}

/* Returns the answer for

each query with range L

to R querying for the number

of elements with the Kth bit

set in the range */

static int answerQuery(int L, int R,

 int K, int arr[])

{

 // counter stores the number

 // of element in the range

 // with the kth bit set

 int counter = 0;

 for (int i = L; i <= R; i++)

 {

 if (isKthBitSet(arr[i], K))

 {

 counter++;

 }

 }

 return counter;

}

// Print the answer

// for all queries

static void answerQueries(int queries[][], int Q,

 int arr[], int N)

{

 int query_L, query_R, query_K;

 for (int i = 0; i < Q; i++)

 {

 query_L = queries[i][0] - 1;

 query_R = queries[i][1] - 1;

 query_K = queries[i][2];

 System.out.println("Result for Query " +

 (i + 1) + " = " +

 answerQuery(query_L, query_R,

 query_K, arr));

 

 }

}

// Driver Code

public static void main(String args[])

{

 int arr[] = { 8, 9, 1, 3 };

 int N = arr.length;

 /* queries[][] denotes the array

 of queries where each query has

 three integers

 query[i][0] -> Value of L for ith query

 query[i][0] -> Value of R for ith query

 query[i][0] -> Value of K for ith query */

 int queries[][] =

 {

 { 1, 3, 4 },

 { 2, 4, 1 }

 };

 int Q = queries.length;

 answerQueries(queries, Q, arr, N);

}

}

// This code is contributed

// by Subhadeep  
  
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

# Python3 Program to find the number of elements

# in a range L to R having the Kth bit as set

# Maximum bits required in binary represention

# of an array element

MAX_BITS = 32

# Returns true if n has its kth bit as set,

# else returns false

def isKthBitSet(n, k):

 if (n & (1 << (k - 1))):

 return True

 return False

# Returns the answer for each query with range L

# to R querying for the number of elements with

# the Kth bit set in the range

def answerQuery(L, R, K, arr):

 

 # counter stores the number of element

 # in the range with the kth bit set

 counter = 0

 for i in range(L, R + 1):

 if (isKthBitSet(arr[i], K)):

 counter += 1

 return counter

# Print the answer for all queries

def answerQueries(queries, Q, arr, N):

 for i in range(Q):

 query_L = queries[i][0] - 1

 query_R = queries[i][1] - 1

 query_K = queries[i][2]

 print("Result for Query", i + 1, "=",

 answerQuery(query_L, query_R,

 query_K, arr))

# Driver Code

if __name__ == "__main__":

 arr = [ 8, 9, 1, 3 ]

 N = len(arr)

 # queries[][] denotes the array of queries

 # where each query has three integers

 # query[i][0] -> Value of L for ith query

 # query[i][0] -> Value of R for ith query

 # query[i][0] -> Value of K for ith query

 queries = [[ 1, 3, 4 ],

 [ 2, 4, 1 ]]

 Q = len(queries)

 answerQueries(queries, Q, arr, N)

# This code is contributed by ita_c  
  
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

// C# Program to find the number of

// elements in a range L to R having

// the Kth bit as set

using System;

// Maximum bits required

// in binary represention

// of an array element

class GFG

{

static readonly int MAX_BITS = 32;

/* Returns true if n

has its kth bit as set,

else returns false */

static bool isKthBitSet(int n,

 int k)

{

 if ((n & (1 << (k - 1))) != 0)

 return true;

 return false;

}

/* Returns the answer for each query

with range L to R querying for the

number of elements with the Kth bit

set in the range */

static int answerQuery(int L, int R,

 int K, int []arr)

{

 // counter stores the number

 // of element in the range

 // with the kth bit set

 int counter = 0;

 for (int i = L; i <= R; i++)

 {

 if (isKthBitSet(arr[i], K))

 {

 counter++;

 }

 }

 return counter;

}

// Print the answer for all queries

static void answerQueries(int [,]queries, int Q,

 int []arr, int N)

{

 int query_L, query_R, query_K;

 for (int i = 0; i < Q; i++)

 {

 query_L = queries[i,0] - 1;

 query_R = queries[i,1] - 1;

 query_K = queries[i,2];

 Console.WriteLine("Result for Query " +

 (i + 1) + " = " +

 answerQuery(query_L, query_R,

 query_K, arr));

 }

}

// Driver Code

public static void Main()

{

 int []arr = { 8, 9, 1, 3 };

 int N = arr.Length;

 /* queries[][] denotes the array

 of queries where each query has

 three integers

 query[i][0] -> Value of L for ith query

 query[i][0] -> Value of R for ith query

 query[i][0] -> Value of K for ith query */

 int [,]queries = { { 1, 3, 4 },

 { 2, 4, 1 } };

 int Q = queries.GetLength(0);

 answerQueries(queries, Q, arr, N);

}

}

// This code is contributed

// by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    Result for Query 1 = 2
    Result for Query 2 = 3

**Time Complexity** : O(N) for each query.

 **Method 2 (Efficient)** : Assuming that every integer in the array has at
max **32** bits in its Binary Representation. A 2D prefix sum array can be
built to solve the problem. Here the 2nd dimension of the prefix array is of
size equal to the **maximum number of bits** required to represent a integer
of the array in binary.  
Let the Prefix Sum Array be **P[][]**. Now, **P[i][j]** denotes the number of
Elements from **0** to **i** , which have their **j th** bit as set. This
prefix sum array is built before answering the queries. If a query from L to R
is encountered, querying for elements in this range having their Kth bit as
set, then the answer for that query is **P[R][K] – P[L – 1][K]**.

Below is the implementation of above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

/* C++ Program to find the number of elements

 in a range L to R having the Kth bit as set */

#include <bits/stdc++.h>

using namespace std;

// Maximum bits required in binary represention

// of an array element

#define MAX_BITS 32

/* Returns true if n has its kth bit as set,

 else returns false */

bool isKthBitSet(int n, int k)

{

 if (n & (1 << (k - 1)))

 return true;

 return false;

}

// Return pointer to the prefix sum array

int** buildPrefixArray(int N, int arr[])

{

 // Build a prefix sum array P[][]

 // where P[i][j] represents the number of

 // elements from 0 to i having the jth bit as set

 int** P = new int*[N + 1];

 for (int i = 0; i <= N; ++i) {

 P[i] = new int[MAX_BITS + 1];

 }

 for (int i = 0; i <= MAX_BITS; i++) {

 P[0][i] = 0;

 }

 for (int i = 0; i < N; i++) {

 for (int j = 1; j <= MAX_BITS; j++) {

 // prefix sum from 0 to i for each bit

 // position jhas the value of sum from 0

 // to i-1 for each j

 if (i)

 P[i][j] = P[i - 1][j];

 // if jth bit set then increment P[i][j] by 1

 bool isJthBitSet = isKthBitSet(arr[i], j);

 if (isJthBitSet) {

 P[i][j]++;

 }

 }

 }

 return P;

}

/* Returns the answer for each query with range

 L to R querying for the number of elements with

 the Kth bit set in the range */

int answerQuery(int L, int R, int K, int** P)

{

 /* Number of elements in range L to R with Kth

 bit set = (Number of elements from 0 to R with

 kth bit set) - (Number of elements from 0 to L-1

 with kth bit set) */

 if (L)

 return P[R][K] - P[L - 1][K];

 else

 return P[R][K];

}

// Print the answer for all queries

void answerQueries(int queries[][3], int Q,

 int arr[], int N)

{

 // Build Prefix Array to answer queries efficiently

 int** P = buildPrefixArray(N, arr);

 int query_L, query_R, query_K;

 for (int i = 0; i < Q; i++) {

 query_L = queries[i][0] - 1;

 query_R = queries[i][1] - 1;

 query_K = queries[i][2];

 cout << "Result for Query " << i + 1 << " = "

 << answerQuery(query_L, query_R, query_K, P)

 << endl;

 }

}

// Driver Code

int main()

{

 int arr[] = { 8, 9, 1, 3 };

 int N = sizeof(arr) / sizeof(arr[0]);

 /* queries[][] denotes the array of queries

 where each query has three integers

 query[i][0] -> Value of L for ith query

 query[i][0] -> Value of R for ith query

 query[i][0] -> Value of K for ith query */

 int queries[][3] = {

 { 1, 3, 4 },

 { 2, 4, 1 }

 };

 int Q = sizeof(queries) / sizeof(queries[0]);

 answerQueries(queries, Q, arr, N);

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

/* Java Program to find the number of elements

 in a range L to R having the Kth bit as set */

import java.io.*;

class GFG

{

 // Maximum bits required in binary represention

 // of an array element

 static int MAX_BITS = 32;

 /* Returns true if n has its kth bit as set,

 else returns false */

 static boolean isKthBitSet(int n, int k)

 {

 if((n & (1 << (k - 1))) != 0)

 {

 return true;

 }

 return false;

 }

 // Return pointer to the prefix sum array

 static int[][] buildPrefixArray(int N, int[] arr)

 {

 // Build a prefix sum array P[][]

 // where P[i][j] represents the number of

 // elements from 0 to i having the jth bit as set

 int[][] P = new int[N + 1][MAX_BITS + 1];

 for(int i = 0; i <= MAX_BITS; i++)

 {

 P[0][i] = 0;

 }

 for(int i = 0; i < N; i++)

 {

 for(int j = 1; j <= MAX_BITS; j++)

 {

 // prefix sum from 0 to i for each bit

 // position jhas the value of sum from 0

 // to i-1 for each j

 if(i != 0)

 {

 P[i][j] = P[i - 1][j];

 }

 // if jth bit set then increment P[i][j] by 1

 boolean isJthBitSet = isKthBitSet(arr[i], j);

 if(isJthBitSet)

 {

 P[i][j]++;

 }

 }

 }

 return P;

 }

 /* Returns the answer for each query with range

 L to R querying for the number of elements with

 the Kth bit set in the range */

 static int answerQuery(int L, int R, int K, int[][]
P)

 {

 /* Number of elements in range L to R with Kth

 bit set = (Number of elements from 0 to R with

 kth bit set) - (Number of elements from 0 to L-1

 with kth bit set) */

 if(L != 0)

 {

 return P[R][K] - P[L - 1][K];

 }

 else

 {

 return P[R][K];

 }

 }

 // Print the answer for all queries

 static void answerQueries(int[][] queries,int Q,

 int[] arr, int N)

 {

 // Build Prefix Array to answer queries efficiently

 int[][] P = buildPrefixArray(N, arr);

 int query_L, query_R, query_K;

 for(int i = 0; i < Q; i++)

 {

 query_L = queries[i][0] - 1;

 query_R = queries[i][1] - 1;

 query_K = queries[i][2];

 System.out.println("Result for Query " + (i + 1) + " = " +
answerQuery(query_L, query_R, query_K, P));

 }

 }

 // Driver Code

 public static void main (String[] args)

 {

 int[] arr = {8, 9, 1, 3};

 int N = arr.length;

 /* queries[][] denotes the array of queries

 where each query has three integers

 query[i][0] -> Value of L for ith query

 query[i][0] -> Value of R for ith query

 query[i][0] -> Value of K for ith query */

 int[][] queries = {{1, 3, 4},{2, 4, 1}};

 int Q = queries.length;

 answerQueries(queries, Q, arr, N);

 }

}

// This code is contributed by avanitrachhadiya2155  
  
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

# Python3 program to find the number

# of elements in a range L to R having

# the Kth bit as set

# Maximum bits required in binary

# represention of an array element

MAX_BITS = 32

# Returns true if n has its kth

# bit as set,else returns false

def isKthBitSet(n, k):

 if (n & (1 << (k - 1))):

 return True

 

 return False

# Return pointer to the prefix sum array

def buildPrefixArray(N, arr):

 

 # Build a prefix sum array P[][]

 # where P[i][j] represents the

 # number of elements from 0 to

 # i having the jth bit as set

 P = [[0 for i in range(MAX_BITS + 1)]

 for i in range(N + 1)]

 for i in range(N):

 for j in range(1, MAX_BITS + 1):

 

 # prefix sum from 0 to i for each bit

 # position jhas the value of sum from 0

 # to i-1 for each j

 if (i):

 P[i][j] = P[i - 1][j]

 # If jth bit set then increment

 # P[i][j] by 1

 isJthBitSet = isKthBitSet(arr[i], j)

 

 if (isJthBitSet):

 P[i][j] += 1

 return P

# Returns the answer for each query

# with range L to R querying for the

# number of elements with the Kth bit

# set in the range

def answerQuery(L, R, K, P):

 # Number of elements in range L to

 # R with Kth bit set = (Number of

 # elements from 0 to R with kth

 # bit set) - (Number of elements

 # from 0 to L-1 with kth bit set)

 if (L):

 return P[R][K] - P[L - 1][K]

 else:

 return P[R][K]

# Print the answer for all queries

def answerQueries(queries, Q, arr, N):

 # Build Prefix Array to answer

 # queries efficiently

 P = buildPrefixArray(N, arr)

 for i in range(Q):

 query_L = queries[i][0] - 1

 query_R = queries[i][1] - 1

 query_K = queries[i][2]

 print("Result for Query ", i + 1,

 " = ", answerQuery(query_L, query_R,

 query_K, P))

# Driver Code

if __name__ == '__main__':

 arr = [ 8, 9, 1, 3 ]

 N = len(arr)

 # queries[]denotes the array of queries

 # where each query has three integers

 # query[i][0] -> Value of L for ith query

 # query[i][0] -> Value of R for ith query

 # query[i][0] -> Value of K for ith query

 queries = [ [ 1, 3, 4 ],

 [ 2, 4, 1 ] ]

 

 Q = len(queries)

 answerQueries(queries, Q, arr, N)

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

// C# program to find the number of elements

// in a range L to R having the Kth bit as set

using System;

class GFG{

 

// Maximum bits required in binary represention

// of an array element

static int MAX_BITS = 32;

// Returns true if n has its kth bit as set,

// else returns false

static bool isKthBitSet(int n, int k)

{

 if ((n & (1 << (k - 1))) != 0)

 {

 return true;

 }

 return false;

}

// Return pointer to the prefix sum array

static int[,] buildPrefixArray(int N, int[] arr)

{

 

 // Build a prefix sum array P[][]

 // where P[i][j] represents the

 // number of elements from 0 to i

 // having the jth bit as set

 int[,] P = new int[N + 1, MAX_BITS + 1];

 for(int i = 0; i <= MAX_BITS; i++)

 {

 P[0, i] = 0;

 }

 

 for(int i = 0; i < N; i++)

 {

 for(int j = 1; j <= MAX_BITS; j++)

 {

 

 // prefix sum from 0 to i for each bit

 // position jhas the value of sum from 0

 // to i-1 for each j

 if (i != 0)

 {

 P[i, j] = P[i - 1, j];

 }

 

 // If jth bit set then increment P[i][j] by 1

 bool isJthBitSet = isKthBitSet(arr[i], j);

 if (isJthBitSet)

 {

 P[i, j]++;

 }

 }

 }

 return P;

}

// Returns the answer for each query with range

// L to R querying for the number of elements with

// the Kth bit set in the range

static int answerQuery(int L, int R, int K, int[,] P)

{

 

 // Number of elements in range L to R with Kth

 // bit set = (Number of elements from 0 to R with

 // kth bit set) - (Number of elements from 0 to L-1

 // with kth bit set)

 if (L != 0)

 {

 return P[R, K] - P[L - 1, K];

 }

 else

 {

 return P[R, K];

 }

}

// Print the answer for all queries

static void answerQueries(int[,] queries, int Q,

 int[] arr, int N)

{

 

 // Build Prefix Array to answer queries efficiently

 int[,] P = buildPrefixArray(N, arr);

 int query_L, query_R, query_K;

 for(int i = 0; i < Q; i++)

 {

 query_L = queries[i, 0] - 1;

 query_R = queries[i, 1] - 1;

 query_K = queries[i, 2];

 Console.WriteLine("Result for Query " +

 (i + 1) + " = " +

 answerQuery(query_L,

 query_R,

 query_K, P));

 }

}

// Driver Code

static public void Main()

{

 int[] arr = { 8, 9, 1, 3 };

 int N = arr.Length;

 

 /* queries[][] denotes the array of queries

 where each query has three integers

 query[i][0] -> Value of L for ith query

 query[i][0] -> Value of R for ith query

 query[i][0] -> Value of K for ith query */

 int[,] queries = { { 1, 3, 4 }, { 2, 4, 1 } };

 int Q = queries.GetLength(0);

 

 answerQueries(queries, Q, arr, N);

}

}

// This code is contributed by rag2127  
  
---  
  
 __

 __

 **Output:**

    
    
    Result for Query 1 = 2
    Result for Query 2 = 3

**Time Complexity** of building the Prefix array is O(N * Maximum number of
Bits) and each query is answered in O(1).  
**Auxiliary space** : O(N * Maximum Number of Bits) is required to build the
Prefix Sum Array  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

