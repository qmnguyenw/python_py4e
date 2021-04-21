Number of ways to convert a character X to a string Y



Given a character **X** and a string **Y** of length **N** and the task is to
find the number of ways to convert **X** to **Y** by appending characters to
the left and the right ends of **X**. **Note** that any two ways are
considered different if either the sequence of left and right appends are
different or if the sequence is same, then characters appended are different
i.e. a left append followed by a right append is different from a right append
followed by a left append. Since the answer can be large print the final
answer MOD (109 \+ 7).

 **Examples:**

>  **Input:** X = ‘a’, Y = “xxay”  
>  **Output:** 3  
> All possible ways are:
>
>   1. Left append ‘x’ (“xa”), left append ‘x’ (“xxa”), right append
> y(“xxay”).
>   2. Left append ‘x’ (“xa”), right append y(“xay”), left append ‘x’
> (“xxay”).
>   3. Right append y(“ay”), left append ‘x’ (“xay”), left append ‘x’
> (“xxay”).
>

>
>  **Input:** X = ‘a’, Y = “cd”  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1:** One way for solving this problem will be using dynamic
programming.

  

  

  * Initialize a variable ans = 0, mod = 1000000007.
  * For all index ‘i’ such that Y[i] = X, update answer as ans = (ans + dp[i][i])%mod.

Here, **dp[l][r]** is the number of ways to make **Y** from the sub-string
**Y[l…r]**.  
The recurrence relation will be:

> dp[l][r] = (dp[l][r + 1] + dp[l – 1][r]) % mod

The time complexity for this approach will be O(N2).

 **Method 2:**

  * Initialize a variable ans = 0, mod = 1000000007.
  * For all index **i** such that **Y[i] = X** , update answer as **ans = (ans + F(i)) % mod** where **F(i) = (((N – 1)!) / (i! * (N – i – 1)!)) % mod**.

Reason the above formula works: Just try to find the answer of the question,
find the number of permutations of (p number of L) and (q number of R) where L
and R the left append and the right append operations respectively.  
The answer is **(p + q)! / (p! * q!)**. For each valid **i** , just find the
number of permutations of **i** Ls and **N – i – 1** Rs.  
The time complexity of this approach will be **O(N)**.

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

 

const int MOD = 1000000007;

 

// Function to find the modular-inverse

long long modInv(long long a, long long p = MOD - 2)

{

 long long s = 1;

 

 // While power > 1

 while (p != 1) {

 

 // Updating s and a

 if (p % 2)

 s = (s * a) % MOD;

 a = (a * a) % MOD;

 

 // Updating power

 p /= 2;

 }

 

 // Return the final answer

 return (a * s) % MOD;

}

 

// Function to return the count of ways

long long findCnt(char x, string y)

{

 // To store the final answer

 long long ans = 0;

 

 // To store pre-computed factorials

 long long fact[y.size() + 1] = { 1 };

 

 // Computing factorials

 for (long long i = 1; i <= y.size(); i++)

 fact[i] = (fact[i - 1] * i) % MOD;

 

 // Loop to find the occurrences of x

 // and update the ans

 for (long long i = 0; i < y.size(); i++) {

 if (y[i] == x) {

 ans += (modInv(fact[i])

 * modInv(fact[y.size() - i - 1]))

 % MOD;

 ans %= MOD;

 }

 }

 

 // Multiplying the answer by (n - 1)!

 ans *= fact[(y.size() - 1)];

 ans %= MOD;

 

 // Return the final answer

 return ans;

}

 

// Driver code

int main()

