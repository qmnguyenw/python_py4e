Maximum number of overlapping string



Given two strings **S** and **T** , the task is to count the number of the
overlapping string T in the string S.  
 **Note:** If there are some mismatch words as a subsequence which do not
matche to the string T, then print -1.  
**Examples:**

>  **Input:** S = “chirpchirp”, T = “chirp”  
> **Output:** 0  
> **Explanation:**  
> There are no overlapping strings of “chirp”.  
>  **Input:** S = “chcirphirp”, T = “chirp”  
> **Output:** 2  
> There are two overlapping string of T:  
> First “chirp” can be **ch** c **irp** hirp.  
> Second “chirp” can be ch **c** irp **hirp**.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to iterate over the string **S** and increase the
overlapping count at an instant when the first character of the string T
occurs If at any instant the current character is equal to the last character
then decrement the overlapping count. Meanwhile, update the maximum
overlapping count if it is greater than 2. Finally, to check that every
subsequence matches to the string T check overlapping count is equal to zero
or not. If yes return the maximum overlap count.  
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

// maximum number of occurrence of

// the overlapping count

#include <bits/stdc++.h>

using namespace std;

// Function to find the maximum

// overlapping strings

int maxOverlap(string S, string T)

{

 string str = T;

 int count[T.length()] = { 0 };

 int overlap = 0;

 int max_overlap = 0;

 for (int i = 0; i <= S.length(); i++) {

 

 // Get the current character

 int index = str.find(S[i]);

 // Condition to check if the current

 // character is the first character

 // of the string T then increment the

 // overlapping count

 if (index == 0) {

 overlap++;

 if (overlap >= 2)

 max_overlap = max(overlap, max_overlap);

 count[index]++;

 }

 else {

 // Condition to check

 // previous character is also

 // occurred

 if (count[index - 1] <= 0)

 return -1;

 // Update count of previous

 // and current character

 count[index]++;

 count[index - 1]--;

 }

 // Condition to check the current

 // character is the last character

 // of the string T

 if (index == 4)

 overlap--;

 }

 

 // Condition to check the every

 // subsequence is a valid string T

 if (overlap == 0)

 return max_overlap;

 else

 return -1;

}

// Driver Code

int main()

{

 string S = "chcirphirp";

 string T = "chirp";

 

 // Function Call

 cout << maxOverlap(S, T);

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

// maximum number of occurrence of

// the overlapping count

import java.util.*;

class GFG{

// Function to find the maximum

// overlapping Strings

static int maxOverlap(String S, String T)

{

 String str = T;

 int count[] = new int[T.length()];

 int overlap = 0;

 int max_overlap = 0;

 for(int i = 0; i < S.length(); i++)

 {

 

 // Get the current character

 int index = str.indexOf(S.charAt(i));

 

 // Condition to check if the current

 // character is the first character

 // of the String T then increment the

 // overlapping count

 if (index == 0)

 {

 overlap++;

 

 if (overlap >= 2)

 max_overlap = Math.max(overlap,

 max_overlap);

 count[index]++;

 }

 else

 {

 

 // Condition to check

 // previous character is also

 // occurred

 if (count[index - 1] <= 0)

 return -1;

 

 // Update count of previous

 // and current character

 count[index]++;

 count[index - 1]--;

 }

 

 // Condition to check the current

 // character is the last character

 // of the String T

 if (index == 4)

 overlap--;

 

 }

 

 // Condition to check the every

 // subsequence is a valid String T

 if (overlap == 0)

 return max_overlap;

 else

 return -1;

}

// Driver code

public static void main(String[] args)

{

 String S = "chcirphirp";

 String T = "chirp";

 

 // Function call

 System.out.print(maxOverlap(S, T));

}

}

// This code is contributed by Princi Singh  
  
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

# maximum number of occurrence of

# the overlapping count

# Function to find the maximum

# overlapping strings

def maxOverlap(S, T):

 

 str = T

 count = [0 for i in range(len(T))]

 overlap = 0

 max_overlap = 0

 for i in range(0, len(S)):

 # Get the current character

 index = str.find(S[i])

 # Condition to check if

 # the current character is

 # the first character of the

 # string T then increment the

 # overlapping count

 if(index == 0):

 overlap += 1

 

 if(overlap >= 2):

 max_overlap = max(overlap,

 max_overlap)

 count[index] += 1

 else:

 # Condition to check 

 # previous character is also 

 # occurred

 if(count[index - 1] <= 0):

 return -1

 

 # Update count of previous 

 # and current character

 count[index] += 1

 count[index - 1] -= 1

 # Condition to check the current

 # character is the last character 

 # of the string T

 if(index == 4):

 overlap -= 1

 # Condition to check the every 

 # subsequence is a valid string T

 if(overlap == 0):

 return max_overlap

 else:

 return -1

# Driver Code

S = "chcirphirp"

T = "chirp"

# Function Call

print(maxOverlap(S, T))

# This code is contributed by avanitrachhadiya2155  
  
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

// maximum number of occurrence of

// the overlapping count

using System;

class GFG{

// Function to find the maximum

// overlapping Strings

static int maxOverlap(String S, String T)

{

 String str = T;

 int []count = new int[T.Length];

 int overlap = 0;

 int max_overlap = 0;

 for(int i = 0; i < S.Length; i++)

 {

 

 // Get the current character

 int index = str.IndexOf(S[i]);

 

 // Condition to check if the current

 // character is the first character

 // of the String T then increment the

 // overlapping count

 if (index == 0)

 {

 overlap++;

 

 if (overlap >= 2)

 {

 max_overlap = Math.Max(overlap,

 max_overlap);

 }

 count[index]++;

 }

 else

 {

 

 // Condition to check

 // previous character is also

 // occurred

 if (count[index - 1] <= 0)

 return -1;

 

 // Update count of previous

 // and current character

 count[index]++;

 count[index - 1]--;

 }

 

 // Condition to check the current

 // character is the last character

 // of the String T

 if (index == 4)

 overlap--;

 }

 

 // Condition to check the every

 // subsequence is a valid String T

 if (overlap == 0)

 return max_overlap;

 else

 return -1;

}

// Driver code

public static void Main(String[] args)

{

 String S = "chcirphirp";

 String T = "chirp";

 

 // Function call

 Console.Write(maxOverlap(S, T));

}

}

// This code is contributed by sapnasingh4991  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

