Minimum window size containing atleast P primes in every window of given range



Given three integers **X** , **Y** and **P** , the task is to find the minimum
window size **K** such that every window in the range [X, Y] of this size have
atleast **P** prime numbers.

 **Examples:**

>  **Input:** X = 2, Y = 8, P = 2  
>  **Output:** 4  
>  **Explanation:**  
>  In the range [2, 8], window size of 4 contains atleast 2 primes in each
> window.  
> Possible Windows –  
> {2, 3, 4, 5} – No of Primes = 3  
> {3, 4, 5, 6} – No of Primes = 2  
> {4, 5, 6, 7} – No of Primes = 2  
> {5, 6, 7, 8} – No of Primes = 2
>
>  **Input:** X = 12, Y = 42, P = 3  
>  **Output:** 14  
>  **Explanation:**  
>  In the range [12, 42], window size of 14 contains atleast 3 primes in each
> window.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** Traverse over all the possible window sizes, for each
window size traverse in range [X, Y] and check that each window contains
atleast K primes. Minimum of these window size will be the desired value.

  

  

 **Efficient Approach:** The key observation in this problem is if a window
size W is the minimum window size satisfying the condition, then all window
size in the range [W, Y – X + 1] will satisfy the condition. Using this we can
reduce our search space at each step by half which is precisely the idea of
Binary Search. Below is the illustration of the steps:

  *  **Search Space:** The search space for this problem can be the minimum length of the window size that is 1 and the maximum window size can be the difference between the ending value of the range and the starting value of the range.
    
    
    low = 1
    high = Y - X + 1
    

  * **Next Search Space:** In each step generally the idea is to check that for the given window size the primes in each window possible have **P** primes or not with the help of the sliding window technique. Whereas the search space for the problem can be reduced on the basis of below decision:
    *  **Case 1:** When the number of primes in each window contains at least **P** primes, then the size of the window can be reduced to find the window size of less than the current window.
        
        
        if (checkPPrimes(mid) == True)
            high = mid - 1
        

    * **Case 2:** When the number of primes in each window contains do not have then the window size must be greater than the current window size. Then,
        
        
        if (checkPPrimes(mid) == False)
            low = mid + 1
        

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

// minimum window size in the range

// such that each window of that size

// contains atleast P primes

 

#include <bits/stdc++.h>

 

using namespace std;

 

// Function to check that a number is 

// a prime or not in O(sqrt(N))

bool isPrime(int N)

{

 if (N < 2)

 return false;

 if (N < 4)

 return true;

 if ((N & 1) == 0)

 return false;

 if (N % 3 == 0)

 return false;

 int curr = 5, s = sqrt(N);

 

 // Loop to check if any number

 // number is divisible by any 

 // other number or not

 while (curr <= s) {

 if (N % curr == 0)

 return false;

 curr += 2;

 if (N % curr == 0)

 return false;

 curr += 4;

 }

 return true;

}

 

// Function to check whether window

// size satisfies condition or not

bool check(int s, int p, 

 int prefix_sum[], int n)

{

 bool satisfies = true;

 

 // Loop to check each window of 

 // size have atleast P primes

 for (int i = 0; i < n; i++) {

 if (i + s - 1 >= n)

 break;

 

 // Checking condition 

 // using prefix sum

 if (prefix_sum[i + s - 1] - 

 (i - 1 >= 0 ? 

 prefix_sum[i - 1] : 0) < p)

 satisfies = false;

 }

 return satisfies;

}

 

// Function to find the minimum 

// window size possible for the

// given range in X and Y

int minimumWindowSize(int x, int y,

 int p)

