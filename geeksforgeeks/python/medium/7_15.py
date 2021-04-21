Check whether count of odd and even factors of a number are equal



Given a number **N** , the task is to find whether N has an equal number of
odd and even factors.  
 **Examples:**

> **Input:** N = 10  
> **Output:** YES  
> **Explanation:** 10 has two odd factors (1 and 5) and two even factors (2
> and 10)
>
>  **Input:** N = 24  
> **Output:** NO  
> **Explanation:** 24 has two odd factors (1 and 3) and six even factors (2,
> 4, 6, 8 12 and 24)
>
>  **Input:** N = 125  
> **Output:** NO

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**Find all the divisors and check whether count of odd
divisors is same as count of even divisors.  
Below is the implementation of the above approach

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ solution for the above approach

#include <bits/stdc++.h>

using namespace std;

#define lli long long int

 

// Function to check condition

void isEqualFactors(lli N)

{

 // Initialize even_count

 // and od_count

 lli ev_count = 0, od_count = 0;

 

 // loop runs till square root

 for (lli i = 1;

 i <= sqrt(N) + 1; i++) {

 

 if (N % i == 0) {

 if (i == N / i) {

 if (i % 2 == 0)

 ev_count += 1;

 else

 od_count += 1;

 }

 

 else {

 if (i % 2 == 0)

 ev_count += 1;

 else

 od_count += 1;

 

 if ((N / i) % 2 == 0)

 ev_count += 1;

 

 else

 od_count += 1;

 }

 }

 }

 

 if (ev_count == od_count)

 cout << "YES" << endl;

 else

 cout << "NO" << endl;

}

 

// Driver Code

int main()

