Find pairs of elements from two different arrays whose product is a perfect
square



 **Prerequisites:** Prime Factorization using Sieve

Given two arrays **arr1[]** and **arr2[]** of size **M** and **N** with
distinct elements in each of the arrays, the task is to find those pair of
elements (one from the first array and other from the second array) whose
product is a perfect square. Print -1 if no pairs can be formed.

 **Examples:**

>  **Input:** arr1[] = {1, 8, 6, 9}, arr2[] = {2, 24, 49}  
>  **Output:** (1, 49), (8, 2), (6, 24), (9, 49)  
>  **Explanation:**  
>  The product of pairs in the output are all perfect squares.  
> Pair 1: 1 x 49 = 49  
> Pair 2: 8 x 2 = 16  
> Pair 3: 6 x 24 = 144  
> Pair 4: 9 x 49 = 441
>
>  **Input:** arr1[] = {2, 3, 4}, arr2[] = {9, 5}  
>  **Output:** -1
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** Naive approach is to choose all the possible pairs and
check if they form a perfect square. This can be done in quadratic time.  
 **Time Complexity:** O(M*N)

 **Efficient Approach:** The idea is to use the concept of prime
factorization. Let’s analyse how to use the concept in this problem.  
The following are the scenarios where the product of two numbers form a
perfect square:

  * If both the numbers are perfect squares their product always form a perfect square.
  * If one of the numbers is not a perfect square their product can never be a perfect square.
  * In case both the numbers are non-perfect squares, then the number of prime factors of both the numbers combined have to be even.
  * For example,  

> let x = 6, y = 1176  
> prime factorization of x = 2 x 3 (2 and 3 occurs odd times)  
> prime factorization of y = 2 x 2 x 2 x 3 x 7 x 7 (2 and 3 occurs odd times)  
> x * y = 7056 which is square of 84

Since x and y have all odd times occurring primes, but x * y has even number
of prime factors. Therefore, they will form a perfect square.

Therefore, the array **arr1[]** is traversed and for each element in
**arr1[]** , the numbers in array **arr2[]** which have same product of odd
times occurring primes as of current element. This can be done using map STL
in C++ in **logn** time.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print pairs whose

// product is a perfect square

#include <bits/stdc++.h>

using namespace std;

 

// Maximum number upto which sieve is performed

#define MAXN 100001

 

// Array to perform Sieve of Eratosthenes

// and store prime numbers

int spf[MAXN];

 

// Function to perform sieve of

// eratosthenes on the array spf.

void sieve()

{

 spf[1] = 1;

 for (int i = 2; i < MAXN; i++)

 spf[i] = i;

 

 for (int i = 4; i < MAXN; i += 2)

 spf[i] = 2;

 

 for (int i = 3; i * i < MAXN; i++) {

 if (spf[i] == i) {

 for (int j = i * i; j < MAXN; j += i)

 

 if (spf[j] == j)

 spf[j] = i;

 }

 }

}

 

// Function to return the product of the

// odd occurring prime factors of a number

int getProductOddOccuringPrimes(int x)

{

 // Product of 1 with perfect square gives

 // perfect square, 1 is returned for x = 1

 if (x == 1)

 return 1;

 

 // Temperory container of prime factors

 vector<int> ret;

 while (x != 1) {

 ret.push_back(spf[x]);

 x = x / spf[x];

 }

 

 // ans contains the product of primes

 // which occurs odd number of times

 int count = 1, ans = 1;

 for (int i = 0, j = 1; j < ret.size(); ++j, ++i) {

 if (ret[i] != ret[j]) {

 if (count & 1)

 ans *= ret[i];

 count = 0;

 }

 count++;

 }

 

 // Checks if count is odd or not

 if (count & 1)

 ans *= ret[ret.size() - 1];

 

 return ans;

}

 

// Function to print the pairs whose product is

// a perfect square

void printPairs(int n, int m, int a[], int b[])

{

 int countPairs = 0;

 

 // For storing the indicies with same

 // product of odd times occuring Primes as key

 map<int, vector<int> > productOfPrimes;

 

 // Every number from both the array is iterated

 // getProductOddOccuringPrimes function is called

 // and the product of odd occurring primes is

 // stored in the map productOfPrimes.

 // A pair is printed if the product is same

 for (int i = 0; i < n; ++i) {

 

 // Generating the product of odd times

 // occurring primes

 int productPrimesOfA

 = getProductOddOccuringPrimes(a[i]);

 

 // Pushing the indices to the to the

 // vector with the product of

 // odd times occurring Primes

 productOfPrimes[productPrimesOfA].push_back(i);

 }

 

 for (int i = 0; i < m; ++i) {

 // Generating the product of odd times

 // occurring Primes

 int productPrimesOfB

 = getProductOddOccuringPrimes(b[i]);

 

 // Checking if productPrimesOfB

 // lies in the productOfPrimes

 if (productOfPrimes.find(productPrimesOfB)

 != productOfPrimes.end()) {

 for (auto itr : productOfPrimes[productPrimesOfB]) {

 countPairs++;

 cout << " (" << b[i] << ", "

 << a[itr] << ") ";

 }

 }

 }

 if (countPairs <= 0)

 cout << "No pairs Found!";

 cout << endl;

}