{

 // Prefix array

 int prefix_sum[y - x + 1] = { 0 };

 

 // Mark those numbers 

 // which are primes as 1

 for (int i = x; i <= y; i++) {

 if (isPrime(i))

 prefix_sum[i - x] = 1;

 }

 

 // Convert to prefix sum

 for (int i = 1; i < y - x + 1; i++)

 prefix_sum[i] += 

 prefix_sum[i - 1];

 

 // Applying binary search 

 // over window size

 int low = 1, high = y - x + 1;

 int mid;

 while (high - low > 1) {

 mid = (low + high) / 2;

 

 // Check whether mid satisfies 

 // the condition or not

 if (check(mid, p, 

 prefix_sum, y - x + 1)) {

 

 // If satisfies search

 // in first half

 high = mid;

 }

 

 // Else search in second half

 else

 low = mid;

 }

 if (check(low, p, 

 prefix_sum, y - x + 1))

 return low;

 return high;

}

 

// Driver Code

int main()

{

 int x = 12;

 int y = 42;

 int p = 3;

 

 cout << minimumWindowSize(x, y, p);

 

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

// minimum window size in the range

// such that each window of that size

// contains atleast P primes

import java.util.*;

 

class GFG{

 

// Function to check that a number is 

// a prime or not in O(Math.sqrt(N))

static boolean isPrime(int N)

{

 if (N < 2)

 return false;

 if (N < 4)

 return true;

 if ((N & 1) == 0)

 return false;

 if (N % 3 == 0)

 return false;

 int curr = 5, s = (int) Math.sqrt(N);

 

 // Loop to check if any number

 // number is divisible by any 

 // other number or not

 while (curr <= s) {

 if (N % curr == 0)

 return false;

 curr += 2;

 if (N % curr == 0)

 return false;

 curr += 4;

 }

 return true;

}

 

// Function to check whether window

// size satisfies condition or not

static boolean check(int s, int p, 

 int prefix_sum[], int n)

{

 boolean satisfies = true;

 

 // Loop to check each window of 

 // size have atleast P primes

 for (int i = 0; i < n; i++) {

 if (i + s - 1 >= n)

 break;

 

 // Checking condition 

 // using prefix sum

 if (prefix_sum[i + s - 1] - 

 (i - 1 >= 0 ? 

 prefix_sum[i - 1] : 0) < p)

 satisfies = false;

 }

 return satisfies;

}

 

// Function to find the minimum 

// window size possible for the

// given range in X and Y

static int minimumWindowSize(int x, int y,

 int p)

{

 // Prefix array

 int []prefix_sum = new int[y - x + 1];

 

 // Mark those numbers 

 // which are primes as 1

 for (int i = x; i <= y; i++) {

 if (isPrime(i))

 prefix_sum[i - x] = 1;

 }

 

 // Convert to prefix sum

 for (int i = 1; i < y - x + 1; i++)

 prefix_sum[i] += 

 prefix_sum[i - 1];

 

 // Applying binary search 

 // over window size

 int low = 1, high = y - x + 1;

 int mid;

 while (high - low > 1) {

 mid = (low + high) / 2;

 

 // Check whether mid satisfies 

 // the condition or not

 if (check(mid, p, 

 prefix_sum, y - x + 1)) {

 

 // If satisfies search

 // in first half

 high = mid;

 }

 

 // Else search in second half

 else

 low = mid;

 }

 if (check(low, p, 

 prefix_sum, y - x + 1))

 return low;

 return high;

}

 

// Driver Code

public static void main(String[] args)

{

 int x = 12;

 int y = 42;

 int p = 3;

 

 System.out.print(minimumWindowSize(x, y, p));

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

# Python3 implementation to find the

# minimum window size in the range

# such that each window of that size

# contains atleast P primes

 

from math import sqrt

 

# Function to check that a number is 

# a prime or not in O(sqrt(N))

def isPrime(N):

 if (N < 2):

 return False

 if (N < 4):

 return True

 if ((N & 1) == 0):

 return False

 if (N % 3 == 0):

 return False

 

 curr = 5

 s = sqrt(N)

 

 # Loop to check if any number

 # number is divisible by any 

 # other number or not

 while (curr <= s):

 if (N % curr == 0):

 return False

 curr += 2

 if (N % curr == 0):

 return False

 

 curr += 4

 

 return True

 

# Function to check whether window

# size satisfies condition or not

def check(s, p, prefix_sum, n):

 

 satisfies = True

 # Loop to check each window of 

 # size have atleast P primes

 for i in range(n):

 if (i + s - 1 >= n):

 break

 # Checking condition 

 # using prefix sum

 if (i - 1 >= 0):

 x = prefix_sum[i - 1]

 else:

 x = 0

 if (prefix_sum[i + s - 1] - x < p):

 satisfies = False

 

 return satisfies

 

# Function to find the minimum 

# window size possible for the

# given range in X and Y

def minimumWindowSize(x, y, p):

 

 # Prefix array

 prefix_sum = [0]*(y - x + 1)

 

 # Mark those numbers 

 # which are primes as 1 

 for i in range(x ,y+1):

 if (isPrime(i)):

 prefix_sum[i - x] = 1

 

 # Convert to prefix sum

 for i in range(1 ,y - x + 1):

 prefix_sum[i] += prefix_sum[i - 1]

 

 # Applying binary search 

 # over window size

 low = 1

 high = y - x + 1

 

 while (high - low > 1):

 mid = (low + high) // 2

 

 # Check whether mid satisfies 

 # the condition or not

 if (check(mid, p ,prefix_sum, y - x + 1)):

 

 # If satisfies search

 # in first half

 high = mid

 

 # Else search in second half

 else:

 low = mid

 if (check(low, p, prefix_sum, y - x + 1)):

 return low

 return high

 

# Driver Code

x = 12

y = 42

p = 3

 

print(minimumWindowSize(x, y, p))

 

# This code is contributed by shubhamsingh10  
  
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

// minimum window size in the range

// such that each window of that size

// contains atleast P primes

using System;

 

class GFG{

 

// Function to check that a number is 

// a prime or not in O(Math.Sqrt(N))

static bool isPrime(int N)

{

 if (N < 2)

 return false;

 if (N < 4)

 return true;

 if ((N & 1) == 0)

 return false;

 if (N % 3 == 0)

 return false;

 int curr = 5, s = (int) Math.Sqrt(N);

 

 // Loop to check if any number

 // number is divisible by any 

 // other number or not

 while (curr <= s) {

 if (N % curr == 0)

 return false;

 curr += 2;

 if (N % curr == 0)

 return false;

 curr += 4;

 }

 return true;

}

 

// Function to check whether window

// size satisfies condition or not

static bool check(int s, int p, 

 int []prefix_sum, int n)

{

 bool satisfies = true;

 

 // Loop to check each window of 

 // size have atleast P primes

 for (int i = 0; i < n; i++) {

 if (i + s - 1 >= n)

 break;

 

 // Checking condition 

 // using prefix sum

 if (prefix_sum[i + s - 1] - 

 (i - 1 >= 0 ? 

 prefix_sum[i - 1] : 0) < p)

 satisfies = false;

 }

 return satisfies;

}

 

// Function to find the minimum 

// window size possible for the

// given range in X and Y

static int minimumWindowSize(int x, int y,

 int p)

{

 // Prefix array

 int []prefix_sum = new int[y - x + 1];

 

 // Mark those numbers 

 // which are primes as 1

 for (int i = x; i <= y; i++) {

 if (isPrime(i))

 prefix_sum[i - x] = 1;

 }

 

 // Convert to prefix sum

 for (int i = 1; i < y - x + 1; i++)

 prefix_sum[i] += 

 prefix_sum[i - 1];

 

 // Applying binary search 

 // over window size

 int low = 1, high = y - x + 1;

 int mid;

 while (high - low > 1) {

 mid = (low + high) / 2;

 

 // Check whether mid satisfies 

 // the condition or not

 if (check(mid, p, 

 prefix_sum, y - x + 1)) {

 

 // If satisfies search

 // in first half

 high = mid;

 }

 

 // Else search in second half

 else

 low = mid;

 }

 if (check(low, p, 

 prefix_sum, y - x + 1))

 return low;

 return high;

}

 

// Driver Code

public static void Main(String[] args)

{

 int x = 12;

 int y = 42;

 int p = 3;

 

 Console.Write(minimumWindowSize(x, y, p));

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    14
    

**Time complexity:** O(N*log(N))  
 **Auxiliary Space:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

