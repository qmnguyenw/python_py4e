Count of subarrays which start and end with the same element



Given an array **A** of size **N** where the array elements contain values
from **1 to N** with duplicates, the task is to find total number of subarrays
which start and end with the same element.

 **Examples:**

>  **Input:** A[] = {1, 2, 1, 5, 2}  
>  **Output:** 7  
>  **Explanation:**  
>  Total 7 sub-array of the given array are {1}, {2}, {1}, {5}, {2}, {1, 2, 1}
> and {2, 1, 5, 2} are start and end with same element.
>
>  **Input:** A[] = {1, 5, 6, 1, 9, 5, 8, 10, 8, 9}  
>  **Output:** 14  
>  **Explanation:**  
>  Total 14 sub-array {1}, {5}, {6}, {1}, {9}, {5}, {8}, {10}, {8}, {9}, {1,
> 5, 6, 1}, {5, 6, 1, 9, 5}, {9, 5, 8, 10, 8, 9} and {8, 10, 8} start and end
> with same element.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** For each element in the array, if it is present at a
different index as well, we will increase our result by 1. Also, all 1-size
subarray are part of counted in the result. Therefore, add N to the result.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to Count total sub-array

// which start and end with same element

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find total sub-array

// which start and end with same element

void cntArray(int A[], int N)

{

 // initialize result with 0

 int result = 0;

 

 for (int i = 0; i < N; i++) {

 

 // all size 1 sub-array

 // is part of our result

 result++;

 

 // element at current index

 int current_value = A[i];

 

 for (int j = i + 1; j < N; j++) {

 

 // Check if A[j] = A[i]

 // increase result by 1

 if (A[j] == current_value) {

 result++;

 }

 }

 }

 

 // print the result

 cout << result << endl;

}

 

// Driver code

int main()

