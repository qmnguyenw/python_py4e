Sum of GCD of all possible sequences



Given two numbers **N** and **K**. A sequence **A 1, A2, ….AN** of length
**N** can be created by placing numbers from **1 to K** at each position
making a total of KN sequences. The task is to find the sum of GCD of all the
sequences formed.  
 **Note:** The answer can be very large, so take modulo with **10 9 \+ 7**.

**Examples:**

> **Input:** N = 3, K = 2  
> **Output:** 9  
> **Explanation:**  
> The gcd of all the subsequences are:  
> gcd(1, 1, 1) = 1  
> gcd(1, 1, 2) = 1  
> gcd(1, 2, 1) = 1  
> gcd(1, 2, 2) = 1  
> gcd(2, 1, 1) = 1  
> gcd(2, 1, 2) = 1  
> gcd(2, 2, 1) = 1  
> gcd(2, 2, 2) = 2  
> Sum of GCD is 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 = 9.
>
>  **Input:** N = 3, K = 200  
> **Output:** 10813692

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The idea is to generate all the possible subsequence of
length **N** recursively. The summation of GCD of all the sequences formed is
the required result.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

using namespace std;

const int MOD = (int)1e9 + 7;

// A recursive function that generates all

// the sequence and find GCD

int calculate(int pos, int g, int n, int k)

{

 // If we reach the sequence of length N

 // g is the GCD of the sequence

 if (pos == n) {

 return g;

 }

 // Intialise answer to 0

 int answer = 0;

 // Placing all possible values at this

 // position and recursively find the

 // GCD of the sequence

 for (int i = 1; i <= k; i++) {

 // Take GCD of GCD calculated uptill

 // now i.e. g with current element

 answer = (answer % MOD

 + calculate(pos + 1, __gcd(g, i), n, k) % MOD);

 // Take modulo to avoid overflow

 answer %= MOD;

 }

 // Return the final answer

 return answer;

}

// Function that finds the sum of GCD

// of all the subsequence of N length

int sumofGCD(int n, int k)

{

 // Recursive function that generates

 // the sequence and return the GCD

 return calculate(0, 0, n, k);

}

// Driver Code

int main()

