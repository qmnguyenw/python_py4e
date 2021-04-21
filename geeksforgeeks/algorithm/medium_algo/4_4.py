Lexicographically all Shortest Palindromic Substrings from a given string



Given a **string s** of size N. The task is to find lexicographically all
shortest palindromic substrings from the given string.

 **Examples:**

>  **Input:** s= “programming”  
>  **Output:** a g i m n o p r  
>  **Explanation:**  
>  The Lexicographical shortest palindrome substring for the word
> “programming” will be the single characters from the given string. Hence,
> the output is : a g i m n o p r.
>
>  **Input:** s= “geeksforgeeks”  
>  **Output:** e f g k o r s

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

To solve the problem mentioned above the very first observation is that the
shortest palindromic substring will be of size 1. So as per the problem
statement, we have to find all distinct substring of size 1 lexicographically
which means all the characters in the given string.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find Lexicographically all

// Shortest Palindromic Substrings from a given string

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find all lexicographically

// shortest palindromic substring

void shortestPalindrome(string s)

{

 

 // Array to keep track of alphabetic characters

 int abcd[26] = { 0 };

 

 for (int i = 0; i < s.length(); i++)

 abcd[s[i] - 97] = 1;

 

 // Iterate to print all lexicographically shortest substring

 for (int i = 0; i < 26; i++) {

 if (abcd[i] == 1)

 cout << char(i + 97) << " ";

 }

}

 

// Driver code

int main()

{

 string s = "geeksforgeeks";

 

 shortestPalindrome(s);

 

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

// Java program to find Lexicographically all

// Shortest Palindromic Substrings from a given string

class Main

{

 // Function to find all lexicographically

 // shortest palindromic substring

 static void shortestPalindrome(String s)

 {

 

 // Array to keep track of 

 // alphabetic characters

 int[] abcd = new int[26];

 

 for (int i = 0; i < s.length(); i++)

 abcd[s.charAt(i) - 97] = 1;

 

 // Iterate to print all lexicographically

 // shortest substring

 for (int i = 0; i < 26; i++)

 {

 if (abcd[i] == 1) 

 {

 System.out.print((char)(i + 97) + " ");

 }

 }

 }

 

 // Driver code

 public static void main(String[] args)

 {

 String s = "geeksforgeeks";

 shortestPalindrome(s);

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

# C++ program to find Lexicographically all

# Shortest Palindromic Substrings from a given string

 

# Function to find all lexicographically 

# shortest palindromic substring

def shortestPalindrome (s) :

 

 # Array to keep track of alphabetic characters

 abcd = [0]*26

 

 for i in range(len(s)):

 abcd[ord(s[i])-97] = 1

 

 # Iterate to print all lexicographically shortest substring

 for i in range(26): 

 if abcd[i]== 1 :

 print( chr(i + 97), end =' ' )

 

# Driver code

s = "geeksforgeeks"

 

shortestPalindrome (s)  
  
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

// C# program to find Lexicographically

// all shortest palindromic substrings

// from a given string

using System;

 

class GFG{

 

// Function to find all lexicographically 

// shortest palindromic substring 

static void shortestPalindrome(string s) 

{ 

 

 // Array to keep track of

 // alphabetic characters 

 int[] abcd = new int[26]; 

 

 for(int i = 0; i < s.Length; i++) 

 abcd[s[i] - 97] = 1; 

 

 // Iterate to print all lexicographically 

 // shortest substring 

 for(int i = 0; i < 26; i++)

 { 

 if (abcd[i] == 1)

 { 

 Console.Write((char)(i + 97) + " "); 

 } 

 } 

} 

 

// Driver code 

static public void Main(string[] args) 

{ 

 string s = "geeksforgeeks"; 

 shortestPalindrome(s); 

} 

} 

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

    
    
    e f g k o r s
    

**Time Complexity:** O(N), where N is the size of the string.

 **Space Complexity:** O(1)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

