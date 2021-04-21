Count the numbers with N digits and whose suffix is divisible by K



Given two positive integers **N** and **K** , the task is to count the number
of positive integers **D** such that D has N digits and any of the suffix of
its decimal representation is divisible by K.  
 **Examples:**

>  **Input:** N = 1, K = 2  
>  **Output:** 4  
>  **Explanation:**  
>  There are 4 such integers in which any of the suffix is divisible by K:  
> {2, 4, 6, 8}
>
>  **Input:** N = 2, K = 2  
>  **Output:** 45  
>  **Explanation:**  
>  There are 45, Two digit integers in which any of the suffix is divisible by
> 2:  
> Some of such integers is given below –  
> {10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23…}  
> Notice that, 21 and 23 numbers are not divisible by 2. But their suffix 2 is
> divisible by 2.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** Iterate over all the integers of the N digit and for each
integer check that any suffix of the number is divisible by K, If yes then
increment the count of such numbers by 1.

 **Approach:** The idea is to use the concept of Dynamic Programming by
increasing the suffix length and placing the digits from 0 to 9 recusively.
Below is the illustration of steps:

  

  

  *  **Function Definition:** This problem can be solved recursively in which at each step we can choose the digits for the suffix for N digit number. So, the Function Definition of the recursive solution will be:
    
    
    // Recursive Function to count of values
    // whose suffixes of length pos 
    // have remainder **rem** with K
    recur(pos, rem)
    

  * **Base Case:** The base case for this problem is when for any index the remainder of the suffix with K becomes 0, then all the other digits can be placed with all the possible integers from 0 to 9.
    
    
    f(pos, 0) = 9 * (10^(n-i-1))
    

  * **Recursive Case:** At each step of recursion we increase the suffix length by one by placing all integers from 0-9, change the remainder with K accordingly and move to the next step.
    
    
    for num in range [0-9]:
         f(pos, rem) += f(pos+1, (rem*10 + num)%k)
    

Below is the implemenation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to Count the

// numbers with N digits and whose 

// suffix is divisible by K

 

#include <bits/stdc++.h>

 

using namespace std;

 

int mod = 1000000007;

int dp[1005][105][2];

int powers[1005];

int powersModk[1005];

 

// Suffix of length pos with 

// remainder rem and Z representing

// whether the suffix has a 

// non zero digit until now

int calculate(int pos, int rem, 

 int z, int k, int n)

{

 // Base case

 if (rem == 0 && z) {

 

 // If count of digits 

 // is less than n

 if (pos != n)

 

 // Placing all possible 

 // digits in remaining 

 // positions

 return (powers[n - pos - 

 1] * 9) % mod;

 else

 return 1;

 }

 

 // If remainder non zero 

 // and suffix has n digits

 if (pos == n)

 return 0;

 

 // If the subproblem 

 // is already solved

 if (dp[pos][rem][z] != -1)

 return dp[pos][rem][z];

 

 int count = 0;

 

 // Placing all digits at MSB 

 // of suffix and increasing 

 // it's length by 1

 for (int i = 0; i < 10; i++) {

 if (i == 0)

 count = (count + (calculate(

 pos + 1, (rem + (i * 

 powersModk[pos]) % k) % 

 k, z, k, n))) % mod;

 

 // Non zero digit is placed

 else

 count = (count + (calculate(

 pos + 1, (rem + (i * 

 powersModk[pos]) % k) % 

 k, 1, k, n))) % mod;

 }

 

 // Store and return the 

 // solution to this subproblem

 return dp[pos][rem][z] = count;

}

 

// Function to Count the numbers 

// with N digits and whose suffix 

// is divisible by K

int countNumbers(int n, int k)

{

 

 // Since we need powers of 10 

 // for counting, it's better to 

 // pre store them along with their 

 // modulo with 1e9 + 7 for counting

 int st = 1;

 for (int i = 0; i <= n; i++) {

 powers[i] = st;

 st *= 10;

 st %= mod;

 }

 

 // Since at each recursive step 

 // we increase the suffix length by 1

 // by placing digits at its leftmost 

 // position, we need powers of 10

 // modded with k, in order to fpos 

 // the new remainder efficiently

 st = 1;

 for (int i = 0; i <= n; i++) {

 powersModk[i] = st;

 st *= 10;

 st %= mod;

 }

 

 // Initialising dp table values -1

 // represents subproblem hasn't 

 // been solved yet

 memset(dp, -1, sizeof(dp));

 

 return calculate(0, 0, 0, k, n);

}

 

