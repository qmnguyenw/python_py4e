Maximum value of arr[i] % arr[j] for a given array



Given an array **arr[]** , the task is to find the maximum value of **arr[i] %
arr[j]** for all possible pairs.

 **Examples:**

>  **Input:** arr[] = { 2, 3 }  
>  **Output:** 2  
> 2 % 3 = 2  
> 3 % 2 = 1
>
>  **Input:** arr[] = { 2, 2, 2, 2 }  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** Run two nested loops and calculate the value of **arr[i]
% arr[j]** for every pair. Update the answer according to the value
calculated.

  

  

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

 

// Function to return maximum value of

// arr[i] % arr[j]

int computeMaxValue(const int* arr, int n)

{

 int ans = 0;

 for (int i = 0; i < n - 1; i++) {

 for (int j = i + 1; j < n; j++) {

 

 // Check pair (x, y) as well as 

 // (y, x) for maximum value

 int val = max(arr[i] % arr[j], 

 arr[j] % arr[i]);

 

 // Update the answer

 ans = max(ans, val);

 }

 }

 return ans;

}

 

// Driver code

int main()

{

 int arr[] = { 2, 3 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << computeMaxValue(arr, n);

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

 

import java.util.*;

class GFG

{

 

 // Function to return maximum value of

 // arr[i] % arr[j]

 static int computeMaxValue(int []arr, int n)

 {

 int ans = 0;

 for (int i = 0; i < n - 1; i++) {

 for (int j = i + 1; j < n; j++) {

 

 // Check pair (x, y) as well as 

 // (y, x) for maximum value

 int val = Math.max(arr[i] % arr[j], 

 arr[j] % arr[i]);

 

 // Update the answer

 ans = Math.max(ans, val);

 }

 }

 return ans;

 }

 

 // Driver code

 public static void main(String []args)

 {

 int []arr = { 2, 3 };

 int n = arr.length;

 System.out.println(computeMaxValue(arr, n));

 

 }

 

}

 

// This code is contributed

// by ihritik  
  
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

 

# Function to return maximum value of

# arr[i] % arr[j]

def computeMaxValue(arr, n):

 

 ans = 0

 for i in range(0, n-1):

 for j in range( i+1, n):

 

 # Check pair (x, y) as well as 

 # (y, x) for maximum value

 val = max(arr[i] % arr[j], arr[j] % arr[i])

 

 # Update the answer

 ans = max(ans, val)

 

 

 return ans

 

 

# Driver code

arr = [ 2, 3 ]

n = len(arr)

print(computeMaxValue(arr, n))

 

# This code is contributed

# by ihritik  
  
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

class GFG

{

 

 // Function to return maximum value of

 // arr[i] % arr[j]

 static int computeMaxValue(int []arr, int n)

 {

 int ans = 0;

 for (int i = 0; i < n - 1; i++) {

 for (int j = i + 1; j < n; j++) {

 

 // Check pair (x, y) as well as 

 // (y, x) for maximum value

 int val = Math.Max(arr[i] % arr[j], 

 arr[j] % arr[i]);

 

 // Update the answer

 ans = Math.Max(ans, val);

 }

 }

 return ans;

 }

 

 // Driver code

 public static void Main()

 {

 int []arr = { 2, 3 };

 int n = arr.Length;

 Console.WriteLine(computeMaxValue(arr, n));

 

 }

 

}

 

// This code is contributed

// by ihritik  
  
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

 

// Function to return maximum value of

// arr[i] % arr[j]

function computeMaxValue($arr, $n)

{

 $ans = 0;

 for ($i = 0; $i < $n - 1; $i++) {

 for ($j = $i + 1; $j < $n; $j++) {

 

 // Check pair (x, y) as well as 

 // (y, x) for maximum value

 $val = max($arr[$i] % $arr[$j], 

 $arr[$j] % $arr[$i]);

 

 // Update the answer

 $ans = max($ans, $val);

 }

 }

 return $ans;

}

 

// Driver code

$arr = array( 2, 3 );

$n = sizeof($arr);

echo computeMaxValue($arr, $n);

 

// This code is contributed

// by ihritik

 

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

**Efficient Approach:** The maximum value of **A % B** will be yielded when
**A < B** and **A and B are maximum possible**. In other words, the result
will be the second greatest element from the array except for the case when
all the elements of the array are same (in that case, the result will be **0**
).

> A = second largest element of the array.  
> B = largest element of the array and A < B.  
> Maximum value of A % B = A.
>
>  **Corner case:** If all the elements of the array are same say **arr[] =
> {x, x, x, x}** then the result will be x % x = **0**.

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

 

// Function to return maximum value of

// arr[i] % arr[j]

int computeMaxValue(const int* arr, int n)

{

 bool allSame = true;

 int i = 1;

 while (i < n) {

 

 // If current element is different

 // from the previous element

 if (arr[i] != arr[i - 1]) {

 allSame = false;

 break;

 }

 i++;

 }

 

 // If all the elements of the array are equal

 if (allSame)

 return 0;

 

 // Maximum element from the array

 int max = *std::max_element(arr, arr + n);

 int secondMax = 0;

 for (i = 0; i < n; i++) {

 if (arr[i] < max && arr[i] > secondMax)

 secondMax = arr[i];

 }

 

 // Return the second maximum element

 // from the array

 return secondMax;

}

 

// Driver code

int main()

{

 int arr[] = { 2, 3 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << computeMaxValue(arr, n);

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

class GFG

{

 

// Function to return maximum value of

// arr[i] % arr[j]

static int computeMaxValue(int arr[], int n)

{

 boolean allSame = true;

 int i = 1;

 while (i < n) 

 {

 

 // If current element is different

 // from the previous element

 if (arr[i] != arr[i - 1]) 

 {

 allSame = false;

 break;

 }

 i++;

 }

 

 // If all the elements of the 

 // array are equal

 if (allSame)

 return 0;

 

 // Maximum element from the array

 int max = -1;

 for(i = 0; i < n; i++)

 {

 if(max < arr[i])

 max = arr[i];

 }

 int secondMax = 0;

 for (i = 0; i < n; i++)

 {

 if (arr[i] < max && arr[i] > secondMax)

 secondMax = arr[i];

 }

 

 // Return the second maximum element

 // from the array

 return secondMax;

}

 

// Driver code

public static void main(String[] args)

{

 int []arr = { 2, 3 };

 int n = arr.length;

 System.out.println(computeMaxValue(arr, n));

}

}

 

// This code is contributed

// by 29AjayKumar  
  
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

# Python3 implementation of the

# above approach 

 

# Function to return maximum value 

# of arr[i] % arr[j] 

def computeMaxValue(arr, n) :

 

 allSame = True; 

 i = 1; 

 while (i < n) : 

 

 # If current element is different 

 # from the previous element 

 if (arr[i] != arr[i - 1]) :

 allSame = False

 break

 

 i += 1

 

 # If all the elements of the 

 # array are equal 

 if (allSame) :

 return 0

 

 # Maximum element from the array 

 max_element = max(arr) 

 

 secondMax = 0

 for i in range(n) :

 if (arr[i] < max_element and

 arr[i] > secondMax) :

 secondMax = arr[i] 

 

 # Return the second maximum element 

 # from the array 

 return secondMax

 

# Driver code 

if __name__ == "__main__" :

 arr = [ 2, 3 ] 

 n = len(arr)

 

 print(computeMaxValue(arr, n))

 

# This code is contributed by Ryuga  
  
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

 

class GFG

{

 

// Function to return maximum value of

// arr[i] % arr[j]

static int computeMaxValue(int[] arr, int n)

{

 bool allSame = true;

 int i = 1;

 while (i < n) 

 {

 

 // If current element is different

 // from the previous element

 if (arr[i] != arr[i - 1]) 

 {

 allSame = false;

 break;

 }

 i++;

 }

 

 // If all the elements of the 

 // array are equal

 if (allSame)

 return 0;

 

 // Maximum element from the array

 int max = -1;

 for(i = 0; i < n; i++)

 {

 if(max < arr[i])

 max = arr[i];

 }

 int secondMax = 0;

 for (i = 0; i < n; i++)

 {

 if (arr[i] < max && arr[i] > secondMax)

 secondMax = arr[i];

 }

 

 // Return the second maximum element

 // from the array

 return secondMax;

}

 

// Driver code

public static void Main()

{

 int[] arr = { 2, 3 };

 int n = arr.Length;

 Console.Write(computeMaxValue(arr, n));

}

}

 

// This code is contributed by Ita_c.  
  
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

 

// Function to return maximum value of

// arr[i] % arr[j]

function computeMaxValue($arr, $n)

{

 $allSame = true;

 $i = 1;

 while ($i < $n) 

 {

 

 // If current element is different

 // from the previous element

 if ($arr[$i] != $arr[$i - 1]) 

 {

 $allSame = false;

 break;

 }

 $i++;

 }

 

 // If all the elements of the 

 // array are equal

 if ($allSame)

 return 0;

 

 // Maximum element from the array

 $max = max($arr);

 $secondMax = 0;

 for ($i = 0; $i < $n; $i++) 

 {

 if ($arr[$i] < $max && 

 $arr[$i] > $secondMax)

 $secondMax = $arr[$i];

 }

 

 // Return the second maximum 

 // element from the array

 return $secondMax;

}

 

// Driver code

$arr = array(2, 3);

$n = sizeof($arr);

echo computeMaxValue($arr, $n);

 

// This code is contributed by ajit.

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

