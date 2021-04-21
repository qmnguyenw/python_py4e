Pick points from array such that minimum distance is maximized



Given **C** magnets and an array **arr[]** representing **N** index positions
where **C ≤ N**. The task is to place these magnets at these available indices
in such a way that the distance between the two nearest magnets is as large as
possible.

 **Examples:**

>  **Input:** C = 4, arr[] = {1, 2, 5, 8, 10, 18}  
>  **Output:** 4  
> We can place 4 magnets to positions 1, 5, 10, 18 so maximum distance is
> minimum of ( dist(1, 5), dist(5, 10), dist(10, 18) ) = dist(1, 5) = 4.  
> And it will be the maximum possible distance between two nearest magnets.
>
>  **Input:** C = 3, arr[] = {5, 7, 11, 20, 23}  
>  **Output:** 6  
> We can place 3 magnets to positions 5, 11, 23 so answer will be minimum of (
> dist(5, 11), dist(11, 23) ) = dist(5, 11) = 6.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Find all possible positions of magnets that is C(n, c)
possible ways and find one that maximizes the distance between two magnets,
where C(n, c) is selecting c objects from n given objects.

  

  

 **Efficient approach:** Let mx be the maximum possible distance, therefore
all x greater than 0 and less than mx will also allow placing magnets but for
all y greater than mx, it will not be possible to place the magnets. Therefore
we can use binary search to find the maximum possible distance.  
Since our answer will always lie between 0 and the maximum index among the
given N indices. Therefore apply binary search and find the middle value
between the lowest and highest values say ‘mid’, make a function that will
check if it is possible to place C magnets assuming ‘mid’ as the maximum
possible distance.  
Overall time complexity will be O(nlog(n)) since binary search will take
O(log(n)) and O(n) for checking that if it is possible to place all C magnets.

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

 

// Function to check if it is possible

// to place C magnets assuming mid as

// maximum possible distance

bool isPossible(int arr[], int n, int C, int mid)

{

 // Variable magnet will store count of magnets

 // that got placed and currPosition will store

 // the position of last placed magnet

 int magnet = 1, currPosition = arr[0];

 

 for (int i = 1; i < n; i++) {

 

 // If difference between current index and

 // last placed index is greater than or equal to mid

 // it will allow placing magnet to this index

 if (arr[i] - currPosition >= mid) {

 

 magnet++;

 

 // Now this index will become

 // last placed index

 currPosition = arr[i];

 

 // If count of magnets placed becomes C

 if (magnet == C)

 return true;

 }

 }

 

 // If count of placed magnet is

 // less than C then return false

 return false;

}

 

// Function for modified binary search

int binarySearch(int n, int C, int arr[])

{

 int lo, hi, mid, ans;

 

 // Sort the indices in ascending order

 sort(arr, arr + n);

 

 // Minimum possible distance

 lo = 0;

 

 // Maximum possible distance

 hi = arr[n - 1];

 

 ans = 0;

 

 // Run the loop until lo becomes

 // greater than hi

 while (lo <= hi) {

 

 mid = (lo + hi) / 2;

 

 // If not possibble, decrease value of hi

 if (!isPossible(arr, n, C, mid))

 hi = mid - 1;

 else {

 

 // Update the answer

 ans = max(ans, mid);

 lo = mid + 1;

 }

 }

 

 // Return maximum possible distance

 return ans;

}

 

// Driver code

int main()

