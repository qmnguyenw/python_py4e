Find the lexicographically largest palindromic Subsequence of a String



Given a string ![S](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f322ff29bb70c49d154ec39a209a61ca_l3.png). The task is to
find the lexicographically largest subsequence of the string which is a
palindrome.

 **Examples:**

    
    
    **Input :** str = "abrakadabra"
    **Output :** rr
    
    **Input :** str = "geeksforgeeks"
    **Output :** ss
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The idea is to observe a character **a** is said to be lexicographically
larger than a character **b** if it’s ASCII value is greater than that of
**b**.

Since the string has to be palindromic, the string should contain the largest
characters only, as if we place any other smaller character in between the
first and last character then it will make the string lexicographically
smaller.

To find the lexicographically largest subsequence, first find the largest
characters in the given string and append all of its occurrences in the
original string to form the resultant subsequence string.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to find the largest

// palindromic subsequence

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the largest

// palindromic subsequence

string largestPalinSub(string s)

{

 string res;

 

 char mx = s[0];

 

 // Find the largest character

 for (int i = 1; i < s.length(); i++)

 mx = max(mx, s[i]);

 

 // Append all occurrences of largest character

 // to the resultant string

 for (int i = 0; i < s.length(); i++)

 if (s[i] == mx)

 res += s[i];

 

 return res;

}

 

// Driver Code

int main()

{

 string s = "geeksforgeeks";

 

 cout << largestPalinSub(s);

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

// Java program to find the largest

// palindromic subsequence 

class GFG

{

 

// Function to find the largest 

// palindromic subsequence 

static String largestPalinSub(String s) 

{ 

 String res = ""; 

 char mx = s.charAt(0); 

 

 // Find the largest character 

 for (int i = 1; i < s.length(); i++) 

 mx = (char)Math.max((int)mx, 

 (int)s.charAt(i)); 

 

 // Append all occurrences of largest 

 // character to the resultant string 

 for (int i = 0; i < s.length(); i++) 

 if (s.charAt(i) == mx) 

 res += s.charAt(i); 

 

 return res; 

} 

 

// Driver Code

public static void main(String []args)

{

 String s = "geeksforgeeks"; 

 System.out.println(largestPalinSub(s));

}

}

 

// This code is contributed by

// Rituraj Jain  
  
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

# Python3 program to find the largest

# palindromic subsequence 

 

# Function to find the largest 

# palindromic subsequence 

def largestPalinSub(s): 

 

 res = "" 

 mx = s[0] 

 

 # Find the largest character 

 for i in range(1, len(s)): 

 mx = max(mx, s[i]) 

 

 # Append all occurrences of largest 

 # character to the resultant string 

 for i in range(0, len(s)): 

 if s[i] == mx: 

 res += s[i] 

 

 return res 

 

# Driver Code 

if __name__ == "__main__":

 

 s = "geeksforgeeks"

 print(largestPalinSub(s)) 

 

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

// C# program to find the largest

// palindromic subsequence 

using System;

 

class GFG

{

 

 // Function to find the largest 

 // palindromic subsequence 

 static string largestPalinSub(string s) 

 { 

 string res = ""; 

 char mx = s[0]; 

 

 // Find the largest character 

 for (int i = 1; i < s.Length; i++) 

 mx = (char)Math.Max((int)mx, 

 (int)s[i]); 

 

 // Append all occurrences of largest 

 // character to the resultant string 

 for (int i = 0; i < s.Length; i++) 

 if (s[i] == mx) 

 res += s[i]; 

 

 return res; 

 } 

 

 // Driver Code

 public static void Main()

 {

 string s = "geeksforgeeks"; 

 Console.WriteLine(largestPalinSub(s));

 }

}

 

// This code is contributed by Ryuga  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

 

// PHP program to find the largest

// palindromic subsequence

 

// Function to find the largest

// palindromic subsequence

function largestPalinSub($s)

{

 $res="";

 

 $mx = $s[0];

 

 // Find the largest character

 for ($i = 1; $i < strlen($s); $i++)

 {

 $mx = max($mx, $s[$i]);

 

 }

 

 // Append all occurrences of largest character

 // to the resultant string

 for ($i = 0; $i < strlen($s); $i++)

 {

 if ($s[$i] == $mx)

 {

 $res.=$s[$i];

 }

 }

 

 return $res;

}

 

// Driver Code

$s = "geeksforgeeks";

echo(largestPalinSub($s));

 

// This code is contributed by princiraj1992

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    ss
    

**Time Complexity:** O(N), where N is the length of the string.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

