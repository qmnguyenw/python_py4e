Split the array into equal sum parts according to given conditions



Given an integer array **arr[]** , the task is to check if the input array can
be split in two sub-arrays such that:

  * Sum of both the sub-arrays is equal.
  * All the elements which are divisible by 5 should be in the same group.
  * All the elements which are divisible by 3 (but not divisible by 5) should be in the other group.
  * Elements which are neither divisible by 5 nor by 3 can be put in any group.

If possible then print **Yes** else print **No**.

 **Examples:**

>  **Input:** arr[] = {1, 2}  
>  **Output:** No  
> The elements cannot be divided in groups such that there sum is equal.
>
>  **Input:** arr[] = {1, 4, 3}  
>  **Output:** Yes  
> {1, 3} and {4} are the groups satisfying the given condition.
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** We can use a recursive approach by keeping left sum and right
sum to maintain two different groups. **Left sum** is for **multiples of 5**
and **right sum** is for **multiples of 3** (which are not multiples of 5) and
the elements which are **neither divisible by 5 nor by 3** can lie in any
group satisfying the equal sum rule (include them in left sum and right sum
one by one).

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

 

// Recursive function that returns true if the array

// can be divided into two sub-arrays

// satisfying the given condition

bool helper(int* arr, int n, int start, int lsum, int
rsum)

{

 

 // If reached the end

 if (start == n)

 return lsum == rsum;

 

 // If divisible by 5 then add to the left sum

 if (arr[start] % 5 == 0)

 lsum += arr[start];

 

 // If divisible by 3 but not by 5

 // then add to the right sum

 else if (arr[start] % 3 == 0)

 rsum += arr[start];

 

 // Else it can be added to any of the sub-arrays

 else

 

 // Try adding in both the sub-arrays (one by one)

 // and check whether the condition satisfies

 return helper(arr, n, start + 1, lsum + arr[start], rsum)

 || helper(arr, n, start + 1, lsum, rsum + arr[start]);

 

 // For cases when element is multiple of 3 or 5.

 return helper(arr, n, start + 1, lsum, rsum);

}

 

// Function to start the recursive calls

bool splitArray(int* arr, int n)

{

 // Initially start, lsum and rsum will all be 0

 return helper(arr, n, 0, 0, 0);

}

 

// Driver code

int main()