// Driver function

int main()

{

 sieve();

 

 // N, M are size of array a and b respectively

 int N = 5, M = 5;

 int a[] = { 4, 1, 6, 35, 120 };

 int b[] = { 24, 140, 4, 30, 1 };

 

 // Function that prints the pairs

 // whose product is a perfect square

 printPairs(N, M, a, b);

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

// Java program to print pairs whose

// product is a perfect square

import java.util.*;

 

class GFG{

 

// Maximum number upto which sieve is performed

static final int MAXN = 100001;

 

// Array to perform Sieve of Eratosthenes

// and store prime numbers

static int []spf = new int[MAXN];

 

// Function to perform sieve of

// eratosthenes on the array spf.

static void sieve()

{

 spf[1] = 1;

 for (int i = 2; i < MAXN; i++)

 spf[i] = i;

 

 for (int i = 4; i < MAXN; i += 2)

 spf[i] = 2;

 

 for (int i = 3; i * i < MAXN; i++) {

 if (spf[i] == i) {

 for (int j = i * i; j < MAXN; j += i)

 

 if (spf[j] == j)

 spf[j] = i;

 }

 }

}

 

// Function to return the product of the

// odd occurring prime factors of a number

static int getProductOddOccuringPrimes(int x)

{

 // Product of 1 with perfect square gives

 // perfect square, 1 is returned for x = 1

 if (x == 1)

 return 1;

 

 // Temperory container of prime factors

 Vector<Integer> ret = new Vector<Integer>();

 while (x != 1) {

 ret.add(spf[x]);

 x = x / spf[x];

 }

 

 // ans contains the product of primes

 // which occurs odd number of times

 int count = 1, ans = 1;

 for (int i = 0, j = 1; j < ret.size(); ++j, ++i) {

 if (ret.get(i) != ret.get(j)) {

 if (count % 2 == 1)

 ans *= ret.get(i);

 count = 0;

 }

 count++;

 }

 

 // Checks if count is odd or not

 if (count %2 == 1)

 ans *= ret.get(ret.size() - 1);

 

 return ans;

}

 

// Function to print the pairs whose product is

// a perfect square

static void printPairs(int n, int m, int a[], int b[])

{

 int countPairs = 0;

 

 // For storing the indicies with same

 // product of odd times occuring Primes as key

 Map<Integer, Vector<Integer>> productOfPrimes =

 new HashMap<Integer, Vector<Integer>>();

 

 // Every number from both the array is iterated

 // getProductOddOccuringPrimes function is called

 // and the product of odd occurring primes is

 // stored in the map productOfPrimes.

 // A pair is printed if the product is same

 for (int i = 0; i < n; ++i) {

 

 // Generating the product of odd times

 // occurring primes

 int productPrimesOfA

 = getProductOddOccuringPrimes(a[i]);

 

 // Pushing the indices to the to the

 // vector with the product of

 // odd times occurring Primes

 Vector<Integer> temp = new Vector<Integer>();

 if(productOfPrimes.containsKey(productPrimesOfA))

 for (Integer s:productOfPrimes.get(productPrimesOfA)){

 temp.add(s);

 }

 temp.add(i);

 productOfPrimes.put(productPrimesOfA, temp);

 }

 

 for (int i = 0; i < m; ++i)

 {

 

 // Generating the product of odd times

 // occurring Primes

 int productPrimesOfB

 = getProductOddOccuringPrimes(b[i]);

 

 // Checking if productPrimesOfB

 // lies in the productOfPrimes

 if (productOfPrimes.containsKey(productPrimesOfB)) {

 for (Integer itr : productOfPrimes.get(productPrimesOfB)) {

 countPairs++;

 System.out.print(" (" + b[i]+ ", "

 + a[itr]+ ") ");

 }

 }

 }

 if (countPairs <= 0)

 System.out.print("No pairs Found!");

 System.out.println();

}

 

// Driver function

public static void main(String[] args)

{

 sieve();

 

 // N, M are size of array a and b respectively

 int N = 5, M = 5;

 int a[] = { 4, 1, 6, 35, 120 };

 int b[] = { 24, 140, 4, 30, 1 };

 

 // Function that prints the pairs

 // whose product is a perfect square

 printPairs(N, M, a, b);

}

}

 

// This code is contributed by 29AjayKumar  
  
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

// C# program to print pairs whose

// product is a perfect square

using System;

using System.Collections.Generic;

 

class GFG{

 

// Maximum number upto which sieve is performed

static readonly int MAXN = 100001;

 

// Array to perform Sieve of Eratosthenes

// and store prime numbers

static int []spf = new int[MAXN];

 

// Function to perform sieve of

// eratosthenes on the array spf.

static void sieve()

{

 spf[1] = 1;

 for (int i = 2; i < MAXN; i++)

 spf[i] = i;

 

 for (int i = 4; i < MAXN; i += 2)

 spf[i] = 2;

 

 for (int i = 3; i * i < MAXN; i++) {

 if (spf[i] == i) {

 for (int j = i * i; j < MAXN; j += i)

 

 if (spf[j] == j)

 spf[j] = i;

 }

 }

}

 

// Function to return the product of the

// odd occurring prime factors of a number

static int getProductOddOccuringPrimes(int x)

{

 // Product of 1 with perfect square gives

 // perfect square, 1 is returned for x = 1

 if (x == 1)

 return 1;

 

 // Temperory container of prime factors

 List<int> ret = new List<int>();

 while (x != 1) {

 ret.Add(spf[x]);

 x = x / spf[x];

 }

 

 // ans contains the product of primes

 // which occurs odd number of times

 int count = 1, ans = 1;

 for (int i = 0, j = 1; j < ret.Count; ++j, ++i) {

 if (ret[i] != ret[j]) {

 if (count % 2 == 1)

 ans *= ret[i];

 count = 0;

 }

 count++;

 }

 

 // Checks if count is odd or not

 if (count %2 == 1)

 ans *= ret[ret.Count - 1];

 

 return ans;

}

 

// Function to print the pairs whose product is

// a perfect square

static void printPairs(int n, int m, int []a, int []b)

{

 int countPairs = 0;

 

 // For storing the indicies with same

 // product of odd times occuring Primes as key

 Dictionary<int, List<int>> productOfPrimes =

 new Dictionary<int, List<int>>();

 

 // Every number from both the array is iterated

 // getProductOddOccuringPrimes function is called

 // and the product of odd occurring primes is

 // stored in the map productOfPrimes.

 // A pair is printed if the product is same

 for (int i = 0; i < n; ++i) {

 

 // Generating the product of odd times

 // occurring primes

 int productPrimesOfA

 = getProductOddOccuringPrimes(a[i]);

 

 // Pushing the indices to the to the

 // vector with the product of

 // odd times occurring Primes

 List<int> temp = new List<int>();

 if(productOfPrimes.ContainsKey(productPrimesOfA))

 foreach (int s in productOfPrimes[productPrimesOfA]){

 temp.Add(s);

 }

 temp.Add(i);

 if(productOfPrimes.ContainsKey(productPrimesOfA))

 productOfPrimes[productPrimesOfA] = temp;

 else

 productOfPrimes.Add(productPrimesOfA, temp);

 }

 

 for (int i = 0; i < m; ++i)

 {

 

 // Generating the product of odd times

 // occurring Primes

 int productPrimesOfB

 = getProductOddOccuringPrimes(b[i]);

 

 // Checking if productPrimesOfB

 // lies in the productOfPrimes

 if (productOfPrimes.ContainsKey(productPrimesOfB)) {

 foreach (int itr in productOfPrimes[productPrimesOfB]) {

 countPairs++;

 Console.Write(" (" + b[i]+ ", "

 + a[itr]+ ") ");

 }

 }

 }

 if (countPairs <= 0)

 Console.Write("No pairs Found!");

 Console.WriteLine();

}

 

// Driver function

public static void Main(String[] args)

{

 sieve();

 

 // N, M are size of array a and b respectively

 int N = 5, M = 5;

 int []a = { 4, 1, 6, 35, 120 };

 int []b = { 24, 140, 4, 30, 1 };

 

 // Function that prints the pairs

 // whose product is a perfect square

 printPairs(N, M, a, b);

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    (24, 6)  (140, 35)  (4, 4)  (4, 1)  (30, 120)  (1, 4)  (1, 1)
    

**Time Complexity:** O(Klog(K)) where K = max(N,M)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

