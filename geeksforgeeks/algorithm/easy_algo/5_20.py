Code Optimization Technique (logical AND and logical OR)



While using && (logical AND), we must put the condition first whose
probability of getting **false** is high so that compiler doesn’t need to
check the second condition if the first condition is false.

 __

 __  
 __

 __

 __  
 __  
 __

#include<iostream.h>

 

// Function to check whether n is odd

bool isOdd(int n);

 

// Function to check whether n is prime

bool isPrime(int n);

 

int main()

{

 int cnt = 0, n = 10;

 

 // Implementation 1

 for (int i = 2; i <= n; i++) {

 if (isOdd(i) && isPrime(i))

 cnt++;

 }

 

 cnt = 0;

 n = 10;

 

 // Implementation 2

 for (int i = 2; i <= n; i++) {

 if (isPrime(i) && isOdd(i))

 cnt++;

 }

}  
  
---  
  
 __

 __

Consider the above implementation:

>  **In implementation 1** , we avoid checking even numbers whether they are
> prime or not as primality test requires more computation than checking a
> number for even/odd.  
> Probability of a number getting odd is more than of it being a prime that’s
> why we first check whether the number is odd before checking it for prime.

> On the other hand **in implementation 2** , we are checking whether the
> number is prime or not before checking whether it is odd which makes
> unnecessary computation as all even numbers other than **2** are not prime
> but the implementation still checks them for prime.

## Logical OR (||)

While using || (logical OR), we must put the condition first whose probability
of getting **true** is high so that compiler doesn’t need to check the second
condition if the first condition is true.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

#include<iostream.h>

 

// Function to check whether n is odd

bool isEven(int n);

 

// Function to check whether n is prime

bool isPrime(int n);

 

int main()

{

 int cnt = 0, n = 10;

 

 // Implementation 1

 for (int i = 3; i <= n; i++) {

 if (isEven(i) || !isPrime(i))

 cnt++;

 }

}  
  
---  
  
 __

 __

> As described earlier that the probability of a number being even is more
> than that of it being a non-prime. The current order of execution of the
> statements doesn’t allow even numbers greater than 2 to be checked whether
> they are non-prime (as they are all non-primes).

 **Note:** For larger inputs, the order of the execution of statements can
affect the overall execution time for the program.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

