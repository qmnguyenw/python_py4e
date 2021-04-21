Program to print half Diamond star pattern



Given an integer **N** , the task is to print half-diamond-star pattern.

> *  
> **  
> ***  
> ****  
> *****  
> ******  
> *****  
> ****  
> ***  
> **  
> *

 **Examples:**

    
    
    **Input:** N = 3
    **Output:**
    *
    **
    ***
    **
    *
    
    **Input:** N = 6
    **Output:**
    *
    **
    ***
    ****
    *****
    ******
    *****
    ****
    ***
    **
    *
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to break the pattern into two halves that is upper
half and lower half. Then print then separately with the help of the loops.
The key observation for printing the upper half and lower half is described as
below:

  *  **Upper half:** The upper half of the pattern contains star **‘*’** in increasing order where ith line contains following number of star:
    
    
    Number of '*' in ith line = ![i](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-aeba42a2346918ec8531199b1d5c206d_l3.png)
    

  * **Lower Half:** The lower half of the pattern contains star **‘*’** in decreasing order where ith line contains following number of star:
    
    
    Number of '*' in ith line = ![N - i](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-16e4d9cb691220dcc99fe0057aeb853f_l3.png)
    

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to print the

// half diamond star pattern

 

#include <iostream>

 

using namespace std;

 

// Function to print the

// half diamond star pattern

void halfDiamondStar(int N)

{

 int i, j;

 

 // Loop to print the upper half

 // diamond pattern

 for (i = 0; i < N; i++) {

 for (j = 0; j < i + 1; j++)

 cout << "*";

 cout << "\n";

 }

 

 // Loop to print the lower half

 // diamond pattern

 for (i = 1; i < N; i++) {

 for (j = i; j < N; j++)

 cout << "*";

 cout << "\n";

 }

}

 

// Driver Code

int main()

{

 int N = 5;

 

 // Function Call

 halfDiamondStar(N);

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

// Java implementation to print the

// half diamond star pattern

import java.util.*;

 

class GFG{

 

// Function to print the

// half diamond star pattern

static void halfDiamondStar(int N)

{

 int i, j;

 

 // Loop to print the upper half

 // diamond pattern

 for (i = 0; i < N; i++)

 {

 for (j = 0; j < i + 1; j++)

 System.out.print("*");

 System.out.print("\n");

 }

 

 // Loop to print the lower half

 // diamond pattern

 for (i = 1; i < N; i++) 

 {

 for (j = i; j < N; j++)

 System.out.print("*");

 System.out.print("\n");

 }

}

 

// Driver Code

public static void main(String[] args)

{

 int N = 5;

 

 // Function Call

 halfDiamondStar(N);

}

}

 

// This code is contributed by Rohit_ranjan  
  
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

# Python3 implementation to print the

# half diamond star pattern 

 

# Function to print the 

# half diamond star pattern 

def halfDiamondStar(N):

 

 # Loop to print the upper half 

 # diamond pattern 

 for i in range(N):

 

 for j in range(0, i + 1):

 print("*", end = "")

 print()

 

 # Loop to print the lower half 

 # diamond pattern 

 for i in range(1, N):

 

 for j in range(i, N):

 print("*", end = "")

 print()

 

# Driver Code 

N = 5; 

 

# Function Call 

halfDiamondStar(N);

 

# This code is contributed by skylags  
  
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

// C# implementation to print the

// half diamond star pattern

using System;

 

class GFG{

 

// Function to print the

// half diamond star pattern

static void halfDiamondStar(int N)

{

 int i, j;

 

 // Loop to print the upper half

 // diamond pattern

 for(i = 0; i < N; i++)

 {

 for(j = 0; j < i + 1; j++)

 Console.Write("*");

 Console.Write("\n");

 }

 

 // Loop to print the lower half

 // diamond pattern

 for(i = 1; i < N; i++) 

 {

 for(j = i; j < N; j++)

 Console.Write("*");

 Console.Write("\n");

 }

}

 

// Driver Code

public static void Main(String[] args)

{

 int N = 5;

 

 // Function Call

 halfDiamondStar(N);

}

}

 

// This code is contributed by Rohit_ranjan  
  
---  
  
 __

 __

 **Output:**

    
    
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    

Want to learn from the best curated videos and practice problems, check out
the **C++ Foundation Course **for Basic to Advanced C++ and **C++ STL Course**
for foundation plus STL. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

