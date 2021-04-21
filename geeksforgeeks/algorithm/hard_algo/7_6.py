Count of Numbers in a Range divisible by m and having digit d in even
positions



Given a range represented by two positive integers **l** and **r** and two
integers **d** and **m**. Find the count of numbers lying in the range which
is divisible by m and have digit d at even positions of the number. (i.e.
digit d should not occur on odd position). **Note:** Both numbers l and r have
same number of digits.

>  **Examples:**  
>  **Input :** l = 10, r = 99, d = 8, m = 2  
>  **Output :** 8  
>  **Explanation :** Valid numbers are 18, 28, 38, 48, 58, 68, 78 and 98.  
> 88 is not a valid number since 8 is also present at odd position.
>
>  **Input :** l = 1000, r = 9999, d = 7, m = 19  
>  **Output :** 6

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Prerequisites :**Digit DP

 **Approach:** Firstly, if we are able to count the required numbers up to R
i.e. in the range [0, R], we can easily reach our answer in the range [L, R]
by solving for from zero to R and then subtracting the answer we get after
solving for from zero to L – 1. Now, we need to define the DP states.  
 **DP States:**

  

  

  * Since we can consider our number as a sequence of digits, one state is the position at which we are currently in. This position can have values from 0 to 18 if we are dealing with the numbers up to 1018. In each recursive call, we try to build the sequence from left to right by placing a digit from 0 to 9.
  * Second state is the remainder which defines the modulus of the number we have made so far modulo m.
  * Another state is the boolean variable tight which tells the number we are trying to build has already become smaller than R so that in the upcoming recursive calls we can place any digit from 0 to 9. If the number has not become smaller, the maximum limit of digit we can place is digit at the current position in R.

If the current position is an even position, we simply place digit d and
recursively solve for the next positions. But if the current position is an
odd position we can place any digit except d and solve for the next positions.

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

// numbers in a range divisible by m

// having digit d at even positions

#include <bits/stdc++.h>

using namespace std;

 

const int M = 20;

 

// states - position, rem, tight

int dp[M][M][2];

 

// d is required digit and number should

// be divisible by m

int d, m;

 

// This function returns the count of

// required numbers from 0 to num

int count(int pos, int rem, int tight,

 vector<int> num)

{

 // Last position

 if (pos == num.size()) {

 if (rem == 0)

 return 1;

 return 0;

 }

 

 // If this result is already computed

 // simply return it

 if (dp[pos][rem][tight] != -1)

 return dp[pos][rem][tight];

 

 // If the current position is even, place

 // digit d, but since we have considered

 // 0-indexing, check for odd positions

 if (pos % 2) {

 if (tight == 0 && d > num[pos])

 return 0;

 

 int currTight = tight;

 

 // At this position, number becomes

 // smaller

 if (d < num[pos])

 currTight = 1;

 

 int res = count(pos + 1, (10 * rem + d)

 % m,

 currTight, num);

 return dp[pos][rem][tight] = res;

 }

 

 int ans = 0;

 

 // Maximum limit upto which we can place

 // digit. If tight is 1, means number has

 // already become smaller so we can place

 // any digit, otherwise num[pos]

 int limit = (tight ? 9 : num[pos]);

 

 for (int dig = 0; dig <= limit; dig++) {

 

 if (dig == d)

 continue;

 

 int currTight = tight;

 

 // At this position, number becomes

 // smaller

 if (dig < num[pos])

 currTight = 1;

 

 // Next recursive call, also set nonz

 // to 1 if current digit is non zero

 ans += count(pos + 1, (10 * rem + dig)

 % m,

 currTight, num);

 }

 return dp[pos][rem][tight] = ans;

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

 return count(0, 0, 0, num);

}

 

// Driver Code to test above functions

int main()

