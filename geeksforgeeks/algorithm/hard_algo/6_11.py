Find the longest subsequence of an array having LCM at most K



Given an array **arr[]** of **N** elements and a positive integer **K**. The
task is to find the longest sub-sequence in the array having LCM (Least Common
Multiple) at most **K**. Print the LCM and the length of the sub-sequence,
following the indexes (starting from 0) of the elements of the obtained sub-
sequence. Print **-1** if it is not possible to do so.

 **Examples:**

>  **Input:** arr[] = {2, 3, 4, 5}, K = 14  
>  **Output:**  
>  LCM = 12, Length = 3  
> Indexes = 0 1 2
>
>  **Input:** arr[] = {12, 33, 14, 52}, K = 4  
>  **Output:** -1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Find all the unique elements of the array and their respective
frequencies. Now the highest LCM that you are supposed to get is **K**.
Suppose you have a number **X** such that **1 ≤ X ≤ K** , obtain all the
unique numbers from the array whom **X** is a multiple of and add their
frequencies to **numCount** of **X**. The answer will be the number with
highest **numCount** , let it be your LCM. Now, to obtain the indexes of the
numbers of the sub-sequence, start traversing the array from the beginning and
print the index **i** if **LCM % arr[i] = 0**.

  

  

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

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the longest subsequence

// having LCM less than or equal to K

void findSubsequence(int* arr, int n, int k)

{

 

 // Map to store unique elements

 // and their frequencies

 map<int, int> M;

 

 // Update the frequencies

 for (int i = 0; i < n; ++i)

 ++M[arr[i]];

 

 // Array to store the count of numbers whom

 // 1 <= X <= K is a multiple of

 int* numCount = new int[k + 1];

 

 for (int i = 0; i <= k; ++i)

 numCount[i] = 0;

 

 // Check every unique element

 for (auto p : M) {

 if (p.first <= k) {

 

 // Find all its multiples <= K

 for (int i = 1;; ++i) {

 if (p.first * i > k)

 break;

 

 // Store its frequency

 numCount[p.first * i] += p.second;

 }

 }

 else

 break;

 }

 

 int lcm = 0, length = 0;

 

 // Obtain the number having maximum count

 for (int i = 1; i <= k; ++i) {

 if (numCount[i] > length) {

 length = numCount[i];

 lcm = i;

 }

 }

 

 // Condition to check if answer

 // doesn't exist

 if (lcm == 0)

 cout << -1 << endl;

 else {

 

 // Print the answer

 cout << "LCM = " << lcm

 << ", Length = " << length << endl;

 

 cout << "Indexes = ";

 for (int i = 0; i < n; ++i)

 if (lcm % arr[i] == 0)

 cout << i << " ";

 }

}

 

// Driver code

int main()

