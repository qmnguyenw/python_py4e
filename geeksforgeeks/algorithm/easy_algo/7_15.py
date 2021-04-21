Find duplicate in an array in O(n) and by using O(1) extra space



Given an array arr[] containing n + 1 integers where each integer is between 1
and n (inclusive). There is only one duplicate element, find the duplicate
element in O(n) time complexity and O(1) space.  
 **Examples :**  

    
    
    Input  : arr[] = {1, 4, 3, 4, 2} 
    Output : 4
    
    Input  : arr[] = {1, 3, 2, 1}
    Output : 1

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach :**  
Firstly, the constraints of this problem imply that a cycle must exist.
Because each number in an array arr[] is between 1 and n, it will necessarily
point to an index that exists. Therefore, the list can be traversed
infinitely, which implies that there is a cycle. Additionally, because 0
cannot appear as a value in an array arr[], arr[0] cannot be part of the
cycle. Therefore, traversing the array in this manner from arr[0] is
equivalent to traversing a cyclic linked list. The problem can be solved just
like linked list cycle.  
Below is the implementation of above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP code to find the repeated elements

// in the array where every other is present once

#include <iostream>

using namespace std;

// Function to find duplicate

int findDuplicate(int arr[])

{

 // Find the intersection point of

 // the slow and fast.

 int slow = arr[0];

 int fast = arr[0];

 do

 {

 slow = arr[slow];

 fast = arr[arr[fast]];

 } while (slow != fast);

 // Find the "entrance" to the cycle.

 int ptr1 = arr[0];

 int ptr2 = slow;

 while (ptr1 != ptr2)

 {

 ptr1 = arr[ptr1];

 ptr2 = arr[ptr2];

 }

 return ptr1;

}

// Driver code

int main()

{

 int arr[] = { 1, 3, 2, 1 };

 

 cout << findDuplicate(arr) << endl;

 

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

// Java code to find the repeated

// elements in the array where

// every other is present once

import java.util.*;

class GFG

{

// Function to find duplicate

public static int findDuplicate(int []arr)

{

 // Find the intersection

 // point of the slow and fast.

 int slow = arr[0];

 int fast = arr[0];

 do

 {

 slow = arr[slow];

 fast = arr[arr[fast]];

 } while (slow != fast);

 // Find the "entrance"

 // to the cycle.

 int ptr1 = arr[0];

 int ptr2 = slow;

 while (ptr1 != ptr2)

 {

 ptr1 = arr[ptr1];

 ptr2 = arr[ptr2];

 }

 return ptr1;

}

// Driver Code

public static void main(String[] args)

{

 int []arr = {1, 3, 2, 1};

 System.out.println("" +

 findDuplicate(arr));

 System.exit(0);

}

}

// This code is contributed

// by Harshit Saini  
  
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

# Python code to find the

# repeated elements in the

# array where every other

# is present once

# Function to find duplicate

def findDuplicate(arr):

 # Find the intersection

 # point of the slow and fast.

 slow = arr[0]

 fast = arr[0]

 while True:

 slow = arr[slow]

 fast = arr[arr[fast]]

 if slow == fast:

 break

 # Find the "entrance"

 # to the cycle.

 ptr1 = arr[0]

 ptr2 = slow

 while ptr1 != ptr2:

 ptr1 = arr[ptr1]

 ptr2 = arr[ptr2]

 

 return ptr1

 

# Driver code

if __name__ == '__main__':

 

 

 arr = [ 1, 3, 2, 1 ]

 print(findDuplicate(arr))

# This code is contributed

# by Harshit Saini  
  
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

// C# code to find the repeated

// elements in the array where

// every other is present once

using System;

class GFG

{

// Function to find duplicate

public static int findDuplicate(int []arr)

{

 // Find the intersection

 // point of the slow and fast.

 int slow = arr[0];

 int fast = arr[0];

 do

 {

 slow = arr[slow];

 fast = arr[arr[fast]];

 } while (slow != fast);

 // Find the "entrance"

 // to the cycle.

 int ptr1 = arr[0];

 int ptr2 = slow;

 while (ptr1 != ptr2)

 {

 ptr1 = arr[ptr1];

 ptr2 = arr[ptr2];

 }

 return ptr1;

}

// Driver Code

public static void Main()

{

 int[] arr = {1, 3, 2, 1};

 Console.WriteLine("" +

 findDuplicate(arr));

}

}

// This code is contributed

// by Akanksha Rai(Abby_akku)  
  
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

// PHP code to find the repeated

// elements in the array where

// every other is present once

// Function to find duplicate

function findDuplicate(&$arr)

{

 $slow = $arr[0];

 $fast = $arr[0];

 do

 {

 $slow = $arr[$slow];

 $fast = $arr[$arr[$fast]];

 } while ($slow != $fast);

 // Find the "entrance"

 // to the cycle.

 $ptr1 = $arr[0];

 $ptr2 = $slow;

 while ($ptr1 != $ptr2)

 {

 $ptr1 = $arr[$ptr1];

 $ptr2 = $arr[$ptr2];

 }

 return $ptr1;

}

// Driver code

$arr = array(1, 3, 2, 1);

echo " " . findDuplicate($arr);

// This code is contributed

// by Shivi_Aggarwal

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

// JavaScript code to find the repeated elements

// in the array where every other is present once

// Function to find duplicate

function findDuplicate(arr)

{

 // Find the intersection point of

 // the slow and fast.

 let slow = arr[0];

 let fast = arr[0];

 do

 {

 slow = arr[slow];

 fast = arr[arr[fast]];

 } while (slow != fast);

 // Find the "entrance" to the cycle.

 let ptr1 = arr[0];

 let ptr2 = slow;

 while (ptr1 != ptr2)

 {

 ptr1 = arr[ptr1];

 ptr2 = arr[ptr2];

 }

 return ptr1;

}

// Driver code

 let arr = [ 1, 3, 2, 1 ];

 document.write(findDuplicate(arr) + "<br>");

 

// This code is contributed by Surbhi Tyagi.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    1

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

