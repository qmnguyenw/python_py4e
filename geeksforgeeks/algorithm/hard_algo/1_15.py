Fast Doubling method to find the Nth Fibonacci number



Given an integer **N** , the task is to find the N-th Fibonacci numbers.  
 **Examples:**  

> **Input:** N = 3  
> **Output:** 2  
> **Explanation:**  
> F(1) = 1, F(2) = 1  
> F(3) = F(1) + F(2) = 2  
> **Input:** N = 6  
> **Output:** 8  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  

  * The Matrix Exponentiation Method is already discussed before. The Doubling Method can be seen as an improvement to the matrix exponentiation method to find the N-th Fibonacci number although it doesn’t use matrix multiplication itself.  

  * The Fibonacci recursive sequence is given by   

    
    
    **F(n+1) = F(n) + F(n-1)**

  * The Matrix Exponentiation method uses the following formula

![\\\[ \\begin{bmatrix} 1 & 1 \\\\ 1 & 0 \\end{bmatrix}^n = \\begin{bmatrix}
F_{n+1} & F_n \\\\ F_n & F_{n-1} \\end{bmatrix} \\\]
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f6a8435619fa6c35910ff14f57ef7391_l3.png)

  

  

  * The method involves costly matrix multiplication and moreover Fn is redundantly computed twice.  
On the other hand, Fast Doubling Method is based on two basic formulas:  

    
    
    **F(2n) = F(n)[2F(n+1) – F(n)]**
    **F(2n + 1) = F(n) 2 + F(n+1)2**

  * Here is a short explanation of the above results:  

> **Start with:**  
>  F(n+1) = F(n) + F(n-1) &  
> F(n) = F(n)  
> It can be rewritten in the matrix form as:
>
> ![\\\[ \\begin{bmatrix} F\(n+1\) \\\\ F\(n\) \\end{bmatrix} =
> \\begin{bmatrix} 1 & 1 \\\\ 1 & 0 \\end{bmatrix} \\begin{bmatrix} F\(n\)
> \\\\ F\(n-1\) \\end{bmatrix} \\\] \\\[\\quad\\enspace= \\begin{bmatrix} 1 &
> 1 \\\\ 1 & 0 \\end{bmatrix}^2 \\begin{bmatrix} F\(n-1\) \\\\ F\(n-2\)
> \\end{bmatrix} \\\]
> \\quad\\quad\\quad\\quad\\quad\\quad\\quad\\quad\\quad\\quad\\quad\\enspace\\enspace\\thinspace......\\\\
> \\\[= \\begin{bmatrix} 1 & 1 \\\\ 1 & 0 \\end{bmatrix}^n \\begin{bmatrix}
> F\(1\) \\\\ F\(0\) \\end{bmatrix} \\\]  ](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-06ad1ff3486776725bef290b928f784c_l3.png)
>
> For doubling, we just plug in “2n” into the formula:
>
> ![\\\[ \\begin{bmatrix} F\(2n+1\) \\\\ F\(2n\) \\end{bmatrix} =
> \\begin{bmatrix} 1 & 1 \\\\ 1 & 0 \\end{bmatrix}^{2n} \\begin{bmatrix}
> F\(1\) \\\\ F\(0\) \\end{bmatrix} \\\] \\\[\\quad\\enspace= \\begin{bmatrix}
> 1 & 1 \\\\ 1 & 0 \\end{bmatrix}^n \\begin{bmatrix} 1 & 1 \\\\ 1 & 0
> \\end{bmatrix}^n \\begin{bmatrix} F\(1\) \\\\ F\(0\) \\end{bmatrix} \\\]
> \\\[\\quad\\enspace= \\begin{bmatrix} F\(n+1\) & F\(n\) \\\\ F\(n\) &
> F\(n-1\) \\end{bmatrix} \\begin{bmatrix} F\(n+1\) & F\(n\) \\\\ F\(n\) &
> F\(n-1\) \\end{bmatrix} \\begin{bmatrix} F\(1\) \\\\ F\(0\) \\end{bmatrix}
> \\\] \\\[\\quad\\enspace= \\begin{bmatrix} F\(n+1\)^2 + F\(n\)^2 \\\\
> F\(n\)F\(n+1\) + F\(n\)F\(n-1\) \\end{bmatrix} \\\]
> ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
> aba024c65f956e17c8dfbc1baa1d0571_l3.png)
>
> Substituting F(n-1) = F(n+1)- F(n) and after simplification we get,
>
> ![\\\[ \\begin{bmatrix} F\(2n+1\) \\\\ F\(2n\) \\end{bmatrix} =
> \\begin{bmatrix} F\(n+1\)^2 + F\(n\)^2 \\\\ 2F\(n+1\)F\(n\) - F\(n\)^2
> \\end{bmatrix} \\\]  ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-c628efb192c7f9d0bca59bf6d0605efc_l3.png)

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the Nth Fibonacci

// number using Fast Doubling Method

#include <bits/stdc++.h>

using namespace std;

int a, b, c, d;

#define MOD 1000000007

// Function calculate the N-th fibanacci

// number using fast doubling method

void FastDoubling(int n, int res[])

{

 // Base Condition

 if (n == 0) {

 res[0] = 0;

 res[1] = 1;

 return;

 }

 FastDoubling((n / 2), res);

 // Here a = F(n)

 a = res[0];

 // Here b = F(n+1)

 b = res[1];

 c = 2 * b - a;

 if (c < 0)

 c += MOD;

 // As F(2n) = F(n)[2F(n+1) – F(n)]

 // Here c = F(2n)

 c = (a * c) % MOD;

 // As F(2n + 1) = F(n)^2 + F(n+1)^2

 // Here d = F(2n + 1)

 d = (a * a + b * b) % MOD;

 // Check if N is odd

 // or even

 if (n % 2 == 0) {

 res[0] = c;

 res[1] = d;

 }

 else {

 res[0] = d;

 res[1] = c + d;

 }

}

