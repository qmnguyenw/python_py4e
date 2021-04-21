Sum of all divisors from 1 to N | Set 2



Given a positive integer **N** , the task is to find the sum of divisors of
first **N** natural numbers.

 **Examples:**

>  **Input:** N = 4  
> **Output:** 15  
> **Explanation:**  
> Sum of divisors of 1 = (1)  
> Sum of divisors of 2 = (1+2)  
> Sum of divisors of 3 = (1+3)  
> Sum of divisors of 4 = (1+2+4)  
> Hence, total sum = 1 + (1+2) + (1+3) + (1+2+4) = 15
>
> **Input:** N = 5  
> **Output:** 21  
> **Explanation:**  
> Sum of divisors of 1 = (1)  
> Sum of divisors of 2 = (1+2)  
> Sum of divisors of 3 = (1+3)  
> Sum of divisors of 4 = (1+2+4)  
> Sum of divisors of 5 = (1+5)  
> Hence, total sum = (1) + (1+2) + (1+3) + (1+2+4) + (1+5) = 21

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

For linear time approach, refer to Sum of all divisors from 1 to N

  

  

 **Approach:**  
To optimize the approach in the post mentioned above, we need to look for a
solution with logarithmic complexity. A number **D** is added multiple times
in the final answer. Let us try to observe a pattern of repetitive addition.  
Considering **N** = **12** :D| Number of times added| 1| 12| 2| 6| 3| 4| 5, 6|
2| 7, 8, 9, 10, 11, 12| 1  
---|---  
  
From the above pattern, observe that every number **D** is added ( **N** /
**D** ) times. Also, there are multiple D that have same (N / D). Hence, we
can conclude that for a given **N** , and a particular **i** , numbers from (
**N** / ( **i** \+ **1** )) + **1** to ( **N** / **i** ) will be added **i**
times.

> **Illustration:**  
>
>
>   1. N = 12, i = 1  
> (N/(i+1))+1 = 6+1 = 7 and (N/i) = 12  
> All numbers will be 7, 8, 9, 10, 11, 12 and will be added 1 time only.
>   2. N = 12, i = 2  
> (N/(i+1))+1 = 4+1 = 5 and (N/i) = 6  
> All numbers will be 5, 6 and will be added 2 times.
>

Now, assume **A** = (N / (i + 1)), **B** = (N / i)  
Sum of numbers from A + 1 to B = Sum of numbers from 1 to B – Sum of numbers
from 1 to A  
Also, instead of just incrementing i each time by 1, find next i like this, i
= N/(N/(i+1))

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for

// the above approach

#include<bits/stdc++.h>

using namespace std;

int mod = 1000000007;

 

// Functions returns sum

// of numbers from 1 to n

int linearSum(int n)

{

 return (n * (n + 1) / 2) % mod;

}

 

// Functions returns sum

// of numbers from a+1 to b

int rangeSum(int b, int a)

{

 return (linearSum(b) -

 linearSum(a)) % mod;

}

// Function returns total

// sum of divisors

int totalSum(int n)

{

 

 // Stores total sum

 int result = 0;

 int i = 1;

 

 // Finding numbers and

 //its occurence

 while(true)

 {

 

 // Sum of product of each

 // number and its occurence

 result += rangeSum(n / i, n / (i + 1)) *

 (i % mod) % mod;

 

 result %= mod;

 

 if (i == n)

 break;

 

 i = n / (n / (i + 1));

 }

 return result;

} 

 

// Driver code

int main()

{

 int N = 4;

 cout << totalSum(N) << endl;

 

 N = 12;

 cout << totalSum(N) << endl;

 return 0;

}

// This code is contributed by rutvik_56  
  
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

// the above approach

class GFG{

 

static final int mod = 1000000007;

// Functions returns sum

// of numbers from 1 to n

public static int linearSum(int n)

{

 return (n * (n + 1) / 2) % mod;

}

 

// Functions returns sum

// of numbers from a+1 to b

public static int rangeSum(int b, int a)

{

 return (linearSum(b) -

 linearSum(a)) % mod;

}

 

// Function returns total

// sum of divisors

public static int totalSum(int n)

{

 

 // Stores total sum

 int result = 0;

 int i = 1;

 

 // Finding numbers and

 //its occurence

 while(true)

 {

 

 // Sum of product of each

 // number and its occurence

 result += rangeSum(n / i,

 n / (i + 1)) *

 (i % mod) % mod;

 

 result %= mod;

 

 if (i == n)

 break;

 

 i = n / (n / (i + 1));

 }

 return result;

}

// Driver code

public static void main(String[] args)

{

 int N = 4;

 System.out.println(totalSum(N));

 

 N = 12;

 System.out.println(totalSum(N));

}

}

// This code is contributed by divyeshrabadiya07  
  
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

# the above approach

mod = 1000000007

# Functions returns sum

# of numbers from 1 to n

def linearSum(n):

 return n*(n + 1)//2 % mod

# Functions returns sum

# of numbers from a+1 to b

def rangeSum(b, a):

 return (linearSum(b) - (

 linearSum(a))) % mod

# Function returns total

# sum of divisors

def totalSum(n):

 # Stores total sum

 result = 0

 i = 1

 # Finding numbers and

 # its occurence

 while True:

 

 # Sum of product of each

 # number and its occurence

 result += rangeSum(

 n//i, n//(i + 1)) * (

 i % mod) % mod;

 

 result %= mod;

 if i == n:

 break

 i = n//(n//(i + 1))

 

 return result 

# Driver code

N= 4

print(totalSum(N))

N= 12

print(totalSum(N))  
  
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

// the above approach

using System;

class GFG{

 

static readonly int mod = 1000000007;

// Functions returns sum

// of numbers from 1 to n

public static int linearSum(int n)

{

 return (n * (n + 1) / 2) % mod;

}

 

// Functions returns sum

// of numbers from a+1 to b

public static int rangeSum(int b, int a)

{

 return (linearSum(b) -

 linearSum(a)) % mod;

}

 

// Function returns total

// sum of divisors

public static int totalSum(int n)

{

 

 // Stores total sum

 int result = 0;

 int i = 1;

 

 // Finding numbers and

 //its occurence

 while(true)

 {

 

 // Sum of product of each

 // number and its occurence

 result += rangeSum(n / i,

 n / (i + 1)) *

 (i % mod) % mod;

 

 result %= mod;

 

 if (i == n)

 break;

 

 i = n / (n / (i + 1));

 }

 return result;

}

// Driver code

public static void Main(String[] args)

{

 int N = 4;

 Console.WriteLine(totalSum(N));

 

 N = 12;

 Console.WriteLine(totalSum(N));

}

}

// This code is contributed by Amit Katiyar  
  
---  
  
 __

 __

 **Output:**

    
    
    15
    127
    
    
    
    
    
    
    

_**Time complexity:** O(log N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

