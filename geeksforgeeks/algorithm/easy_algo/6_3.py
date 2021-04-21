Minimum K such that every substring of length atleast K contains a character c



Given a string S containing lowercase latin letters. A character c is called
K-amazing if every substring of S with length atleast K contains this
character c. Find the minimum possible K such that there exists atleast one
K-amazing character.

 **Examples:**

>  **Input :** S = “abcde”  
>  **Output :** 3  
>  **Explanation :** Every substring of length atleast 3 contains character
> ‘c’, i.e.  
> {“abc”, “bcd”, “cde”, “abcd”, “bcde”, “abcde”}
>
>  **Input :** S = “aaaa”  
>  **Output :** 1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Prerequisites :**Binary Search

  

  

 **Naive Solution :** A simple approach is to iterate over all possible
lengths of substrings i.e. from 1 to N (size of string) and for every current
length substrings check whether some character appears in all of those
substrings.

 **Efficient Solution :** The key idea is to perform binary search over the
answer **K** , since if some character c appears in all substrings of length
**X** , it will always appear in all substrings of length **(X + 1)**. Hence,
we can check for the current length and try to minimise it using divide and
conquer algorithm. For checking if some character appears in all substrings of
length X, iterate over all characters from ‘a’ to ‘z’ and inside another loop
iteratively store the last occurrence of the last character.  
Let the current position be j, so the last substring of length X will be from
(j – X) to X. Check if the position of last occurrence of current K-amazing
character is greater than (j – X) or not. If it is greater, then that
substring is a valid string.

Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP Program to find minimum K such that

// every substring of length atleast K

// contains some character c

#include <bits/stdc++.h>

using namespace std;

 

// This function checks if there exists some

// character which appears in all K length

// substrings

int check(string s, int K)

{

 // Iterate over all possible characters

 for (int ch = 0; ch < 26; ch++) {

 char c = 'a' + ch;

 

 // stores the last occurrence

 int last = -1;

 

 // set answer as true;

 bool found = true;

 for (int i = 0; i < K; i++)

 if (s[i] == c)

 last = i;

 

 // No occurrence found of current

 // character in first substring

 // of length K

 if (last == -1)

 continue;

 

 // Check for every last substring

 // of length K where last occurr-

 // ence exists in substring

 for (int i = K; i < s.size(); i++) {

 if (s[i] == c)

 last = i;

 

 // If last occ is not

 // present in substring

 if (last <= (i - K)) {

 found = false;

 break;

 }

 }

 // current character is K amazing

 if (found)

 return 1;

 }

 return 0;

}

 

// This function performs binary search over the

// answer to minimise it

int binarySearch(string s)

{

 int low = 1, high = (int)s.size();

 int ans;

 while (low <= high) {

 int mid = (high + low) >> 1;

 

 // Check if answer is found try

 // to minimise it

 if (check(s, mid)) {

 ans = mid;

 high = mid - 1;

 }

 else

 low = mid + 1;

 }

 return ans;

}

 

// Driver Code to test above functions

int32_t main()

