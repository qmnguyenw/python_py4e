Find lexicographically smallest string in at most one swaps



Given a string **str** of length **N**. The task is to find out the
lexicographically smallest string when at most only one swap is allowed. That
is, two indices **1 <= i, j <= n** can be chosen and swapped. This operation
can be performed at most one time.

 **Examples:**

>  **Input:** str = “string”  
>  **Output:** gtrins  
>  **Explanation:**  
>  Choose i=1, j=6, string becomes – gtrins. This is lexicographically
> smallest strings that can be formed.
>
>  **Input:** str = “zyxw”  
>  **Output:** wyxz

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use sorting and compute the smallest
lexicographical string possible for the given string. After computing the
sorted string, find the first unmatched character from the given string and
replace it with the last occurrence of the unmatched character in the sorted
string.

  

  

For example, let str = “geeks” and the sorted = “eegks”. First unmatched
character is in the first place. This character has to swapped such that this
character matches the character with sorted string. Resulting lexicographical
smallest string. On replacing “g” with the last occurring “e”, the string
becomes eegks which is lexicographically smallest.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the lexicographically

// smallest string that can be formed by

// swapping at most one character.

// The characters might not necessarily

// be adjacent.

string findSmallest(string s)

{

 int len = s.size();

 

 // Store last occurrence of every character

 int loccur[26];

 

 // Set -1 as default for every character.

 memset(loccur, -1, sizeof(loccur));

 

 for (int i = len - 1; i >= 0; --i) {

 

 // Character index to fill

 // in the last occurrence array

 int chI = s[i] - 'a';

 if (loccur[chI] == -1) {

 

 // If this is true then this

 // character is being visited

 // for the first time from the last

 // Thus last occurrence of this

 // character is stored in this index

 loccur[chI] = i;

 }

 }

 

 string sorted_s = s;

 sort(sorted_s.begin(), sorted_s.end());

 

 for (int i = 0; i < len; ++i) {

 if (s[i] != sorted_s[i]) {

 

 // Character to replace

 int chI = sorted_s[i] - 'a';

 

 // Find the last occurrence

 // of this character.

 int last_occ = loccur[chI];

 

 // Swap this with the last occurrence

 swap(s[i], s[last_occ]);

 break;

 }

 }

 

 return s;

}

 

// Driver code

int main()

{

 string s = "geeks";

 cout << findSmallest(s);

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

import java.util.*;

 

class GFG{

 

// Function to return the lexicographically

// smallest String that can be formed by

// swapping at most one character.

// The characters might not necessarily

// be adjacent.

static String findSmallest(char []s)

{

 int len = s.length;

 

 // Store last occurrence of every character

 int []loccur = new int[26];

 

 // Set -1 as default for every character.

 Arrays.fill(loccur, -1);

 

 for (int i = len - 1; i >= 0; --i) {

 

 // Character index to fill

 // in the last occurrence array

 int chI = s[i] - 'a';

 if (loccur[chI] == -1) {

 

 // If this is true then this

 // character is being visited

 // for the first time from the last

 // Thus last occurrence of this

 // character is stored in this index

 loccur[chI] = i;

 }

 }

 

 char []sorted_s = s;

 Arrays.sort(sorted_s);

 

 for (int i = 0; i < len; ++i) {

 if (s[i] != sorted_s[i]) {

 

 // Character to replace

 int chI = sorted_s[i] - 'a';

 

 // Find the last occurrence

 // of this character.

 int last_occ = loccur[chI];

 

 // Swap this with the last occurrence

 char temp = s[last_occ];

 s[last_occ] = s[i];

 s[i] = temp;

 break;

 }

 }

 

 return String.valueOf(s);

}

 

// Driver code

public static void main(String[] args)

{

 String s = "geeks";

 System.out.print(findSmallest(s.toCharArray()));

}

}

 

// This code is contributed by 29AjayKumar  
  
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

# Python3 implementation of the above approach

 

# Function to return the lexicographically 

# smallest string that can be formed by 

# swapping at most one character. 

# The characters might not necessarily 

# be adjacent. 

def findSmallest(s) : 

 

 length = len(s); 

 

 # Store last occurrence of every character 

 # Set -1 as default for every character.

 loccur = [-1]*26; 

 

 

 for i in range(length - 1, -1, -1) : 

 

 # Character index to fill 

 # in the last occurrence array 

 chI = ord(s[i]) - ord('a'); 

 if (loccur[chI] == -1) :

 

 # If this is true then this 

 # character is being visited 

 # for the first time from the last 

 # Thus last occurrence of this 

 # character is stored in this index 

 loccur[chI] = i; 

 

 sorted_s = s; 

 sorted_s.sort();

 

 for i in range(length) :

 if (s[i] != sorted_s[i]) :

 

 # Character to replace 

 chI = ord(sorted_s[i]) - ord('a'); 

 

 # Find the last occurrence 

 # of this character. 

 last_occ = loccur[chI]; 

 

 # Swap this with the last occurrence 

 # swap(s[i], s[last_occ]); 

 s[i],s[last_occ] = s[last_occ],s[i]

 break; 

 

 return "".join(s); 

 

# Driver code 

if __name__ == "__main__" : 

 

 s = "geeks"; 

 

 print(findSmallest(list(s))); 

 

# This code is contributed by Yash_R  
  
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

 

class GFG{

 

// Function to return the lexicographically

// smallest String that can be formed by

// swapping at most one character.

// The characters might not necessarily

// be adjacent.

static String findSmallest(char []s)

{

 int len = s.Length;

 

 // Store last occurrence of every character

 int []loccur = new int[26];

 

 // Set -1 as default for every character.

 for (int i = 0; i < 26; i++)

 loccur[i] = -1;

 

 for (int i = len - 1; i >= 0; --i) {

 

 // char index to fill

 // in the last occurrence array

 int chI = s[i] - 'a';

 if (loccur[chI] == -1) {

 

 // If this is true then this

 // character is being visited

 // for the first time from the last

 // Thus last occurrence of this

 // character is stored in this index

 loccur[chI] = i;

 }

 }

 

 char []sorted_s = s;

 Array.Sort(sorted_s);

 

 for (int i = 0; i < len; ++i) {

 if (s[i] != sorted_s[i]) {

 

 // char to replace

 int chI = sorted_s[i] - 'a';

 

 // Find the last occurrence

 // of this character.

 int last_occ = loccur[chI];

 

 // Swap this with the last occurrence

 char temp = s[last_occ];

 s[last_occ] = s[i];

 s[i] = temp;

 break;

 }

 }

 

 return String.Join("", s);

}

 

// Driver code

public static void Main(String[] args)

{

 String s = "geeks";

 Console.Write(findSmallest(s.ToCharArray()));

}

}

 

// This code is contributed by sapnasingh4991  
  
---  
  
 __

 __

 **Output:**

    
    
    eegks
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

