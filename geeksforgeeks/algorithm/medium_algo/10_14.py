Count of Numbers in Range where the number does not contain more than K non
zero digits



Given a range represented by two positive integers L and R and a positive
integer K. Find the count of numbers in the range where the number does not
contain more than K non zero digits.

 **Examples:**

    
    
    **Input :** L = 1, R = 1000, K = 3
    **Output :** 1000
    **Explanation :** All the numbers from 1 to 1000 
    are 3 digit numbers which obviously cannot 
    contain more than 3 non zero digits.
    
    **Input :** L = 9995, R = 10005
    **Output :** 6
    **Explanation :** Required numbers are 
    10000, 10001, 10002, 10003, 10004 and 10005
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Prerequisites : Digit DP

There can be two approaches to solve this type of problem, one can be a
combinatorial solution and other can be a dynamic programming based solution.
Below is a detailed approach of solving this problem using a digit dynamic
programming approach.  
 **Dynamic Programming Solution :** Firstly, if we are able to count the
required numbers upto R i.e. in the range [0, R], we can easily reach our
answer in the range [L, R] by solving for from zero to R and then subtracting
the answer we get after solving for from zero to L – 1. Now, we need to define
the DP states.  
 **DP States** :

  * Since we can consider our number as a sequence of digits, one state is the **_position_** at which we are currently in. This position can have values from 0 to 18 if we are dealing with the numbers upto 1018. In each recursive call, we try to build the sequence from left to right by placing a digit from 0 to 9.
  * Second state is the **_count_** which defines the number of non zero digits, we have placed in the number we are trying to build.
  * Another state is the boolean variable **_tight_** which tells the number we are trying to build has already become smaller than R, so that in the upcoming recursive calls we can place any digit from 0 to 9. If the number has not become smaller, maximum limit of digit we can place is digit at current position in R.

In the final recursive call, when we are at the last position if the count of
non zero digits is less than or equal to K, return 1 otherwise return 0.

  

  

Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP Program to find the count of

// numbers in a range where the number

// does not contain more than K non

// zero digits

 

#include <bits/stdc++.h>

using namespace std;

 

const int M = 20;

 

// states - position, count, tight

int dp[M][M][2];

 

// K is the number of non zero digits

int K;

 

// This function returns the count of

// required numbers from 0 to num

int countInRangeUtil(int pos, int cnt, int tight,

 vector<int> num)

{

 // Last position

 if (pos == num.size()) {

 // If count of non zero digits

 // is less than or equal to K

 if (cnt <= K)

 return 1;

 return 0;

 }

 

 // If this result is already computed

 // simply return it

 if (dp[pos][cnt][tight] != -1)

 return dp[pos][cnt][tight];

 

 int ans = 0;

 

 // Maximum limit upto which we can place

 // digit. If tight is 1, means number has

 // already become smaller so we can place

 // any digit, otherwise num[pos]

 int limit = (tight ? 9 : num[pos]);

 

 for (int dig = 0; dig <= limit; dig++) {

 int currCnt = cnt;

 

 // If the current digit is nonzero

 // increment currCnt

 if (dig != 0)

 currCnt++;

 

 int currTight = tight;

 

 // At this position, number becomes

 // smaller

 if (dig < num[pos])

 currTight = 1;

 

 // Next recursive call

 ans += countInRangeUtil(pos + 1, currCnt,

 currTight, num);

 }

 return dp[pos][cnt][tight] = ans;

}

 

// This function converts a number into its

// digit vector and uses above function to compute

// the answer

int countInRange(int x)

{

 vector<int> num;

 while (x) {

 num.push_back(x % 10);

 x /= 10;

 }

 reverse(num.begin(), num.end());

 

 // Initialize dp

 memset(dp, -1, sizeof(dp));

 return countInRangeUtil(0, 0, 0, num);

}

 

// Driver Code to test above functions

int main()

