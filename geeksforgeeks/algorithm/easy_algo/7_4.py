Maximum removal from array when removal time >= waiting time



Given there are N elements in an array. The task is to remove elements from
the array from left to right. However, some time is required to remove an
element from the array(let us call it **removal time** ). The time to remove
an element is equal to the value of the of that element in seconds.

An element can only be removed when the time required to remove it(removal
time) is **greater than or equal** to the time it waits in the array.

 **Note** : It is allowed to change the order of elements in the array before
starting to remove elements. Your task is to find the maximum number of
elements which can be removed from the array.

 **Examples:**

>  **Input** : arr[] = {6, 5, 11, 3}  
>  **Output** : 3  
>  **Explanation** : Let us reorder the elements in the following way:  
> 3, 5, 6, 11  
> -The first element takes 3 seconds to get removed. Since it is the first
> element, it can be removed in 3 seconds.  
> -The second element waits 3 seconds in the array. This element takes 5
> seconds to get removed, which is more than it’s waiting time, hence it can
> be removed.  
> -The third element waits 8 seconds in the array. This element takes 6
> seconds to get removed, which is less than it’s waiting time, hence it
> cannot be removed and it is skipped.  
> -The fourth element also waits 8 seconds in the array. This element takes 11
> seconds to get removed, which is more than it’s waiting time, hence it can
> be removed.  
> -Hence, a maximum of 3 elements can be removed.
>
>  
>
>
>  
>
>
>  **Input** : arr[] = {5, 4, 1, 10}  
>  **Output** : 4  
>  **Explanation** : Let us reorder the elements in the following way:  
> 1, 4, 5, 10  
> It can be observed that all of them can be removed since each element’s
> removal time is greater or equal to their waiting time.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The idea is to arrange all the elements in **ascending order** of their
removal time. Start iterating from left side and maintain a **cumulative sum**
of the removal time (which will serve as the **waiting time** for next
element). Check at each element, if it’s removal time is greater than or equal
to the cumulative time(it’s waiting time). If it is less, than it cannot be
removed. If it is equal or greater, than it can be removed and add it’s
removal time in cumulative sum. Proceed till the end of the array.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code to find the maximum number of

// elements that can be removed

#include <bits/stdc++.h>

using namespace std;

 

// Function to find maximum number of

// elements that can be removed

int maxRemoval(int arr[], int n)

{

 // it will contain frequency of

 // elements that can be removed

 int count = 0;

 

 // maintain cummulative sum of removal time

 int cummulative_sum = 0;

 

 // arrange elements in ascending order

 // of their removal time

 sort(arr, arr + n);

 

 for (int i = 0; i < n; i++) {

 if (arr[i] >= cummulative_sum) {

 count++;

 cummulative_sum += arr[i];

 }

 }

 

 return count;

}

 

// Driver code

int main()

{

 int arr[] = { 10, 5, 3, 7, 2 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << maxRemoval(arr, n);

 

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

// Java code to find the maximum number of

// elements that can be removed

import java.io.*;

import java.util.*;

 

class GFG {

 

// Function to find maximum number of

// elements that can be removed

static int maxRemoval(int arr[], int n)

{

 // it will contain frequency of

 // elements that can be removed

 int count = 0;

 

 // maintain cummulative sum of removal time

 int cummulative_sum = 0;

 

 // arrange elements in ascending order

 // of their removal time

 Arrays.sort(arr);

 

 for (int i = 0; i < n; i++) {

 if (arr[i] >= cummulative_sum) {

 count++;

 cummulative_sum += arr[i];

 }

 }

 

 return count;

}

 

// Driver code

 

 public static void main (String[] args) {

 int arr[] = { 10, 5, 3, 7, 2 };

 int n = arr.length;

 System.out.println(maxRemoval(arr, n));

 }

}

// This code is contributed 

// by inder_verma..  
  
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

# Python3 code to find the maximum number

# of elements that can be removed 

 

# Function to find maximum number of 

# elements that can be removed 

def maxRemoval(arr, n): 

 

 # It will contain frequency of 

 # elements that can be removed 

 count = 0

 

 # maintain cummulative sum of 

 # removal time 

 cummulative_sum = 0

 

 # arrange elements in ascending 

 # order of their removal time 

 arr.sort()

 

 for i in range(n): 

 if arr[i] >= cummulative_sum: 

 count += 1

 cummulative_sum += arr[i] 

 

 return count 

 

# Driver code 

if __name__ == "__main__":

 

 arr = [10, 5, 3, 7, 2] 

 n = len(arr) 

 

 print(maxRemoval(arr, n)) 

 

# This code is contributed by

# Rituraj Jain  
  
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

// C# code to find the maximum number

// of elements that can be removed

using System; 

 

class GFG

{

 

// Function to find maximum number

// of elements that can be removed

static int maxRemoval(int[] arr, int n)

{

 // it will contain frequency of

 // elements that can be removed

 int count = 0;

 

 // maintain cummulative sum 

 // of removal time

 int cummulative_sum = 0;

 

 // arrange elements in ascending 

 // order of their removal time

 Array.Sort(arr);

 

 for (int i = 0; i < n; i++)

 {

 if (arr[i] >= cummulative_sum)

 {

 count++;

 cummulative_sum += arr[i];

 }

 }

 

 return count;

}

 

// Driver code

public static void Main ()

{

 int[] arr = { 10, 5, 3, 7, 2 };

 int n = arr.Length;

 Console.Write(maxRemoval(arr, n));

}

}

 

// This code is contributed 

// by ChitraNayal  
  
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

// PHP code to find the maximum 

// number of elements that can

// be removed

 

// Function to find maximum number 

// of elements that can be removed

function maxRemoval(&$arr, $n)

{

 // it will contain frequency of

 // elements that can be removed

 $count = 0;

 

 // maintain cummulative 

 // sum of removal time

 $cummulative_sum = 0;

 

 // arrange elements in ascending 

 // order of their removal time

 sort($arr);

 

 for ($i = 0; $i < $n; $i++) 

 {

 if ($arr[$i] >= $cummulative_sum)

 {

 $count++;

 $cummulative_sum += $arr[$i];

 }

 }

 

 return $count;

}

 

// Driver code

$arr = array(10, 5, 3, 7, 2 );

$n = sizeof($arr);

 

echo (maxRemoval($arr, $n));

 

// This code is contributed 

// by Shivi_Aggarwal 

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

