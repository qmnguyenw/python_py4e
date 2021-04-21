Find element that maximizes LCM of an Array in the range 1 to M



Given an array **arr** of size **N** containing numbers in the range **[1,
M]** , the task is to find an element, in the range **[1, M]** , which
maximises the LCM.

 **Examples:**

>  **Input:** arr[]={3, 4, 2, 7}, M = 8  
>  **Output:** 5  
>  **Explanation:**  
>  The LCM of existing array (3, 4, 2, 7) = 84  
> Adding the remaining numbers in 1 to 8 and check the corresponding LCM of
> the resulting array.  
> 1: LCM of(1, 3, 4, 2, 7) is 84  
> 5: LCM of(5, 3, 4, 2, 7) is 420  
> 6: LCM of(6, 3, 4, 2, 7) is 84  
> 8: LCM of(5, 3, 4, 2, 7) is 168  
> Clearly, adding 5 maximizes the LCM.
>
>  **Input:** arr[]={2, 5, 3, 8, 1}, M = 9  
>  **Output:** 7

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:**

  

  

  * Calculate the LCM of the given array.
  * Calculate the LCM after adding each element in the range **[1, M]** not present in the array and return the element for which it is maximum.

 **Efficient Approach:**

  * Precompute the prime factors, of numbers till 1000, using Sieve.
  * Store the frequency of every prime factor of the LCM of the given array.
  * Iterate from values [1, M] and for every value not present in the array, calculate the **product of differences in the frequencies of prime factors of that number and that of the LCM** of the given array.
  * Return the element which provides the maximum product.

Below code is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the element

// to be added to maximize the LCM

 

#include <bits/stdc++.h>

using namespace std;

 

// Vector which stores the prime factors

// of all the numbers upto 10000

vector<int> primeFactors[10001];

set<int> s;

 

// Function which finds prime

// factors using sieve method

void findPrimeFactors()

{

 

 // Boolean array which stores

 // true if the index is prime

 bool primes[10001];

 memset(primes, true, sizeof(primes));

 

 // Sieve of Eratosthenes

 for (int i = 2; i < 10001; i++) {

 

 if (primes[i]) {

 for (int j = i; j < 10001; j += i) {

 

 if (j != i) {

 primes[j] = false;

 }

 primeFactors[j].push_back(i);

 }

 }

 }

}

 

// Function which stores frequency of every

// prime factor of LCM of the initial array

void primeFactorsofLCM(int* frequecyOfPrimes,

 int* arr, int n)

{

 

 for (int i = 0; i < n; i++) {

 for (auto a : primeFactors[arr[i]]) {

 

 int k = 0;

 

 // While the prime factor

 // divides the number

 while ((arr[i] % a) == 0) {

 arr[i] /= a;

 k++;

 }

 

 frequecyOfPrimes[a]

 = max(frequecyOfPrimes[a], k);

 }

 }

}

 

// Function which returns the element

// which should be added to array

int elementToBeAdded(int* frequecyOfPrimes, int m)

{

 int product = 1;

 

 // To store the final answer

 int ans = 1;

 

 for (int i = 2; i <= m; i++) {

 

 if (s.find(i) != s.end())

 continue;

 

 int j = i;

 int current = 1;

 

 for (auto a : primeFactors[j]) {

 

 int k = 0;

 

 // While the prime factor

 // divides the number

 while ((j % a) == 0) {

 

 j /= a;

 k++;

 if (k > frequecyOfPrimes[a]) {

 current *= a;

 }

 }

 }

 

 // Check element which provides

 // the maximum product

 if (current > product) {

 product = current;

 ans = i;

 }

 }

 return ans;

}

 

void findElement(int* arr, int n, int m)

{

 

 for (int i = 0; i < n; i++)

 s.insert(arr[i]);

 int frequencyOfPrimes[10001] = { 0 };

 primeFactorsofLCM(frequencyOfPrimes, arr, n);

 cout << elementToBeAdded(frequencyOfPrimes, m)

 << endl;

}

 

// Driver code

int main()

