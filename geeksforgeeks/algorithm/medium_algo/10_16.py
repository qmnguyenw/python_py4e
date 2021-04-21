Count of Numbers in a Range where digit d occurs exactly K times



Given two positive integers **L** and **R** which represents a range and two
more positive integers **d** and **K**. The task is to find the count of
numbers in the range where digit **d** occurs exactly **K** times.

 **Examples:**

>  **Input:** L = 11, R = 100, d = 2, k = 1  
>  **Output:** 17  
> Required numbers are 12, 20, 21, 23, 24, 25, 26, 27, 28, 29, 32, 42, 52, 62,
> 72, 82 and 92.
>
>  **Input:** L = 95, R = 1005, d = 0, k = 2  
>  **Output:** 14

Prerequisites : Digit DP

  

  

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Firstly, if we are able to count the required numbers upto R
i.e. in the range [0, R], we can easily reach our answer in the range [L, R]
by solving for from zero to R and then subtracting the answer we get after
solving for from zero to L – 1. Now, we need to define the DP states.  
 **DP States** :

* Since we can consider our number as a sequence of digits, one state is the **_position_** at which we are currently in. This position can have values from 0 to 18 if we are dealing with the numbers upto 1018. In each recursive call, we try to build the sequence from left to right by placing a digit from 0 to 9.
* Second state is the **_count_** which defines the number of times, we have placed digit d so far.
* Another state is the boolean variable **_tight_** which tells the number we are trying to build has already become smaller than R so that in the upcoming recursive calls we can place any digit from 0 to 9. If the number has not become smaller, maximum limit of digit we can place is digit at current position in R.
* Last state is also boolean variable **_nonz_** which helps to consider the situation if are any leading zeroes in the number we are building, we don’t need to count them.

In the final recursive call, when we are at the last position if the count of
digit d is equal to K, return 1 otherwise return 0.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP Program to find the count of

// numbers in a range where digit d

// occurs exactly K times

#include <bits/stdc++.h>

using namespace std;

 

const int M = 20;

 

// states - position, count, tight, nonz

int dp[M][M][2][2];

 

// d is required digit and K is occurrence

int d, K;

 

// This function returns the count of

// required numbers from 0 to num

int count(int pos, int cnt, int tight,

 int nonz, vector<int> num)

{

 // Last position

 if (pos == num.size()) {

 if (cnt == K)

 return 1;

 return 0;

 }

 

 // If this result is already computed

 // simply return it

 if (dp[pos][cnt][tight][nonz] != -1)

 return dp[pos][cnt][tight][nonz];

 

 int ans = 0;

 

 // Maximum limit upto which we can place

 // digit. If tight is 1, means number has

 // already become smaller so we can place

 // any digit, otherwise num[pos]

 int limit = (tight ? 9 : num[pos]);

 

 for (int dig = 0; dig <= limit; dig++) {

 int currCnt = cnt;

 

 // Nonz is true if we placed a non

 // zero digit at the starting of

 // the number

 if (dig == d) {

 if (d != 0 || (!d && nonz))

 currCnt++;

 }

 

 int currTight = tight;

 

 // At this position, number becomes

 // smaller

 if (dig < num[pos])

 currTight = 1;

 

 // Next recursive call, also set nonz

 // to 1 if current digit is non zero

 ans += count(pos + 1, currCnt,

 currTight, nonz || (dig != 0), num);

 }

 return dp[pos][cnt][tight][nonz] = ans;

}

 

// Function to convert x into its digit vector and uses

// count() function to return the required count

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

 return count(0, 0, 0, 0, num);

}

 

// Driver Code to test above functions

int main()

