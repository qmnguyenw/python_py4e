Count of ways to represent N as sum of a prime number and twice of a square



Given an integer **N** , the task is to count the number of ways so that N can
be written as the sum of a prime number and twice of a square, i.e.

![N = 2*A^{2} + P  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-bd2a96de7e15c1d360897f702f158b9c_l3.png)

, where P can be any prime number and A is any positive integer.  
 **Note:**

![N <= 10^{6}  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-bcaf5260bb55dc45756eb7539ef49b21_l3.png)

**Examples:**

  

  

> **Input:** N = 9  
> **Output:** 1  
> **Explanation:**  
> 9 can be represented as sum of prime number and twice a square in only one
> way –
>
> ![N = 9 = 7 + 2*\(1^{2}\)  ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-223179947723c05c4c3bb33885f6a7a5_l3.png)
>
> **Input:** N = 15  
> **Output:** 2  
> **Explanation:**  
> 15 can be represented as sum of prime number and twice a square in two ways
> –
>
> ![N = 15 = 7 + 2 * \(2^{2}\)  ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-77d4ff19ff0b688eb5a19ccc0048d9bf_l3.png)[Tex]N = 15 =
> 13 + 2 * (1^{2}) [/Tex]

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to use Seive of Eratosthenes to find all the primes
and then for each prime number check for every possible number starting from
1. If any prime number and twice a square is equal to the given number then
increment the count of the number of ways by 1.  
Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to count the

// number of ways a number can be

// written as sum of prime number

// and twice a square

#include <bits/stdc++.h>

using namespace std;

long long int n = 500000 - 2;

vector<long long int> v;

// Function to mark all the

// prime numbers using sieve

void sieveoferanthones()

{

 bool prime[n + 1];

 // Intially all the numbers

 // are marked as prime

 memset(prime, true,

 sizeof(prime));

 // Loop to mark the prime numbers

 // upto the Square root of N

 for (long long int i = 2; i <= sqrt(n);

 i++) {

 if (prime[i])

 for (long long int j = i * i;

 j <= n; j += i) {

 prime[j] = false;

 }

 }

 // Loop to store the prime

 // numbers in an array

 for (long long int i = 2; i < n; i++) {

 if (prime[i])

 v.push_back(i);

 }

}

// Function to find the number

// ways to represent a number

// as the sum of prime number and

// square of a number

void numberOfWays(long long int n)

{

 long long int count = 0;

 // Loop to iterate over all the

 // possible prime numbers

 for (long long int j = 1;

 2 * (pow(j, 2)) < n; j++) {

 for (long long int i = 1;

 v[i] + 2 <= n; i++) {

 // Incrment the count if

 // the given number is a

 // valid number

 if (n == v[i]

+ (2 * (pow(j, 2))))

 count++;

 }

 }

 cout << count << endl;

}

// Driver Code

int main()

{

 sieveoferanthones();

 long long int n = 9;

 // Function Call

 numberOfWays(n);

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

// Java implementation to count the

// number of ways a number can be

// written as sum of prime number

// and twice a square

import java.util.*;

class GFG{

static int n = 500000 - 2;

static Vector<Integer> v =

 new Vector<>();

// Function to mark all the

// prime numbers using sieve

static void sieveoferanthones()

{

 boolean []prime = new boolean[n + 1];

 // Intially all the numbers

 // are marked as prime

 Arrays.fill(prime, true);

 // Loop to mark the prime numbers

 // upto the Square root of N

 for (int i = 2;

 i <= Math.sqrt(n); i++)

 {

 if (prime[i])

 for (int j = i * i;

 j <= n; j += i)

 {

 prime[j] = false;

 }

 }

 // Loop to store the prime

 // numbers in an array

 for (int i = 2; i < n; i++)

 {

 if (prime[i])

 v.add(i);

 }

}

// Function to find the number

// ways to represent a number

// as the sum of prime number and

// square of a number

static void numberOfWays(int n)

{

 int count = 0;

 // Loop to iterate over all the

 // possible prime numbers

 for (int j = 1; 2 *

 (Math.pow(j, 2)) < n; j++)

 {

 for (int i = 1; v.get(i) +

 2 <= n; i++)

 {

 // Incrment the count if

 // the given number is a

 // valid number

 if (n == v.get(i) +

 (2 * (Math.pow(j, 2))))

 count++;

 }

 }

 System.out.print(count + "\n");

}

// Driver Code

public static void main(String[] args)

{

 sieveoferanthones();

 int n = 9;

 // Function Call

 numberOfWays(n);

}

}

// This code is contributed by Princi Singh  
  
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

# Python3 implementation to count the

# number of ways a number can be

# written as sum of prime number

# and twice a square

import math

n = 500000 - 2

v = []

# Function to mark all the

# prime numbers using sieve

def sieveoferanthones():

 

 prime = [1] * (n + 1)

 # Loop to mark the prime numbers

 # upto the Square root of N

 for i in range(2, int(math.sqrt(n)) + 1):

 if (prime[i] != 0):

 

 for j in range(i * i, n + 1, i):

 prime[j] = False

 

 # Loop to store the prime

 # numbers in an array

 for i in range(2, n):

 if (prime[i] != 0):

 v.append(i)

 

# Function to find the number

# ways to represent a number

# as the sum of prime number and

# square of a number

def numberOfWays(n):

 

 count = 0

 # Loop to iterate over all the

 # possible prime numbers

 j = 1

 while (2 * (pow(j, 2)) < n):

 i = 1

 while (v[i] + 2 <= n):

 # Incrment the count if

 # the given number is a

 # valid number

 if (n == v[i] +

 (2 * (math.pow(j, 2)))):

 count += 1

 

 i += 1

 

 j += 1

 

 print(count)

# Driver Code

sieveoferanthones()

n = 9

# Function call

numberOfWays(n)

# This code is contributed by sanjoy_62  
  
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

// C# implementation to count the

// number of ways a number can be

// written as sum of prime number

// and twice a square 

using System;

using System.Collections;

using System.Collections.Generic;

class GFG{ 

 

static int n = 500000 - 2;

static ArrayList v = new ArrayList();

// Function to mark all the

// prime numbers using sieve

static void sieveoferanthones()

{

 bool []prime = new bool[n + 1];

 // Intially all the numbers

 // are marked as prime

 Array.Fill(prime, true);

 // Loop to mark the prime numbers

 // upto the Square root of N

 for(int i = 2;

 i <= (int)Math.Sqrt(n); i++)

 {

 if (prime[i])

 {

 for(int j = i * i;

 j <= n; j += i)

 {

 prime[j] = false;

 }

 }

 }

 // Loop to store the prime

 // numbers in an array

 for(int i = 2; i < n; i++)

 {

 if (prime[i])

 v.Add(i);

 }

}

// Function to find the number

// ways to represent a number

// as the sum of prime number and

// square of a number

static void numberOfWays(int n)

{

 int count = 0;

 // Loop to iterate over all the

 // possible prime numbers

 for(int j = 1;

 2 * (Math.Pow(j, 2)) < n; j++)

 {

 for(int i = 1;

 (int)v[i] + 2 <= n; i++)

 {

 

 // Incrment the count if

 // the given number is a

 // valid number

 if (n == (int)v[i] +

 (2 * (Math.Pow(j, 2))))

 count++;

 }

 }

 Console.Write(count);

} 

 

// Driver Code 

public static void Main (string[] args)

{ 

 sieveoferanthones();

 int n = 9;

 // Function call

 numberOfWays(n);

} 

}

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

