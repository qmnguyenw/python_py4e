Queries for Count of divisors of product of an Array in given range | Set 2
(MO’s Algorithm)



Given an array **arr** of size **N** and **Q** queries of the form **[L, R]**
, the task is to find the number of divisors of the product of this array in
the given range.

 **Prerequisite:** MO’s Algorithm, Modular Multiplicative Inverse, Prime
Factorization using sieve

 **Examples:**

>  **Input:** arr[] = {4, 1, 9, 12, 5, 3}, Q = {{1, 3}, {3, 5}}  
>  **Output:**  
>  9  
> 24
>
>  **Input:** arr[] = {5, 2, 3, 1, 4}, Q = {{2, 4}, {1, 5}}  
>  **Output:**  
>  4  
> 16
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
Let **a[0…n-1]** be input array and **q[0..m-1]** be an array of queries.

  1. Sort all queries in a way that queries with L values from **0** to **√n – 1** are put together, then all queries from **√n** to **2×√n – 1** , and so on. All queries within a block are sorted in increasing order of R values.
  2. Process all queries one by one in a way that every query uses result computed in the previous query. Let ‘result’ be result of previous query
  3. A number n can be represented as **n =![\\prod_{i=1}^{n} a_{i}^{p_{i}}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a2a5e309f80a5e1a6f44399de840aab6_l3.png)** , where _a i_ are prime factors and _p i_ are integral power of them.  
So, for this factorization we have formula to find total number of divisor of
n and that is:

> ![\\prod_{i=1}^{n} \(p_{i}+1\)](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-42d102b6b4c8490ad52c79a8a1503400_l3.png)

  4. In **Add function** we increment counter array as i.e **counter[a[i]]=counter[a[i]]+ p i**. Let ‘prev’ stores the previous value of counter[a[i]]. Now as counter array changes, result changes as:

>     *  **result = result / (prev + 1)** (Dividing by prev+1 neutralizes the
> effect of previous pi)
>     *  **result = (result × (counter[p i] + 1)** (Now the previous result is
> neutralized so we multiply with the new count i.e counter[a[i]]+1)

  5. In **Remove function** we decrement the counter array as **counter[a[i]] = counter[a[i]] – p i**. Now as counter array changes, result changes as:

>     *  **result = result / (prev + 1)** (Dividing by prev+1 neutralizes the
> effect of previous pi)
>     *  **result = (result × (counter[p i] + 1)** (Now the previous result is
> neutralized so we  
> multiply with the new count i.e counter[a[i]]+1)

Below is the implementation of the above approach

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to Count the divisors

// of product of an Array in range 

// L to R for Q queries

#include <bits/stdc++.h>

using namespace std;

 

#define MAX 1000000

#define MOD 1000000007

#define ll long long int

 

// Variable to represent block size.

// This is made global so compare()

// of sort can use it.

int block;

 

// Structure to represent a query range

struct Query {

 int L, R;

};

 

// Store the prime factor of numbers

// till MAX

vector<pair<int, int> > store[MAX + 1];

 

// Initialized to store the count 

// of prime fators

int counter[MAX + 1] = {};

 

// Result is Initialized to 1

int result = 1;

 

// Inverse array to store

// inverse of number from 1 to MAX

ll inverse[MAX + 1];

 

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

 

// Function to calculate modular

// inverse and storing it in Inverse array

void modularInverse()

{

 

 inverse[0] = inverse[1] = 1;

 for (int i = 2; i <= MAX; i++)

 inverse[i] = inverse[MOD % i]

 * (MOD - MOD / i) 

 % MOD;

}

 

// Function to use Sieve to compute

// and store prime numbers

void sieve()

{

 

 store[1].push_back({ 1, 0 });

 for (int i = 2; i <= MAX; i++)

 {

 if (store[i].size() == 0)

 {

 store[i].push_back({ i, 1 });

 

 for (int j = 2 * i; j <= MAX; j += i)

 {

 int cnt = 0;

 int x = j;

 while (x % i == 0)

 cnt++, x /= i;

 store[j].push_back({ i, cnt });

 }

 }

 }

}

 

// Function to Add elements

// of current range

void add(int currL, int a[])

{

 int value = a[currL];

 for (auto it = store[value].begin();

 it != store[value].end(); it++) {

 // it->first is ai

 // it->second is its integral power

 int prev = counter[it->first];

 counter[it->first] += it->second;

 result = (result * inverse[prev + 1])

 % MOD;

 

 result = (result *

 (counter[it->first] + 1))

 % MOD;

 }

}

 

// Function to remove elements

// of previous range

void remove(int currR, int a[])

{

 int value = a[currR];

 for (auto it = store[value].begin(); 

 it != store[value].end(); it++) {

 // it->first is ai

 // it->second is its integral power

 int prev = counter[it->first];

 counter[it->first] -= it->second;

 result = (result * inverse[prev + 1])

 % MOD;

 result = (result *

 (counter[it->first] + 1)) 

 % MOD;

 }

}

 

// Function to print the answer.

void queryResults(int a[], int n, Query q[],

 int m)

{

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

 

 cout << result << endl;

 }

}

 

// Driver Code

int main()

{

 // Precomputing the prime numbers 

 // using sieve

 sieve();

 

 // Precomputing modular inverse of 

 // numbers from 1 to MAX

 modularInverse();

 

 int a[] = { 5, 2, 3, 1, 4 };

 int n = sizeof(a) / sizeof(a[0]);

 

 Query q[] = { { 1, 3 }, { 0, 4 } };

 

 int m = sizeof(q) / sizeof(q[0]);

 

 // Answer the queries

 queryResults(a, n, q, m);

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    16
    

**Time Complexity:** O(Q×sqrt(N))

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

