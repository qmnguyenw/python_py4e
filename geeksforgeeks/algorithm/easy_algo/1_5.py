Abstraction of Binary Search



 **What is the binary search algorithm?**  
 **Binary Search** Algorithm is used to find a certain value of **x** for
which a certain defined function **f(x)** needs to be maximized or minimized.
It is frequently used to search an element in a sorted sequence by repeatedly
dividing the search interval into halves. Begin with an interval covering the
whole sequence, if the value of the search key is less than the item in the
middle of the interval, then search in the left half of the interval otherwise
search in the right half. Repeatedly check until the value is found or the
interval is empty.  
The main condition to perform a Binary Search is that the sequence must be
monotonous i.e., it must be either increasing or decreasing.

> **Monotonic function**  
> A function f(x) is said to be monotonic if and only if for any x if _f(x)_
> returns true, then for any value of y (where y > x) should also return true
> and similarly if for a certain value of x for which _f(x)_ is false, then
> for any value z (z < x) the function should also return false.  
>

**How to solve a question using Binary Search:**  
If the function is

![f\(x\) = x^{2}         ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-350f710e4466063044bcb0dcc7764ca0_l3.png)

And the task is to find the maximum value of **x** such that **f(x)** is less
than or equal to the **target value**. The interval in which we will search
the target value for the given

  

  

![f\(x\)         ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-95375e3472df6e1fc67a1cbc187a3e77_l3.png)

is from **0 to target value**.  
Then we can use binary search for this problem since the function

![f\(x\) = x^{2}         ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-350f710e4466063044bcb0dcc7764ca0_l3.png)

is a monotonically increasing function.

> **Target** = 17  
> f(x) = x2, since the function is monotonic binary search can be applied to
> it.  
> Range of search interval will be [0, target]  
>  **Step 1:**  
>  low = 0, high = 17, calculate mid = (low + high)/2 = 8  
> Calculate f(8) = 64 which is more than target, so it will return false and
> high will be updated as high = mid – 1 = 7.  
>  **Steps 2:**  
> low = 0, high = 7, calculate mid = (low + high)/2 = 3  
> Calculate f(3) = 9 which is less than target, so it will return true and low
> will be updated as low = mid + 1 = 4.  
>  **Step 3:**  
> low = 4, high = 7, calculate mid = (low + high)/2 = 5  
> Calculate f(5) = 25 which is more than target, so it will return false and
> high will be updated as high = mid – 1 = 4.  
>  **Step 4:**  
> Now since the range [low, high] converges to a single point i.e 4 so the
> final result is found, since f(4) = 16 which is the maximum value of the
> given function less than target.  
>

Below is the implementation of the above example:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above example

 

#include "bits/stdc++.h"

using namespace std;

 

// Function to find X such that it is

// less than the target value and function

// is f(x) = x^2

void findX(int targetValue)

{

 

 // Initialise start and end

 int start = 0, end = targetValue;

 int mid, result;

 

 // Loop till start <= end

 while (start <= end) {

 

 // Find the mid

 mid = start + (end - start) / 2;

 

 // Check for the left half

 if (mid * mid <= targetValue) {

 

 // Store the result

 result = mid;

 

 // Reinitialize the start point

 start = mid + 1;

 }

 

 // Check for the right half

 else {

 end = mid - 1;

 }

 }

 

 // Print the maximum value of x

 // such that x^2 is less than the

 // targetValue

 cout << result << endl;

}

 

// Driver Code

int main()

{

 // Given targetValue;

 int targetValue = 81;

 

 // Function Call

 findX(targetValue);

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

// Java program for

// the above example

import java.util.*;

class GFG{

 

// Function to find X such

// that it is less than the

// target value and function

// is f(x) = x^2

static void findX(int targetValue)

{

 

 // Initialise start and end

 int start = 0, end = targetValue;

 int mid = 0, result = 0;

 

 // Loop till start <= end

 while (start <= end) 

 {

 

 // Find the mid

 mid = start + (end - start) / 2;

 

 // Check for the left half

 if (mid * mid <= targetValue) 

 {

 

 // Store the result

 result = mid;

 

 // Reinitialize the start point

 start = mid + 1;

 }

 

 // Check for the right half

 else

 {

 end = mid - 1;

 }

 }

 

 // Print the maximum value of x

 // such that x^2 is less than the

 // targetValue

 System.out.print(result + "\n");

}

 

// Driver Code

public static void main(String[] args)

{

 

 // Given targetValue;

 int targetValue = 81;

 

 // Function call

 findX(targetValue);

}

}

 

// This code is contributed by 29AjayKumar  
  
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

# Python3 program for

# the above example

 

# Function to find X such

# that it is less than the

# target value and function

# is f(x) = x ^ 2

def findX(targetValue):

 

 # Initialise start and end

 start = 0;

 end = targetValue;

 mid = 0;

 

 # Loop till start <= end

 while (start <= end):

 

 # Find the mid

 mid = start + (end - start) // 2;

 

 # Check for the left half

 if (mid * mid <= targetValue):

 result = mid

 start = mid + 1;

 

 # Check for the right half

 else:

 end = mid - 1;

 

 # Print maximum value of x

 # such that x ^ 2 is less than the

 # targetValue

 print(result);

 

# Driver Code

if __name__ == '__main__':

 

 # Given targetValue;

 targetValue = 81;

 

 # Function Call

 findX(targetValue);

 

# This code is contributed by Rajput-Ji  
  
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

// C# program for

// the above example

using System;

class GFG{

 

// Function to find X such

// that it is less than the

// target value and function

// is f(x) = x^2

static void findX(int targetValue)

{

 

 // Initialise start and end

 int start = 0, end = targetValue;

 int mid = 0, result = 0;

 

 // Loop till start <= end

 while (start <= end)

 {

 

 // Find the mid

 mid = start + (end - start) / 2;

 

 // Check for the left half

 if (mid * mid <= targetValue)

 {

 

 // Store the result

 result = mid;

 

 // Reinitialize the start point

 start = mid + 1;

 }

 

 // Check for the right half

 else

 {

 end = mid - 1;

 }

 }

 

 // Print the maximum value of x

 // such that x^2 is less than the

 // targetValue

 Console.Write(result + "\n");

}

 

// Driver Code

public static void Main(String[] args)

{

 

 // Given targetValue;

 int targetValue = 81;

 

 // Function Call

 findX(targetValue);

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    9

The above binary search algorithm requires at most **O(log N)** comparisons to
find the maximum value less than or equal to the target value. And the value
of the function f(x) = x2 doesn’t need to be evaluated many times.  
 _ **Time Complexity:** O(logN) _  
_**Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

