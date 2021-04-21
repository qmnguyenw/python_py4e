Floor square root without using sqrt() function : Recursive



Given a number **N** , the task is to find the floor square root of the number
N without using the built-in square root function. **Floor square root** of a
number is the greatest whole number which is less than or equal to its square
root.

 **Examples:**

>  **Input:** N = 25  
>  **Output:** 5  
>  **Explanation:**  
>  Square root of 25 = 5. Therefore 5 is the greatest whole number less than
> equal to Square root of 25.
>
>  **Input:** N = 30  
>  **Output:** 5  
>  **Explanation:**  
>  Square root of 25 = 5.47  
> Therefore 5 is the greatest whole number less than equal to Square root of
> 25 (5.47)

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 _ **Naive Approach:**_  
In the basic approach to find the floor square root of a number, find the
square of numbers from **1 to N** , till the square of some number **K**
becomes greater than **N**. Hence the value of **(K – 1)** will be the floor
square root of N.

  

  

Below is the algorithm to solve this problem using Naive approach:

  * Iterate a loop from numbers 1 to N in K.
  * For any K, if its square becomes greater than N, then K-1 is the floor square root of N.

 **Time Complexity:** O(√N)

 _ **Efficient Approach:**_  
From the Naive approach, it is clear that the floor square root of N will lie
in the range [1, N]. Hence instead of checking each number in this range, we
can **efficiently search the required number in this range**. Therefore, the
idea is to use the binary search in order to efficiently find the floor square
root of the number N in **log N**.

Below is the recursive algorithm to solve the above problem using Binary
Search:

  1. Implement the Binary Search in the range 0 to N.
  2. Find the mid value of the range using formula:
    
    
    mid = (start + end) / 2
    

  3. **Base Case:** The recursive call will get executed till square of mid is less than or equal to N and the square of (mid+1) is greater than equal to N.
    
    
    (mid2 ≤ N) and ((mid + 1)2 > N)
    

  4. If the base case is not satisfied, then the range will get changed accordingly.
    * If the square of mid is less than equal to N, then the range gets updated to [mid + 1, end]
        
        
        if(mid2 ≤ N)
            updated range = [mid + 1, end]
        

    * If the square of mid is greater than N, then the range gets updated to [low, mid + 1]
        
        
        if(mid2 > N)
            updated range = [low, mid - 1]
        

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// square root of the number N

// without using sqrt() function

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the square

// root of the number N using BS

int sqrtSearch(int low, int high, int N)

{

 

 // If the range is still valid

 if (low <= high) {

 

 // Find the mid-value of the range

 int mid = (low + high) / 2;

 

 // Base Case

 if ((mid * mid <= N)

 && ((mid + 1) * (mid + 1) > N)) {

 return mid;

 }

 

 // Condition to check if the

 // left search space is useless

 else if (mid * mid < N) {

 return sqrtSearch(mid + 1, high, N);

 }

 else {

 return sqrtSearch(low, mid - 1, N);

 }

 }

 return low;

}

 

// Driver Code

int main()

{

 int N = 25;

 cout << sqrtSearch(0, N, N)

 << endl;

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

// Java implementation to find the

// square root of the number N

// without using sqrt() function

class GFG {

 

 // Function to find the square

 // root of the number N using BS

 static int sqrtSearch(int low, int high, int N)

 {

 

 // If the range is still valid

 if (low <= high) {

 

 // Find the mid-value of the range

 int mid = (int)(low + high) / 2;

 

 // Base Case

 if ((mid * mid <= N)

 && ((mid + 1) * (mid + 1) > N)) {

 return mid;

 }

 

 // Condition to check if the

 // left search space is useless

 else if (mid * mid < N) {

 return sqrtSearch(mid + 1, high, N);

 }

 else {

 return sqrtSearch(low, mid - 1, N);

 }

 }

 return low;

 }

 

 // Driver Code

 public static void main (String[] args)

 {

 int N = 25;

 System.out.println(sqrtSearch(0, N, N));

 }

}

 

// This code is contributed by Yash_R  
  
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

# Python3 implementation to find the

# square root of the number N 

# without using sqrt() function 

 

# Function to find the square 

# root of the number N using BS 

def sqrtSearch(low, high, N) : 

 

 # If the range is still valid 

 if (low <= high) :

 

 # Find the mid-value of the range 

 mid = (low + high) // 2; 

 

 # Base Case 

 if ((mid * mid <= N) and ((mid + 1) * (mid +
1) > N)) :

 return mid; 

 

 # Condition to check if the 

 # left search space is useless 

 elif (mid * mid < N) : 

 return sqrtSearch(mid + 1, high, N); 

 

 else :

 return sqrtSearch(low, mid - 1, N); 

 

 return low; 

 

# Driver Code 

if __name__ == "__main__" : 

 

 N = 25; 

 print(sqrtSearch(0, N, N)) 

 

# This code is contributed by Yash_R  
  
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

// C# implementation to find the

// square root of the number N

// without using sqrt() function

using System;

 

class GFG {

 

 // Function to find the square

 // root of the number N using BS

 static int sqrtSearch(int low, int high, int N)

 {

 

 // If the range is still valid

 if (low <= high) {

 

 // Find the mid-value of the range

 int mid = (int)(low + high) / 2;

 

 // Base Case

 if ((mid * mid <= N)

 && ((mid + 1) * (mid + 1) > N)) {

 return mid;

 }

 

 // Condition to check if the

 // left search space is useless

 else if (mid * mid < N) {

 return sqrtSearch(mid + 1, high, N);

 }

 else {

 return sqrtSearch(low, mid - 1, N);

 }

 }

 return low;

 }

 

 // Driver Code

 public static void Main(String[] args)

 {

 int N = 25;

 Console.WriteLine(sqrtSearch(0, N, N));

 }

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

**Performance Analysis:**

  *  **Time Complexity:** As in the above approach, there is Binary Search used over the search space of 0 to N which takes O(log N) time in worst case, Hence the Time Complexity will be **O(log N)**.
  *  **Space Complexity:** As in the above approach, taking consideration of the stack space used in the recursive calls which can take O(logN) space in worst case, Hence the space complexity will be **O(log N)**

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

