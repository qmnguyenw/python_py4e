Count maximum occurrence of subsequence in string such that indices in
subsequence is in A.P.



Given a string **S** , the task is to count the maximum occurrence of
subsequence in the given string such that indices of the characters of the
subsequence are in Arithmetic Progression.

 **Examples:**

> **Input:** S = “xxxyy”  
> **Output:** 6  
> **Explanation:**  
> There is a subsequence “xy”, where indices of each character of the
> subsequence are in A.P.  
> The indices of the different characters that form the subsequence “xy” –  
> {(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)}
>
>  **Input:** S = “pop”  
> **Output:** 2  
> **Explanation:**  
> There is a subsequence “p”, where indices of each character of the
> subsequence are in A.P.  
> The indices of the different characters that form the subsequence “p” –  
> {(1), (2)}  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The key observation in the problem is if there are two
characters in a string whose collectively occurrence is greater than the
occurrence of any single character, then these characters will form the
maximum occurrence subsequence in the string with the character in Arithmetic
progression because of every two integers will always form an arithmetic
progression. Below is the illustration of the steps:

  

  

  * Iterate over the string and count the frequency of the characters of the string. That is considering the subsequences of length 1.
  * Iterate over the string and choose every two possible characters of the string and increment the frequency of the subsequence of the string.
  * Finally, find the maximum frequency of the subsequence from length 1 and 2.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// maximum occurence of the subsequence

// such that the indices of characters

// are in arithmetic progression

#include <bits/stdc++.h>

using namespace std;

// Function to find the

// maximum occurence of the subsequence

// such that the indices of characters

// are in arithmetic progression

int maximumOccurrence(string s)

{

 int n = s.length();

 // Frequencies of subsequence

 map<string, int> freq;

 // Loop to find the frequencies

 // of subsequence of length 1

 for (int i = 0; i < n; i++) {

 string temp = "";

 temp += s[i];

 freq[temp]++;

 }

 

 // Loop to find the frequencies

 // subsequence of length 2

 for (int i = 0; i < n; i++) {

 for (int j = i + 1; j < n; j++) {

 string temp = "";

 temp += s[i];

 temp += s[j];

 freq[temp]++;

 }

 }

 int answer = INT_MIN;

 // Finding maximum frequency

 for (auto it : freq)

 answer = max(answer, it.second);

 return answer;

}

// Driver Code

int main()

