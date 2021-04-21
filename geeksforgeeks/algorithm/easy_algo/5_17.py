Rearrange Odd and Even values in Alternate Fashion in Ascending Order



Given an array of integers (both odd and even), the task is to arrange them in
such a way that odd and even values come in alternate fashion in non-
decreasing order(ascending) respectively.

  * If the smallest value is **Even** then we have to print **Even-Odd** pattern.
  * If the smallest value is **Odd** then we have to print **Odd-Even** pattern.

 **Note:** **No. of odd elements must be equal to No. of even elements in the
input array.**

 **Examples:**

>  **Input:** arr[] = {1, 3, 2, 5, 4, 7, 10}  
>  **Output:** 1, 2, 3, 4, 5, 10, 7  
> Smallest value is **1** (Odd) so output will be Odd-Even pattern.
>
>  **Input:** arr[] = {9, 8, 13, 2, 19, 14}  
>  **Output:** 2, 9, 8, 13, 14, 19  
> Smallest value is **2** (Even) so output will be Even-Odd pattern.
>
>  
>
>
>  
>

 **Asked In:** Microsoft Tech-Set-Go-2018

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Algorithm:**

  1. Sort the given array.
  2. Insert **Even** values in List-1 and **Odd** values in List-2.
  3. Now if the smallest value is even, then insert an even value from list 1 and odd value from list 2 to original array and so on.
  4. But if the smallest value is odd, then insert an odd value from list 2 and even value from list 1 to original array and so on.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

using namespace std;

 

void AlternateRearrange(int arr[], int n)

{

 // Sort the array

 sort(arr, arr + n);

 

 vector<int> v1; // to insert even values

 vector<int> v2; // to insert odd values

 

 for (int i = 0; i < n; i++)

 if (arr[i] % 2 == 0)

 v1.push_back(arr[i]);

 else

 v2.push_back(arr[i]);

 

 int index = 0, i = 0, j = 0;

 

 bool flag = false;

 

 // Set flag to true if first element is even

 if (arr[0] % 2 == 0)

 flag = true;

 

 // Start rearranging array

 while (index < n) {

 

 // If first element is even

 if (flag == true) {

 arr[index++] = v1[i++];

 flag = !flag;

 }

 

 // Else, first element is Odd

 else {

 arr[index++] = v2[j++];

 flag = !flag;

 }

 }

 

 // Print the rearranged array

 for (i = 0; i < n; i++)

 cout << arr[i] << " ";

}

 

// Driver code

int main()

