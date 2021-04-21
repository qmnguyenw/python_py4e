Check whether an array can be made strictly decreasing by modifying at most
one element



Given an array **arr[]** of positive integers, the task is to find whether it
is possible to make this array strictly decreasing by modifying at most one
element.  
 **Examples:**

> **Input:** arr[] = {12, 9, 10, 5, 2}  
> **Output:** Yes  
> {12, 11, 10, 5, 2} is one of the valid solutions.  
>  **Input:** arr[] = {1, 2, 3, 4}  
> **Output:** No

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** For every element **arr[i]** , if it is greater than both
**arr[i – 1]** and **arr[i + 1]** or it is smaller than both arr[i – 1] and
arr[i + 1] then arr[i] needs to be modified.  
i.e **arr[i] = (arr[i – 1] + arr[i + 1]) / 2**. If after modification,
**arr[i] = arr[i – 1]** or **arr[i + 1]** then the array cannot be made
strictly decreasing without affecting **at most** one element else count all
such modifications, if the count of modifications in the end is less than or
equal to **1** then print **Yes** else print **No**.  
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

using namespace std;

// Function that returns true if the array

// can be made strictly decreasing

// with at most one change

bool check(int* arr, int n)

{

 // To store the number of modifications

 // required to make the array

 // strictly decreasing

 int modify = 0;

 // Check whether the last element needs

 // to be modify or not

 if (arr[n - 1] >= arr[n - 2]) {

 arr[n - 1] = arr[n - 2] - 1;

 modify++;

 }

 // Check whether the first element needs

 // to be modify or not

 if (arr[0] <= arr[1]) {

 arr[0] = arr[1] + 1;

 modify++;

 }

 // Loop from 2nd element to the 2nd last element

 for (int i = n - 2; i > 0; i--) {

 // Check whether arr[i] needs to be modified

 if ((arr[i - 1] <= arr[i] && arr[i + 1] <= arr[i])

 || (arr[i - 1] >= arr[i] && arr[i + 1] >= arr[i])) {

 // Modifying arr[i]

 arr[i] = (arr[i - 1] + arr[i + 1]) / 2;

 modify++;

 // Check if arr[i] is equal to any of

 // arr[i-1] or arr[i+1]

 if (arr[i] == arr[i - 1] || arr[i] == arr[i + 1])

 return false;

 }

 }

 // If more than 1 modification is required

 if (modify > 1)

 return false;

 return true;

}

// Driver code

int main()

{

 int arr[] = { 10, 5, 11, 2 };

 int n = sizeof(arr) / sizeof(arr[0]);

 if (check(arr, n))

 cout << "Yes";

 else

 cout << "No";

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

class GFG {

 // Function that returns true if the array

 // can be made strictly decreasing

 // with at most one change

 public static boolean check(int[] arr, int n)

 {

 // To store the number of modifications

 // required to make the array

 // strictly decreasing

 int modify = 0;

 // Check whether the last element needs

 // to be modify or not

 if (arr[n - 1] >= arr[n - 2]) {

 arr[n - 1] = arr[n - 2] - 1;

 modify++;

 }

 // Check whether the first element needs

 // to be modify or not

 if (arr[0] <= arr[1]) {

 arr[0] = arr[1] + 1;

 modify++;

 }

 // Loop from 2nd element to the 2nd last element

 for (int i = n - 2; i > 0; i--) {

 // Check whether arr[i] needs to be modified

 if ((arr[i - 1] <= arr[i] && arr[i + 1] <= arr[i])

 || (arr[i - 1] >= arr[i] && arr[i + 1] >= arr[i])) {

 // Modifying arr[i]

 arr[i] = (arr[i - 1] + arr[i + 1]) / 2;

 modify++;

 // Check if arr[i] is equal to any of

 // arr[i-1] or arr[i+1]

 if (arr[i] == arr[i - 1] || arr[i] == arr[i + 1])

 return false;

 }

 }

 // If more than 1 modification is required

 if (modify > 1)

 return false;

 return true;

 }

 // Driver code

 public static void main(String[] args)

 {

 int[] arr = { 10, 5, 11, 3 };

 int n = arr.length;

 if (check(arr, n))

 System.out.print("Yes");

 else

 System.out.print("No");

 }

}  
  
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

# Function that returns true if the array

# can be made strictly decreasing

# with at most one change

def check(arr, n):

 modify = 0

 

 # Check whether the last element needs

 # to be modify or not

 if (arr[n - 1] >= arr[n - 2]):

 arr[n-1] = arr[n-2] - 1

 modify += 1

 

 # Check whether the first element needs

 # to be modify or not

 if (arr[0] <= arr[1]):

 arr[0] = arr[1] + 1

 modify += 1

 # Loop from 2nd element to the 2nd last element

 for i in range(n-2, 0, -1):

 # Check whether arr[i] needs to be modified

 if (arr[i - 1] <= arr[i] and arr[i + 1] <=
arr[i]) or \

 (arr[i - 1] >= arr[i] and arr[i + 1] >= arr[i]):

 # Modifying arr[i]

 arr[i] = (arr[i - 1] + arr[i + 1]) // 2

 modify += 1

 

 # Check if arr[i] is equal to any of

 # arr[i-1] or arr[i + 1]

 if (arr[i] == arr[i - 1] or arr[i] == arr[i +
1]):

 return False

 # If more than 1 modification is required

 if (modify > 1):

 return False

 return True

# Driver code

if __name__ == "__main__":

 arr = [10, 5, 11, 3]

 n = len(arr)

 if (check(arr, n)):

 print("Yes")

 else:

 print("No")  
  
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

 

 // Function that returns true if the array

 // can be made strictly decreasing

 // with at most one change

 public static bool check(int[]arr, int n)

 {

 // To store the number of modifications

 // required to make the array

 // strictly decreasing

 int modify = 0;

 // Check whether the last element needs

 // to be modify or not

 if (arr[n - 1] >= arr[n - 2])

 {

 arr[n - 1] = arr[n - 2] - 1;

 modify++;

 }

 // Check whether the first element needs

 // to be modify or not

 if (arr[0] <= arr[1])

 {

 arr[0] = arr[1] + 1;

 modify++;

 }

 // Loop from 2nd element to the 2nd last element

 for (int i = n - 2; i > 0; i--)

 {

 // Check whether arr[i] needs to be modified

 if ((arr[i - 1] <= arr[i] && arr[i + 1] <= arr[i])

 || (arr[i - 1] >= arr[i] && arr[i + 1] >= arr[i]))

 {

 // Modifying arr[i]

 arr[i] = (arr[i - 1] + arr[i + 1]) / 2;

 modify++;

 // Check if arr[i] is equal to any of

 // arr[i-1] or arr[i+1]

 if (arr[i] == arr[i - 1] || arr[i] == arr[i + 1])

 return false;

 }

 }

 // If more than 1 modification is required

 if (modify > 1)

 return false;

 return true;

 }

 // Driver code

 static public void Main ()

 {

 int[]arr = { 10, 5, 11, 3 };

 int n = arr.Length;

 if (check(arr, n))

 Console.Write("Yes");

 else

 Console.Write("No");

 }

}

// This code is contributed by ajit.  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

