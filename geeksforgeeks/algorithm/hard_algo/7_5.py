Number of divisors of product of N numbers



Given an array **arr[]** of integers, the task is to count the number of
divisors of product of all the elements from given array.  
 **Examples:**  

> **Input:** arr[] = {3, 5, 7}  
> **Output:** 8  
> 3 * 5 * 7 = 105.  
> Factors of 105 are 1, 3, 5, 7, 15, 21, 35 and 105.  
>  **Input:** arr[] = {5, 5}  
> **Output:** 3  
> 5 * 5 = 25.  
> Factors of 25 are 1, 5 and 25.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

A **simple solution** is to multiply all the **N** integers and count the
number of divisors of the product. However, if the product goes above **10 7**
then we can’t use this approach because numbers greater than 10^7 can’t be
prime factorized efficiently using the sieve approach.  
An **efficient solution** does not involve the calculation of the product of
all the numbers. We already know that when we multiply 2 numbers, powers get
added. For example,  

> A = 27, B = 23  
> A * B = 210  
> Therefore, we need to maintain the count of every power in the product of
> numbers which can be done by adding counts of powers from every element.  
>
>
>  
>
>
>  
>

Hence, to compute the number of divisors, the main focus is on the count of
primes encountered. So we will stress only on the primes encountered in the
product without bothering about the product itself. While traversing through
the array, we keep the count of every prime encountered.  

> Number of divisors = **(p 1 \+ 1) * (p2 \+ 1) * (p3 \+ 1) * … * (pn \+ 1)**  
> where p1, p2, p3, …, pn are the primes encountered in the prime
> factorization of all the elements.  
>

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

#define MAX 10000002

using namespace std;

int prime[MAX];

// Array to store count of primes

int prime_count[MAX];

// Function to store smallest prime factor

// of every number till MAX

void sieve()

{

 memset(prime, 0, sizeof(prime));

 prime[0] = prime[1] = 1;

 for (int i = 2; i * i < MAX; i++) {

 if (prime[i] == 0) {

 for (int j = i * 2; j < MAX; j += i) {

 if (prime[j] == 0)

 prime[j] = i;

 }

 }

 }

 for (int i = 2; i < MAX; i++) {

 // If the number is prime then it's

 // smallest prime factor is the number

 // itself

 if (prime[i] == 0)

 prime[i] = i;

 }

}

// Function to return the count of the divisors for

// the product of all the numbers from the array

long long numberOfDivisorsOfProduct(const int* arr,

 int n)

{

 memset(prime_count, 0, sizeof(prime_count));

 for (int i = 0; i < n; i++) {

 int temp = arr[i];

 while (temp != 1) {

 // Increase the count of prime

 // encountered

 prime_count[prime[temp]]++;

 temp = temp / prime[temp];

 }

 }

 long long ans = 1;

 // Multiplying the count of primes

 // encountered

 for (int i = 2; i < MAX; i++) {

 ans = ans * (prime_count[i] + 1);

 }

 return ans;

}

// Driver code

int main()