{

 lli N = 10;

 isEqualFactors(N);

 

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

// Java solution for the above approach

class GFG{

 

// Function to check condition

static void isEqualFactors(int N)

{

 

 // Initialize even_count

 // and od_count

 int ev_count = 0, od_count = 0;

 

 // Loop runs till square root

 for(int i = 1; 

 i <= Math.sqrt(N) + 1; i++)

 {

 if (N % i == 0)

 {

 if (i == N / i)

 {

 if (i % 2 == 0)

 ev_count += 1;

 else

 od_count += 1;

 }

 else

 {

 if (i % 2 == 0)

 ev_count += 1;

 else

 od_count += 1;

 

 if ((N / i) % 2 == 0)

 ev_count += 1;

 else

 od_count += 1;

 }

 }

 }

 

 if (ev_count == od_count)

 System.out.print("YES" + "\n");

 else

 System.out.print("NO" + "\n");

}

 

// Driver Code

public static void main(String[] args)

{

 int N = 10;

 

 isEqualFactors(N);

}

}

 

// This code is contributed by amal kumar choubey  
  
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

# Python3 code for the naive approach

import math

 

# Function to check condition

def isEqualFactors(N):

 

# Initialize even_count

# and od_count

 ev_count = 0

 od_count = 0

 

# loop runs till square root

 for i in range(1, (int)(math.sqrt(N)) + 2) :

 if (N % i == 0):

 if(i == N // i):

 if(i % 2 == 0):

 ev_count += 1

 else:

 od_count += 1

 

 else:

 if(i % 2 == 0):

 ev_count += 1

 else:

 od_count += 1

 

 if((N // i) % 2 == 0):

 ev_count += 1;

 else:

 od_count += 1;

 

 if (ev_count == od_count):

 print("YES")

 else:

 print("NO")

 

# Driver Code

N = 10

isEqualFactors(N)  
  
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

// C# solution for the above approach

using System;

 

class GFG{

 

// Function to check condition

static void isEqualFactors(int N)

{

 

 // Initialize even_count

 // and od_count

 int ev_count = 0, od_count = 0;

 

 // Loop runs till square root

 for(int i = 1; 

 i <= Math.Sqrt(N) + 1; i++)

 {

 if (N % i == 0)

 {

 if (i == N / i)

 {

 if (i % 2 == 0)

 ev_count += 1;

 else

 od_count += 1;

 }

 else

 {

 if (i % 2 == 0)

 ev_count += 1;

 else

 od_count += 1;

 

 if ((N / i) % 2 == 0)

 ev_count += 1;

 else

 od_count += 1;

 }

 }

 }

 

 if (ev_count == od_count)

 Console.Write("YES" + "\n");

 else

 Console.Write("NO" + "\n");

}

 

// Driver Code

public static void Main(String[] args)

{

 int N = 10;

 

 isEqualFactors(N);

}

}

 

// This code is contributed by gauravrajput1  
  
---  
  
 __

 __

 **Output:**

    
    
    YES
    

_**Time Complexity:** O(sqrt(N)) _  
_**Auxiliary Space:** O(1)_

 **Efficient Solution:**  
The following observation must be made to optimize the above approach:

  * According to **Unique Factorisation Theorem** any number can be expressed in terms of the product of the power of primes. So, N can be expressed as :   
  

> N = P1A1 * P2A2 * P3A3 * …….. * PkAK where, each Pi is a prime and each Ai
> is a positive integer.(1 <= i <= K)

  * Using law of combinators any divisor of N would be of the form :   

> N = P1B1 * P2B2 * P3B3 * …….. * PKBK where Bi is an integer and 0 <= Bi <=
> Ai for 1 <= i <= K.

  * A divisor would be odd if it dosen’t contain 2 in its prime factorisation. So, if P1 = 2 then B1 must be **0**. It can be done in only 1 way.
  * For even divisors, B1 can be replaced by 1 (or) 2 (or)….A1 to get a divisor. It can be done in B1 ways.
  * Now for others each Bi can be replaced either with 0 (or) 1 (or) 2….(or) Ai for 1 <= i <= K. It can be done in (Ai+1) ways.
  * By Fundamental principle : 
    * **Number of odd divisors** are: **X** = 1 * (A2+1) * (A3+1) * ….. * (AK+1).
    * Similarly, **Number of even divisors** are: **Y** = A1 * (A2+1) * (A3+1) * …. * (AK+1).
  * For no. of even divisors to be equal to no. of odd divisors X, Y should be equal. This is possible only when **A 1 = 1**.

So, it can be concluded that number of even and odd divisors of a number are
equal, **if it has 1 (and only 1) power of 2 in its prime factorisation.**  
Follow the steps below to solve the problem:

  1. For a given number N, check if it is divisible by 2.
  2. If the number is divisible by 2, then check if it is divisible by 22. If yes, then the number won’t have an equal number of odd and even factors. If not, then the number will have an equal number of odd and even factors.
  3. If the number is not divisible by 2, then the number will never have any even factor and thus it won’t have an equal number of odd and even factors.

Below is the implementation of the above approach.

## C

 __

 __  
 __

 __

 __  
 __  
 __

// C code for the above approach

#include <stdio.h>

#define lli long long int

 

// Function to check condition

void isEqualFactors(lli N)

{

 if ((N % 2 == 0)

 && (N % 4 != 0))

 printf("YES\n");

 else

 printf("NO\n");

}

 

// Driver Code

int main()

{

 lli N = 10;

 isEqualFactors(N);

 

 N = 125;

 isEqualFactors(N);

 

 return 0;

}  
  
---  
  
 __

 __

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code for the above approach

#include <bits/stdc++.h>

using namespace std;

#define lli long long int

 

// Function to check condition

void isEqualFactors(lli N)

{

 if ((N % 2 == 0)

 and (N % 4 != 0))

 cout << "YES" << endl;

 else

 cout << "NO" << endl;

}

 

// Driver Code

int main()

{

 lli N = 10;

 isEqualFactors(N);

 

 N = 125;

 isEqualFactors(N);

 

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

// JAVA code for the above approach

public class GFG {

 

 // Function to check condition

 static void isEqualFactors(int N)

 {

 if ((N % 2 == 0)

 && (N % 4 != 0))

 System.out.println("YES");

 

 else

 System.out.println("NO");

 }

 

 // Driver code

 public static void main(String args[])

 {

 int N = 10;

 isEqualFactors(N);

 

 N = 125;

 isEqualFactors(N);

 }

}  
  
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

# Python code for the above approach

 

# Function to check condition

def isEqualFactors(N):

 if ( ( N % 2 == 0 ) and ( N % 4 != 0) ):

 print("YES")

 else:

 print("NO")

 

# Driver Code

N = 10

isEqualFactors(N)

 

N = 125;

isEqualFactors(N)  
  
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

// C# code for the above approach

using System;

 

class GFG {

 

 // Function to check condition

 static void isEqualFactors(int N)

 {

 if ((N % 2 == 0)

 && (N % 4 != 0))

 Console.WriteLine("YES");

 

 else

 Console.WriteLine("NO");

 }

 

 // Driver code

 public static void Main()

 {

 int N = 10;

 isEqualFactors(N);

 

 N = 125;

 isEqualFactors(N);

 }

}  
  
---  
  
 __

 __

 **Output:**

    
    
    YES
    NO
    

_**Time Complexity:** O(1) _  
_**Auxiliary Space:** O(1)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

