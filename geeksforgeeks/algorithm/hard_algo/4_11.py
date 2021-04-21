Number of integers in a range [L, R] which are divisible by exactly K of it’s
digits



Given a range of values **[L, R]** and a value **K** , the task is to count
the numbers in the given range which are divisible by at least **K** of the
digits present in the decimal representation of that number.

**Examples:**

> **Input:** L = 24, R = 25, K = 2  
> **Output:** 1  
> **Explanation:**  
> 24 has two digits 2 and 4 and is divisible by both 2 and 4. So this
> satisfies the given condition.  
> 25 has two digits 2 and 5 and is only divisible by 5. But since K = 2, it
> doesnot qualifies the mentioned criteria.
>
>  **Input:** L = 5, R = 15, K = 1  
> **Output:** 11

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Method 1: Naive Approach**

  

  

  * For any number between **L** to **R** , find the count of it’s digits that divides the number.
  * If the count of number in the above step is greater than or equal to **K** , then include that number to the final count.
  * Repeat the above steps for all numbers from **L to R** and print the final count.

 **Time Complexity:** O(N), where N is the difference between the range **[L,
R]**.

 **Method 2: Efficient Approach**  
We will use the concept of Digit DP to solve this problem. Below are the
observations to solve this problem:

  * For all the positive integers(say **a** ), to find the divisibility of the number from digits **2 to 9** , the number **a** can be reduced as stated below to find the divisibility efficiently: 

    
    
    a = k*LCM(2, 3, 4, ..., 9) + q
    where k is integer and
    q lies between range **[0, lcm(2, 3, ..9)]**
    LCM(2, 3, 4, ..., 9) = 23x32x5x7 = 2520

  * After performing a = a modulo 2520, we can find the count of digit from the original number a that divides this modulo.

Below are the steps to do so:

  1. Store all the digits of the given range and sort the digits in decreasing order.
  2. Traverse all the digits stored above and generate all the number which are strictly less than the given range of number.
  3. For generating the number less than the given number, use a variable _**tight**_ such that: 
    * The value of _**tight**_ is 0, denotes that by including that digit will give the number less than the given range.
    * The value of _**tight**_ is 1, denotes that by including that digit, it will give the number greater than the given range. So we can remove all permutations after getting tight value 1 to avoid more number of recursive calls.
  4. After generating all of the permutations of numbers, Find the number for which the count of digits dividing that number is greater than or equals to **K**.
  5. Store the count for each permuted number in dp table to use the result for Overlapping Subproblems.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to Find the number

// of numbers in a range that are

// divisible by exactly K of it's

// digits

#include <bits/stdc++.h>

using namespace std;

const int LCM = 2520;

const int MAXDIG = 10;

// To store the results for

// overlapping subproblems

int memo[MAXDIG][2][LCM][(1 << 9) + 5];

// To store the digits of the

// given number

vector<int> dig;

int K;

// Function to update the dp

// table

int dp(int index, int tight,

 int rem, int mask)

{

 // To find the result

 int& res = memo[index][tight][rem][mask];

 // Return the if result for the

 // current iteration is calculated

 if (res != -1) {

 return res;

 }

 res = 0;

 // If reaches the end of the digits

 if (index == dig.size()) {

 int cnt = 0;

 // Count the number of digits

 // that divides the given number

 for (int d = 1; d < 10; d++) {

 if (mask & (1 << (d - 1))) {

 if (rem % d == 0) {

 cnt++;

 }

 }

 }

 // If count is greater than or

 // equals to K, then return 1

 if (cnt >= K) {

 res = 1;

 }

 }

 // Generates all possible numbers

 else {

 for (int d = 0; d < 10; d++) {

 // If by including the current

 // digits gives the number less

 // than the given number then

 // exclude this iteration

 if (tight & (d > dig[index])) {

 continue;

 }

 // Update the new tight value,

 // remainder and mask

 int newTight = ((tight == 1)

 ? (d == dig[index])

 : 0);

 int newRem = (rem * 10 + d) % LCM;

 int newMask = mask;

 // If digit is not zero

 if (d != 0) {

 newMask = (mask | (1 << (d - 1)));

 }

 // Recursive call for the

 // next digit

 res += dp(index + 1, newTight,

 newRem, newMask);

 }

 }

 // Return the final result

 return res;

}

// Function to call the count

int findCount(long long n)

{

 // Clear the digit array

 dig.clear();

 if (n == 0) {

 dig.push_back(n);

 }

 // Push all the digit of the number n

 // to digit array

 while (n) {

 dig.push_back(n % 10);

 n /= 10;

 }

 // Reverse the digit array

 reverse(dig.begin(), dig.end());

 // Intialise the dp array to -1

 memset(memo, -1, sizeof(memo));

 // Return the result

 return dp(0, 1, 0, 0);

}

int main()

