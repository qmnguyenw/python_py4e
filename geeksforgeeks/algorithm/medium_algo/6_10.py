Count number of steps to cover a distance if steps can be taken in powers of 2



Given a distance K to cover, the task is to find the minimum steps required to
cover the distance if steps can be taken in powers of 2 like 1, 2, 4, 8,
16……..

 **Examples :**

    
    
    **Input :** K = 9
    **Output :** 2
    
    **Input :** K = 343 
    **Output :** 6
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The minimum steps required can be calculated by reducing K by the highest
power of 2 in each step which can be obtained by counting no. of set bits in
the binary representation of a number.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count the minimum number of steps

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to count the minimum number of steps

int getMinSteps(int K)

{

 // __builtin_popcount() is a C++ function to 

 // count the number of set bits in a number

 return __builtin_popcount(k);

}

 

// Driver Code

int main()

{

 int n = 343;

 

 cout << getMinSteps(n)<< '\n';

 

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

// Java program to count minimum number of steps

import java.io.*;

 

class GFG

{

 

 // Function to count the minimum number of steps 

 static int getMinSteps(int K) 

 { 

 // count the number of set bits in a number 

 return Integer.bitCount(K);

 } 

 

 // Driver Code 

 public static void main (String[] args)

 { 

 int n = 343; 

 

 System.out.println(getMinSteps(n)); 

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

# Python 3 implementation of the approach

 

# Function to count the minimum number of steps 

def getMinSteps(K) :

 

 # bin(K).count("1") is a Python3 function to 

 # count the number of set bits in a number 

 return bin(K).count("1")

 

# Driver Code 

n = 343

print(getMinSteps(n))

 

# This code is contributed by

# divyamohan123  
  
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

// C# program to count minimum number of steps

using System;

 

class GFG

{

 

 // Function to count the minimum number of steps 

 static int getMinSteps(int K) 

 { 

 // count the number of set bits in a number 

 return countSetBits(K);

 } 

 

 static int countSetBits(int x)

 {

 int setBits = 0;

 while (x != 0)

 {

 x = x & (x - 1);

 setBits++;

 }

 return setBits;

 }

 

 // Driver Code 

 public static void Main (String[] args)

 { 

 int n = 343; 

 

 Console.WriteLine(getMinSteps(n)); 

 } 

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    

**Time Complexity :** ![ O\(log\(n\)\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-9ef212fa98559156a302c6143b1cb175_l3.png)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

