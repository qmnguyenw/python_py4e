Find index i such that prefix of S1 and suffix of S2 till i form a palindrome
when concatenated



Given two strings **A** and **B** of equal lengths, the task is to find an
index **i** such that **A[0…i]** and **B[i+1…n-1]** give a palindrome when
concatenated together. If it is not possible to find such an index then print
**-1**.

 **Examples:**

>  **Input:** S1 = “abcdf”, S2 = “sfgba”  
>  **Output:** 1  
> S1[0..1] = “ab”, S2[2..n-1] = “gba”  
> S1 + S2 = “abgba” which is a palindrome.
>
>  **Input :** S1 = “abcda”, S2 = “bacbs”  
>  **Output:** -1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Simple Approach:**

  

  

  * Iterate from **0** to **n** (length of the string) and copy **i th** character from **S1** to another string let’s say **S**.
  * Now take another temporary string **Temp** and copy the characters of **S2** from index **i +1** to **n**.
  * Now check whether the string **(S + Temp)** is palindrome or not.

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

 

// Function that returns true if s is palindrome

bool isPalindrome(string s)

{

 int i = 0;

 int j = s.length() - 1;

 

 while (i < j) {

 if (s[i] != s[j])

 return false;

 i++;

 j--;

 }

 

 return true;

}

 

// Function to return the required index

int getIndex(string S1, string S2, int n)

{

 

 string S = "";

 

 for (int i = 0; i < n; i++) {

 

 // Copy the ith character in S

 S = S + S1[i];

 string Temp = "";

 

 // Copy all the character of string s2 in Temp

 for (int j = i + 1; j < n; j++)

 Temp += S2[j];

 

 // Check whether the string is palindrome

 if (isPalindrome(S + Temp)) {

 return i;

 }

 }

 

 return -1;

}

 

// Driver code

int main()

{

 string S1 = "abcdf", S2 = "sfgba";

 int n = S1.length();

 

 cout << getIndex(S1, S2, n);

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

class GFG

{

 

// Function that returns true if s is palindrome

static boolean isPalindrome(String s)

{

 int i = 0;

 int j = s.length() - 1;

 

 while (i < j) 

 {

 if (s.charAt(i) != s.charAt(j))

 return false;

 i++;

 j--;

 }

 

 return true;

}

 

// Function to return the required index

static int getIndex(String S1, String S2, int n)

{

 

 String S = "";

 

 for (int i = 0; i < n; i++)

 {

 

 // Copy the ith character in S

 S = S + S1.charAt(i);

 String Temp = "";

 

 // Copy all the character of string

 // s2 in Temp

 for (int j = i + 1; j < n; j++)

 Temp += S2.charAt(j);

 

 // Check whether the string is palindrome

 if (isPalindrome(S + Temp)) 

 {

 return i;

 }

 }

 

 return -1;

}

 

// Driver code

public static void main(String[] args)

{

 String S1 = "abcdf", S2 = "sfgba";

 int n = S1.length();

 

 System.out.println(getIndex(S1, S2, n));

}

}

 

// This code is contributed by Code_Mech.  
  
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

 

# Function that returns true if s is palindrome

def isPalindrome(s):

 i = 0;

 j = len(s) - 1;

 

 while (i < j):

 if (s[i] is not s[j]):

 return False;

 i += 1;

 j -= 1;

 

 return True;

 

# Function to return the required index

def getIndex(S1, S2, n):

 

 S = "";

 

 for i in range(n):

 

 # Copy the ith character in S

 S = S + S1[i];

 Temp = "";

 

 # Copy all the character of string s2 in Temp

 for j in range(i + 1, n):

 Temp += S2[j];

 

 # Check whether the string is palindrome

 if (isPalindrome(S + Temp)):

 return i;

 

 return -1;

 

# Driver code

S1 = "abcdf"; S2 = "sfgba";

n = len(S1);

 

print(getIndex(S1, S2, n));

 

# This code is contributed by Rajput-Ji  
  
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

 

// Function that returns true if

// s is palindrome

static bool isPalindrome(string s)

{

 int i = 0;

 int j = s.Length - 1;

 

 while (i < j) 

 {

 if (s[i] != s[j])

 return false;

 i++;

 j--;

 }

 

 return true;

}

 

// Function to return the required index

static int getIndex(string S1, 

 string S2, int n)

{

 string S = "";

 

 for (int i = 0; i < n; i++)

 {

 

 // Copy the ith character in S

 S = S + S1[i];

 string Temp = "";

 

 // Copy all the character of string

 // s2 in Temp

 for (int j = i + 1; j < n; j++)

 Temp += S2[j];

 

 // Check whether the string

 // is palindrome

 if (isPalindrome(S + Temp)) 

 {

 return i;

 }

 }

 

 return -1;

}

 

// Driver code

public static void Main()

{

 string S1 = "abcdf", S2 = "sfgba";

 int n = S1.Length;

 

 Console.WriteLine(getIndex(S1, S2, n));

}

}

 

