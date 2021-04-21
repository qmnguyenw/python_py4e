Largest number made up of X and Y with count of X divisible by Y and of Y by X



Given three integers **X** , **Y** and **N** , the task is to find the largest
number possible of length **N** consisting only of **X** and **Y** as its
digits, such that, the count of **X** ‘s in it is divisible by **Y** and vice-
versa. If no such number can be formed, print **-1**.

 **Examples:**

>  **Input:** N = 3, X = 5, Y = 3  
>  **Output:** 555  
>  **Explanation:**  
>  Count of 5’s = 3, which is divisible by 3  
> Count of 3’s = 0
>
>  **Input:** N = 4, X = 7, Y = 5  
>  **Output:** -1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
Follow the steps below to solve the problem:

  

  

  * Consider the larger of **X** and **Y** as **X** and smaller as **Y**.
  * Since, the number needs to of length **N** , perform the following two steps until N ≤ 0:
    * If N is divisible by Y, append X, N times to the answer and reduce N to zero.
    * Otherwise, reduce N by X and append Y, X times to the answer.
  * After completion of the above step, if N <0, then a number of required type is not possible. Print **-1**.
  * Otherwise, print the answer.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to implement

// the above approach

#include <bits/stdc++.h>

using namespace std;

 

// Function to generate and return

// the largest number

void largestNumber(int n, int X, int Y)

{

 int maxm = max(X, Y);

 

 // Store the smaller in Y

 Y = X + Y - maxm;

 

 // Store the larger in X

 X = maxm;

 

 // Stores respective counts

 int Xs = 0;

 int Ys = 0;

 

 while (n > 0) {

 

 // If N is divisible by Y

 if (n % Y == 0) {

 

 // Append X, N times to

 // the answer

 Xs += n;

 

 // Reduce N to zero

 n = 0;

 }

 else {

 

 // Reduce N by X

 n -= X;

 

 // Append Y, X times

 // to the answer

 Ys += X;

 }

 }

 

 // If number can be formed

 if (n == 0) {

 while (Xs-- > 0)

 cout << X;

 

 while (Ys-- > 0)

 cout << Y;

 }

 

 // Otherwise

 else

 cout << "-1";

}

 

// Driver Code

int main()

{

 int n = 19, X = 7, Y = 5;

 largestNumber(n, X, Y);

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

// Java program to implement the

// above approach 

import java.util.*;

 

class GFG{

 

// Function to generate and return 

// the largest number 

public static void largestNumber(int n, int X,

 int Y) 

{ 

 int maxm = Math.max(X, Y); 

 

 // Store the smaller in Y 

 Y = X + Y - maxm; 

 

 // Store the larger in X 

 X = maxm; 

 

 // Stores respective counts 

 int Xs = 0; 

 int Ys = 0; 

 

 while (n > 0)

 { 

 

 // If N is divisible by Y 

 if (n % Y == 0)

 { 

 

 // Append X, N times to 

 // the answer 

 Xs += n; 

 

 // Reduce N to zero 

 n = 0; 

 } 

 else

 { 

 // Reduce N by X 

 n -= X; 

 

 // Append Y, X times 

 // to the answer 

 Ys += X; 

 } 

 } 

 

 // If number can be formed 

 if (n == 0)

 { 

 while (Xs-- > 0) 

 System.out.print(X);

 

 while (Ys-- > 0) 

 System.out.print(Y); 

 } 

 

 // Otherwise 

 else

 System.out.print("-1");

} 

 

// Driver code

public static void main (String[] args) 

{

 int n = 19, X = 7, Y = 5; 

 

 largestNumber(n, X, Y); 

}

}

 

// This code is contributed by divyeshrabadiya07  
  
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

# Python3 program to implement

# the above approach 

 

# Function to generate and return 

# the largest number

def largestNumber(n, X, Y):

 

 maxm = max(X, Y)

 

 # Store the smaller in Y

 Y = X + Y - maxm

 

 # Store the larger in X

 X = maxm

 

 # Stores respective counts

 Xs = 0

 Ys = 0

 

 while (n > 0):

 

 # If N is divisible by Y

 if (n % Y == 0):

 

 # Append X, N times to

 # the answer

 Xs += n

 

 # Reduce N to zero

 n = 0

 

 else:

 

 # Reduce N by x

 n -= X

 

 # Append Y, X times to

 # the answer

 Ys += X

 

 # If number can be formed

 if (n == 0):

 

 while (Xs > 0):

 Xs -= 1

 print(X, end = '')

 

 while (Ys > 0):

 Ys -= 1

 print(Y, end = '')

 

 # Otherwise

 else:

 print("-1")

 

# Driver code

n = 19

X = 7

Y = 5

 

largestNumber(n, X, Y)

 

# This code is contributed by himanshu77  
  
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

// C# program to implement the

// above approach 

using System;

class GFG{

 

// Function to generate and return 

// the largest number 

public static void largestNumber(int n, int X,

 int Y) 

{ 

 int maxm = Math.Max(X, Y); 

 

 // Store the smaller in Y 

 Y = X + Y - maxm; 

 

 // Store the larger in X 

 X = maxm; 

 

 // Stores respective counts 

 int Xs = 0; 

 int Ys = 0; 

 

 while (n > 0)

 { 

 

 // If N is divisible by Y 

 if (n % Y == 0)

 { 

 

 // Append X, N times to 

 // the answer 

 Xs += n; 

 

 // Reduce N to zero 

 n = 0; 

 } 

 else

 { 

 // Reduce N by X 

 n -= X; 

 

 // Append Y, X times 

 // to the answer 

 Ys += X; 

 } 

 } 

 

 // If number can be formed 

 if (n == 0)

 { 

 while (Xs-- > 0) 

 Console.Write(X);

 

 while (Ys-- > 0) 

 Console.Write(Y); 

 } 

 

 // Otherwise 

 else

 Console.Write("-1");

} 

 

// Driver code

public static void Main (String[] args) 

{

 int n = 19, X = 7, Y = 5; 

 

 largestNumber(n, X, Y); 

}

}

 

// This code is contributed by shivanisinghss2110  
  
---  
  
 __

 __

 **Output:**

    
    
    7777755555555555555
    

_**Time Complexity:** O(N)  
 **Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

