Count the number of ways to divide N in k groups incrementally



Given two integers **N** and **K** , the task is to count the number of ways
to divide N into K groups of positive integers such that their sum is **N**
and the number of elements in groups follows a non-decreasing order (i.e
group[i] <= group[i+1]).  
 **Examples:**  

> **Input:** N = 8, K = 4  
> **Output:** 5  
> **Explanation:**  
> Their are 5 groups such that their sum is 8 and the number of positive
> integers in each group is 4.  
> [1, 1, 1, 5], [1, 1, 2, 4], [1, 1, 3, 3], [1, 2, 2, 3], [2, 2, 2, 2]  
>  **Input:** N = 24, K = 5  
> **Output:** 164  
> **Explanation:**  
> There are 164 such groups such that their sum is 24 and number of positive
> integers in each group is 5

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** We can solve this problem using recursion. At each step
of recursion put all the values greater than equal to the previously computed
value.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to count the

// number of ways to divide N in

// groups such that each group

// has K number of elements

#include <bits/stdc++.h>

using namespace std;

// Function to count the number

// of ways to divide the number N

// in groups such that each group

// has K number of elements

int calculate(int pos, int prev,

 int left, int k)

{

 // Base Case

 if (pos == k) {

 if (left == 0)

 return 1;

 else

 return 0;

 }

 // if N is divides completely

 // into less than k groups

 if (left == 0)

 return 0;

 int answer = 0;

 

 // put all possible values

 // greater equal to prev

 for (int i = prev; i <= left; i++) {

 answer += calculate(pos + 1, i,

 left - i, k);

 }

 return answer;

}

// Function to count the number of

// ways to divide the number N

int countWaystoDivide(int n, int k)

{

 return calculate(0, 1, n, k);

}

// Driver Code

int main()

