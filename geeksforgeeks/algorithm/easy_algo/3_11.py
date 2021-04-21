Maximize the expression (A AND X) * (B AND X) | Bit Manipulation



Given two positive integers **A** and **B** such that **A != B** , the task is
to find a positive integer **X** which maximizes the expression **(A AND X) *
(B AND X)**.

 **Example:**

>  **Input:** A = 9 B = 8  
>  **Output:** 8  
> (9 AND 8) * (8 AND 8) = 8 * 8 = 64 (maximum possible)
>
>  **Input:** A = 11 and B = 13  
>  **Output:** 9

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** One can run a loop from **1** to **max(A, B)** and can
easily find **X** which maximizes the given expression.

  

  

 **Efficient approach:** It is known that,

>  **(a – b) 2 ≥ 0**  
> which implies **(a + b) 2 – 4*a*b ≥ 0**  
> which implies **a * b ≤ (a + b) 2 / 4**
>
> Hence, it concludes that **a * b** will be maximum when **a * b = (a + b) 2
> / 4**  
> which implies **a = b**  
>  From the above result, **(A AND X) * (B AND X)** will be maximum when **(A
> AND X) = (B AND X)**

Now X can be found as:

> A = 11 = 1011  
> B = 13 = 1101  
> X = ? = abcd
>
> At 0th place: (1 AND d) = (1 AND d) implies d = 0, 1 but to maximize (A AND
> X) * (B AND X) d = 1  
> At 1st place: (1 AND d) = (0 AND d) implies c = 0  
> At 2nd place: (0 AND d) = (1 AND d) implies b = 0  
> At 3rd place: (1 AND d) = (1 AND d) implies a = 0, 1 but to maximize (A AND
> X) * (B AND X) a = 1
>
> Hence, X = 1001 = 9

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

 

#define MAX 32

 

// Function to find X according

// to the given conditions

int findX(int A, int B)

{

 int X = 0;

 

 // int can have 32 bits

 for (int bit = 0; bit < MAX; bit++) {

 

 // Temporary ith bit

 int tempBit = 1 << bit;

 

 // Compute ith bit of X according to

 // given conditions

 // Expression below is the direct

 // conclusion from the illustration

 // we had taken earlier

 int bitOfX = A & B & tempBit;

 

 // Add the ith bit of X to X

 X += bitOfX;

 }

 

 return X;

}

 

// Driver code

int main()

{

 int A = 11, B = 13;

 

 cout << findX(A, B);

 

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

class GFG

{

static int MAX = 32;

 

// Function to find X according

// to the given conditions

static int findX(int A, int B)

{

 int X = 0;

 

 // int can have 32 bits

 for (int bit = 0; bit < MAX; bit++)

 {

 

 // Temporary ith bit

 int tempBit = 1 << bit;

 

 // Compute ith bit of X according to

 // given conditions

 // Expression below is the direct

 // conclusion from the illustration

 // we had taken earlier

 int bitOfX = A & B & tempBit;

 

 // Add the ith bit of X to X

 X += bitOfX;

 }

 return X;

}

 

// Driver code

public static void main(String []args) 

{

 int A = 11, B = 13;

 

 System.out.println(findX(A, B));

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

# Python3 implementation of the approach

MAX = 32

 

# Function to find X according 

# to the given conditions 

def findX(A, B) :

 

 X = 0; 

 

 # int can have 32 bits 

 for bit in range(MAX) :

 

 # Temporary ith bit 

 tempBit = 1 << bit; 

 

 # Compute ith bit of X according to 

 # given conditions 

 # Expression below is the direct 

 # conclusion from the illustration 

 # we had taken earlier 

 bitOfX = A & B & tempBit; 

 

 # Add the ith bit of X to X 

 X += bitOfX; 

 

 return X; 

 

# Driver code 

if __name__ == "__main__" :

 

 A = 11; B = 13; 

 print(findX(A, B)); 

 

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

// C# implementation of the approach

using System;

 

class GFG

{

static int MAX = 32;

 

// Function to find X according

// to the given conditions

static int findX(int A, int B)

{

 int X = 0;

 

 // int can have 32 bits

 for (int bit = 0; bit < MAX; bit++)

 {

 

 // Temporary ith bit

 int tempBit = 1 << bit;

 

 // Compute ith bit of X according to

 // given conditions

 // Expression below is the direct

 // conclusion from the illustration

 // we had taken earlier

 int bitOfX = A & B & tempBit;

 

 // Add the ith bit of X to X

 X += bitOfX;

 }

 return X;

}

 

// Driver code

public static void Main(String []args) 

{

 int A = 11, B = 13;

 

 Console.WriteLine(findX(A, B));

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    9
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

