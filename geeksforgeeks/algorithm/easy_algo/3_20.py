Decimal to Binary using recursion and without using power operator



Given an integer **N** , the task is convert and print the binary equaiva;ent
of **N**.

 **Examples:**

>  **Input:** N = 13  
>  **Output:** 1101
>
>  **Input:** N = 15  
>  **Output:** 1111

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach** Write a recursive function that takes an argument **N** and
recursively calls itself with the value **N / 2** as the new argument and
prints **N % 2** after the call. The base condition will be when **N = 0** ,
simply print **0** and return out of the function in that case.

  

  

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

 

// Recursive function to convert n

// to its binary equivalent

void decimalToBinary(int n)

{

 // Base case

 if (n == 0) {

 cout << "0";

 return;

 }

 

 // Recursive call

 decimalToBinary(n / 2);

 cout << n % 2;

}

 

// Driver code

int main()

{

 int n = 13;

 

 decimalToBinary(n);

 

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

import java.io.*;

 

class GFG

{

 

 

// Recursive function to convert n

// to its binary equivalent

static void decimalToBinary(int n)

{

 // Base case

 if (n == 0) 

 {

 System.out.print("0");

 return;

 }

 

 // Recursive call

 decimalToBinary(n / 2);

 System.out.print( n % 2);

}

 

// Driver code

public static void main (String[] args) 

{

 int n = 13;

 

 decimalToBinary(n);

}

}

 

// This code is contributed by anuj_67..  
  
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

 

# Recursive function to convert n 

# to its binary equivalent 

def decimalToBinary(n) :

 

 # Base case 

 if (n == 0) :

 print("0",end=""); 

 return;

 

 # Recursive call 

 decimalToBinary(n // 2); 

 print(n % 2,end=""); 

 

 

# Driver code 

if __name__ == "__main__" : 

 

 n = 13;

 decimalToBinary(n); 

 

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

 

 // Recursive function to convert n

 // to its binary equivalent

 static void decimalToBinary(int n)

 {

 

 // Base case

 if (n == 0) 

 {

 Console.Write("0");

 return;

 }

 

 // Recursive call

 decimalToBinary(n / 2);

 Console.Write(n % 2);

 }

 

 // Driver code

 public static void Main(String[] args) 

 {

 int n = 13;

 

 decimalToBinary(n);

 }

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    01101
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

