Smallest number greater than Y with sum of digits equal to X



Given two integers **X** and **Y** , find the minimal number with the sum of
digits **X,** which is strictly greater than **Y**.

 **Examples:**

> **Input:** X = 18, Y = 99  
> **Output:** 189  
> **Explanation:**  
> 189 is the smallest number greater than 99 having sum of digits = 18.
>
>  **Input:** X = 12, Y = 72  
> **Output:** 75  
> **Explanation:**  
> 75 is the smallest number greater than 72 that has sum of digits = 12.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The naive approach is iterate from **Y + 1** and check if
any number whose sum of digits is **X** or not. If we found any such number
then print that number.

  

  

 _ **Time Complexity:** O((R – Y)*log10N), where R is the maximum number till
where we iterate and N is the number in the range **[Y, R]** _  
_**Auxiliary Space:** O(1)_

 **Efficient Approach:** The idea is to iterate through the digits of **Y**
from right to left, and try to increase the current digit and change the
digits to the right in order to make the sum of digits equal to **X**. Below
are the steps:

  * If we are considering the **(k + 1) th digit** from the right and increasing it, then it is possible to make the sum of **k** least significant digits to be any number in the range **[0, 9k]**.
  * When such a position is found, then stop the process and print the number at that iteration.
  * If **k** least significant digits have sum **M** (where 0 ≤ M ≤ 9k), then obtain the answer **greedily** : 
    * Traverse from the right to the left and insert 9 and subtract 9 from the sum of digits.
    * Once, the sum is less than 9, place the remaining sum.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h>

using namespace std;

// Function to return the minimum string

// of length d having the sum of digits s

string helper(int d, int s)

{

 // Return a string of length d

 string ans(d, '0');

 for (int i = d - 1; i >= 0; i--) {

 // Greedily put 9's in the end

 if (s >= 9) {

 ans[i] = '9';

 s -= 9;

 }

 // Put remaining sum

 else {

 char c = (char)s + '0';

 ans[i] = c;

 s = 0;

 }

 }

 return ans;

}

// Function to find the smallest

// number greater than Y

// whose sum of digits is X

string findMin(int x, int Y)

{

 // Convert number y to string

 string y = to_string(Y);

 int n = y.size();

 vector<int> p(n);

 // Maintain prefix sum of digits

 for (int i = 0; i < n; i++) {

 p[i] = y[i] - '0';

 if (i > 0)

 p[i] += p[i - 1];

 }

 // Iterate over Y from the back where

 // k is current length of suffix

 for (int i = n - 1, k = 0;; i--, k++) {

 // Stores current digit

 int d = 0;

 if (i >= 0)

 d = y[i] - '0';

 // Increase current digit

 for (int j = d + 1; j <= 9; j++) {

 // Sum upto current prefix

 int r = (i > 0) * p[i - 1] + j;

 // Return answer if remaining

 // sum can be obtained in suffix

 if (x - r >= 0 and x - r <= 9 * k) {

 // Find suffix of length k

 // having sum of digits x-r

 string suf = helper(k, x - r);

 string pre = "";

 if (i > 0)

 pre = y.substr(0, i);

 // Append current character

 char cur = (char)j + '0';

 pre += cur;

 // Return the result

 return pre + suf;

 }

 }

 }

}

// Driver Code

int main()

