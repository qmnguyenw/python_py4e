Count numbers less than N containing digits from the given set : Digit DP



Given an integer **N** and set of digits **D[]** , which consists of digits
from [1, 9]. The task is to count the numbers possible less than **N** , whose
digits are from the given set of digits.

 **Examples:**

>  **Input:** D = [“1”, “4”, “9”], N = 10  
>  **Output:** 3  
>  **Explanation:**  
>  There are only 3 numbers possible less than 3 with given set of digits –  
> 1, 4, 9
>
>  **Input:** D[] = {“1”, “3”, “5”, “7”}, N = 100  
>  **Output:** 20  
>  **Explanation:**  
>  There are only 20 numbers possible less than 100 with given set of digits –  
> 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

 **Naive Approach:** Check the digits of all the numbers of range [1, N], If
all the digits of a number belong to the given digit set then increment the
count by 1.

  

  

 **Efficient Approach:** The idea is to use the concept of Digit DP and
traverse the given set of digits and generate all the numbers which are
strictly less than the given number N. Recursively choose the digit for all
the possible position of the number and pass a boolean variable _**tight**_ to
check that by including that digit, the number falls into the given range or
not.  
Let’s think of the possible state for the DP –

  1.  _ **pos**_ : It tells about the position of the digit to be chosen, such that the number falls into the given range.
  2.  _ **tight**_ : This will help us know about the current digits are restricted or not. If the digits are restricted, then any digit can be choosen from the given set of digits. Otherwise, the digits can be chosen in range [1, N[pos]].
  3.  _ **size**_ : It will tells the number of the digits to be chosen.

Below is the illustration of the recursive function:

  *  **Base Case:** The base case for this problem will be when the position of the digit to be chosen is equal to the length of digits to be chosen, then there is only one possible number containing the digits which are chosen till yet.
    
    
    if (position == countDigits(N))
        return 1
    

  * **Recursive Case:** For generating the number in the given range, use the tight variable to choose the possible digits in range as follows:
    * If the value of _**tight**_ is 0, denotes that by including that digit will give the number less than the given range.
    * Otherwise, If the value of **tight** is 1, denotes that by including that digit, it will give the number greater than the given range. So we can remove all permutations after getting tight value 1 to avoid more number of recursive calls.
  * Store the count of the numbers possible after choosing each digit for every position.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// count of numbers possible less 

// than N, such that every digit

// is from the given set of digits

#include <bits/stdc++.h>

 

using namespace std;

 

int dp[15][2];

 

// Function to convert integer 

// into the string

string convertToString(int num)

{

 stringstream ss;

 ss << num;

 string s = ss.str();

 return s;

}

 

// Recursive function to find the

// count of numbers possible less

// than N, such that every digit

// is from the given set of digits

int calculate(int pos, int tight, 

 int D[], int sz, string& num)

{

 // Base case

 if (pos == num.length())

 return 1;

 

 // Condition when the subproblem

 // is computed previously

 if (dp[pos][tight] != -1)

 return dp[pos][tight];

 

 int val = 0;

 

 // Condition when the number

 // chosen till now is definietly

 // smaller than the given number N

 if (tight == 0) {

 

 // Loop to traverse all the 

 // digits of the given set

 for (int i = 0; i < sz; i++) {

 

 if (D[i] < (num[pos] - '0')) {

 val += calculate(pos + 1, 

 1, D, sz, num);

 }

 else if (D[i] == num[pos] - '0')

 val += calculate(pos + 1, 

 tight, D, sz, num);

 }

 }

 else {

 // Loop to traverse all the 

 // digits from the given set

 for (int i = 0; i < sz; i++) {

 val += calculate(pos + 1, 

 tight, D, sz, num);

 }

 }

 

 // Store the solution for 

 // current subproblem

 return dp[pos][tight] = val;

}

 

// Function to count the numbers

// less then N from given set of digits

int countNumbers(int D[], int N, int sz)

