Sum of bitwise AND of all subarrays



Given an array consisting of N positive integers, find the sum of bit-wise and
of all possible sub-arrays of the array.

 **Examples:**

    
    
    **Input :** arr[] = {1, 5, 8}
    **Output :** 15
    Bit-wise AND of {1} = 1
    Bit-wise AND of {1, 5} = 1
    Bit-wise AND of {1, 5, 8} = 0 
    Bit-wise AND of {5} = 5
    Bit-wise AND of {5, 8} = 0
    Bit-wise AND of {8} = 8
    
    Sum = 1 + 1 + 0 + 5 + 0 + 8 =  15
    
    **Input :** arr[] =  {7, 1, 1, 5}
    **Output :** 20
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Simple Solution** : A simple solution will be to generate all the sub-
arrays, and sum up the AND values of all the sub-arrays. It will take linear
time on an average to find the AND value of a sub-array and thus, the over all
time complexity will be O(n3).

 **Efficient Solution:** For the sake of better understanding, let’s assume
that any bit of an element is represented by the variable ‘i’ and the variable
‘sum’ is used to store the final sum.

The idea here is, we will try to find the number of AND values(sub-arrays with
bit-wise and(&)) with ith bit set. Let us suppose, there are ‘Si‘ number of
sub-arrays with ith bit set. For, ith bit, sum can be updated as sum += (2i *
S).

  

  

We will break the task to multiple steps. At each step, we will try to find
the number of AND values with ith bit set. For this, we will simply iterate
through the array and find the number of contiguous segments with ith bit set
and there lengths. For, each such segment of length ‘l’, value of sum can be
updated as sum += (2i * l * (l + 1))/2.

