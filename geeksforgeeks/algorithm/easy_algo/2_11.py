Count ways to partition a string such that both parts have equal distinct
characters



Given a string **S** , the task is to count the number of ways to partition
the string into two non-empty parts such that both the parts have the same
number of distinct characters.

 **Examples:**

>  **Input:** S = “aaaa”  
>  **Output:** 3  
>  **Explanation:**  
>  There can be three ways to partition the string –  
> {{a, aaa}, {aa, aa}, {aaa, a}}
>
>  **Input:** S = “ababa”  
>  **Output:** 2  
>  **Explanation:**  
>  There can be two ways to partition the string –  
> {{ab, aba}, {aba, ba}}

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** The idea is to choose the every possible partition point
of the string and for each partition compute the distinct characters in the
partitioned string. If the count of distinct characters in both the
partitioned string is equal then increment the number of ways by 1.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to count the

// number of ways to partition the 

// string such that each partition 

// have same number of distinct 

// characters in the string

 

#include <bits/stdc++.h>

 

using namespace std;

 

// Function to count the distinct

// characters in the string

int distinctChars(string s)

{

 // Frequency of each character

 int freq[26] = { 0 };

 int count = 0;

 

 // Loop to count the frequency

 // of each character of the string

 for (int i = 0; i < s.length(); i++)

 freq[s[i] - 'a']++;

 

 // If frequency is greater than 0

 // then the character occured

 for (int i = 0; i < 26; i++) {

 if (freq[i] > 0)

 count++;

 }

 

 return count;

}

 

// Function to count the number 

// of ways to partition the string

// such that each partition have 

// same number of distinct character

int waysToSplit(string s)

{

 int n = s.length();

 int answer = 0;

 

 // Loop to choose the partition

 // index for the string

 for (int i = 1; i < n; i++) {

 

 // Divide in two parts

 string left = s.substr(0, i);

 string right = s.substr(i, n - i);

 

 // Check whether number of distinct

 // characters are equal

 if (distinctChars(left) == 

 distinctChars(right))

 answer++;

 }

 return answer;

}

 

// Driver Code

int main()

