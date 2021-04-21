Longest Mountain Subarray



Given an array **arr[]** with **N** elements, the task is to find out the
longest sub-array which has the shape of a mountain.

> A **mountain sub-array** consists of elements that are initially in
> ascending order until a peak element is reached and beyond the peak element
> all other elements of the sub-array are in decreasing order.

 **Examples:**

> **Input:** arr = [2, 2, 2]  
> **Output:** 0  
> **Explanation:**  
> No sub-array exists that shows the behavior of a mountain sub-array.
>
>  **Input:** arr = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]  
> **Output:** 11  
> **Explanation:**  
>  There are two sub-arrays that can be considered as mountain sub-arrays. The
> first one is from index 0 – 2 (3 elements) and next one is from index 2 – 12
> (11 elements). As 11 > 2, our answer is 11.
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**  
Go through every possible sub-array and check whether it is a mountain sub-
array or not. This might take a long time to find the solution and the time
complexity for the above approach can be estimated as **O(N*N)** to go through
every possible sub-array and **O(N)** to check whether it is a mountain sub-
array or not. Thus, the overall time complexity for the program is **O(N 3)
**which is very high.

 **Efficient Approach:**

  1. If the length of the given array is less than 3, print 0 as it is not possible to have a mountain sub-array in such a case.
  2. Set the maximum length to 0 initially.
  3. Use the two-pointer technique (‘begin’ pointer and ‘end’ pointer) to find out the longest mountain sub-array in the given array.
  4. When an increasing sub-array is encountered, mark the beginning index of that increasing sub-array in the ‘begin’ pointer.
  5. If an index value is found in the ‘end’ pointer then reset the values in both the pointers as it marks the beginning of a new mountain sub-array.
  6. When a decreasing sub-array us encountered, mark the ending index of the mountain sub-array in the ‘end’ pointer.
  7. Calculate the length of the current mountain sub-array, compare it with the current maximum length of all-mountain sub-arrays traversed until now and keep updating the current maximum length.

Below is the implementation of the above described efficient approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ codde for Longest Mountain Subarray

#include <bits/stdc++.h>

using namespace std;

// Function to find the

// longest mountain subarray

int LongestMountain(vector<int>& a)

{

 int i = 0, j = -1,

 k = -1, p = 0,

 d = 0, n = 0;

 // If the size of array is less

 // than 3, the array won't show

 // mountain like behaviour

 if (a.size() < 3) {

 return 0;

 }

 for (i = 0; i < a.size() - 1; i++) {

 if (a[i + 1] > a[i]) {

 // When a new mountain sub-array

 // is found, there is a need to

 // set the variables k, j to -1

 // in order to help calculate the

 // length of new mountain sub-array

 if (k != -1) {

 k = -1;

 j = -1;

 }

 // j marks the starting index of a

 // new mountain sub-array. So set the

 // value of j to current index i.

 if (j == -1) {

 j = i;

 }

 }

 else {

 // Checks if next element is

 // less than current element

 if (a[i + 1] < a[i]) {

 // Checks if starting element exists

 // or not, if the starting element

 // of the mountain sub-array exists

 // then the index of ending element

 // is stored in k

 if (j != -1) {

 k = i + 1;

 }

 // This condition checks if both

 // starting index and ending index

 // exists or not, if yes, the

 // length is calculated.

 if (k != -1 && j != -1) {

 // d holds the lenght of the

 // longest mountain sub-array.

 // If the current length is

 // greater than the

 // calculated length, then

 // value of d is updated.

 if (d < k - j + 1) {

 d = k - j + 1;

 }

 }

 }

 // ignore if there is no

 // increase or decrease in

 // the value of the next element

 else {

 k = -1;

 j = -1;

 }

 }

 }

 // Checks and calculates

 // the length if last element

 // of the array is the last

 // element of a mountain sub-array

 if (k != -1 && j != -1) {

 if (d < k - j + 1) {

 d = k - j + 1;

 }

 }

 return d;

}

// Driver code

int main()

