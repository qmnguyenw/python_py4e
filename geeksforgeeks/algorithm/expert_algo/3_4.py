Print numbers such that no two consecutive numbers are co-prime and every
three consecutive numbers are co-prime



Given an integer **N** , the task is to print **N** integers **≤ 10 9** such
that no two consecutive of these integers are co-prime and every 3 consecutive
are co-prime.  
 **Examples:**

> **Input:** N = 3  
> **Output:** 6 15 10  
>  **Input:** N = 4  
> **Output:** 6 15 35 14  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:**

  * We can just multiply consecutive primes and for the last number just multiply the **gcd(last, last-1) * 2**. We do this so that the **(n – 1) th** number, **nth** and **1st** number can also follow the property mentioned in the problem statement.
  * Another important part of the problem is the fact that the numbers should be **≤ 10 9**. If you just multiply consecutive prime numbers, after around 3700 numbers the value will cross 109. So we need to only use those prime numbers whose product won’t cross 109.
  * To do this efficiently, consider a small number of primes say the first 550 primes, and select them in a way such that on making a product no number gets repeated. We first choose every prime consecutively and then choose the primes with an interval of 2 and then 3 and so on, doing that we already make sure that no number gets repeated.

> So we will select  
> 5, 11, 17, …  
> Next time, we can start with 7 and select,  
> 7, 13, 19, …  
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

using namespace std;

#define limit 1000000000

#define MAX_PRIME 2000000

#define MAX 1000000

#define I_MAX 50000

map<int, int> mp;

int b[MAX];

int p[MAX];

int j = 0;

bool prime[MAX_PRIME + 1];

// Function to generate Sieve of

// Eratosthenes

void SieveOfEratosthenes(int n)

{

 memset(prime, true, sizeof(prime));

 for (int p = 2; p * p <= n; p++) {

 // If prime[p] is not changed,

 // then it is a prime

 if (prime[p] == true) {

 for (int i = p * p; i <= n; i += p)

 prime[i] = false;

 }

 }

 // Add the prime numbers to the array b

 for (int p = 2; p <= n; p++) {

 if (prime[p]) {

 b[j++] = p;

 }

 }

}

// Function to return the gcd of a and b

int gcd(int a, int b)

{

 if (b == 0)

 return a;

 return gcd(b, a % b);

}

// Function to print the required

// sequence of integers

void printSeries(int n)

{

 SieveOfEratosthenes(MAX_PRIME);

 int i, g, k, l, m, d;

 int ar[I_MAX + 2];

 for (i = 0; i < j; i++) {

 if ((b[i] * b[i + 1]) > limit)

 break;

 // Including the primes in a series

 // of primes which will be later

 // multiplied

 p[i] = b[i];

 // This is done to mark a product

 // as existing

 mp[b[i] * b[i + 1]] = 1;

 }

 // Maximum number of primes that we consider

 d = 550;

 bool flag = false;

 // For different interval

 for (k = 2; (k < d - 1) && !flag; k++) {

 // For different starting index of jump

 for (m = 2; (m < d) && !flag; m++) {

 // For storing the numbers

 for (l = m + k; l < d; l += k) {

 // Checking for occurrence of a

 // product. Also checking for the

 // same prime occurring consecutively

 if (((b[l] * b[l + k]) < limit)

 && (l + k) < d && p[i - 1] != b[l + k]

 && p[i - 1] != b[l] && mp[b[l] * b[l + k]] != 1) {

 if (mp[p[i - 1] * b[l]] != 1) {

 // Including the primes in a

 // series of primes which will

 // be later multiplied

 p[i] = b[l];

 mp[p[i - 1] * b[l]] = 1;

 i++;

 }

 }

 if (i >= I_MAX) {

 flag = true;

 break;

 }

 }

 }

 }

 for (i = 0; i < n; i++)

 ar[i] = p[i] * p[i + 1];

 for (i = 0; i < n - 1; i++)

 cout << ar[i] << " ";

 g = gcd(ar[n - 1], ar[n - 2]);

 cout << g * 2 << endl;

}

// Driver Code

int main()

