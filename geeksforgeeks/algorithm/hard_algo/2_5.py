Lexicographically smallest string which differs from given strings at exactly
K indices



Given two strings **S 1** and **S 2** of length **N** and a positive integer
**K** , the task is to find the lexicographically smallest string such that it
differ from the given two strings **S 1** and **S 2** at exactly **K** places.
If there is no such string exists then print **“-1”**.  
 **Examples:**  

> **Input:** N = 4, K = 3, S1 = “ccbb”, S2 = “caab”  
> **Output:** abcb  
> **Explanation:**  
> String “abcb” differs from S1 at exactly 3 places i.e., at positions 1, 2
> and 3, and  
> String “abcb” differs from S2 at exactly 3 places i.e., at positions 1, 2
> and 3.
>
>  **Input:** N = 5, K = 1, S1 = “cbabb”, S2 = “babaa”  
> **Output:** -1  
> **Explanation:**  
> No such string exists that simultaneously differs from S1 and S2 only at 1
> position.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  1. Instead of building S3 from scratch, pick S2 as the resultant string S3 and try to modify it according to the given constraints.
  2. Find at how many positions does the answer string S3 differs from S1.
  3. Let they differ from each other at exactly **d** positions. Then the minimum number of places in which the answer string S3 can differ from both the string is **ceil(d/2)** and maximum number of places can be **N**.
  4. If **K** is within the range **[ceil(d/2), N]** then S3 exists otherwise S3 doesn’t exists and print **“-1”**.
  5. For string S3 below are the cases: 
    * **_K_** _greater than_ ** _d_**
      1. If K is greater than d then modify all the positions at which S1 differs from S3 such that after modification, S3 at that position will now differ from both S1 and S2. Decrement K.
      2. Modify the positions at which S1 is the same as S3 such that after modification, S3 at that position will now differ from both S1 and S2. Decrement K.
    *  ** _K_** _less than or equal to_ ** _d_**
      1. In this case, only modify the S3 position at which S1 and S3 differ.
      2. After modification let **X** be the number of positions at which only S1 differs from S3 and S2 differs from S3.
      3. Let **T** be the number of positions which both S1 and S2 differ from S3. Then the equation’s will be:   

> (2 * X) + T = d  
> X + T = K
>
>  
>
>
>  
>

      4. Solving these equations, the values of X and T can be obtained and modify the answer string S3 accordingly.

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

 

char arr[] = { 'a', 'b', 'c' };

 

// Function to find the string which

// differ at exactly K positions

void findString(int n, int k,

 string s1, string s2)

{

 // Initialise s3 as s2

 string s3 = s2;

 

 // Number of places at which

 // s3 differ from s2

 int d = 0;

 for (int i = 0;

 i < s1.size(); i++) {

 if (s1[i] != s2[i])

 d++;

 }

 

 // Minimum possible value

 // is ceil(d/2) if it is

 // not possible then -1

 if ((d + 1) / 2 > k) {

 cout << "-1" << endl;

 return;

 }

 

 else {

 

 // Case 2 when K is

 // less equal d

 if (k <= d) {

 

 // value of X and T

 // after solving

 // equations

 

 // T shows the number

 // of modification

 // such that position

 // differ from both

 

 // X show the modification

 // such that this position

 // only differ from only

 // one string

 int X = d - k;

 int T = 2 * k - d;

 

 for (int i = 0;

 i < s3.size(); i++) {

 

 if (s1[i] != s2[i]) {

 

 // modify the position

 // such that this

 // differ from both

 // S1 & S2 & decrease

 // the T at each step

 if (T > 0) {

 

 // Finding the character

 // which is different

 // from both S1 and S2

 for (int j = 0;

 j < 3; j++) {

 

 if (arr[j] != s1[i]

 && arr[j] != s2[i]) {

 s3[i] = arr[j];

 T--;

 break;

 }

 }

 }

 

 // After we done T

 // start modification

 // to meet our

 // requirement

 // for X type

 else if (X > 0) {

 

 s3[i] = s1[i];

 X--;

 }

 }

 }

 

 // Resultant string

 cout << s3 << endl;

 }

 else {

 

 // Case 1 when K > d

 // In first step, modify all

 // the character which are

 // not same in S1 and S3

 for (int i = 0;

 i < s1.size(); i++) {

 

 if (s1[i] != s3[i]) {

 for (int j = 0;

 j < 3; j++) {

 

 // Finding character

 // which is

 // different from

 // both S1 and S2

 if (arr[j] != s1[i]

 && arr[j] != s3[i]) {

 s3[i] = arr[j];

 k--;

 break;

 }

 }

 }

 }

 

 // Our requrement not

 // satisied by performing

 // step 1. We need to

 // modify the position

 // which matches in

 // both string

 for (int i = 0;

 i < s1.size(); i++) {

 

 if (s1[i] == s3[i] && k) {

 

 // Finding the character

 // which is different

 // from both S1 and S2

 for (int j = 0; j < 3; j++) {

 

 if (arr[j] != s1[i]

 && arr[j] != s3[i]) {

 s3[i] = arr[j];

 k--;

 break;

 }

 }

 }

 }

 

 // Resultant string

 cout << s3 << endl;

 }

 }

}

 

