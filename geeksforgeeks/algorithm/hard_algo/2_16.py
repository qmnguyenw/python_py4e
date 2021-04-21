Check if a string is a scrambled form of another string



Given two strings **S1** and **S2** of equal length, the task is to determine
if S2 is a scrambled form of S1.  
 **Scrambled string:**  
Given string **str** , we can represent it as a binary tree by partitioning it
to two non-empty substrings recursively.  
 **Note:** Srambled string is not same as an Anagram  
Below is one possible representation of str = **“coder”** :  

    
    
        coder
       /    \
      co    der
     / \    /  \
    c   o  d   er
               / \
              e   r

To scramble the string, we may choose any non-leaf node and swap its two
children.  
Suppose, we choose the node “co” and swap its two children, it produces a
scrambled string “ocder”.  

    
    
        ocder
       /    \
      oc    der
     / \    /  \
    o   c  d   er
               / \
              e   r

Thus, **“ocder”** is a scrambled string of **“coder”**.  
Similarly, if we continue to swap the children of nodes **“der”** and **“er”**
, it produces a scrambled string **“ocred”**.  

    
    
        ocred
       /    \
      oc    red
     / \    /  \
    o   c  re  d
           / \
          r   e

Thus, **“ocred”** is a scrambled string of **“coder”**.  
 **Examples:**

>  **Input:** S1=”coder”, S2=”ocder”  
> **Output:** Yes  
> **Explanation:**  
> “ocder” is a scrambled form of “coder”  
>  **Input:** S1=”abcde”, S2=”caebd”  
> **Output:** No  
> **Explanation:**  
> “caebd” is not a scrambled form of “abcde”
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach**  
In order to solve this problem, we are using Divide and Conquer approach.  
Given two strings of equal length (say n+1), S1[0…n] and S2[0…n]. If S2 is a
scrambled form of S1, then there must exist an index i such that at least one
of the following conditions is true:  

  * S2[0…i] is a scrambled string of S1[0…i] and S2[i+1…n] is a scrambled string of S1[i+1…n].
  * S2[0…i] is a scrambled string of S1[n-i…n] and S2[i+1…n] is a scrambled string of S1[0…n-i-1].

 **Note:** An optimization step to consider here is to check beforehand if the
two strings are anagrams of each other. If not, it indicates that the strings
contain different characters and can’t be a scrambled form of each other.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to check if a

// given string is a scrambled

// form of another string

#include <bits/stdc++.h>

using namespace std;

bool isScramble(string S1, string S2)

{

 // Strings of non-equal length

 // cant' be scramble strings

 if (S1.length() != S2.length()) {

 return false;

 }

 int n = S1.length();

 // Empty strings are scramble strings

 if (n == 0) {

 return true;

 }

 // Equal strings are scramble strings

 if (S1 == S2) {

 return true;

 }

 // Check for the condition of anagram

 string copy_S1 = S1, copy_S2 = S2;

 sort(copy_S1.begin(), copy_S1.end());

 sort(copy_S2.begin(), copy_S2.end());

 if (copy_S1 != copy_S2) {

 return false;

 }

 for (int i = 1; i < n; i++) {

 // Check if S2[0...i] is a scrambled

 // string of S1[0...i] and if S2[i+1...n]

 // is a scrambled string of S1[i+1...n]

 if (isScramble(S1.substr(0, i), S2.substr(0, i))

 && isScramble(S1.substr(i, n - i),

 S2.substr(i, n - i))) {

 return true;

 }

 // Check if S2[0...i] is a scrambled

 // string of S1[n-i...n] and S2[i+1...n]

 // is a scramble string of S1[0...n-i-1]

 if (isScramble(S1.substr(0, i),

 S2.substr(n - i, i))

 && isScramble(S1.substr(i, n - i),

 S2.substr(0, n - i))) {

 return true;

 }

 }

 // If none of the above

 // conditions are satisfied

 return false;

}

// Driver Code

int main()

