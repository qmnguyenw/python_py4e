Sum of N-terms of geometric progression for larger values of N | Set 2 (Using
recursion)



  
A Geometric series is a series with a constant ratio between successive terms.
The first term of the series is denoted by **a** and the common ratio is
denoted by **r**. The series looks like this:- ![ a, ar, ar^2, ar^3, ar^4,...
.](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-3e4c316384917cad18f6d404b9773528_l3.png)  
The task is to find the sum of such a series mod **M**.

 **Examples:**

    
    
    **Input:** a = 1, r = 2, N = 10000, M = 10000
    **Output:** 8751
    
    **Input:** a = 1, r = 4, N = 10000, M = 100000
    **Output:** 12501
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  1. To find the sum of series ![ a + ar + ar^2 + ar^3 + . . . . + ar^N ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-352767599f4ef1bc439a384c08715dfb_l3.png) we can easily take a as common and find the sum of ![ 1 + r + r^2 + r^3 + . . . . + r^N ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-3295de7b96bd105b2ab825448083ff52_l3.png) and multiply it with a.
  2. Steps to find the sum of above series.
    * Here, it can be resolved that:  
![ \[1 + r + r^2 + r^3 + . . . + r^\(2*n+1\)\] = \(1+r\)*\(1 + \(r^2\) +
\(r^2\)^2 + \(r^2\)^3 + . . . + \(r^2\)^n\)
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-4f655056b6e51f2614d07de6a0213a25_l3.png).

    * > If we denote,  
> ![ Sum\(r, n\) = 1 + r + r^2 + r^3 + . . . . +
> r^N.](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-82648249a8afdebc5043012fd4e68f13_l3.png) then,  
> ![ Sum\(r, 2 * n + 1\) = \(1 + r\) * Sum\(r^2,
> n\).](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-8179cd8e8945ab7d1e16a8b184bed05a_l3.png) and,  
> ![ Sum\(r, 2 * n\) = 1 + \(r * \(1 + r\) * Sum\(r^2, n -
> 1\)\).](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-d21db9efa874f611abf13b95620c3f5c_l3.png)
>
>  
>
>
>  
>
>
> This will work as our recursive case.

    * So, the Base cases are:
        
        
                     Sum(r, 0) = 1.
                     Sum(r, 1) = 1 + r.
        

Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to

// illustrate the program 

#include <iostream>

using namespace std;

 

// Function to calculate the sum 

// recursively 

int SumGPUtil(long long int r,

 long long int n, 

 long long int m)

{ 

 

 // Base cases 

 if (n == 0)

 return 1;

 if (n == 1)

 return (1 + r) % m;

 

 long long int ans;

 // If n is odd 

 if (n % 2 == 1)

 { 

 ans = (1 + r) * 

 SumGPUtil((r * r) % m,

 (n - 1) / 2, m);

 }

 else

 {

 

 // If n is even 

 ans = 1 + (r * (1 + r) * 

 SumGPUtil((r * r) % m, 

 (n / 2) - 1, m));

 }

 return (ans % m);

}

 

// Function to print the value of Sum 

void SumGP(long long int a,

 long long int r,

 long long int N,

 long long int M)

{

 long long int answer;

 

 answer = a * SumGPUtil(r, N, M);

 answer = answer % M; 

 

 cout << answer << endl; 

}

 

// Driver Code 

int main()

{

 

 // First element

 long long int a = 1;

 

 // Common diffrence 

 long long int r = 4; 

 

 // Number of elements 

 long long int N = 10000; 

 

 // Mod value 

 long long int M = 100000; 

 

 SumGP(a, r, N, M);

 

 return 0;

}

 

// This code is contributed by sanjoy_62  
  
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

// Java implementation to

// illustrate the program 

import java.io.*;

 

class GFG{

 

// Function to calculate the sum 

// recursively 

static long SumGPUtil(long r, long n,

 long m)

{ 

 

 // Base cases 

 if (n == 0)

 return 1;

 if (n == 1)

 return (1 + r) % m;

 

 long ans;

 

 // If n is odd 

 if (n % 2 == 1)

 { 

 ans = (1 + r) * 

 SumGPUtil((r * r) % m, 

 (n - 1) / 2, m);

 }

 else

 {

 // If n is even 

 ans = 1 + (r * (1 + r) * 

 SumGPUtil((r * r) % m, 

 (n / 2) - 1, m));

 }

 

 return (ans % m);

}

 

// Function to prlong the value of Sum 

static void SumGP(long a, long r,

 long N, long M) 

{

 long answer;

 answer = a * SumGPUtil(r, N, M);

 answer = answer % M; 

 

 System.out.println(answer); 

}

 

// Driver Code 

public static void main (String[] args)

{

 

 // First element 

 long a = 1; 

 

 // Common diffrence 

 long r = 4;

 

 // Number of elements 

 long N = 10000;

 

 // Mod value 

 long M = 100000; 

 

 SumGP(a, r, N, M);

}

}

 

// This code is contributed by sanjoy_62  
  
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

# Python3 implementation to illustrate the program

 

# Function to calculate the sum 

# recursively

def SumGPUtil (r, n, m):

 

 # Base cases

 if n == 0: return 1

 if n == 1: return (1 + r) % m

 

 # If n is odd

 if n % 2 == 1:

 ans = (1 + r) * SumGPUtil(r * r % m,

 (n - 1)//2,

 m)

 else:

 #If n is even

 ans = 1 + r * (1 + r) * SumGPUtil(r * r %
m,

 n//2 - 1,

 m)

 

 return ans % m

 

# Function to print the value of Sum

def SumGP (a, r, N, M):

 

 answer = a * SumGPUtil(r, N, M)

 answer = answer % M

 print(answer)

 

#Driver Program

if __name__== '__main__':

 

 a = 1 # first element

 r = 4 # common diffrence

 N = 10000 # Number of elements

 M = 100000 # Mod value 

 

 SumGP(a, r, N, M)  
  
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

// C# implementation to

// illustrate the program 

using System;

 

class GFG{

 

// Function to calculate the sum 

// recursively 

static long SumGPUtil(long r, long n,

 long m)

{ 

 

 // Base cases 

 if (n == 0)

 return 1;

 if (n == 1)

 return (1 + r) % m;

 

 long ans;

 

 // If n is odd 

 if (n % 2 == 1)

 { 

 ans = (1 + r) * 

 SumGPUtil((r * r) % m, 

 (n - 1) / 2, m);

 }

 else

 {

 

 // If n is even 

 ans = 1 + (r * (1 + r) * 

 SumGPUtil((r * r) % m, 

 (n / 2) - 1, m));

 }

 return (ans % m);

}

 

// Function to prlong the value of Sum 

static void SumGP(long a, long r,

 long N, long M)

{

 long answer;

 answer = a * SumGPUtil(r, N, M);

 answer = answer % M; 

 

 Console.WriteLine(answer); 

}

 

// Driver Code 

public static void Main() 

{

 

 // First element 

 long a = 1; 

 

 // Common diffrence 

 long r = 4; 

 

 // Number of elements 

 long N = 10000;

 

 // Mod value 

 long M = 100000; 

 

 SumGP(a, r, N, M);

}

}

 

// This code is contributed by sanjoy_62  
  
---  
  
 __

 __

 **Output:**

    
    
    12501
    

**Time complexity:** O(log N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

