Count of elements A[i] such that A[i] + 1 is also present in the Array



Given an integer array **arr** the task is to count the number of elements
‘A[i]’, such that A[i] + 1 is also present in the array.  
 **Note:** If there are duplicates in the array, count them separately.  
 **Examples:**  

> **Input:** arr = [1, 2, 3]  
> **Output:** 2  
> **Explanation:**  
> 1 and 2 are counted cause 2 and 3 are in arr.  
>  **Input:** arr = [1, 1, 3, 3, 5, 5, 7, 7]  
> **Output:** 0  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 ** _Approach 1: Brute Force Solution_**  
For all the elements in the array, return the total count after examining all
elements  

  * For current element x, compute x + 1, and search all positions before and after the current value for x + 1.
  * If you find x + 1, add 1 to the total count

Below is the implementation of the above approach:  

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count of elements

// A[i] such that A[i] + 1

// is also present in the Array

#include <bits/stdc++.h>

using namespace std;

// Function to find the countElements

int countElements(int* arr, int n)

{

 // Initialize count as zero

 int count = 0;

 // Iterate over each element

 for (int i = 0; i < n; i++) {

 // Store element in int x

 int x = arr[i];

 // Calculate x + 1

 int xPlusOne = x + 1;

 // Initialize found as false

 bool found = false;

 // Run loop to search for x + 1

 // after the current element

 for (int j = i + 1; j < n; j++) {

 if (arr[j] == xPlusOne) {

 found = true;

 break;

 }

 }

 // Run loop to search for x + 1

 // before the current element

 for (int k = i - 1;

 !found && k >= 0; k--) {

 if (arr[k] == xPlusOne) {

 found = true;

 break;

 }

 }

 // if found is true, increment count

 if (found == true) {

 count++;

 }

 }

 return count;

}

// Driver program

int main()

