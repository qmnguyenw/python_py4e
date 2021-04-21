Find the minimum value of the given expression over all pairs of the array



Given an array A of size N, find the minimum value of the expression : ![\(A_i
\\& A_j\) \\oplus \(A_i | A_j\)    ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-6415178fa80101ef25d8a21c6921acfb_l3.png)over
all pairs (i, j) (where i != j). Here ![\\&
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f12158ca106efaeb50a24b943acdbcf4_l3.png), ![|
](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
afcd9a2a0852572aa4f333a2ef930e91_l3.png)and ![\\oplus
](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
cb09ec232b718ee96fa34fd8005a873c_l3.png)represent bitwise AND, bitwise OR and
bitwise XOR resprectively.  
**Examples:**  

    
    
    **Input:** A = [1, 2, 3, 4, 5]
    **Output:** 1
    **Explanation:**
    (A[1] and A[2]) xor (A[1] or A[2]) = 1,
    which is minimum possible value.
    
    **Input :** A = [12, 3, 14, 5, 9, 8]
    **Output :** 1

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**  
Iterate through all the pairs of the array with different index and find the
minimum possible value of given expression over them.  
Below the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the minimum

// value of the given expression

// over all pairs of the array

#include <bits/stdc++.h>

using namespace std;

// Function to find the minimum

// value of the expression

int MinimumValue(int a[], int n)

{

 int answer = INT_MAX;

 

 // Iterate over all the pairs

 // and find the minimum value

 for (int i = 0; i < n; i++)

 {

 for (int j = i + 1; j < n; j++)

 {

 answer = min(answer,

 ((a[i] & a[j])

 ^ (a[i] | a[j])));

 }

 }

 return answer;

}

// Driver code

int main()

