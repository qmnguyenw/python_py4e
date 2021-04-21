Remove minimum numbers from the array to get minimum OR value



Given an array **arr[]** of **N** positive integers, the task is to find the
minimum number of elements to be deleted from the array so that the bitwise OR
of the array elements get minimized. You are not allowed to remove all the
elements i.e. at least one element must remain in the array.

 **Examples:**

>  **Input:** arr[] = {1, 2, 3}  
>  **Output:** 2  
> All possible subsets and there OR values are:  
> a) {1, 2, 3} = 3  
> b) {1, 2} = 3  
> c) {2, 3} = 3  
> d) {1, 3} = 3  
> e) {1} = 1  
> f) {2} = 2  
> g) {3} = 3  
> The minimum possible OR will be 1 from the subset {1}.  
> So, we will need to remove 2 elements.
>
>  **Input:** arr[] = {3, 3, 3}  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Generate all possible sub-sequences and test which one
gives the minimum ‘OR’ value. Let the length of the largest sub-sequence with
minimum possible OR be **L** then the answer will **N – L**. This will take
exponential time.

  

  

 **Better approach:** The minimum value will always be equal to the smallest
number present in the array. If this number get bitwise ORed with any other
number other than itself then the value of the OR will change and it won’t
stay minimum anymore. Thus, we need to remove all the elements that are not
equal to this minimum element.

  * Find the smallest number in the array.
  * Find the frequency of this element in the array say **cnt**.
  * The final answer will be **N – cnt**.

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

 

// Function to return the minimum

// deletions to get minimum OR

int findMinDel(int* arr, int n)

{

 

 // To store the minimum element

 int min_num = INT_MAX;

 

 // Find the minimum element

 // from the array

 for (int i = 0; i < n; i++)

 min_num = min(arr[i], min_num);

 

 // To store the frequency of

 // the minimum element

 int cnt = 0;

 

 // Find the frequency of the

 // minimum element

 for (int i = 0; i < n; i++)

 if (arr[i] == min_num)

 cnt++;

 

 // Return the final answer

 return n - cnt;

}

 

// Driver code

int main()

{

 int arr[] = { 3, 3, 2 };

 int n = sizeof(arr) / sizeof(int);

 

 cout << findMinDel(arr, n);

 

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

class GFG 

{

 

// Function to return the minimum

// deletions to get minimum OR

static int findMinDel(int []arr, int n)

{

 

 // To store the minimum element

 int min_num = Integer.MAX_VALUE;

 

 // Find the minimum element

 // from the array

 for (int i = 0; i < n; i++)

 min_num = Math.min(arr[i], min_num);

 

 // To store the frequency of

 // the minimum element

 int cnt = 0;

 

 // Find the frequency of the

 // minimum element

 for (int i = 0; i < n; i++)

 if (arr[i] == min_num)

 cnt++;

 

 // Return the final answer

 return n - cnt;

}

 

// Driver code

public static void main(String[] args)

{

 int arr[] = { 3, 3, 2 };

 int n = arr.length;

 

 System.out.print(findMinDel(arr, n));

}

}

 

// This code is contributed by PrinciRaj1992  
  
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

import sys

 

# Function to return the minimum 

# deletions to get minimum OR 

def findMinDel(arr, n) : 

 

 # To store the minimum element 

 min_num = sys.maxsize; 

 

 # Find the minimum element 

 # from the array 

 for i in range(n) :

 min_num = min(arr[i], min_num); 

 

 # To store the frequency of 

 # the minimum element 

 cnt = 0; 

 

 # Find the frequency of the 

 # minimum element 

 for i in range(n) : 

 if (arr[i] == min_num) :

 cnt += 1; 

 

 # Return the final answer 

 return n - cnt; 

 

# Driver code 

if __name__ == "__main__" : 

 

 arr = [ 3, 3, 2 ];

 n = len(arr);

 

 print(findMinDel(arr, n)); 

 

# This code is contributed by AnkitRai01  
  
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

 

// Function to return the minimum

// deletions to get minimum OR

static int findMinDel(int []arr, int n)

{

 

 // To store the minimum element

 int min_num = int.MaxValue;

 

 // Find the minimum element

 // from the array

 for (int i = 0; i < n; i++)

 min_num = Math.Min(arr[i], 

 min_num);

 

 // To store the frequency of

 // the minimum element

 int cnt = 0;

 

 // Find the frequency of the

 // minimum element

 for (int i = 0; i < n; i++)

 if (arr[i] == min_num)

 cnt++;

 

 // Return the readonly answer

 return n - cnt;

}

 

// Driver code

public static void Main(String[] args)

{

 int []arr = { 3, 3, 2 };

 int n = arr.Length;

 

 Console.Write(findMinDel(arr, n));

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

