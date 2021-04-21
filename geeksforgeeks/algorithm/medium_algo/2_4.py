Find any one of the multiple repeating elements in read only array | Set 2



Given a read-only array **arr[]** of size **N + 1** , find one of the multiple
repeating elements in the array where the array contains integers only between
**1** and **N**.  
 **Note:** Read-only array means that the contents of the array can’t be
modified.

 **Examples:**

>  **Input:** N = 5, arr[] = {1, 1, 2, 3, 5, 4}  
>  **Output:** 1  
>  **Explanation:**  
>  1 is the only number repeated in the array.
>
>  **Input:** N = 10, arr[] = {10, 1, 2, 3, 5, 4, 9, 8, 5, 6, 4}  
>  **Output:** 5  
>  **Explanation:**  
>  5 is the one of the number repeated in the array.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

In the previous post, we have discussed the same article with a space
complexity _O(N) and O(sqrt(N))_.

  

  

 **Approach:** This approach is based on Floyd’s Tortoise and Hare Algorithm (
**Cycle Detection Algorithm** ).

  1. Use the function **f(x) = arr[x]** to construct the sequence:  

> arr[0], arr[arr[0]], arr[arr[arr[0]]], arr[arr[arr[arr[0]]]] …….

  2. Each new element in the sequence is an element in **arr[]** at the index of the previous element.
  3. Starting from **x = arr[0]** , it will produce a linked list with a cycle.
  4. The cycle appears because **arr[]** contains duplicate elements(at least one). The duplicate value is an entrance to the cycle. Given below is an example to show how cycle exists:  
 **For Example:** Let the array arr[] = {2, 6, 4, 1, 3, 1, 5}index| 0| 1| 2|
3| 4| 5| 6| arr| 2| 6| 4| 1| 3| 1| 5  
---|---|---|---|---|---|---|---  
  
Starting from index 0, the traversal looks as follows:

> arr[0] = **2** –> arr[2] = **4** –> arr[4] = **3** –> arr[3] = **1** –>
> arr[1] = **6** –> arr[6] = **5** –> arr[5] = **1**.

The sequence forms cycle as shown below:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200616013601/Firefox_Screenshot_2020-06-15T20-05-04.185Z.png)

  5. Algorithm consists of two parts and uses two pointers, usually called **tortoise** and **hare**.
    *  **hare = arr[arr[hare]]** is twice as fast as **tortoise = arr[tortoise]**.
    * Since the hare goes fast, it would be the first one who enters the cycle and starts to run around the cycle.
    * At some point, the tortoise enters the cycle as well, and since it’s moving slower the hare catches the tortoise up at some intersection point.
    * Note that the intersection point is not the cycle entrance in the general case, but the two intersect at somewhere middle in cycle.
    * Move tortoise to the starting point of sequence and hare remains within cycle and both move with the same speed i.e. **tortoise = arr[tortoise]** and **hare = arr[hare]**. Now they intersect at duplicate element.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code for the above approach

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the duplicate

// value in the given array arr[]

void findDuplicate(int arr[])

{

 

 // Initialise variables

 int tortoise = arr[0];

 int hare = arr[0];

 

 // Loop till we find the

 // duplicate element

 while (1) {

 

 tortoise = arr[tortoise];

 

 // Hare moves with twice

 // the speed of tortoise

 hare = arr[arr[hare]];

 if (tortoise == hare)

 break;

 }

 

 tortoise = arr[0];

 

 // Loop to get start point

 // of the cycle as start

 // point will be the duplicate

 // element

 while (tortoise != hare) {

 tortoise = arr[tortoise];

 hare = arr[hare];

 }

 

 // Print the duplicate element

 cout << tortoise;

}

 

// Driver Code

int main()

{

 // Given array

 int arr[] = { 2, 6, 4, 1, 3, 1, 5 };

 

 // Function Call

 findDuplicate(arr);

 

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

// Java code for the above approach

class GFG{

 

// Function to find the duplicate

// value in the given array arr[]

static void findDuplicate(int arr[])

{

 

 // Initialise variables

 int tortoise = arr[0];

 int hare = arr[0];

 

 // Loop till we find the

 // duplicate element

 while (true)

 {

 tortoise = arr[tortoise];

 

 // Hare moves with twice

 // the speed of tortoise

 hare = arr[arr[hare]];

 if (tortoise == hare)

 break;

 }

 

 tortoise = arr[0];

 

 // Loop to get start point

 // of the cycle as start

 // point will be the duplicate

 // element

 while (tortoise != hare)

 {

 tortoise = arr[tortoise];

 hare = arr[hare];

 }

 

 // Print the duplicate element

 System.out.print(tortoise);

}

 

// Driver Code

public static void main (String []args)

{

 

 // Given array

 int arr[] = { 2, 6, 4, 1, 3, 1, 5 };

 

 // Function Call

 findDuplicate(arr);

} 

}

 

// This code is contributed by chitranayal  
  
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

 

# Function to find the duplicate 

# value in the given array arr[] 

def findDuplicate(arr): 

 

 # Initialise variables 

 tortoise = arr[0] 

 hare = arr[0]

 

 # Loop till we find the 

 # duplicate element 

 while (1): 

 

 tortoise = arr[tortoise]

 

 # Hare moves with twice 

 # the speed of tortoise 

 hare = arr[arr[hare]] 

 if (tortoise == hare): 

 break

 

 tortoise = arr[0] 

 

 # Loop to get start point 

 # of the cycle as start 

 # point will be the duplicate 

 # element 

 while (tortoise != hare):

 tortoise = arr[tortoise] 

 hare = arr[hare]

 

 # Print the duplicate element 

 print (tortoise) 

 

# Driver Code 

 

# Given array 

arr = [ 2, 6, 4, 1, 3, 1, 5 ]

 

# Function Call 

findDuplicate(arr)

 

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

// C# program for the above approach

using System;

 

class GFG{

 

// Function to find the duplicate

// value in the given array []arr

static void findDuplicate(int []arr)

{

 

 // Initialise variables

 int tortoise = arr[0];

 int hare = arr[0];

 

 // Loop till we find the

 // duplicate element

 while (true)

 {

 tortoise = arr[tortoise];

 

 // Hare moves with twice

 // the speed of tortoise

 hare = arr[arr[hare]];

 if (tortoise == hare)

 break;

 }

 

 tortoise = arr[0];

 

 // Loop to get start point

 // of the cycle as start

 // point will be the duplicate

 // element

 while (tortoise != hare)

 {

 tortoise = arr[tortoise];

 hare = arr[hare];

 }

 

 // Print the duplicate element

 Console.Write(tortoise);

}

 

// Driver Code

public static void Main(String []args)

{

 

 // Given array

 int []arr = { 2, 6, 4, 1, 3, 1, 5 };

 

 // Function Call

 findDuplicate(arr);

} 

}

 

// This code is contributed by Amit Katiyar  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

**Time Complexity:** _O(N)_  
 **Auxiliary Space:** _O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

