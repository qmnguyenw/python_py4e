Count of ways to split given string into two non-empty palindromes



Given a string **S** , the task is to find the number of ways to split the
given string **S** into two non-empty palindromic strings.  
 **Examples:**

>  **Input:** S = “aaaaa”  
> **Output:** 4  
> **Explanation:**  
> Possible Splits: {“a”, “aaaa”}, {“aa”, “aaa”}, {“aaa”, “aa”}, {“aaaa”, “a”}  
>  **Input:** S = “abacc”  
> **Output:** 1  
> **Explanation:**  
> Only possible split is “aba”, “cc”.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The naive approach is to split the string at each
possible index and check if both the substrings are palindromic or not. If yes
then increment the **count** for that index. Print the final **count**.  
Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to implement

// the above approach

#include<bits/stdc++.h>

using namespace std;

// Function to check whether the

// substring from l to r is

// palindrome or not

bool isPalindrome(int l, int r,

 string& s)

{

 while (l <= r) {

 // If characters at l and

 // r differ

 if (s[l] != s[r])

 // Not a palindrome

 return false;

 l++;

 r--;

 }

 // If the string is

 // a palindrome

 return true;

}

// Function to count and return

// the number of possible splits

int numWays(string& s)

{

 int n = s.length();

 // Stores the count

 // of splits

 int ans = 0;

 for (int i = 0;

 i < n - 1; i++) {

 // Check if the two substrings

 // after the split are

 // palindromic or not

 if (isPalindrome(0, i, s)

 && isPalindrome(i + 1,

 n - 1, s)) {

 // If both are palindromes

 ans++;

 }

 }

 // Print the final count

 return ans;

}

// Driver Code

int main()

{

 string S = "aaaaa";

 cout << numWays(S);

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

// Java program to implement

// the above approach

class GFG{

 

// Function to check whether the

// substring from l to r is

// palindrome or not

public static boolean isPalindrome(int l, int r,

 String s)

{

 while (l <= r)

 {

 

 // If characters at l and

 // r differ

 if (s.charAt(l) != s.charAt(r))

 

 // Not a palindrome

 return false;

 

 l++;

 r--;

 }

 // If the string is

 // a palindrome

 return true;

}

// Function to count and return

// the number of possible splits

public static int numWays(String s)

{

 int n = s.length();

 // Stores the count

 // of splits

 int ans = 0;

 for(int i = 0; i < n - 1; i++)

 {

 

 // Check if the two substrings

 // after the split are

 // palindromic or not

 if (isPalindrome(0, i, s) &&

 isPalindrome(i + 1, n - 1, s))

 {

 

 // If both are palindromes

 ans++;

 }

 }

 

 // Print the final count

 return ans;

}

// Driver Code

public static void main(String args[])

{

 String S = "aaaaa";

 System.out.println(numWays(S));

}

}

// This code is contributed by SoumikMondal  
  
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

# Python3 program to implement

# the above approach

# Function to check whether the

# substring from l to r is

# palindrome or not

def isPalindrome(l, r, s):

 while (l <= r):

 

 # If characters at l and

 # r differ

 if (s[l] != s[r]):

 

 # Not a palindrome

 return bool(False)

 

 l += 1

 r -= 1

 # If the string is

 # a palindrome

 return bool(True)

# Function to count and return

# the number of possible splits

def numWays(s):

 

 n = len(s)

 # Stores the count

 # of splits

 ans = 0

 for i in range(n - 1):

 

 # Check if the two substrings

 # after the split are

 # palindromic or not

 if (isPalindrome(0, i, s) and

 isPalindrome(i + 1, n - 1, s)):

 

 # If both are palindromes

 ans += 1

 

 # Print the final count

 return ans

# Driver Code

S = "aaaaa"

print(numWays(S))

# This code is contributed by divyeshrabadiya07  
  
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

class GFG{

 

// Function to check whether the

// substring from l to r is

// palindrome or not

public static bool isPalindrome(int l, int r,

 string s)

{

 while (l <= r)

 {

 

 // If characters at l and

 // r differ

 if (s[l] != s[r])

 

 // Not a palindrome

 return false;

 

 l++;

 r--;

 }

 

 // If the string is

 // a palindrome

 return true;

}

 

// Function to count and return

// the number of possible splits

public static int numWays(string s)

{

 int n = s.Length;

 

 // Stores the count

 // of splits

 int ans = 0;

 for(int i = 0; i < n - 1; i++)

 {

 

 // Check if the two substrings

 // after the split are

 // palindromic or not

 if (isPalindrome(0, i, s) &&

 isPalindrome(i + 1, n - 1, s))

 {

 

 // If both are palindromes

 ans++;

 }

 }

 

 // Print the final count

 return ans;

}

 

// Driver Code

public static void Main(string []args)

{

 string S = "aaaaa";

 

 Console.Write(numWays(S));

}

}

// This code is contributed by Rutvik  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

 // Javascript program to implement

 // the above approach 

 

 // Function to check whether the

 // substring from l to r is

 // palindrome or not

 function isPalindrome(l, r, s)

 {

 while (l <= r)

 {

 // If characters at l and

 // r differ

 if (s[l] != s[r])

 // Not a palindrome

 return false;

 l++;

 r--;

 }

 // If the string is

 // a palindrome

 return true;

 }

 // Function to count and return

 // the number of possible splits

 function numWays(s)

 {

 let n = s.length;

 // Stores the count

 // of splits

 let ans = 0;

 for(let i = 0; i < n - 1; i++)

 {

 // Check if the two substrings

 // after the split are

 // palindromic or not

 if (isPalindrome(0, i, s) && 

 isPalindrome(i + 1, n - 1, s))

 {

 // If both are palindromes

 ans++;

 }

 }

 // Print the final count

 return ans;

 }

 

 let S = "aaaaa";

 

 document.write(numWays(S));

</script>  
  
---  
  
 __

 __

  

**Output:**

  

  

    
    
    4