{

 int arr[] = { 9, 8, 13, 2, 19, 14 };

 int n = sizeof(arr) / sizeof(int);

 AlternateRearrange(arr, n);

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

// Java implementation of the above approach

 

import java.util.* ;

 

class GFG

{

 

 static void AlternateRearrange(int arr[], int n) 

 { 

 // Sort the array

 

 // Collection.sort() sorts the

 // collection in ascending order

 Arrays.sort(arr) ;

 

 Vector v1 = new Vector(); // to insert even values 

 Vector v2 = new Vector(); // to insert odd values 

 

 for (int i = 0; i < n; i++) 

 if (arr[i] % 2 == 0) 

 v1.add(arr[i]); 

 else

 v2.add(arr[i]); 

 

 int index = 0, i = 0, j = 0; 

 

 boolean flag = false; 

 

 // Set flag to true if first element is even 

 if (arr[0] % 2 == 0) 

 flag = true; 

 

 // Start rearranging array 

 while (index < n) 

 { 

 

 // If first element is even 

 if (flag == true) 

 { 

 arr[index] = (int)v1.get(i); 

 i += 1 ;

 index += 1 ;

 flag = !flag; 

 } 

 

 // Else, first element is Odd 

 else

 { 

 arr[index] = (int)v2.get(j) ; 

 j += 1 ;

 index += 1 ;

 flag = !flag; 

 } 

 } 

 

 // Print the rearranged array 

 for (i = 0; i < n; i++) 

 System.out.print(arr[i] + " "); 

 } 

 

 // Driver code 

 public static void main(String []args) 

 { 

 int arr[] = { 9, 8, 13, 2, 19, 14 }; 

 int n = arr.length ;

 

 AlternateRearrange(arr, n); 

 } 

}

 

// This code is contributed by aishwarya.27  
  
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

# Python3 implementation of the above approach

 

def AlternateRearrange(arr, n):

 

 # Sort the array

 arr.sort()

 

 v1 = list() # to insert even values

 v2 = list() # to insert odd values

 

 for i in range(n):

 if (arr[i] % 2 == 0):

 v1.append(arr[i])

 else:

 v2.append(arr[i])

 

 index = 0

 i = 0

 j = 0

 

 flag = False

 

 # Set flag to true if first element is even

 if (arr[0] % 2 == 0):

 flag = True

 

 # Start rearranging array

 while (index < n): 

 

 # If first element is even

 if (flag == True):

 arr[index] = v1[i]

 index += 1

 i += 1

 flag = ~flag

 

 # Else, first element is Odd

 else:

 arr[index] = v2[j]

 index += 1

 j += 1

 

 flag = ~flag

 

 # Print the rearranged array

 for i in range(n):

 print(arr[i], end = " ")

 

# Driver code

arr = [ 9, 8, 13, 2, 19, 14] 

n = len(arr)

 

AlternateRearrange(arr, n)

 

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

// C# implementation of the above approach

 

using System;

using System.Collections;

class GFG

{

 

 static void AlternateRearrange(int []arr, int n) 

 { 

 // Sort the array

 

 // Collection.sort() sorts the

 // collection in ascending order

 Array.Sort(arr) ;

 

 ArrayList v1 = new ArrayList(); // to insert even values 

 ArrayList v2 = new ArrayList(); // to insert odd values 

 

 for (int j = 0; j < n; j++) 

 if (arr[j] % 2 == 0) 

 v1.Add(arr[j]); 

 else

 v2.Add(arr[j]); 

 

 int index = 0, i = 0, k = 0; 

 

 bool flag = false; 

 

 // Set flag to true if first element is even 

 if (arr[0] % 2 == 0) 

 flag = true; 

 

 // Start rearranging array 

 while (index < n) 

 { 

 

 // If first element is even 

 if (flag == true) 

 { 

 arr[index] = (int)v1[i]; 

 i += 1 ;

 index += 1 ;

 flag = !flag; 

 } 

 

 // Else, first element is Odd 

 else

 { 

 arr[index] = (int)v2[k] ; 

 k += 1 ;

 index += 1 ;

 flag = !flag; 

 } 

 } 

 

 // Print the rearranged array 

 for (i = 0; i < n; i++) 

 Console.Write(arr[i] + " "); 

 } 

 

 // Driver code 

 static void Main() 

 { 

 int []arr = { 9, 8, 13, 2, 19, 14 }; 

 int n = arr.Length ;

 

 AlternateRearrange(arr, n); 

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

// PHP implementation of the above approach 

function AlternateRearrange($arr, $n)

{

 

 // Sort the array

 sort($arr); 

 

 $v1 = array(); // to insert even values 

 $v2 = array(); // to insert odd values 

 

 for ($i = 0; $i < $n; $i++) 

 if ($arr[$i] % 2 == 0) 

 array_push($v1, $arr[$i]); 

 else

 array_push($v2, $arr[$i]); 

 

 $index = 0;

 $i = 0;

 $j = 0;

 

 $flag = false; 

 

 // Set flag to true if first element is even 

 if ($arr[0] % 2 == 0) 

 $flag = true; 

 

 // Start rearranging array 

 while ($index < $n) 

 { 

 

 // If first element is even 

 if ($flag == true) 

 { 

 $arr[$index++] = $v1[$i++]; 

 $flag = !$flag; 

 } 

 

 // Else, first element is Odd 

 else

 { 

 $arr[$index++] = $v2[$j++]; 

 $flag = !$flag; 

 } 

 } 

 

 // Print the rearranged array 

 for ($i = 0; $i < $n; $i++) 

 echo $arr[$i], " " ; 

} 

 

// Driver code 

$arr = array( 9, 8, 13, 2, 19, 14 );

$n = sizeof($arr);

 

AlternateRearrange($arr, $n); 

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    2 9 8 13 14 19
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

