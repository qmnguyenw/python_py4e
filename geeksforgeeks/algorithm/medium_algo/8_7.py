Find the number of binary strings of length N with at least 3 consecutive 1s



Given an integer **N**. The task is to find the number of all possible
distinct binary strings of length **N** which have at least 3 consecutive 1s.

 **Examples:**

>  **Input:** N = 3  
>  **Output:** 1  
> The only string of length 3 possible is “111”.
>
>  **Input:** N = 4  
>  **Output:** 3  
> The 3 strings are “1110”, “0111” and “1111”.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Consider all possible strings.

  

  

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

 

// Function that returns true if s contains

// three consecutive 1's

bool check(string& s)

{

 int n = s.length();

 for (int i = 2; i < n; i++) {

 if (s[i] == '1' && s[i - 1] == '1' && s[i - 2] == '1')

 return 1;

 }

 return 0;

}

 

// Function to return the count

// of required strings

int countStr(int i, string& s)

{

 if (i < 0) {

 if (check(s))

 return 1;

 return 0;

 }

 s[i] = '0';

 int ans = countStr(i - 1, s);

 s[i] = '1';

 ans += countStr(i - 1, s);

 s[i] = '0';

 return ans;

}

 

// Driver code

int main()

{

 int N = 4;

 string s(N, '0');

 cout << countStr(N - 1, s);

 

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

 

// Function that returns true if s contains

// three consecutive 1's

static boolean check(String s)

{

 int n = s.length();

 for (int i = 2; i < n; i++) 

 {

 if (s.charAt(i) == '1' && 

 s.charAt(i-1) == '1' && 

 s.charAt(i-2) == '1')

 return true;

 }

 return false;

}

 

// Function to return the count

// of required strings

static int countStr(int i, String s)

{

 if (i < 0)

 {

 if (check(s))

 return 1;

 return 0;

 }

 char[] myNameChars = s.toCharArray();

 myNameChars[i] = '0';

 s = String.valueOf(myNameChars);

 

 int ans = countStr(i - 1, s);

 char[] myChar = s.toCharArray();

 myChar[i] = '1';

 s = String.valueOf(myChar);

 

 ans += countStr(i - 1, s);

 char[]myChar1 = s.toCharArray();

 myChar1[i] = '0';

 s = String.valueOf(myChar1);

 

 return ans;

}

 

// Driver code

public static void main(String args[])

{

 int N = 4;

 String s = "0000";

 System.out.println(countStr(N - 1, s));

}

}

 

// This code is contributed by

// Surendra_Gangwar  
  
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

 

# Function that returns true if s contains

# three consecutive 1's

def check(s) :

 n = len(s);

 for i in range(2, n) :

 if (s[i] == '1' and s[i - 1] == '1' and

 s[i - 2] == '1') :

 return 1;

 

# Function to return the count

# of required strings

def countStr(i, s) :

 

 if (i < 0) :

 if (check(s)) :

 return 1;

 return 0;

 

 s[i] = '0';

 ans = countStr(i - 1, s);

 

 s[i] = '1';

 ans += countStr(i - 1, s);

 

 s[i] = '0';

 return ans;

 

# Driver code

if __name__ == "__main__" :

 N = 4;

 s = list('0' * N);

 

 print(countStr(N - 1, s));

 

# This code is contributed by Ryuga  
  
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

// value x

using System; 

 

class GFG

{

 

// Function that returns true if s contains

// three consecutive 1's

static bool check(String s)

{

 int n = s.Length;

 for (int i = 2; i < n; i++)

 {

 if (s[i] == '1' && s[i - 1] == '1' && s[i - 2] == '1')

 return true;

 }

 return false;

}

 

// Function to return the count

// of required strings

static int countStr(int i, String s)

{

 if (i < 0)

 {

 if (check(s))

 return 1;

 return 0;

 }

 char[] myNameChars = s.ToCharArray();

 myNameChars[i] = '0';

 s = String.Join("", myNameChars);

 

 int ans = countStr(i - 1, s);

 char[] myChar = s.ToCharArray();

 myChar[i] = '1';

 s = String.Join("", myChar);

 

 ans += countStr(i - 1, s);

 char[]myChar1 = s.ToCharArray();

 myChar1[i] = '0';

 s = String.Join("", myChar1);

 

 return ans;

}

 

// Driver code

public static void Main(String []args)

{

 int N = 4;

 String s = "0000";

 Console.WriteLine(countStr(N - 1, s));

}

}

 

/* This code contributed by PrinciRaj1992 */  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time Complexity:** O(2N)  
 **Space Complexity:** O(N) because of recurrence stack space.

 **Efficient approach:** We use dynamic programming for computing the number
of strings.  
 **State of dp:** dp(i, x) : denotes number of strings of length i with x