{

 char x = 'a';

 string y = "xxayy";

 

 cout << findCnt(x, y);

 

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

 

class GFG 

{

 

 final static int MOD = 1000000007; 

 

 // Function to find the modular-inverse 

 static long modInv(long a) 

 { 

 long p = MOD - 2;

 long s = 1; 

 

 // While power > 1 

 while (p != 1) 

 { 

 

 // Updating s and a 

 if (p % 2 == 1) 

 s = (s * a) % MOD; 

 

 a = (a * a) % MOD; 

 

 // Updating power 

 p /= 2; 

 } 

 

 // Return the final answer 

 return (a * s) % MOD; 

 } 

 

 // Function to return the count of ways 

 static long findCnt(char x, String y) 

 { 

 // To store the final answer 

 long ans = 0; 

 

 // To store pre-computed factorials 

 long fact[] = new long[y.length() + 1];

 

 for(int i = 0; i < y.length() + 1; i++)

 fact[i] = 1;

 

 // Computing factorials 

 for (int i = 1; i <= y.length(); i++) 

 fact[i] = (fact[i - 1] * i) % MOD; 

 

 // Loop to find the occurrences of x 

 // and update the ans 

 for (int i = 0; i < y.length(); i++) 

 { 

 if (y.charAt(i) == x)

 { 

 ans += (modInv(fact[i]) 

 * modInv(fact[y.length() - i - 1])) % MOD;

 

 ans %= MOD; 

 } 

 } 

 

 // Multiplying the answer by (n - 1)! 

 ans *= fact[(y.length() - 1)]; 

 ans %= MOD; 

 

 // Return the final answer 

 return ans; 

 } 

 

 // Driver code 

 public static void main (String[] args)

 { 

 char x = 'a'; 

 String y = "xxayy"; 

 

 System.out.println(findCnt(x, y)); 

 

 } 

}

 

// This code is contributed by AnkitRai01  
  
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

MOD = 1000000007; 

 

# Function to find the modular-inverse 

def modInv(a, p = MOD - 2) :

 

 s = 1; 

 

 # While power > 1 

 while (p != 1) :

 

 # Updating s and a 

 if (p % 2) :

 s = (s * a) % MOD; 

 a = (a * a) % MOD; 

 

 # Updating power 

 p //= 2; 

 

 # Return the final answer 

 return (a * s) % MOD; 

 

 

# Function to return the count of ways 

def findCnt(x, y) :

 

 # To store the final answer 

 ans = 0; 

 

 # To store pre-computed factorials 

 fact = [1]*(len(y) + 1) ; 

 

 # Computing factorials 

 for i in range(1,len(y)) :

 fact[i] = (fact[i - 1] * i) % MOD; 

 

 # Loop to find the occurrences of x 

 # and update the ans 

 for i in range(len(y)) :

 if (y[i] == x) :

 ans += (modInv(fact[i]) *

 modInv(fact[len(y)- i - 1])) % MOD; 

 ans %= MOD; 

 

 # Multiplying the answer by (n - 1)! 

 ans *= fact[(len(y) - 1)]; 

 ans %= MOD; 

 

 # Return the final answer 

 return ans; 

 

# Driver code 

if __name__ == "__main__" : 

 

 x = 'a'; 

 y = "xxayy"; 

 

 print(findCnt(x, y)); 

 

# This code is contributed by AnkitRai01  
  
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

 

class GFG 

{ 

 

 static int MOD = 1000000007; 

 

 // Function to find the modular-inverse 

 static long modInv(long a) 

 { 

 long p = MOD - 2; 

 long s = 1; 

 

 // While power > 1 

 while (p != 1) 

 { 

 

 // Updating s and a 

 if (p % 2 == 1) 

 s = (s * a) % MOD; 

 

 a = (a * a) % MOD; 

 

 // Updating power 

 p /= 2; 

 } 

 

 // Return the final answer 

 return (a * s) % MOD; 

 } 

 

 // Function to return the count of ways 

 static long findCnt(char x, String y) 

 { 

 // To store the final answer 

 long ans = 0; 

 

 // To store pre-computed factorials 

 long []fact = new long[y.Length + 1]; 

 

 for(int i = 0; i < y.Length + 1; i++) 

 fact[i] = 1; 

 

 // Computing factorials 

 for (int i = 1; i <= y.Length; i++) 

 fact[i] = (fact[i - 1] * i) % MOD; 

 

 // Loop to find the occurrences of x 

 // and update the ans 

 for (int i = 0; i < y.Length; i++) 

 { 

 if (y[i] == x) 

 { 

 ans += (modInv(fact[i]) 

 * modInv(fact[y.Length - i - 1])) % MOD; 

 

 ans %= MOD; 

 } 

 } 

 

 // Multiplying the answer by (n - 1)! 

 ans *= fact[(y.Length - 1)]; 

 ans %= MOD; 

 

 // Return the final answer 

 return ans; 

 } 

 

 // Driver code 

 public static void Main () 

 { 

 char x = 'a'; 

 string y = "xxayy"; 

 

 Console.WriteLine(findCnt(x, y)); 

 } 

} 

 

// This code is contributed by AnkitRai01   
  
---  
  
__

__

**Output:**

    
    
    6
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