{

 string s = "abcde";

 cout << binarySearch(s) << endl;

 

 s = "aaaa";

 cout << binarySearch(s) << endl;

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

// Java Program to find minimum K such that

// every substring of length atleast K

// contains some character c

 

class GFG

{

 

 

 // This function checks if there exists some

 // character which appears in all K length

 // substrings

 static int check(String s, int K)

 {

 // Iterate over all possible characters

 for (int ch = 0; ch < 26; ch++) {

 char c = (char)( 'a' + ch);

 

 // stores the last occurrence

 int last = -1;

 

 // set answer as true;

 boolean found = true;

 for (int i = 0; i < K; i++)

 if (s.charAt(i) == c)

 last = i;

 

 // No occurrence found of current

 // character in first substring

 // of length K

 if (last == -1)

 continue;

 

 // Check for every last substring

 // of length K where last occurr-

 // ence exists in substring

 for (int i = K; i < s.length(); i++) {

 if (s.charAt(i) == c)

 last = i;

 

 // If last occ is not

 // present in substring

 if (last <= (i - K)) {

 found = false;

 break;

 }

 }

 // current character is K amazing

 if (found)

 return 1;

 }

 return 0;

 }

 

 // This function performs binary search over the

 // answer to minimise it

 static int binarySearch(String s)

 {

 int low = 1, high = s.length();

 int ans=0;

 while (low <= high) {

 int mid = (high + low) >> 1;

 

 // Check if answer is found try

 // to minimise it

 if (check(s, mid)==1) {

 ans = mid;

 high = mid - 1;

 }

 else

 low = mid + 1;

 }

 return ans;

 }

 

 // Driver Code to test above functions

 public static void main(String args[])

 {

 String s = "abcde";

 System.out.println(binarySearch(s));

 

 s = "aaaa";

 System.out.println(binarySearch(s));

 

 }

 

}

 

// This article is contributed 

// by ihritik  
  
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

# Python3 Program to find minimum K such

# that every substring of length atleast 

# K contains some character c 

 

# This function checks if there exists 

# some character which appears in all 

# K length substrings 

def check(s, K): 

 

 # Iterate over all possible characters 

 for ch in range(0, 26): 

 c = chr(97 + ch) # Ascii value of 'a' => 97

 

 # stores the last occurrence 

 last = -1

 

 # set answer as true 

 found = True

 for i in range(0, K): 

 if s[i] == c: 

 last = i 

 

 # No occurrence found of current character 

 # in first substring of length K 

 if last == -1: 

 continue

 

 # Check for every last substring 

 # of length K where last occurr- 

 # ence exists in substring 

 for i in range(K, len(s)):

 if s[i] == c: 

 last = i 

 

 # If last occ is not 

 # present in substring 

 if last <= (i - K): 

 found = False

 break

 

 # current character is K amazing 

 if found: 

 return 1

 

 return 0

 

# This function performs binary search 

# over the answer to minimise it 

def binarySearch(s): 

 

 low, high, ans = 1, len(s), None

 

 while low <= high: 

 mid = (high + low) >> 1

 

 # Check if answer is found 

 # try to minimise it 

 if check(s, mid): 

 ans, high = mid, mid - 1

 

 else:

 low = mid + 1

 

 return ans 

 

# Driver Code

if __name__ == "__main__": 

 

 s = "abcde"

 print(binarySearch(s)) 

 

 s = "aaaa"

 print(binarySearch(s)) 

 

# This code is contributed by Rituraj Jain  
  
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

// C# Program to find minimum K such that

// every substring of length atleast K

// contains some character c

 

using System;

class GFG

{

 

 

 // This function checks if there exists some

 // character which appears in all K length

 // substrings

 static int check(String s, int K)

 {

 // Iterate over all possible characters

 for (int ch = 0; ch < 26; ch++) {

 char c = (char)( 'a' + ch);

 

 // stores the last occurrence

 int last = -1;

 

 // set answer as true;

 bool found = true;

 for (int i = 0; i < K; i++)

 if (s[i] == c)

 last = i;

 

 // No occurrence found of current

 // character in first substring

 // of length K

 if (last == -1)

 continue;

 

 // Check for every last substring

 // of length K where last occurr-

 // ence exists in substring

 for (int i = K; i < s.Length; i++) {

 if (s[i] == c)

 last = i;

 

 // If last occ is not

 // present in substring

 if (last <= (i - K)) {

 found = false;

 break;

 }

 }

 // current character is K amazing

 if (found)

 return 1;

 }

 return 0;

 }

 

 // This function performs binary search over the

 // answer to minimise it

 static int binarySearch(String s)

 {

 int low = 1, high = s.Length;

 int ans=0;

 while (low <= high) {

 int mid = (high + low) >> 1;

 

 // Check if answer is found try

 // to minimise it

 if (check(s, mid)==1) {

 ans = mid;

 high = mid - 1;

 }

 else

 low = mid + 1;

 }

 return ans;

 }

 

 // Driver Code to test above functions

 public static void Main()

 {

 String s = "abcde";

 Console.WriteLine(binarySearch(s));

 

 s = "aaaa";

 Console.WriteLine(binarySearch(s));

 

 }

 

}

 

// This article is contributed 

// by ihritik  
  
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

// Php Program to find minimum K such that 

// every substring of length atleast K 

// contains some character c 

 

// This function checks if there exists some 

// character which appears in all K length 

// substrings 

function check($s, $K) 

{ 

 // Iterate over all possible characters 

 for ($ch = 0; $ch < 26; $ch++) 

 { 

 $c = chr(ord('a') + $ch) ; 

 

 // stores the last occurrence 

 $last = -1; 

 

 // set answer as true; 

 $found = true; 

 for ($i = 0; $i < $K; $i++) 

 if ($s[$i] == $c) 

 $last = $i; 

 

 // No occurrence found of current 

 // character in first substring 

 // of length K 

 if ($last == -1) 

 continue; 

 

 // Check for every last substring 

 // of length K where last occurr- 

 // ence exists in substring 

 for ($i = $K; $i < strlen($s); $i++) 

 { 

 if ($s[$i] == $c) 

 $last = $i; 

 

 // If last occ is not 

 // present in substring 

 if ($last <= ($i - $K))

 { 

 $found = false; 

 break; 

 } 

 } 

 

 // current character is K amazing 

 if ($found) 

 return 1; 

 } 

 return 0; 

} 

 

// This function performs binary search 

// over the answer to minimise it 

function binarySearch($s) 

{ 

 $low = 1 ;

 $high = strlen($s) ; 

 while ($low <= $high) 

 { 

 $mid = ($high + $low) >> 1; 

 

 // Check if answer is found try 

 // to minimise it 

 if (check($s, $mid))

 { 

 $ans = $mid; 

 $high = $mid - 1; 

 } 

 else

 $low = $mid + 1; 

 } 

 return $ans; 

} 

 

// Driver Code

$s = "abcde"; 

echo binarySearch($s) . "\n";

 

$s = "aaaa"; 

echo binarySearch($s) . "\n"; 

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    1
    

**Time Complexity :** O(N * logN * 26), where N is the size of the given
string.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

