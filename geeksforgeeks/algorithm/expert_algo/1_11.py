Represent N as sum of K even numbers



Given two integers **N** and **K** , the task is to represent N as sum of K
even number. If it is not possible to represent the number, print -1.

 _ **Note:** The representation may contain duplicate even numbers._

 **Examples:**

>  **Input:** N = 6, K = 3  
>  **Output:** 2 2 2  
>  **Explanation:**  
>  The given number 6 can be represented as 2 + 2 + 2 = 6
>
>  **Input:** N = 8, K = 2  
>  **Output:** 2 6  
>  **Explanation:**  
>  The given number 3 can be represented as 2 + 6 = 8
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** To solve the problem mentioned above a simple solution is to
maximise the occurrence of 2 which is the smallest even number. Necessary
condition to represent N as sum of K numbers are:

  *  **(K – 1) * 2** must be less than N.
  *  **N – (K – 1) * 2** must be Even.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to represent

// N as sum of K even numbers

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to print the representation

void sumEvenNumbers(int N, int K)

{

 int check = N - 2 * (K - 1);

 

 // N must be greater than equal to 2*K

 // and must be even

 if (check > 0 && check % 2 == 0) {

 for (int i = 0; i < K - 1; i++) {

 cout << "2 ";

 }

 cout << check;

 }

 else {

 cout << "-1";

 }

}

 

// Driver Code

int main()

{

 int N = 8;

 int K = 2;

 

 sumEvenNumbers(N, K);

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

// Java implementation to represent

// N as sum of K even numbers

import java.util.*;

 

class GFG{

 

// Function to print the representation

static void sumEvenNumbers(int N, int K)

{

 int check = N - 2 * (K - 1);

 

 // N must be greater than equal to 2 * K

 // and must be even

 if (check > 0 && check % 2 == 0)

 {

 for(int i = 0; i < K - 1; i++)

 {

 System.out.print("2 ");

 }

 System.out.println(check);

 }

 else

 {

 System.out.println("-1");

 }

}

 

// Driver Code

public static void main(String args[])

{

 int N = 8;

 int K = 2;

 

 sumEvenNumbers(N, K);

}

}

 

// This code is contributed by ANKITKUMAR34  
  
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

# Python3 implementation to represent

# N as sum of K even numbers

 

# Function to print the representation

def sumEvenNumbers(N, K):

 

 check = N - 2 * (K - 1)

 

 # N must be greater than equal to 2 * K

 # and must be even

 if (check > 0 and check % 2 == 0):

 for i in range(K - 1):

 print("2 ", end = "")

 

 print(check)

 else:

 print("-1")

 

# Driver Code

N = 8

K = 2

sumEvenNumbers(N, K)

 

# This code is contributed by ANKITKUMAR34  
  
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

// C# implementation to represent

// N as sum of K even numbers

using System;

 

class GFG{

 

// Function to print the representation

static void sumEvenNumbers(int N, int K)

{

 int check = N - 2 * (K - 1);

 

 // N must be greater than equal to

 // 2 * K and must be even

 if (check > 0 && check % 2 == 0)

 {

 for(int i = 0; i < K - 1; i++)

 {

 Console.Write("2 ");

 }

 Console.WriteLine(check);

 }

 else

 {

 Console.WriteLine("-1");

 }

}

 

// Driver Code

static public void Main(String []args)

{

 int N = 8;

 int K = 2;

 

 sumEvenNumbers(N, K);

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    2 6
    

_**Time Complexity:** O(K)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

