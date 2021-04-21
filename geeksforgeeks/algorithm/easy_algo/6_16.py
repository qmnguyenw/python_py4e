Number of strictly increasing Buildings from right with distinct Colors



Given an integer ![K  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-1fa1ce8b3a40f8a06279f12b773c8172_l3.png)and two integer
arrays **H[]** and **C[]** of size ![K  ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-1fa1ce8b3a40f8a06279f12b773c8172_l3.png)where
**H[]** stores the height of consecutive buildings and **C[]** stores the
color codes for those building in which they are painted.  
The task is to determine how many colors are visible at once from the view on
the right i.e. right of the rightmost building.  
 **Examples:**  

> **Input:** K = 5, H[] = {5, 4, 3, 2, 3}, C[] = {1, 2, 3, 4, 5}  
> **Output:** 3  
>
>
> ![](https://media.geeksforgeeks.org/wp-content/uploads/3-192.png)
>
> **Input:** K = 5, H[] = {1, 2, 3, 4, 5}, C[] = {3, 3, 3, 3, 3}  
> **Output:** 1  
>

  

  

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** On observing carefully, the above problem can be simplified to
find the number of strictly increasing buildings from right with distinct
colors.  

  1. Store the Last element of Height array in _max_ variable.
  2. Now in an array _Arr_ , at position corresponding to the element at the last of the colour array store _1_.
  3. Now start traversing the Height array from _n-2 to 0_.
  4. If we get element greater than _max_ then store that variable in _max_ and again in array _Arr_ , at position correspond to the _ith_ element in the colour array store _1_.   

  5. At last Count the number of _1’s_ present in the array _Arr_. It gives the total number of colour visible from the end.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of above approach

#include <bits/stdc++.h>

using namespace std;

// Function to return the number of

// colors visible

int colourVisible(int height[], int colour[], int K)

{

 int arr[K + 1] = { 0 }, visible = 0;

 int max = height[K - 1];

 arr[colour[K - 1]] = 1;

 for (int i = K - 2; i >= 0; i--) {

 if (height[i] > max) {

 max = height[i];

 arr[colour[i]] = 1;

 }

 }

 // Count the Number of 1's

 for (int i = 1; i <= K; i++) {

 if (arr[i] == 1)

 visible++;

 }

 return visible;

}

// Driver code

int main()

{

 int height[] = { 3, 5, 1, 2, 3 };

 int colour[] = { 1, 2, 3, 4, 3 };

 int K = sizeof(colour) / sizeof(colour[0]);

 cout << colourVisible(height, colour, K);

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

//Java implementation of above approach

import java.io.*;

class GFG {

 // Function to return the number of

// colors visible

static int colourVisible(int height[], int colour[], int K)

{

 int arr[]=new int[K + 1] ;

 int visible = 0;

 int max = height[K - 1];

 arr[colour[K - 1]] = 1;

 for (int i = K - 2; i >= 0; i--) {

 if (height[i] > max) {

 max = height[i];

 arr[colour[i]] = 1;

 }

 }

 // Count the Number of 1's

 for (int i = 1; i <= K; i++) {

 if (arr[i] == 1)

 visible++;

 }

 return visible;

}

// Driver code

 

 public static void main (String[] args) {

 

 int height[] = { 3, 5, 1, 2, 3 };

 int colour[] = { 1, 2, 3, 4, 3 };

 int K = colour.length;

 System.out.println (colourVisible(height, colour, K));

 }

}  
  
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

# Python3 implementation of above approach

# Function to return the number of

# colors visible

def colourVisible(height, colour, K):

 arr = [0 for i in range(K + 1)]

 visible = 0

 max = height[K - 1]

 arr[colour[K - 1]] = 1

 

 i = K - 2

 while(i >= 0):

 if (height[i] > max):

 max = height[i]

 arr[colour[i]] = 1

 i -= 1

 

 # Count the Number of 1 complement

 for i in range(1, K + 1, 1):

 if (arr[i] == 1):

 visible += 1

 

 return visible

# Driver code

if __name__ == '__main__':

 height = [3, 5, 1, 2, 3]

 colour = [1, 2, 3, 4, 3]

 K = len(colour)

 print(colourVisible(height, colour, K))

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

// C# implementation of above approach

using System;

class GFG

{

// Function to return the number of

// colors visible

static int colourVisible(int []height,

 int []colour, int K)

{

 int []arr=new int[K + 1] ;

 int visible = 0;

 int max = height[K - 1];

 arr[colour[K - 1]] = 1;

 for (int i = K - 2; i >= 0; i--)

 {

 if (height[i] > max)

 {

 max = height[i];

 arr[colour[i]] = 1;

 }

 }

 // Count the Number of 1's

 for (int i = 1; i <= K; i++)

 {

 if (arr[i] == 1)

 visible++;

 }

 return visible;

}

// Driver code

static public void Main ()

{

 int []height = { 3, 5, 1, 2, 3 };

 int []colour = { 1, 2, 3, 4, 3 };

 int K = colour.Length;

 

 Console.WriteLine(colourVisible(height, colour, K));

}

}

// This code is contributed by Sach_Code  
  
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

// PHP implementation of above approach

// Function to return the number of

// colors visible

function colourVisible($height, $colour, $K)

{

 $arr = array_fill(0, $K + 1, 0);

 $visible = 0;

 $max = $height[$K - 1];

 $arr[$colour[$K - 1]] = 1;

 for ($i = $K - 2; $i >= 0; $i--)

 {

 if ($height[$i] > $max)

 {

 $max = $height[$i];

 $arr[$colour[$i]] = 1;

 }

 }

 // Count the Number of 1's

 for ($i = 1; $i <= $K; $i++)

 {

 if ($arr[$i] == 1)

 $visible++;

 }

 return $visible;

}

// Driver code

$height = array( 3, 5, 1, 2, 3 );

$colour = array( 1, 2, 3, 4, 3 );

$K = count($colour);

echo colourVisible($height, $colour, $K);

// This code is contributed by mits

?>  
  
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

// Javascript implementation of above approach

// Function to return the number of

// colors visible

function colourVisible(height, colour, K)

{

 var arr = Array(K+1).fill(0), visible = 0;

 var max = height[K - 1];

 arr[colour[K - 1]] = 1;

 for (var i = K - 2; i >= 0; i--) {

 if (height[i] > max) {

 max = height[i];

 arr[colour[i]] = 1;

 }

 }

 // Count the Number of 1's

 for (var i = 1; i <= K; i++) {

 if (arr[i] == 1)

 visible++;

 }

 return visible;

}

// Driver code

var height = [ 3, 5, 1, 2, 3 ];

var colour = [ 1, 2, 3, 4, 3 ];

var K = colour.length;

document.write( colourVisible(height, colour, K));

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    2

Want to learn from the best curated videos and practice problems, check out
the **C++ Foundation Course **for Basic to Advanced C++ and **C++ STL Course**
for foundation plus STL.

My Personal Notes _arrow_drop_up_

Save

