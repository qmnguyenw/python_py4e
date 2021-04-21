Make A, B and C equal by adding total value N to them



Given 3 integers **A, B, and C** , and an integer **N** , the task is to
distribute **N** among all the other 3 numbers such that at the end **A = B =
C**. If the distribution is possible then print “Yes” otherwise output “No”.  
 **Examples:**  

> **Input:** A = 5, B = 3, C = 2, N = 8  
> **Output:** Yes  
> **Explanation:**  
> We can distribute N = 8 by adding 1 to A, 3 to B and 4 to C to get all of
> them as 6. Hence the distribution is possible.
>
>  **Input:** A = 10, B = 20, C = 15, N = 14  
> **Output:** No  
> **Explanation:**  
> Distribution of N among all three integers to make them equal is not
> possible.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
To solve the problem mentioned above we have to follow the steps given below:

  * Find **maximum** out of all the three integers A, B and C. Let that be integer _K_
  * Multiply the integer K by 3 and then subtract it by the sum of the three integers.
  * Check if the difference of that number and N is **divisible by 3** or not.
  * If it is, then the output is “Yes”, otherwise it is not possible to distribute the number.

Below is the implementation of the above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to distribute integer N

// among A, B, C such that they become equal 

#include<bits/stdc++.h>

using namespace std;

 

void distributeN(int A, int B, int C, int n)

{

 // Find maximum among the three elements 

 int max1 = max(A, B);

 int max2 = max(B, C);

 int maximum = max(max1, max2);

 

 // Summation of three elements 

 int sum = A + B + C;

 int p = (3 * maximum) - sum;

 int diff = n - p;

 

 // Check if difference is divisible by 3 

 if (diff < 0 || diff % 3) 

 cout << "No";

 else

 cout << "Yes";

}

 

// Driver code

int main()

{

 int A = 10, B = 20;

 int C = 15, n = 14;

 

 distributeN(A, B, C, n);

 return 0;

}

 

// This code is contributed by PratikBasu  
  
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

// Java program to distribute integer N

// among A, B, C such that they become equal 

class GFG{

 

static void distributeN(int A, int B, int C, 

 int n)

{

 

 // Find maximum among the three elements 

 int max1 = Math.max(A, B);

 int max2 = Math.max(B, C);

 int maximum = Math.max(max1, max2);

 

 // Summation of three elements 

 int sum = A + B + C;

 int p = (3 * maximum) - sum;

 int diff = n - p;

 

 // Check if difference is divisible by 3 

 if (diff < 0 || diff % 3 == 0) 

 System.out.print("No");

 else

 System.out.print("Yes");

}

 

// Driver code

public static void main(String[] args)

{

 int A = 10, B = 20;

 int C = 15, n = 14;

 

 distributeN(A, B, C, n);

}

}

 

// This code is contributed by Rajput-Ji   
  
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

# Python3 Program to Distribute integer N

# among A, B, C such that they become equal

 

def distributeN(A, B, C, n):

 

 # find maximum among the three elements

 maximum = max(A, B, C)

 

 # summation of three elements

 sum = A + B+C

 

 

 p = (3 * maximum)-sum

 

 diff = n-p

 

 # check if difference is divisible by 3

 if diff < 0 or diff % 3: 

 print "No"

 else:

 print "Yes"

 

 

# Driver code 

A = 10

B = 20

C = 15

n = 14

distributeN(A, B, C, n)  
  
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

// C# program to distribute integer N

// among A, B, C such that they become equal 

using System;

 

class GFG{

 

static void distributeN(int A, int B, int C, 

 int n)

{

 

 // Find maximum among the three elements 

 int max1 = Math.Max(A, B);

 int max2 = Math.Max(B, C);

 int maximum = Math.Max(max1, max2);

 

 // Summation of three elements 

 int sum = A + B + C;

 int p = (3 * maximum) - sum;

 int diff = n - p;

 

 // Check if difference is divisible by 3 

 if (diff < 0 || diff % 3 == 0) 

 Console.Write("No");

 else

 Console.Write("Yes");

}

 

// Driver code

public static void Main(String[] args)

{

 int A = 10, B = 20;

 int C = 15, n = 14;

 

 distributeN(A, B, C, n);

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    No
    

_**Time Complexity:** O(1)_  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

