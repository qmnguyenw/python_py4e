Sum of LCM(1, n), LCM(2, n), LCM(3, n), … , LCM(n, n)



Given an integer **n** , the task is to find the sum:

> LCM(1, n) + LCM(2, n) + LCM(3, n) + … + LCM(n, n)  
> where LCM(i, n) is the Least Common Multiple of i and n.

**Examples:**

> **Input:** 3  
> **Output:** 10  
> LCM(1, 3) + LCM(2, 3) + LCM(3, 3) = 3 + 6 + 3 = 12
>
>  **Input:** 5  
> **Output:** 55  
> LCM(1, 5) + LCM(2, 5) + LCM(3, 5) + LCM(4, 5) + LCM(5, 5) = 55
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Naive Approach:** LCM of two numbers **a** and **b** = **(a * b) / gcd(a,
b)** where **gcd(a, b)** is the Greatest Common Divisor of **a** and **b**.

  * Calculate the values of individual LCM for all pairs starting from **(1, n)** to **(n, n)**.
  * Sum all the LCM results from the previous step.
  * Print the **sum** in the end.

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

#define ll long long int

// Function to calculate the required LCM sum

ll lcmSum(long long n)

{

 ll sum = 0;

 for (long long int i = 1; i <= n; i++) {

 // GCD of i and n

 long long int gcd = __gcd(i, n);

 // LCM of i and n i.e. (i * n) / gcd(i, n)

 long long int lcm = (i * n) / gcd;

 // Update sum

 sum = sum + lcm;

 }

 return sum;

}

// Driver code

int main()

