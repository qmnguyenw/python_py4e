Minimum operations required to convert X to Y by multiplying X with the given
co-primes



Given four integers **X** , **Y** , **P** and **Q** such that **X ≤ Y** and
**gcd(P, Q) = 1**. The task is to find minimum operation required to convert
**X** to **Y**. In a single operation, you can multiply **X** with either
**P** or **Q**. If it is not possible to convert **X** to **Y** then print
**-1**.

 **Examples:**

>  **Input:** X = 12, Y = 2592, P = 2, Q = 3  
>  **Output:** 6  
> (12 * 2) -> (24 * 3) -> (72 * 2) -> (144 * 3) -> (432 * 3) -> (1296 * 2)
> ->2592
>
>  **Input:** X = 7, Y = 9, P = 2, Q = 7  
>  **Output:** -1  
> There is no way we can reach 9 from 7 by  
> multiplying 7 with either 2 or 7

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** If **Y** is not divisible by **X** then no integral
multiplication of any integer with **X** any number of times can lead to **Y**
and the result is **-1**.  
Else, let **d = Y / X**. Now, **P a * Qb = d** must hold in order to have a
valid solution and the result in that case will be **(a + b)** else **-1** if
**d** cannot be expressed in the powers of **P** and **Q**.  
In order to check the condition, keep dividing **d** with **P** and **Q**
until divisible. Now, if **d = 1** in the end then the solution is possible
else not.

  

  

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

// operations required

int minOperations(int x, int y, int p, int q)

{

 

 // Not possible

 if (y % x != 0)

 return -1;

 

 int d = y / x;

 

 // To store the greatest power

 // of p that divides d

 int a = 0;

 

 // While divible by p

 while (d % p == 0) {

 d /= p;

 a++;

 }

 

 // To store the greatest power

 // of q that divides d

 int b = 0;

 

 // While divible by q

 while (d % q == 0) {

 d /= q;

 b++;

 }

 

 // If d > 1

 if (d != 1)

 return -1;

 

 // Since, d = p^a * q^b

 return (a + b);

}

 

// Driver code

int main()

{

 int x = 12, y = 2592, p = 2, q = 3;

 

 cout << minOperations(x, y, p, q);

 

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

 // operations required 

 static int minOperations(int x, int y, int p, int q) 

 { 

 

 // Not possible 

 if (y % x != 0) 

 return -1; 

 

 int d = y / x; 

 

 // To store the greatest power 

 // of p that divides d 

 int a = 0; 

 

 // While divible by p 

 while (d % p == 0) 

 { 

 d /= p; 

 a++; 

 } 

 

 // To store the greatest power 

 // of q that divides d 

 int b = 0; 

 

 // While divible by q 

 while (d % q == 0)

 { 

 d /= q; 

 b++; 

 } 

 

 // If d > 1

 if (d != 1) 

 return -1; 

 

 // Since, d = p^a * q^b 

 return (a + b); 

 } 

 

 // Driver code 

 public static void main (String[] args) 

 {

 int x = 12, y = 2592, p = 2, q = 3; 

 System.out.println(minOperations(x, y, p, q)); 

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

# Python3 implementation of the approach

 

# Function to return the minimum

# operations required

def minOperations(x, y, p, q):

 

 # Not possible

 if (y % x != 0):

 return -1

 

 d = y // x

 

 # To store the greatest power

 # of p that divides d

 a = 0

 

 # While divible by p

 while (d % p == 0):

 d //= p

 a+=1

 

 # To store the greatest power

 # of q that divides d

 b = 0

 

 # While divible by q

 while (d % q == 0):

 d //= q

 b+=1

 

 # If d > 1

 if (d != 1):

 return -1

 

 # Since, d = p^a * q^b

 return (a + b)

 

 

# Driver code

 

x = 12

y = 2592

p = 2

q = 3

 

print(minOperations(x, y, p, q))

 

# This code is contributed by mohit kumar 29  
  
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

 // operations required 

 static int minOperations(int x, int y, int p, int q) 

 { 

 

 // Not possible 

 if (y % x != 0) 

 return -1; 

 

 int d = y / x; 

 

 // To store the greatest power 

 // of p that divides d 

 int a = 0; 

 

 // While divible by p 

 while (d % p == 0) 

 { 

 d /= p; 

 a++; 

 } 

 

 // To store the greatest power 

 // of q that divides d 

 int b = 0; 

 

 // While divible by q 

 while (d % q == 0)

 { 

 d /= q; 

 b++; 

 } 

 

 // If d > 1

 if (d != 1) 

 return -1; 

 

 // Since, d = p^a * q^b 

 return (a + b); 

 } 

 

 // Driver code 

 public static void Main () 

 {

 int x = 12, y = 2592, p = 2, q = 3; 

 Console.Write(minOperations(x, y, p, q)); 

 }

}

 

// This code is contributed by anuj_67..  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