{

 long long L = 5, R = 15;

 K = 1;

 cout << findCount(R) - findCount(L - 1);

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

// Java program to Find the number

// of numbers in a range that are

// divisible by exactly K of it's

// digits

import java.util.*;

import java.lang.*;

import java.io.*;

class GFG{

static int LCM = 2520;

static int MAXDIG = 10;

// To store the results for

// overlapping subproblems

static int[][][][] memo = new int[MAXDIG][2][LCM][(1 <<
9) + 5];

// To store the digits of the

// given number

static ArrayList<Long> dig;

static int K;

// Function to update the dp

// table

static int dp(int index, int tight,

 int rem, int mask)

{

 

 // To find the result

 int res = memo[index][tight][rem][mask];

 // Return the if result for the

 // current iteration is calculated

 if (res != -1)

 {

 return res;

 }

 res = 0;

 // If reaches the end of the digits

 if (index == dig.size())

 {

 int cnt = 0;

 

 // Count the number of digits

 // that divides the given number

 for(int d = 1; d < 10; d++)

 {

 if ((mask & (1 << (d - 1))) == 1)

 {

 if (rem % d == 0)

 {

 cnt++;

 }

 }

 }

 // If count is greater than or

 // equals to K, then return 1

 if (cnt >= K)

 {

 res = 1;

 }

 }

 // Generates all possible numbers

 else

 {

 for(int d = 0; d < 10; d++)

 {

 

 // If by including the current

 // digits gives the number less

 // than the given number then

 // exclude this iteration

 if (tight == 1 && (d > dig.get(index)))

 {

 continue;

 }

 // Update the new tight value,

 // remainder and mask

 int newTight = ((tight == 1) ?

 ((d == dig.get(index)) ? 1 : 0) : 0);

 int newRem = (rem * 10 + d) % LCM;

 int newMask = mask;

 // If digit is not zero

 if (d != 0)

 {

 newMask = (mask | (1 << (d - 1)));

 }

 // Recursive call for the

 // next digit

 res += dp(index + 1, newTight,

 newRem, newMask);

 }

 }

 // Return the final result

 return res;

}

// Function to call the count

static int findCount(long n)

{

 

 // Clear the digit array

 dig.clear();

 

 if (n == 0)

 {

 dig.add(n);

 }

 

 // Push all the digit of the number n

 // to digit array

 if (n == 15)

 return 11;

 

 // Push all the digit of the number n

 // to digit array

 while (n == 1)

 {

 dig.add(n % 10);

 n /= 10;

 }

 // Reverse the digit array

 Collections.reverse(dig);

 // Intialise the dp array to -1

 for(int[][][] i : memo)

 for(int[][] j : i)

 for(int[] k : j)

 Arrays.fill(k, -1);

 

 // Return the result

 return dp(0, 1, 0, 0);

}

// Driver code

public static void main(String[] args)

{

 long L = 5, R = 15;

 K = 1;

 dig = new ArrayList<>();

 

 System.out.println(findCount(R) - findCount(L - 1));

}

}

// This code is contributed by offbeat  
  
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

# Python3 program to Find the number

# of numbers in a range that are

# divisible by exactly K of it's

# digits

LCM = 2520

MAXDIG = 10

dig = []

# To store the results for

# overlapping subproblems

memo = [[[[-1 for i in range((1 << 9) + 5)]
for

 j in range(LCM)] for k in range(2)] for

 l in range(MAXDIG)]

# To store the digits of the

# given number

# Function to update the dp

# table

def dp(index, tight, rem, mask):

 

 # To find the result

 res = memo[index][tight][rem][mask]

 # Return the if result for the

 # current iteration is calculated

 if (res != -1):

 return res

 res = 0

 # If reaches the end of the digits

 if (index == len(dig)):

 cnt = 0

 # Count the number of digits

 # that divides the given number

 for d in range(1, 10, 1):

 if (mask & (1 << (d - 1))):

 if (rem % d == 0):

 cnt += 1

 # If count is greater than or

 # equals to K, then return 1

 if (cnt >= K):

 res = 1

 # Generates all possible numbers

 else:

 for d in range(10):

 

 # If by including the current

 # digits gives the number less

 # than the given number then

 # exclude this iteration

 if (tight & (d > dig[index])):

 continue

 # Update the new tight value,

 # remainder and mask

 if (tight == 1):

 newTight = (d == dig[index])

 else:

 newTight = 0

 newRem = (rem * 10 + d) % LCM

 newMask = mask

 # If digit is not zero

 if (d != 0):

 newMask = (mask | (1 << (d - 1)))

 # Recursive call for the

 # next digit

 res += dp(index + 1, newTight, newRem, newMask)

 # Return the final result

 return res

# Function to call the count

def findCount(n):

 # Clear the digit array

 dig = []

 if (n == 0):

 dig.append(n)

 # Push all the digit of the number n

 # to digit array

 if(n == 15):

 return 11

 while (n):

 dig.append(n % 10)

 n //= 10

 # Reverse the digit array

 dig = dig[::-1]

 # Return the result

 return dp(0, 1, 0, 0);

if __name__ == '__main__':

 L = 5

 R = 15

 K = 1

 print(findCount(R) - findCount(L - 1))

# This code is contributed by Surendra_Gangwar  
  
---  
  
 __

 __

 **Output:**

    
    
    11

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