consecutive 1s in position i + 1 to i + x.  
 **Recurrence:** dp(i, x) = dp(i – 1, 0) + dp(i – 1, x + 1)  
The recurrence is based on the fact that either the string can have a ‘0’ at
position i or a ‘1’.

  1. If it has a ‘0’ at position i then for (i-1)th position value of x = 0.
  2. If it has a ‘1’ at position i the for (i-1)th position value of x = value of x at position i + 1.

 **Base Condition:** dp(i, 3) = 2i. Because once you have 3 consecutive ‘1’s
you don’t care what characters are there at position 1, 2…i of string as all
the strings are valid.

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

 

int n;

 

// Function to return the count

// of required strings

int solve(int i, int x, int dp[][4])

{

 if (i < 0)

 return x == 3;

 if (dp[i][x] != -1)

 return dp[i][x];

 

 // '0' at ith position

 dp[i][x] = solve(i - 1, 0, dp);

 

 // '1' at ith position

 dp[i][x] += solve(i - 1, x + 1, dp);

 return dp[i][x];

}

 

// Driver code

int main()

{

 n = 4;

 int dp[n][4];

 

 for (int i = 0; i < n; i++)

 for (int j = 0; j < 4; j++)

 dp[i][j] = -1;

 

 for (int i = 0; i < n; i++) {

 

 // Base condition:

 // 2^(i+1) because of 0 indexing

 dp[i][3] = (1 << (i + 1));

 }

 cout << solve(n - 1, 0, dp);

 

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

// Java implementation of the above approach

import java.util.*;

 

class GFG 

{

 

 static int n;

 

 // Function to return the count

 // of required strings

 static int solve(int i, int x, int dp[][]) 

 {

 if (i < 0) 

 {

 return x == 3 ? 1 : 0;

 }

 if (dp[i][x] != -1) 

 {

 return dp[i][x];

 }

 

 // '0' at ith position

 dp[i][x] = solve(i - 1, 0, dp);

 

 // '1' at ith position

 dp[i][x] += solve(i - 1, x + 1, dp);

 return dp[i][x];

 }

 

 // Driver code

 public static void main(String[] args) 

 {

 n = 4;

 int dp[][] = new int[n][4];

 

 for (int i = 0; i < n; i++) 

 {

 for (int j = 0; j < 4; j++) 

 {

 dp[i][j] = -1;

 }

 }

 

 for (int i = 0; i < n; i++) 

 {

 

 // Base condition:

 // 2^(i+1) because of 0 indexing

 dp[i][3] = (1 << (i + 1));

 }

 System.out.print(solve(n - 1, 0, dp));

 }

}

 

// This code has been contributed by 29AjayKumar  
  
---  
  
 __

 __

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 implementation of the approach

 

# Function to return the count

# of required strings

def solve(i, x, dp):

 if (i < 0):

 return x == 3

 if (dp[i][x] != -1):

 return dp[i][x]

 

 # '0' at ith position

 dp[i][x] = solve(i - 1, 0, dp)

 

 # '1' at ith position

 dp[i][x] += solve(i - 1, x + 1, dp)

 return dp[i][x]

 

 

# Driver code

if __name__ == "__main__":

 

 n = 4;

 dp = [[0 for i in range(n)] for j in
range(4)]

 

 for i in range(n):

 for j in range(4):

 dp[i][j] = -1

 

 for i in range(n) :

 

 # Base condition:

 # 2^(i+1) because of 0 indexing

 dp[i][3] = (1 << (i + 1))

 

 print(solve(n - 1, 0, dp))

 

# This code is contributed by ChitraNayal  
  
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

// C# implementation of the above approach

using System; 

 

class GFG 

{

 

 static int n;

 

 // Function to return the count

 // of required strings

 static int solve(int i, int x, int [,]dp) 

 {

 if (i < 0) 

 {

 return x == 3 ? 1 : 0;

 }

 if (dp[i,x] != -1) 

 {

 return dp[i,x];

 }

 

 // '0' at ith position

 dp[i,x] = solve(i - 1, 0, dp);

 

 // '1' at ith position

 dp[i,x] += solve(i - 1, x + 1, dp);

 return dp[i,x];

 }

 

 // Driver code

 public static void Main(String[] args) 

 {

 n = 4;

 int [,]dp = new int[n, 4];

 

 for (int i = 0; i < n; i++) 

 {

 for (int j = 0; j < 4; j++) 

 {

 dp[i, j] = -1;

 }

 }

 

 for (int i = 0; i < n; i++) 

 {

 

 // Base condition:

 // 2^(i+1) because of 0 indexing

 dp[i,3] = (1 << (i + 1));

 }

 Console.Write(solve(n - 1, 0, dp));

 }

}

 

// This code contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time complexity:** O(N)  
 **Space Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