{

 // Precomputing the prime factors

 // of all numbers upto 10000

 findPrimeFactors();

 

 int N = 5;

 int M = 9;

 int arr[] = { 2, 5, 3, 8, 1 };

 

 findElement(arr, N, M);

 

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

// Java program to find the element

// to be added to maximize the LCM 

import java.util.*;

 

class GFG{ 

 

// Vector which stores the prime factors 

// of all the numbers upto 10000 

static Vector<Integer> []primeFactors = new Vector[10001]; 

static HashSet<Integer> s = new HashSet<Integer>(); 

 

// Function which finds prime 

// factors using sieve method 

static void findPrimeFactors() 

{ 

 

 // Boolean array which stores 

 // true if the index is prime 

 boolean []primes = new boolean[10001]; 

 Arrays.fill(primes, true); 

 

 // Sieve of Eratosthenes 

 for (int i = 2; i < 10001; i++) { 

 

 if (primes[i]) { 

 for (int j = i; j < 10001; j += i) { 

 

 if (j != i) { 

 primes[j] = false; 

 } 

 primeFactors[j].add(i); 

 } 

 } 

 } 

} 

 

// Function which stores frequency of every 

// prime factor of LCM of the initial array 

static void primeFactorsofLCM(int []frequecyOfPrimes, 

 int[] arr, int n) 

{ 

 

 for (int i = 0; i < n; i++) { 

 for (int a : primeFactors[arr[i]]) { 

 

 int k = 0; 

 

 // While the prime factor 

 // divides the number 

 while ((arr[i] % a) == 0) { 

 arr[i] /= a; 

 k++; 

 } 

 

 frequecyOfPrimes[a] 

 = Math.max(frequecyOfPrimes[a], k); 

 } 

 } 

} 

 

// Function which returns the element 

// which should be added to array 

static int elementToBeAdded(int []frequecyOfPrimes, int m) 

{ 

 int product = 1; 

 

 // To store the final answer 

 int ans = 1; 

 

 for (int i = 2; i <= m; i++) { 

 

 if (s.contains(i)) 

 continue; 

 

 int j = i; 

 int current = 1; 

 

 for (int a : primeFactors[j]) { 

 

 int k = 0; 

 

 // While the prime factor 

 // divides the number 

 while ((j % a) == 0) { 

 

 j /= a; 

 k++; 

 if (k > frequecyOfPrimes[a]) { 

 current *= a; 

 } 

 } 

 } 

 

 // Check element which provides 

 // the maximum product 

 if (current > product) { 

 product = current; 

 ans = i; 

 } 

 } 

 return ans; 

} 

 

static void findElement(int[] arr, int n, int m) 

{ 

 

 for (int i = 0; i < n; i++) 

 s.add(arr[i]); 

 int frequencyOfPrimes[] = new int[10001]; 

 primeFactorsofLCM(frequencyOfPrimes, arr, n); 

 System.out.print(elementToBeAdded(frequencyOfPrimes, m) 

 +"\n"); 

} 

 

// Driver code 

public static void main(String[] args) 

{ 

 for (int i = 0; i < 10001; i++) 

 primeFactors[i] = new Vector<Integer>();

 // Precomputing the prime factors 

 // of all numbers upto 10000 

 findPrimeFactors(); 

 

 int N = 5; 

 int M = 9; 

 int arr[] = { 2, 5, 3, 8, 1 }; 

 

 findElement(arr, N, M); 

}

} 

 

// This code is contributed by Rajput-Ji  
  
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

// C# program to find the element

// to be added to maximize the LCM 

using System;

using System.Collections.Generic;

 

class GFG{ 

 

// List which stores the prime factors 

// of all the numbers upto 10000 

static List<int> []primeFactors = new List<int>[10001]; 

static HashSet<int> s = new HashSet<int>(); 

 

// Function which finds prime 

// factors using sieve method 

static void findPrimeFactors() 

{ 

 

 // Boolean array which stores 

 // true if the index is prime 

 bool []primes = new bool[10001]; 

 for (int i = 0; i < 10001; i++) 

 primes[i] = true;

 

 // Sieve of Eratosthenes 

 for (int i = 2; i < 10001; i++) { 

 

 if (primes[i]) { 

 for (int j = i; j < 10001; j += i) { 

 

 if (j != i) { 

 primes[j] = false; 

 } 

 primeFactors[j].Add(i); 

 } 

 } 

 } 

} 

 

// Function which stores frequency of every 

// prime factor of LCM of the initial array 

static void primeFactorsofLCM(int []frequecyOfPrimes, 

 int[] arr, int n) 

{ 

 

 for (int i = 0; i < n; i++) { 

 foreach (int a in primeFactors[arr[i]]) { 

 

 int k = 0; 

 

 // While the prime factor 

 // divides the number 

 while ((arr[i] % a) == 0) { 

 arr[i] /= a; 

 k++; 

 } 

 

 frequecyOfPrimes[a] 

 = Math.Max(frequecyOfPrimes[a], k); 

 } 

 } 

} 

 

// Function which returns the element 

// which should be added to array 

static int elementToBeAdded(int []frequecyOfPrimes, int m) 

{ 

 int product = 1; 

 

 // To store the readonly answer 

 int ans = 1; 

 

 for (int i = 2; i <= m; i++) { 

 

 if (s.Contains(i)) 

 continue; 

 

 int j = i; 

 int current = 1; 

 

 foreach (int a in primeFactors[j]) { 

 

 int k = 0; 

 

 // While the prime factor 

 // divides the number 

 while ((j % a) == 0) { 

 

 j /= a; 

 k++; 

 if (k > frequecyOfPrimes[a]) { 

 current *= a; 

 } 

 } 

 } 

 

 // Check element which provides 

 // the maximum product 

 if (current > product) { 

 product = current; 

 ans = i; 

 } 

 } 

 return ans; 

} 

 

static void findElement(int[] arr, int n, int m) 

{ 

 

 for (int i = 0; i < n; i++) 

 s.Add(arr[i]); 

 int []frequencyOfPrimes = new int[10001]; 

 primeFactorsofLCM(frequencyOfPrimes, arr, n); 

 Console.Write(elementToBeAdded(frequencyOfPrimes, m) 

 +"\n"); 

} 

 

// Driver code 

public static void Main(String[] args) 

{ 

 for (int i = 0; i < 10001; i++) 

 primeFactors[i] = new List<int>();

 

 // Precomputing the prime factors 

 // of all numbers upto 10000 

 findPrimeFactors(); 

 

 int N = 5; 

 int M = 9; 

 int []arr = { 2, 5, 3, 8, 1 }; 

 

 findElement(arr, N, M); 

}

} 

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    7
    

**Time Complexity:** O(N * log N + M * log M)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