{

 sieve();

 int arr[] = { 2, 4, 6 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << numberOfDivisorsOfProduct(arr, n);

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

// Java implementation of the approach

import java.util.Arrays;

// Java implementation of the approach

class GFG {

 final static int MAX = 10000002;

 static int prime[] = new int[MAX];

// Array to store count of primes

 static int prime_count[] = new int[MAX];

// Function to store smallest prime factor

// of every number till MAX

 static void sieve() {

 Arrays.fill(prime, 0, MAX, 0);

 prime[0] = prime[1] = 1;

 for (int i = 2; i * i < MAX; i++) {

 if (prime[i] == 0) {

 for (int j = i * 2; j < MAX; j += i) {

 if (prime[j] == 0) {

 prime[j] = i;

 }

 }

 }

 }

 for (int i = 2; i < MAX; i++) {

 // If the number is prime then it's

 // smallest prime factor is the number

 // itself

 if (prime[i] == 0) {

 prime[i] = i;

 }

 }

 }

// Function to return the count of the divisors for

// the product of all the numbers from the array

 static long numberOfDivisorsOfProduct(int[] arr,

 int n) {

 Arrays.fill(prime_count, 0, MAX, 0);

 for (int i = 0; i < n; i++) {

 int temp = arr[i];

 while (temp != 1) {

 // Increase the count of prime

 // encountered

 prime_count[prime[temp]]++;

 temp = temp / prime[temp];

 }

 }

 long ans = 1;

 // Multiplying the count of primes

 // encountered

 for (int i = 2; i < MAX; i++) {

 ans = ans * (prime_count[i] + 1);

 }

 return ans;

 }

// Driver code

 public static void main(String[] args) {

 sieve();

 int arr[] = {2, 4, 6};

 int n = arr.length;

 System.out.println(numberOfDivisorsOfProduct(arr, n));

 }

}

// This code is contributed by 29AjayKumar  
  
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

# Python3 implementation of the approach

MAX = 10000002

prime = [0] * (MAX)

MAX_sqrt = int(MAX ** (0.5))

# Array to store count of primes

prime_count = [0] * (MAX)

# Function to store smallest prime

# factor in prime[]

def sieve():

 prime[0], prime[1] = 1, 1

 for i in range(2, MAX_sqrt):

 if prime[i] == 0:

 for j in range(i * 2, MAX, i):

 if prime[j] == 0:

 prime[j] = i

 

 for i in range(2, MAX):

 # If the number is prime then it's

 # the smallest prime factor is the

 # number itself

 if prime[i] == 0:

 prime[i] = i

# Function to return the count of the divisors for

# the product of all the numbers from the array

def numberOfDivisorsOfProduct(arr, n):

 for i in range(0, n):

 temp = arr[i]

 while temp != 1:

 # Increase the count of prime

 # encountered

 prime_count[prime[temp]] += 1

 temp = temp // prime[temp]

 ans = 1

 # Multiplying the count of primes

 # encountered

 for i in range(2, len(prime_count)):

 ans = ans * (prime_count[i] + 1)

 

 return ans

# Driver code

if __name__ == "__main__":

 sieve()

 arr = [2, 4, 6]

 n = len(arr)

 print(numberOfDivisorsOfProduct(arr, n))

# This code is contributed by Rituraj Jain  
  
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

// C# implementation of the approach

using System;

public class GFG {

 static int MAX = 1000000;

 static int []prime = new int[MAX];

// Array to store count of primes

 static int []prime_count = new int[MAX];

// Function to store smallest prime factor

// of every number till MAX

 static void sieve() { 

 for(int i =0;i<MAX;i++)

 prime[i]=0;

 prime[0] = prime[1] = 1;

 for (int i = 2; i * i < MAX; i++) {

 if (prime[i] == 0) {

 for (int j = i * 2; j < MAX; j += i) {

 if (prime[j] == 0) {

 prime[j] = i;

 }

 }

 }

 }

 for (int i = 2; i < MAX; i++) {

 // If the number is prime then it's

 // smallest prime factor is the number

 // itself

 if (prime[i] == 0) {

 prime[i] = i;

 }

 }

 }

// Function to return the count of the divisors for

// the product of all the numbers from the array

 static long numberOfDivisorsOfProduct(int[] arr,

 int n) { 

 for(int i =0;i<MAX;i++)

 prime_count[i]=0;

 for (int i = 0; i < n; i++) {

 int temp = arr[i];

 while (temp != 1) {

 // Increase the count of prime

 // encountered

 prime_count[prime[temp]]++;

 temp = temp / prime[temp];

 }

 }

 long ans = 1;

 // Multiplying the count of primes

 // encountered

 for (int i = 2; i < MAX; i++) {

 ans = ans * (prime_count[i] + 1);

 }

 return ans;

 }

// Driver code

 public static void Main() {

 sieve();

 int []arr = {2, 4, 6};

 int n = arr.Length;

 Console.Write(numberOfDivisorsOfProduct(arr, n));

 }

}

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    10

In a **memory efficient** approach, the array can be replaced by an
**unordered map** to store count of only those primes which have been
encountered.  
Below is the implementation of the memory efficient approach:  

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

#define MAX 10000002

using namespace std;

int prime[MAX];

// Map to store count of primes

unordered_map<int, int> prime_count;

// Function to store smallest prime factor

// in prime[]

void sieve()

{

 memset(prime, 0, sizeof(prime));

 prime[0] = prime[1] = 1;

 for (int i = 2; i * i < MAX; i++) {

 if (prime[i] == 0) {

 for (int j = i * 2; j < MAX; j += i) {

 if (prime[j] == 0)

 prime[j] = i;

 }

 }

 }

 for (int i = 2; i < MAX; i++) {

 // If the number is prime then

 // it's the smallest prime factor

 // is the number itself

 if (prime[i] == 0)

 prime[i] = i;

 }

}

// Function to return the count of the divisors for

// the product of all the numbers from the array

long long numberOfDivisorsOfProduct(const int* arr,

 int n)

{

 for (int i = 0; i < n; i++) {

 int temp = arr[i];

 while (temp != 1) {

 // Increase the count of prime

 // encountered

 prime_count[prime[temp]]++;

 temp = temp / prime[temp];

 }

 }

 long long ans = 1;

 // Multiplying the count of primes

 // encountered

 unordered_map<int, int>::iterator it;

 for (it = prime_count.begin();

 it != prime_count.end(); it++) {

 ans = ans * (it->second + 1);

 }

 return ans;

}

// Driver code

int main()

{

 sieve();

 int arr[] = { 3, 5, 7 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << numberOfDivisorsOfProduct(arr, n);

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

// Java implementation of the approach

import java.util.*;

class GFG

{

static int MAX = 10000002;

static int []prime = new int[MAX];

// Map to store count of primes

static Map<Integer, Integer> prime_count = new HashMap<>();

// Function to store smallest prime factor

// in prime[]

static void sieve()

{

 prime[0] = 1;

 prime[1] = 1;

 for (int i = 2; i * i < MAX; i++)

 {

 if (prime[i] == 0)

 {

 for (int j = i * 2; j < MAX; j += i)

 {

 if (prime[j] == 0)

 prime[j] = i;

 }

 }

 }

 for (int i = 2; i < MAX; i++)

 {

 // If the number is prime then

 // it's the smallest prime factor

 // is the number itself

 if (prime[i] == 0)

 prime[i] = i;

 }

}

// Function to return the count of the divisors for

// the product of all the numbers from the array

static long numberOfDivisorsOfProduct(int arr[],

 int n)

{

 for (int i = 0; i < n; i++)

 {

 int temp = arr[i];

 while (temp != 1)

 {

 // Increase the count of prime

 // encountered

 if(!prime_count.containsKey(prime[temp]))

 {

 prime_count.put(prime[temp], 0); 

 }

 prime_count.put(prime[temp], prime_count.get(prime[temp]) + 1);

 temp = temp / prime[temp];

 }

 }

 long ans = 1;

 // Multiplying the count of primes

 // encountered

 for(Map.Entry<Integer,Integer> it : prime_count.entrySet())

 {

 ans = ans * (it.getValue() + 1);

 }

 return ans;

}

// Driver code

public static void main(String []args)

{

 sieve();

 int arr[] = new int[] { 3, 5, 7 };

 int n = arr.length;

 System.out.print(numberOfDivisorsOfProduct(arr, n));

}

}

// This code is contributed by rutvik_56.  
  
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

# Python3 implementation of the approach

from collections import defaultdict

MAX = 10000002

prime = [0] * (MAX)

MAX_sqrt = int(MAX ** (0.5))

# Map to store count of primes

prime_count = defaultdict(lambda:0)

# Function to store smallest prime

# factor in prime[]

def sieve():

 prime[0], prime[1] = 1, 1

 for i in range(2, MAX_sqrt):

 if prime[i] == 0:

 for j in range(i * 2, MAX, i):

 if prime[j] == 0:

 prime[j] = i

 

 for i in range(2, MAX):

 # If the number is prime then

 # it's the smallest prime factor

 # is the number itself

 if prime[i] == 0:

 prime[i] = i

# Function to return the count of the divisors for

# the product of all the numbers from the array

def numberOfDivisorsOfProduct(arr, n):

 for i in range(0, n):

 temp = arr[i]

 while temp != 1:

 # Increase the count of prime

 # encountered

 prime_count[prime[temp]] += 1

 temp = temp // prime[temp]

 ans = 1

 # Multiplying the count of primes

 # encountered

 for key in prime_count:

 ans = ans * (prime_count[key] + 1)

 

 return ans

# Driver code

if __name__ == "__main__":

 sieve()

 arr = [3, 5, 7]

 n = len(arr)

 print(numberOfDivisorsOfProduct(arr, n))

# This code is contributed by Rituraj Jain  
  
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

// C# implementation of the approach

using System;

using System.Collections;

using System.Collections.Generic;

class GFG

{

 static int MAX = 10000002;

 static int []prime = new int[MAX];

 // Map to store count of primes

 static Dictionary<int,int> prime_count = new
Dictionary<int,int>();

 // Function to store smallest prime factor

 // in prime[]

 static void sieve()

 {

 prime[0] = 1;

 prime[1] = 1;

 for (int i = 2; i * i < MAX; i++)

 {

 if (prime[i] == 0)

 {

 for (int j = i * 2; j < MAX; j += i)

 {

 if (prime[j] == 0)

 prime[j] = i;

 }

 }

 }

 for (int i = 2; i < MAX; i++)

 {

 // If the number is prime then

 // it's the smallest prime factor

 // is the number itself

 if (prime[i] == 0)

 prime[i] = i;

 }

 }

 // Function to return the count of the divisors for

 // the product of all the numbers from the array

 static long numberOfDivisorsOfProduct(int []arr,

 int n)

 {

 for (int i = 0; i < n; i++)

 {

 int temp = arr[i];

 while (temp != 1)

 {

 // Increase the count of prime

 // encountered

 if(!prime_count.ContainsKey(prime[temp]))

 {

 prime_count[prime[temp]] = 0; 

 }

 prime_count[prime[temp]] += 1; 

 temp = temp / prime[temp];

 }

 }

 long ans = 1;

 // Multiplying the count of primes

 // encountered

 foreach(KeyValuePair<int,int> it in prime_count)

 {

 ans = ans * (it.Value + 1);

 }

 return ans;

 }

 // Driver code

 public static void Main(string []args)

 {

 sieve();

 int []arr = new int[] { 3, 5, 7 };

 int n = arr.Length;

 Console.Write(numberOfDivisorsOfProduct(arr, n));

 }

}

// This code is contributed by pratham76.  
  
---  
  
 __

 __

 **Output:**

    
    
    8

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

