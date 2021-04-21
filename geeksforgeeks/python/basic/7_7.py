Minimum steps to make sum and the product of all elements of array non-zero



Given an array **arr** of **N** integers, the task is to find the minimum
steps in which the sum and product of all elements of the array can be made
non-zero. In one step any element of the array can be incremented by 1.

 **Examples:**

>  **Input:** N = 4, arr[] = {0, 1, 2, 3}  
>  **Output:** 1  
>  **Explanation:**  
>  As product of all elements of the array is zero  
> Increment the array element 0 by 1, such that array sum and product is not
> equal to zero.
>
>  **Input:** N = 4, arr[] = {-1, -1, 0, 0}  
>  **Output:** 3  
>  **Explanation:**  
>  As product of all elements of the array is zero  
> Increment the array element 2 and 3 by 1, such that array sum and product is
> not equal to zero

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to break problem into two parts that is –

  

  

  1. Minimum steps required to make the array product not equal to zero.
  2. Minimum steps required to make the array sum not equal to zero.

For the product of all elements of the array not equal to zero, then every
element of the array should be non-zero and to get the array sum not equal to
zero increment any element by 1 if the array sum is zero.

 **For Example:**

    
    
    N = 4, arr[] = {0, 1, 2, 3}
    
    Iterate over the array to find,
    If there is an element that is zero.
    If yes, then increment it by 1 and also
    increment the number of steps by 1.
    
    Again, Iterate over the updated array,
    To check if the array sum is zero. 
    If the array sum of the updated array
    is zero then increment any element by 1. 
    

**Algorithm:**

  * Iterate over the array to check if there is an element which is zero, then increment the element by 1 and also increment the number of steps by 1
  * Again, Iterate over the array and find the sum of the array if the sum of the array is zero then increment any element by 1 and also increment the number of steps by 1.

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

// minimum steps to make the array sum

// and the product not equal to zero

#include <bits/stdc++.h>

using namespace std;

 

int sum(int arr[], int n)

{

 int sum = 0;

 for(int i= 0; i < n; i++)

 sum += arr[i];

 return sum;

} 

 

// Function to to find the 

// minimum steps to make the array sum

// and the product not equal to zero

int steps(int n, int a[])

{

 

 // Variable to store the minimum 

 // number of steps required

 int count_steps = 0;

 

 // Loop to iterate over the array to

 // find if there is any element in 

 // array which is zero

 for(int i = 0; i < n; i++) 

 {

 if(a[i] == 0)

 {

 a[i] += 1;

 count_steps += 1;

 }

 }

 

 // Condition to check if the sum

 // of array elements is zero

 if( sum(a, n) != 0)

 return count_steps;

 else

 return count_steps + 1;

}

 

// Driver code

int main()

{

 int n = 4;

 int a[] = {-1, -1, 0, 0};

 int count = steps(n, a);

 cout<<(count);

 return 0;

}

 

// This code is contributed by Rajput-Ji  
  
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

// minimum steps to make the array sum

// and the product not equal to zero

class GFG

{

 

// Function to to find the 

// minimum steps to make the array sum

// and the product not equal to zero

static int steps(int n, int []a)

{

 

 // Variable to store the minimum 

 // number of steps required

 int count_steps = 0;

 

 // Loop to iterate over the array to

 // find if there is any element in 

 // array which is zero

 for(int i = 0; i < n; i++) 

 {

 if(a[i] == 0)

 {

 a[i] += 1;

 count_steps += 1;

 }

 }

 

 // Condition to check if the sum

 // of array elements is zero

 if( sum(a) != 0)

 return count_steps;

 else

 return count_steps + 1;

}

 

static int sum(int[] arr)

{

 int sum = 0;

 for(int i= 0; i < arr.length; i++)

 sum += arr[i];

 return sum;

}

 

// Driver code

public static void main(String []args) {

 int n = 4;

 int []a = {-1, -1, 0, 0};

 int count = steps(n, a);

 System.out.println(count);

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation to find the

# minimum steps to make the array sum

# and the product not equal to zero

 

# Function to to find the 

# minimum steps to make the array sum

# and the product not equal to zero

def steps(n, a):

 

 # Variable to store the minimum 

 # number of steps required

 count_steps = 0

 

 # Loop to iterate over the array to

 # find if there is any element in 

 # array which is zero

 for i in range(n):

 if a[i]== 0:

 a[i] += 1

 count_steps += 1

 

 # Condition to check if the sum

 # of array elements is zero

 if sum(a)!= 0:

 return count_steps

 else:

 return count_steps + 1

 

# Driver code

if __name__ == "__main__":

 n = 4

 a = [-1, -1, 0, 0]

 count = steps(n, a)

 print(count)  
  
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

// minimum steps to make the array sum

// and the product not equal to zero

using System;

 

class GFG

{

 

// Function to to find the 

// minimum steps to make the array sum

// and the product not equal to zero

static int steps(int n, int []a)

{

 

 // Variable to store the minimum 

 // number of steps required

 int count_steps = 0;

 

 // Loop to iterate over the array to

 // find if there is any element in 

 // array which is zero

 for(int i = 0; i < n; i++) 

 {

 if(a[i] == 0)

 {

 a[i] += 1;

 count_steps += 1;

 }

 }

 

 // Condition to check if the sum

 // of array elements is zero

 if( sum(a) != 0)

 return count_steps;

 else

 return count_steps + 1;

}

 

static int sum(int[] arr)

{

 int sum = 0;

 for(int i= 0; i < arr.Length; i++)

 sum += arr[i];

 return sum;

}

 

// Driver code

public static void Main(String []args) {

 int n = 4;

 int []a = {-1, -1, 0, 0};

 int count = steps(n, a);

 Console.WriteLine(count);

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Performance Analysis:**

  *  **Time Complexity:** In the given approach, there are two iterations to compute the minimum steps required to make the product to non-zero and another iteration to compute the sum of the array. **O(N)**
  *  **Space Complexity:** In the given approach, there is no extra space used. **O(1)**

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

