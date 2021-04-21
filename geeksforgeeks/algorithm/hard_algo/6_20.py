Count of numbers between range having only non-zero digits whose sum of digits
is N and number is divisible by M



Given a range **[L, R]** and two positive integers **N** and **M**. The task
is to count the numbers in the range containing only non-zero digits whose
**sum of digits is equal to N** and the **number is divisible by M**.

 **Examples:**

>  **Input:** L = 1, R = 100, N = 8, M = 2  
>  **Output:** 4  
> Only 8, 26, 44 and 62 are valid numbers
>
>  **Input:** L = 1, R = 200, N = 4, M = 11  
>  **Output:** 2  
> Only 22 and 121 are valid numbers

 **Prerequisites :**Digit DP

  

  

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Firstly, if we are able to count the required numbers up to R
i.e. in the range [0, R], we can easily reach our answer in the range [L, R]
by solving for from zero to R and then subtracting the answer we get after
solving for from zero to L – 1. Now, we need to define the DP states.  
 **DP States** :

  * Since we can consider our number as a sequence of digits, one state is the **position** at which we are currently in. This position can have values from 0 to 18 if we are dealing with the numbers up to 1018. In each recursive call, we try to build the sequence from left to right by placing a digit from 0 to 9.
  * Second state is the **sum** of the digits we have placed so far.
  * Third state is the **remainder** which defines the modulus of the number we have made so far modulo M.
  * Another state is the boolean variable **tight** which tells the number we are trying to build has already become smaller than R so that in the upcoming recursive calls we can place any digit from 0 to 9. If the number has not become smaller, the maximum limit of digit we can place is digit at the current position in R.

For the number to have only non-zero digits, we maintain a variable **nonz**
whose value if 1 tells the first digit in the number we have placed is a non-
zero digit and thus, now we can’t place any zero digit in upcoming calls.
Otherwise, we can place a zero digit as a leading zero so as to make number of
digits in current number smaller than number of digits in upper limit.

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

 

const int M = 20;

 

// states - position, sum, rem, tight

// sum can have values upto 162, if we

// are dealing with numbers upto 10^18

// when all 18 digits are 9, then sum

// is 18 * 9 = 162

int dp[M][165][M][2];

 

// n is the sum of digits and number should

// be divisible by m

int n, m;

 

// Function to return the count of

// required numbers from 0 to num

int count(int pos, int sum, int rem, int tight,

 int nonz, vector<int> num)

{

 // Last position

 if (pos == num.size()) {

 if (rem == 0 && sum == n)

 return 1;

 return 0;

 }

 

 // If this result is already computed

 // simply return it

 if (dp[pos][sum][rem][tight] != -1)

 return dp[pos][sum][rem][tight];

 

 int ans = 0;

 

 // Maximum limit upto which we can place

 // digit. If tight is 1, means number has

 // already become smaller so we can place

 // any digit, otherwise num[pos]

 int limit = (tight ? 9 : num[pos]);

 

 for (int d = 0; d <= limit; d++) {

 

 // If the current digit is zero

 // and nonz is 1, we can't place it

 if (d == 0 && nonz)

 continue;

 int currSum = sum + d;

 int currRem = (rem * 10 + d) % m;

 int currF = tight || (d < num[pos]);

 ans += count(pos + 1, currSum, currRem,

 currF, nonz || d, num);

 }

 return dp[pos][sum][rem][tight] = ans;

}

 

// Function to convert x into its digit vector

// and uses count() function to return the

// required count

int solve(int x)

{

 vector<int> num;

 while (x) {

 num.push_back(x % 10);

 x /= 10;

 }

 reverse(num.begin(), num.end());

 

 // Initialize dp

 memset(dp, -1, sizeof(dp));

 return count(0, 0, 0, 0, 0, num);

}

 

// Driver code

int main()

{

 int L = 1, R = 100;

 n = 8, m = 2;

 cout << solve(R) - solve(L);

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

 

static int M = 20; 

 

// states - position, sum, rem, tight 

// sum can have values upto 162, if we 

// are dealing with numbers upto 10^18 

// when all 18 digits are 9, then sum 

// is 18 * 9 = 162 

static int dp[][][][] = new int [M][165][M][2]; 

 

// n is the sum of digits and number should 

// be divisible by m 

static int n, m; 

 

// Function to return the count of 

// required numbers from 0 to num 

static int count(int pos, int sum, int rem, int tight, 

 int nonz, Vector<Integer> num) 

{ 

 // Last position 

 if (pos == num.size())

 { 

 if (rem == 0 && sum == n) 

 return 1; 

 return 0; 

 } 

 

 // If this result is already computed 

 // simply return it 

 if (dp[pos][sum][rem][tight] != -1) 

 return dp[pos][sum][rem][tight]; 

 

 int ans = 0; 

 

 // Maximum limit upto which we can place 

 // digit. If tight is 1, means number has 

 // already become smaller so we can place 

 // any digit, otherwise num[pos] 

 int limit = (tight != 0 ? 9 : num.get(pos)); 

 

 for (int d = 0; d <= limit; d++)

 { 

 

 // If the current digit is zero 

 // and nonz is 1, we can't place it 

 if (d == 0 && nonz != 0) 

 continue; 

 int currSum = sum + d; 

 int currRem = (rem * 10 + d) % m; 

 int currF = (tight != 0 || (d < num.get(pos))) ? 1 : 0; 

 ans += count(pos + 1, currSum, currRem, 

 currF, (nonz != 0 || d != 0) ? 1 : 0, num); 

 } 

 return dp[pos][sum][rem][tight] = ans; 

} 

 

// Function to convert x into its digit vector 

// and uses count() function to return the 

// required count 

static int solve(int x) 

{ 

 Vector<Integer> num = new Vector<Integer>(); 

 while (x != 0) 

 { 

 num.add(x % 10); 

 x /= 10; 

 } 

 Collections.reverse(num); 

 

 // Initialize dp 

 for(int i = 0; i < M; i++)

 for(int j = 0; j < 165; j++)

 for(int k = 0; k < M; k++)

 for(int l = 0; l < 2; l++)

 dp[i][j][k][l]=-1;

 

 return count(0, 0, 0, 0, 0, num); 

} 

 

// Driver code 

public static void main(String args[]) 

{ 

 int L = 1, R = 100; 

 n = 8; m = 2; 

 System.out.print( solve(R) - solve(L)); 

} 

}

 

