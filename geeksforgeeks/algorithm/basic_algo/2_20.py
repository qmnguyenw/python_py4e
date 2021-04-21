Count number of pairs (i, j) such that arr[i] * arr[j] > arr[i] + arr[j]



Given an array **arr[]** of non-negative integers, the task is to count pairs
of indices **(i, j** such that **arr[i] * arr[j] > arr[i] + arr[j]** where **i
< j**.

 **Examples:**

>  **Input:** arr[] = { 5, 0, 3, 1, 2 }  
>  **Output:** 3
>
>  **Input:** arr[] = { 1, 1, 1 }  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** Run two nested loops and check for every pair whether the
condition is satisfied. If the condition is satisfied for any pair then update
**count = count + 1** and print the **count** in the end.

  

  

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count pairs (i, j)

// such that arr[i] * arr[j] > arr[i] + arr[j]

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the count of pairs

// such that arr[i] * arr[j] > arr[i] + arr[j]

long countPairs(int arr[], int n)

{

 long count = 0;

 for (int i = 0; i < n - 1; i++) {

 for (int j = i + 1; j < n; j++) {

 

 // If condition is satisfied

 if (arr[i] * arr[j] > arr[i] + arr[j])

 count++;

 }

 }

 return count;

}

 

// Driver code

int main()

{

 int arr[] = { 5, 0, 3, 1, 2 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << countPairs(arr, n);

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

// Java program to count pairs (i, j)

// such that arr[i] * arr[j] > arr[i] + arr[j]

import java.util.*;

 

class solution

{

 

// Function to return the count of pairs

// such that arr[i] * arr[j] > arr[i] + arr[j]

static long countPairs(int arr[], int n)

{

 long count = 0;

 for (int i = 0; i < n - 1; i++) {

 for (int j = i + 1; j < n; j++) {

 

 // If condition is satisfied

 if (arr[i] * arr[j] > arr[i] + arr[j])

 count++;

 }

 }

 return count;

}

 

// Driver code

public static void main(String args[])

{

 int arr[] = { 5, 0, 3, 1, 2 };

 int n = arr.length;

 System.out.println(countPairs(arr, n));

 

}

}

 

// This code is contributed by

// Surendra_Gangwar  
  
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

# Python3 program to count pairs(i,j)

# such that arr[i]*arr[j]>arr[i]+arr[j]

import math as mt

 

# function to return the count of pairs 

# such that arr[i]*arr[j]>arr[i]+arr[j]

def countPairs(arr, n):

 count = 0

 

 for i in range(n):

 for j in range(i + 1, n):

 

 # if condition is satisified

 if arr[i] * arr[j] > arr[i] + arr[j]:

 count += 1

 

 return count

 

# Driver code

arr = [5, 0, 3, 1, 2]

n = len(arr)

 

print(countPairs(arr, n))

 

# This code is contributed 

# by Mohit Kumar 29  
  
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

// C# program to count pairs (i, j)

// such that arr[i] * arr[j] > arr[i] + arr[j]

 

using System;

 

public class GFG{

 

// Function to return the count of pairs

// such that arr[i] * arr[j] > arr[i] + arr[j]

static long countPairs(int []arr, int n)

{

 long count = 0;

 for (int i = 0; i < n - 1; i++) {

 for (int j = i + 1; j < n; j++) {

 

 // If condition is satisfied

 if (arr[i] * arr[j] > arr[i] + arr[j])

 count++;

 }

 }

 return count;

}

 

// Driver code

 static public void Main (){

 int []arr = { 5, 0, 3, 1, 2 };

 int n = arr.Length;

 Console.WriteLine (countPairs(arr, n));

 }

}  
  
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

// PHP program to count pairs (i, j) 

// such that arr[i] * arr[j] > arr[i] + arr[j] 

 

// Function to return the count of pairs 

// such that arr[i] * arr[j] > arr[i] + arr[j] 

function countPairs($arr, $n) 

{ 

 $count = 0; 

 for ($i = 0; $i < $n - 1; $i++) 

 { 

 for ($j = $i + 1; $j < $n; $j++) 

 { 

 

 // If condition is satisfied 

 if ($arr[$i] * 

 $arr[$j] > $arr[$i] + 

 $arr[$j]) 

 $count++; 

 } 

 } 

 return $count; 

} 

 

// Driver code 

$arr = array( 5, 0, 3, 1, 2 ); 

$n = sizeof($arr) ;

 

echo countPairs($arr, $n);

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Efficient Approach:** Consider the following cases:

>  **1) arr[i] = 0 or arr[i] = 1 and arr[j] = any element**  
>  In this case, arr[j] * arr[i] will always be less than arr[i] + arr[j].  
> Hence we can discard all pairs which have one element either 0 or 1.
>
>  **2) arr[i] = 2 and arr[j] <= 2**  
> In this case, arr[j] * arr[i] will always be less than or equal to arr[i] +
> arr[j].  
> Hence again we can discard all such pairs.
>
>  **3) arr[i] = 2 and arr[j] > 2**  
> This case will produce valid pairs. If count_2 is the count of ‘2’s and
> count_others  
> is the count of elements greater than 2,  
> then number of pairs will be _count_2 * count_others_.
>
>  **4) arr[i] > 2 and arr[j] > 2**  
> This case will also produce valid pairs. Let count_others be the number of
> elements  
> greater than 2, then every two elements among these _count_others_ elements  
> will form a valid pair. Hence the number of pairs will be  
> ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/formula-1.png)
>
> Therefore, **total count = (count_2 * count_others) + (count_others *
> (count_others – 1)) / 2**.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count pairs (i, j)

