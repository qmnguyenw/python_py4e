Number of ways to color N-K blocks using given operation



Given **N** blocks out of which **K** are colored. These K colored blocks are
denoted by an array **arr[]**. The task is to count the number of ways to
color the remaining uncolored blocks such that only any one of the adjacent
blocks, of a colored block, can be colored in one step. Print the answer with
modulo 109+7.  
 **Examples:**  

> **Input:** N = 6, K = 3, arr[] = {1, 2, 6}  
> **Output:** 4  
> **Explanation:**  
> Following are the 4 ways to color the blocks(each set reblockquotesents the
> order in which blocks are colored):  
> 1\. {3, 4, 5}  
> 2\. {3, 5, 4}  
> 3\. {5, 3, 4}  
> 4\. {5, 4, 3}  
>  **Input:** N = 9, K = 3, A = [3, 6, 7]  
> **Output:** 180  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The idea is to use recursion. Below are the steps:  

  1. Traverse each block from 1 to N.
  2. If the current block(say **b** ) is not colored then check whether one of the adjacent blocks is colored or not.
  3. If the adjacent block is colored then color the current block and recursively iterate to find the next uncolored block.
  4. After the above recursive call end then, uncolored the block for the blockquotevious recursive call and repeat the above steps for next uncolored block.
  5. The count of coloring the blocks in all the above recursive call gives the number of ways to color the uncolored block.

Below is the implementation of the above approach:  

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h>

using namespace std;

const int mod = 1000000007;

// Recursive function to count the ways

int countWays(int colored[], int count,

 int n)

{

 // Base case

 if (count == n) {

 return 1;

 }

 // Intialise answer to 0

 int answer = 0;

 // Color each uncolored block according

 // to the given condition

 for (int i = 1; i < n + 1; i++) {

 // If any block is uncolored

 if (colored[i] == 0) {

 // Check if adjacent blocks

 // are colored or not

 if (colored[i - 1] == 1

 || colored[i + 1] == 1) {

 // Color the block

 colored[i] = 1;

 // recursively iterate for

 // next uncolored block

 answer = (answer

 + countWays(colored,

 count + 1,

 n))

 % mod;

 // Uncolored for the next

 // recursive call

 colored[i] = 0;

 }

 }

 }

 // Return the final count

 return answer;

}

// Function to count the ways to color

// block

int waysToColor(int arr[], int n, int k)

{

 // Mark which blocks are colored in

 // each recursive step

 int colored[n + 2] = { 0 };

 for (int i = 0; i < k; i++) {

 colored[arr[i]] = 1;

 }

 // Function call to count the ways

 return countWays(colored, k, n);

}

// Driver Code

int main()

