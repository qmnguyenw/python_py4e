Longest subsequence such that adjacent elements have at least one common digit



Given an array **arr[]** of **N** integers, the task is to find the length of
the longest sub-sequence such that adjacent elements of the sub-sequence have
at least one digit in common.

 **Examples:**

>  **Input:** arr[] = {1, 12, 44, 29, 33, 96, 89}  
>  **Output:** 5  
> The longest sub-sequence is {1 12 29 96 89}
>
>  **Input:** arr[] = {12, 23, 45, 43, 36, 97}  
>  **Output:** 4  
> The longest sub-sequence is {12 23 43 36}

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to store the length of longest sub-sequence for
each digit present in an element of the array.

  

  

* dp[i][d] represents the length of the longest sub-sequence up to ith element if digit d is the common digit.
* Declare a cnt array and set cnt[d] = 1 for each digit present in current element.
* Consider each digit d as common digit and find maximum length sub-sequence ending at arr[i] as dp[i][d] = max(dp[j][d]+1) (0<=j<i).
* Also find a local maximum max(dp[i][d]) for current element.
* After finding local maximum update dp[i][d] for all digits present in the current element to a local maximum.
* This is required as local maximum represents maximum length sub-sequence for an element having digit d.

>  **E.g.** Consider arr[] = {24, 49, 96}.  
> The local maximum for 49 is 2 obtain from digit 4.  
> This local maximum will be used in finding the local maximum for 96 with
> common digit 9.  
> For that it is required for all digits in 49, dp[i][d] should be set to
> local maximum.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find maximum length subsequence

// such that adjacent elements have at least

// one common digit

#include <bits/stdc++.h>

using namespace std;

 

// Returns length of maximum length subsequence

int findSubsequence(int arr[], int n)

{

 

 // To store the length of the

 // maximum length subsequence

 int len = 1;

 

 // To store current element arr[i]

 int tmp;

 

 int i, j, d;

 

 // To store the length of the sub-sequence

 // ending at index i and having common digit d

 int dp[n][10];

 

 memset(dp, 0, sizeof(dp));

 

 // To store digits present in current element

 int cnt[10];

 

 // To store length of maximum length subsequence

 // ending at index i

 int locMax;

 

 // For first element maximum length is 1 for

 // each digit

 tmp = arr[0];

 while (tmp > 0) {

 dp[0][tmp % 10] = 1;

 tmp /= 10;

 }

 

 // Find digits of each element, then find length

 // of subsequence for each digit and then find

 // local maximum

 for (i = 1; i < n; i++) {

 tmp = arr[i];

 locMax = 1;

 memset(cnt, 0, sizeof(cnt));

 

 // Find digits in current element

 while (tmp > 0) {

 cnt[tmp % 10] = 1;

 tmp /= 10;

 }

 

 // For each digit present find length of

 // subsequence and find local maximum

 for (d = 0; d <= 9; d++) {

 if (cnt[d]) {

 dp[i][d] = 1;

 for (j = 0; j < i; j++) {

 dp[i][d] = max(dp[i][d], dp[j][d] + 1);

 locMax = max(dp[i][d], locMax);

 }

 }

 }

 

 // Update value of dp[i][d] for each digit

 // present in current element to local maximum

 // found.

 for (d = 0; d <= 9; d++) {

 if (cnt[d]) {

 dp[i][d] = locMax;

 }

 }

 

 // Update maximum length with local maximum

 len = max(len, locMax);

 }

 

 return len;

}

 

// Driver code

int main()