{

 int N = 8;

 int K = 4;

 cout << countWaystoDivide(N, K);

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

// Java implementation to count the

// number of ways to divide N in

// groups such that each group

// has K number of elements

import java.util.*;

class GFG{

// Function to count the number

// of ways to divide the number N

// in groups such that each group

// has K number of elements

static int calculate(int pos, int prev,

 int left, int k)

{

 

 // Base Case

 if (pos == k)

 {

 if (left == 0)

 return 1;

 else

 return 0;

 }

 // If N is divides completely

 // into less than k groups

 if (left == 0)

 return 0;

 int answer = 0;

 

 // Put all possible values

 // greater equal to prev

 for(int i = prev; i <= left; i++)

 {

 answer += calculate(pos + 1, i,

 left - i, k);

 }

 return answer;

}

// Function to count the number of

// ways to divide the number N

static int countWaystoDivide(int n, int k)

{

 return calculate(0, 1, n, k);

}

// Driver Code

public static void main(String[] args)

{

 int N = 8;

 int K = 4;

 System.out.print(countWaystoDivide(N, K));

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

# Python3 implementation to count the

# number of ways to divide N in

# groups such that each group

# has K number of elements

# Function to count the number

# of ways to divide the number N

# in groups such that each group

# has K number of elements

def calculate(pos, prev, left, k):

 

 # Base Case

 if (pos == k):

 if (left == 0):

 return 1;

 else:

 return 0;

 # If N is divides completely

 # into less than k groups

 if (left == 0):

 return 0;

 answer = 0;

 # Put all possible values

 # greater equal to prev

 for i in range(prev, left + 1):

 answer += calculate(pos + 1, i,

 left - i, k);

 return answer;

# Function to count the number of

# ways to divide the number N

def countWaystoDivide(n, k):

 

 return calculate(0, 1, n, k);

# Driver Code

if __name__ == '__main__':

 

 N = 8;

 K = 4;

 print(countWaystoDivide(N, K));

# This code is contributed by 29AjayKumar  
  
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

// C# implementation to count the

// number of ways to divide N in

// groups such that each group

// has K number of elements

using System;

class GFG{

// Function to count the number

// of ways to divide the number N

// in groups such that each group

// has K number of elements

static int calculate(int pos, int prev,

 int left, int k)

{

 

 // Base Case

 if (pos == k)

 {

 if (left == 0)

 return 1;

 else

 return 0;

 }

 // If N is divides completely

 // into less than k groups

 if (left == 0)

 return 0;

 int answer = 0;

 

 // Put all possible values

 // greater equal to prev

 for(int i = prev; i <= left; i++)

 {

 answer += calculate(pos + 1, i,

 left - i, k);

 }

 return answer;

}

// Function to count the number of

// ways to divide the number N

static int countWaystoDivide(int n, int k)

{

 return calculate(0, 1, n, k);

}

// Driver Code

public static void Main(String[] args)

{

 int N = 8;

 int K = 4;

 Console.Write(countWaystoDivide(N, K));

}

}

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    
    
    

**Time complexity:** O(NK)  
 **Efficient Approach:** In the previous approach we can see that we are
solving the subproblems repeatedly, i.e. it follows the property of
Overlapping Subproblems. So we can memoize the same using DP table.  
Below is the implementation of the above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to count the

// number of ways to divide N in

// groups such that each group

// has K number of elements

#include <bits/stdc++.h>

using namespace std;

// DP Table

int dp[500][500][500];

// Function to count the number

// of ways to divide the number N

// in groups such that each group

// has K number of elements

int calculate(int pos, int prev,

 int left, int k)

{

 // Base Case

 if (pos == k) {

 if (left == 0)

 return 1;

 else

 return 0;

 }

 // if N is divides completely

 // into less than k groups

 if (left == 0)

 return 0;

 // If the subproblem has been

 // solved, use the value

 if (dp[pos][prev][left] != -1)

 return dp[pos][prev][left];

 int answer = 0;

 // put all possible values

 // greater equal to prev

 for (int i = prev; i <= left; i++) {

 answer += calculate(pos + 1, i,

 left - i, k);

 }

 return dp[pos][prev][left] = answer;

}

// Function to count the number of

// ways to divide the number N in groups

int countWaystoDivide(int n, int k)

{

 // Intialize DP Table as -1

 memset(dp, -1, sizeof(dp));

 return calculate(0, 1, n, k);

}

// Driver Code

int main()

{

 int N = 8;

 int K = 4;

 cout << countWaystoDivide(N, K);

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

// Java implementation to count the

// number of ways to divide N in

// groups such that each group

// has K number of elements

import java.util.*;

class GFG{

 

// DP Table

static int [][][]dp = new int[500][500][500];

 

// Function to count the number

// of ways to divide the number N

// in groups such that each group

// has K number of elements

static int calculate(int pos, int prev,

 int left, int k)

{

 // Base Case

 if (pos == k)

 {

 if (left == 0)

 return 1;

 else

 return 0;

 }

 

 // if N is divides completely

 // into less than k groups

 if (left == 0)

 return 0;

 

 // If the subproblem has been

 // solved, use the value

 if (dp[pos][prev][left] != -1)

 return dp[pos][prev][left];

 

 int answer = 0;

 

 // put all possible values

 // greater equal to prev

 for (int i = prev; i <= left; i++)

 {

 answer += calculate(pos + 1, i,

 left - i, k);

 }

 

 return dp[pos][prev][left] = answer;

}

 

// Function to count the number of

// ways to divide the number N in groups

static int countWaystoDivide(int n, int k)

{

 // Intialize DP Table as -1

 for (int i = 0; i < 500; i++)

 {

 for (int j = 0; j < 500; j++)

 {

 for (int l = 0; l < 500; l++)

 dp[i][j][l] = -1;

 }

 }

 

 return calculate(0, 1, n, k);

}

 

// Driver Code

public static void main(String[] args)

{

 int N = 8;

 int K = 4;

 

 System.out.print(countWaystoDivide(N, K));

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

# Python3 implementation to count the

# number of ways to divide N in

# groups such that each group

# has K number of elements

 

# DP Table

dp = [[[0 for i in range(50)]

 for j in range(50)]

 for j in range(50)]

# Function to count the number

# of ways to divide the number N

# in groups such that each group

# has K number of elements

def calculate(pos, prev, left, k):

 

 # Base Case

 if (pos == k):

 if (left == 0):

 return 1;

 else:

 return 0;

 

 # if N is divides completely

 # into less than k groups

 if (left == 0):

 return 0;

 

 # If the subproblem has been

 # solved, use the value

 if (dp[pos][prev][left] != -1):

 return dp[pos][prev][left];

 

 answer = 0;

 

 # put all possible values

 # greater equal to prev

 for i in range(prev,left+1):

 answer += calculate(pos + 1, i,

 left - i, k);

 dp[pos][prev][left] = answer;

 return dp[pos][prev][left];

 

# Function to count the number of

# ways to divide the number N in groups

def countWaystoDivide(n, k):

 

 # Intialize DP Table as -1

 for i in range(50):

 for j in range(50):

 for l in range(50):

 dp[i][j][l] = -1;

 

 return calculate(0, 1, n, k);

 

# Driver Code

if __name__ == '__main__':

 N = 8;

 K = 4;

 

 print(countWaystoDivide(N, K));

 

# This code is contributed by Rajput-Ji  
  
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

// C# implementation to count the

// number of ways to divide N in

// groups such that each group

// has K number of elements

using System;

class GFG{

 

// DP Table

static int [,,]dp = new int[50, 50, 50];

 

// Function to count the number

// of ways to divide the number N

// in groups such that each group

// has K number of elements

static int calculate(int pos, int prev,

 int left, int k)

{

 // Base Case

 if (pos == k)

 {

 if (left == 0)

 return 1;

 else

 return 0;

 }

 

 // if N is divides completely

 // into less than k groups

 if (left == 0)

 return 0;

 

 // If the subproblem has been

 // solved, use the value

 if (dp[pos, prev, left] != -1)

 return dp[pos, prev, left];

 

 int answer = 0;

 

 // put all possible values

 // greater equal to prev

 for (int i = prev; i <= left; i++)

 {

 answer += calculate(pos + 1, i,

 left - i, k);

 }

 

 return dp[pos, prev, left] = answer;

}

 

// Function to count the number of

// ways to divide the number N in groups

static int countWaystoDivide(int n, int k)

{

 // Intialize DP Table as -1

 for (int i = 0; i < 50; i++)

 {

 for (int j = 0; j < 50; j++)

 {

 for (int l = 0; l < 50; l++)

 dp[i, j, l] = -1;

 }

 }

 

 return calculate(0, 1, n, k);

}

 

// Driver Code

public static void Main(String[] args)

{

 int N = 8;

 int K = 4;

 

 Console.Write(countWaystoDivide(N, K));

}

}

// This code is contributed by gauravrajput1  
  
---  
  
 __

 __

 **Output:**

    
    
    5

 **Time complexity :** O(N2 * K)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

