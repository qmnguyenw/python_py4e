Check if minimum element in array is less than or equals half of every other
element



Given an **array arr[]** , the task is to check if the minimum element in the
array is less than or equal to half of every other element. If it is then
print “yes” otherwise print “no”.

 _ **Note:** The minimum number in the given array is always unique._

 **Examples:**

>  **Input:** arr = {2, 1, 4, 5}  
>  **Output:** Yes  
>  **Explanation:**  
>  1 is the minimum element in the array arr[] and on dividing 2, 4, 5 by 2 we
> get 1, 2, 2.5 which is greater than or equal to the minimum number. Hence,
> print “yes”.
>
>  **Input :** arr = {2, 4, 5, 3}  
>  **Output :** No  
>  **Explanation:**  
>  2 is the minimum element in the array arr[] and on dividing 4, 5, 3 by 2 we
> get 2, 2.5, 1.5 in which the integer 3 does not return a value which is
> greater than or equal to the minimum number ( 1.5 < 2). Hence, print "no".
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1:**

To solve the problem mentioned above we have to **find the smallest element**
with the help of loops and then **scan through the entire array** again and
check if twice the smallest element is smaller than or equal to every other
element. But this solution takes O(N) time using two loops and can be
optimized further where only one iteration is involved.

 **Method 2:**

To optimize the above solution we can **find the smallest as well as the
second smallest element in a single iteration** itself. Then simply check if
twice of the smallest element is smaller than or equal to the second smallest
element.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to Check if the minimum element in the

// array is greater than or equal to half of every other elements

#include <bits/stdc++.h>

using namespace std;

 

// Function to Check if the minimum element in the array is

// greater than or equal to half of every other element

void checkMin(int arr[], int len)

{

 

 // Initialise the variables to store

 // smallest and second smallest

 int smallest = INT_MAX, secondSmallest = INT_MAX;

 

 for (int i = 0; i < len; i++) {

 

 // Check if current element is smaller than smallest,

 // the current smallest will become secondSmallest

 // and current element will be the new smallest

 if (arr[i] < smallest) {

 secondSmallest = smallest;

 smallest = arr[i];

 }

 

 // Check if current element is smaller than

 // secondSmallest simply update the latter

 else if (arr[i] < secondSmallest) {

 secondSmallest = arr[i];

 }

 }

 

 if (2 * smallest <= secondSmallest)

 cout << "Yes";

 else

 cout << "No";

}

 

// Driver code

int main()

{

 int arr[] = { 2, 3, 4, 5 };

 

 int len = sizeof(arr) / sizeof(arr[0]);

 

 checkMin(arr, len);

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

// Java implementation to check

// if the minimum element in the

// array is greater than or equal

// to half of every other elements

import java.util.*;

class GFG{

 

// Function to Check if the minimum

// element in the array is greater

// than or equal to half of every

// other elements

static void checkMin(int arr[], int len)

{

 

 // Initialise the variables to store

 // smallest and second smallest

 int smallest = Integer.MAX_VALUE; 

 int secondSmallest = Integer.MAX_VALUE;

 

 for(int i = 0; i < len; i++)

 {

 

 // Check if current element is smaller than 

 // smallest, the current smallest will 

 // become secondSmallest and current 

 // element will be the new smallest

 if (arr[i] < smallest)

 {

 secondSmallest = smallest;

 smallest = arr[i];

 }

 

 // Check if current element is smaller than

 // secondSmallest simply update the latter

 else if (arr[i] < secondSmallest)

 {

 secondSmallest = arr[i];

 }

 }

 if (2 * smallest <= secondSmallest)

 System.out.print("Yes");

 else

 System.out.print("No");

}

 

// Driver code

public static void main(String[] args)

{

 int arr[] = { 2, 3, 4, 5 };

 int len = arr.length;

 

 checkMin(arr, len);

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

# Python3 implementation to Check if

# the minimum element in the array

# is greater than or equal to half 

# of every other element

import math

 

# Function to Check if the minimum element 

# in the array is greater than or equal to 

# half of every other element

def checkMin(arr, n):

 

 # Initialise the variables to store

 # smallest and second smallest

 smallest = math.inf

 secondSmallest = math.inf

 

 for i in range(n):

 

 # Check if current element is 

 # smaller than smallest, 

 # the current smallest will become 

 # secondSmallest and current element 

 # will be the new smallest

 if(arr[i] < smallest):

 secondSmallest = smallest

 smallest = arr[i]

 

 # Check if current element is smaller than

 # secondSmallest simply update the latter

 elif(arr[i] < secondSmallest):

 secondSmallest = arr[i]

 

 if(2 * smallest <= secondSmallest):

 print("Yes")

 else:

 print("No")

 

# Driver code 

if __name__ == '__main__':

 arr = [ 2, 3, 4, 5 ]

 

 n = len(arr)

 

 checkMin(arr, n)

 

# This code is contributed by Shivam Singh.  
  
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

// C# implementation to check

// if the minimum element in the

// array is greater than or equal

// to half of every other elements

using System;

 

class GFG{

 

// Function to Check if the minimum

// element in the array is greater

// than or equal to half of every

// other elements

static void checkMin(int []arr, int len)

{

 

 // Initialise the variables to store

 // smallest and second smallest

 int smallest = int.MaxValue; 

 int secondSmallest = int.MaxValue;

 

 for(int i = 0; i < len; i++)

 {

 

 // Check if current element is smaller than 

 // smallest, the current smallest will 

 // become secondSmallest and current 

 // element will be the new smallest

 if (arr[i] < smallest)

 {

 secondSmallest = smallest;

 smallest = arr[i];

 }

 

 // Check if current element is smaller than

 // secondSmallest simply update the latter

 else if (arr[i] < secondSmallest)

 {

 secondSmallest = arr[i];

 }

 }

 if (2 * smallest <= secondSmallest)

 Console.Write("Yes");

 else

 Console.Write("No");

}

 

// Driver code

public static void Main(String[] args)

{

 int []arr = { 2, 3, 4, 5 };

 int len = arr.Length;

 

 checkMin(arr, len);

}

}

 

// This code is contributed by amal kumar choubey  
  
---  
  
 __

 __

 **Output:**

    
    
    No
    

**Time Complexity:** O(n)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

