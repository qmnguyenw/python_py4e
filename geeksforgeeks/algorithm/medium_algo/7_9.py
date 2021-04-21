Find a triplet in an array whose sum is closest to a given number



Given an array **arr[]** of **N** integers and an integer **X** , the task is
to find three integers in **arr[]** such that the sum is closest to **X**.  
 **Examples:**

    
    
     **Input:** arr[] = {-1, 2, 1, -4}, X = 1
    **Output:** 2
    **Explanation:**
    Sums of triplets:
    (-1) + 2 + 1 = 2
    (-1) + 2 + (-4) = -3
    2 + 1 + (-4) = -1
    2 is closest to 1.
    
    **Input:** arr[] = {1, 2, 3, 4, -5}, X = 10
    **Output:** 9
    **Explanation:**
    Sums of triplets:
    1 + 2 + 3 = 6
    2 + 3 + 4 = 9
    1 + 3 + 4 = 7
    ...
    9 is closest to 10.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 ** _Simple Approach:_** The naive approach is to explore all the subsets of
size 3 and keep a track of the difference between X and the sum of this
subset. Then return the subset whose difference between its sum and X is
minimum.

 **Algorithm:**

  1. Create three nested loops with counter i, j and k respectively.
  2. The first loop will start from start to end, the second loop will run from i+1 to end, the third loop will run from j+1 to end.
  3. Check if the difference of the sum of ith, jth and kth element with the given sum is less than the current minimum or not. Update the current minimum
  4. Print the closest sum.

 **Implementation:**

## C++14

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

// Function to return the sum of a

// triplet which is closest to x

int solution(vector<int>& arr, int x)

{

 // To store the closets sum

 int closestSum = INT_MAX;

 // Run three nested loops each loop

 // for each element of triplet

 for (int i = 0; i < arr.size() ; i++)

 {

 for(int j =i + 1; j < arr.size(); j++)

 {

 for(int k =j + 1; k < arr.size(); k++)

 {

 //update the closestSum

 if(abs(x - closestSum) > abs(x - (arr[i] + arr[j] + arr[k])))

 closestSum = (arr[i] + arr[j] + arr[k]);

 }

 }

 }

 // Return the closest sum found

 return closestSum;

}

// Driver code

int main()

{

 vector<int> arr = { -1, 2, 1, -4 };

 int x = 1;

 cout << solution(arr, x);

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

class GFG{

 

// Function to return the sum of a

// triplet which is closest to x

public static int solution(int arr[], int x)

{

 

 // To store the closets sum

 int closestSum = Integer.MAX_VALUE;

 

 // Run three nested loops each loop 

 // for each element of triplet

 for(int i = 0; i < arr.length ; i++) 

 {

 for(int j = i + 1; j < arr.length; j++)

 {

 for(int k = j + 1; k < arr.length; k++)

 {

 

 // Update the closestSum

 if (Math.abs(x - closestSum) >

 Math.abs(x - (arr[i] + arr[j] + arr[k])))

 closestSum = (arr[i] + arr[j] + arr[k]);

 } 

 }

 }

 

 // Return the closest sum found

 return closestSum;

}

// Driver code

public static void main(String[] args)

{

 int arr[] = { -1, 2, 1, -4 };

 int x = 1;

 

 System.out.print(solution(arr, x));

}

}

// This code is contributed by divyeshrabadiya07  
  
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

import sys

# Function to return the sum of a

# triplet which is closest to x

def solution(arr, x):

 # To store the closets sum

 closestSum = sys.maxsize

 # Run three nested loops each loop

 # for each element of triplet

 for i in range (len(arr)) :

 for j in range(i + 1, len(arr)):

 for k in range(j + 1, len( arr)):

 

 # Update the closestSum

 if(abs(x - closestSum) >

 abs(x - (arr[i] +

 arr[j] + arr[k]))):

 closestSum = (arr[i] +

 arr[j] + arr[k])

 

 # Return the closest sum found

 return closestSum

# Driver code

if __name__ == "__main__":

 

 arr = [ -1, 2, 1, -4 ]

 x = 1

 

 print(solution(arr, x))

# This code is contributed by chitranayal  
  
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

using System.Collections.Generic;

class GFG{

// Function to return the sum of a

// triplet which is closest to x

static int solution(ArrayList arr, int x)

{

 

 // To store the closets sum

 int closestSum = int.MaxValue;

 // Run three nested loops each loop

 // for each element of triplet

 for(int i = 0; i < arr.Count; i++)

 {

 for(int j = i + 1; j < arr.Count; j++)

 {

 for(int k = j + 1; k < arr.Count; k++)

 {

 if (Math.Abs(x - closestSum) >

 Math.Abs(x - ((int)arr[i] +

 (int)arr[j] + (int)arr[k])))

 {

 closestSum = ((int)arr[i] +

 (int)arr[j] +

 (int)arr[k]);

 }

 }

 }

 }

 

 // Return the closest sum found

 return closestSum;

}

// Driver code

public static void Main(string[] args)

{

 ArrayList arr = new ArrayList(){ -1, 2, 1, -4 };

 int x = 1;

 Console.Write(solution(arr, x));

}

}

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    2

