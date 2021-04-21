Minimum value of K such that sum of cubes of first K natural number is greater
than equal to N



Given a number **N** , the task is to find the minimum value **K** such that
the sum of cubes of the first **K** natural number is greater than or equal to
**N**.  
**Examples:**  

> **Input:** N = 100  
> **Output:** 4  
> **Explanation:**  
> The sum of cubes of first 4 natural number is 100 which is equal to N = 100  
>  **Input:** N = 15  
> **Output:** 3  
> **Explanation:**  
> The sum of cubes of first 2 natural number is 9 which is lesser than K = 15
> and sum of first  
> 3 natural number is 36 which is just greater than K. So the answer is 3.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The naive approach for this problem is to run a loop from
and find the sum of cubes. Whenever the sum exceeds the value of N, break from
the loop.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to determine the

// minimum value of K such that the

// sum of cubes of first K

// natural number is greater than

// or equal to N

#include <bits/stdc++.h>

using namespace std;

// Function to determine the

// minimum value of K such that the

// sum of cubes of first K

// natural number is greater than

// or equal to N

int naive_find_x(int N)

{

 // Variable to store the

 // sum of cubes

 int c = 0, i;

 // Loop to find the number

 // K

 for(i = 1; i < N; i++)

 {

 c += i * i * i;

 

 // If C is just greater then

 // N, then break the loop

 if (c >= N)

 break;

 }

 return i;

}

// Driver code

int main()

{

 int N = 100;

 cout << naive_find_x(N);

 return 0;

}

// This code is contributed by sapnasingh4991  
  
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

// Java program to determine the

// minimum value of K such that the

// sum of cubes of first K

// natural number is greater than

// or equal to N

class GFG {

 

// Function to determine the

// minimum value of K such that the

// sum of cubes of first K

// natural number is greater than

// or equal to N

static int naive_find_x(int N)

{

 // Variable to store the

 // sum of cubes

 int c = 0, i;

 // Loop to find the number

 // K

 for(i = 1; i < N; i++)

 {

 c += i * i * i;

 

 // If C is just greater then

 // N, then break the loop

 if (c >= N)

 break;

 }

 return i;

}

// Driver code

public static void main(String[] args)

{

 int N = 100;

 

 System.out.println(naive_find_x(N));

}

}

// This code is contributed by sapnasingh4991  
  
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

# Python3 program to determine the

# minimum value of K such that the

# sum of cubes of first K

# natural number is greater than

# or equal to N

# Function to determine the

# minimum value of K such that the

# sum of cubes of first K

# natural number is greater than

# or equal to N

def naive_find_x(N):

 # Variable to store the

 # sum of cubes

 c = 0

 # Loop to find the number

 # K

 for i in range(1, N):

 c += i*i*i

 # If C is just greater then

 # N, then break the loop

 if c>= N:

 break

 return i

# Driver code

if __name__ == "__main__":

 

 N = 100

 print(naive_find_x(N))  
  
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

// C# program to determine the

// minimum value of K such that the

// sum of cubes of first K

// natural number is greater than

// or equal to N

using System;

class GFG {

 

// Function to determine the

// minimum value of K such that the

// sum of cubes of first K

// natural number is greater than

// or equal to N

static int naive_find_x(int N)

{

 // Variable to store the

 // sum of cubes

 int c = 0, i;

 // Loop to find the number

 // K

 for(i = 1; i < N; i++)

 {

 c += i * i * i;

 

 // If C is just greater then

 // N, then break the loop

 if (c >= N)

 break;

 }

 return i;

}

// Driver code

public static void Main(String[] args)

{

 int N = 100;

 

 Console.WriteLine(naive_find_x(N));

}

}

// This code is contributed by 29AjayKumar  
  
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

// javascript program to determine the

// minimum value of K such that the

// sum of cubes of first K

// natural number is greater than

// or equal to N

// Function to determine the

// minimum value of K such that the

// sum of cubes of first K

// natural number is greater than

// or equal to N

function naive_find_x(N)

{

 // Variable to store the

 // sum of cubes

 var c = 0, i;

 // Loop to find the number

 // K

 for(i = 1; i < N; i++)

 {

 c += i * i * i;

 

 // If C is just greater then

 // N, then break the loop

 if (c >= N)

 break;

 }

 return i;

}

// Driver code

var N = 100;

document.write(naive_find_x(N));

// This code is contributed by Amit Katiyar

</script>  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    4

