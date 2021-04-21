Count number of ways to convert string S to T by performing K cyclic shifts



Given two strings **S and T** and a number **K** , the task is to count the
number of ways to convert string **S** to string **T** by performing **K
cyclic shifts**.

> The cyclic shift is defined as the string **S** can be split into two non-
> empty parts **X + Y** and in one operation we can transform **S** to **Y +
> X** from **X + Y**.

 **Note:** Since count can be very large print the answer to modulo **10 9 \+
7**.

 **Examples:**

>  **Input:** S = “ab”, T = “ab”, K = 2  
>  **Output:** 1  
>  **Explanation:**  
>  The only way to do this is to convert **[ab to ba]** in the first move and
> then [ba to ab] in the second move.
>
>  
>
>
>  
>
>
>  **Input:** S = “ababab”, T = “ababab”, K = 1  
>  **Output:** 2  
>  **Explanation:**  
>  One possible way to convert S to T in one move is **[ab | abab]** ->
> **[ababab]** , the second way is **[abab | ab]** -> **[ababab]**. So there
> are total two ways.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can be solved using Dynamic Programming. Let us
call a cyclic shift **‘good’** if at the end we are at string **T** and the
vice versa for **‘bad’**. Below are the steps:

  1. Precompute the number of good(denoted by a) and bad(denoted by b) cyclic shifts.
  2. Initialize two dp arrays such that **dp1[i]** denote the number of ways to get to a good shift in **i moves** and **dp2[i]** denotes the number of ways to get to a bad shift in **i moves**.
  3. For transition, we are only concerned about previous state i.e., **(i – 1)th state** and the answer to this question is **dp1[K]**.
  4. So the number of ways to reach a good state in **i moves** is equal to the number of ways of reaching a good shift in **i-1** moves multiplied by **(a-1)** (as last shift is also good)
  5. So the number of ways of reaching a bad shift in **i-1 moves** multiplied by **(a)** (as next move can be any of the good shifts).

Below is the recurrence relation for the good and bad shifts:

> So for good shifts we have:  
> ![dp1\[i\]= dp1\[i-1\]*\(a-1\) +
> dp2\[i-1\]*a](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-339bfb2e91046a3ae594cded4b3a739d_l3.png)
>
> Similarly, for bad shifts we have:  
> ![dp2\[i\]=dp1\[i-1\]*b +
> dp2\[i-1\]*\(b-1\)](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-97bb7cfe0c50fff4993d2918b026b615_l3.png)

Below is the implementation of above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h> 

using namespace std; 

#define mod 10000000007 

 

// Function to count number of ways to 

// convert string S to string T by 

// performing K cyclic shifts 

long long countWays(string s, string t, 

 int k) 

{ 

 // Calculate length of string 

 int n = s.size(); 

 

 // 'a' is no of good cyclic shifts 

 // 'b' is no of bad cyclic shifts 

 int a = 0, b = 0; 

 

 // Iterate in the string 

 for (int i = 0; i < n; i++) { 

 

 string p = s.substr(i, n - i) 

 + s.substr(0, i); 

 

 // Precompute the number of good 

 // and bad cyclic shifts 

 if (p == t) 

 a++; 

 else

 b++; 

 } 

 

 // Initialize two dp arrays 

 // dp1[i] to store the no of ways to 

 // get to a good shift in i moves 

 

 // dp2[i] to store the no of ways to 

 // get to a bad shift in i moves 

 vector<long long> dp1(k + 1), dp2(k + 1); 

 

 if (s == t) { 

 dp1[0] = 1; 

 dp2[0] = 0; 

 } 

 else { 

 dp1[0] = 0; 

 dp2[0] = 1; 

 } 

 

 // Calculate good and bad shifts 

 for (int i = 1; i <= k; i++) { 

 

 dp1[i] 

 = ((dp1[i - 1] * (a - 1)) % mod 

 + (dp2[i - 1] * a) % mod) 

 % mod; 

 

 dp2[i] 

 = ((dp1[i - 1] * (b)) % mod 

 + (dp2[i - 1] * (b - 1)) % mod) 

 % mod; 

 } 

 

 // Return the required number of ways 

 return dp1[k]; 

} 

 

// Driver Code 

int main() 