// This code is contributed by Arnab Kundu  
  
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

 

# Function to return the count of 

# required numbers from 0 to num 

def count(pos, Sum, rem, tight, nonz, num): 

 

 # Last position 

 if pos == len(num): 

 if rem == 0 and Sum == n: 

 return 1

 return 0

 

 # If this result is already computed 

 # simply return it

 if dp[pos][Sum][rem][tight] != -1: 

 return dp[pos][Sum][rem][tight] 

 

 ans = 0

 

 # Maximum limit upto which we can place 

 # digit. If tight is 1, means number has 

 # already become smaller so we can place 

 # any digit, otherwise num[pos]

 if tight:

 limit = 9

 else: 

 limit = num[pos]

 

 for d in range(0, limit + 1): 

 

 # If the current digit is zero 

 # and nonz is 1, we can't place it 

 if d == 0 and nonz:

 continue

 

 currSum = Sum + d 

 currRem = (rem * 10 + d) % m 

 currF = int(tight or (d < num[pos])) 

 ans += count(pos + 1, currSum, currRem, 

 currF, nonz or d, num) 

 

 dp[pos][Sum][rem][tight] = ans

 return ans

 

# Function to convert x into its digit 

# vector and uses count() function to 

# return the required count 

def solve(x): 

 

 num = []

 global dp

 

 while x > 0: 

 num.append(x % 10) 

 x //= 10

 

 num.reverse() 

 

 # Initialize dp 

 dp = [[[[-1, -1] for i in range(M)] 

 for j in range(165)] 

 for k in range(M)]

 return count(0, 0, 0, 0, 0, num) 

 

# Driver code 

if __name__ == "__main__":

 

 L, R = 1, 100

 

 # n is the sum of digits and number 

 # should be divisible by m

 n, m, M = 8, 2, 20

 

 # States - position, sum, rem, tight 

 # sum can have values upto 162, if we 

 # are dealing with numbers upto 10^18 

 # when all 18 digits are 9, then sum 

 # is 18 * 9 = 162 

 dp = []

 

 print(solve(R) - solve(L)) 

 

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

using System.Collections.Generic;

 

class GFG

{

 

static int M = 20; 

 

// states - position, sum, rem, tight 

// sum can have values upto 162, if we 

// are dealing with numbers upto 10^18 

// when all 18 digits are 9, then sum 

// is 18 * 9 = 162 

static int [,,,]dp = new int [M, 165, M, 2]; 

 

// n is the sum of digits and number should 

// be divisible by m 

static int n, m; 

 

// Function to return the count of 

// required numbers from 0 to num 

static int count(int pos, int sum, int rem, int tight, 

 int nonz, List<int> num) 

{ 

 // Last position 

 if (pos == num.Count)

 { 

 if (rem == 0 && sum == n) 

 return 1; 

 return 0; 

 } 

 

 // If this result is already computed 

 // simply return it 

 if (dp[pos,sum,rem,tight] != -1) 

 return dp[pos,sum,rem,tight]; 

 

 int ans = 0; 

 

 // Maximum limit upto which we can place 

 // digit. If tight is 1, means number has 

 // already become smaller so we can place 

 // any digit, otherwise num[pos] 

 int limit = (tight != 0 ? 9 : num[pos]); 

 

 for (int d = 0; d <= limit; d++)

 { 

 

 // If the current digit is zero 

 // and nonz is 1, we can't place it 

 if (d == 0 && nonz != 0) 

 continue; 

 int currSum = sum + d; 

 int currRem = (rem * 10 + d) % m; 

 int currF = (tight != 0 || (d < num[pos])) ? 1 : 0; 

 ans += count(pos + 1, currSum, currRem, 

 currF, (nonz != 0 || d != 0) ? 1 : 0, num); 

 } 

 return dp[pos, sum, rem, tight] = ans; 

} 

 

// Function to convert x into its digit vector 

// and uses count() function to return the 

// required count 

static int solve(int x) 

{ 

 List<int> num = new List<int>(); 

 while (x != 0) 

 { 

 num.Add(x % 10); 

 x /= 10; 

 } 

 num.Reverse(); 

 

 // Initialize dp 

 for(int i = 0; i < M; i++)

 for(int j = 0; j < 165; j++)

 for(int k = 0; k < M; k++)

 for(int l = 0; l < 2; l++)

 dp[i, j, k, l] = -1;

 

 return count(0, 0, 0, 0, 0, num); 

} 

 

// Driver code 

public static void Main(String []args) 

{ 

 int L = 1, R = 100; 

 n = 8; m = 2; 

 Console.Write( solve(R) - solve(L)); 

} 

}

 

// This code has been contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

**  
Short Python Implementation :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# User Input

l, r, n, m = 1, 100, 8, 2

 

# Initialize Result

output = []

 

# Traverse through all numbers

for x in range(l, r+1):

 

 # Check for all conditions in every number 

 if sum([int(k) for k in str(x)]) == n and x
% m == 0 and '0' not in str(x): # Check conditions

 output.append(x)

 

print(len(output)) 

 

# This code is contributed by mailprakashindia  
  
---  
  
 __

 __

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

