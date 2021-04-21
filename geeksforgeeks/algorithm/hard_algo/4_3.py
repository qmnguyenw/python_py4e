Find a N-digit number such that it is not divisible by any of its digits



Given an integer N, the task is to find an N-digit number such that it is not
divisible by any of its digits.

 **Note:** There can be multiple answers for each value of N.  
 **Examples:**

>  **Input:** N = 4  
>  **Output:** 6789  
>  **Explanation:**  
>  As the number 6789 is not divisible by any of its digits that is 6, 7, 8
> and 9 and it is also a four digit number, Hence it can be the desired
> number.  
>  **Input:** N = 2  
>  **Output:** 57  
>  **Explanation:**  
>  As the number 57 is not divisible by any of its digits that is 5 and 7 and
> it is also a 2-digit number, Hence it can be the desired number.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The key observation in the problem is that 2 and 3 are those
numbers which don’t divide each other also the numbers “23, 233, 2333, …” are
not divisible by neither 2 nor 3. Hence, for any N-digit number, the most-
significant digit will be 2 and the rest of the digits will be 3 to get the
desired number.

 **Algorithm:**

  

  

  * Check if the value of the N is equal to 1, then there is no such number is possible hence return -1.
  * Otherwise initialize a variable **num** , to store the number by 2.
  * Run a loop from 1 to N and then for each iteration multiply the number by 10 and add 3 to it.
    
    
    num = (num * 10) + 3 
    

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find a

// N-digit number such that the number

// it is not divisible by its digits

 

#include <bits/stdc++.h>

using namespace std;

 

typedef long long int ll;

 

// Function to find the number

// such that it is not divisible

// by its digits

void solve(ll n)

{

 // Base Cases

 if (n == 1)

 {

 cout << -1;

 }

 else {

 

 // First Digit of the

 // number will be 2

 int num = 2;

 

 // Next digits of the numbers

 for (ll i = 0; i < n - 1; i++) {

 num = (num * 10) + 3;

 }

 cout << num;

 }

}

 

// Driver Code

int main()

{

 ll n = 4;

 

 // Function Call

 solve(n);

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

// Java implementation to find a

// N-digit number such that the number

// it is not divisible by its digits

class GFG {

 

 long ll;

 

 // Function to find the number

 // such that it is not divisible

 // by its digits

 static void solve(long n)

 {

 // Base Cases

 if (n == 1)

 {

 System.out.println(-1);

 }

 else {

 

 // First Digit of the

 // number will be 2

 int num = 2;

 

 // Next digits of the numbers

 for (long i = 0; i < n - 1; i++) {

 num = (num * 10) + 3;

 }

 System.out.println(num);

 }

 }

 

 // Driver Code

 public static void main (String[] args)

 {

 long n = 4;

 

 // Function Call

 solve(n);

 }

}

 

// This code is contributed by AnkitRai01  
  
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

# Python3 implementation to find a

# N-digit number such that the number 

# it is not divisible by its digits 

 

# Function to find the number 

# such that it is not divisible 

# by its digits 

def solve(n) : 

 

 # Base Cases 

 if (n == 1) :

 

 print(-1); 

 

 else :

 

 # First Digit of the 

 # number will be 2 

 num = 2; 

 

 # Next digits of the numbers 

 for i in range(n - 1) : 

 num = (num * 10) + 3; 

 

 print(num); 

 

# Driver Code 

if __name__ == "__main__" : 

 

 n = 4; 

 

 # Function Call 

 solve(n); 

 

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

// C# implementation to find a

// N-digit number such that the number

// it is not divisible by its digits

using System;

 

class GFG {

 

 long ll;

 

 // Function to find the number

 // such that it is not divisible

 // by its digits

 static void solve(long n)

 {

 // Base Cases

 if (n == 1)

 {

 Console.WriteLine(-1);

 }

 else {

 

 // First Digit of the

 // number will be 2

 int num = 2;

 

 // Next digits of the numbers

 for (long i = 0; i < n - 1; i++) {

 num = (num * 10) + 3;

 }

 Console.WriteLine(num);

 }

 }

 

 // Driver Code

 public static void Main(String[] args)

 {

 long n = 4;

 

 // Function Call

 solve(n);

 }

}

 

// This code is contributed by sapnasingh4991  
  
---  
  
 __

 __

 **Output:**

    
    
    2333
    

**Performance Analysis:**

  *  **Time Complexity:** O(N).
  *  **Auxiliary Space:** O(1).

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

