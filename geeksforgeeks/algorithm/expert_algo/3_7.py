Number of balanced bracket expressions that can be formed from a string



Given a string **str** comprising of characters **(** , **)** , **{** , **}**
, **[** , **]** and **?**. The task is to find the total number of balanced
bracket expressions formed when **?** can be replaced with any of the bracket
characters.  
Here are some examples of balanced bracket expressions: **{([])}** ,
**{()}[{}]** etc.  
And, unbalanced bracket expressions: **{[}** , **{()]** , **{()}[)** etc.

 **Examples:**

>  **Input:** str = “(?([?)]?}?”  
>  **Output:** 3  
> ({([()]]}), ()([()]{}) and ([([])]{}) are the only possible balanced
> expressions that can be generated from the input.
>
>  **Input:** str = “???[???????]????”  
>  **Output:** 392202

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  1. If **n** is **odd** then the result will always be **0** as there will be no balanced expression possible.
  2. If **n** id **even** then create a **dp** array for storing precomputations.
  3. Call a recursive function with following operations:
    * If **starting index > ending index** then return **1**.
    * If **dp[start][end]** is already computed return **dp[start][end]**.
    * Run a loop from **start + 1** till **end** incrementing by **2** to find its pair bracket or ‘?’.
    * Then divide the string into two halves for checking proper subsequent bracket expressions from **start + 1** till **i – 1** and **i + 1** till end by calling the recursive function.
    * If **st[start] = ’?’** and **st[i] = ’?’** then a total of **3** combinations of bracket pairs can be formed thus multiplying the result of the recursive function by **3**.
  4. Return dp[start][end]

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find number of balanced

// bracket expressions possible

#include <bits/stdc++.h>

using namespace std;

typedef long long int lli;

 

// Max string length

const int MAX = 300;

 

// Function to check whether index start

// and end can form a bracket pair or not

int checkFunc(int i, int j, string st)

{

 // Check for brackets ( )

 if (st[i] == '(' && st[j] == ')')

 return 1;

 if (st[i] == '(' && st[j] == '?')

 return 1;

 if (st[i] == '?' && st[j] == ')')

 return 1;

 

 // Check for brackets [ ]

 if (st[i] == '[' && st[j] == ']')

 return 1;

 if (st[i] == '[' && st[j] == '?')

 return 1;

 if (st[i] == '?' && st[j] == ']')

 return 1;

 

 // Check for brackets { }

 if (st[i] == '{' && st[j] == '}')

 return 1;

 if (st[i] == '{' && st[j] == '?')

 return 1;

 if (st[i] == '?' && st[j] == '}')

 return 1;

 

 return 0;

}

 

// Function to find number of

// proper bracket expressions

int countRec(int start, int end, int dp[][MAX],

 string st)

{

 int sum = 0;

 

 // If starting index is greater

 // than ending index

 if (start > end)

 return 1;

 

 // If dp[start][end] has already been computed

 if (dp[start][end] != -1)

 return dp[start][end];

 

 lli i, r = 0;

 

 // Search for the bracket in from next index

 for (i = start + 1; i <= end; i += 2) {

 

 // If bracket pair is formed,

 // add number of combination

 if (checkFunc(start, i, st)) {

 

 sum = sum

 + countRec(start + 1, i - 1, dp, st)

 * countRec(i + 1, end, dp, st);

 }

 

 // If ? comes then all three bracket

 // expressions are possible

 else if (st[start] == '?' && st[i] == '?') {

 

 sum = sum

 + countRec(start + 1, i - 1, dp, st)

 * countRec(i + 1, end, dp, st)

 * 3;

 }

 }

 

 // Return answer

 return dp[start][end] = sum;

}

 

int countWays(string st)

{

 int n = st.length();

 

 // If n is odd, string cannot be balanced

 if (n % 2 == 1)

 return 0;

 int dp[MAX][MAX];

 memset(dp, -1, sizeof(dp));

 return countRec(0, n - 1, dp, st);

}

 

// Driving function

int main()

{

 string st = "(?([?)]?}?";

 cout << countWays(st);

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

// Java program to find number of balanced

// bracket expressions possible

 

class GFG {

 // Max string length

 static int MAX = 300;

 

 // Function to check whether index start

 // and end can form a bracket pair or not

 static int checkFunc(int i, int j, String st)

 {

 // Check for brackets ( )

 if (st.charAt(i) == '(' && st.charAt(j) == ')')

 return 1;

 if (st.charAt(i) == '(' && st.charAt(j) == '?')

 return 1;

 if (st.charAt(i) == '?' && st.charAt(j) == ')')

 return 1;

 

 // Check for brackets [ ]

 if (st.charAt(i) == '[' && st.charAt(j) == ']')

 return 1;

 if (st.charAt(i) == '[' && st.charAt(j) == '?')

 return 1;

 if (st.charAt(i) == '?' && st.charAt(j) == ']')

 return 1;

 

 // Check for brackets { }

 if (st.charAt(i) == '{' && st.charAt(j) == '}')

 return 1;

 if (st.charAt(i) == '{' && st.charAt(j) == '?')

 return 1;

 if (st.charAt(i) == '?' && st.charAt(j) == '}')

 return 1;

 

 return 0;

 }

 

 // Function to find number of

 // proper bracket expressions

 static int countRec(int start, int end, int dp[][],

 String st)

 {

 int sum = 0;

 

 // If starting index is greater

 // than ending index

 if (start > end)

 return 1;

 

 // If dp[start][end] has already been computed

 if (dp[start][end] != -1)

 return dp[start][end];

 

 int i, r = 0;

 

 // Search for the bracket in from next index

 for (i = start + 1; i <= end; i += 2) {

 

 // If bracket pair is formed,

 // add number of combination

 if (checkFunc(start, i, st) == 1) {

 

 sum = sum

 + countRec(start + 1, i - 1, dp, st)

 * countRec(i + 1, end, dp, st);

 }

 

 // If ? comes then all three bracket

 // expressions are possible

 else if (st.charAt(start) == '?' && st.charAt(i) == '?') {

 

 sum = sum

 + countRec(start + 1, i - 1, dp, st)

 * countRec(i + 1, end, dp, st)

 * 3;

 }

 }

 

 // Return answer

 return dp[start][end] = sum;

 }

 

 static int countWays(String st)

 {

 int n = st.length();

 

 // If n is odd, string cannot be balanced

 if (n % 2 == 1)

 return 0;

 

 int dp[][] = new int[MAX][MAX];

 

 for (int i = 0; i < MAX; i++)

 for (int j = 0; j < MAX; j++)

 dp[i][j] = -1;

 

 return countRec(0, n - 1, dp, st);

 }

 

 // Driving function

 public static void main(String[] args)

 {

 

 String st = "(?([?)]?}?";

 System.out.println(countWays(st));

 }

}

 

// This code is contributed by ihritik  
  
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

# Python 3 program to find number of balanced

# bracket expressions possible

 

# Max string length

MAX = 300

 

# Function to check whether index start

# and end can form a bracket pair or not

def checkFunc(i, j, st):

 

 # Check for brackets ( )

 if (st[i] == '(' and st[j] == ')'):

 return 1

 if (st[i] == '(' and st[j] == '?'):

 return 1

 if (st[i] == '?' and st[j] == ')'):

 return 1

 

 # Check for brackets [ ]

 if (st[i] == '[' and st[j] == ']'):

 return 1

 if (st[i] == '[' and st[j] == '?'):

 return 1

 if (st[i] == '?' and st[j] == ']'):

 return 1

 

 # Check for brackets { }

 if (st[i] == '{' and st[j] == '}'):

 return 1

 if (st[i] == '{' and st[j] == '?'):

 return 1

 if (st[i] == '?' and st[j] == '}'):

 return 1

 

 return 0

 

# Function to find number of

# proper bracket expressions

def countRec(start, end, dp, st):

 

 sum = 0

 

 # If starting index is greater

 # than ending index

 if (start > end):

 return 1

 

 # If dp[start][end] has already

 # been computed

 if (dp[start][end] != -1):

 return dp[start][end]

 

 r = 0

 

 # Search for the bracket in from next index

 for i in range(start + 1, end + 1, 2):

 

 # If bracket pair is formed,

 # add number of combination

 if (checkFunc(start, i, st)):

 

 sum = (sum + countRec(start + 1, i - 1, dp, st) *

 countRec(i + 1, end, dp, st))

 

 # If ? comes then all three bracket

 # expressions are possible

 elif (st[start] == '?' and st[i] == '?'):

 

 sum = (sum + countRec(start + 1, i - 1, dp, st) *

 countRec(i + 1, end, dp, st) * 3)

 

 # Return answer

 dp[start][end] = sum

 return dp[start][end]

 

def countWays( st):

 

 n = len(st)

 

 # If n is odd, string cannot be balanced

 if (n % 2 == 1):

 return 0

 dp = [[-1 for i in range(MAX)]

 for i in range(MAX)]

 return countRec(0, n - 1, dp, st)

 

# Driver Code

if __name__ =="__main__":

 

 st = "(?([?)]?}?"

 print(countWays(st))

 

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

// C# program to find number of balanced

// bracket expressions possible

 

using System;

class GFG {

 // Max string length

 static int MAX = 300;

 

 // Function to check whether index start

 // and end can form a bracket pair or not

 static int checkFunc(int i, int j, string st)

 {

 // Check for brackets ( )

 if (st[i] == '(' && st[j] == ')')

 return 1;

 if (st[i] == '(' && st[j] == '?')

 return 1;

 if (st[i] == '?' && st[j] == ')')

 return 1;

 

 // Check for brackets [ ]

 if (st[i] == '[' && st[j] == ']')

 return 1;

 if (st[i] == '[' && st[j] == '?')

 return 1;

 if (st[i] == '?' && st[j] == ']')

 return 1;

 

 // Check for brackets { }

 if (st[i] == '{' && st[j] == '}')

 return 1;

 if (st[i] == '{' && st[j] == '?')

 return 1;

 if (st[i] == '?' && st[j] == '}')

 return 1;

 

 return 0;

 }

 

 // Function to find number of

 // proper bracket expressions

 static int countRec(int start, int end, int[, ] dp,

 string st)

 {

 int sum = 0;

 

 // If starting index is greater

 // than ending index

 if (start > end)

 return 1;

 

 // If dp[start, end] has already been computed

 if (dp[start, end] != -1)

 return dp[start, end];

 

 int i;

 

 // Search for the bracket in from next index

 for (i = start + 1; i <= end; i += 2) {

 

 // If bracket pair is formed,

 // add number of combination

 if (checkFunc(start, i, st) == 1) {

 

 sum = sum

 + countRec(start + 1, i - 1, dp, st)

 * countRec(i + 1, end, dp, st);

 }

 

 // If ? comes then all three bracket

 // expressions are possible

 else if (st[start] == '?' && st[i] == '?') {

 

 sum = sum

 + countRec(start + 1, i - 1, dp, st)

 * countRec(i + 1, end, dp, st)

 * 3;

 }

 }

 

 // Return answer

 return dp[start, end] = sum;

 }

 

 static int countWays(string st)

 {

 int n = st.Length;

 

 // If n is odd, string cannot be balanced

 if (n % 2 == 1)

 return 0;

 

 int[, ] dp = new int[MAX, MAX];

 

 for (int i = 0; i < MAX; i++)

 for (int j = 0; j < MAX; j++)

 dp[i, j] = -1;

 

 return countRec(0, n - 1, dp, st);

 }

 

 // Driving function

 public static void Main()

 {

 

 string st = "(?([?)]?}?";

 Console.WriteLine(countWays(st));

 }

}

 

// This code is contributed by ihritik  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

