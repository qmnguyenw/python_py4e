Number of pairs of arrays (A, B) such that A is ascending, B is descending and
A[i] ≤ B[i]



Given two integers **N** and **M** , the task is to find the number of pairs
of arrays **(A, B)** such that array **A** and **B** both are of size **M**
each where each entry of **A** and **B** is an integer between **1** and **N**
such that for each **i** between **1** and **M** , **A[i] ≤ B[i]**. It is also
given that the array **A** is sorted in **non-descending** order and **B** is
sorted in **non-ascending** order. Since the answer can be very large, return
answer modulo **10 9 \+ 7**.

 **Examples:**

>  **Input:** N = 2, M = 2  
>  **Output:** 5  
> 1: A= [1, 1] B=[1, 1]  
> 2: A= [1, 1] B=[1, 2]  
> 3: A= [1, 1] B=[2, 2]  
> 4: A= [1, 2] B=[2, 2]  
> 5: A= [2, 2] B=[2, 2]
>
>  **Input:** N = 5, M = 3  
>  **Output:** 210

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Notice that if there is a valid pair of arrays A and B and if B
is concatenated after A the resultant array will always be either an ascending
or a non-descending array of size of 2 * M. Each element of (A + B) will be
between 1 and N (It is not necessary that all elements between 1 and N have to
be used). This now simply converts the given problem to finding all the
possible combinations of size **2 * M** where each element is between 1 to N
(with repetitions allowed) whose formula is **2 * M + N – 1 CN – 1** or (2 * M
+ N – 1)! / ((2 * M)! * (N – 1)!).

  

  

Below is the implementation of the above approach:  

## CPP

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code of above approach

#include <bits/stdc++.h>

#define mod 1000000007

using namespace std;

 

long long fact(long long n)

{

 if(n == 1) 

 return 1;

 else

 return (fact(n - 1) * n) % mod;

}

 

// Function to return the count of pairs

long long countPairs(int m, int n)

{

 long long ans = fact(2 * m + n - 1) / 

 (fact(n - 1) * fact(2 * m));

 return (ans % mod);

}

 

// Driver code

int main()

{

 int n = 5, m = 3;

 cout << (countPairs(m, n));

 return 0;

}

 

// This code is contributed by mohit kumar 29  
  
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

// Java code of above approach

class GFG 

{

 final static long mod = 1000000007 ;

 

 static long fact(long n) 

 { 

 if(n == 1) 

 return 1; 

 else

 return (fact(n - 1) * n) % mod; 

 } 

 

 // Function to return the count of pairs 

 static long countPairs(int m, int n) 

 { 

 long ans = fact(2 * m + n - 1) / 

 (fact(n - 1) * fact(2 * m)); 

 

 return (ans % mod); 

 } 

 

 // Driver code 

 public static void main (String[] args)

 { 

 int n = 5, m = 3; 

 

 System.out.println(countPairs(m, n)); 

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

from math import factorial as fact

 

# Function to return the count of pairs

def countPairs(m, n):

 ans = fact(2 * m +
n-1)//(fact(n-1)*fact(2 * m))

 return (ans %(10**9 + 7))

 

# Driver code

n, m = 5, 3

print(countPairs(m, n))  
  
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

// C# code of above approach

using System;

 

class GFG 

{

 static long mod = 1000000007 ;

 

 static long fact(long n) 

 { 

 if(n == 1) 

 return 1; 

 else

 return (fact(n - 1) * n) % mod; 

 } 

 

 // Function to return the count of pairs 

 static long countPairs(int m, int n) 

 { 

 long ans = fact(2 * m + n - 1) / 

 (fact(n - 1) * fact(2 * m)); 

 

 return (ans % mod); 

 } 

 

 // Driver code 

 public static void Main()

 { 

 int n = 5, m = 3; 

 

 Console.WriteLine(countPairs(m, n)); 

 } 

}

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

    
    
    210
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