{

 vector<int> d = { 1, 3, 1, 4,

 5, 6, 7, 8,

 9, 8, 7, 6, 5 };

 cout << LongestMountain(d)

 << endl;

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

// Java code for Longest Mountain Subarray

import java.io.*;

class GFG{

 

// Function to find the

// longest mountain subarray

public static int LongestMountain(int a[])

{

 int i = 0, j = -1, k = -1,

 p = 0, d = 0, n = 0;

 // If the size of array is less than 3,

 // the array won't show mountain like

 // behaviour

 if (a.length < 3)

 return 0;

 for(i = 0; i < a.length - 1; i++)

 {

 if (a[i + 1] > a[i])

 {

 

 // When a new mountain sub-array is

 // found, there is a need to set the

 // variables k, j to -1 in order to

 // help calculate the length of new

 // mountain sub-array

 if (k != -1)

 {

 k = -1;

 j = -1;

 }

 // j marks the starting index of a

 // new mountain sub-array. So set the

 // value of j to current index i.

 if (j == -1)

 j = i;

 }

 else

 {

 

 // Checks if next element is

 // less than current element

 if (a[i + 1] < a[i])

 {

 

 // Checks if starting element exists

 // or not, if the starting element of

 // the mountain sub-array exists then

 // the index of ending element is

 // stored in k

 if (j != -1)

 k = i + 1;

 // This condition checks if both

 // starting index and ending index

 // exists or not, if yes,the length

 // is calculated.

 if (k != -1 && j != -1)

 {

 // d holds the lenght of the

 // longest mountain sub-array.

 // If the current length is

 // greater than the calculated

 // length, then value of d is

 // updated.

 if (d < k - j + 1)

 d = k - j + 1;

 }

 }

 

 // Ignore if there is no increase

 // or decrease in the value of the

 // next element

 else

 {

 k = -1;

 j = -1;

 }

 }

 }

 // Checks and calculates the length

 // if last element of the array is

 // the last element of a mountain sub-array

 if (k != -1 && j != -1)

 {

 if (d < k - j + 1)

 d = k - j + 1;

 }

 return d;

}

// Driver code

public static void main (String[] args)

{

 int a[] = { 1, 3, 1, 4, 5, 6, 7,

 8, 9, 8, 7, 6, 5 };

 

 System.out.println(LongestMountain(a));

}

}

// This code is contributed by piyush3010  
  
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

# Python3 code for longest mountain subarray

# Function to find the

# longest mountain subarray

def LongestMountain(a):

 

 i = 0

 j = -1

 k = -1

 p = 0

 d = 0

 n = 0

 

 # If the size of the array is less

 # than 3, the array won't show

 # mountain like behaviour

 if (len(a) < 3):

 return 0

 

 for i in range(len(a) - 1):

 if (a[i + 1] > a[i]):

 

 # When a new mountain sub-array

 # is found, there is a need to

 # set the variables k, j to -1

 # in order to help calculate the

 # length of new mountain sub-array

 if (k != -1):

 k = -1

 j = -1

 

 # j marks the starting index of a

 # new mountain sub-array. So set the

 # value of j to current index i.

 if (j == -1):

 j = i

 else:

 

 # Checks if next element is

 # less than current element

 if (a[i + 1] < a[i]):

 

 # Checks if starting element exists

 # or not, if the starting element

 # of the mountain sub-array exists

 # then the index of ending element

 # is stored in k

 if (j != -1):

 k = i + 1

 

 # This condition checks if both

 # starting index and ending index

 # exists or not, if yes, the

 # length is calculated.

 if (k != -1 and j != -1):

 

 # d holds the lenght of the

 # longest mountain sub-array.

 # If the current length is

 # greater than the

 # calculated length, then

 # value of d is updated.

 if (d < k - j + 1):

 d = k - j + 1

 

 # Ignore if there is no

 # increase or decrease in

 # the value of the next element

 else:

 k = -1

 j = -1

 

 # Checks and calculates

 # the length if last element

 # of the array is the last

 # element of a mountain sub-array

 if (k != -1 and j != -1):

 if (d < k - j + 1):

 d = k - j + 1

 

 return d

# Driver code

d = [ 1, 3, 1, 4, 5, 6,

 7, 8, 9, 8, 7, 6, 5 ]

print(LongestMountain(d))

 

# This code is contributed by shubhamsingh10  
  
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

// C# code for the

// longest Mountain Subarray

using System;

class GFG{

 

// Function to find the

// longest mountain subarray

public static int longestMountain(int []a)

{

 int i = 0, j = -1, k = -1,

 p = 0, d = 0;

 // If the size of array is less than 3,

 // the array won't show mountain like

 // behaviour

 if (a.Length < 3)

 return 0;

 for(i = 0; i < a.Length - 1; i++)

 {

 if (a[i + 1] > a[i])

 {

 // When a new mountain sub-array is

 // found, there is a need to set the

 // variables k, j to -1 in order to

 // help calculate the length of new

 // mountain sub-array

 if (k != -1)

 {

 k = -1;

 j = -1;

 }

 // j marks the starting index of a

 // new mountain sub-array. So set the

 // value of j to current index i.

 if (j == -1)

 j = i;

 }

 else

 {

 // Checks if next element is

 // less than current element

 if (a[i + 1] < a[i])

 {

 // Checks if starting element exists

 // or not, if the starting element of

 // the mountain sub-array exists then

 // the index of ending element is

 // stored in k

 if (j != -1)

 k = i + 1;

 // This condition checks if both

 // starting index and ending index

 // exists or not, if yes,the length

 // is calculated.

 if (k != -1 && j != -1)

 {

 // d holds the lenght of the

 // longest mountain sub-array.

 // If the current length is

 // greater than the calculated

 // length, then value of d is

 // updated.

 if (d < k - j + 1)

 d = k - j + 1;

 }

 }

 // Ignore if there is no increase

 // or decrease in the value of the

 // next element

 else

 {

 k = -1;

 j = -1;

 }

 }

 }

 // Checks and calculates the length

 // if last element of the array is

 // the last element of a mountain sub-array

 if (k != -1 && j != -1)

 {

 if (d < k - j + 1)

 d = k - j + 1;

 }

 return d;

}

// Driver code

public static void Main(String[] args)

{

 int []a = {1, 3, 1, 4, 5, 6, 7,

 8, 9, 8, 7, 6, 5};

 Console.WriteLine(longestMountain(a));

}

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    11
    
    
    
    

_**Time Complexity:** O(N) _  
_**Auxiliary Space Complexity:** O(1) _

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

