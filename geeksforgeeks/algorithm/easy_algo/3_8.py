Longest sub-sequence of a binary string divisible by 3



Given a binary string **S** of length **N** , the task is to find the length
of the longest sub-sequence in it which is divisible by **3**. Leading zeros
in the sub-sequences are allowed.

 **Examples:**

>  **Input:** S = “1001”  
>  **Output:** 4  
> The longest sub-sequence divisible by 3 is “1001”.  
> 1001 = 9 which is divisible by 3.
>
>  **Input:** S = “1011”  
>  **Output:** 3

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Generate all the possible sub-sequences and check if they
are divisible by **3**. The time complexity for this will be **O((2 N) * N)**.

  

  

 **Efficient approach:** Dynamic programming can be used to solve this
problem. Let’s look at the states of DP.  
 **DP[i][r]** will store the longest sub-sequence of the substring
**S[i…N-1]** such that it gives a remainder of **(3 – r) % 3** when divided by
**3**.  
Let’s write the recurrence relation now.

> DP[i][r] = max(1 + DP[i + 1][(r * 2 + s[i]) % 3], DP[i + 1][r])

The recurrence is derived because of the following two choices:

  1. Include the current index **i** in the sub-sequence. Thus, the **r** will be updated as **r = (r * 2 + s[i]) % 3**.
  2. Don’t include the current index in the sub-sequence.

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

#define N 100

 

int dp[N][3];

bool v[N][3];

 

// Function to return the length of the

// largest sub-string divisible by 3

int findLargestString(string& s, int i, int r)

{

 // Base-case

 if (i == s.size()) {

 if (r == 0)

 return 0;

 else

 return INT_MIN;

 }

 

 // If the state has been solved

 // before then return its value

 if (v[i][r])

 return dp[i][r];

 

 // Marking the state as solved

 v[i][r] = 1;

 

 // Recurrence relation

 dp[i][r]

 = max(1 + findLargestString(s, i + 1,

 (r * 2 + (s[i] - '0')) % 3),

 findLargestString(s, i + 1, r));

 return dp[i][r];

}

 

// Driver code

int main()

{

 string s = "101";

 

 cout << findLargestString(s, 0, 0);

 

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

// Java implementation of th approach

class GFG 

{

 

 final static int N = 100 ;

 final static int INT_MIN = Integer.MIN_VALUE;

 

 static int dp[][] = new int[N][3]; 

 static int v[][] = new int[N][3]; 

 

 

 // Function to return the length of the 

 // largest sub-string divisible by 3 

 static int findLargestString(String s, int i, int r) 

 { 

 // Base-case 

 if (i == s.length())

 { 

 if (r == 0) 

 return 0; 

 else

 return INT_MIN; 

 } 

 

 // If the state has been solved 

 // before then return its value 

 if (v[i][r] == 1) 

 return dp[i][r]; 

 

 // Marking the state as solved 

 v[i][r] = 1; 

 

 // Recurrence relation 

 dp[i][r] = Math.max(1 + findLargestString(s, i + 1, 

 (r * 2 + (s.charAt(i) - '0')) % 3), 

 findLargestString(s, i + 1, r)); 

 return dp[i][r];

 }

 

 // Driver code 

 public static void main (String[] args) 

 { 

 String s = "101"; 

 

 System.out.print(findLargestString(s, 0, 0)); 

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

import numpy as np

import sys

 

N = 100

INT_MIN = -(sys.maxsize - 1)

 

dp = np.zeros((N, 3)); 

v = np.zeros((N, 3)); 

 

# Function to return the length of the 

# largest sub-string divisible by 3 

def findLargestString(s, i, r) : 

 

 # Base-case 

 if (i == len(s)) :

 if (r == 0) :

 return 0; 

 else :

 return INT_MIN; 

 

 # If the state has been solved 

 # before then return its value 

 if (v[i][r]) :

 return dp[i][r]; 

 

 # Marking the state as solved 

 v[i][r] = 1; 

 

 # Recurrence relation 

 dp[i][r] = max(1 + findLargestString(s, i + 1, 

 (r * 2 + (ord(s[i]) - ord('0'))) % 3),

 findLargestString(s, i + 1, r)); 

 

 return dp[i][r]; 

 

# Driver code 

if __name__ == "__main__" : 

 

 s = "101"; 

 

 print(findLargestString(s, 0, 0)); 

 

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

// C# implementation of th approach

using System;

using System.Collections.Generic;

 

class GFG 

{

 

 readonly static int N = 100 ;

 readonly static int INT_MIN = int.MinValue;

 

 static int [,]dp = new int[N, 3]; 

 static int [,]v = new int[N, 3]; 

 

 // Function to return the length of the 

 // largest sub-string divisible by 3 

 static int findLargestString(String s, int i, int r) 

 { 

 // Base-case 

 if (i == s.Length)

 { 

 if (r == 0) 

 return 0; 

 else

 return INT_MIN; 

 } 

 

 // If the state has been solved 

 // before then return its value 

 if (v[i, r] == 1) 

 return dp[i, r]; 

 

 // Marking the state as solved 

 v[i, r] = 1; 

 

 // Recurrence relation 

 dp[i, r] = Math.Max(1 + findLargestString(s, i + 1, 

 (r * 2 + (s[i] - '0')) % 3), 

 findLargestString(s, i + 1, r)); 

 return dp[i, r];

 }

 

 // Driver code 

 public static void Main(String[] args) 

 { 

 String s = "101"; 

 

 Console.Write(findLargestString(s, 0, 0)); 

 } 

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

**Time Complexity:** O(n)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

