Count of odd and even parity elements in subarray using MO’s algorithm



  
Given an array **arr** consisting of **N** elements and **Q** queries
represented by **L** and **R** denoting a range, the task is to print the
count of odd and even parity elements in the subarray **[L, R]**.

 **Examples:**

>  **Input:**  
>  arr[]=[5, 2, 3, 1, 4, 8, 10]  
> Q=2  
> 1 3  
> 0 4  
>  **Output:**  
>  2 1  
> 3 2
>
>  **Explanation** :  
> In query 1, odd parity elements in subarray [1:3] are 2 and 1 and even
> parity element is 3.  
> In query 2, odd parity elements in subarray [0:4] are 2, 1 and 4 and even
> parity elements are 5 and 3.
>
>  **Input:**  
>  arr[] = { 13, 17, 12, 10, 18, 19, 15, 7, 9, 6 }  
> Q=3  
> 1 5  
> 0 7  
> 2 9  
>  **Output:**  
>  1 4  
> 3 5  
> 2 6  
>  **Explanation** :  
> In query 1, odd parity element in subarray [1:4] is 19 and even parity
> elements are 17,12,10 and 18.  
> In query 2, odd parity elements in subarray [0:7] are 13, 19 and 7 and even
> parity elements are 17,12,10,18 and 15.  
> In query 3, odd parity elements in subarray [2:6] are 19 and 7 and even
> parity elements are 12,10,18, 15, 9 and 6.
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
The idea of MO’s algorithm is to pre-process all queries so that result of one
query can be used in the next query.

  1. Sort all queries in a way that queries with **L** values from **0 to √n – 1** are put together, followed by queries from **√n to 2×√n – 1** , and so on. All queries within a block are sorted in increasing order of **R** values.
  2. Count the **odd parity** elements and then calculate the **even parity** elements as **(R-L+1- odd parity elements)**
  3. Process all queries one by one and increase the count of odd parity elements and store the result in the structure.
    * Let **count_oddP** store the count of odd parity elements in previous query.
    * Remove extra elements of previous query and add new elements for the current query. For example, if previous query was [0, 8] and the current query is [3, 9], then remove the elements arr[0], arr[1] and arr[2] and add arr[9].
  4. In order to display the results, sort the queries in the order they were provided.

 **Adding elements()**

  * If the current element has odd parity then increase the count of **count_oddP**.

 **Removing elements()**

      * If the current element has odd parity then decrease the count of **count_oddP**.

Below code is the implementation of the above approach:

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

// using MO's algorithm

 

#include <bits/stdc++.h>

using namespace std;

 

#define MAX 100000

 

// Variable to represent block size.

// This is made global so compare()

// of sort can use it.

int block;

 

// Structure to represent a query range 

struct Query {

 // Starting index

 int L; 

 // Ending index

 int R;

 // Index of query

 int index;

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

 

// Function used to sort all queries in order of their

// index value so that results of queries can be printed

// in same order as of input

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

 int L = q[i].L, R = q[i].R;

 

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

 

 q[i].odd = count_oddP;

 q[i].even = R - L + 1 - count_oddP;

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

 

 int arr[] = { 5, 2, 3, 1, 4, 8, 10, 12 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 Query q[] = { { 1, 3, 0, 0, 0 }, 

 { 0, 4, 1, 0, 0 }, 

 { 4, 7, 2, 0, 0 } };

 

 int m = sizeof(q) / sizeof(q[0]);

 

 queryResults(arr, n, q, m);

 

 printResults(q, m);

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

                
                
                2 1
                3 2
                2 2
                

**Time Complexity:** O(Q × √n)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

