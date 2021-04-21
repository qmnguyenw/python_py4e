Find whether X exists in Y after jumbling X



Given two strings **X** and **Y** containing lower-case alphabets, the task is
to check whether any permutation of string **X** exists in **Y** as its
substring.

 **Examples:**

>  **Input:** X = “skege”, Y = “geeksforgeeks”  
>  **Output:** Yes  
> “geeks” is a permutation of X which  
> appears as a substring in Y.
>
>  **Input:** X = “aabb”, Y = “bbbbbbb”  
>  **Output:** No

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can be solved using the two pointer technique.

  

  

  * Compute the frequency count of every character of string **X** and store it in an array say **cnt_X[]**.
  * Now for substring **Y[i…(i+X.length()-1)]** , the same frequency array can be generated say **cnt[]**.
  * Using the array from step 2, the frequency count for the next window can be calculated in O(1) time by decrementing **cnt[Y[i] – ‘a’]** by **1** and incrementing **cnt[Y[i + X.length()] – ‘a’]** by **1**.
  * Compare **cnt[]** and **cnt_X[]** for every window. If both of them are equal then a match has been found.

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

 

const int MAX = 26;

 

// Function that returns true if both

// the arrays have equal values

bool areEqual(int* a, int* b)

{

 // Test the equality

 for (int i = 0; i < MAX; i++)

 if (a[i] != b[i])

 return false;

 return true;

}

 

// Function that returns true if any permutation

// of X exists as a substring in Y

bool xExistsInY(string x, string y)

{

 

 // Base case

 if (x.size() > y.size())

 return false;

 

 // To store cumulative frequency

 int cnt_x[MAX] = { 0 };

 int cnt[MAX] = { 0 };

 

 // Finding the frequency of

 // characters in X

 for (int i = 0; i < x.size(); i++)

 cnt_x[x[i] - 'a']++;

 

 // Finding the frequency of characters

 // in Y upto the length of X

 for (int i = 0; i < x.size(); i++)

 cnt[y[i] - 'a']++;

 

 // Equality check

 if (areEqual(cnt_x, cnt))

 return true;

 

 // Two pointer approach to generate the

 // entire cumulative frequency

 for (int i = 1; i < y.size() - x.size() + 1; i++) {

 

 // Remove the first character of

 // the previous window

 cnt[y[i - 1] - 'a']--;

 

 // Add the last character of

 // the current window

 cnt[y[i + x.size() - 1] - 'a']++;

 

 // Equality check

 if (areEqual(cnt, cnt_x))

 return true;

 }

 

 return false;

}

 

// Driver code

int main()