// Driver Code

int main()

{

 int N = 4, k = 2;

 

 // Given two strings

 string S1 = "zzyy";

 string S2 = "zxxy";

 

 // Function Call

 findString(N, k, S1, S2);

 

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

class GFG{

 

static char arr[] = { 'a', 'b', 'c' };

 

// Function to find the String which

// differ at exactly K positions

static void findString(int n, int k,

 char []s1, 

 char []s2)

{

 // Initialise s3 as s2

 char []s3 = s2;

 

 // Number of places at which

 // s3 differ from s2

 int d = 0;

 for (int i = 0;

 i < s1.length; i++)

 {

 if (s1[i] != s2[i])

 d++;

 }

 

 // Minimum possible value

 // is Math.ceil(d/2) if it is

 // not possible then -1

 if ((d + 1) / 2 > k) 

 {

 System.out.print("-1" + "\n");

 return;

 }

 

 else

 {

 

 // Case 2 when K is

 // less equal d

 if (k <= d) 

 {

 

 // value of X and T

 // after solving

 // equations

 

 // T shows the number

 // of modification

 // such that position

 // differ from both

 

 // X show the modification

 // such that this position

 // only differ from only

 // one String

 int X = d - k;

 int T = 2 * k - d;

 

 for (int i = 0; i < s3.length; i++) 

 {

 if (s1[i] != s2[i]) 

 {

 

 // modify the position

 // such that this

 // differ from both

 // S1 & S2 & decrease

 // the T at each step

 if (T > 0) 

 {

 

 // Finding the character

 // which is different

 // from both S1 and S2

 for (int j = 0; j < 3; j++)

 {

 

 if (arr[j] != s1[i] && 

 arr[j] != s2[i]) 

 {

 s3[i] = arr[j];

 T--;

 break;

 }

 }

 }

 

 // After we done T

 // start modification

 // to meet our

 // requirement

 // for X type

 else if (X > 0) 

 {

 s3[i] = s1[i];

 X--;

 }

 }

 }

 

 // Resultant String

 System.out.print(new String(s3) + "\n");

 }

 else

 {

 

 // Case 1 when K > d

 // In first step, modify all

 // the character which are

 // not same in S1 and S3

 for (int i = 0;

 i < s1.length; i++) 

 {

 

 if (s1[i] != s3[i]) 

 {

 for (int j = 0;

 j < 3; j++) 

 {

 

 // Finding character

 // which is

 // different from

 // both S1 and S2

 if (arr[j] != s1[i] &&

 arr[j] != s3[i]) 

 {

 s3[i] = arr[j];

 k--;

 break;

 }

 }

 }

 }

 

 // Our requrement not

 // satisied by performing

 // step 1. We need to

 // modify the position

 // which matches in

 // both String

 for (int i = 0;

 i < s1.length; i++) 

 {

 if (s1[i] == s3[i] && k > 0) 

 {

 

 // Finding the character

 // which is different

 // from both S1 and S2

 for (int j = 0; j < 3; j++) 

 {

 if (arr[j] != s1[i] &&

 arr[j] != s3[i]) 

 {

 s3[i] = arr[j];

 k--;

 break;

 }

 }

 }

 }

 

 // Resultant String

 System.out.print(new String(s3) + "\n");

 }

 }

}

 

// Driver Code

public static void main(String[] args)

{

 int N = 4, k = 2;

 

 // Given two Strings

 String S1 = "zzyy";

 String S2 = "zxxy";

 

 // Function Call

 findString(N, k, S1.toCharArray(), S2.toCharArray());

}

}

 

// This code is contributed by amal kumar choubey  
  
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

# Python3 program for the above approach

arr = [ 'a', 'b', 'c' ]

 

# Function to find the string which

# differ at exactly K positions

def findString(n, k, s1, s2):

 

 # Initialise s3 as s2

 s3 = s2

 s3 = list(s3)

 

 # Number of places at which

 # s3 differ from s2

 d = 0

 for i in range(len(s1)):

 if (s1[i] != s2[i]):

 d += 1

 

 # Minimum possible value

 # is ceil(d/2) if it is

 # not possible then -1

 if ((d + 1) // 2 > k):

 print ("-1")

 return

 

 else:

 

 # Case 2 when K is

 # less equal d

 if (k <= d):

 

 # Value of X and T

 # after solving

 # equations

 

 # T shows the number

 # of modification

 # such that position

 # differ from both

 

 # X show the modification

 # such that this position

 # only differ from only

 # one string

 X = d - k

 T = 2 * k - d

 

 for i in range(len(s3)):

 if (s1[i] != s2[i]):

 

 # Modify the position

 # such that this

 # differ from both

 # S1 & S2 & decrease

 # the T at each step

 if (T > 0):

 

 # Finding the character

 # which is different

 # from both S1 and S2

 for j in range(3):

 if (arr[j] != s1[i] and

 arr[j] != s2[i]):

 s3[i] = arr[j]

 T -= 1

 break

 

 # After we done T

 # start modification

 # to meet our

 # requirement

 # for X type

 elif (X > 0):

 s3[i] = s1[i]

 X -= 1

 

 # Resultant string

 print("".join(s3))

 

 else:

 

 # Case 1 when K > d

 # In first step, modify all

 # the character which are

 # not same in S1 and S3

 for i in range(len(s1)):

 if (s1[i] != s3[i]):

 for j in range(3):

 

 # Finding character

 # which is

 # different from

 # both S1 and S2

 if (arr[j] != s1[i] and

 arr[j] != s3[i]):

 s3[i] = arr[j]

 k -= 1

 break

 

 # Our requrement not

 # satisied by performing

 # step 1. We need to

 # modify the position

 # which matches in

 # both string

 for i in range(len(s1)):

 if (s1[i] == s3[i] and k):

 

 # Finding the character

 # which is different

 # from both S1 and S2

 for j in range (3):

 if (arr[j] != s1[i] and

 arr[j] != s3[i]):

 s3[i] = arr[j]

 k -= 1

 break

 

 # Resultant string

 print("".join(s3))

 

# Driver Code

if __name__ == "__main__":

 

 N = 4

 k = 2

 

 # Given two strings

 S1 = "zzyy"

 S2 = "zxxy"

 

 # Function call

 findString(N, k, S1, S2)

 

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

// C# program for the above approach

using System;

 

class GFG{

 

static char []arr = { 'a', 'b', 'c' };

 

// Function to find the String which

// differ at exactly K positions

static void findString(int n, int k,

 char []s1, 

 char []s2)

{

 

 // Initialise s3 as s2

 char []s3 = s2;

 

 // Number of places at which

 // s3 differ from s2

 int d = 0;

 for(int i = 0;

 i < s1.Length; i++)

 {

 if (s1[i] != s2[i])

 d++;

 }

 

 // Minimum possible value

 // is Math.Ceiling(d/2) if it is

 // not possible then -1

 if ((d + 1) / 2 > k) 

 {

 Console.Write("-1" + "\n");

 return;

 }

 else

 {

 

 // Case 2 when K is

 // less equal d

 if (k <= d) 

 {

 

 // Value of X and T

 // after solving

 // equations

 

 // T shows the number

 // of modification

 // such that position

 // differ from both

 

 // X show the modification

 // such that this position

 // only differ from only

 // one String

 int X = d - k;

 int T = 2 * k - d;

 

 for(int i = 0; i < s3.Length; i++) 

 {

 if (s1[i] != s2[i]) 

 {

 

 // Modify the position

 // such that this

 // differ from both

 // S1 & S2 & decrease

 // the T at each step

 if (T > 0) 

 {

 

 // Finding the character

 // which is different

 // from both S1 and S2

 for(int j = 0; j < 3; j++)

 {

 if (arr[j] != s1[i] && 

 arr[j] != s2[i]) 

 {

 s3[i] = arr[j];

 T--;

 break;

 }

 }

 }

 

 // After we done T start

 // modification to meet our

 // requirement for X type

 else if (X > 0) 

 {

 s3[i] = s1[i];

 X--;

 }

 }

 }

 

 // Resultant String

 Console.Write(new String(s3) + "\n");

 }

 else

 {

 

 // Case 1 when K > d

 // In first step, modify all

 // the character which are

 // not same in S1 and S3

 for(int i = 0; i < s1.Length; i++) 

 {

 if (s1[i] != s3[i]) 

 {

 for(int j = 0; j < 3; j++)

 {

 

 // Finding character

 // which is different

 // from both S1 and S2

 if (arr[j] != s1[i] &&

 arr[j] != s3[i]) 

 {

 s3[i] = arr[j];

 k--;

 break;

 }

 }

 }

 }

 

 // Our requrement not

 // satisied by performing

 // step 1. We need to

 // modify the position

 // which matches in

 // both String

 for(int i = 0; i < s1.Length; i++) 

 {

 if (s1[i] == s3[i] && k > 0) 

 {

 

 // Finding the character

 // which is different

 // from both S1 and S2

 for(int j = 0; j < 3; j++)

 {

 if (arr[j] != s1[i] &&

 arr[j] != s3[i]) 

 {

 s3[i] = arr[j];

 k--;

 break;

 }

 }

 }

 }

 

 // Resultant String

 Console.Write(new String(s3) + "\n");

 }

 }

}

 

// Driver Code

public static void Main(String[] args)

{

 int N = 4, k = 2;

 

 // Given two Strings

 String S1 = "zzyy";

 String S2 = "zxxy";

 

 // Function Call

 findString(N, k, S1.ToCharArray(), 

 S2.ToCharArray());

}

}

 

// This code is contributed by amal kumar choubey  
  
---  
  
 __

 __

 **Output:**

    
    
    zaay
    

**Time Complexity:** _O(N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

