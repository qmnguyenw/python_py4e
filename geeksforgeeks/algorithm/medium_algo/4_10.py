Check if a number can be expressed as a product of exactly K prime divisors



Given an **integer N** , the task is to check if it can be expressed as a
product of exactly **K** prime divisors.  
**Examples:**  

    
    
    **Input:** N = 12, K = 3
    **Output:** Yes
    **Explanation:**
    12 can be expressed as product of 2×2×3.
    
    **Input:** N = 14, K = 3
    **Output:**  No
    **Explanation:**
    14 can be only expressed as product of 2×7.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
To solve the problem mentioned above we are given the value N and we will find
the **maximum number of values we can split N into**. We can represent prime
factorization of **N** as ![\\prod_{i=1}^{K} {p_{i}}^{a_{i}}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-9233dd742deafc147475ed3babba8095_l3.png)where _p i_ are
the prime factors of **N** and _a i_ are the exponents. We know that total
number of divisors of **N** is ![\\prod_{i=1}^{K} \(a_{i}+1\)
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d9e67b215bef85d5666f4558dfb4013e_l3.png). Therefore, we
can observe that we have to check whether it is possible to represent **N** as
product of **K** numbers or not. If the maximum split is less than K then it
is not possible to express it in exactly K prime divisors, else it is always
possible.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP implementation to Check if a

// number can be expressed as a

// product of exactly K prime divisors

#include <bits/stdc++.h>

using namespace std;

// function to find K prime divisors

void KPrimeDivisors(int N, int K)

{

 int maximum_split = 0;

 // count number of 2s that divide N

 while (N % 2 == 0) {

 maximum_split++;

 N /= 2;

 }

 // N must be odd at this point.

 // So we can skip one element

 for (int i = 3; i * i <= N; i = i + 2) {

 while (N % i == 0) {

 // divide the value of N

 N = N / i;

 // increment count

 maximum_split++;

 }

 }

 // Condition to handle the case when n

 // is a prime number greater than 2

 if (N > 2)

 maximum_split++;

 // check if maximum_split is less than K

 // then it not possible

 if (maximum_split < K) {

 printf("No\n");

 return;

 }

 printf("Yes\n");

}

/* Driver code */

int main()

{

 // initialise N and K

 int N = 12;

 int K = 3;

 KPrimeDivisors(N, K);

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

// Java implementation to Check if a

// number can be expressed as a

// product of exactly K prime divisors

class GFG {

 

 // function to find K prime divisors

 static void KPrimeDivisors(int N, int K)

 {

 int maximum_split = 0;

 

 // count number of 2s that divide N

 while (N % 2 == 0) {

 maximum_split++;

 N /= 2;

 }

 

 // N must be odd at this point.

 // So we can skip one element

 for (int i = 3; i * i <= N; i = i + 2) {

 

 while (N % i == 0) {

 // divide the value of N

 N = N / i;

 

 // increment count

 maximum_split++;

 }

 }

 

 // Condition to handle the case when n

 // is a prime number greater than 2

 if (N > 2)

 maximum_split++;

 

 // check if maximum_split is less than K

 // then it not possible

 if (maximum_split < K) {

 System.out.println("No");

 return;

 }

 

 System.out.println("Yes");

 }

 

 /* Driver code */

 public static void main (String[] args)

 {

 // initialise N and K

 int N = 12;

 int K = 3;

 

 KPrimeDivisors(N, K);

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

# Python implementation to Check if a

# number can be expressed as a

# product of exactly K prime divisors

import math as mt

# function to find K prime divisors

def KPrimeDivisors(n, k):

 

 # To count maximum split of N

 maximum_split = 0

 

 # count number of 2s that divide N

 while n % 2 == 0:

 maximum_split+= 1

 n = n // 2

 

 # n must be odd at this point

 # so we skip one element

 for i in range(3, mt.ceil(mt.sqrt(n)), 2):

 while n % i == 0:

 n = n / i;

 maximum_split+= 1

 

 # Condition to handle the case when n

 # is a prime number greater than 2

 if n > 2:

 maximum_split+= 1

 

 # check if maximum_split is less than K

 # then it not possible

 if maximum_split < k:

 print("No")

 return

 print("Yes")

 

 

# Driver code

N = 12

K = 3

KPrimeDivisors(N, K)  
  
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

// C# implementation to Check if a

// number can be expressed as a

// product of exactly K prime divisors

using System;

class GFG {

 

 // function to find K prime divisors

 static void KPrimeDivisors(int N, int K)

 {

 int maximum_split = 0;

 

 // count number of 2s that divide N

 while (N % 2 == 0) {

 maximum_split++;

 N /= 2;

 }

 

 // N must be odd at this point.

 // So we can skip one element

 for (int i = 3; i * i <= N; i = i + 2) {

 

 while (N % i == 0) {

 // divide the value of N

 N = N / i;

 

 // increment count

 maximum_split++;

 }

 }

 

 // Condition to handle the case when n

 // is a prime number greater than 2

 if (N > 2)

 maximum_split++;

 

 // check if maximum_split is less than K

 // then it not possible

 if (maximum_split < K) {

 Console.WriteLine("No");

 return;

 }

 

 Console.WriteLine("Yes");

 }

 

 /* Driver code */

 public static void Main(String[] args)

 {

 // initialise N and K

 int N = 12;

 int K = 3;

 

 KPrimeDivisors(N, K);

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

// javascript implementation to Check if a

// number can be expressed as a

// product of exactly K prime divisors 

// function to find K prime divisors

 function KPrimeDivisors(N , K)

 {

 var maximum_split = 0;

 // count number of 2s that divide N

 while (N % 2 == 0)

 {

 maximum_split++;

 N /= 2;

 }

 // N must be odd at this point.

 // So we can skip one element

 for (i = 3; i * i <= N; i = i + 2)

 {

 while (N % i == 0)

 {

 

 // divide the value of N

 N = N / i;

 // increment count

 maximum_split++;

 }

 }

 // Condition to handle the case when n

 // is a prime number greater than 2

 if (N > 2)

 maximum_split++;

 // check if maximum_split is less than K

 // then it not possible

 if (maximum_split < K)

 {

 document.write("No");

 return;

 }

 document.write("Yes");

 }

 /* Driver code */

 

 // initialise N and K

 var N = 12;

 var K = 3;

 KPrimeDivisors(N, K);

// This code is contributed by gauravrajput1.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

**Time Complexity:** O(sqrt(N))  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