{

 string S1 = "coder";

 string S2 = "ocred";

 if (isScramble(S1, S2)) {

 cout << "Yes";

 }

 else {

 cout << "No";

 }

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

// Java program to check if a

// given string is a scrambled

// form of another string

import java.util.*;

class GFG{

 

static boolean isScramble(String S1,

 String S2)

{

 

 // Strings of non-equal length

 // cant' be scramble strings

 if (S1.length() != S2.length())

 {

 return false;

 }

 

 int n = S1.length();

 // Empty strings are scramble strings

 if (n == 0)

 {

 return true;

 }

 

 // Equal strings are scramble strings

 if (S1.equals(S2))

 {

 return true;

 }

 

 // Converting string to

 // character array

 char[] tempArray1 = S1.toCharArray();

 char[] tempArray2 = S2.toCharArray();

 

 // Checking condition for Anagram

 Arrays.sort(tempArray1);

 Arrays.sort(tempArray2);

 

 String copy_S1 = new String(tempArray1);

 String copy_S2 = new String(tempArray2);

 

 if (!copy_S1.equals(copy_S2))

 {

 return false;

 }

 

 for(int i = 1; i < n; i++)

 {

 

 // Check if S2[0...i] is a scrambled

 // string of S1[0...i] and if S2[i+1...n]

 // is a scrambled string of S1[i+1...n]

 if (isScramble(S1.substring(0, i),

 S2.substring(0, i)) &&

 isScramble(S1.substring(i, n),

 S2.substring(i, n)))

 {

 return true;

 }

 // Check if S2[0...i] is a scrambled

 // string of S1[n-i...n] and S2[i+1...n]

 // is a scramble string of S1[0...n-i-1]

 if (isScramble(S1.substring(n - i, n),

 S2.substring(0, i)) &&

 isScramble(S1.substring(0, n - i),

 S2.substring(i, n)))

 {

 return true;

 }

 }

 

 // If none of the above

 // conditions are satisfied

 return false;

}

// Driver Code

public static void main(String[] args)

{

 String S1 = "coder";

 String S2 = "ocred";

 

 if (isScramble(S1, S2))

 {

 System.out.println("Yes");

 }

 else

 {

 System.out.println("No");

 }

}

}

// This code is contributed by dadi madhav  
  
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

# Python3 program to check if a

# given string is a scrambled

# form of another string

def isScramble(S1: str, S2: str):

 

 # Strings of non-equal length

 # cant' be scramble strings

 if len(S1) != len(S2):

 return False

 n = len(S1)

 # Empty strings are scramble strings

 if not n:

 return True

 # Equal strings are scramble strings

 if S1 == S2:

 return True

 # Check for the condition of anagram

 if sorted(S1) != sorted(S2):

 return False

 for i in range(1, n):

 

 # Check if S2[0...i] is a scrambled

 # string of S1[0...i] and if S2[i+1...n]

 # is a scrambled string of S1[i+1...n]

 if (isScramble(S1[:i], S2[:i]) and

 isScramble(S1[i:], S2[i:])):

 return True

 # Check if S2[0...i] is a scrambled

 # string of S1[n-i...n] and S2[i+1...n]

 # is a scramble string of S1[0...n-i-1]

 if (isScramble(S1[-i:], S2[:i]) and

 isScramble(S1[:-i], S2[i:])):

 return True

 # If none of the above

 # conditions are satisfied

 return False

# Driver Code

if __name__ == "__main__":

 

 S1 = "coder"

 S2 = "ocred"

 

 if (isScramble(S1, S2)):

 print("Yes")

 else:

 print("No")

# This code is contributed by sgshah2  
  
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

// C# program to check if a

// given string is a scrambled

// form of another string

using System;

using System.Collections.Generic;

class GFG {

 

 static bool isScramble(string S1, string S2)

 {

 

 // Strings of non-equal length

 // cant' be scramble strings

 if (S1.Length != S2.Length) 

 {

 return false;

 }

 

 int n = S1.Length;

 

 // Empty strings are scramble strings

 if (n == 0) 

 {

 return true;

 }

 

 // Equal strings are scramble strings

 if (S1.Equals(S2))

 {

 return true;

 }

 

 // Converting string to 

 // character array

 char[] tempArray1 = S1.ToCharArray();

 char[] tempArray2 = S2.ToCharArray();

 

 // Checking condition for Anagram

 Array.Sort(tempArray1);

 Array.Sort(tempArray2);

 

 string copy_S1 = new string(tempArray1);

 string copy_S2 = new string(tempArray2);

 

 if (!copy_S1.Equals(copy_S2)) 

 {

 return false;

 }

 

 for(int i = 1; i < n; i++)

 {

 

 // Check if S2[0...i] is a scrambled

 // string of S1[0...i] and if S2[i+1...n]

 // is a scrambled string of S1[i+1...n]

 if (isScramble(S1.Substring(0, i), 

 S2.Substring(0, i)) && 

 isScramble(S1.Substring(i, n - i),

 S2.Substring(i, n - i)))

 {

 return true;

 }

 

 // Check if S2[0...i] is a scrambled

 // string of S1[n-i...n] and S2[i+1...n]

 // is a scramble string of S1[0...n-i-1]

 if (isScramble(S1.Substring(0, i),

 S2.Substring(n - i, i)) && 

 isScramble(S1.Substring(i, n - i),

 S2.Substring(0, n - i))) 

 {

 return true;

 }

 }

 

 // If none of the above

 // conditions are satisfied

 return false;

 }

 

 // Driver code

 static void Main()

 {

 string S1 = "coder";

 string S2 = "ocred";

 

 if (isScramble(S1, S2)) 

 {

 Console.WriteLine("Yes");

 }

 else

 {

 Console.WriteLine("No");

 }

 }

}

// This code is contributed by divyeshrabadiya07  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

