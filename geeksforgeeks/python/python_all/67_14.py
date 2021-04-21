Binary string with given frequencies of sums of consecutive pairs of
characters



Given three integers **P** , **Q** , and **R** , the task is to generate a
binary string with P, Q, and R pairs of consecutive characters with sum 0, 1,
and 2 respectively.  
 **Examples:**

> **Input:** P = 1, Q = 2, R = 2  
> **Output:** 111001  
> **Explanation:**  
>  Substrings “00”, “10”, “01”, and “11” have sums 0, 1, 1, and 2
> respectively.  
> Thus, the following set of substrings { {“11”}, {“11”}, {“10”}, {“00”},
> {“01”} } satisfy the given constraints. Hence, the string formed by the
> substrings is 111001.  
>  **Input:** P = 3, Q = 1, R = 0  
> **Output:** 10000  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** In order to solve this problem, we need to follow the following
steps:

  * If **P** and **R** are _non-zero_ , then there is at least one pair of consecutive characters with sum 1. Thus, if **Q** provided is 0, in such a case, then no such string can be formed. Hence, return _-1_.
  * If Q is zero, and only one of P and R is non-zero, then append **0 P+1** times _if P is non-zero_ or append **1 R+1** time _if R is non-zero_.
  * If all of them are non-zero: 
    * Append **0** and **1** **P + 1** and **Q + 1** times respectively.
    * Append **0** and **1** alternatingly **Q – 1** time.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to generate a binary

// string with given frequencies

// of sums of consecutive

// pair of characters

#include <bits/stdc++.h>

using namespace std;

// A Function that generates

// and returns the binary string

string build_binary_str(int p,

 int q, int r)

{

 // P: Frequency of consecutive

 // characters with sum 0

 // Q: Frequency of consecutive

 // characters with sum 1

 // R: Frequency of consecutive

 // characters with sum 2

 string ans = "";

 // If no consecutive

 // character adds up to 1

 if (q == 0) {

 // Not possible if both P

 // and Q are non - zero

 if (p != 0 && r != 0) {

 return "-1";

 }

 else {

 // If P is not equal to 0

 if (p) {

 // Append 0 P + 1 times

 ans = string(p + 1, '0');

 }

 else {

 // Append 1 R + 1 times

 ans = string(r + 1, '1');

 }

 }

 }

 else {

 // Append "01" to satisfy Q

 for (int i = 1; i <= q + 1; i++) {

 if (i % 2 == 0) {

 ans += '0';

 }

 else {

 ans += '1';

 }

 }

 // Append "0" P times

 ans.insert(1, string(p, '0'));

 // Append "1" R times

 ans.insert(0, string(r, '1'));

 }

 return ans;

}

// Driver Code

int main()

