Maximum subarray sum in array formed by repeating the given array k times



Given an integer **k** and an integer array **arr[]** of **n** elements, the
task is to find the largest sub-array sum in the modified array (formed by
repeating the given array k times). For example, if arr[] = {1, 2} and k = 3
then modified array will be {1, 2, 1, 2, 1, 2}.

 **Examples:**

>  **Input:** arr[] = {1, 2}, k = 3  
>  **Output:** 9  
> Modified array will be {1, 2, 1, 2, 1, 2}  
> And the maximum sub-array sum will be 1 + 2 + 1 + 2 + 1 + 2 = 9
>
>  **Input:** arr[] = {1, -2, 1}, k = 5  
>  **Output:** 2

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **simple solution** is to create an array of size **n * k** , then run
Kadane’s algorithm to find the maximum sub-array sum. Time complexity would be
**O(n * k)** with auxiliary space **O(n * k)**.

  

  

A **better solution** is to calculate the sum of the array **arr[]** and store
it in **sum**.

  * If **sum < 0** then calculate the maximum sub-array sum of an array formed by concatenating the array two times irrespective of the **K**. For example, take arr[] = {1, -4, 1} and k = 5. The sum of the array is less than 0. So, the maximum sub-array sum of the array can be found after concatenating the array two times only irrespective of the value of **K** i.e. b[] = {1, -4, 1, 1, -4, 1} and the maximum sub-array sum = 1 + 1 = 2

.

  * If **sum > 0** then maximum sub-array will include the maximum sum as calculated in the previous step (where the array was concatenated twice) + the rest (k – 2) repetitions of the array can also be included as their sum is greater than 0 that will contribute to the maximum sum.

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

#include<bits/stdc++.h>

using namespace std;

 

 // Function to concatenate array

 void arrayConcatenate(int *arr, int *b,

 int k,int len)

 {

 // Array b will be formed by concatenation

 // array a exactly k times

 int j = 0;

 while (k > 0) 

 {

 

 for (int i = 0; i < len; i++)

 {

 b[j++] = arr[i];

 }

 k--;

 }

 }

 

 // Function to return the maximum 

 // subarray sum of arr[]

 long maxSubArrSum(int *a,int len)

 {

 int size = len;

 int max_so_far = INT_MIN;

 long max_ending_here = 0;

 

 for (int i = 0; i < size; i++)

 {

 max_ending_here = max_ending_here + a[i];

 if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 if (max_ending_here < 0)

 max_ending_here = 0;

 }

 return max_so_far;

 }

 

 // Function to return the maximum sub-array 

 // sum of the modified array

 long maxSubKSum(int *arr, int k,int len)

 {

 int arrSum = 0;

 long maxSubArrSum1 = 0;

 

 int b[(2 * len)]={0};

 

 // Concatenating the array 2 times

 arrayConcatenate(arr, b, 2,len);

 

 // Finding the sum of the array

 for (int i = 0; i < len; i++)

 arrSum += arr[i];

 

 // If sum is less than zero

 if (arrSum < 0)

 maxSubArrSum1 = maxSubArrSum(b,2*len);

 

 // If sum is greater than zero

 else

 maxSubArrSum1 = maxSubArrSum(b,2*len) +

 (k - 2) * arrSum;

 

 return maxSubArrSum1;

 }

 

 // Driver code

 int main()

 {

 int arr[] = { 1, -2, 1 };

 int arrlen=sizeof(arr)/sizeof(arr[0]);

 int k = 5;

 cout << maxSubKSum(arr, k,arrlen) << endl;

 return 0;

 }

 

// This code is contributed by mits  
  
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

public class GFG {

 

 // Function to concatenate array

 static void arrayConcatenate(int arr[], int b[], 

 int k)

 {

 // Array b will be formed by concatenation

 // array a exactly k times

 int j = 0;

 while (k > 0) {

 

 for (int i = 0; i < arr.length; i++) {

 b[j++] = arr[i];

 }

 k--;

 }

 }

 

 // Function to return the maximum 

 // subarray sum of arr[]

 static int maxSubArrSum(int a[])

 {

 int size = a.length;

 int max_so_far = Integer.MIN_VALUE,

 max_ending_here = 0;

 

 for (int i = 0; i < size; i++) {

 max_ending_here = max_ending_here + a[i];

 if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 if (max_ending_here < 0)

 max_ending_here = 0;

 }

 return max_so_far;

 }

 

 // Function to return the maximum sub-array 

 // sum of the modified array

 static long maxSubKSum(int arr[], int k)

 {

 int arrSum = 0;

 long maxSubArrSum = 0;

 

 int b[] = new int[(2 * arr.length)];

 

 // Concatenating the array 2 times

 arrayConcatenate(arr, b, 2);

 

 // Finding the sum of the array

 for (int i = 0; i < arr.length; i++)

 arrSum += arr[i];

 

 // If sum is less than zero

 if (arrSum < 0)

 maxSubArrSum = maxSubArrSum(b);

 

 // If sum is greater than zero

 else

 maxSubArrSum = maxSubArrSum(b) +

 (k - 2) * arrSum;

 

 return maxSubArrSum;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int arr[] = { 1, -2, 1 };

 int k = 5;

 System.out.println(maxSubKSum(arr, k));

 }

}  
  