{

 int n = 3;

 cout << lcmSum(n);

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

import java.util.*;

class GFG

{

// return gcd of two numbers

static int gcd(int a,int b)

{

 // Everything divides 0

 if (a == 0)

 return b;

 if (b == 0)

 return a;

 

 // base case

 if (a == b)

 return a;

 

 // a is greater

 if (a > b)

 return gcd(a - b, b);

 return gcd(a, b - a);

}

// Function to calculate the required LCM sum

static int lcmSum(int n)

{

 int sum = 0;

 for (int i = 1; i <= n; i++)

 {

 // GCD of i and n

 int gcd = gcd(i, n);

 // LCM of i and n i.e. (i * n) / gcd(i, n)

 int lcm = (i * n) / gcd;

 // Update sum

 sum = sum + lcm;

 }

 return sum;

}

// Driver code

public static void main(String args[])

{

 int n = 3;

 System.out.println(lcmSum(n));

}

}

// This code is contributed by

// Surendra _Gangwar  
  
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

import math

# Function to calculate the required LCM sum

def lcmSum(n):

 Sum = 0

 for i in range(1, n + 1):

 # GCD of i and n

 gcd = math.gcd(i, n)

 # LCM of i and n i.e. (i * n) / gcd(i, n)

 lcm = (i * n) // gcd

 # Update sum

 Sum = Sum + lcm

 return Sum

# Driver code

if __name__ == "__main__":

 n = 3

 print(lcmSum(n))

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

// C# implementation of the approach

class GFG

{

// return gcd of two numbers

static int gcd1(int a,int b)

{

 // Everything divides 0

 if (a == 0)

 return b;

 if (b == 0)

 return a;

 

 // base case

 if (a == b)

 return a;

 

 // a is greater

 if (a > b)

 return gcd1(a - b, b);

 return gcd1(a, b - a);

}

// Function to calculate the required LCM sum

static int lcmSum(int n)

{

 int sum = 0;

 for (int i = 1; i <= n; i++)

 {

 // GCD of i and n

 int gcd = gcd1(i, n);

 // LCM of i and n i.e. (i * n) / gcd(i, n)

 int lcm = (i * n) / gcd;

 // Update sum

 sum = sum + lcm;

 }

 return sum;

}

// Driver code

static void Main()

{

 int n = 3;

 System.Console.WriteLine(lcmSum(n));

}

}

// This code is contributed by chandan_jnu  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP implementation of the approach

function __gcd($a, $b)

{

 if($b == 0)

 return $a;

 return __gcd($b, $a % $b);

}

// Function to calculate the required LCM sum

function lcmSum($n)

{

 $sum = 0;

 for ($i = 1; $i <= $n; $i++)

 {

 // GCD of i and n

 $gcd = __gcd($i, $n);

 // LCM of i and n i.e. (i * n) / gcd(i, n)

 $lcm = ($i * $n) / $gcd;

 // Update sum

 $sum = $sum + $lcm;

 }

 return $sum;

}

// Driver code

$n = 3;

echo lcmSum($n);

// This code is contributed by chandan_jnu

?>  
  
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

// Javascript implementation of the approach

// return gcd of two numbers

function gcd(a, b)

{

 

 // Everything divides 0

 if (a == 0)

 return b;

 if (b == 0)

 return a;

 

 // base case

 if (a == b)

 return a;

 

 // a is greater

 if (a > b)

 return gcd(a - b, b);

 

 return gcd(a, b - a);

}

// Function to calculate the required LCM sum

function lcmSum(n)

{

 var sum = 0;

 for(var i = 1; i <= n; i++)

 {

 // GCD of i and n

 var _gcd = gcd(i, n);

 // LCM of i and n i.e. (i * n) / gcd(i, n)

 var lcm = (i * n) / _gcd;

 // Update sum

 sum = sum + lcm;

 }

 return sum;

}

// Driver code

var n = 3;

document.write(lcmSum(n));

 

// This code is contributed by Ankita saini

 

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    12

**Efficient Approach:** Using Euler Totient Function,  
**∑LCM(i, n) = ((∑(d * ETF(d)) + 1) * n) / 2**  
where **ETF(d)** is Euler totient function of **d** and **d** belongs to the
**set of divisors of n**.

 **Example:**

> Let n be 5 then LCM(1, 5) + LCM(2, 5) + LCM(3, 5) + LCM(4, 5) + LCM(5, 5)  
> = 5 + 10 + 15 + 20 + 5  
> = 55  
> With Euler Totient Function:  
> All divisors of 5 are {1, 5}  
> Hence, ((1*ETF(1) + 5*ETF(5) + 1) * 5) / 2 = 55

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

#define n 1000002

#define ll long long int

ll phi[n + 2], ans[n + 2];

// Euler totient Function

void ETF()

{

 for (int i = 1; i <= n; i++) {

 phi[i] = i;

 }

 for (int i = 2; i <= n; i++) {

 if (phi[i] == i) {

 phi[i] = i - 1;

 for (int j = 2 * i; j <= n; j += i) {

 phi[j] = (phi[j] * (i - 1)) / i;

 }

 }

 }

}

// Function to return the required LCM sum

ll LcmSum(int m)

{

 ETF();

 for (int i = 1; i <= n; i++) {

 // Summation of d * ETF(d) where

 // d belongs to set of divisors of n

 for (int j = i; j <= n; j += i) {

 ans[j] += (i * phi[i]);

 }

 }

 ll answer = ans[m];

 answer = (answer + 1) * m;

 answer = answer / 2;

 return answer;

}

// Driver code

int main()

{

 int m = 5;

 cout << LcmSum(m);

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

 

static int n = 1000002;

static int[] phi = new int[n + 2];

static int[] ans = new int[n + 2];

// Euler totient Function

static void ETF()

{

 for (int i = 1; i <= n; i++)

 {

 phi[i] = i;

 }

 for (int i = 2; i <= n; i++)

 {

 if (phi[i] == i)

 {

 phi[i] = i - 1;

 for (int j = 2 * i; j <= n; j += i)

 {

 phi[j] = (phi[j] * (i - 1)) / i;

 }

 }

 }

}

// Function to return the required LCM sum

static int LcmSum(int m)

{

 ETF();

 for (int i = 1; i <= n; i++)

 {

 // Summation of d * ETF(d) where

 // d belongs to set of divisors of n

 for (int j = i; j <= n; j += i)

 {

 ans[j] += (i * phi[i]);

 }

 }

 int answer = ans[m];

 answer = (answer + 1) * m;

 answer = answer / 2;

 return answer;

}

// Driver code

public static void main (String[] args)

{

 int m = 5;

 System.out.println(LcmSum(m));

}

}

// This code is contributed by chandan_jnu  
  
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

n = 100002;

phi = [0] * (n + 2);

ans = [0] * (n + 2);

# Euler totient Function

def ETF():

 for i in range(1, n + 1):

 phi[i] = i;

 for i in range(2, n + 1):

 if (phi[i] == i):

 phi[i] = i - 1;

 for j in range(2 * i, n + 1, i):

 phi[j] = (phi[j] * (i - 1)) // i;

# Function to return the required LCM sum

def LcmSum(m):

 ETF();

 for i in range(1, n + 1):

 # Summation of d * ETF(d) where

 # d belongs to set of divisors of n

 for j in range(i, n + 1, i):

 ans[j] += (i * phi[i]);

 answer = ans[m];

 answer = (answer + 1) * m;

 answer = answer // 2;

 return answer;

# Driver code

m = 5;

print(LcmSum(m));

# This code is contributed

# by chandan_jnu  
  
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

static int n = 1000002;

static int[] phi = new int[n + 2];

static int[] ans = new int[n + 2];

// Euler totient Function

static void ETF()

{

 for (int i = 1; i <= n; i++)

 {

 phi[i] = i;

 }

 for (int i = 2; i <= n; i++)

 {

 if (phi[i] == i)

 {

 phi[i] = i - 1;

 for (int j = 2 * i; j <= n; j += i)

 {

 phi[j] = (phi[j] * (i - 1)) / i;

 }

 }

 }

}

// Function to return the required LCM sum

static int LcmSum(int m)

{

 ETF();

 for (int i = 1; i <= n; i++)

 {

 // Summation of d * ETF(d) where

 // d belongs to set of divisors of n

 for (int j = i; j <= n; j += i)

 {

 ans[j] += (i * phi[i]);

 }

 }

 int answer = ans[m];

 answer = (answer + 1) * m;

 answer = answer / 2;

 return answer;

}

// Driver code

static void Main()

{

 int m = 5;

 Console.WriteLine(LcmSum(m));

}

}