{

 int C = 4;

 int arr[] = { 1, 2, 5, 8, 10, 18 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << binarySearch(n, C, arr) << endl;

 

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

import java.util.*;

 

class GFG

{

 

// Function to check if it is possible

// to place C magnets assuming mid as

// maximum possible distance

static boolean isPossible(int []arr, int n, 

 int C, int mid)

{

 // Variable magnet will store count of magnets

 // that got placed and currPosition will store

 // the position of last placed magnet

 int magnet = 1, currPosition = arr[0];

 

 for (int i = 1; i < n; i++) 

 {

 

 // If difference between current index and

 // last placed index is greater than or equal to mid

 // it will allow placing magnet to this index

 if (arr[i] - currPosition >= mid)

 {

 

 magnet++;

 

 // Now this index will become

 // last placed index

 currPosition = arr[i];

 

 // If count of magnets placed becomes C

 if (magnet == C)

 return true;

 }

 }

 

 // If count of placed magnet is

 // less than C then return false

 return false;

}

 

// Function for modified binary search

static int binarySearch(int n, int C, int []arr)

{

 int lo, hi, mid, ans;

 

 // Sort the indices in ascending order

 Arrays.sort(arr);

 

 // Minimum possible distance

 lo = 0;

 

 // Maximum possible distance

 hi = arr[n - 1];

 

 ans = 0;

 

 // Run the loop until lo becomes

 // greater than hi

 while (lo <= hi) 

 {

 

 mid = (lo + hi) / 2;

 

 // If not possibble, decrease value of hi

 if (!isPossible(arr, n, C, mid))

 hi = mid - 1;

 else

 {

 

 // Update the answer

 ans = Math.max(ans, mid);

 lo = mid + 1;

 }

 }

 

 // Return maximum possible distance

 return ans;

}

 

// Driver code

public static void main(String args[])

{

 int C = 4;

 int []arr = { 1, 2, 5, 8, 10, 18 };

 int n = arr.length;

 System.out.println(binarySearch(n, C, arr));

}

}

 

// This code is contributed by Akanksha Rai  
  
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

 

# Function to check if it is possible

# to place C magnets assuming mid as

# maximum possible distance

def isPossible(arr, n, C, mid):

 

 # Variable magnet will store count of 

 # magnets that got placed and 

 # currPosition will store the position 

 # of last placed magnet

 magnet = 1

 currPosition = arr[0]

 

 for i in range(1, n):

 

 # If difference between current index 

 # and last placed index is greater than 

 # or equal to mid it will allow placing 

 # magnet to this index

 if (arr[i] - currPosition >= mid):

 magnet += 1

 

 # Now this index will become

 # last placed index

 currPosition = arr[i]

 

 # If count of magnets placed becomes C

 if (magnet == C):

 return True

 

 # If count of placed magnet is

 # less than C then return false

 return False

 

# Function for modified binary search

def binarySearch(n, C, arr):

 

 # Sort the indices in ascending order

 arr.sort(reverse = False)

 

 # Minimum possible distance

 lo = 0

 

 # Maximum possible distance

 hi = arr[n - 1]

 ans = 0

 

 # Run the loop until lo becomes

 # greater than hi

 while (lo <= hi):

 mid = int((lo + hi) / 2)

 

 # If not possibble, decrease value of hi

 if (isPossible(arr, n, C, mid) == False):

 hi = mid - 1

 else:

 

 # Update the answer

 ans = max(ans, mid)

 lo = mid + 1

 

 # Return maximum possible distance

 return ans

 

# Driver code

if __name__ == '__main__':

 C = 4

 arr = [1, 2, 5, 8, 10, 18]

 n = len(arr)

 print(binarySearch(n, C, arr))

 

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

// Function to check if it is possible

// to place C magnets assuming mid as

// maximum possible distance

static bool isPossible(int []arr, int n, 

 int C, int mid)

{

 // Variable magnet will store count of magnets

 // that got placed and currPosition will store

 // the position of last placed magnet

 int magnet = 1, currPosition = arr[0];

 

 for (int i = 1; i < n; i++) 

 {

 

 // If difference between current index and

 // last placed index is greater than or equal to mid

 // it will allow placing magnet to this index

 if (arr[i] - currPosition >= mid)

 {

 

 magnet++;

 

 // Now this index will become

 // last placed index

 currPosition = arr[i];

 

 // If count of magnets placed becomes C

 if (magnet == C)

 return true;

 }

 }

 

 // If count of placed magnet is

 // less than C then return false

 return false;

}

 

// Function for modified binary search

static int binarySearch(int n, int C, int []arr)

{

 int lo, hi, mid, ans;

 

 // Sort the indices in ascending order

 Array.Sort(arr);

 

 // Minimum possible distance

 lo = 0;

 

 // Maximum possible distance

 hi = arr[n - 1];

 

 ans = 0;

 

 // Run the loop until lo becomes

 // greater than hi

 while (lo <= hi) 

 {

 

 mid = (lo + hi) / 2;

 

 // If not possibble, decrease value of hi

 if (!isPossible(arr, n, C, mid))

 hi = mid - 1;

 else

 {

 

 // Update the answer

 ans = Math.Max(ans, mid);

 lo = mid + 1;

 }

 }

 

 // Return maximum possible distance

 return ans;

}

 

// Driver code

static void Main()

{

 int C = 4;

 int []arr = { 1, 2, 5, 8, 10, 18 };

 int n = arr.Length;

 Console.WriteLine(binarySearch(n, C, arr));

}

}

 

// This code is contributed by chandan_jnu  
  
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

 

// Function to check if it is possible

// to place C magnets assuming mid as

// maximum possible distance

function isPossible($arr, $n, $C, $mid)

{

 // Variable magnet will store count of magnets

 // that got placed and currPosition will store

 // the position of last placed magnet

 $magnet = 1; $currPosition = $arr[0];

 

 for ($i = 1; $i < $n; $i++) 

 {

 

 // If difference between current index and

 // last placed index is greater than or equal to mid

 // it will allow placing magnet to this index

 if ($arr[$i] - $currPosition >= $mid)

 {

 $magnet++;

 

 // Now this index will become

 // last placed index

 $currPosition = $arr[$i];

 

 // If count of magnets placed becomes C

 if ($magnet == $C)

 return true;

 }

 }

 

 // If count of placed magnet is

 // less than C then return false

 return false;

}

 

// Function for modified binary search

function binarySearch($n, $C, $arr)

{

 

 // Sort the indices in ascending order

 sort($arr, 0);

 

 // Minimum possible distance

 $lo = 0;

 

 // Maximum possible distance

 $hi = $arr[$n - 1];

 

 $ans = 0;

 

 // Run the loop until lo becomes

 // greater than hi

 while ($lo <= $hi) 

 {

 $mid = ($lo + $hi) / 2;

 

 // If not possibble, decrease value of hi

 if (!isPossible($arr, $n, $C, $mid))

 $hi = $mid - 1;

 else

 {

 

 // Update the answer

 $ans = max($ans, $mid);

 $lo = $mid + 1;

 }

 }

 

 // Return maximum possible distance

 return $ans;

}

 

// Driver code

$C = 4;

$arr = array(1, 2, 5, 8, 10, 18);

$n = sizeof($arr);

echo binarySearch($n, $C, $arr) . "\n";

 

// This code is contributed 

// by Akanksha Rai

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

**Time Complexity:** O(n * log(n))

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

