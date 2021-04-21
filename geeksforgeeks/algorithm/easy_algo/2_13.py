Number of factors of very large number N modulo M where M is any prime number



Given a large number N, the task is to find the total number of factors of the
number N modulo M where M is any prime number.  
**Examples:**  

> **Input:** N = 9699690, M = 17  
> **Output:** 1  
> **Explanation:**  
> Total Number of factors of 9699690 is 256 and (256 % 17) = 1  
>  **Input:** N = 193748576239475639, M = 9  
> **Output:** 8  
> **Explanation:**  
> Total Number of factors of 9699690 is 256 and (256 % 17) = 1  
>

## Recommended: Please try your approach on _**_{IDE}_**_ first, before moving
on to the solution.

 **Definition of Factors of a number:**  
In mathematics, a factor of an integer N also called a divisor of N, is an
integer M that may be multiplied by some integer to produce N.  
Any number can be written as:  

> N = (P1A1) * (P2A2) * (P3A3) …. (PnAn)
>
>  
>
>
>  
>

  
where P1, P2, P3…Pn are distinct prime and A1, A2, A3…An are number of times
the corresponding prime number occurs.  
The general formula of total number of factors of a given number will be:  

> Factors = (1+A1) * (1+A2) * (1+A3) * … (1+An)

  
where A1, A2, A3, … An are count of distinct prime factors of N.  
Here Sieve’s implementation to find prime factorization of a large number
cannot be used because it requires proportional space.  
 **Approach:**  

  1. Count the number of times **2** is the factor of the given number N.
  2. Iterate from **3** to **√(N)** to find the number of times a prime number divides a particular number which reduces every time by **N / i**.
  3. Divide number **N** by its corresponding smallest prime factor till **N becomes 1**.
  4. Find the number of factors of the number by using the formula   

> Factors = (1+A1) * (1+A2) * (1+A3) * … (1+An)

Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// Number of factors of very

// large number N modulo M

#include <bits/stdc++.h>

using namespace std;

#define ll long long

ll mod = 1000000007;

// Function for modular

// multiplication

ll mult(ll a, ll b)

{

 return ((a % mod) *

 (b % mod)) % mod;

}

// Function to find the number

// of factors of large Number N

ll calculate_factors(ll n)

{

 ll ans, cnt;

 cnt = 0;

 ans = 1;

 

 // Count the number of times

 // 2 divides the number N

 while (n % 2 == 0) {

 cnt++;

 n = n / 2;

 }

 

 // Condition to check

 // if 2 divides it

 if (cnt) {

 ans = mult(ans, (cnt + 1));

 }

 

 // Check for all the possible

 // numbers that can divide it

 for (int i = 3; i <= sqrt(n);

 i += 2) {

 cnt = 0;

 

 // Loop to check the number

 // of times prime number

 // i divides it

 while (n % i == 0) {

 cnt++;

 n = n / i;

 }

 

 // Condition to check if

 // prime number i divides it

 if (cnt) {

 ans = mult(ans, (cnt + 1));

 }

 }

 // Condition to check if N

 // at the end is a prime number.

 if (n > 2) {

 ans = mult(ans, (2));

 }

 return ans % mod;

}

// Driver Code

int main()

