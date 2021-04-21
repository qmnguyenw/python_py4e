Count of elements having odd number of divisors in index range [L, R] for Q
queries



Given an array **arr[]** of **N** positive integers and the number of queries
**Q** , each query contains two numbers **L** and **R**. The task is to count
the number of elements in the array having odd number of divisors from index
**L to R**.

 **Examples:**

> **Input:** arr[] = [2, 4, 5, 6, 9], Q = 3, Query[][] = { {0, 2}, {1, 3}, {1,
> 4} }  
> **Output:** 1 1 2  
> **Explanation:**  
> 1st query: in 2 4 5 only 4 has an odd number of divisors.  
> 2nd query: in 4 5 6 only 4 has an odd number of divisors.  
> 3rd query: in 4 5 6 9 only 4, 9 has an odd number of divisors.
>
>  **Input:** arr[] = [1, 16, 5, 4, 9], Q = 2, Query[][] = { {1, 3}, {0, 2} }  
> **Output:** 2 1

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The naive approach is to iterate over the array from **L
to R** for each query and count the element in the range **[L, R]** having odd
numbers of divisors. If yes then count that element for that query.

  

  

 _ **Time Complexity:** O(Q * N * sqrt(N)) _  
_**Auxiliary Space:** O(1)_

 **Efficient Approach:** We can observe that the number of divisors is odd
only in case of perfect squares. Hence the best solution is to check if the
given number is a perfect square or not in the range **[L, R]**. Below are the
steps:

  1. Initialize the array **dp[]** of size **N** with value **0**.
  2. Traverse the given array **arr[]** and if any element in the it is a perfect square the update the value at that index in **dp[]** as **1**.
  3. To calculate the answer for each query efficiently we will precompute the answer.
  4. We will do the prefix sum of the array **dp[]** and for each query in the range [L, R] the answer will be given by: 

    
    
    OddDivisorCount(L, R) = DP[R] - DP[L-1]
    

Below is the implementation of the above approach:

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

// Function count the number of elements

// having odd number of divisors

void OddDivisorsCount(

 int n, int q, int a[],

 vector<pair<int, int> > Query)

{

 // Initialise dp[] array

 int DP[n] = { 0 };

 // Precomputation

 for (int i = 0; i < n; i++) {

 int x = sqrt(a[i]);

 if (x * x == a[i])

 DP[i] = 1;

 }

 // Find the Prefix Sum

 for (int i = 1; i < n; i++) {

 DP[i] = DP[i - 1] + DP[i];

 }

 int l, r;

 // Iterate for each query

 for (int i = 0; i < q; i++) {

 l = Query[i].first;

 r = Query[i].second;

 // Find the answer for each query

 if (l == 0) {

 cout << DP[r] << endl;

 }

 else {

 cout << DP[r] - DP[l - 1]

 << endl;

 }

 }

}

// Driver Code

int main()

{

 int N = 5;

 int Q = 3;

 // Given array arr[]

 int arr[] = { 2, 4, 5, 6, 9 };

 // Given Query

 vector<pair<int, int> > Query

 Query

 = { { 0, 2 }, { 1, 3 }, { 1, 4 } };

 // Function Call

 OddDivisorsCount(N, Q, arr, Query);

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

import java.util.*;

class GFG{

 

static class pair

{

 int first, second;

 public pair(int first, int second)

 {

 this.first = first;

 this.second = second;

 }

}

// Function count the number of elements

// having odd number of divisors

static void OddDivisorsCount(int n, int q,

 int a[],

 pair []Query)

{

 

 // Initialise dp[] array

 int DP[] = new int[n];

 // Precomputation

 for(int i = 0; i < n; i++)

 {

 int x = (int)Math.sqrt(a[i]);

 

 if (x * x == a[i])

 DP[i] = 1;

 }

 

 // Find the Prefix Sum

 for(int i = 1; i < n; i++)

 {

 DP[i] = DP[i - 1] + DP[i];

 }

 

 int l, r;

 // Iterate for each query

 for(int i = 0; i < q; i++)

 {

 l = Query[i].first;

 r = Query[i].second;

 

 // Find the answer for each query

 if (l == 0)

 {

 System.out.print(DP[r] + "\n");

 }

 else

 {

 System.out.print(DP[r] -

 DP[l - 1] + "\n");

 }

 }

}

// Driver Code

public static void main(String[] args)

{

 int N = 5;

 int Q = 3;

 // Given array arr[]

 int arr[] = { 2, 4, 5, 6, 9 };

 // Given Query

 pair []Query = { new pair(0, 2),

 new pair(1, 3),

 new pair(1, 4) };

 // Function Call

 OddDivisorsCount(N, Q, arr, Query);

}

}

// This code is contributed by amal kumar choubey  
  
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

import math

# Function count the number of elements

# having odd number of divisors

def OddDivisorsCount(n, q, a, Query):

 

 # Initialise dp[] array

 DP = [0 for i in range(n)]

 

 # Precomputation

 for i in range(n):

 x = int(math.sqrt(a[i]));

 

 if (x * x == a[i]):

 DP[i] = 1;

 

 # Find the Prefix Sum

 for i in range(1, n):

 DP[i] = DP[i - 1] + DP[i];

 

 l = 0

 r = 0

 

 # Iterate for each query

 for i in range(q):

 l = Query[i][0];

 r = Query[i][1];

 

 # Find the answer for each query

 if (l == 0):

 print(DP[r])

 else:

 print(DP[r] - DP[l - 1])

# Driver code

if __name__=="__main__":

 

 N = 5;

 Q = 3;

 

 # Given array arr[]

 arr = [ 2, 4, 5, 6, 9 ]

 

 # Given Query

 Query = [ [ 0, 2 ],

 [ 1, 3 ],

 [ 1, 4 ] ]

 

 # Function call

 OddDivisorsCount(N, Q, arr, Query);

# This code is contributed by rutvik_56  
  
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

class pair

{

 public int first, second;

 public pair(int first, int second)

 {

 this.first = first;

 this.second = second;

 }

}

// Function count the number of elements

// having odd number of divisors

static void OddDivisorsCount(int n, int q,

 int []a,

 pair []Query)

{

 

 // Initialise []dp array

 int []DP = new int[n];

 // Precomputation

 for(int i = 0; i < n; i++)

 {

 int x = (int)Math.Sqrt(a[i]);

 if (x * x == a[i])

 DP[i] = 1;

 }

 

 // Find the Prefix Sum

 for(int i = 1; i < n; i++)

 {

 DP[i] = DP[i - 1] + DP[i];

 }

 

 int l, r;

 // Iterate for each query

 for(int i = 0; i < q; i++)

 {

 l = Query[i].first;

 r = Query[i].second;

 

 // Find the answer for each query

 if (l == 0)

 {

 Console.Write(DP[r] + "\n");

 }

 else

 {

 Console.Write(DP[r] -

 DP[l - 1] + "\n");

 }

 }

}

// Driver Code

public static void Main(String[] args)

{

 int N = 5;

 int Q = 3;

 // Given array []arr

 int []arr = { 2, 4, 5, 6, 9 };

 // Given Query

 pair []Query = { new pair(0, 2),

 new pair(1, 3),

 new pair(1, 4) };

 // Function Call

 OddDivisorsCount(N, Q, arr, Query);

}

}

// This code is contributed by gauravrajput1  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    1
    2
    
    

_**Time complexity:** _

  * _Precomputation: O(N)_
  *  _For each query: O(1)_  

_**Auxiliary Space:** O(1)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