{

 // Number of blocks

 int N = 6;

 // Number of colored blocks

 int K = 3;

 int arr[K] = { 1, 2, 6 };

 // Function call

 cout << waysToColor(arr, N, K);

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

// Java program for the above approach

import java.util.*;

class GFG{

static int mod = 1000000007;

// Recursive function to count the ways

static int countWays(int colored[],

 int count, int n)

{

 // Base case

 if (count == n)

 {

 return 1;

 }

 // Intialise answer to 0

 int answer = 0;

 // Color each uncolored block according

 // to the given condition

 for (int i = 1; i < n + 1; i++)

 {

 // If any block is uncolored

 if (colored[i] == 0)

 {

 // Check if adjacent blocks

 // are colored or not

 if (colored[i - 1] == 1 ||

 colored[i + 1] == 1)

 {

 // Color the block

 colored[i] = 1;

 // recursively iterate for

 // next uncolored block

 answer = (answer +

 countWays(colored,

 count + 1,

 n)) % mod;

 // Uncolored for the next

 // recursive call

 colored[i] = 0;

 }

 }

 }

 // Return the final count

 return answer;

}

// Function to count the ways to color

// block

static int waysToColor(int arr[],

 int n, int k)

{

 // Mark which blocks are colored in

 // each recursive step

 int colored[] = new int[n + 2];

 for (int i = 0; i < k; i++)

 {

 colored[arr[i]] = 1;

 }

 // Function call to count the ways

 return countWays(colored, k, n);

}

// Driver Code

public static void main(String[] args)

{

 // Number of blocks

 int N = 6;

 // Number of colored blocks

 int K = 3;

 int arr[] = { 1, 2, 6 };

 // Function call

 System.out.print(waysToColor(arr, N, K));

}

}

// This code is contributed by sapnasingh4991  
  
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

# Python3 program for the above approach

mod = 1000000007

# Recursive function to count the ways

def countWays(colored, count, n):

 # Base case

 if (count == n):

 return 1

 # Intialise answer to 0

 answer = 0

 # Color each uncolored block according

 # to the given condition

 for i in range(1, n + 1):

 # If any block is uncolored

 if (colored[i] == 0):

 # Check if adjacent blocks

 # are colored or not

 if (colored[i - 1] == 1 or

 colored[i + 1] == 1):

 # Color the block

 colored[i] = 1

 # recursively iterate for

 # next uncolored block

 answer = ((answer +

 countWays(colored,

 count + 1,

 n)) % mod)

 # Uncolored for the next

 # recursive call

 colored[i] = 0

 # Return the final count

 return answer

# Function to count the ways to color

# block

def waysToColor( arr, n, k):

 # Mark which blocks are colored in

 # each recursive step

 colored = [0] * (n + 2)

 

 for i in range(k):

 colored[arr[i]] = 1

 # Function call to count the ways

 return countWays(colored, k, n)

# Driver Code

if __name__ == "__main__":

 

 # Number of blocks

 N = 6

 # Number of colored blocks

 K = 3

 arr = [ 1, 2, 6 ]

 # Function call

 print(waysToColor(arr, N, K))

# This code is contributed by chitranayal  
  
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

// C# program for the above approach

using System;

class GFG{

static int mod = 1000000007;

// Recursive function to count the ways

static int countWays(int []colored,

 int count, int n)

{

 // Base case

 if (count == n)

 {

 return 1;

 }

 // Intialise answer to 0

 int answer = 0;

 // Color each uncolored block according

 // to the given condition

 for (int i = 1; i < n + 1; i++)

 {

 // If any block is uncolored

 if (colored[i] == 0)

 {

 // Check if adjacent blocks

 // are colored or not

 if (colored[i - 1] == 1 ||

 colored[i + 1] == 1)

 {

 // Color the block

 colored[i] = 1;

 // recursively iterate for

 // next uncolored block

 answer = (answer +

 countWays(colored,

 count + 1,

 n)) % mod;

 // Uncolored for the next

 // recursive call

 colored[i] = 0;

 }

 }

 }

 // Return the final count

 return answer;

}

// Function to count the ways to color

// block

static int waysToColor(int []arr,

 int n, int k)

{

 // Mark which blocks are colored in

 // each recursive step

 int []colored = new int[n + 2];

 for (int i = 0; i < k; i++)

 {

 colored[arr[i]] = 1;

 }

 // Function call to count the ways

 return countWays(colored, k, n);

}

// Driver Code

public static void Main()

{

 // Number of blocks

 int N = 6;

 // Number of colored blocks

 int K = 3;

 int []arr = { 1, 2, 6 };

 // Function call

 Console.Write(waysToColor(arr, N, K));

}

}

// This code is contributed by Code_Mech  
  
---  
  
 __

 __

 **Output:**

    
    
    4

_**Time Complexity:** O(NN-K) _  
**Efficient Approach:** For solving this problem efficiently we will use the
concept of Permutation and Combination. Below are the steps:  

  1. If the number of blocks between two consecutive colored blocks is x, then the number of ways to color these set of blocks is given by:   

> ways = 2x-1  
>

  1.   2. Coloring each set of uncolored blocks is independent of the other. Suppose there are **x blocks** in one section and **y block** in the other section. To find the total combinations when the two sections are merged is given by:   

> total combinations = ![{n \\choose x}*2^{x-1}*2^{y-1}
> ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
> ed919e79f64fbee23537b8f59188acc0_l3.png)  
>

  1.   2. Sort the colored block indices to find length of each uncolored block section and iterate and find the combination each two section using the above formula.
  3. Find Binomial Coefficient using the approach discussed in this article.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h>

using namespace std;

const int mod = 1000000007;

// Function to count the ways to color

// block

int waysToColor(int arr[], int n, int k)

{

 // For storing powers of 2

 int powOf2[500] = { 0 };

 // For storing binomial coefficient

 // values

 int c[500][500];

 // Calculating binomial coefficient

 // using DP

 for (int i = 0; i <= n; i++) {

 c[i][0] = 1;

 for (int j = 1; j <= i; j++) {

 c[i][j] = (c[i - 1][j]

 + c[i - 1][j - 1])

 % mod;

 }

 }

 powOf2[0] = powOf2[1] = 1;

 // Calculating powers of 2

 for (int i = 2; i <= n; i++) {

 powOf2[i] = powOf2[i - 1] * 2 % mod;

 }

 int rem = n - k;

 arr[k++] = n + 1;

 // Sort the indices to calculate

 // length of each section

 sort(arr, arr + k);

 // Initialise answer to 1

 int answer = 1;

 for (int i = 0; i < k; i++) {

 // Find the length of each section

 int x = arr[i] - (i - 1 >= 0

 ? arr[i - 1]

 : 0)

 - 1;

 // Merge this section

 answer *= c[rem][x] % mod * (i != 0

 && i != k - 1

 ? powOf2[x]

 : 1)

 % mod;

 rem -= x;

 }

 // Return the final count

 return answer;

}

// Driver Code

int main()

{

 // Number of blocks

 int N = 6;

 // Number of colored blocks

 int K = 3;

 int arr[K] = { 1, 2, 6 };

 // Function call

 cout << waysToColor(arr, N, K);

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

// Java program for the above approach

import java.util.*;

class GFG{

static int mod = 1000000007;

// Function to count the ways to color

// block

static int waysToColor(int arr[], int n, int k)

{

 

 // For storing powers of 2

 int powOf2[] = new int[500];

 // For storing binomial coefficient

 // values

 int [][]c = new int[500][500];

 // Calculating binomial coefficient

 // using DP

 for(int i = 0; i <= n; i++)

 {

 c[i][0] = 1;

 for(int j = 1; j <= i; j++)

 {

 c[i][j] = (c[i - 1][j] +

 c[i - 1][j - 1]) % mod;

 }

 }

 powOf2[0] = powOf2[1] = 1;

 // Calculating powers of 2

 for(int i = 2; i <= n; i++)

 {

 powOf2[i] = powOf2[i - 1] * 2 % mod;

 }

 int rem = n - k;

 arr[k++] = n + 1;

 

 // Sort the indices to calculate

 // length of each section

 Arrays.sort(arr);

 // Initialise answer to 1

 int answer = 1;

 for(int i = 0; i < k; i++)

 {

 

 // Find the length of each section

 int x = arr[i] - (i - 1 >= 0 ?

 arr[i - 1] : 0) - 1;

 

 // Merge this section

 answer *= c[rem][x] % mod * (i != 0 &&

 i != k - 1 ?

 powOf2[x] : 1) %

 mod;

 rem -= x;

 }

 

 // Return the final count

 return answer;

}

// Driver Code

public static void main(String[] args)

{

 

 // Number of blocks

 int N = 6;

 // Number of colored blocks

 int K = 3;

 int arr[] = { 1, 2, 6 ,0 };

 // Function call

 System.out.print(waysToColor(arr, N, K));

}

}

// This code is contributed by 29AjayKumar  
  
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

# Python3 program for the above approach

mod = 1000000007

 

# Function to count the ways to color

# block

def waysToColor(arr, n, k):

 

 global mod

 # For storing powers of 2

 powOf2 = [0 for i in range(500)]

 

 # For storing binomial coefficient

 # values

 c = [[0 for i in range(500)] for j in
range(500)]

 

 # Calculating binomial coefficient

 # using DP

 for i in range(n + 1):

 

 c[i][0] = 1;

 

 for j in range(1, i + 1):

 

 c[i][j] = (c[i - 1][j]+ c[i - 1][j - 1])%
mod;

 

 powOf2[0] = 1

 powOf2[1] = 1;

 

 # Calculating powers of 2

 for i in range(2, n + 1):

 

 powOf2[i] = (powOf2[i - 1] * 2) % mod;

 

 rem = n - k;

 arr[k] = n + 1;

 k += 1

 

 # Sort the indices to calculate

 # length of each section

 arr.sort()

 

 # Initialise answer to 1

 answer = 1;

 

 for i in range(k):

 

 x = 0

 

 # Find the length of each section

 if i - 1 >= 0:

 x = arr[i] - arr[i - 1] -1

 else:

 x = arr[i] - 1

 

 # Merge this section

 answer = answer * (c[rem][x] % mod) * ((powOf2[x] if
(i != 0 and i != k - 1) else 1))% mod

 rem -= x;

 

 # Return the final count

 return answer;

# Driver Code

if __name__=='__main__':

 

 # Number of blocks

 N = 6;

 

 # Number of colored blocks

 K = 3;

 arr = [ 1, 2, 6, 0]

 

 # Function call

 print(waysToColor(arr, N, K))

# This code is contributed by rutvik_56  
  
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

// C# program for the above approach

using System;

class GFG{

static int mod = 1000000007;

// Function to count the ways to color

// block

static int waysToColor(int []arr, int n, int k)

{

 

 // For storing powers of 2

 int []powOf2 = new int[500];

 // For storing binomial coefficient

 // values

 int [,]c = new int[500, 500];

 // Calculating binomial coefficient

 // using DP

 for(int i = 0; i <= n; i++)

 {

 c[i, 0] = 1;

 for(int j = 1; j <= i; j++)

 {

 c[i, j] = (c[i - 1, j] +

 c[i - 1, j - 1]) % mod;

 }

 }

 powOf2[0] = powOf2[1] = 1;

 // Calculating powers of 2

 for(int i = 2; i <= n; i++)

 {

 powOf2[i] = powOf2[i - 1] * 2 % mod;

 }

 int rem = n - k;

 arr[k++] = n + 1;

 

 // Sort the indices to calculate

 // length of each section

 Array.Sort(arr);

 // Initialise answer to 1

 int answer = 1;

 for(int i = 0; i < k; i++)

 {

 

 // Find the length of each section

 int x = arr[i] - (i - 1 >= 0 ?

 arr[i - 1] : 0) - 1;

 

 // Merge this section

 answer *= c[rem, x] % mod * (i != 0 &&

 i != k - 1 ?

 powOf2[x] : 1) %

 mod;

 rem -= x;

 }

 

 // Return the readonly count

 return answer;

}

// Driver Code

public static void Main(String[] args)

{

 

 // Number of blocks

 int N = 6;

 // Number of colored blocks

 int K = 3;

 int []arr = { 1, 2, 6, 0 };

 // Function call

 Console.Write(waysToColor(arr, N, K));

}

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    4

_**Time Complexity:** O(N2) _  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