// This code is contributed by Code_Mech.  
  
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

 

// Function that returns true if s 

// is palindrome

function isPalindrome($s)

{

 $i = 0;

 $j = strlen($s) - 1;

 

 while ($i < $j) 

 {

 if ($s[$i] != $s[$j])

 return false;

 $i++;

 $j--;

 }

 

 return true;

}

 

// Function to return the required index

function getIndex($S1, $S2, $n)

{

 $S = "";

 

 for ($i = 0; $i < $n; $i++)

 {

 

 // Copy the ith character in S

 $S = $S . $S1[$i];

 $Temp = "";

 

 // Copy all the character of string

 // s2 in Temp

 for ($j = $i + 1; $j < $n; $j++)

 $Temp .= $S2[$j];

 

 // Check whether the string is palindrome

 if (isPalindrome($S . $Temp)) 

 {

 return $i;

 }

 }

 

 return -1;

}

 

// Driver code

$S1 = "abcdf"; $S2 = "sfgba";

$n = strlen($S1);

 

echo getIndex($S1, $S2, $n);

 

// This code is contributed 

// by Akanksha Rai

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

**Time complexity:** O(n2)

 **Efficient Approach** : The efficient approach will be to observe that the
concatenated string will be palindrome if the first character of first string
matches with the last character of second string as we are considering prefix
of first string and suffix of second string.

  * Start iterating the first string from start using a pointer say **i** and second string from end using a pointer say **j** until **i < j** and **s1[i] == s2[j]**.
  * Check if both of the pointers i and j are equal at first mismatch.
  * If yes, then return index i, that is we can concatenates strings **s1[0..i]** and **s2[j..N]** to form a palindrome.
  * Otherwise, check if either **s1[i..j]** or **s2[i..j]** is a palindrome. If yes, then we can still concatenate either **s1[0..j] + s2[j+1, N-1]** or **s1[0..i-1] + s2[i..N-1]** to form a palindrome.
  * Else, return -1.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to implement the

// above approach

 

#include <bits/stdc++.h>

using namespace std;

 

// Function that returns true if the sub-string

// starting from index i and ending at index j

// is a palindrome

bool isPalindrome(string s, int i, int j)

{

 while (i < j) {

 if (s[i] != s[j])

 return false;

 i++;

 j--;

 }

 return true;

}

 

// Function to get the required index

int getIndex(string s1, string s2, int len)

{

 int i = 0, j = len - 1;

 

 // Start comparing the two strings

 // from both ends.

 while (i < j) {

 // Break from the loop at first mismatch

 if (s1[i] != s2[j]) {

 break;

 }

 

 i++;

 j--;

 }

 

 // If it is possible to concatenate

 // the strings to form palindrome,

 // return index

 if (i == j) {

 return i - 1;

 }

 

 // If remaining part for s2

 // is palindrome

 else if (isPalindrome(s2, i, j))

 return i - 1;

 

 // If remaining part for s1

 // is palindrome

 else if (isPalindrome(s1, i, j))

 return j;

 

 // If not possible, return -1

 return -1;

}

 

// Driver Code

int main()

