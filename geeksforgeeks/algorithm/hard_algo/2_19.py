Split a binary string into K subsets minimizing sum of products of occurrences
of 0 and 1



Given a binary string **S** , the task is to partition the sequence into **K**
non-empty subsets such that the sum of products of occurences of **0** and
**1** for all subsets is minimum. If impossible print -1.

 **Examples:**

>  **Input:** S = “0001”, K = 2  
>  **Output:** 0  
>  **Explaination**  
>  We have 3 choices {0, 001}, {00, 01}, {000, 1}  
> The respective sum of products are {1*0 + 2*1 = 2}, {2*0 + 1*1 = 1}, {3*0 +
> 0*1 = 0}.
>
>  **Input:** S = “1011000110110100”, K = 5  
>  **Output:** 8  
>  **Explanation:** The subsets {10, 11, 000, 11011, 0100} minimizes the sum
> of product { 1*1 + 0*2 + 3*0 + 1*4 + 3*1 = 8 }.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** In order to solve this problem we are using bottom-up dynamic
programming.

  

  

  * We calculate the minimum sum of products for all subsets and then, for every subset we use this value to compute the minimum sum of products for all sizes of that subset.
  * For a subset starting at index **i** and ending at index **j** the value will be minimum of **dp[i-1] + (count_zero * count_one)** where **count_zero** and **count_one** are the occurences of **0** and **1** between **i** and **j** respectively.
  * For each index **j** , we find the minimum value amongst all possible values of **i**.
  * Return **dp[N – 1]** for the final answer.

Below code is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to split a given string

// into K segments such that the sum

// of product of occurence of

// characters in them is minimized

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the minimum

// sum of products of occurences

// of 0 and 1 in each segments

int minSumProd(string S, int K)

{

 // Store the length of

 // the string

 int len = S.length();

 

 // Not possible to

 // generate subsets

 // greater than the

 // length of string

 if (K > len)

 return -1;

 

 // If the number of subsets

 // equals the length

 if (K == len)

 return 0;

 

 vector<int> dp(len);

 int count_zero = 0, count_one = 0;

 

 // Precompute the sum of

 // products for all index

 for (int j = 0; j < len; j++) {

 

 (S[j] == '0')

 ? count_zero++

 : count_one++;

 dp[j] = count_zero * count_one;

 }

 

 // Calculate the minimum sum of

 // products for K subsets

 for (int i = 1; i < K; i++) {

 

 for (int j = len; j >= i; j--) {

 

 count_zero = 0, count_one = 0;

 dp[j] = INT_MAX;

 

 for (int k = j; k >= i; k--) {

 

 (S[k] == '0') ? count_zero++

 : count_one++;

 dp[j]

 = min(

 dp[j],

 count_zero * count_one

 + dp[k - 1]);

 }

 }

 }

 

 return dp[len - 1];

}

 

// Driver code

int main()