{

 int n = 4;

 printSeries(n);

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

static int limit = 1000000000;

static int MAX_PRIME = 2000000;

static int MAX = 1000000;

static int I_MAX = 50000;

static HashMap<Integer,

 Integer> mp = new HashMap<Integer,

 Integer>();

static int []b = new int[MAX];

static int []p = new int[MAX];

static int j = 0;

static boolean []prime = new boolean[MAX_PRIME + 1];

// Function to generate Sieve of

// Eratosthenes

static void SieveOfEratosthenes(int n)

{

 for(int i = 0; i < MAX_PRIME + 1; i++)

 prime[i] = true;

 for (int p = 2; p * p <= n; p++)

 {

 // If prime[p] is not changed,

 // then it is a prime

 if (prime[p] == true)

 {

 for (int i = p * p; i <= n; i += p)

 prime[i] = false;

 }

 }

 // Add the prime numbers to the array b

 for (int p = 2; p <= n; p++)

 {

 if (prime[p])

 {

 b[j++] = p;

 }

 }

}

// Function to return the gcd of a and b

static int gcd(int a, int b)

{

 if (b == 0)

 return a;

 return gcd(b, a % b);

}

// Function to print the required

// sequence of integers

static void printSeries(int n)

{

 SieveOfEratosthenes(MAX_PRIME);

 int i, g, k, l, m, d;

 int []ar = new int[I_MAX + 2];

 for (i = 0; i < j; i++)

 {

 if ((b[i] * b[i + 1]) > limit)

 break;

 // Including the primes in a series

 // of primes which will be later

 // multiplied

 p[i] = b[i];

 // This is done to mark a product

 // as existing

 mp.put(b[i] * b[i + 1], 1);

 }

 // Maximum number of primes that we consider

 d = 550;

 boolean flag = false;

 // For different interval

 for (k = 2; (k < d - 1) && !flag; k++)

 {

 // For different starting index of jump

 for (m = 2; (m < d) && !flag; m++)

 {

 // For storing the numbers

 for (l = m + k; l < d; l += k)

 {

 // Checking for occurrence of a

 // product. Also checking for the

 // same prime occurring consecutively

 if (((b[l] * b[l + k]) < limit) &&

 mp.containsKey(b[l] * b[l + k]) &&

 mp.containsKey(p[i - 1] * b[l]) &&

 (l + k) < d && p[i - 1] != b[l + k] &&

 p[i - 1] != b[l] &&

 mp.get(b[l] * b[l + k]) != 1)

 {

 if (mp.get(p[i - 1] * b[l]) != 1)

 {

 // Including the primes in a

 // series of primes which will

 // be later multiplied

 p[i] = b[l];

 mp.put(p[i - 1] * b[l], 1);

 i++;

 }

 }

 if (i >= I_MAX)

 {

 flag = true;

 break;

 }

 }

 }

 }

 for (i = 0; i < n; i++)

 ar[i] = p[i] * p[i + 1];

 for (i = 0; i < n - 1; i++)

 System.out.print(ar[i]+" ");

 g = gcd(ar[n - 1], ar[n - 2]);

 System.out.print(g * 2);

}

// Driver Code

public static void main(String[] args)

{

 int n = 4;

 printSeries(n);

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

# Python3 implementation of

# the above approach

limit = 1000000000

MAX_PRIME = 2000000

MAX = 1000000

I_MAX = 50000

mp = {}

b = [0] * MAX

p = [0] * MAX

j = 0

prime = [True] * (MAX_PRIME + 1)

# Function to generate Sieve of

# Eratosthenes

def SieveOfEratosthenes(n):

 global j

 p = 2

 while p * p <= n:

 # If prime[p] is not changed,

 # then it is a prime

 if (prime[p] == True):

 for i in range(p * p, n + 1, p):

 prime[i] = False

 p += 1

 # Add the prime numbers to the array b

 for p in range(2, n + 1):

 if (prime[p]):

 b[j] = p

 j += 1

# Function to return

# the gcd of a and b

def gcd(a, b):

 if (b == 0):

 return a

 return gcd(b, a % b)

# Function to print the required

# sequence of integers

def printSeries(n):

 SieveOfEratosthenes(MAX_PRIME)

 ar = [0] * (I_MAX + 2)

 for i in range(j):

 if ((b[i] * b[i + 1]) > limit):

 break

 # Including the primes in a series

 # of primes which will be later

 # multiplied

 p[i] = b[i]

 # This is done to mark a product

 # as existing

 mp[b[i] * b[i + 1]] = 1

 # Maximum number of

 # primes that we consider

 d = 550

 flag = False

 # For different interval

 k = 2

 while (k < d - 1) and not flag:

 # For different starting

 # index of jump

 m = 2

 while (m < d) and not flag:

 # For storing the numbers

 for l in range(m + k, d, k):

 # Checking for occurrence of a

 # product. Also checking for the

 # same prime occurring consecutively

 if (((b[l] * b[l + k]) < limit) and

 (l + k) < d and p[i - 1] != b[l + k] and

 p[i - 1] != b[l] and

 ((b[l] * b[l + k] in mp) and

 mp[b[l] * b[l + k]] != 1)):

 

 if (mp[p[i - 1] * b[l]] != 1):

 # Including the primes in a

 # series of primes which will

 # be later multiplied

 p[i] = b[l]

 mp[p[i - 1] * b[l]] = 1

 i += 1

 if (i >= I_MAX):

 flag = True

 break

 m += 1

 k += 1

 for i in range(n):

 ar[i] = p[i] * p[i + 1]

 for i in range(n - 1):

 print(ar[i], end = " ")

 g = gcd(ar[n - 1], ar[n - 2])

 print(g * 2)

# Driver Code

if __name__ == "__main__":

 n = 4

 printSeries(n)

# This code is contributed by Chitranayal  
  
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

using System.Collections.Generic; 

 

class GFG

{

static int limit = 1000000000;

static int MAX_PRIME = 2000000;

static int MAX = 1000000;

static int I_MAX = 50000;

static Dictionary<int,

 int> mp = new Dictionary<int,

 int>();

static int []b = new int[MAX];

static int []p = new int[MAX];

static int j = 0;

static bool []prime = new bool[MAX_PRIME + 1];

// Function to generate Sieve of

// Eratosthenes

static void SieveOfEratosthenes(int n)

{

 for(int i = 0; i < MAX_PRIME + 1; i++)

 prime[i] = true;

 for (int p = 2; p * p <= n; p++)

 {

 // If prime[p] is not changed,

 // then it is a prime

 if (prime[p] == true)

 {

 for (int i = p * p; i <= n; i += p)

 prime[i] = false;

 }

 }

 // Add the prime numbers to the array b

 for (int p = 2; p <= n; p++)

 {

 if (prime[p])

 {

 b[j++] = p;

 }

 }

}

// Function to return the gcd of a and b

static int gcd(int a, int b)

{

 if (b == 0)

 return a;

 return gcd(b, a % b);

}

// Function to print the required

// sequence of integers

static void printSeries(int n)

{

 SieveOfEratosthenes(MAX_PRIME);

 int i, g, k, l, m, d;

 int []ar = new int[I_MAX + 2];

 for (i = 0; i < j; i++)

 {

 if ((b[i] * b[i + 1]) > limit)

 break;

 // Including the primes in a series

 // of primes which will be later

 // multiplied

 p[i] = b[i];

 // This is done to mark a product

 // as existing

 mp.Add(b[i] * b[i + 1], 1);

 }

 // Maximum number of primes that we consider

 d = 550;

 bool flag = false;

 // For different interval

 for (k = 2; (k < d - 1) && !flag; k++)

 {

 // For different starting index of jump

 for (m = 2; (m < d) && !flag; m++)

 {

 // For storing the numbers

 for (l = m + k; l < d; l += k)

 {

 // Checking for occurrence of a

 // product. Also checking for the

 // same prime occurring consecutively

 if (((b[l] * b[l + k]) < limit) &&

 mp.ContainsKey(b[l] * b[l + k]) &&

 mp.ContainsKey(p[i - 1] * b[l]) &&

 (l + k) < d && p[i - 1] != b[l + k] &&

 p[i - 1] != b[l] &&

 mp[b[l] * b[l + k]] != 1)

 {

 if (mp[p[i - 1] * b[l]] != 1)

 {

 // Including the primes in a

 // series of primes which will

 // be later multiplied

 p[i] = b[l];

 mp.Add(p[i - 1] * b[l], 1);

 i++;

 }

 }

 if (i >= I_MAX)

 {

 flag = true;

 break;

 }

 }

 }

 }

 for (i = 0; i < n; i++)

 ar[i] = p[i] * p[i + 1];

 for (i = 0; i < n - 1; i++)

 Console.Write(ar[i] + " ");

 g = gcd(ar[n - 1], ar[n - 2]);

 Console.Write(g * 2);

}

// Driver Code

public static void Main(String[] args)

{

 int n = 4;

 printSeries(n);

}

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    6 15 35 14
    
    
    

**Another approach:** List all the prime numbers up to 6 million by using the
Sieve of Eratosthenes. We know the base condition i.e. N = 3 forms {6, 10,
15}.  
So, we use these three values to generate further terms of the sequence.  
As {2, 3, 5}, these primes can not be used to generate sequences because they
are already used in {6, 10, 15}. We also can’t use {7, 11} which we’ll see
later.  
Now we have a prime list {13, 17, 19, 23, 29, ……}. We take the first prime and
multiply it with  
6, second with 15, third with 10, again 4th with 6, and so on…

    
    
    13 * 6, 17 * 15, 19 * 10, 23 * 6, 29 * 15, ........upto N - 2 terms.
    (N - 1)th term = (N - 1)th prime * 7.
    Nth term = 7 * 11.
    again, first term = first term * 11 to make 1st and last noncoprime.
    For example, N = 5
    6 * 11 * 13, 15 * 17, 10 * 19, 11 * 19, 7 * 11
    
    
    

Now we see that we can not use 7 and 11 from the list as these are used to
generate last and second last term.  
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

using namespace std;

const int MAX = 620000;

int prime[MAX];

// Function for Sieve of Eratosthenes

void Sieve()

{

 for (int i = 2; i < MAX; i++) {

 if (prime[i] == 0) {

 for (int j = 2 * i; j < MAX; j += i) {

 prime[j] = 1;

 }

 }

 }

}

// Function to print the required sequence

void printSequence(int n)

{

 Sieve();

 vector<int> v, u;

 // Store only the required primes

 for (int i = 13; i < MAX; i++) {

 if (prime[i] == 0) {

 v.push_back(i);

 }

 }

 // Base condition

 if (n == 3) {

 cout << 6 << " " << 10 << " " << 15;

 return;

 }

 int k;

 for (k = 0; k < n - 2; k++) {

 // First integer in the list

 if (k % 3 == 0) {

 u.push_back(v[k] * 6);

 }

 // Second integer in the list

 else if (k % 3 == 1) {

 u.push_back(v[k] * 15);

 }

 // Third integer in the list

 else {

 u.push_back(v[k] * 10);

 }

 }

 k--;

 // Generate (N - 1)th term

 u.push_back(v[k] * 7);

 // Generate Nth term

 u.push_back(7 * 11);

 // Modify first term

 u[0] = u[0] * 11;

 // Print the sequence

 for (int i = 0; i < u.size(); i++) {

 cout << u[i] << " ";

 }

}

// Driver code

int main()

{

 int n = 4;

 printSequence(n);

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

 static int MAX = 620000;

 static int[] prime = new int[MAX];

 // Function for Sieve of Eratosthenes

 static void Sieve()

 {

 for (int i = 2; i < MAX; i++)

 {

 if (prime[i] == 0)

 {

 for (int j = 2 * i;

 j < MAX; j += i)

 {

 prime[j] = 1;

 }

 }

 }

 }

 // Function to print the required sequence

 static void printSequence(int n)

 {

 Sieve();

 Vector<Integer> v = new Vector<Integer>();

 Vector<Integer> u = new Vector<Integer>();

 // Store only the required primes

 for (int i = 13; i < MAX; i++)

 {

 if (prime[i] == 0)

 {

 v.add(i);

 }

 }

 

 // Base condition

 if (n == 3)

 {

 System.out.print(6 + " " + 10 + " " + 15);

 return;

 }

 int k;

 for (k = 0; k < n - 2; k++)

 {

 // First integer in the list

 if (k % 3 == 0)

 {

 u.add(v.get(k) * 6);

 }

 

 // Second integer in the list

 else if (k % 3 == 1)

 {

 u.add(v.get(k) * 15);

 }

 

 // Third integer in the list

 else

 {

 u.add(v.get(k) * 10);

 }

 }

 k--;

 // Generate (N - 1)th term

 u.add(v.get(k) * 7);

 // Generate Nth term

 u.add(7 * 11);

 // Modify first term

 u.set(0, u.get(0) * 11);

 // Print the sequence

 for (int i = 0; i < u.size(); i++)

 {

 System.out.print(u.get(i) + " ");

 }

 }

 // Driver code

 public static void main(String[] args)

 {

 int n = 4;

 printSequence(n);

 }

}

// This code is contributed by Rajput-Ji  
  
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

MAX = 620000

prime = [0] * MAX

# Function for Sieve of Eratosthenes

def Sieve():

 for i in range(2, MAX):

 if (prime[i] == 0):

 for j in range(2 * i, MAX, i):

 prime[j] = 1

# Function to print the required sequence

def printSequence (n):

 Sieve()

 v = []

 u = []

 # Store only the required primes

 for i in range(13, MAX):

 if (prime[i] == 0):

 v.append(i)

 # Base condition

 if (n == 3):

 print(6, 10, 15)

 return

 k = 0

 for k in range(n - 2):

 # First integer in the list

 if (k % 3 == 0):

 u.append(v[k] * 6)

 # Second integer in the list

 elif (k % 3 == 1):

 u.append(v[k] * 15)

 # Third integer in the list

 else:

 u.append(v[k] * 10)

 

 # Generate (N - 1)th term

 u.append(v[k] * 7)

 # Generate Nth term

 u.append(7 * 11)

 # Modify first term

 u[0] = u[0] * 11

 # Print the sequence

 print(*u)

# Driver code

if __name__ == '__main__':

 n = 4

 printSequence(n)

# This code is contributed by himanshu77  
  
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

using System.Collections.Generic;

class GFG

{

 static int MAX = 620000;

 static int[] prime = new int[MAX];

 // Function for Sieve of Eratosthenes

 static void Sieve()

 {

 for (int i = 2; i < MAX; i++)

 {

 if (prime[i] == 0)

 {

 for (int j = 2 * i;

 j < MAX; j += i)

 {

 prime[j] = 1;

 }

 }

 }

 }

 // Function to print the required sequence

 static void printSequence(int n)

 {

 Sieve();

 List<int> v = new List<int>();

 List<int> u = new List<int>();

 // Store only the required primes

 for (int i = 13; i < MAX; i++)

 {

 if (prime[i] == 0)

 {

 v.Add(i);

 }

 }

 

 // Base condition

 if (n == 3)

 {

 Console.Write(6 + " " + 10 + " " + 15);

 return;

 }

 int k;

 for (k = 0; k < n - 2; k++)

 {

 // First integer in the list

 if (k % 3 == 0)

 {

 u.Add(v[k] * 6);

 }

 

 // Second integer in the list

 else if (k % 3 == 1)

 {

 u.Add(v[k] * 15);

 }

 

 // Third integer in the list

 else

 {

 u.Add(v[k] * 10);

 }

 }

 k--;

 // Generate (N - 1)th term

 u.Add(v[k] * 7);

 // Generate Nth term

 u.Add(7 * 11);

 // Modify first term

 u[0] = u[0] * 11;

 // Print the sequence

 for (int i = 0; i < u.Count; i++)

 {

 Console.Write(u[i] + " ");

 }

 }

 // Driver code

 public static void Main(String[] args)

 {

 int n = 4;

 printSequence(n);

 }

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    858 255 119 77
    
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

