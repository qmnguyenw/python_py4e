Find minimum value of the expression by choosing K elements from given array



Given an array of integers **arr** of size **N** , the task is to find the
minimum possible of the expression by choosing exactly **K(≤ N)** integers
form given array **arr**. Let say if choosen elements are stored in array
**B** **(B 1, B2, B3…..Bk)** then value of expression:  
![x = \\sum_{i=1}^k\\sum_{j=1}^k\(B_i - B_j\)^{2}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c30cd4aefa887bd9d8379997f4d7d4e6_l3.png)  
**Examples:**  

> **Input :** arr[] = {2, 0, 9, 5}, k = 2  
> **Output :** 8  
> Let say, choosen elements are {2, 0}, then x = 8, which is minimum possible  
>  **Input :** arr[] = {4, 21, 5, 3, 8}, k = 3  
> **Output :** 200  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach :**  
The above expression can be simplified as:  

  * ![\\sum_{i=1}^k\\sum_{j=1}^k\(B_i^2 + B_j^2 - 2*B_i*B_j\)  ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-fe02a42afb54e1dfb364533f00af90c0_l3.png)  

  * ![\\sum_{i=1}^k\\sum_{j=1}^k{B_i^2} + \\sum_{i=1}^k\\sum_{j=1}^k{B_j^2} - 2\\sum_{i=1}^k\\sum_{j=1}^k{B_i*B_j}  ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-68522641a5b252e32497fd8c62321ae5_l3.png)  

  * ![k*\\sum_{i=1}^k{B_i^2} + k*\\sum_{i=1}^k{B_j^2} - 2\\sum_{i=1}^k{B_i}*\\sum_{j=1}^k{B_j}  ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-1f7a846c0df293e554e0af3b11625101_l3.png)  

  * ![2*k*\\sum_{i=1}^k{B_i^2} - 2\\sum_{i=1}^k{B_i^2}  ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-591c3ac5f058eff3d10c2d8fe9169d3a_l3.png)  

  * ![\(2*k-2\)*\\sum_{i=1}^k{B_i^2}  ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-bcf0d781f920dcb3698d28a7aa8b7bfd_l3.png)  

So, all we need to do is select the **k** smallest elements from the array and
solve the expression.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to find the minimum possible of the expression

// by choosing exactly K(? N) integers form given array arr

#include <bits/stdc++.h>

using namespace std;

// Function to find the minimum possible of the expression

// by choosing exactly K(? N) integers form given array arr

int minimumValue(int arr[], int n, int k)

{

 // Sorting the array for least k element selection

 sort(arr, arr + n);

 int answer = 0;

 // Select first k elements from sorted array

 for (int i = 0; i < k; i++)

 answer += arr[i] * arr[i];

 // Return value of solved expression

 return answer * (2 * k - 2);

}

// Driver code

int main()

{

 int arr[] = { 4, 21, 5, 3, 8 }, k = 3;

 

 int n = sizeof(arr) / sizeof(arr[0]);

 

 // Function call

 cout << minimumValue(arr, n, k);

 

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

// JAVA program to find the minimum possible of the expression

// by choosing exactly K(? N) integers form given array arr 

import java.util.*;

class GFG{

// Function to find the minimum possible of the expression

// by choosing exactly K(? N) integers form given array arr

static int minimumValue(int arr[], int n, int k)

{

 // Sorting the array for least k element selection

 Arrays.sort(arr);

 int answer = 0;

 // Select first k elements from sorted array

 for (int i = 0; i < k; i++)

 answer += arr[i] * arr[i];

 // Return value of solved expression

 return answer * (2 * k - 2);

}

// Driver code

public static void main(String[] args)

{

 int arr[] = { 4, 21, 5, 3, 8 }, k = 3;

 

 int n = arr.length;

 

 // Function call

 System.out.print(minimumValue(arr, n, k)); 

}

}

// This code is contributed by Rajput-Ji  
  
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

# Python program to find the minimum

# possible of the expression by choosing

# exactly K(? N) integers form given array arr

# Function to find the minimum

# possible of the expression by

# choosing exactly K(? N) integers

# form given array arr

def minimumValue(arr, n, k):

 # Sorting the array for least k element selection

 arr.sort();

 answer = 0;

 # Select first k elements from sorted array

 for i in range(k):

 answer += arr[i] * arr[i];

 # Return value of solved expression

 return answer * (2 * k - 2);

# Driver code

if __name__ == '__main__':

 arr = [ 4, 21, 5, 3, 8 ];

 k = 3;

 n = len(arr);

 # Function call

 print(minimumValue(arr, n, k));

# This code is contributed by Rajput-Ji  
  
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

// C# program to find the minimum possible of the expression

// by choosing exactly K(? N) integers form given array arr 

using System;

class GFG{

 

// Function to find the minimum possible of the expression

// by choosing exactly K(? N) integers form given array arr

static int minimumValue(int []arr, int n, int k)

{

 

 // Sorting the array for least k element selection

 Array.Sort(arr);

 

 int answer = 0;

 

 // Select first k elements from sorted array

 for (int i = 0; i < k; i++)

 answer += arr[i] * arr[i];

 

 // Return value of solved expression

 return answer * (2 * k - 2);

}

 

// Driver code

public static void Main(String[] args)

{

 int []arr = { 4, 21, 5, 3, 8 };

 int k = 3;

 

 int n = arr.Length;

 

 // Function call

 Console.Write(minimumValue(arr, n, k)); 

}

}

// This code is contributed by 29AjayKumar  
  
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

// JavaScript program to find the minimum possible of the expression

// by choosing exactly K(? N) integers form given array arr

// Function to find the minimum possible of the expression

// by choosing exactly K(? N) integers form given array arr

function minimumValue(arr, n, k)

{

 // Sorting the array for least k element selection

 arr.sort((a, b) => a - b);

 let answer = 0;

 // Select first k elements from sorted array

 for (let i = 0; i < k; i++)

 answer += arr[i] * arr[i];

 // Return value of solved expression

 return answer * (2 * k - 2);

}

// Driver code

 let arr = [ 4, 21, 5, 3, 8 ], k = 3;

 

 let n = arr.length;

 

 // Function call

 document.write(minimumValue(arr, n, k));

 

// This code is contributed by Surbhi Tyagi.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    200

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

