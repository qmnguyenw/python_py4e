Split the binary string into substrings with equal number of 0s and 1s



Given a binary string **str** of length **N** , the task is to find the
maximum count of substrings **str** can be divided into such that all the
substrings are balanced i.e. they have equal number of **0s** and **1s**. If
it is not possible to split **str** satisfying the conditions then print
**-1**.

 **Example:**

>  **Input:** str = “0100110101”  
>  **Output:** 4  
> The required substrings are “01”, “0011”, “01” and “01”.
>
>  **Input:** str = “0111100010”  
>  **Output:** 3

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Initialize **count = 0** and traverse the string character by
character and keep track of the number of **0s** and **1s** so far, whenever
the count of **0s** and **1s** become equal increment the count. If the count
of **0s** and **1s** in the original string is not equal then print **-1**
else print the value of count after the traversal of the complete string.

  

  

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

 

// Function to return the count

// of maximum substrings str

// can be divided into

int maxSubStr(string str, int n)

{

 

 // To store the count of 0s and 1s

 int count0 = 0, count1 = 0;

 

 // To store the count of maximum

 // substrings str can be divided into

 int cnt = 0;

 for (int i = 0; i < n; i++) {

 if (str[i] == '0') {

 count0++;

 }

 else {

 count1++;

 }

 if (count0 == count1) {

 cnt++;

 }

 }

 

 // It is not possible to

 // split the string

 if (count0 != count1) {

 return -1;

 }

 

 return cnt;

}

 

// Driver code

int main()

{

 string str = "0100110101";

 int n = str.length();

 

 cout << maxSubStr(str, n);

 

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

class GFG

{

 

// Function to return the count

// of maximum substrings str

// can be divided into

static int maxSubStr(String str, int n)

{

 

 // To store the count of 0s and 1s

 int count0 = 0, count1 = 0;

 

 // To store the count of maximum

 // substrings str can be divided into

 int cnt = 0;

 for (int i = 0; i < n; i++)

 {

 if (str.charAt(i) == '0') 

 {

 count0++;

 }

 else

 {

 count1++;

 }

 if (count0 == count1) 

 {

 cnt++;

 }

 }

 

 // It is not possible to

 // split the string

 if (count0 != count1) 

 {

 return -1;

 }

 return cnt;

}

 

// Driver code

public static void main(String []args) 

{

 String str = "0100110101";

 int n = str.length();

 

 System.out.println(maxSubStr(str, n));

}

}

 

// This code is contributed by PrinciRaj1992  
  
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

 

# Function to return the count 

# of maximum substrings str 

# can be divided into

def maxSubStr(str, n):

 

 # To store the count of 0s and 1s

 count0 = 0

 count1 = 0

 

 # To store the count of maximum 

 # substrings str can be divided into

 cnt = 0

 

 for i in range(n):

 if str[i] == '0':

 count0 += 1

 else:

 count1 += 1

 

 if count0 == count1:

 cnt += 1

 

# It is not possible to 

 # split the string

 if count0 != count1:

 return -1

 

 return cnt

 

# Driver code

str = "0100110101"

n = len(str)

print(maxSubStr(str, n))  
  
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

 

class GFG

{

 

// Function to return the count

// of maximum substrings str

// can be divided into

static int maxSubStr(String str, int n)

{

 

 // To store the count of 0s and 1s

 int count0 = 0, count1 = 0;

 

 // To store the count of maximum

 // substrings str can be divided into

 int cnt = 0;

 for (int i = 0; i < n; i++)

 {

 if (str[i] == '0') 

 {

 count0++;

 }

 else

 {

 count1++;

 }

 if (count0 == count1) 

 {

 cnt++;

 }

 }

 

 // It is not possible to

 // split the string

 if (count0 != count1) 

 {

 return -1;

 }

 return cnt;

}

 

// Driver code

public static void Main(String []args) 

{

 String str = "0100110101";

 int n = str.Length;

 

 Console.WriteLine(maxSubStr(str, n));

}

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

**Time complexity:** O(N) where N is the length of string  
 **Space Complexity:** O(1)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

