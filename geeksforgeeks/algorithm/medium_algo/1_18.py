Count of binary strings of given length consisting of at least one 1



Given an integer **N** , the task is to print the number of binary strings of
length N which at least one ‘1’.

 **Examples:**

>  **Input:** 2  
>  **Output:** 3  
>  **Explanation:**  
>  “01”, “10” and “11” are the possible strings
>
>  **Input:** 3  
>  **Output:** 7  
>  **Expalnation:**  
>  “001”, “011”, “010”, “100”, “101”, “110” and “111” are the possible strings

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
We can observe that:

  

  

> Only one string of length N does not contain any 1, the one filled with only
> 0’s.  
> Since **2 N** strings are possible of length N, the required answer is **2 N
> – 1**.

Follow the steps below to solve the problem:

  * Initialize X = 1.
  * Compute upto **2 N** by performing bitwise left shift on X, N-1 times.
  * Finally, print X – 1 as the required answer.

Below is the implementation of our approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to implement

// the above approach

#include <bits/stdc++.h>

using namespace std;

 

// Function to return

// the count of strings

long count_strings(long n)

{

 int x = 1;

 

 // Calculate pow(2, n)

 for (int i = 1; i < n; i++) {

 x = (1 << x);

 }

 

 // Return pow(2, n) - 1

 return x - 1;

}

 

// Driver Code

int main()

{

 long n = 3;

 

 cout << count_strings(n);

 

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

// Java program to implement

// the above approach

import java.util.*;

 

class GFG{

 

// Function to return

// the count of Strings

static long count_Strings(long n)

{

 int x = 1;

 

 // Calculate Math.pow(2, n)

 for(int i = 1; i < n; i++)

 {

 x = (1 << x);

 }

 

 // Return Math.pow(2, n) - 1

 return x - 1;

}

 

// Driver Code

public static void main(String[] args)

{

 long n = 3;

 

 System.out.print(count_Strings(n));

}

}

 

// This code is contributed by Amit Katiyar  
  
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

 

# Function to return

# the count of Strings

def count_Strings(n):

 

 x = 1;

 

 # Calculate pow(2, n)

 for i in range(1, n):

 x = (1 << x);

 

 # Return pow(2, n) - 1

 return x - 1;

 

# Driver Code

if __name__ == '__main__':

 

 n = 3;

 

 print(count_Strings(n));

 

# This code is contributed by Princi Singh  
  
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

// C# program to implement

// the above approach

using System;

 

class GFG{

 

// Function to return

// the count of Strings

static long count_Strings(long n)

{

 int x = 1;

 

 // Calculate Math.Pow(2, n)

 for(int i = 1; i < n; i++)

 {

 x = (1 << x);

 }

 

 // Return Math.Pow(2, n) - 1

 return x - 1;

}

 

// Driver Code

public static void Main(String[] args)

{

 long n = 3;

 

 Console.Write(count_Strings(n));

}

}

 

// This code is contributed by Amit Katiyar  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

_  
**Time Complexity:** O(N)  
 **Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

