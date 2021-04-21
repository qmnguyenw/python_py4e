Find the number of boxes to be removed



Given an array arr[] representing a sequence of piles of boxes where each and
every box has the same height of 1 unit. Given that you are on the top of the
first pile and need to reach the ground by moving from each pile starting from
leftmost to rightmost.

 **Constraints** :

  * One can move from the current pile of box to the next one when the height of the next pile is equal or less than the height of the pile on which they are standing.
  * One can also encounter some piles whose height is greater than the pile they are standing on. So, they will need to remove some boxes from that pile to move forward. So, the task is to tell the total number of boxes needed to be removed from every pile(if necessary) during the journey to the ground.

The height of all the piles is given. Suppose that you are standing on the
first pile. Print the total number of boxes to be removed.

 **Examples** :

>  **Input** : arr[] = {3, 3, 2, 4, 1}  
>  **Output** : 2  
>  **Explanation** : After removing boxes, the heights of piles will be {3, 3,
> 2, 2, 1}  
> We are currently standing on 1st pile of height 3.  
>  **Step 1** : We can move to the 2nd pile, since it’s height is equal to the
> height of the current pile.  
>  **Step 2** : We can move to the 3rd pile of height 2, since it less than 3.  
>  **Step 3** : We cannot go from 3rd pile to 4th pile(of height 4), so we
> need to remove 2 boxes from 4th pile to make it’s height equal to 2.  
>  **Step 4** : We can easily move to the last pile since it’s height is 1
> which is less than the height of the 4th pile of height 2(by removing 2
> boxes in the previous step).
>
>  
>
>
>  
>
>
>  **Input** : arr[] = {5, 6, 7, 1}  
>  **Output** : 3  
>  **Explanation** : After removing boxes, the heights of piles will be {5, 5,
> 5, 1}  
> We are currently standing on 1st pile of height 5.  
>  **Step 1** : We cannot move to the 2nd pile since it’s height is more. So,
> we remove 1 box and make its height equal to 5 and then we move forward.  
>  **Step 2** : We cannot move to the 3rd pile of height 7, so we remove 2
> boxes from it.  
>  **Step 3** : We can easily move to the last pile since it’s height is 1
> which is less than the height of the 3rd pile of height 5.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The idea is to traverse the array starting from left and every time before
moving forward compare the height of the current pile with the previous pile.
If the height of the current pile is greater than the previous pile, then
increment count by the difference of the two heights otherwise move forward in
the array.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the number of

// boxes to be removed

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the number of

// boxes to be removed

int totalBoxesRemoved(int arr[], int n)

{

 int count = 0;

 

 // Store height of previous pile

 int prev = arr[0];

 

 // Start traversing the array

 for (int i = 1; i < n; i++) {

 // if height of current pile is greater

 // than previous pile

 if (arr[i] > prev) {

 // Increment count by difference

 // of two heights

 count += (arr[i] - prev);

 

 // Update current height

 arr[i] = prev;

 

 // Update prev for next iteration

 prev = arr[i];

 }

 else {

 // Update prev for next iteration

 prev = arr[i];

 }

 }

 

 return count;

}

 

// Driver code

int main()

{

 int arr[] = { 5, 4, 7, 3, 2, 1 };

 

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << totalBoxesRemoved(arr, n);

 

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

// Java program to find the number of

// boxes to be removed

import java.io.*;

 

class GFG {

 

// Function to find the number of

// boxes to be removed

static int totalBoxesRemoved(int arr[], int n)

{

 int count = 0;

 

 // Store height of previous pile

 int prev = arr[0];

 

 // Start traversing the array

 for (int i = 1; i < n; i++) {

 // if height of current pile is greater

 // than previous pile

 if (arr[i] > prev) {

 // Increment count by difference

 // of two heights

 count += (arr[i] - prev);

 

 // Update current height

 arr[i] = prev;

 

 // Update prev for next iteration

 prev = arr[i];

 }

 else {

 // Update prev for next iteration

 prev = arr[i];

 }

 }

 

 return count;

}

 

 // Driver code

 public static void main (String[] args) {

 int arr[] = { 5, 4, 7, 3, 2, 1 };

 

 int n = arr.length;

 

 System.out.println(totalBoxesRemoved(arr, n));

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

# Python3 program to find the

# number of boxes to be removed 

 

# Function to find the number

# of boxes to be removed 

def totalBoxesRemoved(arr, n): 

 

 count = 0

 

 # Store height of previous pile 

 prev = arr[0] 

 

 # Start traversing the array 

 for i in range(1, n):

 

 # if height of current pile 

 # is greater than previous pile 

 if (arr[i] > prev) : 

 

 # Increment count by 

 # difference of two heights 

 count += (arr[i] - prev) 

 

 # Update current height 

 arr[i] = prev 

 

 # Update prev for next 

 # iteration 

 prev = arr[i] 

 

 else :

 # Update prev for next 

 # iteration 

 prev = arr[i] 

 

 return count

 

# Driver code 

arr = [ 5, 4, 7, 3, 2, 1 ] 

 

n = len(arr) 

 

print(totalBoxesRemoved(arr, n)) 

 

# This code is contributed 

# by Yatin Gupta  
  
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

// C# program to find the number of

// boxes to be removed

using System;

 

class GFG {

 

// Function to find the number of

// boxes to be removed

static int totalBoxesRemoved(int []arr, int n)

{

 int count = 0;

 

 // Store height of previous pile

 int prev = arr[0];

 

 // Start traversing the array

 for (int i = 1; i < n; i++) {

 // if height of current pile is greater

 // than previous pile

 if (arr[i] > prev) {

 // Increment count by difference

 // of two heights

 count += (arr[i] - prev);

 

 // Update current height

 arr[i] = prev;

 

 // Update prev for next iteration

 prev = arr[i];

 }

 else {

 // Update prev for next iteration

 prev = arr[i];

 }

 }

 

 return count;

}

 

 // Driver code

 public static void Main () {

 int []arr = { 5, 4, 7, 3, 2, 1 };

 

 int n = arr.Length;

 

 Console.WriteLine(totalBoxesRemoved(arr, n));

 }

}

 

// This code is contributed 

// by shs  
  
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

// PHP program to find the number

// of boxes to be removed

 

 

// Function to find the number 

// of boxes to be removed

function totalBoxesRemoved($arr, $n)

{

 $count = 0;

 

 // Store height of previous pile

 $prev = $arr[0];

 

 // Start traversing the array

 for ($i = 1; $i <$n; $i++) 

 {

 // if height of current pile is 

 // greater than previous pile

 if ($arr[$i] > $prev) 

 {

 // Increment count by difference

 // of two heights

 $count += ($arr[$i] - $prev);

 

 // Update current height

 $arr[$i] = $prev;

 

 // Update prev for next iteration

 $prev = $arr[$i];

 }

 else

 {

 // Update prev for next iteration

 $prev = $arr[$i];

 }

 }

 

 return $count;

}

 

// Driver code

$arr = array( 5, 4, 7, 3, 2, 1 );

 

$n = count($arr);

 

echo totalBoxesRemoved($arr, $n);

 

// This code is contributed 

// by shs

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time Complexity** : O(N), where N is the total number of piles.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

