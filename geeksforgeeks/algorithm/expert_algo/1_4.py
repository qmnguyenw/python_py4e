Count of subsequences of length 4 in form (x, x, x+1, x+1) | Set 2



Given a large number in form of string **str** of size **N** , the task is to
count the subsequence of length 4 whose digit are in the form of **(x, x, x+1,
x+1)**.  
 **Example:**

>  **Input:** str = “1515732322”  
> **Output:** 3  
> **Explanation:**  
> For the given input string str = “1515732322”, there are 3 subsequence
> {1122}, {1122}, and {1122} which are in the given form of (x, x, x+1, x+1).
>
>  **Input:** str = “224353”  
> **Output:** 1  
> **Explanation:**  
> For the given input string str = “224353”, there is only 1 subsequence
> possible {2233} in the given form of (x, x, x+1, x+1).

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Prefix Sum Approach:** Please refer to the Set 1, for the Prefix sum
approach.

 **Dynamic Programming Approach:** This problem can be solved using Dynamic
Programming.  
We will be using 2 arrays as **count1[][j]** and **count2[][10]** such that
**count1[i][10]** will store the count of consecutive equal element of **digit
j** at current index **i** traversing string from left and **count2[i][j]**
will store the count of consecutive equal element of **digit j** at current
index i traversing string from right. Below are the steps:

  

  

  * Initialize two count array **count1[][10]** for filling table from left to right and **count2[][10]** for filling table from right to left of input string.
  * Traverse input string and fill the both count1 and count2 array.
  * Recurrence Relation for **count1[][]** is given by:

> count1[i][j] += count1[i – 1][j]  
> where count1[i][j] is the count of two adjacent at index i for digit j

  * Recurrence Relation for **count2[][]** is given by:

> count2[i][j] += count1[i + 1][j]  
> where count2[i][j] is the count of two adjacent at index i for digit j

  * Initialize a variable **ans to 0** that stores the resultant count of stable numbers.
  * Traverse the input string and get the count of numbers from **count1[][]** and **count2[][]** array such that difference between number from **count1[][]** and **count2[][]** array is 1 and store it in variable **c1** and **c2.**
  * Finally update result(say **ans** ) with **(c1 * ((c2 * (c2 – 1) / 2)))**.
  * Print the answer **ans** calculated above.

Below is the implementation of above approach:

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

// Function to count the numbers

int countStableNum(string str, int N)

{

 // Array that stores the

 // digits from left to right

 int count1[N][10];

 // Array that stores the

 // digits from right to left

 int count2[N][10];

 // Initially both array store zero

 for (int i = 0; i < N; i++)

 for (int j = 0; j < 10; j++)

 count1[i][j] = count2[i][j] = 0;

 // Fill the table for count1 array

 for (int i = 0; i < N; i++) {

 if (i != 0) {

 for (int j = 0; j < 10; j++) {

 count1[i][j] += count1[i - 1][j];

 }

 }

 // Update the count of current character

 count1[i][str[i] - '0']++;

 }

 // Fill the table for count2 array

 for (int i = N - 1; i >= 0; i--) {

 if (i != N - 1) {

 for (int j = 0; j < 10; j++) {

 count2[i][j] += count2[i + 1][j];

 }

 }

 // Update the count of cuuent character

 count2[i][str[i] - '0']++;

 }

 // Variable that stores the

 // count of the numbers

 int ans = 0;

 // Traverse Input string and get the

 // count of digits from count1 and

 // count2 array such that difference

 // b/w digit is 1 & store it int c1 &c2.;

 // And store it in variable c1 and c2

 for (int i = 1; i < N - 1; i++) {

 if (str[i] == '9')

 continue;

 int c1 = count1[i - 1][str[i] - '0'];

 int c2 = count2[i + 1][str[i] - '0' + 1];

 if (c2 == 0)

 continue;

 // Update the ans

 ans = (ans

 + (c1 * ((c2 * (c2 - 1) / 2))));

 }

 // Return the final count

 return ans;

}

// Driver Code

int main()

