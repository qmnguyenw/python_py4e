Remove characters from a numeric string such that string becomes divisible by
8



Given a non-negative integer represented in the form of a numeric string
**str**. Remove zero or more characters from the string such that the number
becomes **divisible by 8**. If it is possible, print the string after removing
the characters otherwise print **-1**.

 **Examples:**

>  **Input:** str = “3454”  
>  **Output:** 344  
> After removing ‘5’, string becomes 344 which is divisible by 8.
>
>  **Input:** str = “111”  
>  **Output:** -1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Considering the divisibility rule of 8, we just need to check
if the number formed by last 3 characters of str is divisible by 8 or not.
Thus, we can iterate over all multiples of 8 upto 1000 and check if any of the
multiple exists as a sub-sequence in the given string, then that multiple is
our required answer. Otherwise, there exists no answer since all multiples of
8 greater than 1000 also needs to have the number (formed from last 3 digits)
which has already been checked.

  

  

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to remove digits from a

// numeric string such that the number

// becomes divisible by 8

#include <bits/stdc++.h>

using namespace std;

 

// Function that return true if sub

// is a sub-sequence in s

int checkSub(string sub, string s)

{

 int j = 0;

 for (int i = 0; i < s.size(); i++)

 if (sub[j] == s[i])

 j++;

 return j == (int)sub.size();

}

 

// Function to return a multiple of 8

// formed after removing 0 or more characters

// from the given string

int getMultiple(string s)

{

 // Iterate over all multiples of 8

 for (int i = 0; i < 1e3; i += 8) {

 

 // If current multiple

 // exists as a subsequence

 // in the given string

 if (checkSub(to_string(i), s))

 return i;

 }

 

 return -1;

}

 

// Driver Code

int main()

{

 string s = "3454";

 cout << getMultiple(s);

 

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

// Java program to remove digits from a

// numeric string such that the number 

// becomes divisible by 8 

 

class GFG

{

 

 // Function that return true if sub 

 // is a sub-sequence in s 

 static boolean checkSub(String sub, String s) 

 { 

 int j = 0; 

 for (int i = 0; i < s.length(); i++) 

 if (sub.charAt(j) == s.charAt(i)) 

 j++; 

 

 return j == sub.length(); 

 } 

 

 // Function to return a multiple of 8 

 // formed after removing 0 or more characters 

 // from the given string 

 static int getMultiple(String s) 

 { 

 // Iterate over all multiples of 8 

 for (int i = 0; i < 1E3; i += 8) 

 { 

 

 // If current multiple 

 // exists as a subsequence 

 // in the given string 

 if (checkSub(Integer.toString(i), s)) 

 return i; 

 } 

 return -1; 

 } 

 

 // Driver Code 

 public static void main (String[] args) 

 {

 String s = "3454"; 

 System.out.println(getMultiple(s)); 

 }

}

 

// This code is contributed by mits  
  
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

# Python3 program to remove digits from

# a numeric string such that the number

# becomes divisible by 8

import math as mt

 

# Function that return true if sub

# is a sub-sequence in s

def checkSub(sub, s):

 

 j = 0

 for i in range(len(s)):

 if (sub[j] == s[i]):

 j += 1

 

 if j == int(len(sub)):

 return True

 else:

 return False

 

# Function to return a multiple of 8

# formed after removing 0 or more 

# characters from the given string

def getMultiple(s):

 

 # Iterate over all multiples of 8

 for i in range(0, 10**3, 8):

 

 # If current multiple

 # exists as a subsequence

 # in the given string

 if (checkSub(str(i), s)):

 return i

 

 return -1

 

# Driver Code

s = "3454"

print(getMultiple(s))

 

# This code is contributed

# by Mohit Kumar 29  
  
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

// C# program to remove digits from a

// numeric string such that the number 

// becomes divisible by 8 

using System;

 

class GFG

{

 

 // Function that return true if sub 

 // is a sub-sequence in s 

 static bool checkSub(string sub, string s) 

 { 

 int j = 0; 

 for (int i = 0; i < s.Length; i++) 

 if (sub[j] == s[i]) 

 j++; 

 

 return j == sub.Length; 

 } 

 

 // Function to return a multiple of 8 

 // formed after removing 0 or more characters 

 // from the given string 

 static int getMultiple(string s) 

 { 

 // Iterate over all multiples of 8 

 for (int i = 0; i < 1e3; i += 8) 

 { 

 

 // If current multiple 

 // exists as a subsequence 

 // in the given string 

 if (checkSub(i.ToString(), s)) 

 return i; 

 } 

 return -1; 

 } 

 

 // Driver Code 

 static void Main()

 {

 string s = "3454"; 

 Console.WriteLine(getMultiple(s)); 

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

// PHP program to remove digits from a

// numeric string such that the number

// becomes divisible by 8

 

// Function that return true if sub

// is a sub-sequence in s

function checkSub($sub, $s)

{

 $j = 0;

 for ($i = 0; $i < strlen($s); $i++)

 if ($sub[$j] == $s[$i])

 $j++;

 return $j == strlen($sub);

}

 

// Function to return a multiple of 8

// formed after removing 0 or more 

// characters from the given string

function getMultiple($s)

{

 // Iterate over all multiples of 8

 for ($i = 0; $i < 1e3; $i += 8) 

 {

 

 // If current multiple

 // exists as a subsequence

 // in the given string

 if (checkSub((string)($i), $s))

 return $i;

 }

 

 return -1;

}

 

// Driver Code

$s = "3454";

echo getMultiple($s);

 

// This code is contributed 

// by Akanksha Rai  
  
---  
  
 __

 __

 **Output:**

    
    
    344
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

