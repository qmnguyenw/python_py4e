Minimum increment operations to make K elements equal



Given an array **arr[]** of **N** elements and an integer **K** , the task is
to make any **K** elements of the array equal by performing only increment
operations i.e. in one operation, any element can be incremented by 1. Find
the minimum number of operations required to make any **K** elements equal.

 **Examples:**

>  **Input:** arr[] = {3, 1, 9, 100}, K = 3  
>  **Output:** 14  
> Increment 3 six times and 1 eight times for a total of  
> 14 operations to make 3 elements equal to 9.
>
>  **Input:** arr[] = {5, 3, 10, 5}, K = 2  
>  **Output:** 0  
> No operations are required as first and last  
> elements are already equal.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:**

  

  

  1. Sort the array in increasing order.
  2. Now select **K** elements and make them equal.
  3. Choose the **i th** value as the largest value and make all elements just smaller than it equal to the **i th** element.
  4. Calculate the number of operations needed to make **K** elements equal to the **i th** element for all **i**.
  5. The answer will be the minimum of all the possibilities.

Time Complexity of this approach will be **O(n*K + nlogn)**.

 **Efficient approach:** the naive approach can be modified to calculate the
minimum operations needed to make **K** elements equal to the **i th** element
faster than **O(K)** using the sliding window technique in constant time given
that the operations required for making the **1 st** **K** elements equal to
the **K th** element are known.

Let **C** be the operations needed or cost for making the elements in the
range **[l, l + K – 1]** equal to the **(l + K – 1) th** element. Now to find
the cost for the range **[l + 1, l + K]** , the solution for the range **[l, l
+ K – 1]** can be used.  
Let **C’** be the cost for the range **[l + 1, l + K]**.

  1. Since we increment **l th** element to **(l + K – 1) th** element, **C** includes the cost element(l + k – 1) – element(l) but **C’** does not need to include this cost.  
So, **C’ = C – (element(l + k – 1) – element(l))**

  2. Now **C’** represents the cost of making all the elements in the range **[l + 1, l + K – 1]** equal to **(l + K – 1) th** element.  
Since, we need to make all elements equal to the **(l + K) th** element
instead of the **(l + K – 1) th** element, we can increment these **k – 1**
elements to the **(l + K) th** element which makes **C’ = C’ + (k – 1) *
(element(l + k) – element(l + k -1))**

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

 

// Function to return the minimum number of

// increment operations required to make

// any k elements of the array equal

int minOperations(vector<int> ar, int k)

{

 // Sort the array in increasing order

 sort(ar.begin(), ar.end());

 

 // Calculate the number of operations

 // needed to make 1st k elements equal to

 // the kth element i.e. the 1st window

 int opsNeeded = 0;

 for (int i = 0; i < k; i++) {

 opsNeeded += ar[k - 1] - ar[i];

 }

 

 // Answer will be the minimum of all

 // possible k sized windows

 int ans = opsNeeded;

 

 // Find the operations needed to make

 // k elements equal to ith element

 for (int i = k; i < ar.size(); i++) {

 

 // Slide the window to the right and

 // subtract increments spent on leftmost

 // element of the previous window

 opsNeeded = opsNeeded - (ar[i - 1] - ar[i - k]);

 

 // Add increments needed to make the 1st k-1

 // elements of this window equal to the

 // kth element of the current window

 opsNeeded += (k - 1) * (ar[i] - ar[i - 1]);

 ans = min(ans, opsNeeded);

 }

 return ans;

}

 

// Driver code

int main()