{

 string x = "skege";

 string y = "geeksforgeeks";

 

 if (xExistsInY(x, y))

 cout << "Yes";

 else

 cout << "No";

 

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

// Java implementation of the approach

class GFG

{

static int MAX = 26;

 

// Function that returns true if both

// the arrays have equal values

static boolean areEqual(int []a, int []b)

{

 // Test the equality

 for (int i = 0; i < MAX; i++)

 if (a[i] != b[i])

 return false;

 return true;

}

 

// Function that returns true if 

// any permutation of X exists 

// as a subString in Y

static boolean xExistsInY(String x, String y)

{

 

 // Base case

 if (x.length() > y.length())

 return false;

 

 // To store cumulative frequency

 int []cnt_x = new int[MAX];

 int []cnt = new int[MAX];

 

 // Finding the frequency of

 // characters in X

 for (int i = 0; i < x.length(); i++)

 cnt_x[x.charAt(i) - 'a']++;

 

 // Finding the frequency of characters

 // in Y upto the length of X

 for (int i = 0; i < x.length(); i++)

 cnt[y.charAt(i) - 'a']++;

 

 // Equality check

 if (areEqual(cnt_x, cnt))

 return true;

 

 // Two pointer approach to generate the

 // entire cumulative frequency

 for (int i = 1; i < y.length() - 

 x.length() + 1; i++) 

 {

 

 // Remove the first character of

 // the previous window

 cnt[y.charAt(i - 1) - 'a']--;

 

 // Add the last character of

 // the current window

 cnt[y.charAt(i + x.length() - 1) - 'a']++;

 

 // Equality check

 if (areEqual(cnt, cnt_x))

 return true;

 }

 return false;

}

 

// Driver code

public static void main(String[] args)

{

 String x = "skege";

 String y = "geeksforgeeks";

 

 if (xExistsInY(x, y))

 System.out.print("Yes");

 else

 System.out.print("No");

}

}

 

// This code contributed by PrinciRaj1992  
  
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

 

# Function that returns true if both

# the arrays have equal values

def areEqual(a, b):

 

 # Test the equality

 for i in range(MAX):

 if (a[i] != b[i]):

 return False

 return True

 

# Function that returns true if any permutation

# of X exists as a sub in Y

def xExistsInY(x,y):

 

 # Base case

 if (len(x) > len(y)):

 return False

 

 # To store cumulative frequency

 cnt_x = [0] * MAX

 cnt = [0] * MAX

 

 # Finding the frequency of

 # characters in X

 for i in range(len(x)):

 cnt_x[ord(x[i]) - ord('a')] += 1;

 

 # Finding the frequency of characters

 # in Y upto the length of X

 for i in range(len(x)):

 cnt[ord(y[i]) - ord('a')] += 1

 

 # Equality check

 if (areEqual(cnt_x, cnt)):

 return True

 

 # Two pointer approach to generate the

 # entire cumulative frequency

 for i in range(1, len(y) - len(x) + 1):

 

 # Remove the first character of

 # the previous window

 cnt[ord(y[i - 1]) - ord('a')] -= 1

 

 # Add the last character of

 # the current window

 cnt[ord(y[i + len(x) - 1]) - ord('a')] +=
1

 

 # Equality check

 if (areEqual(cnt, cnt_x)):

 return True

 

 return False

 

# Driver Code

if __name__ == '__main__':

 x = "skege"

 y = "geeksforgeeks"

 

 if (xExistsInY(x, y)):

 print("Yes")

 else:

 print("No")

 

# This code is contributed by Mohit Kumar  
  
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

static int MAX = 26;

 

// Function that returns true if both

// the arrays have equal values

static bool areEqual(int []a, 

 int []b)

{

 // Test the equality

 for (int i = 0; i < MAX; i++)

 if (a[i] != b[i])

 return false;

 return true;

}

 

// Function that returns true if 

// any permutation of X exists 

// as a subString in Y

static bool xExistsInY(String x, 

 String y)

{

 

 // Base case

 if (x.Length > y.Length)

 return false;

 

 // To store cumulative frequency

 int []cnt_x = new int[MAX];

 int []cnt = new int[MAX];

 

 // Finding the frequency of

 // characters in X

 for (int i = 0; i < x.Length; i++)

 cnt_x[x[i] - 'a']++;

 

 // Finding the frequency of characters

 // in Y upto the length of X

 for (int i = 0; i < x.Length; i++)

 cnt[y[i] - 'a']++;

 

 // Equality check

 if (areEqual(cnt_x, cnt))

 return true;

 

 // Two pointer approach to generate the

 // entire cumulative frequency

 for (int i = 1; i < y.Length - 

 x.Length + 1; i++) 

 {

 

 // Remove the first character of

 // the previous window

 cnt[y[i - 1] - 'a']--;

 

 // Add the last character of

 // the current window

 cnt[y[i + x.Length - 1] - 'a']++;

 

 // Equality check

 if (areEqual(cnt, cnt_x))

 return true;

 }

 return false;

}

 

// Driver code

public static void Main(String[] args)

{

 String x = "skege";

 String y = "geeksforgeeks";

 

 if (xExistsInY(x, y))

 Console.Write("Yes");

 else

 Console.Write("No");

}

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

**Time Complexity:** O(xLen + yLen) where xLen and yLen are the lengths of the
strings X and Y respectively.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

