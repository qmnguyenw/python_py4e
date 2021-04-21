Maximize the Expression | Bit Manipulation



Given two positive integers **A** and **B**. Let’s define **D** such that **B
AND D = D**. The task is to maximize the expression **A XOR D**.

 **Examples:**

    
    
    **Input:** A = 11 B = 4
    **Output:** 15
    Take D = 4 as (B AND D) = (4 AND 4) = 4.
    Also, (A XOR D) = (11 XOR 4) = 15 which is the 
    maximum according to the given condition.
    
    **Input:** A = 9 and B = 13
    **Output:** 13
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Since **B AND D = D** , **D** will always be smaller than
or equal to **B**. Hence, one can run a loop from **1** to **B** and check
whether the given conditions are satisfied or not.

 **Efficient approach:** Instead of running a loop and checking for each **D**
, the maximum value of the expression **(A XOR D)** can be easily calculated
using Bit Manipulation techniques.  
Let’s take an example to understand the way to approach the problem:

    
    
    A = 11 = 1011, B = 14 = 1110
    Let's assume D = abcd in base 2 notation
    
    B AND D:     1110           A XOR D:     1011
                 abcd                        abcd   
                ------                      ------
                 abcd                        ????
    
    At 0th place: (0 AND d) = d implies d = 0 
    At 1st place: (1 AND c) = c implies c = 0, 1 but to maximize (A XOR D), take c = 0
    At 2nd place: (1 AND b) = b implies b = 0, 1 but to maximize (A XOR D), take b = 1
    At 3rd place: (1 AND a) = a implies a = 0, 1 but to maximize (A XOR D), take a = 0
    
    Hence, D = 0100 = 4 and maximum value of (A XOR D) = (11 XOR 4) = 15.
    

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

#include <iostream>

using namespace std;

 

#define MAX 32

 

// Function to return the value of

// the maximized expression

int maximizeExpression(int a, int b)

{

 int result = a;

 

 // int can have 32 bits

 for (int bit = MAX - 1; bit >= 0; bit--) {

 

 // Consider the ith bit of D to be 1

 int bitOfD = 1 << bit;

 

 // Calculate the value of (B AND bitOfD)

 int x = b & bitOfD;

 

 // Check if bitOfD satisfies (B AND D = D)

 if (x == bitOfD) {

 

 // Check if bitOfD can maximize (A XOR D)

 int y = result & bitOfD;

 if (y == 0) {

 result = result ^ bitOfD;

 }

 }

 

 // Note that we do not need to consider ith bit of D

 // to be 0 because if above condition are not satisfied

 // then value of result will not change

 // which is similar to considering bitOfD = 0

 // as result XOR 0 = result

 }

 

 return result;

}

 

// Driver code

int main()

{

 int a = 11, b = 14;

 

 cout << maximizeExpression(a, b);

 

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

 final static int MAX = 32;

 

 // Function to return the value of 

 // the maximized expression 

 static int maximizeExpression(int a, int b) 

 { 

 int result = a; 

 

 // int can have 32 bits 

 for (int bit = MAX - 1; bit >= 0; bit--) 

 { 

 

 // Consider the ith bit of D to be 1 

 int bitOfD = 1 << bit; 

 

 // Calculate the value of (B AND bitOfD) 

 int x = b & bitOfD; 

 

 // Check if bitOfD satisfies (B AND D = D) 

 if (x == bitOfD) { 

 

 // Check if bitOfD can maximize (A XOR D) 

 int y = result & bitOfD; 

 if (y == 0) 

 { 

 result = result ^ bitOfD; 

 } 

 } 

 

 // Note that we do not need to consider ith bit of D 

 // to be 0 because if above condition are not satisfied 

 // then value of result will not change 

 // which is similar to considering bitOfD = 0 

 // as result XOR 0 = result 

 } 

 return result; 

 } 

 

 // Driver code 

 public static void main (String[] args) 

 { 

 int a = 11, b = 14; 

 

 System.out.println(maximizeExpression(a, b)); 

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

MAX = 32

 

# Function to return the value of 

# the maximized expression 

def maximizeExpression(a, b) : 

 

 result = a 

 

 # int can have 32 bits 

 for bit in range(MAX - 1, -1, -1) : 

 

 # Consider the ith bit of D to be 1 

 bitOfD = 1 << bit 

 

 # Calculate the value of (B AND bitOfD) 

 x = b & bitOfD 

 

 # Check if bitOfD satisfies (B AND D = D) 

 if (x == bitOfD) : 

 

 # Check if bitOfD can maximize (A XOR D) 

 y = result & bitOfD 

 if (y == 0) :

 result = result ^ bitOfD 

 

 # Note that we do not need to consider ith bit of D 

 # to be 0 because if above condition are not satisfied 

 # then value of result will not change 

 # which is similar to considering bitOfD = 0 

 # as result XOR 0 = result 

 

 return result

 

# Driver code 

a = 11

b = 14

print(maximizeExpression(a, b)) 

 

# This code is contributed by divyamohan123  
  
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

// C# implementation of the above approach

using System; 

class GFG 

{

 static int MAX = 32;

 

 // Function to return the value of 

 // the maximized expression 

 static int maximizeExpression(int a, int b) 

 { 

 int result = a; 

 

 // int can have 32 bits 

 for (int bit = MAX - 1; bit >= 0; bit--) 

 { 

 

 // Consider the ith bit of D to be 1 

 int bitOfD = 1 << bit; 

 

 // Calculate the value of (B AND bitOfD) 

 int x = b & bitOfD; 

 

 // Check if bitOfD satisfies (B AND D = D) 

 if (x == bitOfD)

 { 

 

 // Check if bitOfD can maximize (A XOR D) 

 int y = result & bitOfD; 

 if (y == 0) 

 { 

 result = result ^ bitOfD; 

 } 

 } 

 

 // Note that we do not need to consider 

 // ith bit of D to be 0 because if 

 // above condition are not satisfied then 

 // value of result will not change which is 

 // similar to considering bitOfD = 0 as 

 // result XOR 0 = result 

 } 

 return result; 

 } 

 

 // Driver code 

 public static void Main (String []args) 

 { 

 int a = 11, b = 14; 

 

 Console.WriteLine(maximizeExpression(a, b)); 

 } 

}

 

// This code is contributed by Arnab Kundu  
  
---  
  
 __

 __

 **Output:**

    
    
    15
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

