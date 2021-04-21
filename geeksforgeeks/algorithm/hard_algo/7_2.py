Sum of maximum elements of all possible sub-arrays of an array



Given an array **arr[]** , the task is to find the sum of the maximum elements
of every possible sub-array of the array.

 **Examples:**

>  **Input:** arr[] = {1, 3, 2}  
>  **Output:** 15  
> All possible sub-arrays are {1}, {2}, {3}, {1, 3}, {3, 2} and {1, 3, 2}  
> And, the sum of all the maximum elements is 1 + 2 + 3 + 3 + 3 + 3 = 15
>
>  **Input:** arr[] = {3, 1}  
>  **Output:** 7

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **simple method** is to generate all the sub-arrays and then sum the maximum
elements in all of them. The time complexity of this solution will be O(n3).

  

  

 **Better method:**  
The key for optimization is the question-

> In how many segments, the value at an index will be maximum?

The next idea that might come into our mind will be for every index **i** in
the array **arr** , we try to find:  
 **Left count:** We iterate towards left of the index **i** till we don’t
encounter an element **strictly greater** than **arr[i]** or we don’t reach
the left end of the array. Let us call this count for the index **i** of the
given array as **CLi**.  
 **Right count:** We iterate towards right of the index till we don’t
encounter an element **greater than or equal to** the value at the index or we
don’t reach the right end. Let us call this count for the index **i** of the
given array as **CRi**.

 **(CLi + 1) * (CRi + 1)** will be the number of sub-arrays for the current
index **i** in which its value will be maximum because there are **CLi + 1**
ways to choose elements from left side (including choosing no element) and
**CRi + 1** ways to choose elements from the right side.

> The time complexity of this approach will be O(n2)

 **Best method:**  
This problem can be solved using stack data structure in **O(n)** time. The
idea remains the same as is in the previous approach. For the sake of saving
some time, we will use stack from the Standard Template Library of C++.

 **Left count:** Let **CLi** represent the left count for an index **i**.
**CLi** for an index **i** can be defined as the number of elements between
the index **i** and the right most element whose value is strictly greater
than **arr[i]** having index less than **i**. If, there is no such element,
then **CLi** for an element will be equal to the number of elements to the
left of the index **i**.

To achieve this, we will insert only the index of the elements from left to
right into the stack. Let us suppose, we are inserting an index **i** in the
stack and **j** be the index of the topmost element currently present in the
stack. While the value **arr[i]** is **greater than or equal to** the value at
the top most index in the stack and the stack is not empty, keep popping the
elements in the stack. Whenever, an element is popped, the left count(CLi) of
the current index(i) is updated as **CLi = CLi + CLj + 1**.

 **Right count:** We calculate the right count for all the indexes in the
similar way. The only difference is we push the elements in stack while
traversing right to left in the array. While **arr[i]** is **strictly
greater** than the value at the top most index in the stack and the stack is
not empty, keep popping the elements. Whenever, an element is popped, the
right count of the current index(i) is updated as **CRi = CRi + CRj + 1**.

 **Final step:** Let **ans** be the variable containing the final answer. We
will initialize it with **0**. Then, we will iterate through all the indexes
from **1** to **n** of the array and update the **ans** as **ans = ans + (CLi
+ 1) * (CRi + 1) * arr[i]** for all possible values of **i** from **1** to
**n**.

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

#include <iostream>

#include <stack>

using namespace std;

 

// Function to return the required sum

int findMaxSum(int arr[], int n)

{

 // Arrays for maintaining left and right count

 int CL[n] = { 0 }, CR[n] = { 0 };

 

 // Stack for storing the indexes

 stack<int> q;

 

 // Calculate left count for every index

 for (int i = 0; i < n; i++) {

 while (q.size() != 0 && arr[q.top()] <= arr[i]) {

 CL[i] += CL[q.top()] + 1;

 q.pop();

 }

 q.push(i);

 }

 

 // Clear the stack

 while (q.size() != 0)

 q.pop();

 

 // Calculate right count for every index

 for (int i = n - 1; i >= 0; i--) {

 while (q.size() != 0 && arr[q.top()] < arr[i]) {

 CR[i] += CR[q.top()] + 1;

 q.pop();

 }

 q.push(i);

 }

 

 // Clear the stack

 while (q.size() != 0)

 q.pop();

 

 // To store the required sum

 int ans = 0;

 

 // Calculate the final sum

 for (int i = 0; i < n; i++)

 ans += (CL[i] + 1) * (CR[i] + 1) * arr[i];

 

 return ans;

}

 

// Driver code

int main()

