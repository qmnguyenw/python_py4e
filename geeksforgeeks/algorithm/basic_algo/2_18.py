Check if a binary string has two consecutive occurrences of one everywhere



Given a string **str** consisting of only characters **‘a’** and **‘b’** , the
task is to check whether the string is valid or not. In a valid string, every
group of consecutive **b** must be of length **2** and must appear after **1
or more** occurrences of character **‘a’** i.e. **“abba”** is a valid sub-
string but **“abbb”** and **aba** are not. Print **1** if the string is valid
else print **-1**.

 **Examples:**

>  **Input:** str = “abbaaabbabba”  
>  **Output:** 1
>
>  **Input:** str = “abbaaababb”  
>  **Output:** -1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Find every occurrence of **‘b’** in the string and check
whether it is a part of the sub-string **“abb”**. If the condition fails for
any sub-string then print **-1** else print **1**.

  

  

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

 

// Function that returns 1 if str is valid

bool isValidString(string str, int n)

{

 // Index of first appearance of 'b'

 int index = find(str.begin(), 

 str.end(), 'b') - 

 str.begin();

 

 // If str starts with 'b'

 if (index == 0)

 return false;

 

 // While 'b' occurs in str

 while (index <= n - 1)

 {

 // If 'b' doesn't appear after an 'a'

 if (str[index - 1] != 'a')

 return false;

 

 // If 'b' is not succeeded by another 'b'

 if (index + 1 < n && str[index + 1] != 'b')

 return false;

 

 // If sub-string is of the type "abbb"

 if (index + 2 < n && str[index + 2] == 'b')

 return false;

 

 // If str ends with a single b

 if (index == n - 1)

 return false;

 

 index = find(str.begin() + index + 2, 

 str.end(), 'b') - str.begin();

 }

 return true;

}

 

// Driver code

int main()

{

 string str = "abbaaabbabba";

 int n = str.length();

 isValidString(str, n) ? cout

 << "true" : cout << "false";

 return 0;

}

 

// This code is contributed by

// sanjeev2552  
  
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

class GFG {

 

 // Function that returns 1 if str is valid

 private static boolean isValidString(String str, int n)

 {

 

 // Index of first appearance of 'b'

 int index = str.indexOf("b");

 

 // If str starts with 'b'

 if (index == 0)

 return false;

 

 // While 'b' occurs in str

 while (index != -1) {

 

 // If 'b' doesn't appear after an 'a'

 if (str.charAt(index - 1) != 'a')

 return false;

 

 // If 'b' is not succeeded by another 'b'

 if (index + 1 < n && str.charAt(index + 1) != 'b')

 return false;

 

 // If sub-string is of the type "abbb"

 if (index + 2 < n && str.charAt(index + 2) == 'b')

 return false;

 

 // If str ends with a single b

 if (index == n - 1)

 return false;

 

 index = str.indexOf("b", index + 2);

 }

 return true;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 String str = "abbaaabbabba";

 int n = str.length();

 System.out.println(isValidString(str, n));

 }

}  
  
---  
  
 __

 __

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 implementation of the approach

 

# Function that returns 1 if str is valid

def isValidString(str, n):

 

 # Index of first appearance of 'b'

 idx = str.find("b")

 

 # If str starts with 'b'

 if (idx == 0):

 return False

 

 # While 'b' occurs in str

 while (idx != -1):

 

 # If 'b' doesn't appear after an 'a'

 if (str[idx - 1] != 'a'):

 return False

 

 # If 'b' is not succeeded by another 'b'

 if (idx + 1 < n and str[idx + 1] != 'b'):

 return False

 

 # If sub-string is of the type "abbb"

 if (idx + 2 < n and str[idx + 2] == 'b'):

 return False

 

 # If str ends with a single b

 if (idx == n - 1):

 return False

 

 idx = str.find("b", idx + 2)

 

 return True

 

# Driver code

if __name__ == "__main__":

 

 str = "abbaaabbabba"

 n = len(str)

 print(isValidString(str, n))

 

# This code is contributed by ita_c  
  
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

 

 // Function that returns 1 if str is valid 

 private static bool isValidString(string str, int n) 

 { 

 

 // Index of first appearance of 'b' 

 int index = str.IndexOf("b"); 

 

 // If str starts with 'b' 

 if (index == 0) 

 return false; 

 

 // While 'b' occurs in str 

 while (index != -1) 

 { 

 

 // If 'b' doesn't appear after an 'a' 

 if (str[index - 1] != 'a') 

 return false; 

 

 // If 'b' is not succeeded by another 'b' 

 if (index + 1 < n && str[index + 1] != 'b') 

 return false; 

 

 // If sub-string is of the type "abbb" 

 if (index + 2 < n && str[index + 2] == 'b') 

 return false; 

 

 // If str ends with a single b 

 if (index == n - 1) 

 return false; 

 

 index = str.IndexOf("b", index + 2); 

 } 

 return true; 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 string str = "abbaaabbabba"; 

 int n = str.Length; 

 Console.WriteLine(isValidString(str, n)); 

 } 

} 

 

// This code is contributed by Ryuga  
  
---  
  
 __

 __

 **Output:**

    
    
    true
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