{

 // Given Number and Sum

 int x = 18;

 int y = 99;

 // Function Call

 cout << findMin(x, y) << endl;

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

// Java program for the above approach

import java.util.*;

@SuppressWarnings("unchecked")

class GFG{

 

// Function to return the minimum String

// of length d having the sum of digits s

static String helper(int d, int s)

{

 

 // Return a String of length d

 StringBuilder ans = new StringBuilder();

 

 for(int i = 0; i < d; i++)

 {

 ans.append("0");

 }

 

 for(int i = d - 1; i >= 0; i--)

 {

 

 // Greedily put 9's in the end

 if (s >= 9)

 {

 ans.setCharAt(i,'9');

 s -= 9;

 }

 

 // Put remaining sum

 else

 {

 char c = (char)(s + (int)'0');

 ans.setCharAt(i, c);

 s = 0;

 }

 }

 return ans.toString();

}

 

// Function to find the smallest

// number greater than Y

// whose sum of digits is X

static String findMin(int x, int Y)

{

 

 // Convert number y to String

 String y = Integer.toString(Y);

 

 int n = y.length();

 

 ArrayList p = new ArrayList();

 

 for(int i = 0; i < n; i++)

 {

 p.add(0);

 }

 

 // Maintain prefix sum of digits

 for(int i = 0; i < n; i++)

 {

 p.add(i, (int)((int) y.charAt(i) - (int)'0'));

 

 if (i > 0)

 {

 p.add(i, (int)p.get(i) +

 (int)p.get(i - 1));

 }

 }

 

 // Iterate over Y from the back where

 // k is current length of suffix

 for(int i = n - 1, k = 0;; i--, k++)

 {

 

 // Stores current digit

 int d = 0;

 

 if (i >= 0)

 {

 d = (int) y.charAt(i) - (int)'0';

 }

 

 // Increase current digit

 for(int j = d + 1; j <= 9; j++)

 {

 int r = j;

 

 // Sum upto current prefix

 if (i > 0)

 {

 r += (int) p.get(i - 1);

 }

 

 // Return answer if remaining

 // sum can be obtained in suffix

 if (x - r >= 0 && x - r <= 9 * k)

 {

 

 // Find suffix of length k

 // having sum of digits x-r

 String suf = helper(k, x - r);

 

 String pre = "";

 

 if (i > 0)

 pre = y.substring(0, i);

 

 // Append current character

 char cur = (char)(j + (int)'0');

 pre += cur;

 

 // Return the result

 return pre + suf;

 }

 }

 }

}

 

// Driver code

public static void main(String[] arg)

{

 

 // Given number and sum

 int x = 18;

 int y = 99;

 

 // Function call

 System.out.print(findMin(x, y));

}

}

// This code is contributed by pratham76  
  
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

# Python3 program for the

# above approach

# Function to return the

# minimum string of length

# d having the sum of digits s

def helper(d, s):

 # Return a string of

 # length d

 ans = ['0'] * d

 for i in range(d - 1,

 -1, -1):

 # Greedily put 9's

 # in the end

 if (s >= 9):

 ans[i] = '9'

 s -= 9

 # Put remaining sum

 else:

 c = chr(s +

 ord('0'))

 ans[i] = c;

 s = 0;

 return ''.join(ans);

# Function to find the

# smallest number greater

# than Y whose sum of

# digits is X

def findMin(x, Y):

 # Convert number y

 # to string

 y = str(Y);

 n = len(y)

 p = [0] * n

 # Maintain prefix sum

 # of digits

 for i in range(n):

 p[i] = (ord(y[i]) -

 ord('0'))

 if (i > 0):

 p[i] += p[i - 1];

 # Iterate over Y from the

 # back where k is current

 # length of suffix

 n - 1

 k = 0

 

 while True:

 # Stores current digit

 d = 0;

 if (i >= 0):

 d = (ord(y[i]) -

 ord('0'))

 # Increase current

 # digit

 for j in range(d + 1,

 10):

 # Sum upto current

 # prefix

 r = ((i > 0) *

 p[i - 1] + j);

 # Return answer if

 # remaining sum can

 # be obtained in suffix

 if (x - r >= 0 and

 x - r <= 9 * k):

 # Find suffix of length

 # k having sum of digits

 # x-r

 suf = helper(k,

 x - r);

 pre = "";

 if (i > 0):

 pre = y[0 : i]

 # Append current

 # character

 cur = chr(j +

 ord('0'))

 pre += cur;

 # Return the result

 return pre + suf;

 i -= 1

 k += 1

# Driver Code

if __name__ == "__main__":

 

 # Given Number and Sum

 x = 18;

 y = 99;

 # Function Call

 print ( findMin(x, y))

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

// C# program for the above approach

using System;

using System.Text;

using System.Collections;

class GFG{

// Function to return the minimum string

// of length d having the sum of digits s

static string helper(int d, int s)

{

 // Return a string of length d

 StringBuilder ans = new StringBuilder();

 

 for(int i = 0; i < d; i++)

 {

 ans.Append("0");

 }

 

 for(int i = d - 1; i >= 0; i--)

 {

 

 // Greedily put 9's in the end

 if (s >= 9)

 {

 ans[i] = '9';

 s -= 9;

 }

 

 // Put remaining sum

 else

 {

 char c = (char)(s + (int)'0');

 ans[i] = c;

 s = 0;

 }

 }

 return ans.ToString();

}

// Function to find the smallest

// number greater than Y

// whose sum of digits is X

static string findMin(int x, int Y)

{

 

 // Convert number y to string

 string y = Y.ToString();

 

 int n = y.Length;

 

 ArrayList p = new ArrayList();

 

 for(int i = 0; i < n; i++)

 {

 p.Add(0);

 }

 

 // Maintain prefix sum of digits

 for(int i = 0; i < n; i++)

 {

 p[i] = (int)((int) y[i] - (int)'0');

 

 if (i > 0)

 {

 p[i] = (int)p[i] +

 (int)p[i - 1];

 }

 }

 

 // Iterate over Y from the back where

 // k is current length of suffix

 for(int i = n - 1, k = 0;; i--, k++)

 {

 

 // Stores current digit

 int d = 0;

 

 if (i >= 0)

 {

 d = (int) y[i] - (int)'0';

 }

 

 // Increase current digit

 for(int j = d + 1; j <= 9; j++)

 {

 int r = j;

 

 // Sum upto current prefix

 if (i > 0)

 {

 r += (int) p[i - 1];

 }

 

 // Return answer if remaining

 // sum can be obtained in suffix

 if (x - r >= 0 && x - r <= 9 * k)

 {

 

 // Find suffix of length k

 // having sum of digits x-r

 string suf = helper(k, x - r);

 

 string pre = "";

 

 if (i > 0)

 pre = y.Substring(0, i);

 

 // Append current character

 char cur = (char)(j + (int)'0');

 pre += cur;

 

 // Return the result

 return pre + suf;

 }

 }

 }

}

// Driver code

public static void Main(string[] arg)

{

 

 // Given number and sum

 int x = 18;

 int y = 99;

 

 // Function call

 Console.Write(findMin(x, y));

}

}

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    189

_**Time Complexity:** O(log10Y) _  
_**Auxiliary Space:** O(log10Y)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