{

 string S = "1011000110110100";

 int K = 5;

 cout << minSumProd(S, K) << '\n';

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

// Java Program to split a given String

// into K segments such that the sum

// of product of occurence of

// characters in them is minimized

import java.util.*;

 

class GFG{

 

// Function to return the minimum

// sum of products of occurences

// of 0 and 1 in each segments

static int minSumProd(String S, int K)

{

 // Store the length of

 // the String

 int len = S.length();

 

 // Not possible to

 // generate subsets

 // greater than the

 // length of String

 if (K > len)

 return -1;

 

 // If the number of subsets

 // equals the length

 if (K == len)

 return 0;

 

 int []dp = new int[len];

 int count_zero = 0, count_one = 0;

 

 // Precompute the sum of

 // products for all index

 for (int j = 0; j < len; j++) 

 {

 if(S.charAt(j) == '0')

 count_zero++;

 else

 count_one++;

 dp[j] = count_zero * count_one;

 }

 

 // Calculate the minimum sum of

 // products for K subsets

 for (int i = 1; i < K; i++) 

 {

 for (int j = len-1; j >= i; j--) 

 {

 count_zero = 0;

 count_one = 0;

 dp[j] = Integer.MAX_VALUE;

 

 for (int k = j; k >= i; k--)

 {

 if(S.charAt(k) == '0')

 count_zero++;

 else

 count_one++;

 dp[j] = Math.min(dp[j], count_zero * 

 count_one + 

 dp[k - 1]);

 }

 }

 }

 

 return dp[len - 1];

}

 

// Driver code

public static void main(String[] args)

{

 String S = "1011000110110100";

 int K = 5;

 System.out.print(minSumProd(S, K));

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

# Python3 program to split a given String

# into K segments such that the sum

# of product of occurence of

# characters in them is minimized

import sys

 

# Function to return the minimum

# sum of products of occurences

# of 0 and 1 in each segments

def minSumProd(S, K):

 

 # Store the length of

 # the String

 Len = len(S);

 

 # Not possible to

 # generate subsets

 # greater than the

 # length of String

 if (K > Len):

 return -1;

 

 # If the number of subsets

 # equals the length

 if (K == Len):

 return 0;

 

 dp = [0] * Len;

 count_zero = 0;

 count_one = 0;

 

 # Precompute the sum of

 # products for all index

 for j in range(0, Len, 1):

 if (S[j] == '0'):

 count_zero += 1;

 else:

 count_one += 1;

 dp[j] = count_zero * count_one;

 

 # Calculate the minimum sum of

 # products for K subsets

 for i in range(1, K):

 for j in range(Len - 1, i - 1, -1):

 count_zero = 0;

 count_one = 0;

 dp[j] = sys.maxsize;

 

 for k in range(j, i - 1, -1):

 if (S[k] == '0'):

 count_zero += 1;

 else:

 count_one += 1;

 

 dp[j] = min(dp[j], count_zero *

 count_one +

 dp[k - 1]);

 return dp[Len - 1];

 

# Driver code

if __name__ == '__main__':

 

 S = "1011000110110100";

 K = 5;

 

 print(minSumProd(S, K));

 

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

// C# program to split a given String

// into K segments such that the sum

// of product of occurence of

// characters in them is minimized

using System;

 

class GFG{

 

// Function to return the minimum

// sum of products of occurences

// of 0 and 1 in each segments

static int minSumProd(string S, int K)

{

 

 // Store the length of

 // the String

 int len = S.Length;

 

 // Not possible to

 // generate subsets

 // greater than the

 // length of String

 if (K > len)

 return -1;

 

 // If the number of subsets

 // equals the length

 if (K == len)

 return 0;

 

 int []dp = new int[len];

 int count_zero = 0, count_one = 0;

 

 // Precompute the sum of

 // products for all index

 for(int j = 0; j < len; j++) 

 {

 if(S[j] == '0')

 {

 count_zero++;

 }

 else

 {

 count_one++;

 }

 dp[j] = count_zero * count_one;

 }

 

 // Calculate the minimum sum 

 // of products for K subsets

 for(int i = 1; i < K; i++) 

 {

 for(int j = len - 1; j >= i; j--) 

 {

 count_zero = 0;

 count_one = 0;

 dp[j] = Int32.MaxValue;

 

 for(int k = j; k >= i; k--)

 {

 if(S[k] == '0')

 {

 count_zero++;

 }

 else

 {

 count_one++;

 }

 dp[j] = Math.Min(dp[j], count_zero * 

 count_one + 

 dp[k - 1]);

 }

 }

 }

 return dp[len - 1];

}

 

// Driver code

public static void Main(string[] args)

{

 string S = "1011000110110100";

 int K = 5;

 

 Console.Write(minSumProd(S, K));

}

}

 

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    8
    

**Time Complexity:** _O(K*N*N)_  
 **Auxiliary Space Complexity:** _O(N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

