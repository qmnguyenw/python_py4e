Minimum number of steps to make all elements of array equal



Given two arrays **A[]** and **B[]** of the same length, the task is to find
the minimum number of steps required to make all the elements of the array
equal by replacing the element with the difference of the corresponding
element from array B.  
**Note:** If this is not possible print -1.  
 **Examples:**

> **Input:** A[] = {5, 7, 10, 5, 15} B[] = {2, 2, 1, 3, 5}  
> **Output:** 8  
> **Explanation:**  
> Steps to convert Array elements equal –  
> **Index 0:** 5 is not changed, Steps Taken = 0  
> **Index 1:** 7 – (2 * 1) = 5, Steps Taken = 1  
> **Index 2:** 10 – (1 * 5) = 5, Steps Taken = 5  
> **Index 3:** 5 is not changed, Steps Taken = 0  
> **Index 4:** 15 – (5 * 2) = 5, Steps Taken = 2  
> Therefore, total steps required = 0 + 1 + 5 + 0 + 2 = 8
>
>  **Input:** A[] = {5, 6}, B[] = {4, 3}  
> **Output:** -1  
> **Explanation:**  
> It’s not possible to make all elements of array equal.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to find the value at which the array elements can
be converged, this value will definitely lie in between 0 to the minimum value
of the array. Below is the illustration of the approach:

  * Initially, mark the flag as False, to check that the array is convertible or not.
  * Run a while loop until the minimum of the array is greater than -1. 
    * Iterate over the indices of the array, that is from 0 to length – 1
    * For each index, check that if the element at that index in array A is greater than the minimum of the array, If yes then update the array element A[i] as A[i] – B[i].
    * Increment the number of steps by 1.
    * Check that all the array elements are equal if yes then mark the flag as True and break the while loop
    * Otherwise, repeat the steps above to compute the total number of steps required.
  * Finally, check if the flag is True, If yes then the array is convertible.

 **Explanation with Example:**  
Given arrays be – A[] = {5, 7, 10, 5, 15}, B[] = {2, 2, 1, 3, 5}

  

  
Array A| Current Index| Minimum of Array A| Steps| Comments| {5, 7, 10, 5,
15}| 0| 5| 0| No operation !| {5, 5, 10, 5, 15}| 1| 5| 1| Array element is
subtracted once. 7 – 2 = 5| {5, 5, 9, 5, 15}| 2| 5| 2| Array element is
subtracted once. 10 – 1 = 9| {5, 5, 8, 5, 15}| 2| 5| 3| Array element is
subtracted once. 9 – 1 = 8| {5, 5, 7, 5, 15}| 2| 5| 4| Array element is
subtracted once. 8 – 1 = 7| {5, 5, 6, 5, 15}| 2| 5| 5| Array element is
subtracted once. 7 – 1 = 6| {5, 5, 5, 5, 15}| 2| 5| 6| Array element is
subtracted once. 6 – 1 = 5| {5, 5, 5, 5, 10}| 4| 5| 7| Array element is
subtracted once. 15 – 5 = 10| {5, 5, 5, 5, 5}| 4| 5| 8| Array element is
subtracted once. 10 – 5 = 5  
---|---|---|---|---  
  
Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// minimum number of steps to convert

// array by subtracting the corresponding

// element from array B

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the minimum steps

void minimumSteps(int ar1[], int ar2[], int n)

{

 

 // Counter to store the steps

 int ans = 0;

 

 // Flag to check that

 // array is converted

 bool flag = true;

 

 // Loop until the minimum of the

 // array is greater than -1

 while (*min_element(ar1, ar1 + n) > -1)

 {

 int a = *min_element(ar1, ar1 + n);

 

 // Loop to convert the array

 // elements by substraction

 for(int i = 0; i < n; i++)

 {

 if (ar1[i] != a)

 {

 ar1[i] -= ar2[i];

 ans += 1;

 }

 }

 

 set<int> s1(ar1, ar1 + n);

 

 // If the array is converted

 if (s1.size() == 1)

 {

 flag = false;

 cout << ans << endl;

 break;

 }

 }

 

 if (flag)

 {

 cout << -1 << endl;

 }

}

 

// Driver Code

int main()

{

 int n = 5;

 int ar1[] = { 5, 7, 10, 5, 15 };

 int ar2[] = { 1, 2, 1, 5, 5 };

 

 // Function call

 minimumSteps(ar1, ar2, n);

 

 return 0;

}

