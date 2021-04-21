Bitonic string



Given a string **str** , the task is to check if that string is a Bitonic
String or not. If string **str** is Bitonic String then print **“YES”** else
print **“NO”**.  

> A Bitonic String is a string in which the characters are arranged in
> increasing order followed by decreasing order of their ASCII values.  
>

**Examples:**  

> **Input:** str = “abcdfgcba”  
> **Output:** YES  
> **Explanation:**  
> In the above string, the ASCII values first increases {a, b, c, d, f, g} and
> then decreases {g, c, b, a}.  
>  **Input:** str = “abcdwef”  
> **Output:** NO  
>

  

  

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
To solve the problem, we simply need to traverse the string and check if the
ASCII values of the characters of the string follow any of the following
patterns:  

  * Strictly increasing.
  * Strictly decreasing.
  * Strictly increasing followed by strictly decreasing.

Follow these steps below to solve the problem:  

  1. Start traversing the string and keep checking if the ASCII value of the next character is greater than the ASCII value of the current character or not.
  2. If at any point, the ASCII value of the next character is not greater than the ASCII value of the current character, break the loop.
  3. Again start traversing from the above break index and check if the ASCII value of the next character is smaller than the ASCII value of the current character or not.
  4. If at any point the ASCII value of the next character is not smaller than the ASCII value of the current character before the end of the array is reached, then print **“NO”** and break the loop.
  5. If the end of the array is reached successfully, print **“YES”**.

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

 

// Function to check if the given

// string is bitonic

int checkBitonic(string s)

{

 int i, j;

 

 // Check for increasing sequence

 for (i = 1; i < s.size(); i++) {

 if (s[i] > s[i - 1])

 continue;

 

 if (s[i] <= s[i - 1])

 break;

 }

 

 // If end of string has been reached

 if (i == s.size() - 1)

 return 1;

 

 // Check for decreasing sequence

 for (j = i + 1; j < s.size();

 j++) {

 if (s[j] < s[j - 1])

 continue;

 

 if (s[j] >= s[j - 1])

 break;

 }

 

 i = j;

 

 // If the end of string hasn't

 // been reached

 if (i != s.size())

 return 0;

 

 // Return true if bitonic

 return 1;

}

 

// Driver Code

int main()

{

 // Given string

 string s = "abcdfgcba";

 

 // Function Call

 (checkBitonic(s) == 1)

 ? cout << "YES"

 : cout << "NO";

 

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

// Java program for the above approach

import java.util.*;

 

class GFG{

 

// Function to check if the given

// String is bitonic

static int checkBitonic(char []s)

{

 int i, j;

 

 // Check for increasing sequence

 for(i = 1; i < s.length; i++)

 {

 if (s[i] > s[i - 1])

 continue;

 

 if (s[i] <= s[i - 1])

 break;

 }

 

 // If end of String has been reached

 if (i == s.length - 1)

 return 1;

 

 // Check for decreasing sequence

 for(j = i + 1; j < s.length; j++)

 {

 if (s[j] < s[j - 1])

 continue;

 

 if (s[j] >= s[j - 1])

 break;

 }

 i = j;

 

 // If the end of String hasn't

 // been reached

 if (i != s.length)

 return 0;

 

 // Return true if bitonic

 return 1;

}

 

// Driver Code

public static void main(String[] args)

{

 

 // Given String

 String s = "abcdfgcba";

 

 // Function Call

 System.out.print((checkBitonic(

 s.toCharArray()) == 1) ? "YES" : "NO");

}

}

 

// This code is contributed by PrinciRaj1992  
  
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

# Python3 program for the above approach

 

# Function to check if the given 

# string is bitonic 

def checkBitonic(s): 

 

 i = 0

 j = 0

 

 # Check for increasing sequence 

 for i in range(1, len(s)): 

 if (s[i] > s[i - 1]):

 continue; 

 

 if (s[i] <= s[i - 1]):

 break; 

 

 # If end of string has been reached 

 if (i == (len(s) - 1)):

 return True;

 

 # Check for decreasing sequence 

 for j in range(i + 1, len(s)):

 if (s[j] < s[j - 1]):

 continue;

 

 if (s[j] >= s[j - 1]):

 break;

 i = j; 

 

 # If the end of string hasn't 

 # been reached

 if (i != len(s) - 1):

 return False; 

 

 # Return true if bitonic

 return True; 

 

# Driver code

 

# Given string

s = "abcdfgcba"

 

# Function Call

if(checkBitonic(s)):

 print("YES")

else:

 print("NO") 

 

# This code is contributed by grand_master  
  
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

// C# program for the above approach

using System;

 

class GFG{ 

 

// Function to check if the given 

// String is bitonic 

static int checkBitonic(char []s) 

{ 

 int i, j; 

 

 // Check for increasing sequence 

 for(i = 1; i < s.Length; i++) 

 { 

 if (s[i] > s[i - 1]) 

 continue; 

 

 if (s[i] <= s[i - 1]) 

 break; 

 } 

 

 // If end of String has been reached 

 if (i == s.Length - 1) 

 return 1; 

 

 // Check for decreasing sequence 

 for(j = i + 1; j < s.Length; j++) 

 { 

 if (s[j] < s[j - 1]) 

 continue; 

 

 if (s[j] >= s[j - 1]) 

 break; 

 } 

 i = j; 

 

 // If the end of String hasn't 

 // been reached 

 if (i != s.Length) 

 return 0; 

 

 // Return true if bitonic 

 return 1; 

} 

 

// Driver Code 

public static void Main(String[] args) 

{ 

 

 // Given String 

 String s = "abcdfgcba"; 

 

 // Function call 

 Console.Write((checkBitonic( 

 s.ToCharArray()) == 1) ? "YES" : "NO"); 

} 

} 

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    YES
    

**Time Complexity:** _O(N)_  
**Auxiliary Space:** _O(1)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

