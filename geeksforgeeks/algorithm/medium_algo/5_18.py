Value to be subtracted from array elements to make sum of all elements equals
K



Given an integer **K** and an array **height[]** where **height[i]** denotes
the height of the **i th** tree in a forest. The task is to make a cut of
height **X** from the ground such that exactly **K** unit wood is collected.
If it is not possible then print **-1** else print **X**.

 **Examples:**

>  **Input:** height[] = {1, 2, 1, 2}, K = 2  
>  **Output:** 1  
> Make a cut at height 1, the updated array will be {1, 1, 1, 1} and  
> the collected wood will be {0, 1, 0, 1} i.e. 0 + 1 + 0 + 1 = 2.
>
>  **Input:** height = {1, 1, 2, 2}, K = 1  
>  **Output:** -1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can be solved using binary search.

  

  

  * Sort the heights of the trees.
  * The lowest height to make the cut is **0** and the highest is the maximum height among all the trees. So, set **low = 0** and **high = max(height[i])**.
  * Repeat the below steps **while low ≤ high:**
    1. Set **mid = low + ((high – low) / 2)**.
    2. Count the amount of wood that can be collected if the cut is made at height **mid** and store it in a variable **collected**.
    3. If **collected = K** then **mid** is the answer.
    4. If **collecetd > K** then update **low = mid + 1** as the cut needs to be made at a height higher than the current height
    5. Else update **high = mid – 1** as cuts need to made at a lower height.
  * Print **-1** if no such value of **mid** is found.

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

#include <iostream>

using namespace std;

 

// Function to return the amount of wood

// collected if the cut is made at height m

int woodCollected(int height[], int n, int m)

{

 int sum = 0;

 for (int i = n - 1; i >= 0; i--) {

 if (height[i] - m <= 0)

 break;

 sum += (height[i] - m);

 }

 

 return sum;

}

 

// Function that returns Height at

// which cut should be made

int collectKWood(int height[], int n, int k)

{

 // Sort the heights of the trees

 sort(height, height + n);

 

 // The minimum and the maximum

 // cut that can be made

 int low = 0, high = height[n - 1];

 

 // Binary search to find the answer

 while (low <= high) {

 int mid = low + ((high - low) / 2);

 

 // The amount of wood collected

 // when cut is made at the mid

 int collected = woodCollected(height, n, mid);

 

 // If the current collected wood is

 // equal to the required amount

 if (collected == k)

 return mid;

 

 // If it is more than the required amount

 // then the cut needs to be made at a

 // height higher than the current height

 if (collected > k)

 low = mid + 1;

 

 // Else made the cut at a lower height

 else

 high = mid - 1;

 }

 

 return -1;

}

 

// Driver code

int main()

{

 

 int height[] = { 1, 2, 1, 2 };

 int n = sizeof(height) / sizeof(height[0]);

 int k = 2;

 

 cout << collectKWood(height, n, k);

 

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

import java.util.Arrays; 

 

class GFG 

{

 static int[] height = new int[]{ 1, 2, 1, 2 }; 

 

 // Function to return the amount of wood 

 // collected if the cut is made at height m 

 public static int woodCollected(int n, int m) 

 { 

 int sum = 0; 

 for (int i = n - 1; i >= 0; i--)

 { 

 if (height[i] - m <= 0) 

 break; 

 sum += (height[i] - m); 

 } 

 return sum; 

 } 

 

 // Function that returns Height at 

 // which cut should be made 

 public static int collectKWood(int n, int k) 

 { 

 // Sort the heights of the trees 

 Arrays.sort(height);

 

 // The minimum and the maximum 

 // cut that can be made 

 int low = 0, high = height[n - 1]; 

 

 // Binary search to find the answer 

 while (low <= high)

 { 

 int mid = low + ((high - low) / 2); 

 

 // The amount of wood collected 

 // when cut is made at the mid 

 int collected = woodCollected(n, mid); 

 

 // If the current collected wood is 

 // equal to the required amount 

 if (collected == k) 

 return mid; 

 

 // If it is more than the required amount 

 // then the cut needs to be made at a 

 // height higher than the current height 

 if (collected > k) 

 low = mid + 1; 

 

 // Else made the cut at a lower height 

 else

 high = mid - 1; 

 } 

 return -1; 

 } 

 

 // Driver code 

 public static void main(String[] args)

 { 

 int k = 2; 

 int n = height.length;

 System.out.print(collectKWood(n,k)); 

 } 

}

 

// This code is contributed by Sanjit_Prasad  
  
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

# Python3 implementation of the approach

 

# Function to return the amount of wood

# collected if the cut is made at height m

def woodCollected(height, n, m):

 sum = 0

 for i in range(n - 1, -1, -1):

 if (height[i] - m <= 0):

 break

 sum += (height[i] - m)

 

 return sum

 

# Function that returns Height at

# which cut should be made

def collectKWood(height, n, k):

 

 # Sort the heights of the trees

 height = sorted(height)

 

 # The minimum and the maximum

 # cut that can be made

 low = 0

 high = height[n - 1]

 

 # Binary search to find the answer

 while (low <= high):

 mid = low + ((high - low) // 2)

 

 # The amount of wood collected

 # when cut is made at the mid

 collected = woodCollected(height, n, mid)

 

 # If the current collected wood is

 # equal to the required amount

 if (collected == k):

 return mid

 

 # If it is more than the required amount

 # then the cut needs to be made at a

 # height higher than the current height

 if (collected > k):

 low = mid + 1

 

 # Else made the cut at a lower height

 else:

 high = mid - 1

 

 return -1

 

# Driver code

height = [1, 2, 1, 2]

n = len(height)

k = 2

 

print(collectKWood(height, n, k))

 

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

// C# implementation of the approach

using System;

using System.Collections; 

 

class GFG 

{ 

 static int[] height = { 1, 2, 1, 2 }; 

 

 // Function to return the amount of wood 

 // collected if the cut is made at height m 

 public static int woodCollected(int n, int m) 

 { 

 int sum = 0; 

 for (int i = n - 1; i >= 0; i--) 

 { 

 if (height[i] - m <= 0) 

 break; 

 sum += (height[i] - m); 

 } 

 return sum; 

 } 

 

 // Function that returns Height at 

 // which cut should be made 

 public static int collectKWood(int n, int k) 

 { 

 // Sort the heights of the trees 

 Array.Sort(height); 

 

 // The minimum and the maximum 

 // cut that can be made 

 int low = 0, high = height[n - 1]; 

 

 // Binary search to find the answer 

 while (low <= high) 

 { 

 int mid = low + ((high - low) / 2); 

 

 // The amount of wood collected 

 // when cut is made at the mid 

 int collected = woodCollected(n, mid); 

 

 // If the current collected wood is 

 // equal to the required amount 

 if (collected == k) 

 return mid; 

 

 // If it is more than the required amount 

 // then the cut needs to be made at a 

 // height higher than the current height 

 if (collected > k) 

 low = mid + 1; 

 

 // Else made the cut at a lower height 

 else

 high = mid - 1; 

 } 

 return -1; 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 int k = 2; 

 int n = height.Length; 

 Console.WriteLine(collectKWood(n,k)); 

 } 

} 

 

// This code is contributed by AnkitRai01  
  
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