{

 int L = 1, R = 1000;

 K = 3;

 cout << countInRange(R) - countInRange(L - 1) << endl;

 

 L = 9995, R = 10005, K = 2;

 cout << countInRange(R) - countInRange(L - 1) << endl;

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

// numbers in a range where the number 

// does not contain more than K non 

// zero digits

import java.util.*;

class Solution

{

static final int M = 20; 

 

// states - position, count, tight 

static int dp[][][]= new int[M][M][2]; 

 

// K is the number of non zero digits 

static int K; 

static Vector<Integer> num;

 

// This function returns the count of 

// required numbers from 0 to num 

static int countInRangeUtil(int pos, int cnt, int tight ) 

{ 

 // Last position 

 if (pos == num.size()) { 

 // If count of non zero digits 

 // is less than or equal to K 

 if (cnt <= K) 

 return 1; 

 return 0; 

 } 

 

 // If this result is already computed 

 // simply return it 

 if (dp[pos][cnt][tight] != -1) 

 return dp[pos][cnt][tight]; 

 

 int ans = 0; 

 

 // Maximum limit upto which we can place 

 // digit. If tight is 1, means number has 

 // already become smaller so we can place 

 // any digit, otherwise num[pos] 

 int limit = (tight!=0 ? 9 : num.get(pos)); 

 

 for (int dig = 0; dig <= limit; dig++) { 

 int currCnt = cnt; 

 

 // If the current digit is nonzero 

 // increment currCnt 

 if (dig != 0) 

 currCnt++; 

 

 int currTight = tight; 

 

 // At this position, number becomes 

 // smaller 

 if (dig < num.get(pos)) 

 currTight = 1; 

 

 // Next recursive call 

 ans += countInRangeUtil(pos + 1, currCnt, currTight); 

 } 

 return dp[pos][cnt][tight] = ans; 

} 

 

// This function converts a number into its 

// digit vector and uses above function to compute 

// the answer 

static int countInRange(int x) 

{ 

 num= new Vector<Integer>(); 

 while (x!=0) { 

 num.add(x % 10); 

 x /= 10; 

 } 

 Collections.reverse(num); 

 

 // Initialize dp 

 for(int i=0;i<M;i++)

 for(int j=0;j<M;j++)

 for(int k=0;k<2;k++)

 dp[i][j][k]=-1;

 return countInRangeUtil(0, 0, 0); 

} 

 

// Driver Code to test above functions 

public static void main(String args[])

{ 

 int L = 1, R = 1000; 

 K = 3; 

 System.out.println( countInRange(R) - countInRange(L - 1) ); 

 

 L = 9995; R = 10005; K = 2; 

 System.out.println( countInRange(R) - countInRange(L - 1) ); 

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

# numbers in a range where the number

# does not contain more than K non

# zero digits

 

# This function returns the count of

# required numbers from 0 to num

def countInRangeUtil(pos, cnt, tight, num):

 

 # Last position

 if pos == len(num):

 

 # If count of non zero digits

 # is less than or equal to K

 if cnt <= K:

 return 1

 return 0

 

 # If this result is already computed

 # simply return it

 if dp[pos][cnt][tight] != -1:

 return dp[pos][cnt][tight]

 

 ans = 0

 

 # Maximum limit upto which we can place

 # digit. If tight is 1, means number has

 # already become smaller so we can place

 # any digit, otherwise num[pos]

 limit = 9 if tight else num[pos]

 

 for dig in range(limit + 1):

 currCnt = cnt

 

 # If the current digit is nonzero

 # increment currCnt

 if dig != 0:

 currCnt += 1

 

 currTight = tight

 

 # At this position, number becomes

 # smaller

 if dig < num[pos]:

 currTight = 1

 

 # Next recursive call

 ans += countInRangeUtil(pos + 1, currCnt, currTight, num)

 

 dp[pos][cnt][tight] = ans

 return dp[pos][cnt][tight]

 

# This function converts a number into its

# digit vector and uses above function to compute

# the answer

def countInRange(x):

 global dp, K, M

 

 num = []

 while x:

 num.append(x % 10)

 x //= 10

 

 num.reverse()

 

 # Initialize dp

 dp = [[[-1, -1] for i in range(M)] for j
in range(M)]

 return countInRangeUtil(0, 0, 0, num)

 

# Driver Code

if __name__ == "__main__":

 

 # states - position, count, tight

 dp = []

 M = 20

 

 # K is the number of non zero digits

 K = 0

 

 L = 1

 R = 1000

 K = 3

 print(countInRange(R) - countInRange(L - 1))

 

 L = 9995

 R = 10005

 K = 2

 print(countInRange(R) - countInRange(L - 1))

 

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

// numbers in a range where the number 

// does not contain more than K non 

// zero digits

using System;

using System.Collections.Generic; 

 

class GFG

{

 

static int M = 20; 

 

// states - position, count, tight 

static int [,,]dp = new int[M, M, 2]; 

 

// K is the number of non zero digits 

static int K; 

static List<int> num;

 

// This function returns the count of 

// required numbers from 0 to num 

static int countInRangeUtil(int pos,

 int cnt, int tight ) 

{ 

 // Last position 

 if (pos == num.Count) 

 { 

 // If count of non zero digits 

 // is less than or equal to K 

 if (cnt <= K) 

 return 1; 

 return 0; 

 } 

 

 // If this result is already computed 

 // simply return it 

 if (dp[pos, cnt, tight] != -1) 

 return dp[pos, cnt, tight]; 

 

 int ans = 0; 

 

 // Maximum limit upto which we can place 

 // digit. If tight is 1, means number has 

 // already become smaller so we can place 

 // any digit, otherwise num[pos] 

 int limit = (tight != 0 ? 9 : num[pos]); 

 

 for (int dig = 0; dig <= limit; dig++) 

 { 

 int currCnt = cnt; 

 

 // If the current digit is nonzero 

 // increment currCnt 

 if (dig != 0) 

 currCnt++; 

 

 int currTight = tight; 

 

 // At this position, number becomes 

 // smaller 

 if (dig < num[pos]) 

 currTight = 1; 

 

 // Next recursive call 

 ans += countInRangeUtil(pos + 1, currCnt, currTight); 

 } 

 return dp[pos,cnt,tight] = ans; 

} 

 

// This function converts a number into its 

// digit vector and uses above function to compute 

// the answer 

static int countInRange(int x) 

{ 

 num = new List<int>(); 

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

 dp[i, j, k] = -1;

 return countInRangeUtil(0, 0, 0); 

} 

 

// Driver Code 

public static void Main()

{ 

 int L = 1, R = 1000; 

 K = 3; 

 Console.WriteLine( countInRange(R) - countInRange(L - 1) ); 

 

 L = 9995; R = 10005; K = 2; 

 Console.WriteLine( countInRange(R) - countInRange(L - 1) ); 

}

} 

 

/* This code contributed by PrinciRaj1992 */  
  
---  
  
 __

 __

 **Output:**

    
    
    1000
    6
    

**Time Complexity :** O(18 * 18 * 2 * 10), if we are dealing with the numbers
upto 1018

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