// Driver Code

int main()

{

 int N = 2;

 int K = 2;

 

 cout << countNumbers(N, K);

 

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

// Java implementation to Count the

// numbers with N digits and whose 

// suffix is divisible by K

import java.util.*;

import java.util.Arrays;

 

class GFG

{

 

 static int mod = 1000000007;

 static int dp[][][] = new int[1005][105][2];

 static int powers[] = new int[1005];

 static int powersModk[] = new int[1005];

 

 // Suffix of length pos with 

 // remainder rem and Z representing

 // whether the suffix has a 

 // non zero digit until now

 static int calculate(int pos, int rem, 

 int z, int k, int n)

 {

 // Base case

 if (rem == 0 && z!=0) {

 

 // If count of digits 

 // is less than n

 if (pos != n)

 

 // Placing all possible 

 // digits in remaining 

 // positions

 return (powers[n - pos - 

 1] * 9) % mod;

 else

 return 1;

 }

 

 // If remainder non zero 

 // and suffix has n digits

 if (pos == n)

 return 0;

 

 // If the subproblem 

 // is already solved

 if (dp[pos][rem][z] != -1)

 return dp[pos][rem][z];

 

 int count = 0;

 

 // Placing all digits at MSB 

 // of suffix and increasing 

 // it's length by 1

 for (int i = 0; i < 10; i++) {

 if (i == 0)

 count = (count + (calculate(

 pos + 1, (rem + (i * 

 powersModk[pos]) % k) % 

 k, z, k, n))) % mod;

 

 // Non zero digit is placed

 else

 count = (count + (calculate(

 pos + 1, (rem + (i * 

 powersModk[pos]) % k) % 

 k, 1, k, n))) % mod;

 }

 

 // Store and return the 

 // solution to this subproblem

 return dp[pos][rem][z] = count;

 }

 

 // Function to Count the numbers 

 // with N digits and whose suffix 

 // is divisible by K

 static int countNumbers(int n, int k)

 {

 

 // Since we need powers of 10 

 // for counting, it's better to 

 // pre store them along with their 

 // modulo with 1e9 + 7 for counting

 int st = 1;

 int i;

 for (i = 0; i <= n; i++) {

 powers[i] = st;

 st *= 10;

 st %= mod;

 }

 

 // Since at each recursive step 

 // we increase the suffix length by 1

 // by placing digits at its leftmost 

 // position, we need powers of 10

 // modded with k, in order to fpos 

 // the new remainder efficiently

 st = 1;

 for (i = 0; i <= n; i++) {

 powersModk[i] = st;

 st *= 10;

 st %= mod;

 }

 

 // Initialising dp table values -1

 // represents subproblem hasn't 

 // been solved yet

 for (int[][] row: dp)

 {

 for (int[] innerRow: row)

 {

 Arrays.fill(innerRow, -1);

 }

 };

 

 return calculate(0, 0, 0, k, n);

 }

 

 // Driver Code

 public static void main(String []args)

 {

 int N = 2;

 int K = 2;

 

 System.out.print(countNumbers(N, K));

 }

}

 

// This code is contributed by chitranayal  
  
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

# Python3 implementation to Count the

# numbers with N digits and whose

# suffix is divisible by K

 

mod = 1000000007

dp = [[[-1 for i in range(2)] for i in
range(105)] for i in range(1005)]

powers = [0]*1005

powersModk = [0]*1005

 

# Suffix of length pos with

# remainder rem and Z representing

# whether the suffix has a

# non zero digit until now

def calculate(pos, rem, z, k, n):

 # Base case

 if (rem == 0 and z):

 

 # If count of digits

 # is less than n

 if (pos != n):

 

 # Placing all possible

 # digits in remaining

 # positions

 return (powers[n - pos -1] * 9) % mod

 else:

 return 1

 

 # If remainder non zero

 # and suffix has n digits

 if (pos == n):

 return 0

 

 # If the subproblem

 # is already solved

 if (dp[pos][rem][z] != -1):

 return dp[pos][rem][z]

 

 count = 0

 

 # Placing all digits at MSB

 # of suffix and increasing

 # it's length by 1

 for i in range(10):

 if (i == 0):

 count = (count + (calculate(

 pos + 1, (rem + (i *

 powersModk[pos]) % k) %

 k, z, k, n))) % mod

 

 # Non zero digit is placed

 else:

 count = (count + (calculate(

 pos + 1, (rem + (i *

 powersModk[pos]) % k) %

 k, 1, k, n))) % mod

 

 # Store and return the

 # solution to this subproblem

 dp[pos][rem][z] = count

 return count

 

# Function to Count the numbers

# with N digits and whose suffix

# is divisible by K

def countNumbers(n, k):

 

 # Since we need powers of 10

 # for counting, it's better to

 # pre store them along with their

 # modulo with 1e9 + 7 for counting

 st = 1

 for i in range(n + 1):

 powers[i] = st

 st *= 10

 st %= mod

 

 # Since at each recursive step

 # we increase the suffix length by 1

 # by placing digits at its leftmost

 # position, we need powers of 10

 # modded with k, in order to fpos

 # the new remainder efficiently

 st = 1

 for i in range(n + 1):

 powersModk[i] = st

 st *= 10

 st %= mod

 

 # Initialising dp table values -1

 # represents subproblem hasn't

 # been solved yet

 # memset(dp, -1, sizeof(dp))

 

 return calculate(0, 0, 0, k, n)

 

# Driver Code

if __name__ == '__main__':

 N = 2

 K = 2

 

 print(countNumbers(N, K))

 

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

// C# implementation to Count the

// numbers with N digits and whose 

// suffix is divisible by K

using System;

 

class GFG

{

 

 static int mod = 1000000007;

 static int [,,]dp = new int[1005, 105, 2];

 static int []powers = new int[1005];

 static int []powersModk = new int[1005];

 

 // Suffix of length pos with 

 // remainder rem and Z representing

 // whether the suffix has a 

 // non zero digit until now

 static int calculate(int pos, int rem, 

 int z, int k, int n)

 {

 // Base case

 if (rem == 0 && z != 0) {

 

 // If count of digits 

 // is less than n

 if (pos != n)

 

 // Placing all possible 

 // digits in remaining 

 // positions

 return (powers[n - pos - 

 1] * 9) % mod;

 else

 return 1;

 }

 

 // If remainder non zero 

 // and suffix has n digits

 if (pos == n)

 return 0;

 

 // If the subproblem 

 // is already solved

 if (dp[pos, rem, z] != -1)

 return dp[pos,rem,z];

 

 int count = 0;

 

 // Placing all digits at MSB 

 // of suffix and increasing 

 // it's length by 1

 for (int i = 0; i < 10; i++) {

 if (i == 0)

 count = (count + (calculate(

 pos + 1, (rem + (i * 

 powersModk[pos]) % k) % 

 k, z, k, n))) % mod;

 

 // Non zero digit is placed

 else

 count = (count + (calculate(

 pos + 1, (rem + (i * 

 powersModk[pos]) % k) % 

 k, 1, k, n))) % mod;

 }

 

 // Store and return the 

 // solution to this subproblem

 return dp[pos,rem,z] = count;

 }

 

 // Function to Count the numbers 

 // with N digits and whose suffix 

 // is divisible by K

 static int countNumbers(int n, int k)

 {

 

 // Since we need powers of 10 

 // for counting, it's better to 

 // pre store them along with their 

 // modulo with 1e9 + 7 for counting

 int st = 1;

 int i;

 for (i = 0; i <= n; i++) {

 powers[i] = st;

 st *= 10;

 st %= mod;

 }

 

 // Since at each recursive step 

 // we increase the suffix length by 1

 // by placing digits at its leftmost 

 // position, we need powers of 10

 // modded with k, in order to fpos 

 // the new remainder efficiently

 st = 1;

 for (i = 0; i <= n; i++) {

 powersModk[i] = st;

 st *= 10;

 st %= mod;

 }

 

 // Initialising dp table values -1

 // represents subproblem hasn't 

 // been solved yet

 for(i = 0; i < 1005; i++){

 for(int j = 0; j < 105; j++){

 for(int l = 0; l < 2; l++)

 dp[i, j, l] = -1;

 }

 }

 

 return calculate(0, 0, 0, k, n);

 }

 

 // Driver Code

 public static void Main(String []args)

 {

 int N = 2;

 int K = 2;

 

 Console.Write(countNumbers(N, K));

 }

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    45
    

**Time Complexity:** O(N * K)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