Since, for each bit, we are performing O(N) iterations and as there are at
most log(max(A)) bits, the time complexity of this approach will be
O(N*log(max(A)), assuming max(A) = maximum value in the array.

Below is the implementation of the above idea:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to find sum of bitwise AND

// of all subarrays

 

#include <iostream>

#include <vector>

using namespace std;

 

// Function to find the sum of

// bitwise AND of all subarrays

int findAndSum(int arr[], int n)

{

 // variable to store

 // the final sum

 int sum = 0;

 

 // multiplier

 int mul = 1;

 

 for (int i = 0; i < 30; i++) {

 // variable to check if

 // counting is on

 bool count_on = 0;

 

 // variable to store the

 // length of the subarrays

 int l = 0;

 

 // loop to find the contiguous

 // segments

 for (int j = 0; j < n; j++) {

 if ((arr[j] & (1 << i)) > 0)

 if (count_on)

 l++;

 else {

 count_on = 1;

 l++;

 }

 

 else if (count_on) {

 sum += ((mul * l * (l + 1)) / 2);

 count_on = 0;

 l = 0;

 }

 }

 

 if (count_on) {

 sum += ((mul * l * (l + 1)) / 2);

 count_on = 0;

 l = 0;

 }

 

 // updating the multiplier

 mul *= 2;

 }

 

 // returning the sum

 return sum;

}

 

// Driver Code

int main()

{

 

 int arr[] = { 7, 1, 1, 5 };

 

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << findAndSum(arr, n);

 

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

// Java program to find sum of bitwise AND

// of all subarrays

class GFG

{

 

// Function to find the sum of

// bitwise AND of all subarrays

static int findAndSum(int []arr, int n)

{

 // variable to store

 // the final sum

 int sum = 0;

 

 // multiplier

 int mul = 1;

 

 for (int i = 0; i < 30; i++) 

 {

 // variable to check if

 // counting is on

 boolean count_on = false;

 

 // variable to store the

 // length of the subarrays

 int l = 0;

 

 // loop to find the contiguous

 // segments

 for (int j = 0; j < n; j++) 

 {

 if ((arr[j] & (1 << i)) > 0)

 if (count_on)

 l++;

 else

 {

 count_on = true;

 l++;

 }

 

 else if (count_on)

 {

 sum += ((mul * l * (l + 1)) / 2);

 count_on = false;

 l = 0;

 }

 }

 

 if (count_on) 

 {

 sum += ((mul * l * (l + 1)) / 2);

 count_on = false;

 l = 0;

 }

 

 // updating the multiplier

 mul *= 2;

 }

 

 // returning the sum

 return sum;

}

 

// Driver Code

public static void main(String[] args)

{

 int []arr = { 7, 1, 1, 5 };

 int n = arr.length;

 

 System.out.println(findAndSum(arr, n));

}

}

 

// This code is contributed 

// by Code_Mech.  
  
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

# Python3 program to find Sum of

# bitwise AND of all subarrays

import math as mt

 

# Function to find the Sum of

# bitwise AND of all subarrays

def findAndSum(arr, n):

 

 # variable to store the final Sum

 Sum = 0

 

 # multiplier

 mul = 1

 

 for i in range(30):

 

 # variable to check if counting is on

 count_on = 0

 

 # variable to store the length

 # of the subarrays

 l = 0

 

 # loop to find the contiguous

 # segments

 for j in range(n):

 

 if ((arr[j] & (1 << i)) > 0):

 if (count_on):

 l += 1

 else:

 count_on = 1

 l += 1

 

 elif (count_on):

 Sum += ((mul * l * (l + 1)) // 2)

 count_on = 0

 l = 0

 

 if (count_on): 

 Sum += ((mul * l * (l + 1)) // 2)

 count_on = 0

 l = 0

 

 # updating the multiplier

 mul *= 2

 

 # returning the Sum

 return Sum

 

# Driver Code

arr = [7, 1, 1, 5]

 

n = len(arr)

 

print(findAndSum(arr, n))

 

# This code is contributed by Mohit Kumar  
  
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

// C# program to find sum of bitwise AND

// of all subarrays

using System;

 

class GFG

{

 

// Function to find the sum of

// bitwise AND of all subarrays

static int findAndSum(int []arr, int n)

{

 // variable to store

 // the final sum

 int sum = 0;

 

 // multiplier

 int mul = 1;

 

 for (int i = 0; i < 30; i++) 

 {

 // variable to check if

 // counting is on

 bool count_on = false;

 

 // variable to store the

 // length of the subarrays

 int l = 0;

 

 // loop to find the contiguous

 // segments

 for (int j = 0; j < n; j++) 

 {

 if ((arr[j] & (1 << i)) > 0)

 if (count_on)

 l++;

 else

 {

 count_on = true;

 l++;

 }

 

 else if (count_on)

 {

 sum += ((mul * l * (l + 1)) / 2);

 count_on = false;

 l = 0;

 }

 }

 

 if (count_on) 

 {

 sum += ((mul * l * (l + 1)) / 2);

 count_on = false;

 l = 0;

 }

 

 // updating the multiplier

 mul *= 2;

 }

 

 // returning the sum

 return sum;

}

 

// Driver Code

public static void Main()

{

 int []arr = { 7, 1, 1, 5 };

 int n = arr.Length;

 

 Console.Write(findAndSum(arr, n));

}

}

 

// This code is contributed 

// by Akanksha Rai  
  
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

// PHP program to find sum of bitwise 

// AND of all subarrays 

 

// Function to find the sum of 

// bitwise AND of all subarrays 

function findAndSum($arr, $n) 

{ 

 // variable to store the

 // final sum 

 $sum = 0; 

 

 // multiplier 

 $mul = 1; 

 

 for ($i = 0; $i < 30; $i++)

 { 

 

 // variable to check if 

 // counting is on 

 $count_on = 0; 

 

 // variable to store the 

 // length of the subarrays 

 $l = 0; 

 

 // loop to find the contiguous 

 // segments 

 for ($j = 0; $j < $n; $j++)

 { 

 if (($arr[$j] & (1 << $i)) > 0) 

 if ($count_on) 

 $l++; 

 else

 { 

 $count_on = 1; 

 $l++; 

 } 

 

 else if ($count_on) 

 { 

 $sum += (($mul * $l * ($l + 1)) / 2); 

 $count_on = 0; 

 $l = 0; 

 } 

 } 

 

 if ($count_on) 

 { 

 $sum += (($mul * $l * ($l + 1)) / 2); 

 $count_on = 0; 

 $l = 0; 

 } 

 

 // updating the multiplier 

 $mul *= 2; 

 } 

 

 // returning the sum 

 return $sum; 

} 

 

// Driver Code 

$arr = array( 7, 1, 1, 5 ); 

 

$n = sizeof($arr); 

 

echo findAndSum($arr, $n); 

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    20
    

**Time Complexity** : O(N*log(max(A))

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