{

 // Given String

 string str = "224353";

 int N = str.length();

 // Function Call

 cout << countStableNum(str, N);

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

import java.io.*;

class GFG{

// Function to count the numbers

static int countStableNum(String str, int N)

{

 

 // Array that stores the

 // digits from left to right

 int count1[][] = new int[N][10];

 

 // Array that stores the

 // digits from right to left

 int count2[][] = new int[N][10];

 

 // Initially both array store zero

 for(int i = 0; i < N; i++)

 for(int j = 0; j < 10; j++)

 count1[i][j] = count2[i][j] = 0;

 

 // Fill the table for count1 array

 for(int i = 0; i < N; i++)

 {

 if (i != 0)

 {

 for(int j = 0; j < 10; j++)

 {

 count1[i][j] += count1[i - 1][j];

 }

 }

 

 // Update the count of current character

 count1[i][str.charAt(i) - '0']++;

 }

 

 // Fill the table for count2 array

 for(int i = N - 1; i >= 0; i--)

 {

 if (i != N - 1)

 {

 for(int j = 0; j < 10; j++)

 {

 count2[i][j] += count2[i + 1][j];

 }

 }

 

 // Update the count of cuuent character

 count2[i][str.charAt(i) - '0']++;

 }

 

 // Variable that stores the

 // count of the numbers

 int ans = 0;

 

 // Traverse Input string and get the

 // count of digits from count1 and

 // count2 array such that difference

 // b/w digit is 1 & store it int c1 &c2.;

 // And store it in variable c1 and c2

 for(int i = 1; i < N - 1; i++)

 {

 if (str.charAt(i) == '9')

 continue;

 

 int c1 = count1[i - 1][str.charAt(i) - '0'];

 int c2 = count2[i + 1][str.charAt(i) - '0' + 1];

 

 if (c2 == 0)

 continue;

 

 // Update the ans

 ans = (ans + (c1 * ((c2 * (c2 - 1) / 2))));

 }

 

 // Return the final count

 return ans;

}

// Driver code

public static void main(String[] args)

{

 

 // Given String

 String str = "224353";

 int N = str.length();

 

 // Function call

 System.out.println(countStableNum(str, N));

}

}

// This code is contributed by Pratima Pandey  
  
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

# Function to count the numbers

def countStableNum(Str, N):

 # Array that stores the

 # digits from left to right

 count1 = [[0 for j in range(10)]

 for i in range(N)]

 

 # Array that stores the

 # digits from right to left

 count2 = [[0 for j in range(10)]

 for i in range(N)]

 

 # Initially both array store zero

 for i in range(N):

 for j in range(10):

 count1[i][j], count2[i][j] = 0, 0

 

 # Fill the table for count1 array

 for i in range(N):

 if (i != 0):

 for j in range(10):

 count1[i][j] = (count1[i][j] +

 count1[i - 1][j])

 

 # Update the count of current character

 count1[i][ord(Str[i]) - ord('0')] += 1

 

 # Fill the table for count2 array

 for i in range(N - 1, -1, -1):

 if (i != N - 1):

 for j in range(10): 

 count2[i][j] += count2[i + 1][j]

 

 # Update the count of cuuent character

 count2[i][ord(Str[i]) -

 ord('0')] = count2[i][ord(Str[i]) -

 ord('0')] + 1

 

 # Variable that stores the

 # count of the numbers

 ans = 0

 

 # Traverse Input string and get the

 # count of digits from count1 and

 # count2 array such that difference

 # b/w digit is 1 & store it int c1 &c2.;

 # And store it in variable c1 and c2

 for i in range(1, N - 1):

 if (Str[i] == '9'):

 continue

 

 c1 = count1[i - 1][ord(Str[i]) - ord('0')]

 c2 = count2[i + 1][ord(Str[i]) - ord('0') +
1]

 

 if (c2 == 0):

 continue

 

 # Update the ans

 ans = (ans + (c1 * ((c2 * (c2 - 1) // 2))))

 

 # Return the final count

 return ans

 

# Driver code

# Given String

Str = "224353"

N = len(Str)

# Function call

print(countStableNum(Str, N))

# This code is contributed by divyeshrabadiya07  
  
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

// Function to count the numbers

static int countStableNum(String str, int N)

{

 

 // Array that stores the

 // digits from left to right

 int [,]count1 = new int[N, 10];

 

 // Array that stores the

 // digits from right to left

 int [,]count2 = new int[N, 10];

 

 // Initially both array store zero

 for(int i = 0; i < N; i++)

 for(int j = 0; j < 10; j++)

 count1[i, j] = count2[i, j] = 0;

 

 // Fill the table for count1 array

 for(int i = 0; i < N; i++)

 {

 if (i != 0)

 {

 for(int j = 0; j < 10; j++)

 {

 count1[i, j] += count1[i - 1, j];

 }

 }

 // Update the count of current character

 count1[i, str[i] - '0']++;

 }

 // Fill the table for count2 array

 for(int i = N - 1; i >= 0; i--)

 {

 if (i != N - 1)

 {

 for(int j = 0; j < 10; j++)

 {

 count2[i, j] += count2[i + 1, j];

 }

 }

 

 // Update the count of cuuent character

 count2[i, str[i] - '0']++;

 }

 

 // Variable that stores the

 // count of the numbers

 int ans = 0;

 

 // Traverse Input string and get the

 // count of digits from count1 and

 // count2 array such that difference

 // b/w digit is 1 & store it int c1 &c2.;

 // And store it in variable c1 and c2

 for(int i = 1; i < N - 1; i++)

 {

 if (str[i] == '9')

 continue;

 

 int c1 = count1[i - 1, str[i] - '0'];

 int c2 = count2[i + 1, str[i] - '0' + 1];

 

 if (c2 == 0)

 continue;

 

 // Update the ans

 ans = (ans + (c1 * ((c2 * (c2 - 1) / 2))));

 }

 

 // Return the readonly count

 return ans;

}

// Driver code

public static void Main(String[] args)

{

 

 // Given String

 String str = "224353";

 int N = str.Length;

 

 // Function call

 Console.WriteLine(countStableNum(str, N));

}

}

// This code is contributed by Amit Katiyar  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    
    
    
    
    

**Time Complexity:** _O(N)_  
**Auxiliary Space Complexity:** _O(N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

