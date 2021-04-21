Python program to check whether a number is Prime or not



Given a positive integer N, The task is to write a Python program to check if
the number is prime or not.  
 **Definition:** A prime number is a natural number greater than 1 that has no
positive divisors other than 1 and itself. The first few prime numbers are {2,
3, 5, 7, 11, ….}.

 **Examples :**

>  **Input:** n = 11  
>  **Output:** true
>
>  **Input:** n = 15  
>  **Output:** false
>
>  **Input:** n = 1  
>  **Output:** false
>
>  
>
>
>  
>

The idea to solve this problem is to iterate through all the numbers starting
from 2 to (N/2) using a for loop and for every number check if it divides N.
If we find any number that divides, we return false. If we did not find any
number between 2 and N/2 which divides N then it means that N is prime and we
will return True.

Below is the Python program to check if a number is prime:

## C

 __

 __  
 __

 __

 __  
 __  
 __

// C program for

// the above approach

#include <stdio.h>

int main()

{

 // Given number

 int n = 11;

 // checking the given number

 // whether it is 1 or not

 if (n == 1) {

 printf("%d is not a prime number", n);

 }

 else {

 int f = 0;

 // iterate from 2 to n/2

 for (int i = 2; i <= (n / 2); i++) {

 

 // If n is divisible by any number between

 // 2 and n/2, it is not prime

 if (n % 2 == 0) {

 f = 1;

 

 // break out of for loop as

 // it is not prime

 break;

 }

 }

 if (f == 1) {

 printf("%d is not a prime number", n);

 }

 else {

 printf("%d is a prime number", n);

 }

 }

 return 0;

}

// This Code is Contributed by

// Murarishetty Santhosh Charan  
  
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

# Python program to check if

# given number is prime or not

num = 11

# If given number is greater than 1

if num > 1:

 # Iterate from 2 to n / 2

 for i in range(2, int(num/2)+1):

 # If num is divisible by any number between

 # 2 and n / 2, it is not prime

 if (num % i) == 0:

 print(num, "is not a prime number")

 break

 else:

 print(num, "is a prime number")

else:

 print(num, "is not a prime number")  
  
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

// C++ program for

// the above approach

#include <bits/stdc++.h>

using namespace std;

int main() {

 // Given number

 int n=11;

 // checking the given number

 // whether it is 1 or not

 if(n==1)

 {

 cout<<n<<" is not a prime number";

 }

 else

 {

 int f=0;

 // iterate from 2 to n/2

 for(int i=2;i<=(n/2);i++)

 {

 // If n is divisible by any number between

 // 2 and n/2, it is not prime

 if(n%2==0)

 {

 f=1;

 // break out of for loop as

 // it is not prime

 break;

 }

 }

 if(f==1)

 {

 cout<<n<<" is not a prime number";

 }

 else

 {

 cout<<n<<" is a prime number";

 }

 }

 return 0;

}

// This code is contributed by

// Murarishetty Santhosh Charan  
  
---  
  
 __

 __

 **Output**

    
    
    11 is a prime number

 **Optimized Method**  
We can do the following optimizations:

  1. Instead of checking till n, we can check till √n because a larger factor of n must be a multiple of a smaller factor that has been already checked.
  2. The algorithm can be improved further by observing that all primes are of the form 6k ± 1, with the exception of 2 and 3. This is because all integers can be expressed as (6k + i) for some integer k and for i = ?1, 0, 1, 2, 3, or 4; 2 divides (6k + 0), (6k + 2), (6k + 4); and 3 divides (6k + 3). So a more efficient method is to test if n is divisible by 2 or 3, then to check through all the numbers of form 6k ± 1. (Source: wikipedia)

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A optimized school method based

# Python3 program to check

# if a number is prime

def isPrime(n) :

 # Corner cases

 if (n <= 1) :

 return False

 if (n <= 3) :

 return True

 # This is checked so that we can skip

 # middle five numbers in below loop

 if (n % 2 == 0 or n % 3 == 0) :

 return False

 i = 5

 while(i * i <= n) :

 if (n % i == 0 or n % (i + 2) == 0) :

 return False

 i = i + 6

 return True

# Driver Program

if (isPrime(11)) :

 print(" true")

else :

 print(" false")

 

if(isPrime(15)) :

 print(" true")

else :

 print(" false")

 

 

# This code is contributed

# by Nikita Tiwari.  
  
---  
  
 __

 __

 **Output:**

    
    
     true
     false

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