{

 

 int k = 14;

 int arr[] = { 2, 3, 4, 5 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 findSubsequence(arr, n, k);

 

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

// Java implementation of the approach

import java.util.*;

 

class GFG

{

 // Function to find the longest subsequence

 // having LCM less than or equal to K

 static void findSubsequence(int []arr, int n, int k)

 {

 

 // Map to store unique elements

 // and their frequencies

 HashMap<Integer, Integer> M = new HashMap<Integer,Integer>();

 

 // Update the frequencies

 for (int i = 0; i < n; ++i)

 {

 if(M.containsKey(arr[i]))

 M.put(arr[i], M.get(arr[i])+1);

 else

 M.put(arr[i], 1);

 }

 

 // Array to store the count of numbers whom

 // 1 <= X <= K is a multiple of

 int [] numCount = new int[k + 1];

 

 for (int i = 0; i <= k; ++i)

 numCount[i] = 0;

 

 Iterator<HashMap.Entry<Integer, Integer>> itr = M.entrySet().iterator(); 

 

 // Check every unique element

 while(itr.hasNext()) 

 {

 HashMap.Entry<Integer, Integer> entry = itr.next();

 if (entry.getKey() <= k) 

 {

 

 // Find all its multiples <= K

 for (int i = 1;; ++i) 

 {

 if (entry.getKey() * i > k)

 break;

 

 // Store its frequency

 numCount[entry.getKey() * i] += entry.getValue();

 }

 }

 else

 break;

 }

 

 int lcm = 0, length = 0;

 

 // Obtain the number having maximum count

 for (int i = 1; i <= k; ++i) 

 {

 if (numCount[i] > length) 

 {

 length = numCount[i];

 lcm = i;

 }

 }

 

 // Condition to check if answer

 // doesn't exist

 if (lcm == 0)

 System.out.println(-1);

 else

 {

 

 // Print the answer

 System.out.println("LCM = " + lcm

 + " Length = " + length );

 

 System.out.print( "Indexes = ");

 for (int i = 0; i < n; ++i)

 if (lcm % arr[i] == 0)

 System.out.print(i + " ");

 }

 }

 

 // Driver code

 public static void main (String[] args) 

 {

 

 int k = 14;

 int arr[] = { 2, 3, 4, 5 };

 int n = arr.length;

 

 findSubsequence(arr, n, k);

 }

}

 

// This code is contributed by ihritik  
  
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

from collections import defaultdict

 

# Function to find the longest subsequence

# having LCM less than or equal to K

def findSubsequence(arr, n, k):

 

 # Map to store unique elements

 # and their frequencies

 M = defaultdict(lambda:0)

 

 # Update the frequencies

 for i in range(0, n):

 M[arr[i]] += 1

 

 # Array to store the count of numbers

 # whom 1 <= X <= K is a multiple of

 numCount = [0] * (k + 1)

 

 # Check every unique element

 for p in M: 

 if p <= k: 

 

 # Find all its multiples <= K

 i = 1

 while p * i <= k: 

 

 # Store its frequency

 numCount[p * i] += M[p]

 i += 1

 

 else:

 break

 

 lcm, length = 0, 0

 

 # Obtain the number having maximum count

 for i in range(1, k + 1): 

 if numCount[i] > length: 

 length = numCount[i]

 lcm = i

 

 # Condition to check if answer doesn't exist

 if lcm == 0:

 print(-1)

 else:

 

 # Print the answer

 print("LCM = {0}, Length = {1}".format(lcm, length))

 

 print("Indexes = ", end = "")

 for i in range(0, n):

 if lcm % arr[i] == 0:

 print(i, end = " ")

 

# Driver code

if __name__ == "__main__":

 

 k = 14

 arr = [2, 3, 4, 5] 

 n = len(arr)

 

 findSubsequence(arr, n, k)

 

# This code is contributed by Rituraj Jain  
  
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

using System.Collections.Generic;

 

class GFG

{

 // Function to find the longest subsequence

 // having LCM less than or equal to K

 static void findSubsequence(int []arr, int n, int k)

 {

 

 // Map to store unique elements

 // and their frequencies

 Dictionary<int, int> M = new Dictionary<int, int>();

 

 // Update the frequencies

 for (int i = 0; i < n; ++i)

 {

 if(M.ContainsKey(arr[i]))

 M[arr[i]]++;

 else

 M[arr[i]] = 1;

 }

 

 // Array to store the count of numbers whom

 // 1 <= X <= K is a multiple of

 int [] numCount = new int[k + 1];

 

 for (int i = 0; i <= k; ++i)

 numCount[i] = 0;

 

 Dictionary<int, int>.KeyCollection keyColl = M.Keys;

 

 // Check every unique element

 foreach(int key in keyColl)

 {

 if ( key <= k) 

 {

 

 // Find all its multiples <= K

 for (int i = 1;; ++i) 

 {

 if (key * i > k)

 break;

 

 // Store its frequency

 numCount[key * i] += M[key];

 }

 }

 else

 break;

 }

 

 int lcm = 0, length = 0;

 

 // Obtain the number having maximum count

 for (int i = 1; i <= k; ++i)

 {

 if (numCount[i] > length) 

 {

 length = numCount[i];

 lcm = i;

 }

 }

 

 // Condition to check if answer

 // doesn't exist

 if (lcm == 0)

 Console.WriteLine(-1);

 else

 {

 

 // Print the answer

 Console.WriteLine("LCM = " + lcm

 + " Length = " + length );

 

 Console.Write( "Indexes = ");

 for (int i = 0; i < n; ++i)

 if (lcm % arr[i] == 0)

 Console.Write(i + " ");

 }

 }

 

 // Driver code

 public static void Main () 

 {

 

 int k = 14;

 int []arr = { 2, 3, 4, 5 };

 int n = arr.Length;

 

 findSubsequence(arr, n, k);

 }

}

 

// This code is contributed by ihritik  
  
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

// PHP implementation of the approach 

 

// Function to find the longest subsequence 

// having LCM less than or equal to K 

function findSubsequence($arr, $n, $k) 

{ 

 

 // Map to store unique elements 

 // and their frequencies 

 $M = array();

 

 for($i = 0; $i < $n; $i++)

 $M[$arr[$i]] = 0 ;

 

 // Update the frequencies 

 for ($i = 0; $i < $n; ++$i) 

 ++$M[$arr[$i]]; 

 

 // Array to store the count of numbers 

 // whom 1 <= X <= K is a multiple of 

 $numCount = array(); 

 

 for ($i = 0; $i <= $k; ++$i) 

 $numCount[$i] = 0; 

 

 // Check every unique element 

 foreach($M as $key => $value)

 {

 if ($key <= $k)

 { 

 

 // Find all its multiples <= K 

 for ($i = 1;; ++$i) 

 { 

 if ($key * $i > $k) 

 break; 

 

 // Store its frequency 

 $numCount[$key * $i] += $value; 

 } 

 } 

 else

 break; 

 } 

 

 $lcm = 0; $length = 0; 

 

 // Obtain the number having

 // maximum count 

 for ($i = 1; $i <= $k; ++$i) 

 { 

 if ($numCount[$i] > $length)

 { 

 $length = $numCount[$i]; 

 $lcm = $i; 

 } 

 } 

 

 // Condition to check if answer 

 // doesn't exist 

 if ($lcm == 0) 

 echo -1 << "\n"; 

 else

 { 

 

 // Print the answer 

 echo "LCM = ", $lcm, 

 ", Length = ", $length, "\n"; 

 

 echo "Indexes = "; 

 for ($i = 0; $i < $n; ++$i) 

 if ($lcm % $arr[$i] == 0) 

 echo $i, " "; 

 } 

} 

 

// Driver code 

$k = 14; 

$arr = array( 2, 3, 4, 5 ); 

$n = count($arr);

 

findSubsequence($arr, $n, $k); 

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    LCM = 12, Length = 3
    Indexes = 0 1 2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

