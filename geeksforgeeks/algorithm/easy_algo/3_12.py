Sentinel Linear Search



Sentinel Linear Search as the name suggests is a type of Linear Search where
the number of comparisons are reduced as compared to a traditional linear
search. When a linear search is performed on an array of size N then in the
worst case a total of N comparisons are made when the element to be searched
is compared to all the elements of the array and (N + 1) comparisons are made
for the index of the element to be compared so that the index is not out of
bounds of the array which can be reduced in a Sentinel Linear Search.  
In this search, the last element of the array is replaced with the element to
be searched and then the linear search is performed on the array without
checking whether the current index is inside the index range of the array or
not because the element to be searched will definitely be found inside the
array even if it was not present in the original array since the last element
got replaced with it. So, the index to be checked will never be out of bounds
of the array. The number of comparisons in the worst case here will be (N +
2).  
 **Examples:**

> **Input:** arr[] = {10, 20, 180, 30, 60, 50, 110, 100, 70}, x = 180  
> **Output:** 180 is present at index 2  
>  **Input:** arr[] = {10, 20, 180, 30, 60, 50, 110, 100, 70}, x = 90  
> **Output:** Not found

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <iostream>

using namespace std;

// Function to search x in the given array

void sentinelSearch(int arr[], int n, int key)

{

 // Last element of the array

 int last = arr[n - 1];

 // Element to be searched is

 // placed at the last index

 arr[n - 1] = key;

 int i = 0;

 while (arr[i] != key)

 i++;

 // Put the last element back

 arr[n - 1] = last;

 if ((i < n - 1) || (arr[n - 1] == key))

 cout << key << " is present at index " << i;

 else

 cout << "Element Not found";

}

// Driver code

int main()

{

 int arr[] = { 10, 20, 180, 30, 60, 50, 110, 100, 70 };

 int n = sizeof(arr) / sizeof(arr[0]);

 int key = 180;

 sentinelSearch(arr, n, key);

 return 0;

}

// This code is contributed by Mandeep Dalavi  
  
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

// Java implementation of the approach

class GFG {

 // Function to search x in the given array

 static void sentinelSearch(int arr[], int n, int key)

 {

 // Last element of the array

 int last = arr[n - 1];

 // Element to be searched is

 // placed at the last index

 arr[n - 1] = key;

 int i = 0;

 while (arr[i] != key)

 i++;

 // Put the last element back

 arr[n - 1] = last;

 if ((i < n - 1) || (arr[n - 1] == key))

 System.out.println(key + " is present at index "

 + i);

 else

 System.out.println("Element Not found");

 }

 // Driver code

 public static void main(String[] args)

 {

 int arr[]

 = { 10, 20, 180, 30, 60, 50, 110, 100,
70 };

 int n = arr.length;

 int key = 180;

 sentinelSearch(arr, n, key);

 }

}

// This code is contributed by Ankit Rai, Mandeep Dalavi  
  
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

# Python3 implementation of the approach

# Function to search key in the given array

def sentinelSearch(arr, n, key):

 # Last element of the array

 last = arr[n - 1]

 # Element to be searched is

 # placed at the last index

 arr[n - 1] = key

 i = 0

 while (arr[i] != key):

 i += 1

 # Put the last element back

 arr[n - 1] = last

 if ((i < n - 1) or (arr[n - 1] == key)):

 print(key, "is present at index", i)

 else:

 print("Element Not found")

# Driver code

arr = [10, 20, 180, 30, 60, 50, 110, 100,
70]

n = len(arr)

key = 180

sentinelSearch(arr, n, key)

# This code is contributed by divyamohan123, Mandeep Dalavi  
  
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

// C# implementation of the approach

using System;

class GFG {

 // Function to search x in the given array

 static void sentinelSearch(int[] arr, int n, int key)

 {

 // Last element of the array

 int last = arr[n - 1];

 // Element to be searched is

 // placed at the last index

 arr[n - 1] = key;

 int i = 0;

 while (arr[i] != key)

 i++;

 // Put the last element back

 arr[n - 1] = last;

 if ((i < n - 1) || (arr[n - 1] == key))

 Console.WriteLine(key + " is present"

 + " at index " + i);

 else

 Console.WriteLine("Element Not found");

 }

 // Driver code

 public static void Main()

 {

 int[] arr

 = { 10, 20, 180, 30, 60, 50, 110, 100, 70 };

 int n = arr.Length;

 int key = 180;

 sentinelSearch(arr, n, key);

 }

}

// This code is contributed by Mohit kumar, Mandeep Dalavi  
  
---  
  
 __

 __

 **Output:**

    
    
    180 is present at index 2

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