{ 

 // Given Strings 

 string S = "ab", T = "ab"; 

 

 // Given K shifts required 

 int K = 2; 

 

 // Function Call 

 cout << countWays(S, T, K); 

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

// Java program for above approach

class GFG{ 

 

static long mod = 10000000007L; 

 

// Function to count number of ways to 

// convert string S to string T by 

// performing K cyclic shifts 

static long countWays(String s, String t, 

 int k) 

{ 

 

 // Calculate length of string 

 int n = s.length(); 

 

 // 'a' is no of good cyclic shifts 

 // 'b' is no of bad cyclic shifts 

 int a = 0, b = 0; 

 

 // Iterate in the string 

 for(int i = 0; i < n; i++) 

 { 

 String p = s.substring(i, n - i) + 

 s.substring(0, i); 

 

 // Precompute the number of good 

 // and bad cyclic shifts 

 if (p == t) 

 a++; 

 else

 b++; 

 } 

 

 // Initialize two dp arrays 

 // dp1[i] to store the no of ways to 

 // get to a good shift in i moves 

 

 // dp2[i] to store the no of ways to 

 // get to a bad shift in i moves 

 long dp1[] = new long[k + 1]; 

 long dp2[] = new long[k + 1]; 

 

 if (s == t) 

 { 

 dp1[0] = 1; 

 dp2[0] = 0; 

 } 

 else

 { 

 dp1[0] = 0; 

 dp2[0] = 1; 

 } 

 

 // Calculate good and bad shifts 

 for(int i = 1; i <= k; i++) 

 { 

 dp1[i] = ((dp1[i - 1] * (a - 1)) % mod + 

 (dp2[i - 1] * a) % mod) % mod; 

 dp2[i] = ((dp1[i - 1] * (b)) % mod + 

 (dp2[i - 1] * (b - 1)) % mod) % mod; 

 } 

 

 // Return the required number of ways 

 return dp1[k]; 

} 

 

// Driver code 

public static void main(String[] args) 

{ 

 

 // Given Strings 

 String S = "ab", T = "ab"; 

 

 // Given K shifts required 

 int K = 2; 

 

 // Function Call 

 System.out.print(countWays(S, T, K)); 

} 

} 

 

// This code is contributed by Pratima Pandey   
  
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

mod = 1000000007

 

# Function to count number of ways 

# to convert string S to string T by 

# performing K cyclic shifts 

def countWays(s, t, k): 

 

 # Calculate length of string 

 n = len(s) 

 

 # a is no. of good cyclic shifts 

 # b is no. of bad cyclic shifts 

 a = 0

 b = 0

 

 # Iterate in string 

 for i in range(n): 

 p = s[i : n - i + 1] + s[: i + 1] 

 

 # Precompute the number of good 

 # and bad cyclic shifts 

 if(p == t): 

 a += 1

 else: 

 b += 1

 

 # Initialize two dp arrays 

 # dp1[i] to store the no of ways to 

 # get to a goof shift in i moves 

 

 # dp2[i] to store the no of ways to 

 # get to a bad shift in i moves 

 dp1 = [0] * (k + 1) 

 dp2 = [0] * (k + 1) 

 

 if(s == t): 

 dp1[0] = 1

 dp2[0] = 0

 else: 

 dp1[0] = 0

 dp2[0] = 1

 

 # Calculate good and bad shifts 

 for i in range(1, k + 1): 

 dp1[i] = ((dp1[i - 1] * (a - 1)) % mod +

 (dp2[i - 1] * a) % mod) % mod 

 

 dp2[i] = ((dp1[i - 1] * (b)) % mod +

 (dp2[i - 1] * (b - 1)) % mod) % mod 

 

 # Return the required number of ways 

 return(dp1[k]) 

 

# Driver Code 

 

# Given Strings 

S = 'ab'

T = 'ab'

 

# Given K shifts required 

K = 2

 

# Function call 

print(countWays(S, T, K)) 

 

# This code is contributed by Arjun Saini   
  
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

// C# program for the above approach

using System;

 

class GFG{ 

 

static long mod = 10000000007L;

 

// Function to count number of ways to

// convert string S to string T by

// performing K cyclic shifts

static long countWays(string s, string t,

 int k)

{

 

 // Calculate length of string

 int n = s.Length;

 

 // 'a' is no of good cyclic shifts

 // 'b' is no of bad cyclic shifts

 int a = 0, b = 0;

 

 // Iterate in the string

 for(int i = 0; i < n; i++)

 {

 string p = s.Substring(i, n - i) + 

 s.Substring(0, i);

 

 // Precompute the number of good

 // and bad cyclic shifts

 if (p == t)

 a++;

 else

 b++;

 }

 

 // Initialize two dp arrays

 // dp1[i] to store the no of ways to

 // get to a good shift in i moves

 

 // dp2[i] to store the no of ways to

 // get to a bad shift in i moves

 long []dp1 = new long[k + 1];

 long []dp2 = new long[k + 1];

 

 if (s == t)

 {

 dp1[0] = 1;

 dp2[0] = 0;

 }

 else

 {

 dp1[0] = 0;

 dp2[0] = 1;

 }

 

 // Calculate good and bad shifts

 for(int i = 1; i <= k; i++)

 {

 dp1[i] = ((dp1[i - 1] * (a - 1)) % mod +

 (dp2[i - 1] * a) % mod) % mod;

 dp2[i] = ((dp1[i - 1] * (b)) % mod +

 (dp2[i - 1] * (b - 1)) % mod) % mod;

 }

 

 // Return the required number of ways

 return dp1[k];

}

 

// Driver code 

public static void Main(string[] args) 

{ 

 

 // Given Strings

 string S = "ab", T = "ab";

 

 // Given K shifts required

 int K = 2;

 

 // Function call

 Console.Write(countWays(S, T, K)); 

} 

} 

 

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

**Time Complexity:** _O(N)_  
 **Auxiliary Space:** _O(K)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

