Square Difference of Two large Consecutive Numbers



Given two positive consecutive numbers M and N, the task is to find the square
difference of the two numbers without computing the square of those numbers.  
 **Examples:**  

> **Input:** N = 4, M = 5  
> **Output:** 9  
> **Explanation:**  
> 52 – 42 = 25 – 16 = 9.  
>  **Input:** N = 999999999, M = 1000000000  
> **Output:** 1999999999  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to use the algebraic expression to solve this
problem. It is given in the question that M = N + 1. Therefore:  

  * The value to be computed is M2 – N2.
  * On replacing M with N + 1, the above equation becomes:   

    
    
    (N + 1)2 - N2

  * (N + 1)2 can be expanded to:   

    
    
    N2 + 12 + 2 * N - N2

  * On simplifying, the above equation becomes:

    
    
    1 + 2 * N
    1 + N + N
    (1 + N) + N
    M + N

  * Therefore, we simply need to compute and return the value of M + N.

Below is the implementation of the above approach:  

## CPP

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the square

// difference of two large

// consecutive numbers

#include <bits/stdc++.h>

using namespace std;

typedef long long l;

// Function to find the square

// difference of two large

// consecutive numbers

l difference(l M, l N)

{

 return M + N;

}

// Driver code

int main()

{

 l M = 999999999;

 l N = 1000000000;

 cout << difference(M, N) << endl;

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

// Java program to find the square

// difference of two large

// consecutive numbers

class GFG{

 

// Function to find the square

// difference of two large

// consecutive numbers

static long difference(long M, long N)

{

 return M + N;

}

 

// Driver code

public static void main(String[] args)

{

 long M = 999999999;

 long N = 1000000000;

 

 System.out.print(difference(M, N) +"\n");

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

# Python3 program to find the square

# difference of two large

# consecutive numbers

# Function to find the square

# difference of two large

# consecutive numbers

def difference(M, N):

 return M + N

# Driver code

if __name__ == '__main__':

 M = 999999999

 N = 1000000000

 print(difference(M, N))

# This code is contributed by mohit kumar 29   
  
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

// C# program to find the square

// difference of two large

// consecutive numbers

using System;

public class GFG{

 

// Function to find the square

// difference of two large

// consecutive numbers

static long difference(long M, long N)

{

 return M + N;

}

 

// Driver code

public static void Main(String[] args)

{

 long M = 999999999;

 long N = 1000000000;

 

 Console.Write(difference(M, N) +"\n");

}

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// JavaScript program to find the square

// difference of two large

// consecutive numbers

// Function to find the square

// difference of two large

// consecutive numbers

function difference(M, N)

{

 return M + N;

}

// Driver code

let M = 999999999;

let N = 1000000000;

document.write(difference(M, N));

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    1999999999

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