{

 int N = 3, K = 2;

 // Function Call

 cout << sumofGCD(N, K);

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

// Java implementation of the above approach

class GFG{

 

static int MOD = (int)1e9 + 7;

 

// A recursive function that generates all

// the sequence and find GCD

static int calculate(int pos, int g, int n, int k)

{

 

 // If we reach the sequence of length N

 // g is the GCD of the sequence

 if (pos == n) {

 return g;

 }

 

 // Intialise answer to 0

 int answer = 0;

 

 // Placing all possible values at this

 // position and recursively find the

 // GCD of the sequence

 for (int i = 1; i <= k; i++) {

 

 // Take GCD of GCD calculated uptill

 // now i.e. g with current element

 answer = (answer % MOD

 + calculate(pos + 1, __gcd(g, i), n, k) % MOD);

 

 // Take modulo to astatic void overflow

 answer %= MOD;

 }

 

 // Return the final answer

 return answer;

}

 

// Function that finds the sum of GCD

// of all the subsequence of N length

static int sumofGCD(int n, int k)

{

 

 // Recursive function that generates

 // the sequence and return the GCD

 return calculate(0, 0, n, k);

}

static int __gcd(int a, int b) 

{ 

 return b == 0? a:__gcd(b, a % b); 

}

// Driver Code

public static void main(String[] args)

{

 int N = 3, K = 2;

 

 // Function Call

 System.out.print(sumofGCD(N, K));

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

# Pyhton3 implementation of the

# above approach

MOD = 1e9 + 7

def gcd(a, b):

 

 if (b == 0):

 return a

 else:

 return gcd(b, a % b)

# A recursive function that generates all

# the sequence and find GCD

def calculate(pos, g, n, k):

 

 # If we reach the sequence of length N

 # g is the GCD of the sequence

 if (pos == n):

 return g

 

 # Intialise answer to 0

 answer = 0

 

 # Placing all possible values at this

 # position and recursively find the

 # GCD of the sequence

 for i in range(1, k + 1):

 

 # Take GCD of GCD calculated uptill

 # now i.e. g with current element

 answer = (answer % MOD +

 calculate(pos + 1,

 gcd(g, i), n, k) % MOD)

 

 # Take modulo to avoid overflow

 answer %= MOD

 

 # Return the final answer

 return answer

 

# Function that finds the sum of GCD

# of all the subsequence of N length

def sumofGCD(n, k):

 

 # Recursive function that generates

 # the sequence and return the GCD

 return calculate(0, 0, n, k)

# Driver code 

if __name__=="__main__":

 

 N = 3

 K = 2

 

 # Function Call

 print(sumofGCD(N, K))

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

// C# implementation of the above approach

using System;

public class GFG{

static int MOD = (int)1e9 + 7;

// A recursive function that generates all

// the sequence and find GCD

static int calculate(int pos, int g, int n, int k)

{

 

 // If we reach the sequence of length N

 // g is the GCD of the sequence

 if (pos == n) {

 return g;

 }

 // Intialise answer to 0

 int answer = 0;

 // Placing all possible values at this

 // position and recursively find the

 // GCD of the sequence

 for (int i = 1; i <= k; i++) {

 // Take GCD of GCD calculated uptill

 // now i.e. g with current element

 answer = (answer % MOD

 + calculate(pos + 1, __gcd(g, i), n, k) % MOD);

 // Take modulo to astatic void overflow

 answer %= MOD;

 }

 // Return the readonly answer

 return answer;

}

// Function that finds the sum of GCD

// of all the subsequence of N length

static int sumofGCD(int n, int k)

{

 // Recursive function that generates

 // the sequence and return the GCD

 return calculate(0, 0, n, k);

}

static int __gcd(int a, int b)

{

 return b == 0 ? a : __gcd(b, a % b); 

}

// Driver code

public static void Main(String[] args)

{

 int N = 3, K = 2;

 // Function call

 Console.Write(sumofGCD(N, K));

}

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    9

**Time Complexity:** O(NK)

 **Efficient Approach:**

  * Since the numbers of the sequence can be from **1 to K** , the gcd value of the sequence will be in the range 1 to K.
  * Let **count[i]** represent the number of sequences with gcd = i. For i = 1, we have no constraints on which elements can belong to the sequence, so at each of the **N** places we have **K** possibilities to place elements making the total sequences to be **K N**. But the resulting sequences may have higher GCD, So subtract the over counted values:

    
    
    count[1] = KN - count[2] - count[3] - count[4] - .... count[K]

  * Similarly for i = 2, since every number must be a multiple of 2, we have **K/2** possibilities at each place making the total to be **(K/2) N**. And Subtract all the over counted values by subtracting sequence count with GCD of all multiples of 2.

    
    
    count[2] = (K/2)N - count[4] - count[6] - count[8] - ... all multiples of 2

  * Similarly, follow the above steps for each gcd value till K.
  * The summation of each GCD value(say **g** ) with **count[g]** is the sum of GCD of all the sequence formed.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

using namespace std;

const int MOD = (int)1e9 + 7;

// Function to find a^b in log(b)

int fastexpo(int a, int b)

{

 int res = 1;

 a %= MOD;

 while (b) {

 if (b & 1)

 res = (res * a) % MOD;

 a *= a;

 a %= MOD;

 b >>= 1;

 }

 return res;

}

// Function that finds the sum of GCD

// of all the subsequence of N length

int sumofGCD(int n, int k)

{

 // To stores the number of sequences

 // with gcd i

 int count[k + 1] = { 0 };

 // Find contribution of each gcd

 // to happen

 for (int g = k; g >= 1; g--) {

 // To count multiples

 int count_multiples = k / g;

 // possible sequences with

 // overcounting

 int temp;

 temp = fastexpo(count_multiples, n);

 // to avoid overflow

 temp %= MOD;

 // Find extra element which will

 // not form gcd = i

 int extra = 0;

 // Find overcounting

 for (int j = g * 2; j <= k; j += g) {

 extra = (extra + count[j]);

 extra %= MOD;

 }

 // Remove the overcounting

 count[g] = (temp - extra + MOD);

 count[g] %= MOD;

 }

 // To store the final answer

 int sum = 0;

 int add;

 for (int i = 1; i <= k; ++i) {

 add = (count[i] % MOD * i % MOD);

 add %= MOD;

 sum += add;

 sum %= MOD;

 }

 // Return Final answer

 return sum;

}

// Driver Code

int main()

{

 int N = 3, K = 2;

 // Function call

 cout << sumofGCD(N, K);

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

// Java implementation of the above approach

class GFG{

static int MOD = (int)1e9 + 7;

 

// Function to find a^b in log(b)

static int fastexpo(int a, int b)

{

 

 int res = 1;

 a %= MOD;

 

 while (b > 0) {

 if (b % 2 == 1)

 res = (res * a) % MOD;

 a *= a;

 a %= MOD;

 b >>= 1;

 }

 return res;

}

 

// Function that finds the sum of GCD

// of all the subsequence of N length

static int sumofGCD(int n, int k)

{

 

 // To stores the number of sequences

 // with gcd i

 int []count = new int[k + 1];

 

 // Find contribution of each gcd

 // to happen

 for (int g = k; g >= 1; g--) {

 

 // To count multiples

 int count_multiples = k / g;

 

 // possible sequences with

 // overcounting

 int temp;

 

 temp = fastexpo(count_multiples, n);

 

 // to astatic void overflow

 temp %= MOD;

 

 // Find extra element which will

 // not form gcd = i

 int extra = 0;

 

 // Find overcounting

 for (int j = g * 2; j <= k; j += g) {

 

 extra = (extra + count[j]);

 extra %= MOD;

 }

 

 // Remove the overcounting

 count[g] = (temp - extra + MOD);

 count[g] %= MOD;

 }

 

 // To store the final answer

 int sum = 0;

 int add;

 

 for (int i = 1; i <= k; ++i) {

 

 add = (count[i] % MOD * i % MOD);

 add %= MOD;

 sum += add;

 sum %= MOD;

 }

 

 // Return Final answer

 return sum;

}

 

// Driver Code

public static void main(String[] args)

{

 int N = 3, K = 2;

 

 // Function call

 System.out.print(sumofGCD(N, K));

}

}

// This code is contributed by PrinciRaj1992  
  
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

# Python3 implementation of the above approach

MOD = (int)(1e9 + 7)

# Function to find a^b in log(b)

def fastexpo(a, b) :

 res = 1

 a = a % MOD

 while (b > 0) :

 if ((b & 1) != 0) :

 res = (res * a) % MOD

 a = a * a

 a = a % MOD

 b = b >> 1

 return res

# Function that finds the sum of GCD

# of all the subsequence of N length

def sumofGCD(n, k) :

 

 # To stores the number of sequences

 # with gcd i

 count = [0] * (k + 1)

 # Find contribution of each gcd

 # to happen

 for g in range(k, 0, -1) :

 # To count multiples

 count_multiples = k // g

 # possible sequences with

 # overcounting

 temp = fastexpo(count_multiples, n)

 # to avoid overflow

 temp = temp % MOD

 # Find extra element which will

 # not form gcd = i

 extra = 0

 # Find overcounting

 for j in range(g * 2, k + 1, g) :

 extra = extra + count[j]

 extra = extra % MOD

 # Remove the overcounting

 count[g] = temp - extra + MOD

 count[g] = count[g] % MOD

 # To store the final answer

 Sum = 0

 for i in range(1, k + 1) :

 add = count[i] % MOD * i % MOD

 add = add % MOD

 Sum = Sum + add

 Sum = Sum % MOD

 # Return Final answer

 return Sum

 # Driver code

N, K = 3, 2

# Function call

print(sumofGCD(N, K))

# This code is contributed by divyeshrabadiya07.  
  
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

// C# implementation of the above approach

using System;

class GFG{

static int MOD = (int)1e9 + 7;

 

// Function to find a^b in log(b)

static int fastexpo(int a, int b)

{

 

 int res = 1;

 a %= MOD;

 

 while (b > 0) {

 if (b % 2 == 1)

 res = (res * a) % MOD;

 a *= a;

 a %= MOD;

 b >>= 1;

 }

 return res;

}

 

// Function that finds the sum of GCD

// of all the subsequence of N length

static int sumofGCD(int n, int k)

{

 

 // To stores the number of sequences

 // with gcd i

 int []count = new int[k + 1];

 

 // Find contribution of each gcd

 // to happen

 for (int g = k; g >= 1; g--) {

 

 // To count multiples

 int count_multiples = k / g;

 

 // possible sequences with

 // overcounting

 int temp;

 

 temp = fastexpo(count_multiples, n);

 

 // to astatic void overflow

 temp %= MOD;

 

 // Find extra element which will

 // not form gcd = i

 int extra = 0;

 

 // Find overcounting

 for (int j = g * 2; j <= k; j += g) {

 

 extra = (extra + count[j]);

 extra %= MOD;

 }

 

 // Remove the overcounting

 count[g] = (temp - extra + MOD);

 count[g] %= MOD;

 }

 

 // To store the readonly answer

 int sum = 0;

 int add;

 

 for (int i = 1; i <= k; ++i) {

 

 add = (count[i] % MOD * i % MOD);

 add %= MOD;

 sum += add;

 sum %= MOD;

 }

 

 // Return Final answer

 return sum;

}

 

// Driver Code

public static void Main(String[] args)

{

 int N = 3, K = 2;

 

 // Function call

 Console.Write(sumofGCD(N, K));

}

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    9

**Time Complexity:** O( K*log(N) + K*log(log(K)) )  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