{

 ll n = 193748576239475639;

 mod = 17;

 cout << calculate_factors(n) << endl;

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

// Java implementation to find the

// Number of factors of very

// large number N modulo M

class GFG{

 

static long mod = 1000000007L;

 

// Function for modular

// multiplication

static long mult(long a, long b)

{

 return ((a % mod) *

 (b % mod)) % mod;

}

 

// Function to find the number

// of factors of large Number N

static long calculate_factors(long n)

{

 long ans, cnt;

 cnt = 0;

 ans = 1;

 

 // Count the number of times

 // 2 divides the number N

 while (n % 2 == 0) {

 cnt++;

 n = n / 2;

 }

 

 // Condition to check

 // if 2 divides it

 if (cnt % 2 == 1) {

 ans = mult(ans, (cnt + 1));

 }

 

 // Check for all the possible

 // numbers that can divide it

 for (int i = 3; i <= Math.sqrt(n);

 i += 2) {

 cnt = 0;

 

 // Loop to check the number

 // of times prime number

 // i divides it

 while (n % i == 0) {

 cnt++;

 n = n / i;

 }

 

 // Condition to check if

 // prime number i divides it

 if (cnt % 2 == 1) {

 ans = mult(ans, (cnt + 1));

 }

 }

 // Condition to check if N

 // at the end is a prime number.

 if (n > 2) {

 ans = mult(ans, (2));

 }

 return ans % mod;

}

 

// Driver Code

public static void main(String[] args)

{

 long n = 193748576239475639L;

 mod = 17;

 

 System.out.print(calculate_factors(n) +"\n");

}

}

// This code is contributed by sapnasingh4991  
  
---  
  
 __

 __

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 implementation to find the

# Number of factors of very

# large number N modulo M

from math import sqrt

mod = 1000000007

# Function for modular

# multiplication

def mult(a, b):

 return ((a % mod) * (b % mod)) % mod

# Function to find the number

# of factors of large Number N

def calculate_factors(n):

 cnt = 0

 ans = 1

 

 # Count the number of times

 # 2 divides the number N

 while (n % 2 == 0):

 cnt += 1

 n = n // 2

 

 # Condition to check

 # if 2 divides it

 if (cnt):

 ans = mult(ans, (cnt + 1))

 

 # Check for all the possible

 # numbers that can divide it

 for i in range(3, int(sqrt(n)), 2):

 cnt = 0

 

 # Loop to check the number

 # of times prime number

 # i divides it

 while (n % i == 0):

 cnt += 1

 n = n // i

 

 # Condition to check if

 # prime number i divides it

 if (cnt):

 ans = mult(ans, (cnt + 1))

 # Condition to check if N

 # at the end is a prime number.

 if (n > 2):

 ans = mult(ans, 2)

 return ans % mod

# Driver Code

if __name__ == '__main__':

 n = 19374857

 mod = 17

 print(calculate_factors(n))

# This code is contributed by Surendra_Gangwar  
  
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

// C# implementation to find the

// Number of factors of very

// large number N modulo M

using System;

class GFG{

 

static long mod = 1000000007L;

 

// Function for modular

// multiplication

static long mult(long a, long b)

{

 return ((a % mod) *

 (b % mod)) % mod;

}

 

// Function to find the number

// of factors of large Number N

static long calculate_factors(long n)

{

 long ans, cnt;

 cnt = 0;

 ans = 1;

 

 // Count the number of times

 // 2 divides the number N

 while (n % 2 == 0) {

 cnt++;

 n = n / 2;

 }

 

 // Condition to check

 // if 2 divides it

 if (cnt % 2 == 1) {

 ans = mult(ans, (cnt + 1));

 }

 

 // Check for all the possible

 // numbers that can divide it

 for (int i = 3; i <= Math.Sqrt(n);

 i += 2) {

 cnt = 0;

 

 // Loop to check the number

 // of times prime number

 // i divides it

 while (n % i == 0) {

 cnt++;

 n = n / i;

 }

 

 // Condition to check if

 // prime number i divides it

 if (cnt % 2 == 1) {

 ans = mult(ans, (cnt + 1));

 }

 }

 // Condition to check if N

 // at the end is a prime number.

 if (n > 2) {

 ans = mult(ans, (2));

 }

 return ans % mod;

}

 

// Driver Code

public static void Main(String[] args)

{

 long n = 193748576239475639L;

 mod = 17;

 

 Console.Write(calculate_factors(n) +"\n");

}

}

// This code is contributed by sapnasingh4991  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// javascript implementation to find the

// Number of factors of very

// large number N modulo M

 

mod = 1000000007;

 

// Function for modular

// multiplication

function mult( a , b)

{

 return ((a % mod) *

 (b % mod)) % mod;

}

 

// Function to find the number

// of factors of large Number N

function calculate_factors( n)

{

 var ans, cnt;

 cnt = 0;

 ans = 1;

 

 // Count the number of times

 // 2 divides the number N

 while (n % 2 == 0) {

 cnt++;

 n = n / 2;

 }

 

 // Condition to check

 // if 2 divides it

 if (cnt % 2 == 1) {

 ans = mult(ans, (cnt + 1));

 }

 

 // Check for all the possible

 // numbers that can divide it

 for (i = 3; i <= Math.sqrt(n);

 i += 2) {

 cnt = 0;

 

 // Loop to check the number

 // of times prime number

 // i divides it

 while (n % i == 0) {

 cnt++;

 n = n / i;

 }

 

 // Condition to check if

 // prime number i divides it

 if (cnt % 2 == 1) {

 ans = mult(ans, (cnt + 1));

 }

 }

 // Condition to check if N

 // at the end is a prime number.

 if (n > 2) {

 ans = mult(ans, (2));

 }

 return ans % mod;

}

 

// Driver Code

var n = 193748576239475639;

mod = 17;

document.write(calculate_factors(n));

// This code contributed by shikhasingrajput

</script>  
  
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