{

 int L = 11, R = 100;

 d = 2, K = 1;

 cout << solve(R) - solve(L - 1) << endl;

 

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

// Java Program to find the count of

// numbers in a range where digit d

// occurs exactly K times

import java.util.*;

class Solution

{

static final int M = 20;

 

// states - position, count, tight, nonz

static int dp[][][][]= new int[M][M][2][2];

 

// d is required digit and K is occurrence

static int d, K;

 

// This function returns the count of

// required numbers from 0 to num

static int count(int pos, int cnt, int tight,

 int nonz, Vector<Integer> num)

{

 // Last position

 if (pos == num.size()) {

 if (cnt == K)

 return 1;

 return 0;

 }

 

 // If this result is already computed

 // simply return it

 if (dp[pos][cnt][tight][nonz] != -1)

 return dp[pos][cnt][tight][nonz];

 

 int ans = 0;

 

 // Maximum limit upto which we can place

 // digit. If tight is 1, means number has

 // already become smaller so we can place

 // any digit, otherwise num[pos]

 int limit = ((tight !=0)? 9 : num.get(pos));

 

 for (int dig = 0; dig <= limit; dig++) {

 int currCnt = cnt;

 

 // Nonz is true if we placed a non

 // zero digit at the starting of

 // the number

 if (dig == d) {

 if (d != 0 || (d==0 && nonz!=0))

 currCnt++;

 }

 

 int currTight = tight;

 

 // At this position, number becomes

 // smaller

 if (dig < num.get(pos))

 currTight = 1;

 

 // Next recursive call, also set nonz

 // to 1 if current digit is non zero

 ans += count(pos + 1, currCnt,

 currTight, (dig != 0?1:0), num);

 }

 return dp[pos][cnt][tight][nonz] = ans;

}

 

// Function to convert x into its digit vector and uses

// count() function to return the required count

static int solve(int x)

{

 Vector<Integer> num= new Vector<Integer>();

 while (x!=0) {

 num.add(x % 10);

 x /= 10;

 }

 Collections.reverse(num);

 

 // Initialize dp

 for(int i=0;i<M;i++)

 for(int j=0;j<M;j++)

 for(int k=0;k<2;k++)

 for(int l=0;l<2;l++)

 dp[i][j][k][l]=-1;

 

 return count(0, 0, 0, 0, num);

}

 

// Driver Code to test above functions

public static void main(String args[])

{

 int L = 11, R = 100;

 d = 2; K = 1;

 System.out.print( solve(R) - solve(L - 1) );

}

 

}

//contributed by Arnab Kundu  
  
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

# Python Program to find the count of

# numbers in a range where digit d

# occurs exactly K times

M = 20

 

# states - position, count, tight, nonz

dp = []

 

# d is required digit and K is occurrence

d, K = None, None

 

# This function returns the count of

# required numbers from 0 to num

def count(pos, cnt, tight, nonz, num: list):

 

 # Last position

 if pos == len(num):

 if cnt == K:

 return 1

 return 0

 

 # If this result is already computed

 # simply return it

 if dp[pos][cnt][tight][nonz] != -1:

 return dp[pos][cnt][tight][nonz]

 

 ans = 0

 

 # Maximum limit upto which we can place

 # digit. If tight is 1, means number has

 # already become smaller so we can place

 # any digit, otherwise num[pos]

 limit = 9 if tight else num[pos]

 

 for dig in range(limit + 1):

 currCnt = cnt

 

 # Nonz is true if we placed a non

 # zero digit at the starting of

 # the number

 if dig == d:

 if d != 0 or not d and nonz:

 currCnt += 1

 

 currTight = tight

 

 # At this position, number becomes

 # smaller

 if dig < num[pos]:

 currTight = 1

 

 # Next recursive call, also set nonz

 # to 1 if current digit is non zero

 ans += count(pos + 1, currCnt, 

 currTight, (nonz or dig != 0), num)

 

 dp[pos][cnt][tight][nonz] = ans

 return dp[pos][cnt][tight][nonz]

 

 

# Function to convert x into its digit vector and uses

# count() function to return the required count

def solve(x):

 global dp, K, d

 

 num = []

 while x:

 num.append(x % 10)

 x //= 10

 

 num.reverse()

 

 # Initialize dp

 dp = [[[[-1, -1] for i in range(2)] 

 for j in range(M)] for k in range(M)]

 return count(0, 0, 0, 0, num)

 

# Driver Code

if __name__ == "__main__":

 

 L = 11

 R = 100

 d = 2

 K = 1

 print(solve(R) - solve(L - 1))

 

# This code is contributed by

# sanjeev2552  
  
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

// C# Program to find the count of

// numbers in a range where digit d

// occurs exactly K times

using System;

using System.Collections.Generic; 

 

class GFG

{

 static readonly int M = 20;

 

 // states - position, count, tight, nonz

 static int [,,,]dp= new int[M, M, 2, 2];

 

 // d is required digit and K is occurrence

 static int d, K;

 

 // This function returns the count of

 // required numbers from 0 to num

 static int count(int pos, int cnt, int tight,

 int nonz, List<int> num)

 {

 // Last position

 if (pos == num.Count) 

 {

 if (cnt == K)

 return 1;

 return 0;

 }

 

 // If this result is already computed

 // simply return it

 if (dp[pos, cnt, tight, nonz] != -1)

 return dp[pos, cnt, tight, nonz];

 

 int ans = 0;

 

 // Maximum limit upto which we can place

 // digit. If tight is 1, means number has

 // already become smaller so we can place

 // any digit, otherwise num[pos]

 int limit = ((tight != 0) ? 9 : num[pos]);

 

 for (int dig = 0; dig <= limit; dig++)

 {

 int currCnt = cnt;

 

 // Nonz is true if we placed a non

 // zero digit at the starting of

 // the number

 if (dig == d) 

 {

 if (d != 0 || (d == 0 && nonz != 0))

 currCnt++;

 }

 

 int currTight = tight;

 

 // At this position, number becomes

 // smaller

 if (dig < num[pos])

 currTight = 1;

 

 // Next recursive call, also set nonz

 // to 1 if current digit is non zero

 ans += count(pos + 1, currCnt,

 currTight, (dig != 0 ? 1 : 0), num);

 }

 return dp[pos, cnt, tight, nonz] = ans;

 }

 

 // Function to convert x into its 

 // digit vector and uses count() 

 // function to return the required count

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

 for(int j = 0; j < M; j++)

 for(int k = 0; k < 2; k++)

 for(int l = 0; l < 2; l++)

 dp[i, j, k, l]=-1;

 

 return count(0, 0, 0, 0, num);

 }

 

 // Driver Code 

 public static void Main()

 {

 int L = 11, R = 100;

 d = 2; K = 1;

 Console.Write( solve(R) - solve(L - 1) );

 }

}

 

// This code is contributed by Rajput-JI  
  
---  
  
 __

 __

 **Output:**

    
    
    17
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