// such that arr[i] * arr[j] > arr[i] + arr[j]

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the count of pairs

// such that arr[i] * arr[j] > arr[i] + arr[j]

long countPairs(const int* arr, int n)

{

 int count_2 = 0, count_others = 0;

 for (int i = 0; i < n; i++) {

 if (arr[i] == 2)

 count_2++;

 else if (arr[i] > 2)

 count_others++;

 }

 long ans

 = 1L * count_2 * count_others

 + (1L * count_others * (count_others - 1)) / 2;

 return ans;

}

 

// Driver code

int main()

{

 int arr[] = { 5, 0, 3, 1, 2 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << countPairs(arr, n);

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

// Java program to count pairs (i, j)

// such that arr[i] * arr[j] > arr[i] + arr[j] 

 

class GFG 

{

 // Function to return the count of pairs 

 // such that arr[i] * arr[j] > arr[i] + arr[j] 

 static long countPairs(int[] arr, int n) 

 {

 int count_2 = 0, count_others = 0;

 for (int i = 0; i < n; i++) 

 {

 if (arr[i] == 2) 

 {

 count_2++;

 } 

 else if (arr[i] > 2) 

 {

 count_others++;

 }

 }

 

 long ans = 1L * count_2 * count_others +

 (1L * count_others * (count_others - 1)) / 2;

 return ans;

 }

 

 // Driver code 

 public static void main(String[] args) 

 {

 int arr[] = {5, 0, 3, 1, 2};

 int n = arr.length;

 System.out.println(countPairs(arr, n));

 }

}

 

// This code is contributed by 

// 29AjayKumar   
  
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

# Python3 program to count pairs(i,j)

# such that arr[i]*arr[j]>arr[i]+arr[j]

import math as mt

 

# function to return the count of pairs 

# such that arr[i]*arr[j]>arr[i]+arr[j]

def countPairs(arr, n):

 count_2, count_others = 0, 0

 

 for i in range(n):

 if arr[i] == 2:

 count_2 += 1

 elif arr[i] > 2:

 count_others += 1

 ans = (count_2 * count_others +

 (count_others *

 (count_others - 1)) // 2)

 return ans

 

# Driver code

arr = [5, 0, 3, 1, 2]

n = len(arr)

 

print(countPairs(arr, n))

 

# This code is contributed 

# by Mohit Kumar  
  
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

// C# program to count pairs (i, j) such

// that arr[i] * arr[j] > arr[i] + arr[j] 

using System;

 

class GFG 

{

 // Function to return the count of pairs 

 // such that arr[i] * arr[j] > arr[i] + arr[j] 

 static long countPairs(int[] arr, int n) 

 {

 int count_2 = 0, count_others = 0;

 for (int i = 0; i < n; i++) 

 {

 if (arr[i] == 2) 

 {

 count_2++;

 } 

 else if (arr[i] > 2) 

 {

 count_others++;

 }

 }

 

 long ans = 1L * count_2 * count_others +

 (1L * count_others * 

 (count_others - 1)) / 2;

 return ans;

 }

 

 // Driver code 

 public static void Main() 

 {

 int[] arr = {5, 0, 3, 1, 2};

 int n = arr.Length;

 Console.WriteLine(countPairs(arr, n));

 }

}

 

// This code is contributed by 

// Mukul Singh  
  
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

// PHP program to count pairs (i, j) such

// that arr[i] * arr[j] > arr[i] + arr[j]

 

// Function to return the count of pairs

// such that arr[i] * arr[j] > arr[i] + arr[j]

function countPairs($arr, $n)

{

 $count_2 = 0; $count_others = 0;

 for ($i = 0; $i < $n; $i++) 

 {

 if ($arr[$i] == 2)

 $count_2++;

 else if ($arr[$i] > 2)

 $count_others++;

 }

 $ans = $count_2 * $count_others + 

 ($count_others * 

 ($count_others - 1)) / 2;

 return $ans;

}

 

// Driver code

$arr = array( 5, 0, 3, 1, 2 );

$n = sizeof($arr);

echo countPairs($arr, $n);

 

// This code is contributed

// by Akanksha Rai

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