{

 int p = 1, q = 2, r = 2;

 cout << build_binary_str(p, q, r);

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

// Java program to generate a binary

// String with given frequencies

// of sums of consecutive

// pair of characters

 class GFG{

 

// A Function that generates

// and returns the binary String

static String build_binary_str(int p,

 int q, int r)

{

 

 // P: Frequency of consecutive

 // characters with sum 0

 // Q: Frequency of consecutive

 // characters with sum 1

 // R: Frequency of consecutive

 // characters with sum 2

 String ans = "";

 

 // If no consecutive

 // character adds up to 1

 if (q == 0)

 {

 

 // Not possible if both P

 // and Q are non - zero

 if (p != 0 && r != 0)

 {

 return "-1";

 }

 

 else

 {

 

 // If P is not equal to 0

 if (p > 0)

 {

 

 // Append 0 P + 1 times

 ans = Strings(p + 1, '0');

 }

 else

 {

 // Append 1 R + 1 times

 ans = Strings(r + 1, '1');

 }

 }

 }

 else

 {

 

 // Append "01" to satisfy Q

 for (int i = 1; i <= q + 1; i++)

 {

 if (i % 2 == 0)

 {

 ans += '0';

 }

 else

 {

 ans += '1';

 }

 }

 

 // Append "0" P times

 ans = ans.substring(0, 1) + Strings(p, '0') +
ans.substring(1);

 

 // Append "1" R times

 ans = Strings(r, '1') + ans;

 }

 return ans;

}

 

static String Strings(int p, char c)

{

 String ans = "";

 for (int i = 0; i < p; i++)

 ans += c;

 return ans;

}

 

// Driver Code

public static void main(String[] args)

{

 int p = 1, q = 2, r = 2;

 System.out.print(build_binary_str(p, q, r));

}

}

// This code is contributed by shikhasingrajput  
  
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

# Python3 program to generate a binary

# string with given frequencies

# of sums of consecutive

# pair of characters

# A Function that generates

# and returns the binary string

def build_binary_str(p, q, r):

 

 # P: Frequency of consecutive

 # characters with sum 0

 # Q: Frequency of consecutive

 # characters with sum 1

 # R: Frequency of consecutive

 # characters with sum 2

 ans = ""

 # If no consecutive

 # character adds up to 1

 if (q == 0):

 

 # Not possible if both P

 # and Q are non - zero

 if (p != 0 and r != 0):

 return "-1"

 else:

 

 # If P is not equal to 0

 if (p):

 

 # Append 0 P + 1 times

 temp = ""

 for i in range(p + 1):

 temp += '0'

 

 ans = temp

 

 else:

 

 # Append 1 R + 1 times

 temp = ""

 for i in range(r + 1):

 temp += '1'

 

 ans = temp

 else:

 

 # Append "01" to satisfy Q

 for i in range(1, q + 2):

 if (i % 2 == 0):

 ans += '0'

 else:

 ans += '1'

 # Append "0" P times

 temp = ""

 for i in range(p):

 temp += '0'

 

 st = ""

 st += ans[0]

 st += temp

 

 for i in range(1, len(ans)):

 st += ans[i]

 

 ans = st

 # Append "1" R times

 temp = ""

 for i in range(r):

 temp += '1'

 ans = temp + ans

 

 return ans

# Driver Code

if __name__ == '__main__':

 

 p = 1

 q = 2

 r = 2

 

 print(build_binary_str(p, q, r))

# This code is contributed by Surendra_Gangwar  
  
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

// C# program to generate a binary

// String with given frequencies

// of sums of consecutive

// pair of characters

using System;

class GFG{

 

// A Function that generates

// and returns the binary String

static String build_binary_str(int p,

 int q, int r)

{

 // P: Frequency of consecutive

 // characters with sum 0

 // Q: Frequency of consecutive

 // characters with sum 1

 // R: Frequency of consecutive

 // characters with sum 2

 String ans = "";

 // If no consecutive

 // character adds up to 1

 if (q == 0)

 {

 // Not possible if both P

 // and Q are non - zero

 if (p != 0 && r != 0)

 {

 return "-1";

 }

 else

 { 

 // If P is not equal to 0

 if (p > 0)

 {

 // Append 0 P + 1 times

 ans = Strings(p + 1, '0');

 }

 else

 {

 // Append 1 R + 1 times

 ans = Strings(r + 1, '1');

 }

 }

 }

 else

 {

 // Append "01" to satisfy Q

 for (int i = 1; i <= q + 1; i++)

 {

 if (i % 2 == 0)

 {

 ans += '0';

 }

 else

 {

 ans += '1';

 }

 }

 // Append "0" P times

 ans = ans.Substring(0, 1) +

 Strings(p, '0') +

 ans.Substring(1);

 // Append "1" R times

 ans = Strings(r, '1') + ans;

 }

 return ans;

}

 static String Strings(int p, char c)

 {

 String ans = "";

 for (int i = 0; i < p; i++)

 ans += c;

 return ans;

 }

 // Driver Code

 public static void Main(String[] args)

 {

 int p = 1, q = 2, r = 2;

 Console.Write(build_binary_str(p,

 q, r));

 }

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    111001
    
    
    
    
    
    

**Time Complexity:** _O(P + Q + R)_

![competitive-programming-img](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200604102100/GFG-CP-Article-2.png)

  
  

  

My Personal Notes _arrow_drop_up_

Save

