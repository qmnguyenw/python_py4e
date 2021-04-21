Generate a string whose all K-size substrings can be concatenated to form the
given string



Given a string **str** of size **N** and an integer **K** , the task is to
generate a string whose substrings of size **K** can be concatenated to form
the given string.  
**Examples:**

> **Input:** str = “abbaaa” K = 2  
> **Output:** abaa  
> **Explanation:**  
> All substring of size 2 of parent string “abaa” are “ab”, “ba” and “aa”.
> After concatenating all these substrings, the given string “abbaaa” can be
> obtained.
>
>  **Input:** str = “abcbcscsesesesd” K = 3  
> **Output:** abcsesd  
> **Explanation :**  
> All substring of size 3 of parent string “abcsesd” are “abc”, “bcs”, “cse”,
> “ses” and “esd”. After concatenating all these substrings, the given string
> “abcbcscsesesesd” can be obtained.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
Follow the steps below to solve the problem:

  1. We can clearly observe that by concatenating substrings of length **K** , except the first character, the remaining **K-1** characters of any substring is present in the next substring as well.
  2. Hence, traverse the string and append the first character of every substring to **ans** and then ignore next the **K-1** characters.
  3. Repeat this process for all substrings except the last substring.
  4. Append all characters of the last substring to **ans**.
  5. Return ans as the required decoded string.

Below is the implementation of the above approach :

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to generate a

// string whose substrings of

// length K concatenates to 

// form given strings

 

#include <bits/stdc++.h> 

using namespace std;

 

// Function to return the required 

// required string 

void decode_String(string str, 

int K)

{

 string ans = "";

 // Iterate the given string

 for (int i = 0; i < str.size(); 

 i += K)

 // Append the first 

 // character of every 

 // substring of length K

 ans += str[i];

 

 // Consider all characters 

 // from the last substring

 for(int i = str.size() - (K - 1); 

 i < str.size(); i++)

 ans += str[i];

 

 cout << ans << endl;

}

 

// Driver Program

int main()

{

 int K = 3;

 string str = "abcbcscsesesesd";

 decode_String(str, K);

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

// Java program to generate a

// string whose substrings of 

// length K concatenates to 

// form given strings 

class GFG{

 

// Function to return the required 

// required string 

public static void decode_String(String str,

 int K) 

{ 

 String ans = ""; 

 

 // Iterate the given string 

 for(int i = 0; 

 i < str.length(); i += K) 

 

 // Append the first 

 // character of every 

 // substring of length K 

 ans += str.charAt(i); 

 

 // Consider all characters 

 // from the last substring 

 for(int i = str.length() - (K - 1);

 i < str.length(); i++) 

 ans += str.charAt(i); 

 

 System.out.println(ans);

} 

 

// Driver code

public static void main(String[] args)

{

 int K = 3; 

 String str = "abcbcscsesesesd"; 

 

 decode_String(str, K); 

}

}

 

// This code is contributed by divyeshrabadiya07  
  
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

# Python3 program to generate a

# string whose substrings of

# length K concatenates to 

# form given strings

 

# Function to return the required 

# required string 

def decode_String(st, K):

 

 ans = ""

 

 # Iterate the given string

 for i in range(0, len(st), K):

 

 # Append the first 

 # character of every 

 # substring of length K

 ans += st[i]

 

 # Consider all characters 

 # from the last substring

 for i in range(len(st) - (K - 1), len(st)):

 ans += st[i]

 

 print(ans)

 

# Driver code

if __name__ == "__main__":

 

 K = 3

 st = "abcbcscsesesesd"

 

 decode_String(st, K)

 

# This code is contributed by chitranayal  
  
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

// C# program to generate a string

// whose substrings of length K

// concatenates to form given strings 

using System;

 

class GFG{

 

// Function to return the required 

// required string 

public static void decode_String(String str,

 int K) 

{ 

 String ans = ""; 

 

 // Iterate the given string 

 for(int i = 0; 

 i < str.Length; i += K) 

 

 // Append the first 

 // character of every 

 // substring of length K

 ans += str[i]; 

 

 // Consider all characters 

 // from the last substring 

 for(int i = str.Length - (K - 1);

 i < str.Length; i++) 

 ans += str[i]; 

 

 Console.WriteLine(ans);

} 

 

// Driver code

public static void Main(String[] args)

{

 int K = 3; 

 String str = "abcbcscsesesesd"; 

 

 decode_String(str, K); 

}

}

 

// This code is contributed by Rohit_ranjan  
  
---  
  
 __

 __

 **Output:**

    
    
    abcsesd
    

_**Time Complexity:** O(N)_  
_**Auxiliary Space:** O(1)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

