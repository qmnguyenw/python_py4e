Print all repeating digits present in a given number in sorted order



Given an integer **N** , the task is to print all the repeating digits present
in **N** in sorted order.

Examples:

>  **Input:** N = 45244336543  
>  **Output:** 3 4 5  
>  **Explanation:** The duplicate digits are 3 4 5
>
>  **Input:** N = 987065467809  
>  **Output:** 0 6 7 8 9

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to use Hashing to store the frequency of digits of
**N** and print those digits whose frequency exceeds **1.**

  

  

  * Initialize a HashMap, to store frequency of digits **0-9**.
  * Convert the integer to its equivalent string.
  * Iterate over the characters of the string, and for each character, perform the following steps:
    * Convert the current character to an integer using typecasting
    * Increment the count of that digit in a HashMap.
  * Traverse the HashMap and print the digits whose count exceeds 1.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h>

using namespace std;

// Function to print repeating

// digits present in the number N

void printDup(string N)

{

 // Stores the count of

 // unique digits

 int res = 0;

 // Map to store frequency

 // of each digit

 int cnt[10];

 // Set count of all digits to 0

 for (int i = 0; i < 10; i++)

 cnt[i] = 0;

 // Traversing the string

 for (int i = 0; i < N.size(); i++) {

 // Convert the character

 // to equivalent integer

 int digit = (N[i] - '0');

 // Increase the count of digit

 cnt[digit] += 1;

 }

 // Traverse the Map

 for (int i = 0; i < 10; i++) {

 // If frequency

 // of digit exceeds 1

 if (cnt[i] > 1)

 cout << i << " ";

 }

 cout << endl;

}

// Driver Code

int main()

{

 string N = "45244336543";

 // Function call to print

 // repeating digits in N

 printDup(N);

 return 0;

}

// This code is contributed by Kingash.  
  
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

// Java program for the above approach

import java.io.*;

import java.util.*;

class GFG {

 // Function to print repeating

 // digits present in the number N

 static void printDup(String N)

 {

 // Stores the count of

 // unique digits

 int res = 0;

 // Map to store frequency

 // of each digit

 int cnt[] = new int[10];

 // Traversing the string

 for (int i = 0; i < N.length(); i++) {

 // Convert the character

 // to equivalent integer

 int digit = (N.charAt(i) - '0');

 // Increase the count of digit

 cnt[digit] += 1;

 }

 // Traverse the Map

 for (int i = 0; i < 10; i++) {

 // If frequency

 // of digit exceeds 1

 if (cnt[i] > 1)

 System.out.print(i + " ");

 }

 System.out.println();

 }

 // Driver Code

 public static void main(String[] args)

 {

 String N = "45244336543";

 // Function call to print

 // repeating digits in N

 printDup(N);

 }

}

// This code is contributed by Kingash.  
  
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

# Python implementation

# of the above approach

# Function to print repeating

# digits present in the number N

def printDup(N):

 # Stores the count of

 # unique digits

 res = 0

 # Set count of all digits to 0

 cnt = [0] * 10

 # Convert integer to

 # equivalent string

 string = str(N)

 # Traversing the string

 for i in string:

 # Convert the character

 # to equivalent integer

 digit = int(i)

 # Increase the count of digit

 cnt[digit] += 1

 # Traverse the Map

 for i in range(10):

 # If frequency

 # of digit is 1

 if (cnt[i] > 1):

 # If count exceeds 1

 print(i, end=" ")

# Driver Code

N = 45244336543

# Function call to print

# repeating digits in N

printDup(N)  
  
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

class GFG

{

 // Function to print repeating

 // digits present in the number N

 static void printDup(string N)

 {

 

 // Stores the count of

 // unique digits

 int res = 0;

 // Map to store frequency

 // of each digit

 int[] cnt = new int[10];

 // Traversing the string

 for (int i = 0; i < N.Length; i++) {

 // Convert the character

 // to equivalent integer

 int digit = (N[i] - '0');

 // Increase the count of digit

 cnt[digit] += 1;

 }

 // Traverse the Map

 for (int i = 0; i < 10; i++) {

 // If frequency

 // of digit exceeds 1

 if (cnt[i] > 1)

 Console.Write(i + " ");

 }

 Console.WriteLine();

 }

 // Driver code

 public static void Main()

 {

 string N = "45244336543";

 // Function call to print

 // repeating digits in N

 printDup(N);

 }

}

// This code is contributed by code_hunt.  
  
---  
  
 __

 __

 **Output:**

    
    
    3 4 5

_**Time Complexity:** O(log10N)_  
 _ **Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

