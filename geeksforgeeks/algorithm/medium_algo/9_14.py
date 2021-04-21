Make palindromic string non-palindromic by rearranging its letters



Given a string **str** containing lowercase alphabets (a – z). The task is to
print the string after rearranging some characters such that the string
becomes non-palindromic. If its impossible to make the string non-palindrome
then print **-1**.

 **Examples:**

>  **Input:** str = “abba”  
>  **Output:** aabb
>
>  **Input:** str = “zzz”  
>  **Output:** -1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** If all the characters in the string are same then no matter how
you rearrange the characters, string will remain the same and will be
palindromic. Now, if a non-palindromic arrangement exists, the best way to
rearrange the characters is to sort the string which will form continuous
segment of same characters and will never be palindromic. In order to reduce
the time required to sort the string, we can store the frequencies of all the
26 characters and print them in sorted manner.

  

  

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP Program to rearrange letters of string

// to find a non-palindromic string if it exists

#include <bits/stdc++.h>

using namespace std;

 

// Function to print the non-palindromic string

// if it exists, otherwise prints -1

void findNonPalinString(string s)

{

 int freq[26] = { 0 }, flag = 0;

 

 for (int i = 0; i < s.size(); i++) {

 

 // If all characters are not

 // same, set flag to 1

 if (s[i] != s[0])

 flag = 1;

 

 // Update frequency of the current character

 freq[s[i] - 'a']++;

 }

 

 // If all characters are same

 if (!flag)

 cout << "-1";

 else {

 

 // Print characters in sorted manner

 for (int i = 0; i < 26; i++)

 for (int j = 0; j < freq[i]; j++)

 cout << char('a' + i);

 }

}

 

// Driver Code

int main()

{

 string s = "abba";

 

 findNonPalinString(s);

 

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

// Java Program to rearrange letters of string

// to find a non-palindromic string if it exists 

class GfG 

{ 

 

// Function to print the non-palindromic string 

// if it exists, otherwise prints -1 

static void findNonPalinString(char s[]) 

{ 

 int freq[] = new int[26];

 int flag = 0; 

 

 for (int i = 0; i < s.length; i++) 

 { 

 

 // If all characters are not 

 // same, set flag to 1 

 if (s[i] != s[0]) 

 flag = 1; 

 

 // Update frequency of 

 // the current character 

 freq[s[i] - 'a']++; 

 } 

 

 // If all characters are same 

 if (flag == 0) 

 System.out.println("-1"); 

 else

 { 

 

 // Print characters in sorted manner 

 for (int i = 0; i < 26; i++) 

 for (int j = 0; j < freq[i]; j++) 

 System.out.print((char)('a' + i)); 

 } 

} 

 

// Driver Code 

public static void main(String[] args) 

{ 

 String s = "abba"; 

 

 findNonPalinString(s.toCharArray()); 

}

} 

 

// This code is contributed by 

// Prerna Saini.  
  
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

# Python3 Program to rearrange letters of string

# to find a non-palindromic string if it exists 

 

# Function to print the non-palindromic string 

# if it exists, otherwise prints -1 

def findNonPalinString(s): 

 

 freq = [0] * (26) 

 flag = 0

 

 for i in range(0, len(s)): 

 

 # If all characters are not same,

 # set flag to 1 

 if s[i] != s[0]:

 flag = 1

 

 # Update frequency of the current 

 # character 

 freq[ord(s[i]) - ord('a')] += 1

 

 # If all characters are same 

 if not flag:

 print("-1") 

 

 else:

 

 # Print characters in sorted manner 

 for i in range(0, 26): 

 for j in range(0, freq[i]): 

 print(chr(ord('a') + i),

 end = "") 

 

# Driver Code 

if __name__ == "__main__":

 

 s = "abba"

 findNonPalinString(s) 

 

# This code is contributed by

# Rituraj Jain  
  
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

// C# Program to rearrange letters

// of string to find a non-palindromic

// string if it exists 

using System;

 

class GfG 

{ 

 

 // Function to print the 

 // non-palindromic string 

 // if it exists, otherwise 

 // prints -1 

 static void findNonPalinString(char []s) 

 { 

 int []freq = new int[26]; 

 int flag = 0; 

 

 for (int i = 0; i < s.Length; i++) 

 { 

 

 // If all characters are not 

 // same, set flag to 1 

 if (s[i] != s[0]) 

 flag = 1; 

 

 // Update frequency of 

 // the current character 

 freq[s[i] - 'a']++; 

 } 

 

 // If all characters are same 

 if (flag == 0) 

 Console.WriteLine("-1"); 

 else

 { 

 

 // Print characters in sorted manner 

 for (int i = 0; i < 26; i++) 

 for (int j = 0; j < freq[i]; j++) 

 Console.Write((char)('a' + i)); 

 } 

 } 

 

 // Driver Code 

 public static void Main() 

 { 

 string s = "abba"; 

 

 findNonPalinString(s.ToCharArray()); 

 } 

} 

 

// This code is contributed by Ryuga  
  
---  
  
 __

 __

 **Output:**

    
    
    aabb
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