{

 vector<int> arr = { 3, 1, 9, 100 };

 int n = arr.size();

 int k = 3;

 

 cout << minOperations(arr, k);

 

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

 

class geeksforgeeks {

 

// Function to return the minimum number of 

// increment operations required to make 

// any k elements of the array equal 

static int minOperations(int ar[], int k) 

{ 

 // Sort the array in increasing order 

 Arrays.sort(ar); 

 

 // Calculate the number of operations 

 // needed to make 1st k elements equal to 

 // the kth element i.e. the 1st window 

 int opsNeeded = 0; 

 for (int i = 0; i < k; i++) { 

 opsNeeded += ar[k - 1] - ar[i]; 

 } 

 

 // Answer will be the minimum of all 

 // possible k sized windows 

 int ans = opsNeeded; 

 

 // Find the operations needed to make 

 // k elements equal to ith element 

 for (int i = k; i < ar.length; i++) { 

 

 // Slide the window to the right and 

 // subtract increments spent on leftmost 

 // element of the previous window 

 opsNeeded = opsNeeded - (ar[i - 1] - ar[i - k]); 

 

 // Add increments needed to make the 1st k-1 

 // elements of this window equal to the 

 // kth element of the current window 

 opsNeeded += (k - 1) * (ar[i] - ar[i - 1]); 

 ans = Math.min(ans, opsNeeded); 

 } 

 return ans; 

} 

 

// Driver code 

public static void main(String[] args) 

{ 

 int[] arr = { 3, 1, 9, 100 }; 

 int n = arr.length; 

 int k = 3; 

 

 System.out.printf("%d",minOperations(arr, k)); 

} 

}

 

// This code is contributed by Atul_kumar_Shrivastava  
  
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

 

# Function to return the minimum number of

# increment operations required to make

# any k elements of the array equal

def minOperations(ar, k):

 

 # Sort the array in increasing order

 ar = sorted(ar)

 

 # Calculate the number of operations

 # needed to make 1st k elements equal to

 # the kth element i.e. the 1st window

 opsNeeded = 0

 for i in range(k):

 opsNeeded += ar[k - 1] - ar[i]

 

 # Answer will be the minimum of all

 # possible k sized windows

 ans = opsNeeded

 

 # Find the operations needed to make

 # k elements equal to ith element

 for i in range(k, len(ar)):

 

 # Slide the window to the right and

 # subtract increments spent on leftmost

 # element of the previous window

 opsNeeded = opsNeeded - (ar[i - 1] - ar[i - k])

 

 # Add increments needed to make the 1st k-1

 # elements of this window equal to the

 # kth element of the current window

 opsNeeded += (k - 1) * (ar[i] - ar[i - 1])

 ans = min(ans, opsNeeded)

 

 return ans

 

# Driver code

arr = [3, 1, 9, 100]

n = len(arr)

k = 3

 

print(minOperations(arr, k))

 

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

 

class geeksforgeeks {

 

// Function to return the minimum number of 

// increment operations required to make 

// any k elements of the array equal 

static int minOperations(int[] ar, int k) 

{ 

 // Sort the array in increasing order 

 Array.Sort(ar); 

 

 // Calculate the number of operations 

 // needed to make 1st k elements equal to 

 // the kth element i.e. the 1st window 

 int opsNeeded = 0; 

 for (int i = 0; i < k; i++) { 

 opsNeeded += ar[k - 1] - ar[i]; 

 } 

 

 // Answer will be the minimum of all 

 // possible k sized windows 

 int ans = opsNeeded; 

 

 // Find the operations needed to make 

 // k elements equal to ith element 

 for (int i = k; i < ar.Length; i++) { 

 

 // Slide the window to the right and 

 // subtract increments spent on leftmost 

 // element of the previous window 

 opsNeeded = opsNeeded - (ar[i - 1] - ar[i - k]); 

 

 // Add increments needed to make the 1st k-1 

 // elements of this window equal to the 

 // kth element of the current window 

 opsNeeded += (k - 1) * (ar[i] - ar[i - 1]); 

 ans = Math.Min(ans, opsNeeded); 

 } 

 return ans; 

} 

 

// Driver code 

public static void Main() 

{ 

 int[] arr = { 3, 1, 9, 100 }; 

 int n = arr.Length; 

 int k = 3; 

 

 Console.Write(minOperations(arr, k)); 

} 

}

 

// This code is contributed by AbhiThakur  
  
---  
  
 __

 __

 **Output:**

    
    
    14
    

**Time Complexity:** O(nlogn)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

