Find sum of xor of all unordered triplets of the array



Given an array A, consisting of N non-negative integers, find the sum of xor
of all unordered triplets of the array. For unordered triplets, the triplet
(A[i], A[j], A[k]) is considered same as triplet (A[j], A[i], A[k]) and all
the other permutations.  
Since the answer can be large calculate its mod with 10037.  
 **Examples:**  

    
    
    **Input :** A = [3, 5, 2, 18, 7]
    **Output :** 132
    
    **Input :** A = [140, 1, 66]
    **Output :** 207
    
    
    
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach**  
Iterate over all the unordered triplets and add xor of each to the sum.  
 **Efficient Approach**

  * An important point to observe is that xor is independent over all the bits. So we can do the required computation over each bit individually.
  * Let’s consider the k’th bit of all the array elements. If the number of unoredered triplets whose k’th bit xor to 1 be C, we can simply add C * 2k to the answer. Let the number of elements whose k’th bit is 1 be X and whose k’th bit is 0 be Y. Then to find the unordered triplets whose k’th bits xor to 1 can be formed using two cases: 
    1. Only one of the three elements have k’th bit 1.
    2. All three of them have k’th bit 1.
  * Number of ways to select 3 element having k’th bit 1 =

![ {X \\choose 3}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-53394d639802976ad5cf5a42d3e77374_l3.png)

  * Number of ways to select 1 element with k’th bit 1 and rest with 0 =

![ X * {Y \\choose 3}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-daa36ac8859036457ef747625fc0e056_l3.png)

  

  

  * We will use nCr mod p to compute the combinotorial function values.

Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find sum of xor of

// all unordered triplets of the array

#include <bits/stdc++.h>

using namespace std;

// Iterative Function to calculate

// (x^y)%p in O(log y)

int power(int x, int y, int p)

{

 // Initialize result

 int res = 1;

 // Update x if it is more than or

 // equal to p

 x = x % p;

 

 while (y > 0)

 {

 // If y is odd, multiply x

 // with result

 if (y & 1)

 res = (res * x) % p;

 // y must be even now

 y = y >> 1; // y = y/2

 x = (x * x) % p;

 }

 return res;

}

// Returns n^(-1) mod p

int modInverse(int n, int p)

{

 return power(n, p - 2, p);

}

// Returns nCr % p using Fermat's little

// theorem.

int nCrModPFermat(int n, int r, int p)

{

 // Base case

 if (r == 0)

 return 1;

 if (n < r)

 return 0;

 

 // Fill factorial array so that we

 // can find all factorial of r, n

 // and n-r

 int fac[n + 1];

 fac[0] = 1;

 for (int i = 1; i <= n; i++)

 fac[i] = fac[i - 1] * i % p;

 return (fac[n] * modInverse(fac[r], p) % p

 * modInverse(fac[n - r], p) % p) % p;

}

// Function returns sum of xor of all

// unordered triplets of the array

int SumOfXor(int a[], int n)

{

 int mod = 10037;

 int answer = 0;

 // Iterating over the bits

 for (int k = 0; k < 32; k++)

 {

 // Number of elements whith k'th bit

 // 1 and 0 respectively

 int x = 0, y = 0;

 for (int i = 0; i < n; i++)

 {

 // Checking if k'th bit is 1

 if (a[i] & (1 << k))

 x++;

 else

 y++;

 }

 // Adding this bit's part to the answer

 answer += ((1 << k) % mod *

 (nCrModPFermat(x, 3, mod)

 + x * nCrModPFermat(y, 2, mod))

 % mod) % mod;

 }

 return answer;

}

// Drivers code

int main()