// Driver code

int main()

{

 int N = 6;

 int res[2] = { 0 };

 FastDoubling(N, res);

 cout << res[0] << "\n";

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

// Java program to find the Nth Fibonacci

// number using Fast Doubling Method

class GFG{

// Function calculate the N-th fibanacci

// number using fast doubling method

static void FastDoubling(int n, int []res)

{

 int a, b, c, d;

 int MOD = 1000000007;

 

 // Base Condition

 if (n == 0)

 {

 res[0] = 0;

 res[1] = 1;

 return;

 }

 FastDoubling((n / 2), res);

 // Here a = F(n)

 a = res[0];

 // Here b = F(n+1)

 b = res[1];

 c = 2 * b - a;

 if (c < 0)

 c += MOD;

 // As F(2n) = F(n)[2F(n+1) – F(n)]

 // Here c = F(2n)

 c = (a * c) % MOD;

 // As F(2n + 1) = F(n)^2 + F(n+1)^2

 // Here d = F(2n + 1)

 d = (a * a + b * b) % MOD;

 // Check if N is odd

 // or even

 if (n % 2 == 0)

 {

 res[0] = c;

 res[1] = d;

 }

 else

 {

 res[0] = d;

 res[1] = c + d;

 }

}

// Driver code

public static void main(String []args)

{

 int N = 6;

 int res[] = new int[2];

 FastDoubling(N, res);

 System.out.print(res[0]);

}

}

// This code is contributed by rock_cool  
  
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

# Python3 program to find the Nth Fibonacci

# number using Fast Doubling Method

MOD = 1000000007

# Function calculate the N-th fibanacci

# number using fast doubling method

def FastDoubling(n, res):

 

 # Base Condition

 if (n == 0):

 res[0] = 0

 res[1] = 1

 return

 

 FastDoubling((n // 2), res)

 # Here a = F(n)

 a = res[0]

 # Here b = F(n+1)

 b = res[1]

 c = 2 * b - a

 if (c < 0):

 c += MOD

 # As F(2n) = F(n)[2F(n+1) – F(n)]

 # Here c = F(2n)

 c = (a * c) % MOD

 # As F(2n + 1) = F(n)^2 + F(n+1)^2

 # Here d = F(2n + 1)

 d = (a * a + b * b) % MOD

 # Check if N is odd

 # or even

 if (n % 2 == 0):

 res[0] = c

 res[1] = d

 else :

 res[0] = d

 res[1] = c + d

 

# Driver code

N = 6

res = [0] * 2

FastDoubling(N, res)

print(res[0])

 

# This code is contributed by divyamohan123  
  
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

// C# program to find the Nth Fibonacci

// number using Fast Doubling Method

using System;

class GFG{

// Function calculate the N-th fibanacci

// number using fast doubling method

static void FastDoubling(int n, int []res)

{

 int a, b, c, d;

 int MOD = 1000000007;

 

 // Base Condition

 if (n == 0)

 {

 res[0] = 0;

 res[1] = 1;

 return;

 }

 FastDoubling((n / 2), res);

 // Here a = F(n)

 a = res[0];

 // Here b = F(n+1)

 b = res[1];

 c = 2 * b - a;

 if (c < 0)

 c += MOD;

 // As F(2n) = F(n)[2F(n+1) – F(n)]

 // Here c = F(2n)

 c = (a * c) % MOD;

 // As F(2n + 1) = F(n)^2 + F(n+1)^2

 // Here d = F(2n + 1)

 d = (a * a + b * b) % MOD;

 // Check if N is odd

 // or even

 if (n % 2 == 0)

 {

 res[0] = c;

 res[1] = d;

 }

 else

 {

 res[0] = d;

 res[1] = c + d;

 }

}

// Driver code

public static void Main()

{

 int N = 6;

 int []res = new int[2];

 FastDoubling(N, res);

 Console.Write(res[0]);

}

}

// This code is contributed by Code_Mech  
  
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

 // Javascript program to find the Nth Fibonacci

 // number using Fast Doubling Method

 

 let a, b, c, d;

 let MOD = 1000000007;

 // Function calculate the N-th fibanacci

 // number using fast doubling method

 function FastDoubling(n, res)

 {

 // Base Condition

 if (n == 0) {

 res[0] = 0;

 res[1] = 1;

 return;

 }

 FastDoubling(parseInt(n / 2, 10), res);

 // Here a = F(n)

 a = res[0];

 // Here b = F(n+1)

 b = res[1];

 c = 2 * b - a;

 if (c < 0)

 c += MOD;

 // As F(2n) = F(n)[2F(n+1) – F(n)]

 // Here c = F(2n)

 c = (a * c) % MOD;

 // As F(2n + 1) = F(n)^2 + F(n+1)^2

 // Here d = F(2n + 1)

 d = (a * a + b * b) % MOD;

 // Check if N is odd

 // or even

 if (n % 2 == 0) {

 res[0] = c;

 res[1] = d;

 }

 else {

 res[0] = d;

 res[1] = c + d;

 }

 }

 let N = 6;

 let res = new Array(2);

 res.fill(0);

 

 FastDoubling(N, res);

 

 document.write(res[0]);

 

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    8

**Time Complexity:** Repeated squaring reduces time from linear to logarithmic
. Hence, with constant time arithmetic, the time complexity is **O(log n)**.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