// This code is contributed by rutvik_56  
  
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

// Java implementation to find the

// minimum number of steps to convert

// array by subtracting the corresponding

// element from array B

import java.util.*;

class GFG{

 

// Function to find the

// minimum steps

static void minimumSteps(int ar1[],

 int ar2[],

 int n)

{

 // Counter to store the steps

 int ans = 0;

 // Flag to check that

 // array is converted

 boolean flag = true;

 // Loop until the minimum of the

 // array is greater than -1

 while (Arrays.stream(ar1).min().getAsInt() > -1)

 {

 int a = Arrays.stream(ar1).min().getAsInt();

 // Loop to convert the array

 // elements by substraction

 for(int i = 0; i < n; i++)

 {

 if (ar1[i] != a)

 {

 ar1[i] -= ar2[i];

 ans += 1;

 }

 }

 HashSet<Integer> s1 = new HashSet<>();

 for(int i = 0; i < n; i++)

 {

 s1.add(ar1[i]);

 }

 // If the array is converted

 if (s1.size() == 1)

 {

 flag = false;

 System.out.print(ans + "\n");

 break;

 }

 }

 if (flag)

 {

 System.out.print(-1 + "\n");

 }

}

 

// Driver Code

public static void main(String[] args)

{

 int n = 5;

 int ar1[] = {5, 7, 10, 5, 15};

 int ar2[] = {1, 2, 1, 5, 5};

 // Function call

 minimumSteps(ar1, ar2, n);

}

}

// This code is contributed by Princi Singh  
  
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

# Python3 implementation to find the

# minimum number of steps to convert

# array by subtracting the corresponding

# element from array B

# Function to find the minimum steps

def minimumSteps(ar1, ar2, n):

 

 # Counter to store the steps

 ans = 0

 

 # Flag to check that

 # array is converted

 flag = True

 

 # Loop until the minimum of the

 # array is greater than -1

 while min(ar1)>-1:

 a = min(ar1)

 

 # Loop to convert the array

 # elements by substraction

 for i in range(n):

 if ar1[i]!= a:

 ar1[i]-= ar2[i]

 ans+= 1

 

 # If the array is converted

 if len(set(ar1))== 1:

 flag = False

 print(ans)

 break

 if flag:

 print(-1)

# Driver Code

if __name__ == "__main__":

 n = 5

 ar1 = [5, 7, 10, 5, 15]

 ar2 = [1, 2, 1, 5, 5]

 

 # Function Call

 minimumSteps(ar1, ar2, n)  
  
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

// C# implementation to

// find the minimum number

// of steps to convert array

// by subtracting the

// corresponding element from

// array B

using System;

using System.Linq;

using System.Collections.Generic;

class GFG{

 

// Function to find the

// minimum steps

static void minimumSteps(int []ar1,

 int []ar2,

 int n)

{

 // Counter to store the steps

 int ans = 0;

 // Flag to check that

 // array is converted

 bool flag = true;

 // Loop until the minimum of the

 // array is greater than -1

 while (ar1.Min() > -1)

 {

 int a = ar1.Min();

 // Loop to convert the array

 // elements by substraction

 for(int i = 0; i < n; i++)

 {

 if (ar1[i] != a)

 {

 ar1[i] -= ar2[i];

 ans += 1;

 }

 }

 HashSet<int> s1 = new HashSet<int>();

 

 for(int i = 0; i < n; i++)

 {

 s1.Add(ar1[i]);

 }

 // If the array is converted

 if (s1.Count == 1)

 {

 flag = false;

 Console.Write(ans + "\n");

 break;

 }

 }

 if (flag)

 {

 Console.Write(-1 + "\n");

 }

}

 

// Driver Code

public static void Main(String[] args)

{

 int n = 5;

 int []ar1 = {5, 7, 10, 5, 15};

 int []ar2 = {1, 2, 1, 5, 5};

 // Function call

 minimumSteps(ar1, ar2, n);

}

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    8
    
    
    
    
    
    

**Performance Analysis:**

  * **Time Complexity:** As in the above approach, there are two loops to convert the array which takes O(N2) in the worst case, Hence the Time Complexity will be **O(N 2)**.
  *  **Space Complexity:** As in the above approach, there is no extra space used, Hence the space complexity will be **O(1)**.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