{

 string s = "ababa";

 

 cout << waysToSplit(s);

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

// Java implementation to count the

// number of ways to partition the 

// String such that each partition 

// have same number of distinct 

// characters in the String

class GFG{

 

// Function to count the distinct

// characters in the String

static int distinctChars(String s)

{

 // Frequency of each character

 int freq[] = new int[26];

 int count = 0;

 

 // Loop to count the frequency

 // of each character of the String

 for (int i = 0; i < s.length(); i++)

 freq[s.charAt(i) - 'a']++;

 

 // If frequency is greater than 0

 // then the character occured

 for (int i = 0; i < 26; i++) {

 if (freq[i] > 0)

 count++;

 }

 

 return count;

}

 

// Function to count the number 

// of ways to partition the String

// such that each partition have 

// same number of distinct character

static int waysToSplit(String s)

{

 int n = s.length();

 int answer = 0;

 

 // Loop to choose the partition

 // index for the String

 for (int i = 1; i < n; i++) {

 

 // Divide in two parts

 String left = s.substring(0, i);

 String right = s.substring(i, n);

 

 // Check whether number of distinct

 // characters are equal

 if (distinctChars(left) == 

 distinctChars(right))

 answer++;

 }

 return answer;

}

 

// Driver Code

public static void main(String[] args)

{

 String s = "ababa";

 

 System.out.print(waysToSplit(s));

}

}

 

// This code is contributed by sapnasingh4991  
  
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

# Python3 implementation to count the

# number of ways to partition the 

# string such that each partition 

# have same number of distinct 

# characters in the string 

 

# Function to count the distinct 

# characters in the string 

def distinctChars(s) : 

 

 # Frequency of each character 

 freq = [0]*26; 

 count = 0; 

 

 # Loop to count the frequency 

 # of each character of the string 

 for i in range(len(s)) : 

 freq[ord(s[i]) - ord('a')] += 1; 

 

 # If frequency is greater than 0 

 # then the character occured 

 for i in range(26) :

 if (freq[i] > 0) :

 count += 1; 

 

 return count; 

 

# Function to count the number 

# of ways to partition the string 

# such that each partition have 

# same number of distinct character 

def waysToSplit(s) : 

 n = len(s); 

 answer = 0; 

 

 # Loop to choose the partition 

 # index for the string 

 for i in range(1, n) :

 

 # Divide in two parts 

 left = s[0 : i]; 

 right = s[i : n ]; 

 

 # Check whether number of distinct 

 # characters are equal 

 if (distinctChars(left) == distinctChars(right)) :

 answer += 1; 

 

 return answer; 

 

# Driver Code 

if __name__ == "__main__" : 

 

 s = "ababa"; 

 

 print(waysToSplit(s)); 

 

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

// C# implementation to count the

// number of ways to partition the 

// String such that each partition 

// have same number of distinct 

// characters in the String

using System;

 

class GFG{

 

// Function to count the distinct

// characters in the String

static int distinctChars(string s)

{

 // Frequency of each character

 int []freq = new int[26];

 int count = 0;

 

 // Loop to count the frequency

 // of each character of the String

 for (int i = 0; i < s.Length; i++)

 freq[s[i] - 'a']++;

 

 // If frequency is greater than 0

 // then the character occured

 for (int i = 0; i < 26; i++) {

 if (freq[i] > 0)

 count++;

 }

 

 return count;

}

 

// Function to count the number 

// of ways to partition the String

// such that each partition have 

// same number of distinct character

static int waysToSplit(string s)

{

 int n = s.Length;

 int answer = 0;

 

 // Loop to choose the partition

 // index for the String

 for (int i = 1; i < n; i++) {

 

 // Divide in two parts

 string left = s.Substring(0, i);

 string right = s.Substring(i, n-i);

 

 // Check whether number of distinct

 // characters are equal

 if (distinctChars(left) == 

 distinctChars(right))

 answer++;

 }

 return answer;

}

 

// Driver Code

public static void Main(string[] args)

{

 string s = "ababa";

 

 Console.WriteLine(waysToSplit(s));

}

}

 

// This code is contributed by Yash_R  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

**Time complexity:** O(N2)  
 **Auxiliary Space:** O(26)

 **Efficient Approach:** The idea is to precompute the distinct character for
every possible substring with the help of hash-map for visited characters and
Prefix and suffix sum arrays for the distinct characters from start to current
index of the string. Below is the illustration of the steps:

  * Traverse the string for each possible indices and compute the count of distinct characters from start to that index.
    * If the current index character is visited for the first time, then increment the count of the distinct characters from the previous index by 1.
        
        
        if (visited[s[i]] == False)
            prefix[i] = prefix[i-1] + 1
        

    * If the current index character is visited earlier, then count of distinct characters from starting index to current index will be equal to last index distinct characters. That is –
        
        
        if (visited[s[i]] == True)
            prefix[i] = prefix[i-1]
        

  * Finally, Traverse the string and for each index count of distinct characters for each partitioned string can be calculated as –
    
    
    Count in left partitioned string 
        = prefix[i]
    
    Count in right partitioned string
        = prefix[L] - prefix[i+1] 
    

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to count the

// number of ways to partition the 

// string such that each partition 

// have same number of distinct 

// characters in the string

 

#include <bits/stdc++.h>

 

using namespace std;

 

// Function to count the number 

// of ways to partition the string

// such that each partition have 

// same number of distinct character

int waysToSplit(string s)

{

 int n = s.length();

 int answer = 0;

 

 // Prefix and suffix array for 

 // distinct character from 

 // start and end

 int prefix[n] = { 0 };

 int suffix[n] = { 0 };

 

 // To check whether a character 

 // has appeared till ith index

 int seen[26] = { 0 };

 

 // Calculating prefix array

 for (int i = 0; i < n; i++) {

 

 int prev = (i - 1 >= 0 ? 

 prefix[i - 1] : 0);

 

 // Character appears for 

 // the first time in string

 if (seen[s[i] - 'a'] == 0) {

 prefix[i] += (prev + 1);

 }

 else

 prefix[i] = prev;

 

 // Character is visited

 seen[s[i] - 'a'] = 1;

 }

 

 // Resetting seen for 

 // suffix calculation

 memset(seen, 0, sizeof(seen));

 

 // Calculating the suffix array

 suffix[n - 1] = 0;

 for (int i = n - 1; i >= 1; i--) {

 int prev = suffix[i];

 

 // Character appears 

 // for the first time

 if (seen[s[i] - 'a'] == 0) {

 suffix[i - 1] += (prev + 1);

 }

 else

 suffix[i - 1] = prev;

 

 // This character 

 // has now appeared

 seen[s[i] - 'a'] = 1;

 }

 

 // Loop to calculate the number

 // partition points in the string

 for (int i = 0; i < n; i++) {

 // Check whether number of 

 // distinct characters are equal

 if (prefix[i] == suffix[i])

 answer++;

 }

 return answer;

}

 

// Driver Code

int main()

{

 string s = "ababa";

 

 cout << waysToSplit(s);

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

// Java implementation to count the

// number of ways to partition the 

// string such that each partition 

// have same number of distinct 

// characters in the string 

class GFG {

 

 // Function to count the number 

 // of ways to partition the string 

 // such that each partition have 

 // same number of distinct character 

 static int waysToSplit(String s) 

 { 

 int n = s.length(); 

 int answer = 0; 

 

 // Prefix and suffix array for 

 // distinct character from 

 // start and end 

 int prefix[] = new int[n] ; 

 int suffix[] = new int[n]; 

 

 // To check whether a character 

 // has appeared till ith index 

 int seen[] = new int[26];

 

 // Calculating prefix array 

 for (int i = 0; i < n; i++) { 

 

 int prev = (i - 1 >= 0 ? 

 prefix[i - 1] : 0); 

 

 // Character appears for 

 // the first time in string 

 if (seen[s.charAt(i) - 'a'] == 0) { 

 prefix[i] += (prev + 1); 

 } 

 else

 prefix[i] = prev; 

 

 // Character is visited 

 seen[s.charAt(i)- 'a'] = 1; 

 } 

 

 // Resetting seen for 

 // suffix calculation 

 for(int i = 0; i <26; i++)

 seen[i] = 0;

 

 // Calculating the suffix array 

 suffix[n - 1] = 0; 

 for (int i = n - 1; i >= 1; i--) { 

 int prev = suffix[i]; 

 

 // Character appears 

 // for the first time 

 if (seen[s.charAt(i) - 'a'] == 0) { 

 suffix[i - 1] += (prev + 1); 

 } 

 else

 suffix[i - 1] = prev; 

 

 // This character 

 // has now appeared 

 seen[s.charAt(i)- 'a'] = 1; 

 } 

 

 // Loop to calculate the number 

 // partition points in the string 

 for (int i = 0; i < n; i++) {

 

 // Check whether number of 

 // distinct characters are equal 

 if (prefix[i] == suffix[i]) 

 answer++; 

 } 

 return answer; 

 } 

 

 // Driver Code 

 public static void main (String[] args)

 { 

 String s = "ababa"; 

 

 System.out.println(waysToSplit(s)); 

 } 

 

}

 

// This code is contributed by Yash_R  
  
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

# Python3 implementation to count the

# number of ways to partition the 

# string such that each partition 

# have same number of distinct 

# characters in the string 

 

# Function to count the number 

# of ways to partition the string 

# such that each partition have 

# same number of distinct character 

def waysToSplit(s) : 

 

 n = len(s);

 answer = 0; 

 

 # Prefix and suffix array for 

 # distinct character from 

 # start and end 

 prefix = [ 0 ]*n; 

 suffix = [0 ]*n; 

 

 # To check whether a character 

 # has appeared till ith index 

 seen = [ 0 ]*26; 

 

 # Calculating prefix array 

 for i in range(n) :

 

 prev = prefix[i - 1] if (i - 1 >= 0 ) else
0; 

 

 # Character appears for 

 # the first time in string 

 if (seen[ord(s[i]) - ord('a')] == 0) :

 prefix[i] += (prev + 1); 

 

 else :

 prefix[i] = prev; 

 

 # Character is visited 

 seen[ord(s[i]) - ord('a')] = 1; 

 

 # Resetting seen for 

 # suffix calculation 

 seen = [0]*len(seen); 

 

 # Calculating the suffix array 

 suffix[n - 1] = 0; 

 for i in range(n - 1, 0, -1) :

 prev = suffix[i]; 

 

 # Character appears 

 # for the first time 

 if (seen[ord(s[i]) - ord('a')] == 0) :

 suffix[i - 1] += (prev + 1); 

 

 else :

 suffix[i - 1] = prev; 

 

 # This character 

 # has now appeared 

 seen[ord(s[i]) - ord('a')] = 1; 

 

 # Loop to calculate the number 

 # partition points in the string 

 for i in range(n) :

 # Check whether number of 

 # distinct characters are equal 

 if (prefix[i] == suffix[i]) :

 answer += 1; 

 

 return answer; 

 

 

# Driver Code 

if __name__ == "__main__" : 

 

 s = "ababa"; 

 

 print(waysToSplit(s)); 

 

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

// C# implementation to count the

// number of ways to partition the 

// string such that each partition 

// have same number of distinct 

// characters in the string 

using System;

 

public class GFG {

 

 // Function to count the number 

 // of ways to partition the string 

 // such that each partition have 

 // same number of distinct character 

 static int waysToSplit(string s) 

 { 

 int n = s.Length; 

 int answer = 0; 

 

 // Prefix and suffix array for 

 // distinct character from 

 // start and end 

 int []prefix = new int[n] ; 

 int []suffix = new int[n]; 

 

 // To check whether a character 

 // has appeared till ith index 

 int []seen = new int[26];

 

 // Calculating prefix array 

 for (int i = 0; i < n; i++) { 

 

 int prev = (i - 1 >= 0 ? prefix[i - 1] : 0); 

 

 // Character appears for 

 // the first time in string 

 if (seen[s[i] - 'a'] == 0) { 

 prefix[i] += (prev + 1); 

 } 

 else

 prefix[i] = prev; 

 

 // Character is visited 

 seen[s[i]- 'a'] = 1; 

 } 

 

 // Resetting seen for 

 // suffix calculation 

 for(int i = 0; i <26; i++)

 seen[i] = 0;

 

 // Calculating the suffix array 

 suffix[n - 1] = 0; 

 for (int i = n - 1; i >= 1; i--) { 

 int prev = suffix[i]; 

 

 // Character appears 

 // for the first time 

 if (seen[s[i] - 'a'] == 0) { 

 suffix[i - 1] += (prev + 1); 

 } 

 else

 suffix[i - 1] = prev; 

 

 // This character 

 // has now appeared 

 seen[s[i]- 'a'] = 1; 

 } 

 

 // Loop to calculate the number 

 // partition points in the string 

 for (int i = 0; i < n; i++) {

 

 // Check whether number of 

 // distinct characters are equal 

 if (prefix[i] == suffix[i]) 

 answer++; 

 } 

 return answer; 

 } 

 

 // Driver Code 

 public static void Main (string[] args)

 { 

 string s = "ababa"; 

 

 Console.WriteLine(waysToSplit(s)); 

 } 

 

}

 

// This code is contributed by Yash_R  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

**Time Complexity:** O(N)  
 **Auxiliary Space:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