{

 int n = 5;

 int A[n] = { 3, 5, 2, 18, 7 };

 cout << SumOfXor(A, n);

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

// Java program to find sum of xor of

// all unordered triplets of the array

class GFG{

// Iterative Function to calculate

// (x^y)%p in O(log y)

static int power(int x, int y, int p)

{

 

 // Initialize result

 int res = 1;

 // Update x if it is more than or

 // equal to p

 x = x % p;

 while (y > 0)

 {

 

 // If y is odd, multiply x

 // with result

 if ((y & 1) == 1)

 res = (res * x) % p;

 // y must be even now

 y = y >> 1; // y = y/2

 x = (x * x) % p;

 }

 return res;

}

// Returns n^(-1) mod p

static int modInverse(int n, int p)

{

 return power(n, p - 2, p);

}

// Returns nCr % p using Fermat's little

// theorem.

static int nCrModPFermat(int n, int r, int p)

{

 

 // Base case

 if (r == 0)

 return 1;

 if (n < r)

 return 0;

 // Fill factorial array so that we

 // can find all factorial of r, n

 // and n-r

 int fac[] = new int[n + 1];

 fac[0] = 1;

 for(int i = 1; i <= n; i++)

 fac[i] = fac[i - 1] * i % p;

 return (fac[n] * modInverse(fac[r], p) % p *

 modInverse(fac[n - r], p) %

 p) % p;

}

// Function returns sum of xor of all

// unordered triplets of the array

static int SumOfXor(int a[], int n)

{

 int mod = 10037;

 int answer = 0;

 // Iterating over the bits

 for(int k = 0; k < 32; k++)

 {

 

 // Number of elements whith k'th bit

 // 1 and 0 respectively

 int x = 0, y = 0;

 for(int i = 0; i < n; i++)

 {

 

 // Checking if k'th bit is 1

 if ((a[i] & (1 << k)) != 0)

 x++;

 else

 y++;

 }

 // Adding this bit's part to the answer

 answer += ((1 << k) % mod *

 (nCrModPFermat(x, 3, mod) + x *

 nCrModPFermat(y, 2, mod)) %

 mod) % mod;

 }

 return answer;

}

// Driver code

public static void main(String[] args)

{

 int n = 5;

 int A[] = { 3, 5, 2, 18, 7 };

 System.out.println(SumOfXor(A, n));

}

}

// This code is contributed by jrishabh99  
  
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

# Python3 program to find sum of xor of

# all unordered triplets of the array

# Iterative Function to calculate

# (x^y)%p in O(log y)

def power(x, y, p):

 

 # Initialize result

 res = 1

 # Update x if it is more than or

 # equal to p

 x = x % p

 while (y > 0):

 # If y is odd, multiply x

 # with result

 if (y & 1):

 res = (res * x) % p

 # y must be even now

 y = y >> 1#y = y/2

 x = (x * x) % p

 return res

# Returns n^(-1) mod p

def modInverse(n, p):

 return power(n, p - 2, p)

# Returns nCr % p using Fermat's little

# theorem.

def nCrModPFermat(n, r, p):

 

 # Base case

 if (r == 0):

 return 1

 if (n < r):

 return 0

 # Fill factorial array so that we

 # can find all factorial of r, n

 # and n-r

 fac = [0]*(n + 1)

 fac[0] = 1

 for i in range(1, n + 1):

 fac[i] = fac[i - 1] * i % p

 return (fac[n] * modInverse(fac[r], p) % p *

 modInverse(fac[n - r], p) % p) % p

# Function returns sum of xor of all

# unordered triplets of the array

def SumOfXor(a, n):

 mod = 10037

 answer = 0

 # Iterating over the bits

 for k in range(32):

 

 # Number of elements whith k'th bit

 # 1 and 0 respectively

 x = 0

 y = 0

 for i in range(n):

 

 # Checking if k'th bit is 1

 if (a[i] & (1 << k)):

 x += 1

 else:

 y += 1

 # Adding this bit's part to the answer

 answer += ((1 << k) % mod * (nCrModPFermat(x, 3,
mod)

 + x * nCrModPFermat(y, 2, mod))

 % mod) % mod

 return answer

# Drivers code

if __name__ == '__main__':

 n = 5

 A=[3, 5, 2, 18, 7]

 print(SumOfXor(A, n))

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

// C# program to find sum of xor of

// all unordered triplets of the array

using System;

class GFG{

// Iterative Function to calculate

// (x^y)%p in O(log y)

static int power(int x, int y, int p)

{

 

 // Initialize result

 int res = 1;

 // Update x if it is more than or

 // equal to p

 x = x % p;

 while (y > 0)

 {

 

 // If y is odd, multiply x

 // with result

 if ((y & 1) == 1)

 res = (res * x) % p;

 // y must be even now

 y = y >> 1; // y = y/2

 x = (x * x) % p;

 }

 return res;

}

// Returns n^(-1) mod p

static int modInverse(int n, int p)

{

 return power(n, p - 2, p);

}

// Returns nCr % p using Fermat's little

// theorem.

static int nCrModPFermat(int n, int r, int p)

{

 

 // Base case

 if (r == 0)

 return 1;

 if (n < r)

 return 0;

 // Fill factorial array so that we

 // can find all factorial of r, n

 // and n-r

 int []fac = new int[n + 1];

 fac[0] = 1;

 for(int i = 1; i <= n; i++)

 fac[i] = fac[i - 1] * i % p;

 return (fac[n] * modInverse(fac[r], p) % p *

 modInverse(fac[n - r], p) %

 p) % p;

}

// Function returns sum of xor of all

// unordered triplets of the array

static int SumOfXor(int []a, int n)

{

 int mod = 10037;

 int answer = 0;

 // Iterating over the bits

 for(int k = 0; k < 32; k++)

 {

 

 // Number of elements whith k'th bit

 // 1 and 0 respectively

 int x = 0, y = 0;

 for(int i = 0; i < n; i++)

 {

 

 // Checking if k'th bit is 1

 if ((a[i] & (1 << k)) != 0)

 x++;

 else

 y++;

 }

 // Adding this bit's part to the answer

 answer += ((1 << k) % mod *

 (nCrModPFermat(x, 3, mod) + x *

 nCrModPFermat(y, 2, mod)) %

 mod) % mod;

 }

 return answer;

}

// Driver code

public static void Main(String[] args)

{

 int n = 5;

 int []A = { 3, 5, 2, 18, 7 };

 Console.WriteLine(SumOfXor(A, n));

}

}

// This code is contributed by gauravrajput1  
  
---  
  
 __

 __

 **Output:**

    
    
    132
    
    
    
    

**Time Complexity :** O(32 * N)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