{

 int L = 10, R = 99;

 d = 8, m = 2;

 cout << solve(R) - solve(L) << endl;

 

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

// numbers in a range divisible by m 

// having digit d at even positions

 

import java.util.*;

 

class GFG 

{

 

 static int M = 20;

 

 // states - position, rem, tight

 static Integer[][][] dp = new Integer[M][M][2];

 

 // d is required digit and number should

 // be divisible by m

 static int d, m;

 

 // This function returns the count of

 // required numbers from 0 to num

 static int count(int pos, int rem, int tight,

 Vector<Integer> num)

 {

 

 // Last position

 if (pos == num.size()) 

 {

 if (rem == 0)

 return 1;

 return 0;

 }

 

 // If this result is already computed

 // simply return it

 if (dp[pos][rem][tight] != -1)

 return dp[pos][rem][tight];

 

 // If the current position is even, place

 // digit d, but since we have considered

 // 0-indexing, check for odd positions

 if (pos % 2 == 1)

 {

 if (tight == 0 && d > num.elementAt(pos))

 return 0;

 

 int currTight = tight;

 

 // At this position, number becomes

 // smaller

 if (d < num.elementAt(pos))

 currTight = 1;

 

 int res = count(pos + 1, (10 * rem + d) % m,

 currTight, num);

 return dp[pos][rem][tight] = res;

 }

 

 int ans = 0;

 

 // Maximum limit upto which we can place

 // digit. If tight is 1, means number has

 // already become smaller so we can place

 // any digit, otherwise num[pos]

 int limit = (tight != 0) ? 9 : num.elementAt(pos);

 for (int dig = 0; dig <= limit; dig++) 

 {

 

 if (dig == d)

 continue;

 

 int currTight = tight;

 

 // At this position, number becomes

 // smaller

 if (dig < num.elementAt(pos))

 currTight = 1;

 

 // Next recursive call, also set nonz

 // to 1 if current digit is non zero

 ans += count(pos + 1, (10 * rem + dig) % m,

 currTight, num);

 }

 return dp[pos][rem][tight] = ans;

 }

 

 // Function to convert x into its digit vector

 // and uses count() function to return the

 // required count

 static int solve(int x)

 {

 Vector<Integer> num = new Vector<>();

 while (x > 0)

 {

 num.add(x % 10);

 x /= 10;

 }

 Collections.reverse(num);

 

 // Initialize dp

 for (int i = 0; i < dp.length; i++)

 for (int j = 0; j < dp[i].length; j++)

 for (int k = 0; k < dp[i][j].length; k++)

 dp[i][j][k] = -1;

 

 return count(0, 0, 0, num);

 }

 

 // Driver Code

 public static void main(String[] args)

 {

 int L = 10, R = 99;

 d = 8;

 m = 2;

 System.out.println(solve(R) - solve(L));

 }

}

 

// This code is contributed by

// sanjeev2552  
  
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

# Python3 Program to find the count of

# numbers in a range divisible by m 

# having digit d at even positions 

 

# This Function returns the count of 

# required numbers from 0 to num 

def count(pos, rem, tight, num): 

 

 # Last position 

 if pos == len(num): 

 if rem == 0: 

 return 1

 return 0

 

 # If this result is already

 # computed simply return it 

 if dp[pos][rem][tight] != -1: 

 return dp[pos][rem][tight] 

 

 # If the current position is even, 

 # place digit d, but since we have 

 # considered 0-indexing, check for 

 # odd positions 

 if pos % 2 == 1:

 if tight == 0 and d > num[pos]: 

 return 0

 

 currTight = tight 

 

 # At this position, number 

 # becomes smaller 

 if d < num[pos]: 

 currTight = 1

 

 res = count(pos + 1, (10 * rem + d) % m, 

 currTight, num)

 

 dp[pos][rem][tight] = res 

 return res

 

 ans = 0

 

 # Maximum limit upto which we can place 

 # digit. If tight is 1, means number has 

 # already become smaller so we can place 

 # any digit, otherwise num[pos] 

 limit = 9 if tight else num[pos] 

 

 for dig in range(0, limit + 1): 

 if dig == d:

 continue

 

 currTight = tight 

 

 # At this position, number becomes 

 # smaller 

 if dig < num[pos]: 

 currTight = 1

 

 # Next recursive call, also set nonz 

 # to 1 if current digit is non zero 

 ans += count(pos + 1, (10 * rem + dig) % m, 

 currTight, num) 

 

 dp[pos][rem][tight] = ans

 return ans

 

# Function to convert x into its digit 

# vector and uses count() function to 

# return the required count 

def solve(x): 

 

 global dp

 num = [] 

 while x > 0: 

 num.append(x % 10) 

 x = x // 10

 

 num.reverse() 

 # Initialize dp with -1

 dp = [[[-1, -1] for x in range(M)] 

 for y in range(M)]

 

 return count(0, 0, 0, num) 

 

# Driver Code

if __name__ == "__main__":

 

 L, R = 10, 99

 

 # d is required digit and number

 # should be divisible by m 

 d, m = 8, 2

 M = 20

 

 # states - position, rem, tight

 dp = []

 print(solve(R) - solve(L))

 

# This code is contributed 

# by Rituraj Jain  
  
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

// numbers in a range divisible by m 

// having digit d at even positions

using System;

using System.Collections.Generic;

 

class GFG 

{

 

 static int M = 20;

 

 // states - position, rem, tight

 static int[,,] dp = new int[M, M, 2];

 

 // d is required digit and number should

 // be divisible by m

 static int d, m;

 

 // This function returns the count of

 // required numbers from 0 to num

 static int count(int pos, int rem, int tight,

 List<int> num)

 {

 

 // Last position

 if (pos == num.Count) 

 {

 if (rem == 0)

 return 1;

 return 0;

 }

 

 // If this result is already computed

 // simply return it

 if (dp[pos, rem, tight] != -1)

 return dp[pos, rem, tight];

 

 // If the current position is even, place

 // digit d, but since we have considered

 // 0-indexing, check for odd positions

 if (pos % 2 == 1)

 {

 if (tight == 0 && d > num[pos])

 return 0;

 

 int currTight = tight;

 

 // At this position, number becomes

 // smaller

 if (d < num[pos])

 currTight = 1;

 

 int res = count(pos + 1, (10 * rem + d) % m,

 currTight, num);

 return dp[pos, rem, tight] = res;

 }

 

 int ans = 0;

 

 // Maximum limit upto which we can place

 // digit. If tight is 1, means number has

 // already become smaller so we can place

 // any digit, otherwise num[pos]

 int limit = (tight != 0) ? 9 : num[pos];

 for (int dig = 0; dig <= limit; dig++) 

 {

 

 if (dig == d)

 continue;

 

 int currTight = tight;

 

 // At this position, number becomes

 // smaller

 if (dig < num[pos])

 currTight = 1;

 

 // Next recursive call, also set nonz

 // to 1 if current digit is non zero

 ans += count(pos + 1, (10 * rem + dig) % m,

 currTight, num);

 }

 return dp[pos, rem, tight] = ans;

 }

 

 // Function to convert x into its digit vector

 // and uses count() function to return the

 // required count

 static int solve(int x)

 {

 List<int> num = new List<int>();

 while (x > 0)

 {

 num.Add(x % 10);

 x /= 10;

 }

 num.Reverse();

 

 // Initialize dp

 for (int i = 0; i < dp.GetLength(0); i++)

 for (int j = 0; j < dp.GetLength(1); j++)

 for (int k = 0; k < dp.GetLength(2); k++)

 dp[i, j, k] = -1;

 

 return count(0, 0, 0, num);

 }

 

 // Driver Code

 public static void Main(String[] args)

 {

 int L = 10, R = 99;

 d = 8;

 m = 2;

 Console.WriteLine(solve(R) - solve(L));

 }

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP Program to find the count of 

// numbers in a range divisible by m 

// having digit d at even positions 

 

// This function returns the count of 

// required numbers from 0 to num 

function count_num($pos, $rem, $tight, $num) 

{ 

 // Last position 

 if ($pos == sizeof($num)) 

 { 

 if ($rem == 0) 

 return 1; 

 return 0; 

 } 

 

 // If this result is already computed 

 // simply return it 

 if ( $GLOBALS['dp'][$pos][$rem][$tight] != -1) 

 return $GLOBALS['dp'][$pos][$rem][$tight]; 

 

 // If the current position is even, place 

 // digit d, but since we have considered 

 // 0-indexing, check for odd positions 

 if ($pos % 2)

 { 

 if ($tight == 0 && 

 $GLOBALS['d'] > $num[$pos]) 

 return 0; 

 

 $currTight = $tight; 

 

 // At this position, number becomes 

 // smaller 

 if ($GLOBALS['d'] < $num[$pos]) 

 $currTight = 1; 

 

 $res = count_num($pos + 1, (10 * $rem + 

 $GLOBALS['d']) % $GLOBALS['m'], 

 $currTight, $num); 

 return $dp[$pos][$rem][$tight] = $res; 

 } 

 

 $ans = 0; 

 

 // Maximum limit upto which we can place 

 // digit. If tight is 1, means number has 

 // already become smaller so we can place 

 // any digit, otherwise num[pos] 

 $limit = ($tight ? 9 : $num[$pos]); 

 

 for ($dig = 0; $dig <= $limit; $dig++)

 { 

 

 if ($dig == $GLOBALS['d']) 

 continue; 

 

 $currTight = $tight; 

 

 // At this position, number becomes 

 // smaller 

 if ($dig < $num[$pos]) 

 $currTight = 1; 

 

 // Next recursive call, also set nonz 

 // to 1 if current digit is non zero 

 $ans += count_num($pos + 1, (10 * $rem + $dig) % 

 $GLOBALS['m'], $currTight, $num); 

 } 

 return $dp[$pos][$rem][$tight] = $ans; 

} 

 

// Function to convert x into its digit 

// vector and uses count() function to 

// return the required count 

function solve($x) 

{ 

 $num = array() ;

 while ($x) 

 { 

 array_push($num, $x % 10); 

 $x = floor($x / 10); 

 } 

 $num = array_reverse($num) ;

 

 // Initialize dp 

 for($i = 0 ; $i < $GLOBALS['M'] ; $i++)

 for($j = 0; $j < $GLOBALS['M']; $j++)

 for($k = 0; $k < 2; $k ++)

 $GLOBALS['dp'][$i][$j][$k] = -1;

 

 return count_num(0, 0, 0, $num); 

} 

 

// Driver Code

$GLOBALS['M'] = 20; 

 

// states - position, rem, tight 

$GLOBALS['dp'] = array(array(array()));

 

$L = 10;

$R = 99; 

 

// d is required digit and number 

// should be divisible by m 

$GLOBALS['d'] = 8 ;

$GLOBALS['m'] = 2; 

 

echo solve($R) - solve($L) ; 

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    8

 **Time Complexity :** O(18 * (m – 1) * 2), if we are dealing with the numbers
upto 1018

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