{

 string s = "xxxyy";

 cout << maximumOccurrence(s);

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

// Java implementation to find the

// maximum occurence of the subsequence

// such that the indices of characters

// are in arithmetic progression

import java.util.*;

class GFG

{

 // Function to find the

 // maximum occurence of the subsequence

 // such that the indices of characters

 // are in arithmetic progression

 static int maximumOccurrence(String s)

 {

 int n = s.length();

 

 // Frequencies of subsequence

 HashMap<String, Integer> freq = new HashMap<String,Integer>();

 int i, j;

 // Loop to find the frequencies

 // of subsequence of length 1

 for ( i = 0; i < n; i++) {

 String temp = "";

 temp += s.charAt(i);

 if (freq.containsKey(temp)){

 freq.put(temp,freq.get(temp)+1);

 }

 else{

 freq.put(temp, 1);

 }

 }

 

 // Loop to find the frequencies

 // subsequence of length 2

 for (i = 0; i < n; i++) {

 for (j = i + 1; j < n; j++) {

 String temp = "";

 temp += s.charAt(i);

 temp += s.charAt(j);

 if(freq.containsKey(temp))

 freq.put(temp,freq.get(temp)+1);

 else

 freq.put(temp,1);

 }

 }

 int answer = Integer.MIN_VALUE;

 

 // Finding maximum frequency

 for (int it : freq.values())

 answer = Math.max(answer, it);

 return answer;

 }

 

 // Driver Code

 public static void main(String []args)

 {

 String s = "xxxyy";

 

 System.out.print(maximumOccurrence(s));

 }

}

// This code is contributed by chitranayal  
  
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

# Python3 implementation to find the

# maximum occurence of the subsequence

# such that the indices of characters

# are in arithmetic progression

# Function to find the

# maximum occurence of the subsequence

# such that the indices of characters

# are in arithmetic progression

def maximumOccurrence(s):

 n = len(s)

 # Frequencies of subsequence

 freq = {}

 # Loop to find the frequencies

 # of subsequence of length 1

 for i in s:

 temp = ""

 temp += i

 freq[temp] = freq.get(temp, 0) + 1

 # Loop to find the frequencies

 # subsequence of length 2

 for i in range(n):

 for j in range(i + 1, n):

 temp = ""

 temp += s[i]

 temp += s[j]

 freq[temp] = freq.get(temp, 0) + 1

 answer = -10**9

 # Finding maximum frequency

 for it in freq:

 answer = max(answer, freq[it])

 return answer

# Driver Code

if __name__ == '__main__':

 s = "xxxyy"

 print(maximumOccurrence(s))

# This code is contributed by mohit kumar 29  
  
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

// C# implementation to find the

// maximum occurence of the subsequence

// such that the indices of characters

// are in arithmetic progression

using System;

using System.Collections.Generic;

class GFG

{

// Function to find the

// maximum occurence of the subsequence

// such that the indices of characters

// are in arithmetic progression

static int maximumOccurrence(string s)

{

 int n = s.Length;

 // Frequencies of subsequence

 Dictionary<string,

 int> freq = new Dictionary<string,

 int>();

 int i, j;

 // Loop to find the frequencies

 // of subsequence of length 1

 for ( i = 0; i < n; i++)

 {

 string temp = "";

 temp += s[i];

 if (freq.ContainsKey(temp))

 {

 freq[temp]++;

 }

 else

 {

 freq[temp] = 1;

 }

 }

 // Loop to find the frequencies

 // subsequence of length 2

 for (i = 0; i < n; i++)

 {

 for (j = i + 1; j < n; j++)

 {

 string temp = "";

 temp += s[i];

 temp += s[j];

 if(freq.ContainsKey(temp))

 freq[temp]++;

 else

 freq[temp] = 1;

 }

 }

 int answer =int.MinValue;

 // Finding maximum frequency

 foreach(KeyValuePair<string,

 int> it in freq)

 answer = Math.Max(answer, it.Value);

 return answer;

}

 

// Driver Code

public static void Main(string []args)

{

 string s = "xxxyy";

 Console.Write(maximumOccurrence(s));

}

}

// This code is contributed by Rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    
    
    
    
    

**Time Complexity:** O(N2)

 **Efficient Approach:** The idea is to use the dynamic programming paradigm
to compute the frequency of the subsequences of length 1 and 2 in the string.
Below is the illustration of the steps:

  * Compute the frequency of the characters of the string in a frequency array.
  * For subsequences of the string of length 2, the DP state will be

    
    
    dp[i][j] = Total number of times ith
      character occured before jth character.
    
    
    

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// maximum occurence of the subsequence

// such that the indices of characters

// are in arithmetic progression

#include <bits/stdc++.h>

using namespace std;

// Function to find the

// maximum occurence of the subsequence

// such that the indices of characters

// are in arithmetic progression

int maximumOccurrence(string s)

{

 int n = s.length();

 // Frequency for characters

 int freq[26] = { 0 };

 int dp[26][26] = { 0 };

 

 // Loop to count the occurence

 // of ith character before jth

 // character in the given string

 for (int i = 0; i < n; i++) {

 int c = (s[i] - 'a');

 for (int j = 0; j < 26; j++)

 dp[j] += freq[j];

 // Increase the frequency

 // of s[i] or c of string

 freq++;

 }

 int answer = INT_MIN;

 

 // Maximum occurence of subsequence

 // of length 1 in given string

 for (int i = 0; i < 26; i++)

 answer = max(answer, freq[i]);

 

 // Maximum occurence of subsequence

 // of length 2 in given string

 for (int i = 0; i < 26; i++) {

 for (int j = 0; j < 26; j++) {

 answer = max(answer, dp[i][j]);

 }

 }

 return answer;

}

// Driver Code

int main()

{

 string s = "xxxyy";

 cout << maximumOccurrence(s);

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

// Java implementation to find the

// maximum occurence of the subsequence

// such that the indices of characters

// are in arithmetic progression

class GFG{

 

// Function to find the

// maximum occurence of the subsequence

// such that the indices of characters

// are in arithmetic progression

static int maximumOccurrence(String s)

{

 int n = s.length();

 

 // Frequency for characters

 int freq[] = new int[26];

 int dp[][] = new int[26][26];

 

 // Loop to count the occurence

 // of ith character before jth

 // character in the given String

 for (int i = 0; i < n; i++) {

 int c = (s.charAt(i) - 'a');

 

 for (int j = 0; j < 26; j++)

 dp[j] += freq[j];

 

 // Increase the frequency

 // of s[i] or c of String

 freq++;

 }

 

 int answer = Integer.MIN_VALUE;

 

 // Maximum occurence of subsequence

 // of length 1 in given String

 for (int i = 0; i < 26; i++)

 answer = Math.max(answer, freq[i]);

 

 // Maximum occurence of subsequence

 // of length 2 in given String

 for (int i = 0; i < 26; i++) {

 for (int j = 0; j < 26; j++) {

 answer = Math.max(answer, dp[i][j]);

 }

 }

 

 return answer;

}

 

// Driver Code

public static void main(String[] args)

{

 String s = "xxxyy";

 

 System.out.print(maximumOccurrence(s));

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

# Python3 implementation to find the

# maximum occurence of the subsequence

# such that the indices of characters

# are in arithmetic progression

import sys

# Function to find the maximum occurence

# of the subsequence such that the

# indices of characters are in

# arithmetic progression

def maximumOccurrence(s):

 

 n = len(s)

 # Frequency for characters

 freq = [0] * (26)

 dp = [[0 for i in range(26)]

 for j in range(26)]

 # Loop to count the occurence

 # of ith character before jth

 # character in the given String

 for i in range(n):

 c = (ord(s[i]) - ord('a'))

 for j in range(26):

 dp[j] += freq[j]

 # Increase the frequency

 # of s[i] or c of String

 freq += 1

 answer = -sys.maxsize

 # Maximum occurence of subsequence

 # of length 1 in given String

 for i in range(26):

 answer = max(answer, freq[i])

 # Maximum occurence of subsequence

 # of length 2 in given String

 for i in range(26):

 for j in range(26):

 answer = max(answer, dp[i][j])

 return answer

# Driver Code

if __name__ == '__main__':

 

 s = "xxxyy"

 print(maximumOccurrence(s))

# This code is contributed by Princi Singh  
  
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

// C# implementation to find the

// maximum occurence of the subsequence

// such that the indices of characters

// are in arithmetic progression

using System;

class GFG{

 

// Function to find the maximum

// occurence of the subsequence

// such that the indices of characters

// are in arithmetic progression

static int maximumOccurrence(string s)

{

 int n = s.Length;

 

 // Frequency for characters

 int []freq = new int[26];

 int [,]dp = new int[26, 26];

 

 // Loop to count the occurence

 // of ith character before jth

 // character in the given String

 for(int i = 0; i < n; i++)

 {

 int x = (s[i] - 'a');

 

 for(int j = 0; j < 26; j++)

 dp[x, j] += freq[j];

 

 // Increase the frequency

 // of s[i] or c of String

 freq[x]++;

 }

 

 int answer = int.MinValue;

 

 // Maximum occurence of subsequence

 // of length 1 in given String

 for(int i = 0; i < 26; i++)

 answer = Math.Max(answer, freq[i]);

 

 // Maximum occurence of subsequence

 // of length 2 in given String

 for(int i = 0; i < 26; i++)

 {

 for(int j = 0; j < 26; j++)

 {

 answer = Math.Max(answer, dp[i, j]);

 }

 }

 return answer;

}

 

// Driver Code

public static void Main(string[] args)

{

 string s = "xxxyy";

 

 Console.Write(maximumOccurrence(s));

}

}

// This code is contributed by Yash_R  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    
    
    
    
    

**Time complexity:** O(26 * N)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

