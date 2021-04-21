Largest sub-string where all the characters appear at least K times



Given a string **str** and an integer **K** , the task is to find the length
of the longest sub-string **S’** such that every character in **S’** appears
at least **K** times.

>  **Input:** s = “xyxyyz”, k = 2  
>  **Output:** 5  
> “xyxyy” is the longest sub-string where  
> every character appears at least twice.
>
>  **Input:** s = “geeksforgeeks”, k = 2  
>  **Output:** 2

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Consider all the possible sub-strings and for every sub-string,
calculate the frequency of each of its character and check whether all the
characters appear at least K times. For all such valid sub-strings, find the
largest length possible.

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

 

#define MAX 26

 

// Function that return true if frequency

// of all the present characters is at least k

bool atLeastK(int freq[], int k)

{

 for (int i = 0; i < MAX; i++) {

 

 // If the character is present and

 // its frequency is less than k

 if (freq[i] != 0 && freq[i] < k)

 return false;

 }

 

 return true;

}

 

// Function to set every frequency to zero

void setZero(int freq[])

{

 for (int i = 0; i < MAX; i++)

 freq[i] = 0;

}

 

// Function to return the length of the longest

// sub-string such that it contains every

// character at least k times

int findlength(string str, int n, int k)

{

 

 // To store the requried maximum length

 int maxLen = 0;

 

 int freq[MAX];

 

 // Starting index of the sub-string

 for (int i = 0; i < n; i++) {

 setZero(freq);

 

 // Ending index of the sub-string

 for (int j = i; j < n; j++) {

 freq[str[j] - 'a']++;

 

 // If the frequency of every character

 // of the current sub-string is at least k

 if (atLeastK(freq, k)) {

 

 // Update the maximum possible length

 maxLen = max(maxLen, j - i + 1);

 }

 }

 }

 

 return maxLen;

}

 

// Driver code

int main()

{

 string str = "xyxyyz";

 int n = str.length();

 int k = 2;

 

 cout << findlength(str, n, k);

 

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

// Java Implementation of the above approach

class GFG 

{

 

static final int MAX = 26;

 

// Function that return true if frequency

// of all the present characters is at least k

static boolean atLeastK(int freq[], int k)

{

 for (int i = 0; i < MAX; i++) 

 {

 

 // If the character is present and

 // its frequency is less than k

 if (freq[i] != 0 && freq[i] < k)

 return false;

 }

 

 return true;

}

 

// Function to set every frequency to zero

static void setZero(int freq[])

{

 for (int i = 0; i < MAX; i++)

 freq[i] = 0;

}

 

// Function to return the length of the longest

// sub-string such that it contains every

// character at least k times

static int findlength(String str, int n, int k)

{

 

 // To store the requried maximum length

 int maxLen = 0;

 

 int freq[] = new int[MAX];

 

 // Starting index of the sub-string

 for (int i = 0; i < n; i++) 

 {

 setZero(freq);

 

 // Ending index of the sub-string

 for (int j = i; j < n; j++)

 {

 freq[str.charAt(j) - 'a']++;

 

 // If the frequency of every character

 // of the current sub-string is at least k

 if (atLeastK(freq, k))

 {

 

 // Update the maximum possible length

 maxLen = Math.max(maxLen, j - i + 1);

 }

 }

 }

 

 return maxLen;

}

 

// Driver code

public static void main(String args[]) 

{

 String str = "xyxyyz";

 int n = str.length();

 int k = 2;

 

 System.out.println(findlength(str, n, k));

 

}

}

 

// This code has been contributed by 29AjayKumar  
  
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

# Python3 implementation of the approach

MAX = 26

 

# Function that return true if frequency 

# of all the present characters is at least k 

def atLeastK(freq, k) : 

 

 for i in range(MAX) :

 

 # If the character is present and 

 # its frequency is less than k 

 if (freq[i] != 0 and freq[i] < k) :

 return False; 

 

 return True; 

 

 

# Function to set every frequency to zero 

def setZero(freq) : 

 

 for i in range(MAX) :

 freq[i] = 0; 

 

 

# Function to return the length of the longest 

# sub-string such that it contains every 

# character at least k times 

def findlength(string, n, k) : 

 

 # To store the requried maximum length 

 maxLen = 0; 

 

 freq = [0]*MAX; 

 

 # Starting index of the sub-string 

 for i in range(n) :

 setZero(freq); 

 

 # Ending index of the sub-string 

 for j in range(i,n) :

 freq[ord(string[j]) - ord('a')] += 1; 

 

 # If the frequency of every character 

 # of the current sub-string is at least k 

 if (atLeastK(freq, k)) :

 

 # Update the maximum possible length 

 maxLen = max(maxLen, j - i + 1); 

 

 return maxLen; 

 

 

# Driver code 

if __name__ == "__main__" : 

 

 string = "xyxyyz"; 

 n = len(string); 

 k = 2; 

 

 print(findlength(string, n, k)); 

 

# This code is contributed by AnkitRai01  
  
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

// C# Implementation of the above approach

using System;

 

class GFG 

{

 

static int MAX = 26;

 

// Function that return true if frequency

// of all the present characters is at least k

static Boolean atLeastK(int []freq, int k)

{

 for (int i = 0; i < MAX; i++) 

 {

 

 // If the character is present and

 // its frequency is less than k

 if (freq[i] != 0 && freq[i] < k)

 return false;

 }

 

 return true;

}

 

// Function to set every frequency to zero

static void setZero(int []freq)

{

 for (int i = 0; i < MAX; i++)

 freq[i] = 0;

}

 

// Function to return the length of the longest

// sub-string such that it contains every

// character at least k times

static int findlength(String str, int n, int k)

{

 

 // To store the requried maximum length

 int maxLen = 0;

 

 int []freq = new int[MAX];

 

 // Starting index of the sub-string

 for (int i = 0; i < n; i++) 

 {

 setZero(freq);

 

 // Ending index of the sub-string

 for (int j = i; j < n; j++)

 {

 freq[str[j] - 'a']++;

 

 // If the frequency of every character

 // of the current sub-string is at least k

 if (atLeastK(freq, k))

 {

 

 // Update the maximum possible length

 maxLen = Math.Max(maxLen, j - i + 1);

 }

 }

 }

 

 return maxLen;

}

 

// Driver code

public static void Main(String []args) 

{

 String str = "xyxyyz";

 int n = str.Length;

 int k = 2;

 

 Console.WriteLine(findlength(str, n, k));

}

}

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

