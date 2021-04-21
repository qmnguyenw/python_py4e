Count possible combinations of pairs with adjacent elements from first N
numbers



Given a number N, the task is to count all possible combinations of pairs
formed using adjacent elements.

 **Note** : If an element exists already in a pair, it cannot be picked in the
next pair. For example: for {1,2,3}: {1,2} and {2,3} will not be considered as
a correct combination.

 **Examples:**

    
    
    **Input :** N = 4
    **Output :** 5
    **Explanation :** If N = 4, the possible combinations are:
    {1}, {2}, {3}, {4}
    {1, 2}, {3, 4}
    {1}, {2, 3}, {4}
    {1}, {2}, {3, 4}
    {1, 2}, {3}, {4}
    
    **Input :** N = 5
    **Output :** 8
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach :** Break the problem into smaller subproblems. If there are N
numbers, and there are two cases either a number is alone, or it is in a pair,
if a number is alone, find the ways of pairing (n-1) numbers left, or if it is
in a pair, find the ways of pairing (n-2) numbers left. If there are just 2
numbers left they can generate 2 combinations either alone or in a pair, and
if a single number is left it will be in singleton, so there is just 1
combination.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

// Function to count the number of ways

int ways(int n)

{

 // If there is a single number left 

 // it will form singleton

 if (n == 1) {

 return 1;

 }

 // if there are just 2 numbers left, 

 // they will form a pair

 if (n == 2) {

 return 2;

 }

 else {

 return ways(n - 1) + ways(n - 2);

 }

}

 

// Driver Code

int main()

{

 int n = 5;

 

 cout << "Number of ways = " << ways(n);

 

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

/*package whatever //do not write package name here */

import java.io.*;

 

class GFG

{

 

// Function to count the number of ways

static int ways(int n)

{

 // If there is a single number left 

 // it will form singleton

 if (n == 1) 

 {

 return 1;

 }

 

 // if there are just 2 numbers left, 

 // they will form a pair

 if (n == 2) 

 {

 return 2;

 }

 else

 {

 return ways(n - 1) + ways(n - 2);

 }

}

 

// Driver Code

public static void main (String[] args) 

{

 int n = 5;

 

 System.out.println("Number of ways = " + ways(n));

}

}  
  
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

# Python3 code implementation of the above program

 

# Function to count the number of ways 

def ways(n) :

 

 # If there is a single number left 

 # it will form singleton 

 if (n == 1) :

 return 1; 

 

 # if there are just 2 numbers left, 

 # they will form a pair 

 if (n == 2) :

 return 2; 

 

 else :

 return ways(n - 1) + ways(n - 2); 

 

# Driver Code 

if __name__ == "__main__" : 

 

 n = 5; 

 

 print("Number of ways = ", ways(n)); 

 

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

// C# implementation of the above code

using System;

 

class GFG 

{ 

 

// Function to count the number of ways 

static int ways(int n) 

{ 

 // If there is a single number left 

 // it will form singleton 

 if (n == 1) 

 { 

 return 1; 

 } 

 

 // if there are just 2 numbers left, 

 // they will form a pair 

 if (n == 2) 

 { 

 return 2; 

 } 

 else

 { 

 return ways(n - 1) + ways(n - 2); 

 } 

} 

 

// Driver Code 

public static void Main() 

{ 

 int n = 5; 

 

 Console.WriteLine("Number of ways = " + ways(n)); 

} 

} 

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

    
    
    Number of ways = 8
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

