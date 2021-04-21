Lexicographically largest sub-sequence of the given string



Given a string **str** containing lowercase characters, the task is to find
the lexicographically largest sub-sequence of **str**.

 **Examples:**

>  **Input:** str = “abc”  
>  **Output:** c  
> All possible sub-sequences are “a”, “ab”, “ac”, “b”, “bc” and “c”  
> and “c” is the largest among them (lexicographically)
>
>  **Input:** str = “geeksforgeeks”  
>  **Output:** ss

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Let **mx** be the lexicographically largest character in the
string. Since we want the lexicographically largest sub-sequence we should
include all occurrences of **mx**. Now after all the occurrences have been
used, the same process can be repeated for the remaining string (i.e. sub-
string after the last occurrence of **mx** ) and so on until the there are no
more characters left.

  

  

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

 

// Function to return the lexicographically

// largest sub-sequence of s

string getSubSeq(string s, int n)

{

 string res = "";

 int cr = 0;

 while (cr < n) {

 

 // Get the max character from the string

 char mx = s[cr];

 for (int i = cr + 1; i < n; i++)

 mx = max(mx, s[i]);

 int lst = cr;

 

 // Use all the occurrences of the

 // current maximum character

 for (int i = cr; i < n; i++)

 if (s[i] == mx) {

 res += s[i];

 lst = i;

 }

 

 // Repeat the steps for the remaining string

 cr = lst + 1;

 }

 return res;

}

 

// Driver code

int main()

{

 string s = "geeksforgeeks";

 int n = s.length();

 cout << getSubSeq(s, n);

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

 

 // Function to return the lexicographically

 // largest sub-sequence of s

 static String getSubSeq(String s, int n)

 {

 String res = "";

 int cr = 0;

 while (cr < n) 

 {

 

 // Get the max character from the String

 char mx = s.charAt(cr);

 for (int i = cr + 1; i < n; i++)

 {

 mx = (char) Math.max(mx, s.charAt(i));

 }

 int lst = cr;

 

 // Use all the occurrences of the

 // current maximum character

 for (int i = cr; i < n; i++) 

 {

 if (s.charAt(i) == mx) 

 {

 res += s.charAt(i);

 lst = i;

 }

 }

 

 // Repeat the steps for 

 // the remaining String

 cr = lst + 1;

 }

 return res;

 }

 

 // Driver code

 public static void main(String[] args) 

 {

 String s = "geeksforgeeks";

 int n = s.length();

 System.out.println(getSubSeq(s, n));

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

# Python 3 implementation of the approach

 

# Function to return the lexicographically

# largest sub-sequence of s

def getSubSeq(s, n):

 res = ""

 cr = 0

 while (cr < n):

 

 # Get the max character from 

 # the string

 mx = s[cr]

 for i in range(cr + 1, n):

 mx = max(mx, s[i])

 lst = cr

 

 # Use all the occurrences of the

 # current maximum character

 for i in range(cr,n):

 if (s[i] == mx):

 res += s[i]

 lst = i

 

 # Repeat the steps for the 

 # remaining string

 cr = lst + 1

 

 return res

 

# Driver code

if __name__ == '__main__':

 s = "geeksforgeeks"

 n = len(s)

 print(getSubSeq(s, n))

 

# This code is contributed by

# Surendra_Gangwar  
  
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

 

 // Function to return the lexicographically 

 // largest sub-sequence of s 

 static String getSubSeq(String s, int n) 

 { 

 String res = ""; 

 int cr = 0; 

 while (cr < n) 

 { 

 

 // Get the max character from 

 // the String 

 char mx = s[cr]; 

 for (int i = cr + 1; i < n; i++) 

 { 

 mx = (char) Math.Max(mx, s[i]); 

 } 

 int lst = cr; 

 

 // Use all the occurrences of the 

 // current maximum character 

 for (int i = cr; i < n; i++) 

 { 

 if (s[i] == mx) 

 { 

 res += s[i]; 

 lst = i; 

 } 

 } 

 

 // Repeat the steps for 

 // the remaining String 

 cr = lst + 1; 

 } 

 return res; 

 } 

 

 // Driver code 

 public static void Main(String[] args) 

 { 

 String s = "geeksforgeeks"; 

 int n = s.Length; 

 Console.WriteLine(getSubSeq(s, n)); 

 } 

} 

 

// This code is contributed by 29AjayKumar  
  
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

// PHP implementation of the approach

 

// Function to return the lexicographically

// largest sub-sequence of s

function getSubSeq($s, $n)

{

 $res = "";

 $cr = 0;

 while ($cr < $n) 

 {

 

 // Get the max character from the string

 $mx = $s[$cr];

 for ($i = $cr + 1; $i < $n; $i++)

 $mx = max($mx, $s[$i]);

 $lst = $cr;

 

 // Use all the occurrences of the

 // current maximum character

 for ($i = $cr; $i < $n; $i++)

 if ($s[$i] == $mx) 

 {

 $res .= $s[$i];

 $lst = $i;

 }

 

 // Repeat the steps for the

 // remaining string

 $cr = $lst + 1;

 }

 return $res;

}

 

// Driver code

$s = "geeksforgeeks";

$n = strlen($s);

echo getSubSeq($s, $n);

 

// This code is contributed by 

// Akanksha Rai

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    ss
    

**Time Complexity:** O(N) where N is the length of the string.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

