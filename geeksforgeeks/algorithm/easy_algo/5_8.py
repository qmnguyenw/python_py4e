Minimize the sum of the squares of the sum of elements of each group the array
is divided into



Given an array consisting of **even** number of elements, the task is to
divide the array into **M** group of elements (every group must contain at
least 2 elements) such that the sum of the squares of the sums of each group
is minimized i.e.,  
(sum_of_elements_of_group1)2 \+ (sum_of_elements_of_group2)2 \+
(sum_of_elements_of_group3)2 \+ (sum_of_elements_of_group4)2 \+ ….. +
(sum_of_elements_of_groupM)2

 **Examples:**

>  **Input:** arr[] = {5, 8, 13, 45, 6, 3}  
>  **Output:** 2824  
> Groups can be (3, 45), (5, 13) and (6, 8)  
> (3 + 45)2 \+ (5 + 13)2 \+ (6 + 8)2 = 482 \+ 182 \+ 142 = 2304 + 324 + 196 =
> 2824
>
>  **Input:** arr[] = {53, 28, 143, 5}  
>  **Output:** 28465

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Our final sum depends on two factors:

  

  

  1. Sum of the elements of each group.
  2. The sum of squares of all such groups.

If we minimize both the factors mentioned above, we can minimize the result.
To minimize the second factor we should make groups of minimum size i.e. just
two elements. To minimize first factor we can pair smallest number with
largest number, second smallest number to second largest number and so on.

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

 

// Function to return the minimized sum

unsigned long long findAnswer(int n, 

 vector<int>& arr)

{

 

 // Sort the array to pair the elements

 sort(arr.begin(), arr.end());

 

 // Variable to hold the answer

 unsigned long long sum = 0;

 

 // Pair smallest with largest, second

 // smallest with second largest, and 

 // so on

 for (int i = 0; i < n / 2; ++i) {

 sum += (arr[i] + arr[n - i - 1])

 * (arr[i] + arr[n - i - 1]);

 }

 

 return sum;

}

 

// Driver code

int main()

{

 std::vector<int> arr = { 53, 28, 143, 5 };

 int n = arr.size();

 cout << findAnswer(n, arr);

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

 

 // Function to return the minimized sum

 static int findAnswer(int n, int[] arr)

 {

 

 // Sort the array to pair the elements

 Arrays.sort(arr);

 

 // Variable to hold the answer

 int sum = 0;

 

 // Pair smallest with largest, second

 // smallest with second largest, and 

 // so on

 for (int i = 0; i < n / 2; ++i) 

 {

 sum += (arr[i] + arr[n - i - 1])

 * (arr[i] + arr[n - i - 1]);

 }

 

 return sum;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int[] arr = {53, 28, 143, 5};

 int n = arr.length;

 System.out.println(findAnswer(n, arr));

 }

}

 

// This code has been contributed by 29AjayKumar  
  
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

# Python 3 implementation of the approach

 

# Function to return the minimized sum

def findAnswer(n, arr):

 

 # Sort the array to pair the elements

 arr.sort(reverse = False)

 

 # Variable to hold the answer

 sum = 0

 

 # Pair smallest with largest, second

 # smallest with second largest, and 

 # so on

 for i in range(int(n / 2)):

 sum += ((arr[i] + arr[n - i - 1]) *

 (arr[i] + arr[n - i - 1]))

 

 return sum

 

# Driver code

if __name__ == '__main__':

 arr = [53, 28, 143, 5]

 n = len(arr)

 print(findAnswer(n, arr))

 

# This code is contributed by

# Surendra_Gangwar  
  
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

 

class GFG

{

 

// Function to return the minimized sum

static int findAnswer(int n, int []arr)

{

 

 // Sort the array to pair the elements

 Array.Sort(arr);

 

 // Variable to hold the answer

 int sum = 0;

 

 // Pair smallest with largest, second

 // smallest with second largest, and 

 // so on

 for (int i = 0; i < n / 2; ++i) 

 {

 sum += (arr[i] + arr[n - i - 1])

 * (arr[i] + arr[n - i - 1]);

 }

 

 return sum;

}

 

// Driver code

static void Main()

{

 int []arr = { 53, 28, 143, 5 };

 int n = arr.Length;

 Console.WriteLine(findAnswer(n, arr));

}

}

 

// This code is contributed by mits  
  
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

 

// Function to return the minimized sum

function findAnswer($n, $arr)

{

 

 // Sort the array to pair the elements

 sort($arr);

 

 // Variable to hold the answer

 $sum = 0;

 

 // Pair smallest with largest, second

 // smallest with second largest, and 

 // so on

 for ($i = 0; $i < $n / 2; ++$i) 

 {

 $sum += ($arr[$i] + $arr[$n - $i - 1]) * 

 ($arr[$i] + $arr[$n - $i - 1]);

 }

 

 return $sum;

}

 

// Driver code

$arr = array( 53, 28, 143, 5);

$n = count($arr);

echo findAnswer($n, $arr);

 

// This code is contributed by chandan_jnu

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    28465
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