{

 int arr[] = { 1, 2, 3 };

 int n = sizeof(arr) / sizeof(arr[0]);

 // call countElements function on array

 cout << countElements(arr, n);

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

// Java program to count of elements

// A[i] such that A[i] + 1

// is also present in the Array

import java.io.*;

import java.util.Arrays;

class GFG{

 

// Function to find the countElements

public static int countElements(int[] arr, int n)

{

 

 // Initialize count as zero

 int count = 0;

 

 // Iterate over each element

 for (int i = 0; i < n; i++)

 {

 

 // Store element in int x

 int x = arr[i];

 

 // Calculate x + 1

 int xPlusOne = x + 1;

 

 // Initialize found as false

 boolean found = false;

 

 // Run loop to search for x + 1

 // after the current element

 for (int j = i + 1; j < n; j++)

 {

 if (arr[j] == xPlusOne)

 {

 found = true;

 break;

 }

 }

 

 // Run loop to search for x + 1

 // before the current element

 for (int k = i - 1; !found && k >= 0; k--)

 {

 if (arr[k] == xPlusOne)

 {

 found = true;

 break;

 }

 }

 

 // If found is true, increment count

 if (found == true)

 {

 count++;

 }

 }

 return count;

}

 

// Driver code

public static void main (String[] args)

{

 int arr[] = { 1, 2, 3 };

 int n = arr.length;

 

 // Call countElements function on array

 System.out.println(countElements(arr, n));

}

}

//This code is contributed by shubhamsingh10  
  
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

# Python3 program to count of elements

# A[i] such that A[i] + 1

# is also present in the Array

# Function to find the countElements

def countElements(arr,n):

 # Initialize count as zero

 count = 0

 # Iterate over each element

 for i in range(n):

 # Store element in int x

 x = arr[i]

 # Calculate x + 1

 xPlusOne = x + 1

 # Initialize found as false

 found = False

 # Run loop to search for x + 1

 # after the current element

 for j in range(i + 1,n,1):

 if (arr[j] == xPlusOne):

 found = True

 break

 # Run loop to search for x + 1

 # before the current element

 k = i - 1

 while(found == False and k >= 0):

 if (arr[k] == xPlusOne):

 found = True

 break

 k -= 1

 # if found is true, increment count

 if (found == True):

 count += 1

 return count

# Driver program

if __name__ == '__main__':

 arr = [1, 2, 3]

 n = len(arr)

 # call countElements function on array

 print(countElements(arr, n))

# This code is contributed by Surendra_Gangwar  
  
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

// C# program to count of elements

// A[i] such that A[i] + 1

// is also present in the Array

using System;

class GFG{

 

 // Function to find the countElements

 static int countElements(int[] arr, int n)

 {

 // Initialize count as zero

 int count = 0;

 

 // Iterate over each element

 for (int i = 0; i < n; i++) {

 

 // Store element in int x

 int x = arr[i];

 

 // Calculate x + 1

 int xPlusOne = x + 1;

 

 // Initialize found as false

 bool found = false;

 

 // Run loop to search for x + 1

 // after the current element

 for (int j = i + 1; j < n; j++) {

 if (arr[j] == xPlusOne) {

 found = true;

 break;

 }

 }

 

 // Run loop to search for x + 1

 // before the current element

 for (int k = i - 1;

 !found && k >= 0; k--) {

 if (arr[k] == xPlusOne) {

 found = true;

 break;

 }

 }

 

 // if found is true,

 // increment count

 if (found == true) {

 count++;

 }

 }

 

 return count;

 }

 

 // Driver program

 static public void Main ()

 {

 int[] arr = { 1, 2, 3 };

 int n = arr.Length;

 

 // call countElements function on array

 Console.WriteLine(countElements(arr, n));

 }

}

// This code is contributed by shubhamsingh10  
  
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

// JavaScript program to count of elements

// A[i] such that A[i] + 1

// is also present in the Array

// Function to find the countElements

function countElements(arr, n)

{

 // Initialize count as zero

 let count = 0;

 // Iterate over each element

 for (let i = 0; i < n; i++) {

 // Store element in int x

 let x = arr[i];

 // Calculate x + 1

 let xPlusOne = x + 1;

 // Initialize found as false

 let found = false;

 // Run loop to search for x + 1

 // after the current element

 for (let j = i + 1; j < n; j++)

 {

 if (arr[j] == xPlusOne)

 {

 found = true;

 break;

 }

 }

 // Run loop to search for x + 1

 // before the current element

 for (let k = i - 1;

 !found && k >= 0; k--) {

 if (arr[k] == xPlusOne) {

 found = true;

 break;

 }

 }

 // if found is true, increment count

 if (found == true) {

 count++;

 }

 }

 return count;

}

// Driver program

 let arr = [ 1, 2, 3 ];

 let n = arr.length;

 // call countElements function on array

 document.write(countElements(arr, n));

// This code is contributed by Surbhi Tyagi.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    2

**Time Complexity** : In the above approach, for a given element, we check all
other elements, So the time complexity is **O(N*N)** where N is no of
elements.  
**Auxiliary Space Complexity** : In the above approach, we are not using any
additional space, so Auxiliary space complexity is **O(1)**.  
 ** _Approach 2: Using_** ** _Map_**  

  * For all elements in the array, say x, add x-1 to the map
  * Again, for all elements in the array, say x, check if it exists in the map. If it exists, increment the counter
  * Return the total count after examining all keys in the map

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count of elements

// A[i] such that A[i] + 1

// is also present in the Array

#include <bits/stdc++.h>

using namespace std;

// Function to find the countElements

int countElements(vector<int>& arr)

{

 int size = arr.size();

 // Initialize result as zero

 int res = 0;

 // Create map

 map<int, bool> dat;

 // First loop to fill the map

 for (int i = 0; i < size; ++i) {

 dat[arr[i] - 1] = true;

 }

 // Second loop to check the map

 for (int i = 0; i < size; ++i) {

 if (dat[arr[i]] == true) {

 res++;

 }

 }

 return res;

}

// Driver program

int main()

{

 // Input Array

 vector<int> arr = { 1, 3, 2, 3, 5, 0 };

 // Call the countElements function

 cout << countElements(arr) << endl;

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

// Java program to count of elements

// A[i] such that A[i] + 1 is 

// also present in the Array

import java.util.*;

class GFG{

 

// Function to find the countElements

public static int countElements(int[] arr)

{

 int size = arr.length;

 

 // Initialize result as zero

 int res = 0;

 

 // Create map

 Map<Integer, Boolean> dat = new HashMap<>();

 

 // First loop to fill the map

 for(int i = 0; i < size; ++i)

 {

 dat.put((arr[i] - 1), true);

 }

 

 // Second loop to check the map

 for(int i = 0; i < size; ++i)

 {

 if (dat.containsKey(arr[i]) == true)

 {

 res++;

 }

 }

 return res;

}

 

// Driver code

public static void main(String[] args)

{

 

 // Input Array

 int[] arr = { 1, 3, 2, 3, 5, 0 };

 

 // Call the countElements function

 System.out.println(countElements(arr));

 

}

}

// This code is contributed by shad0w1947  
  
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

# Python program to count of elements

# A[i] such that A[i] + 1

# is also present in the Array

# Function to find the countElements

def countElements(arr):

 

 size = len(arr)

 

 # Initialize result as zero

 res = 0

 

 # Create map

 dat={}

 

 # First loop to fill the map

 for i in range(size):

 dat[arr[i] - 1] = True

 

 # Second loop to check the map

 for i in range(size):

 if (arr[i] in dat):

 res += 1

 

 return res

# Driver program

# Input Array

arr = [1, 3, 2, 3, 5, 0]

# Call the countElements function

print(countElements(arr))

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

// C# program to count of elements

// A[i] such that A[i] + 1 is

// also present in the Array

using System;

using System.Collections.Generic;

class GFG{

 

// Function to find the countElements

public static int countElements(int[] arr)

{

 int size = arr.Length;

 

 // Initialize result as zero

 int res = 0;

 

 // Create map

 Dictionary<int,

 Boolean> dat = new Dictionary<int,

 Boolean>();

 

 // First loop to fill the map

 for(int i = 0; i < size; ++i)

 {

 if(!dat.ContainsKey(arr[i] - 1))

 dat.Add((arr[i] - 1), true);

 }

 

 // Second loop to check the map

 for(int i = 0; i < size; ++i)

 {

 if (dat.ContainsKey(arr[i]) == true)

 {

 res++;

 }

 }

 return res;

}

 

// Driver code

public static void Main(String[] args)

{

 

 // Input Array

 int[] arr = { 1, 3, 2, 3, 5, 0 };

 

 // Call the countElements function

 Console.WriteLine(countElements(arr));

}

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    3

**Time Complexity** : In the above approach, we iterate over the array twice.
Once for filling the map and second time for checking the elements in the map,
So the time complexity is **O(N)** where N is no of elements.  
**Auxiliary Space Complexity** : In the above approach, we are using an
additional map which can contain N elements, so auxiliary space complexity is
**O(N)**.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

