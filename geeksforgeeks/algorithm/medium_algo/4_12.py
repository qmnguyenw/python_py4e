Generate a string of size N whose each substring of size M has exactly K
distinct characters



Given 3 positive integers **N** , **M** , and **K**. the task is to construct
a string of length **N** consisting of lowercase letters such that each
substring of length **M** having exactly **K** distinct letters.  
 **Examples:**

> **Input:** N = 5, M = 2, K = 2  
> **Output:** abade  
> **Explanation:**  
> Each substring of size 2 “ab”, “ba”, “ad”, “de” have 2 distinct letters.  
>  **Input:** N = 7, M = 5, K = 3  
> **Output:** abcaaab  
> **Explanation:**  
> Each substring of size 5 “tleel”, “leelt”, “eelte” have 3 distinct letters.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** In a string of size N, every substring of size M must contain
exactly K distinct letters-

  * Construct a string having K distinct alphabets starting from ‘a’ to ‘z’ up to the size of M and put the rest of letters like ‘a’..
  * Since we have generated a string of size M with K distinct value. Now, keep repeating it till we reach string size of N.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to generate a string of size N

// whose each substring of size M

// has exactly K distinct characters

#include <bits/stdc++.h>

using namespace std;

// Function to generate the string

string generateString(int N, int M, int K)

{

 // Declare empty string

 string s = "";

 // counter for M

 int cnt1 = 0;

 // counter for K

 int cnt2 = 0;

 // Loop to generate string size of N

 for (int i = 0; i < N; i++) {

 cnt1++;

 cnt2++;

 // Generating K distinct

 // letters one by one

 if (cnt1 <= M) {

 if (cnt2 <= K) {

 s = s + char(96 + cnt1);

 }

 // After generating b distinct letters,

 // append rest a-b letters as 'a'

 else {

 s = s + 'a';

 }

 }

 // Reset the counter value

 // and repeat the process

 else {

 cnt1 = 1;

 cnt2 = 1;

 s = s + 'a';

 }

 }

 // return final result string

 return s;

}

// Driver code

int main()

{

 int N = 7, M = 5, K = 3;

 cout << generateString(N, M, K) << endl;

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

// Java program to generate a String of size N

// whose each subString of size M

// has exactly K distinct characters

import java.util.*;

class GFG{

// Function to generate the String

static String generateString(int N, int M, int K)

{

 // Declare empty String

 String s = "";

 // counter for M

 int cnt1 = 0;

 // counter for K

 int cnt2 = 0;

 // Loop to generate String size of N

 for (int i = 0; i < N; i++)

 {

 cnt1++;

 cnt2++;

 // Generating K distinct

 // letters one by one

 if (cnt1 <= M)

 {

 if (cnt2 <= K)

 {

 s = s + (char)(96 + cnt1);

 }

 // After generating b distinct letters,

 // append rest a-b letters as 'a'

 else

 {

 s = s + 'a';

 }

 }

 // Reset the counter value

 // and repeat the process

 else

 {

 cnt1 = 1;

 cnt2 = 1;

 s = s + 'a';

 }

 }

 // return final result String

 return s;

}

// Driver code

public static void main(String[] args)

{

 int N = 7, M = 5, K = 3;

 System.out.println(generateString(N, M, K));

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

# Python3 program to generate a string of size N

# whose each substring of size M

# has exactly K distinct characters

# Function to generate the string

def generateString(N, M, K):

 # Declare empty string

 s = ""

 # counter for M

 cnt1 = 0

 # counter for K

 cnt2 = 0

 # Loop to generate string size of N

 for i in range (N):

 cnt1 += 1

 cnt2 += 1

 # Generating K distinct

 # letters one by one

 if (cnt1 <= M):

 if (cnt2 <= K):

 s = s + chr(96 + cnt1)

 

 # After generating b distinct letters,

 # append rest a-b letters as 'a'

 else:

 s = s + 'a'

 # Reset the counter value

 # and repeat the process

 else:

 cnt1 = 1

 cnt2 = 1

 s = s + 'a'

 # return final result string

 return s

# Driver code

if __name__ == "__main__": 

 N = 7

 M = 5

 K = 3

 print (generateString(N, M, K))

 

# This code is contributed by Chitranayal  
  
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

// C# program to generate a String of

// size N whose each subString of size

// M has exactly K distinct characters

using System;

class GFG{

// Function to generate the String

static String generateString(int N, int M, int K)

{

 // Declare empty String

 String s = "";

 // Counter for M

 int cnt1 = 0;

 // Counter for K

 int cnt2 = 0;

 // Loop to generate String size of N

 for(int i = 0; i < N; i++)

 {

 cnt1++;

 cnt2++;

 

 // Generating K distinct

 // letters one by one

 if (cnt1 <= M)

 {

 if (cnt2 <= K)

 {

 s = s + (char)(96 + cnt1);

 }

 

 // After generating b distinct letters,

 // append rest a-b letters as 'a'

 else

 {

 s = s + 'a';

 }

 }

 

 // Reset the counter value

 // and repeat the process

 else

 {

 cnt1 = 1;

 cnt2 = 1;

 s = s + 'a';

 }

 }

 

 // Return readonly result String

 return s;

}

// Driver code

public static void Main(String[] args)

{

 int N = 7, M = 5, K = 3;

 Console.WriteLine(generateString(N, M, K));

}

}

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    abcaaab
    
    
    
    

_**Time complexity:** O(N) _  
_**Space complexity:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