{

 string s1 = "abcdf", s2 = "sfgba";

 int len = s1.length();

 

 cout << getIndex(s1, s2, len);

 

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

// Java implementation of the above approach

class GFG

{

 

// Function that returns true if the sub-String 

// starting from index i and ending at index j 

// is a palindrome 

static boolean isPalindrome(String s, int i, int j) 

{ 

 while (i < j) 

 { 

 if (s.charAt(i) != s.charAt(j)) 

 return false; 

 i++; 

 j--; 

 } 

 return true; 

} 

 

// Function to get the required index 

static int getIndex(String s1, String s2, int len) 

{ 

 int i = 0, j = len - 1; 

 

 // Start comparing the two Strings 

 // from both ends. 

 while (i < j) 

 { 

 // Break from the loop at first mismatch 

 if (s1.charAt(i) != s2.charAt(j))

 { 

 break; 

 } 

 

 i++; 

 j--; 

 } 

 

 // If it is possible to concatenate 

 // the Strings to form palindrome, 

 // return index 

 if (i == j) 

 { 

 return i - 1; 

 } 

 

 // If remaining part for s2 

 // is palindrome 

 else if (isPalindrome(s2, i, j)) 

 return i - 1; 

 

 // If remaining part for s1 

 // is palindrome 

 else if (isPalindrome(s1, i, j)) 

 return j; 

 

 // If not possible, return -1 

 return -1; 

} 

 

// Driver Code 

public static void main(String args[])

{ 

 String s1 = "abcdf", s2 = "sfgba"; 

 int len = s1.length(); 

 

 System.out.println( getIndex(s1, s2, len)); 

 

} 

} 

 

// This code is contributed by Arnab Kundu  
  
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

# Python3 program to implement the

# above approach 

 

# Function that returns true if the sub-string 

# starting from index i and ending at index j 

# is a palindrome 

def isPalindrome(s, i, j) : 

 

 while (i < j) :

 

 if (s[i] != s[j]) :

 return False; 

 

 i += 1; 

 j -= 1; 

 

 return True; 

 

# Function to get the required index 

def getIndex(s1, s2, length) :

 

 i = 0 ; j = length - 1; 

 

 # Start comparing the two strings 

 # from both ends. 

 while (i < j) :

 

 # Break from the loop at first mismatch 

 if (s1[i] != s2[j]) :

 break; 

 

 i += 1; 

 j -= 1; 

 

 # If it is possible to concatenate 

 # the strings to form palindrome, 

 # return index 

 if (i == j) :

 return i - 1; 

 

 # If remaining part for s2 

 # is palindrome 

 elif (isPalindrome(s2, i, j)) :

 return i - 1; 

 

 # If remaining part for s1 

 # is palindrome 

 elif (isPalindrome(s1, i, j)) :

 return j; 

 

 # If not possible, return -1 

 return -1; 

 

# Driver Code 

if __name__ == "__main__" :

 

 s1 = "abcdf" ;

 s2 = "sfgba"; 

 length = len(s1) ; 

 

 print(getIndex(s1, s2, length)); 

 

# This code is contributed by Ryuga  
  
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

// C# implementation of the above approach

using System;

 

class GFG

{

 

// Function that returns true if the sub-String 

// starting from index i and ending at index j 

// is a palindrome 

static bool isPalindrome(string s, 

 int i, int j) 

{ 

 while (i < j) 

 { 

 if (s[i] != s[j]) 

 

 return false; 

 i++; 

 j--; 

 } 

 return true; 

} 

 

// Function to get the required index 

static int getIndex(string s1, string s2, int len) 

{ 

 int i = 0, j = len - 1; 

 

 // Start comparing the two Strings 

 // from both ends. 

 while (i < j) 

 { 

 // Break from the loop at first 

 // mismatch 

 if (s1[i] != s2[j])

 { 

 break; 

 } 

 

 i++; 

 j--; 

 } 

 

 // If it is possible to concatenate 

 // the Strings to form palindrome, 

 // return index 

 if (i == j) 

 { 

 return i - 1; 

 } 

 

 // If remaining part for s2 

 // is palindrome 

 else if (isPalindrome(s2, i, j)) 

 return i - 1; 

 

 // If remaining part for s1 

 // is palindrome 

 else if (isPalindrome(s1, i, j)) 

 return j; 

 

 // If not possible, return -1 

 return -1; 

} 

 

// Driver Code 

public static void Main()

{ 

 string s1 = "abcdf", s2 = "sfgba"; 

 int len = s1.Length; 

 

 Console.WriteLine(getIndex(s1, s2, len)); 

 

} 

} 

 

// This code is contributed by Code_Mech.  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

**Time Complexity** : O(N), where N is the length of the string.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