{

 int arr[] = { 1, 4, 3 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 if (splitArray(arr, n))

 cout << "Yes";

 else

 cout << "No";

 

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

class Solution

{

 

// Recursive function that returns true if the array

// can be divided into two sub-arrays

// satisfying the given condition

static boolean helper(int arr[], int n,

 int start, int lsum, int rsum)

{

 

 // If reached the end

 if (start == n)

 return lsum == rsum;

 

 // If divisible by 5 then add to the left sum

 if (arr[start] % 5 == 0)

 lsum += arr[start];

 

 // If divisible by 3 but not by 5

 // then add to the right sum

 else if (arr[start] % 3 == 0)

 rsum += arr[start];

 

 // Else it can be added to any of the sub-arrays

 else

 

 // Try adding in both the sub-arrays (one by one)

 // and check whether the condition satisfies

 return helper(arr, n, start + 1, lsum + arr[start], rsum)

 || helper(arr, n, start + 1, lsum, rsum + arr[start]);

 

 // For cases when element is multiple of 3 or 5.

 return helper(arr, n, start + 1, lsum, rsum);

}

 

// Function to start the recursive calls

static boolean splitArray(int arr[], int n)

{

 // Initially start, lsum and rsum will all be 0

 return helper(arr, n, 0, 0, 0);

}

 

// Driver code

public static void main(String args[])

{

 int arr[] = { 1, 4, 3 };

 int n = arr.length;

 

 if (splitArray(arr, n))

 System.out.println( "Yes");

 else

 System.out.println( "No");

}

}

 

// This code is contributed by Arnab Kundu  
  
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

 

# Recursive function that returns true if 

# the array can be divided into two sub-arrays

# satisfying the given condition

def helper(arr, n, start, lsum, rsum):

 

 # If reached the end

 if (start == n):

 return lsum == rsum

 

 # If divisible by 5 then add 

 # to the left sum

 if (arr[start] % 5 == 0):

 lsum += arr[start]

 

 # If divisible by 3 but not by 5

 # then add to the right sum

 elif (arr[start] % 3 == 0):

 rsum += arr[start]

 

 # Else it can be added to any of

 # the sub-arrays

 else:

 

 # Try adding in both the sub-arrays 

 # (one by one) and check whether

 # the condition satisfies

 return (helper(arr, n, start + 1, 

 lsum + arr[start], rsum) or

 helper(arr, n, start + 1, 

 lsum, rsum + arr[start]));

 

 # For cases when element is multiple of 3 or 5.

 return helper(arr, n, start + 1, lsum, rsum)

 

# Function to start the recursive calls

def splitArray(arr, n):

 

 # Initially start, lsum and rsum 

 # will all be 0

 return helper(arr, n, 0, 0, 0)

 

# Driver code

if __name__ == "__main__":

 

 arr = [ 1, 4, 3 ]

 n = len(arr)

 

 if (splitArray(arr, n)):

 print("Yes")

 else:

 print("No")

 

# This code is contributed by ita_c  
  
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

 

 // Recursive function that returns true if the array 

 // can be divided into two sub-arrays 

 // satisfying the given condition 

 static bool helper(int []arr, int n, 

 int start, int lsum, int rsum) 

 { 

 

 // If reached the end 

 if (start == n) 

 return lsum == rsum; 

 

 // If divisible by 5 then add to the left sum 

 if (arr[start] % 5 == 0) 

 lsum += arr[start]; 

 

 // If divisible by 3 but not by 5 

 // then add to the right sum 

 else if (arr[start] % 3 == 0) 

 rsum += arr[start]; 

 

 // Else it can be added to any of the sub-arrays 

 else

 

 // Try adding in both the sub-arrays (one by one) 

 // and check whether the condition satisfies 

 return helper(arr, n, start + 1, lsum + arr[start], rsum) 

 || helper(arr, n, start + 1, lsum, rsum + arr[start]); 

 

 // For cases when element is multiple of 3 or 5. 

 return helper(arr, n, start + 1, lsum, rsum); 

 } 

 

 // Function to start the recursive calls 

 static bool splitArray(int []arr, int n) 

 { 

 // Initially start, lsum and rsum will all be 0 

 return helper(arr, n, 0, 0, 0); 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 int []arr = { 1, 4, 3 }; 

 int n = arr.Length; 

 

 if (splitArray(arr, n)) 

 Console.WriteLine( "Yes"); 

 else

 Console.WriteLine( "No"); 

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

 

// Recursive function that returns true 

// if the array can be divided into two

// sub-arrays satisfying the given condition

function helper(&$arr, $n, $start, 

 $lsum, $rsum)

{

 

 // If reached the end

 if ($start == $n)

 return $lsum == $rsum;

 

 // If divisible by 5 then 

 // add to the left sum

 if ($arr[$start] % 5 == 0)

 $lsum += $arr[$start];

 

 // If divisible by 3 but not by 5

 // then add to the right sum

 else if ($arr[$start] % 3 == 0)

 $rsum += $arr[$start];

 

 // Else it can be added to any 

 // of the sub-arrays

 else

 

 // Try adding in both the sub-arrays (one by one)

 // and check whether the condition satisfies

 return helper($arr, $n, $start + 1, 

 $lsum + $arr[$start], $rsum) || 

 helper($arr, $n, $start + 1, 

 $lsum, $rsum + $arr[$start]);

 

 // For cases when element is 

 // multiple of 3 or 5.

 return helper($arr, $n, $start + 1,

 $lsum, $rsum);

}

 

// Function to start the recursive calls

function splitArray($arr, $n)

{

 // Initially start, lsum and r

 // sum will all be 0

 return helper($arr, $n, 0, 0, 0);

}

 

// Driver code

$arr = array( 1, 4, 3 );

$n = count($arr);

 

if (splitArray($arr, $n))

 print("Yes");

else

 print("No");

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