{

 int arr[] = { 1, 12, 44, 29, 33, 96, 89 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << findSubsequence(arr, n);

 

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

// Java program to find maximum length subsequence

// such that adjacent elements have at least

// one common digit

 

class GFG

{

 

// Returns length of maximum length subsequence

static int findSubsequence(int arr[], int n)

{

 

 // To store the length of the

 // maximum length subsequence

 int len = 1;

 

 // To store current element arr[i]

 int tmp;

 

 int i, j, d;

 

 // To store the length of the sub-sequence

 // ending at index i and having common digit d

 int[][] dp = new int[n][10];

 

 

 // To store digits present in current element

 int[] cnt = new int[10];

 

 // To store length of maximum length subsequence

 // ending at index i

 int locMax;

 

 // For first element maximum length is 1 for

 // each digit

 tmp = arr[0];

 while (tmp > 0) 

 {

 dp[0][tmp % 10] = 1;

 tmp /= 10;

 }

 

 // Find digits of each element, then find length

 // of subsequence for each digit and then find

 // local maximum

 for (i = 1; i < n; i++) 

 {

 tmp = arr[i];

 locMax = 1;

 for (int x = 0; x < 10; x++)

 cnt[x]=0;

 

 // Find digits in current element

 while (tmp > 0) 

 {

 cnt[tmp % 10] = 1;

 tmp /= 10;

 }

 

 // For each digit present find length of

 // subsequence and find local maximum

 for (d = 0; d <= 9; d++)

 {

 if (cnt[d] > 0)

 {

 dp[i][d] = 1;

 for (j = 0; j < i; j++) 

 {

 dp[i][d] = Math.max(dp[i][d], dp[j][d] + 1);

 locMax = Math.max(dp[i][d], locMax);

 }

 }

 }

 

 // Update value of dp[i][d] for each digit

 // present in current element to local maximum

 // found.

 for (d = 0; d <= 9; d++)

 {

 if (cnt[d] > 0)

 {

 dp[i][d] = locMax;

 }

 }

 

 // Update maximum length with local maximum

 len = Math.max(len, locMax);

 }

 

 return len;

}

 

// Driver code

public static void main (String[] args) 

{

 int arr[] = { 1, 12, 44, 29, 33, 96, 89 };

 int n = arr.length;

 

 System.out.println(findSubsequence(arr, n));

}

}

 

// This code is contributed by mits  
  
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

# Python3 program to find maximum

# Length subsequence such that 

# adjacent elements have at least

# one common digit

 

# Returns Length of maximum 

# Length subsequence

def findSubsequence(arr, n):

 

 # To store the Length of the

 # maximum Length subsequence

 Len = 1

 

 # To store current element arr[i]

 tmp = 0

 

 i, j, d = 0, 0, 0

 

 # To store the Length of the sub-sequence

 # ending at index i and having common digit d

 dp = [[0 for i in range(10)] 

 for i in range(n)]

 

 # To store digits present in current element

 cnt = [0 for i in range(10)]

 

 # To store Length of maximum 

 # Length subsequence ending at index i

 locMax = 0

 

 # For first element maximum 

 # Length is 1 for each digit

 tmp = arr[0]

 while (tmp > 0):

 dp[0][tmp % 10] = 1

 tmp //= 10

 

 # Find digits of each element, 

 # then find Length of subsequence 

 # for each digit and then find

 # local maximum

 for i in range(1, n):

 tmp = arr[i]

 locMax = 1

 cnt = [0 for i in range(10)]

 

 # Find digits in current element

 while (tmp > 0):

 cnt[tmp % 10] = 1

 tmp //= 10

 

 # For each digit present find Length of

 # subsequence and find local maximum

 for d in range(10):

 if (cnt[d]):

 dp[i][d] = 1

 for j in range(i):

 dp[i][d] = max(dp[i][d], 

 dp[j][d] + 1)

 locMax = max(dp[i][d], locMax)

 

 # Update value of dp[i][d] for each digit

 # present in current element to local 

 # maximum found.

 for d in range(10):

 if (cnt[d]):

 dp[i][d] = locMax

 

 # Update maximum Length 

 # with local maximum

 Len = max(Len, locMax)

 return Len

 

# Driver code

arr = [1, 12, 44, 29, 33, 96, 89]

n = len(arr)

 

print(findSubsequence(arr, n))

 

# This code is contributed 

# by mohit kumar  
  
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

// C# program to find maximum length subsequence

// such that adjacent elements have at least

// one common digit

using System;

 

class GFG

{

 

// Returns length of maximum length subsequence

static int findSubsequence(int []arr, int n)

{

 

 // To store the length of the

 // maximum length subsequence

 int len = 1;

 

 // To store current element arr[i]

 int tmp;

 

 int i, j, d;

 

 // To store the length of the sub-sequence

 // ending at index i and having common digit d

 int[,] dp = new int[n, 10];

 

 

 // To store digits present in current element

 int[] cnt = new int[10];

 

 // To store length of maximum length subsequence

 // ending at index i

 int locMax;

 

 // For first element maximum length is 1 for

 // each digit

 tmp = arr[0];

 while (tmp > 0) 

 {

 dp[0, tmp % 10] = 1;

 tmp /= 10;

 }

 

 // Find digits of each element, then find length

 // of subsequence for each digit and then find

 // local maximum

 for (i = 1; i < n; i++) 

 {

 tmp = arr[i];

 locMax = 1;

 for (int x = 0; x < 10; x++)

 cnt[x] = 0;

 

 // Find digits in current element

 while (tmp > 0) 

 {

 cnt[tmp % 10] = 1;

 tmp /= 10;

 }

 

 // For each digit present find length of

 // subsequence and find local maximum

 for (d = 0; d <= 9; d++)

 {

 if (cnt[d] > 0)

 {

 dp[i, d] = 1;

 for (j = 0; j < i; j++) 

 {

 dp[i, d] = Math.Max(dp[i, d], dp[j, d] + 1);

 locMax = Math.Max(dp[i, d], locMax);

 }

 }

 }

 

 // Update value of dp[i,d] for each digit

 // present in current element to local maximum

 // found.

 for (d = 0; d <= 9; d++)

 {

 if (cnt[d] > 0)

 {

 dp[i, d] = locMax;

 }

 }

 

 // Update maximum length with local maximum

 len = Math.Max(len, locMax);

 }

 

 return len;

}

 

// Driver code

public static void Main() 

{

 int []arr = { 1, 12, 44, 29, 33, 96, 89 };

 int n = arr.Length;

 

 Console.WriteLine(findSubsequence(arr, n));

}

}

 

// This code is contributed by mits  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

**Time Complexity:** O(n2)  
 **Auxiliary Space:** O(n)

The auxiliary space required for above solution can be further reduced.
Observe that for each digit d present in arr[i], it is required to find
maximum length sub-sequence upto that digit irrespective of the fact that at
which element the sub-sequence end. This reduces auxiliary space required to
O(1). For each arr[i], find local maximum and update dig[d] for each digit d
in arr[i] to local maximum.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find maximum length subsequence

// such that adjacent elements have at least

// one common digit

#include <bits/stdc++.h>

using namespace std;

 

// Returns length of maximum length subsequence

int findSubsequence(int arr[], int n)

{

 

 // To store length of maximum length subsequence

 int len = 1;

 

 // To store current element arr[i]

 int tmp;

 

 int i, j, d;

 

 // To store length of subsequence

 // having common digit d

 int dp[10];

 

 memset(dp, 0, sizeof(dp));

 

 // To store digits present in current element

 int cnt[10];

 

 // To store local maximum for current element

 int locMax;

 

 // For first element maximum length is 1 for

 // each digit

 tmp = arr[0];

 while (tmp > 0) {

 dp[tmp % 10] = 1;

 tmp /= 10;

 }

 

 // Find digits of each element, then find length

 // of subsequence for each digit and then find

 // local maximum

 for (i = 1; i < n; i++) {

 tmp = arr[i];

 locMax = 1;

 memset(cnt, 0, sizeof(cnt));

 

 // Find digits in current element

 while (tmp > 0) {

 cnt[tmp % 10] = 1;

 tmp /= 10;

 }

 

 // For each digit present find length of

 // subsequence and find local maximum

 for (d = 0; d <= 9; d++) {

 if (cnt[d]) {

 dp[d]++;

 locMax = max(locMax, dp[d]);

 }

 }

 

 // Update value of dp[d] for each digit

 // present in current element to local maximum

 // found

 for (d = 0; d <= 9; d++) {

 if (cnt[d]) {

 dp[d] = locMax;

 }

 }

 

 // Update maximum length with local maximum

 len = max(len, locMax);

 }

 

 return len;

}

 

// Driver code

int main()

{

 int arr[] = { 1, 12, 44, 29, 33, 96, 89 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << findSubsequence(arr, n);

 

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

// Java program to find maximum length subsequence

// such that adjacent elements have at least 

// one common digit 

import java.util.*;

 

class GFG 

{

 

// Returns length of maximum length subsequence 

static int findSubsequence(int arr[], int n) 

{ 

 

 // To store length of maximum length subsequence 

 int len = 1; 

 

 // To store current element arr[i] 

 int tmp; 

 

 int i, j, d; 

 

 // To store length of subsequence 

 // having common digit d 

 int dp[] = new int[10]; 

 

 

 // To store digits present in current element 

 int cnt[] = new int[10]; 

 

 // To store local maximum for current element 

 int locMax; 

 

 // For first element maximum length is 1 for 

 // each digit 

 tmp = arr[0]; 

 while (tmp > 0) 

 { 

 dp[tmp % 10] = 1; 

 tmp /= 10; 

 } 

 

 // Find digits of each element, then find length 

 // of subsequence for each digit and then find 

 // local maximum 

 for (i = 1; i < n; i++) 

 { 

 tmp = arr[i]; 

 locMax = 1; 

 Arrays.fill(cnt, 0);

 

 // Find digits in current element 

 while (tmp > 0) 

 { 

 cnt[tmp % 10] = 1; 

 tmp /= 10; 

 } 

 

 // For each digit present find length of 

 // subsequence and find local maximum 

 for (d = 0; d <= 9; d++) 

 { 

 if (cnt[d] == 1) 

 { 

 dp[d]++; 

 locMax = Math.max(locMax, dp[d]); 

 } 

 } 

 

 // Update value of dp[d] for each digit 

 // present in current element to local maximum 

 // found 

 for (d = 0; d <= 9; d++) 

 { 

 if (cnt[d] == 1) 

 { 

 dp[d] = locMax; 

 } 

 } 

 

 // Update maximum length with local maximum 

 len = Math.max(len, locMax); 

 } 

 

 return len; 

} 

 

// Driver code 

public static void main(String[] args) 

{

 int arr[] = { 1, 12, 44, 29, 33, 96, 89 }; 

 int n = arr.length; 

 System.out.print(findSubsequence(arr, n)); 

}

}

 

/* This code contributed by PrinciRaj1992 */  
  
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

# Python3 program to find maximum length

# subsequence such that adjacent elements 

# have at least one common digit 

 

# Returns length of maximum

# length subsequence 

def findSubsequence(arr, n) :

 

 # To store length of maximum 

 # length subsequence 

 length = 1; 

 

 # To store length of subsequence 

 # having common digit d 

 dp = [0] * 10; 

 

 # For first element maximum length

 # is 1 for each digit 

 tmp = arr[0]; 

 while (tmp > 0) : 

 dp[tmp % 10] = 1; 

 tmp //= 10; 

 

 

 # Find digits of each element, then

 # find length of subsequence for each 

 # digit and then find local maximum 

 for i in range(1, n) :

 tmp = arr[i]; 

 locMax = 1;

 cnt = [0] * 10

 

 # Find digits in current element 

 while (tmp > 0) :

 cnt[tmp % 10] = 1; 

 tmp //= 10; 

 

 # For each digit present find length of 

 # subsequence and find local maximum 

 for d in range(10) : 

 if (cnt[d]) : 

 dp[d] += 1; 

 locMax = max(locMax, dp[d]); 

 

 # Update value of dp[d] for each digit 

 # present in current element to local 

 # maximum found 

 for d in range(10) : 

 if (cnt[d]) :

 dp[d] = locMax; 

 

 # Update maximum length with local 

 # maximum 

 length = max(length, locMax); 

 

 return length; 

 

# Driver code 

if __name__ == "__main__" :

 arr = [ 1, 12, 44, 29, 33, 96, 89 ]; 

 n = len(arr)

 

 print(findSubsequence(arr, n));

 

# This code is contributed by Ryuga  
  
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

// C# program to find maximum length subsequence

// such that adjacent elements have at least 

// one common digit 

using System;

 

class GFG 

{

 

// Returns length of maximum length subsequence 

static int findSubsequence(int []arr, int n) 

{ 

 

 // To store length of maximum length subsequence 

 int len = 1; 

 

 // To store current element arr[i] 

 int tmp; 

 

 int i, j, d; 

 

 // To store length of subsequence 

 // having common digit d 

 int []dp = new int[10]; 

 

 

 // To store digits present in current element 

 int []cnt = new int[10]; 

 

 // To store local maximum for current element 

 int locMax; 

 

 // For first element maximum length is 1 for 

 // each digit 

 tmp = arr[0]; 

 while (tmp > 0) 

 { 

 dp[tmp % 10] = 1; 

 tmp /= 10; 

 } 

 

 // Find digits of each element, then find length 

 // of subsequence for each digit and then find 

 // local maximum 

 for (i = 1; i < n; i++) 

 { 

 tmp = arr[i]; 

 locMax = 1; 

 for(int k = 0; k < 10; k++)

 {

 cnt[k] = 0;

 }

 // Find digits in current element 

 while (tmp > 0) 

 { 

 cnt[tmp % 10] = 1; 

 tmp /= 10; 

 } 

 

 // For each digit present find length of 

 // subsequence and find local maximum 

 for (d = 0; d <= 9; d++) 

 { 

 if (cnt[d] == 1) 

 { 

 dp[d]++; 

 locMax = Math.Max(locMax, dp[d]); 

 } 

 } 

 

 // Update value of dp[d] for each digit 

 // present in current element to local maximum 

 // found 

 for (d = 0; d <= 9; d++) 

 { 

 if (cnt[d] == 1) 

 { 

 dp[d] = locMax; 

 } 

 } 

 

 // Update maximum length with local maximum 

 len = Math.Max(len, locMax); 

 } 

 

 return len; 

} 

 

// Driver code 

public static void Main(String[] args) 

{

 int []arr = { 1, 12, 44, 29, 33, 96, 89 }; 

 int n = arr.Length; 

 Console.WriteLine(findSubsequence(arr, n)); 

}

}

 

// This code contributed by Rajput-Ji  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP program to find maximum length subsequence

// such that adjacent elements have at least

// one common digit

 

// Returns length of maximum length subsequence

function findSubsequence($arr, $n)

{

 

 // To store length of maximum length

 // subsequence

 $len = 1;

 

 // To store length of subsequence

 // having common digit d

 $dp = array_fill(0, 10, NULL);

 

 // For first element maximum length is 1 

 // for each digit

 $tmp = $arr[0];

 while ($tmp > 0)

 {

 $dp[$tmp % 10] = 1;

 $tmp = intval($tmp / 10);

 }

 

 // Find digits of each element, then 

 // find length of subsequence for each 

 // digit and then find local maximum

 for ($i = 1; $i < $n; $i++)

 {

 $tmp = $arr[$i];

 $locMax = 1;

 $cnt = array_fill(0, 10, NULL);

 

 // Find digits in current element

 while ($tmp > 0) 

 {

 $cnt[$tmp % 10] = 1;

 $tmp = intval($tmp / 10);

 }

 

 // For each digit present find length of

 // subsequence and find local maximum

 for ($d = 0; $d <= 9; $d++)

 {

 if ($cnt[$d]) 

 {

 $dp[$d]++;

 $locMax = max($locMax, $dp[$d]);

 }

 }

 

 // Update value of dp[d] for each digit

 // present in current element to local 

 // maximum found

 for ($d = 0; $d <= 9; $d++)

 {

 if ($cnt[$d]) 

 {

 $dp[$d] = $locMax;

 }

 }

 

 // Update maximum length with

 // local maximum

 $len = max($len, $locMax);

 }

 

 return $len;

}

 

// Driver code

$arr = array( 1, 12, 44, 29, 33, 96, 89 );

$n = sizeof($arr);

echo findSubsequence($arr, $n);

 

// This code is contributed by ita_c

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

**Time Complexity:** O(n)  
 **Auxiliary Space:** O(1)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