// This code is contributed by chandan_jnu  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP implementation of the approach

$n = 10002;

$phi = array_fill(0, $n + 2, 0);

$ans = array_fill(0, $n + 2, 0);

// Euler totient Function

function ETF()

{

 global $phi, $n;

 for ($i = 1; $i <= $n; $i++)

 {

 $phi[$i] = $i;

 }

 for ($i = 2; $i <= $n; $i++)

 {

 if ($phi[$i] == $i)

 {

 $phi[$i] = $i - 1;

 for ($j = 2 * $i; $j <= $n; $j += $i)

 {

 $phi[$j] = (int)(($phi[$j] *

 ($i - 1)) / $i);

 }

 }

 }

}

// Function to return the required LCM sum

function LcmSum($m)

{

 ETF();

 global $ans, $n, $phi;

 

 for ($i = 1; $i <= $n; $i++)

 {

 // Summation of d * ETF(d) where

 // d belongs to set of divisors of n

 for ($j = $i; $j <= $n; $j += $i)

 {

 $ans[$j] += ($i * $phi[$i]);

 }

 }

 $answer = $ans[$m];

 $answer = ($answer + 1) * $m;

 $answer = (int)($answer / 2);

 return $answer;

}

// Driver code

$m = 5;

echo LcmSum($m);

// This code is contributed by chandan_jnu

?>  
  
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

// javascript implementation of the approach 

var n = 1000002;

 var phi = Array(n + 2).fill(0);

 var ans = Array(n + 2).fill(0);

 // Euler totient Function

 function ETF() {

 for (i = 1; i <= n; i++) {

 phi[i] = i;

 }

 for (i = 2; i <= n; i++) {

 if (phi[i] == i) {

 phi[i] = i - 1;

 for (j = 2 * i; j <= n; j += i) {

 phi[j] = (phi[j] * (i - 1)) / i;

 }

 }

 }

 }

 // Function to return the required LCM sum

 function LcmSum(m) {

 ETF();

 for (i = 1; i <= n; i++) {

 // Summation of d * ETF(d) where

 // d belongs to set of divisors of n

 for (j = i; j <= n; j += i) {

 ans[j] += (i * phi[i]);

 }

 }

 var answer = ans[m];

 answer = (answer + 1) * m;

 answer = answer / 2;

 return answer;

 }

 // Driver code

 var m = 5;

 document.write(LcmSum(m));

// This code is contributed by aashish1995

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    55

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