{

 // Converting the number to string

 string num = convertToString(N);

 int len = num.length();

 

 // Intially no subproblem

 // is solved till now

 memset(dp, -1, sizeof(dp));

 

 // Find the solution of all the 

 // number equal to the length of

 // the given number N

 int ans = calculate(0, 0, D, sz, num);

 

 // Loop to find the number less in 

 // in the length of the given number

 for (int i = 1; i < len; i++)

 ans += calculate(i, 1, D, sz, num);

 

 return ans;

}

 

// Driver Code

int main()

{

 int sz = 3;

 

 int D[sz] = { 1, 4, 9 };

 int N = 10;

 

 // Function Call

 cout << countNumbers(D, N, sz);

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

// Java implementation to find the

// count of numbers possible less 

// than N, such that every digit

// is from the given set of digits

import java.util.*;

 

class GFG{

 

static int [][]dp = new int[15][2];

 

// Function to convert integer 

// into the String

static String convertToString(int num)

{

 return String.valueOf(num);

}

 

// Recursive function to find the

// count of numbers possible less

// than N, such that every digit

// is from the given set of digits

static int calculate(int pos, int tight, 

 int D[], int sz, String num)

{

 // Base case

 if (pos == num.length())

 return 1;

 

 // Condition when the subproblem

 // is computed previously

 if (dp[pos][tight] != -1)

 return dp[pos][tight];

 

 int val = 0;

 

 // Condition when the number

 // chosen till now is definietly

 // smaller than the given number N

 if (tight == 0) {

 

 // Loop to traverse all the 

 // digits of the given set

 for (int i = 0; i < sz; i++) {

 

 if (D[i] < (num.charAt(pos) - '0')) {

 val += calculate(pos + 1, 

 1, D, sz, num);

 }

 else if (D[i] == num.charAt(pos) - '0')

 val += calculate(pos + 1, 

 tight, D, sz, num);

 }

 }

 else {

 // Loop to traverse all the 

 // digits from the given set

 for (int i = 0; i < sz; i++) {

 val += calculate(pos + 1, 

 tight, D, sz, num);

 }

 }

 

 // Store the solution for 

 // current subproblem

 return dp[pos][tight] = val;

}

 

// Function to count the numbers

// less then N from given set of digits

static int countNumbers(int D[], int N, int sz)

{

 // Converting the number to String

 String num = convertToString(N);

 int len = num.length();

 

 // Intially no subproblem

 // is solved till now

 for (int i = 0; i < 15; i++)

 for (int j = 0; j < 2; j++)

 dp[i][j] = -1;

 

 // Find the solution of all the 

 // number equal to the length of

 // the given number N

 int ans = calculate(0, 0, D, sz, num);

 

 // Loop to find the number less in 

 // in the length of the given number

 for (int i = 1; i < len; i++)

 ans += calculate(i, 1, D, sz, num);

 

 return ans;

}

 

// Driver Code

public static void main(String[] args)

{

 int sz = 3;

 

 int D[] = { 1, 4, 9 };

 int N = 10;

 

 // Function Call

 System.out.print(countNumbers(D, N, sz));

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

# Python3 implementation to find the

# count of numbers possible less 

# than N, such that every digit 

# is from the given set of digits 

import numpy as np;

dp = np.ones((15,2))*-1; 

 

# Function to convert integer 

# into the string 

def convertToString(num) : 

 return str(num); 

 

# Recursive function to find the 

# count of numbers possible less 

# than N, such that every digit 

# is from the given set of digits 

def calculate(pos,tight, D, sz, num) : 

 

 # Base case 

 if (pos == len(num)): 

 return 1; 

 

 # Condition when the subproblem 

 # is computed previously 

 if (dp[pos][tight] != -1) :

 return dp[pos][tight]; 

 

 val = 0; 

 

 # Condition when the number 

 # chosen till now is definietly 

 # smaller than the given number N 

 if (tight == 0) :

 

 # Loop to traverse all the 

 # digits of the given set 

 for i in range(sz) : 

 

 if (D[i] < (ord(num[pos]) - ord('0'))) :

 val += calculate(pos + 1, 1, D, sz, num); 

 

 elif (D[i] == ord(num[pos]) - ord('0')) :

 val += calculate(pos + 1, tight, D, sz, num); 

 

 else :

 # Loop to traverse all the 

 # digits from the given set 

 for i in range(sz) : 

 val += calculate(pos + 1, tight, D, sz, num);

 

 # Store the solution for

 # current subproblem

 dp[pos][tight] = val;

 

 return dp[pos][tight];

 

# Function to count the numbers 

# less then N from given set of digits 

def countNumbers(D, N, sz) : 

 

 # Converting the number to string 

 num = convertToString(N); 

 length = len(num); 

 

 # Intially no subproblem 

 # is solved till now

 # dp = np.ones((15,2))*-1;

 

 # Find the solution of all the 

 # number equal to the length of 

 # the given number N 

 ans = calculate(0, 0, D, sz, num); 

 

 # Loop to find the number less in 

 # in the length of the given number 

 for i in range(1,length) :

 ans += calculate(i, 1, D, sz, num); 

 

 return ans; 

 

 

# Driver Code 

if __name__ == "__main__" : 

 

 sz = 3; 

 

 D = [ 1, 4, 9 ]; 

 N = 10; 

 

 # Function Call 

 print(countNumbers(D, N, sz)); 

 

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

// C# implementation to find the

// count of numbers possible less 

// than N, such that every digit

// is from the given set of digits

using System;

 

class GFG{

 

static int [,]dp = new int[15, 2];

 

// Function to convert integer 

// into the String

static String convertToString(int num)

{

 return String.Join("",num);

}

 

// Recursive function to find the

// count of numbers possible less

// than N, such that every digit

// is from the given set of digits

static int calculate(int pos, int tight, 

 int []D, int sz, String num)

{

 // Base case

 if (pos == num.Length)

 return 1;

 

 // Condition when the subproblem

 // is computed previously

 if (dp[pos,tight] != -1)

 return dp[pos,tight];

 

 int val = 0;

 

 // Condition when the number

 // chosen till now is definietly

 // smaller than the given number N

 if (tight == 0) {

 

 // Loop to traverse all the 

 // digits of the given set

 for (int i = 0; i < sz; i++) {

 

 if (D[i] < (num[pos] - '0')) {

 val += calculate(pos + 1, 

 1, D, sz, num);

 }

 else if (D[i] == num[pos] - '0')

 val += calculate(pos + 1, 

 tight, D, sz, num);

 }

 }

 else {

 // Loop to traverse all the 

 // digits from the given set

 for (int i = 0; i < sz; i++) {

 val += calculate(pos + 1, 

 tight, D, sz, num);

 }

 }

 

 // Store the solution for 

 // current subproblem

 return dp[pos,tight] = val;

}

 

// Function to count the numbers

// less then N from given set of digits

static int countNumbers(int []D, int N, int sz)

{

 // Converting the number to String

 String num = convertToString(N);

 int len = num.Length;

 

 // Intially no subproblem

 // is solved till now

 for (int i = 0; i < 15; i++)

 for (int j = 0; j < 2; j++)

 dp[i,j] = -1;

 

 // Find the solution of all the 

 // number equal to the length of

 // the given number N

 int ans = calculate(0, 0, D, sz, num);

 

 // Loop to find the number less in 

 // in the length of the given number

 for (int i = 1; i < len; i++)

 ans += calculate(i, 1, D, sz, num);

 

 return ans;

}

 

// Driver Code

public static void Main(String[] args)

{

 int sz = 3;

 

 int []D = { 1, 4, 9 };

 int N = 10;

 

 // Function Call

 Console.Write(countNumbers(D, N, sz));

}

}

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time complexity** : O(Len(D))  
 **Space complexity** : O(12*2)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