{

 int arr[] = { 1, 3, 2 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << findMaxSum(arr, n);

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

 

public class GFG 

{ 

 // Function to return the required sum 

 static int findMaxSum(int arr[], int n) 

 { 

 // Arrays for maintaining left and right count 

 int CL[] = new int[n], CR[] = new int[n]; 

 

 // Stack for storing the indexes 

 Stack<Integer> q = new Stack<Integer>(); 

 

 // Calculate left count for every index 

 for (int i = 0; i < n; i++) 

 { 

 while (q.size() != 0 && arr[q.peek()] <= arr[i]) 

 { 

 CL[i] += CL[q.peek()] + 1; 

 q.pop(); 

 } 

 q.push(i); 

 } 

 

 // Clear the stack 

 while (q.size() != 0) 

 q.pop(); 

 

 // Calculate right count for every index 

 for (int i = n - 1; i >= 0; i--) 

 { 

 while (q.size() != 0 && arr[q.peek()] < arr[i]) 

 { 

 CR[i] += CR[q.peek()] + 1; 

 q.pop(); 

 } 

 q.push(i); 

 } 

 

 // Clear the stack 

 while (q.size() != 0) 

 q.pop(); 

 

 // To store the required sum 

 int ans = 0; 

 

 // Calculate the final sum 

 for (int i = 0; i < n; i++) 

 ans += (CL[i] + 1) * (CR[i] + 1) * arr[i]; 

 

 return ans; 

 } 

 

 // Driver code 

 public static void main(String[] args) 

 { 

 int arr[] = { 1, 3, 2 }; 

 int n = arr.length; 

 System.out.println(findMaxSum(arr, n)); 

 } 

} 

 

// This code is contributed by Rituraj Jain  
  
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

 

# Function to return the required sum 

def findMinSum(arr, n): 

 

 # Arrays for maintaining left 

 # and right count 

 CL = [0] * n

 CR = [0] * n 

 

 # Stack for storing the indexes 

 q = []

 

 # Calculate left count for every index 

 for i in range(0, n): 

 while (len(q) != 0 and

 arr[q[-1]] <= arr[i]): 

 CL[i] += CL[q[-1]] + 1

 q.pop() 

 

 q.append(i) 

 

 # Clear the stack 

 while len(q) != 0: 

 q.pop() 

 

 # Calculate right count for every index 

 for i in range(n - 1, -1, -1): 

 while (len(q) != 0 and

 arr[q[-1]] < arr[i]): 

 CR[i] += CR[q[-1]] + 1

 q.pop() 

 

 q.append(i) 

 

 # Clear the stack 

 while len(q) != 0: 

 q.pop() 

 

 # To store the required sum 

 ans = 0

 

 # Calculate the final sum 

 for i in range(0, n): 

 ans += (CL[i] + 1) * (CR[i] + 1) * arr[i] 

 

 return ans 

 

# Driver code 

if __name__ == "__main__":

 

 arr = [1, 3, 2] 

 n = len(arr) 

 print(findMinSum(arr, n))

 

# This code is contributed by Rituraj Jain   
  
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

using System.Collections.Generic;

 

class GFG 

{ 

 // Function to return the required sum 

 static int findMaxSum(int []arr, int n) 

 { 

 // Arrays for maintaining left and right count 

 int []CL = new int[n]; int []CR = new int[n]; 

 

 // Stack for storing the indexes 

 Stack<int> q = new Stack<int>(); 

 

 // Calculate left count for every index 

 for (int i = 0; i < n; i++) 

 { 

 while (q.Count != 0 && arr[q.Peek()] <= arr[i]) 

 { 

 CL[i] += CL[q.Peek()] + 1; 

 q.Pop(); 

 } 

 q.Push(i); 

 } 

 

 // Clear the stack 

 while (q.Count != 0) 

 q.Pop(); 

 

 // Calculate right count for every index 

 for (int i = n - 1; i >= 0; i--) 

 { 

 while (q.Count != 0 && arr[q.Peek()] < arr[i]) 

 { 

 CR[i] += CR[q.Peek()] + 1; 

 q.Pop(); 

 } 

 q.Push(i); 

 } 

 

 // Clear the stack 

 while (q.Count != 0) 

 q.Pop(); 

 

 // To store the required sum 

 int ans = 0; 

 

 // Calculate the final sum 

 for (int i = 0; i < n; i++) 

 ans += (CL[i] + 1) * (CR[i] + 1) * arr[i]; 

 

 return ans; 

 } 

 

 // Driver code 

 public static void Main(String[] args) 

 { 

 int []arr = { 1, 3, 2 }; 

 int n = arr.Length; 

 Console.WriteLine(findMaxSum(arr, n)); 

 } 

} 

 

// This code has been contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    15
    

**Time complexity:** O(n)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