---  
  
 __

 __

Below is the implementation of the above approach:  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python approach to this problem

 

# A python module where element 

# are added to list k times

def MaxsumArrKtimes(c, ktimes):

 

 # Store element in list d k times

 d = c * ktimes

 

 # two variable which can keep 

 # track of maximum sum seen

 # so far and maximum sum ended.

 maxsofar = -99999

 maxending = 0

 

 for i in d:

 maxending = maxending + i

 if maxsofar < maxending:

 maxsofar = maxending

 if maxending < 0:

 maxending = 0

 return maxsofar

 

# Get the Maximum sum of element

print(MaxsumArrKtimes([1, -2, 1], 5))

 

# This code is contributed by AnupGaurav.

   
  
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

 

// Function to concatenate array 

static void arrayConcatenate(int []arr, 

 int []b, int k) 

{ 

 // Array b will be formed by concatenation 

 // array a exactly k times 

 int j = 0; 

 while (k > 0)

 { 

 for (int i = 0; i < arr.Length; i++) 

 { 

 b[j++] = arr[i]; 

 } 

 k--; 

 } 

} 

 

// Function to return the maximum 

// subarray sum of arr[] 

static int maxSubArrSum(int []a) 

{ 

 int size = a.Length; 

 int max_so_far = int.MinValue, 

 max_ending_here = 0; 

 

 for (int i = 0; i < size; i++) 

 { 

 max_ending_here = max_ending_here + a[i]; 

 if (max_so_far < max_ending_here) 

 max_so_far = max_ending_here; 

 if (max_ending_here < 0) 

 max_ending_here = 0; 

 } 

 return max_so_far; 

} 

 

// Function to return the maximum sub-array 

// sum of the modified array 

static long maxSubKSum(int []arr, int k) 

{ 

 int arrSum = 0; 

 long maxSubArrsum = 0; 

 

 int []b = new int[(2 * arr.Length)]; 

 

 // Concatenating the array 2 times 

 arrayConcatenate(arr, b, 2); 

 

 // Finding the sum of the array 

 for (int i = 0; i < arr.Length; i++) 

 arrSum += arr[i]; 

 

 // If sum is less than zero 

 if (arrSum < 0) 

 maxSubArrsum = maxSubArrSum(b); 

 

 // If sum is greater than zero 

 else

 maxSubArrsum = maxSubArrSum(b) + 

 (k - 2) * arrSum; 

 

 return maxSubArrsum; 

} 

 

// Driver code 

public static void Main() 

{ 

 int []arr = { 1, -2, 1 }; 

 int k = 5; 

 Console.WriteLine(maxSubKSum(arr, k)); 

} 

} 

 

// This code is contributed by Ryuga  
  
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

 

// Function to concatenate array

function arrayConcatenate(&$arr, &$b, $k)

{

 // Array b will be formed by concatenation

 // array a exactly k times

 $j = 0;

 while ($k > 0) 

 {

 

 for ($i = 0; $i < sizeof($arr); $i++) 

 {

 $b[$j++] = $arr[$i];

 }

 $k--;

 }

}

 

// Function to return the maximum 

// subarray sum of arr[]

function maxSubArrSum(&$a)

{

 $size = sizeof($a);

 $max_so_far = 0;

 $max_ending_here = 0;

 

 for ($i = 0; $i < $size; $i++) 

 {

 $max_ending_here = $max_ending_here + $a[$i];

 if ($max_so_far < $max_ending_here)

 $max_so_far = $max_ending_here;

 if ($max_ending_here < 0)

 $max_ending_here = 0;

 }

 return $max_so_far;

}

 

// Function to return the maximum sub-array 

// sum of the modified array

function maxSubKSum(&$arr,$k)

{

 $arrSum = 0;

 $maxSubArrSum = 0;

 

 $b = array_fill(0,(2 * sizeof($arr)),NULL);

 

 // Concatenating the array 2 times

 arrayConcatenate($arr, $b, 2);

 

 // Finding the sum of the array

 for ($i = 0; $i < sizeof($arr); $i++)

 $arrSum += $arr[$i];

 

 // If sum is less than zero

 if ($arrSum < 0)

 $maxSubArrSum = maxSubArrSum($b);

 

 // If sum is greater than zero

 else

 $maxSubArrSum = maxSubArrSum($b) +

 ($k - 2) * $arrSum;

 

 return $maxSubArrSum;

}

 

 // Driver code

 $arr = array(1, -2, 1 );

 $k = 5;

 echo maxSubKSum($arr, $k);

 

// This code is contributed by Ita_c. 

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

