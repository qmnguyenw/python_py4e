Longest palindromic string formed by concatenation of prefix and suffix of a
string



Given string **str** , the task is to find the longest palindromic substring
formed by the concatenation of the prefix and suffix of the given string
**str**.  
 **Examples:**  

> **Input:** str = “rombobinnimor”  
> **Output:** rominnimor  
> **Explanation:**  
> The concatenation of string “rombob”(prefix) and “mor”(suffix) is
> “rombobmor” which is a palindromic string.  
> The concatenation of string “rom”(prefix) and “innimor”(suffix) is
> “rominnimor” which is a palindromic string.  
> But the length of “rominnimor” is greater than “rombobmor”.  
> Therefore, “rominnimor” is the required string.  
>  **Input:** str = “geekinakeeg”  
> **Output:** geekakeeg  
> **Explanation:**  
> The concatenation of string “geek”(prefix) and “akeeg”(suffix) is
> “geekakeeg” which is a palindromic string.  
> The concatenation of string “geeki”(prefix) and “keeg”(suffix) is
> “geekigeek” which is a palindromic string.  
> But the length of “geekakeeg” is equals to “geekikeeg”.  
> Therefore, any of the above string is the required string.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to use KMP Algorithm to find the longest proper
prefix which is a palindrome of the suffix of the given string str in O(N)
time.

  1. Find the longest prefix(say **s[0, l]** ) which is also a palindrome of the suffix(say **s[n-l, n-1]** ) of the string str. Prefix and Suffix don’t overlap.
  2. Out of the remaining substring( **s[l+1, n-l-1]** ), find the longest palindromic substring(say **ans** ) which is either a suffix or prefix of the remaining string.
  3. The concatenation of **s[0, l]** , **ans** and **s[n-l, n-l-1]** is the longest palindromic substring.

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

// Function used to calculate the longest prefix

// which is also a suffix

int kmp(string s)

{

 vector<int> lps(s.size(), 0);

 // Traverse the string

 for (int i = 1; i < s.size(); i++) {

 int previous_index = lps[i - 1];

 while (previous_index > 0

 && s[i] != s[previous_index]) {

 previous_index = lps[previous_index - 1];

 }

 // Update the lps size

 lps[i] = previous_index

 + (s[i] == s[previous_index] ? 1 : 0);

 }

 // Returns size of lps

 return lps[lps.size() - 1];

}

// Function to calculate the length of longest

// palindromic substring whcih is either a

// suffix or prefix

int remainingStringLongestPallindrome(string s)

{

 // Append a character to separate the string

 // and reverse of the string

 string t = s + "?";

 // Reverse the string

 reverse(s.begin(), s.end());

 // Append the reversed string

 t += s;

 return kmp(t);

}

// Function to find the Longest palindromic

// string formed from concatenation of prefix

// and suffix of a given string

string longestPrefixSuffixPallindrome(string s)

{

 int length = 0;

 int n = s.size();

 // Calculating the length for which prefix

 // is reverse of suffix

 for (int i = 0, j = n - 1; i < j; i++, j--) {

 if (s[i] != s[j]) {

 break;

 }

 length++;

 }

 // Append prefix to the answer

 string ans = s.substr(0, length);

 

 // Store the remaining string

 string remaining = s.substr(length,

 (n - (2 * length)));

 

 // If the remaining string is not empty

 // that means that there can be a palindrome

 // substring which can be added between the

 // suffix & prefix

 if (remaining.size()) {

 // Calculate the length of longest prefix

 // palindromic substring

 int longest_prefix

 = remainingStringLongestPallindrome(remaining);

 // Reverse the given string to find the

 // longest palindromic suffix

 reverse(remaining.begin(), remaining.end());

 

 // Calculate the length of longest prefix

 // palindromic substring

 int longest_suffix

 = remainingStringLongestPallindrome(remaining);

 // If the prefix palindrome is greater

 // than the suffix palindrome

 if (longest_prefix > longest_suffix) {

 reverse(remaining.begin(), remaining.end());

 // Append the prefix to the answer

 ans += remaining.substr(0, longest_prefix);

 }

 // If the suffix palindrome is greter than

 // the prefix palindrome

 else {

 // Append the suffix to the answer

 ans += remaining.substr(0, longest_suffix);

 }

 }

 // Finally append the suffix to the answer

 ans += s.substr(n - length, length);

 // Return the answer string

 return ans;

}

// Driver Code

int main()

{

 string str = "rombobinnimor";

 cout << longestPrefixSuffixPallindrome(str)

 << endl;

}  
  
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

# Python3 implementation of

# the above approach

# Function used to calculate

# the longest prefix

# which is also a suffix

def kmp(s):

 lps = [0] * (len(s))

 # Traverse the string

 for i in range (1 , len(s)):

 previous_index = lps[i - 1]

 while (previous_index > 0 and

 s[i] != s[previous_index]):

 previous_index = lps[previous_index - 1]

 

 # Update the lps size

 lps[i] = previous_index

 if (s[i] == s[previous_index]):

 lps[i] += 1

 # Returns size of lps

 return lps[- 1]

# Function to calculate the length of

# longest palindromic substring which

# is either a suffix or prefix

def remainingStringLongestPallindrome(s):

 # Append a character to separate

 # the string and reverse of the string

 t = s + "?"

 # Reverse the string

 s = s[: : -1]

 # Append the reversed string

 t += s

 return kmp(t)

# Function to find the Longest

# palindromic string formed from

# concatenation of prefix

# and suffix of a given string

def longestPrefixSuffixPallindrome(s):

 length = 0

 n = len(s)

 # Calculating the length

 # for which prefix

 # is reverse of suffix

 i = 0

 j = n - 1

 while i < j:

 if (s[i] != s[j]):

 break

 i += 1

 j -= 1

 

 length += 1

 # Append prefix to the answer

 ans = s[0 : length]

 # Store the remaining string

 remaining = s[length : length + (n - (2 * length))]

 # If the remaining string is not empty

 # that means that there can be a palindrome

 # substring which can be added between the

 # suffix & prefix

 if (len(remaining)):

 # Calculate the length of longest prefix

 # palindromic substring

 longest_prefix = remainingStringLongestPallindrome(remaining);

 # Reverse the given string to find the

 # longest palindromic suffix

 remaining = remaining[: : -1]

 # Calculate the length of longest prefix

 # palindromic substring

 longest_suffix = remainingStringLongestPallindrome(remaining);

 # If the prefix palindrome is greater

 # than the suffix palindrome

 if (longest_prefix > longest_suffix):

 remaining = remaining[: : -1]

 # Append the prefix to the answer

 ans += remaining[0 : longest_prefix]

 

 # If the suffix palindrome is

 # greter than the prefix palindrome

 else:

 # Append the suffix to the answer

 ans += remaining[0 : longest_suffix]

 

 # Finally append the suffix to the answer

 ans += s[n - length : n]

 # Return the answer string

 return ans

# Driver Code

if __name__ == "__main__": 

 st = "rombobinnimor"

 print (longestPrefixSuffixPallindrome(st))

 

# This code is contributed by Chitranayal  
  
---  
  
 __

 __

 **Output:**

    
    
    rominnimor
    
    
    
    

**Time Complexity:** O(N), where N is the length of the given string.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