{

 int A[] = { 1, 5, 6, 1, 9,

 5, 8, 10, 8, 9 };

 int N = sizeof(A) / sizeof(int);

 

 cntArray(A, N);

 

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

// Java program to Count total sub-array

// which start and end with same element

 

public class Main {

 

 // function to find total sub-array

 // which start and end with same element

 public static void cntArray(int A[], int N)

 {

 // initialize result with 0

 int result = 0;

 

 for (int i = 0; i < N; i++) {

 

 // all size 1 sub-array

 // is part of our result

 result++;

 

 // element at current index

 int current_value = A[i];

 

 for (int j = i + 1; j < N; j++) {

 

 // Check if A[j] = A[i]

 // increase result by 1

 if (A[j] == current_value) {

 result++;

 }

 }

 }

 

 // print the result

 System.out.println(result);

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int[] A = { 1, 5, 6, 1, 9,

 5, 8, 10, 8, 9 };

 int N = A.length;

 cntArray(A, N);

 }

}  
  
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

# Python3 program to count total sub-array

# which start and end with same element 

 

# Function to find total sub-array 

# which start and end with same element 

def cntArray(A, N): 

 

 # Initialize result with 0 

 result = 0

 

 for i in range(0, N): 

 

 # All size 1 sub-array 

 # is part of our result 

 result = result + 1

 

 # Element at current index 

 current_value = A[i]

 

 for j in range(i + 1, N): 

 

 # Check if A[j] = A[i] 

 # increase result by 1 

 if (A[j] == current_value): 

 result = result + 1

 

 # Print the result 

 print(result)

 print("\n")

 

# Driver code 

A = [ 1, 5, 6, 1, 9, 5, 8, 10, 8,
9 ] 

N = len(A)

 

cntArray(A, N)

 

# This code is contributed by PratikBasu   
  
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

// C# program to Count total sub-array

// which start and end with same element

using System;

class GFG{

 

// function to find total sub-array

// which start and end with same element

public static void cntArray(int []A, int N)

{

 // initialize result with 0

 int result = 0;

 

 for (int i = 0; i < N; i++) 

 {

 

 // all size 1 sub-array

 // is part of our result

 result++;

 

 // element at current index

 int current_value = A[i];

 

 for (int j = i + 1; j < N; j++) 

 {

 

 // Check if A[j] = A[i]

 // increase result by 1

 if (A[j] == current_value) 

 {

 result++;

 }

 }

 }

 

 // print the result

 Console.Write(result);

}

 

// Driver code

public static void Main()

{

 int[] A = { 1, 5, 6, 1, 9,

 5, 8, 10, 8, 9 };

 int N = A.Length;

 cntArray(A, N);

}

}

 

// This code is contributed by Code_Mech  
  
---  
  
 __

 __

 **Output:**

    
    
    14
    

_**Time Complexity:** O(N2)_, where N is the size of array

 _ **Space complexity:** O(1)_

 **Efficient approach:** We can optimize the above method by observing that
the answer just depends on **frequencies of numbers** in the original array.  
 _For example_ in array {1, 5, 6, 1, 9, 5, 8, 10, 8, 9}, frequency of 1 is 2
and sub-array contributing to answer are {1}, {1} and {1, 5, 6, 1}
respectively, i.e., a total of 3.  
Therefore calculate the frequency of each element in the array. Then for each
element, the increment the count by the result yielded by the following
formula:

> ( (frequency of element)*(frequency of element + 1) ) / 2

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to Count total sub-array

// which start and end with same element

 

#include <bits/stdc++.h>

using namespace std;

 

// function to find total sub-array

// which start and end with same element

void cntArray(int A[], int N)

{

 // initialize result with 0

 int result = 0;

 

 // array to count frequency of 1 to N

 int frequency[N + 1] = { 0 };

 

 for (int i = 0; i < N; i++) {

 // update frequency of A[i]

 frequency[A[i]]++;

 }

 

 for (int i = 1; i <= N; i++) {

 int frequency_of_i = frequency[i];

 

 // update result with sub-array

 // contributed by number i

 result += +((frequency_of_i)

 * (frequency_of_i + 1))

 / 2;

 }

 

 // print the result

 cout << result << endl;

}

 

// Driver code

int main()

{

 int A[] = { 1, 5, 6, 1, 9, 5,

 8, 10, 8, 9 };

 int N = sizeof(A) / sizeof(int);

 

 cntArray(A, N);

 

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

// Java program to Count total sub-array

// which start and end with same element

 

public class Main {

 

 // function to find total sub-array which

 // start and end with same element

 public static void cntArray(int A[], int N)

 {

 // initialize result with 0

 int result = 0;

 

 // array to count frequency of 1 to N

 int[] frequency = new int[N + 1];

 

 for (int i = 0; i < N; i++) {

 // update frequency of A[i]

 frequency[A[i]]++;

 }

 

 for (int i = 1; i <= N; i++) {

 int frequency_of_i = frequency[i];

 

 // update result with sub-array

 // contributed by number i

 result += ((frequency_of_i)

 * (frequency_of_i + 1))

 / 2;

 }

 

 // print the result

 System.out.println(result);

 }

 

 // Driver code

 public static void main(String[] args)

 {

 

 int[] A = { 1, 5, 6, 1, 9, 5,

 8, 10, 8, 9 };

 int N = A.length;

 cntArray(A, N);

 }

}  
  
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

# Python3 program to count total sub-array

# which start and end with same element 

 

# Function to find total sub-array 

# which start and end with same element 

def cntArray(A, N): 

 

 # Initialize result with 0 

 result = 0

 

 # Array to count frequency of 1 to N 

 frequency = [0] * (N + 1) 

 

 for i in range(0, N):

 

 # Update frequency of A[i] 

 frequency[A[i]] = frequency[A[i]] + 1

 

 for i in range(1, N + 1): 

 frequency_of_i = frequency[i]

 

 # Update result with sub-array 

 # contributed by number i 

 result = result + ((frequency_of_i) *

 (frequency_of_i + 1)) / 2

 

 # Print the result 

 print(int(result))

 print("\n")

 

# Driver code 

A = [ 1, 5, 6, 1, 9, 5, 8, 10, 8,
9 ]

N = len(A)

 

cntArray(A, N) 

 

# This code is contributed by PratikBasu   
  
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

// C# program to Count total sub-array

// which start and end with same element

using System;

class GFG{

 

// function to find total sub-array which

// start and end with same element

public static void cntArray(int []A, int N)

{

 // initialize result with 0

 int result = 0;

 

 // array to count frequency of 1 to N

 int[] frequency = new int[N + 1];

 

 for (int i = 0; i < N; i++) 

 {

 // update frequency of A[i]

 frequency[A[i]]++;

 }

 

 for (int i = 1; i <= N; i++) 

 {

 int frequency_of_i = frequency[i];

 

 // update result with sub-array

 // contributed by number i

 result += ((frequency_of_i) * 

 (frequency_of_i + 1)) / 2;

 }

 

 // print the result

 Console.Write(result);

}

 

// Driver code

public static void Main()

{

 int[] A = { 1, 5, 6, 1, 9, 5,

 8, 10, 8, 9 };

 int N = A.Length;

 cntArray(A, N);

}

}

 

// This code is contributed by Nidhi_Biet  
  
---  
  
 __

 __

 **Output:**

    
    
    14
    

_**Time Complexity:** O(N)_, where N is the size of array

 _ **Space complexity:** O(N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