{

 int N = 6;

 int A[N] = { 12, 3, 14, 5, 9, 8 };

 cout << MinimumValue(A, N);

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

// Java program to find the minimum

// value of the given expression

// over all pairs of the array

import java.io.*;

import java.util.Arrays;

class GFG

{

// Function to find the minimum

// value of the expression

static int MinimumValue(int a[], int n)

{

 int answer = Integer.MAX_VALUE;

 

 // Iterate over all the pairs

 // and find the minimum value

 for (int i = 0; i < n; i++)

 {

 for (int j = i + 1; j < n; j++)

 {

 answer = Math.min(answer, ((a[i] & a[j])

 ^ (a[i] | a[j])));

 }

 }

 return answer;

}

// Driver code

public static void main(String[] args)

{

 int N = 6;

 int[] A = new int[]{ 12, 3, 14, 5, 9, 8
};

 System.out.print(MinimumValue(A, N));

}

}

// This code is contributed by shivanisinghss2110  
  
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

# Python3 program to find the minimum

# value of the given expression

# over all pairs of the array

import sys

# Function to find the minimum

# value of the expression

def MinimumValue(a,n):

 answer = sys.maxsize

 

 # Iterate over all the pairs

 # and find the minimum value

 for i in range(n):

 for j in range(i + 1, n, 1):

 answer = min(answer,((a[i] & a[j])^(a[i] | a[j])))

 return answer

# Driver code

if __name__ == '__main__':

 N = 6

 A = [12, 3, 14, 5, 9, 8]

 print(MinimumValue(A, N))

# This code is contributed by Bhupendra_Singh  
  
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

// C# program to find the minimum

// value of the given expression

// over all pairs of the array

using System;

class GFG{

// Function to find the minimum

// value of the expression

static int MinimumValue(int []a, int n)

{

 int answer = Int32.MaxValue;

 

 // Iterate over all the pairs

 // and find the minimum value

 for(int i = 0; i < n; i++)

 {

 for(int j = i + 1; j < n; j++)

 {

 answer = Math.Min(answer,

 ((a[i] & a[j]) ^

 (a[i] | a[j])));

 }

 }

 return answer;

}

// Driver Code

public static void Main()

{

 int N = 6;

 int[] A = new int[]{ 12, 3, 14, 5, 9, 8 };

 Console.Write(MinimumValue(A, N));

}

}

// This code is contributed by shivanisinghss2110  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// JavaScript program to find the minimum

// value of the given expression

// over all pairs of the array

// Function to find the minimum

// value of the expression

function MinimumValue(a, n)

{

 let answer = Number.MAX_SAFE_INTEGER;

 

 // Iterate over all the pairs

 // and find the minimum value

 for (let i = 0; i < n; i++)

 {

 for (let j = i + 1; j < n; j++)

 {

 answer = Math.min(answer,

 ((a[i] & a[j])

 ^ (a[i] | a[j])));

 }

 }

 return answer;

}

// Driver code

 let N = 6;

 let A = [ 12, 3, 14, 5, 9, 8 ];

 document.write(MinimumValue(A, N));

// This code is contributed by Surbhi Tyagi.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    1

**Time Complexity :** O(N2)  
 **Efficient Approach**  

  

  

  * Let’s simplify the given expression :  

> \+ represents bitwise OR  
> . represents bitwise AND  
> ^ represents bitwise XOR  
> ‘ represents 1’s complement  
> (x . y) ^ (x + y) = (x . y) . (x + y)’ + (x . y)’ . (x + y) (using
> definition of XOR)  
> = (x . y) . (x’ . y’) + (x’+ y’) . (x + y) (De morgan’s law)  
> = x.x’.y.y’ + x’.x + x’.y + y’.x + y.y  
> = 0 + 0 + x’.y + y’.x + 0  
> = x ^ y  
>

  *   * Since the expression simplifies to minimum xor value pair, we can simply use the algorithm mentioned in this article to find the same efficiently.   

Below the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the minimum

// value of the given expression

// over all pairs of the array

#include <bits/stdc++.h>

using namespace std;

// Function to find the minimum

// value of the expression

int MinimumValue(int arr[], int n)

{

 // The expression simplifies to

 // finding the minimum xor

 // value pair

 // Sort given array

 sort(arr, arr + n);

 int minXor = INT_MAX;

 int val = 0;

 // Calculate min xor of

 // consecutive pairs

 for (int i = 0; i < n - 1; i++)

 {

 val = arr[i] ^ arr[i + 1];

 minXor = min(minXor, val);

 }

 return minXor;

}

// Driver code

int main()

{

 int N = 6;

 int A[N] = { 12, 3, 14, 5, 9, 8 };

 cout << MinimumValue(A, N);

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

// Java program to find the minimum

// value of the given expression

// over all pairs of the array

import java.io.*;

import java.util.Arrays;

class GFG {

// Function to find the minimum

// value of the expression

static int MinimumValue(int arr[], int n)

{

 

 // The expression simplifies to

 // finding the minimum xor

 // value pair

 // Sort given array

 Arrays.sort(arr);

 int minXor = Integer.MAX_VALUE;

 int val = 0;

 // Calculate min xor of

 // consecutive pairs

 for(int i = 0; i < n - 1; i++)

 {

 val = arr[i] ^ arr[i + 1];

 minXor = Math.min(minXor, val);

 }

 return minXor;

}

// Driver code

public static void main(String[] args)

{

 int N = 6;

 int[] A = new int[]{ 12, 3, 14, 5, 9, 8
};

 System.out.print(MinimumValue(A, N));

}

}

// This code is contributed by shivanisinghss2110  
  
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

# Python3 program to find the minimum

# value of the given expression

# over all pairs of the array

import sys

# Function to find the minimum

# value of the expression

def MinimumValue(arr, n):

 # The expression simplifies

 # to finding the minimum

 # xor value pair

 # Sort given array

 arr.sort();

 minXor = sys.maxsize;

 val = 0;

 # Calculate min xor of

 # consecutive pairs

 for i in range(0, n - 1):

 val = arr[i] ^ arr[i + 1];

 minXor = min(minXor, val);

 

 return minXor;

# Driver code

if __name__ == '__main__':

 

 N = 6;

 A = [ 12, 3, 14, 5, 9, 8 ];

 print(MinimumValue(A, N));

 

# This code is contributed by sapnasingh4991  
  
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

// C# program to find the minimum

// value of the given expression

// over all pairs of the array

using System;

class GFG{

// Function to find the minimum

// value of the expression

static int MinimumValue(int []arr, int n)

{

 

 // The expression simplifies to

 // finding the minimum xor

 // value pair

 // Sort given array

 Array.Sort(arr);

 int minXor = Int32.MaxValue;

 int val = 0;

 // Calculate min xor of

 // consecutive pairs

 for(int i = 0; i < n - 1; i++)

 {

 val = arr[i] ^ arr[i + 1];

 minXor = Math.Min(minXor, val);

 }

 

 return minXor;

}

// Driver Code

public static void Main()

{

 int N = 6;

 int[] A = new int[]{ 12, 3, 14, 5, 9, 8 };

 Console.Write(MinimumValue(A, N));

}

}

// This code is contributed by shivanisinghss2110  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

 // Javascript program to find the minimum

 // value of the given expression

 // over all pairs of the array

 

 // Function to find the minimum

 // value of the expression

 function MinimumValue(arr, n)

 {

 // The expression simplifies to

 // finding the minimum xor

 // value pair

 // Sort given array

 arr.sort();

 let minXor = Number.MAX_VALUE;

 let val = 0;

 // Calculate min xor of

 // consecutive pairs

 for (let i = 0; i < n - 1; i++)

 {

 val = arr[i] ^ arr[i + 1];

 minXor = Math.min(minXor, val);

 }

 return minXor;

 }

 

 let N = 6;

 let A = [ 12, 3, 14, 5, 9, 8 ];

 

 document.write(MinimumValue(A, N));

 

 //This code is contributed by divyeshrabadiya07

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    1

**Time Complexity :** O(N * log(N))  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

