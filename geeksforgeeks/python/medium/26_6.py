Analysis of Different Methods to find Prime Number in Python



If you participate in the competitive programming, you might be familiar with
the fact that questions related to Prime numbers are one of the choices of the
problem setter. Here, we will discuss how to optimize your function which
checks for the Prime number in the given set of range and will also calculate
the timings to execute them.  
Going by definition, a Prime number is a positive integer which is divisible
only by itself and 1. For example: 2,3,5,7. But if a number is can be factored
into smaller numbers, it is called Composite number. For example: 4=2*2, 6=2*3  
And the integer 1 is neither a prime number nor a composite number. Checking
that a number is prime is easy but efficiently checking needs some effort.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Method 1**  
Let us now go with the very first function to check whether a number, say n,
is prime or not. In this method, we will test all divisors from 2 to n-1. We
will skip 1 and n. If n is divisible by any of the divisor, the function will
return False, else True.  
Following are the steps used in this method:

  1. If the integer is less than equal to 1, it returns False.
  2. If the given number is divisible by any of the numbers from 2 to n, the function will return False
  3. Else it will return True

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to find prime numbers in a range

import time

def is_prime(n):

 if n <= 1:

 return False

 for i in range(2,n):

 if n % i == 0:

 return False

 return True

# Driver function

t0 = time.time()

c = 0 #for counting

for n in range(1,100000):

 x = is_prime(n)

 c += x

print("Total prime numbers in range :", c)

t1 = time.time()

print("Time required :", t1 - t0)  
  
---  
  
 __

 __

 **Output:**

    
    
    Total prime numbers in range: 9592
    Time required: 60.702312707901

In the above code, we check all the numbers from 1 to 100000 whether those
numbers are prime or not. It has a huge runtime as shown. It takes around 1
minute to run. This is a simple approach but takes a lot of time to run. So,
it is not preferred in competitive programming.

 **Method 2**  
In this method, we use a simple trick by reducing the number of divisors we
check for. We have found that there is a fine line which acts as the mirror as
shows the factorization below the line and factorization above the line just
in reverse order. The line which divided the factors into two halves is the
line of the square root of the number. If the number is a perfect square, we
can shift the line by 1 and if we can get the integer value of the line which
divides.

  

  

    
    
    36=1*36          
      =2*18
      =3*12
      =4*9
    ------------
      =6*6
    ------------
      =9*4
      =12*3
      =18*2
      =36*1

In this function, we calculate an integer, say max_div, which is the square
root of the number and get its floor value using the math library of Python.
In the last example, we iterate from 2 to n-1. But in this, we reduce the
divisors by half as shown. You need to import the math module to get the floor
and sqrt function.  
Following are the steps used in this method:

  1. If the integer is less than equal to 1, it returns False.
  2. Now, we reduce the numbers which needs to be checked to the square root of the given number.
  3. If the given number is divisible by any of the numbers from 2 to the square root of the number, the function will return False
  4. Else it will return True

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to find prime numbers in a range

import math

import time

def is_prime(n):

 if n <= 1:

 return False

 max_div = math.floor(math.sqrt(n))

 for i in range(2, 1 + max_div):

 if n % i == 0:

 return False

 return True

# Driver function

t0 = time.time()

c = 0 #for counting

for n in range(1,100000):

 x = is_prime(n)

 c += x

print("Total prime numbers in range :", c)

t1 = time.time()

print("Time required :", t1 - t0)  
  
---  
  
 __

 __

 **Output:**

    
    
    Total prime numbers in range: 9592
    Time required: 0.4116342067718506

In the above code, we check all the numbers from 1 to 100000 whether those
numbers are prime or not. It takes comparatively lesser time than the previous
method. This is a bit tricky approach but makes a huge difference in the
runtime of the code. So, it is more preferred in competitive programming.  
**Method 3**  
Now, we will optimize our code to next level which takes lesser time than the
previous method. You might have noticed that in the last example, we iterated
through every even number up to the limit which was a waste. The thing to
notice is that all the even numbers except two can not be prime number. In
this method, we kick out all the even numbers to optimize our code and will
check only the odd divisors.  
Following are the steps used in this method:

  1. If the integer is less than equal to 1, it returns False.
  2. If the number is equal to 2, it will return True.
  3. If the number is greater than 2 and divisible by 2, then it will return False.
  4. Now, we have checked all the even numbers. Now, look for the odd numbers.
  5. If the given number is divisible by any of the numbers from 3 to the square root of the number skipping all the even numbers, the function will return False
  6. Else it will return True

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to find prime numbers in a range

import math

import time

def is_prime(n):

 if n <= 1:

 return False

 if n == 2:

 return True

 if n > 2 and n % 2 == 0:

 return False

 max_div = math.floor(math.sqrt(n))

 for i in range(3, 1 + max_div, 2):

 if n % i == 0:

 return False

 return True

# Driver function

t0 = time.time()

c = 0 #for counting

for n in range(1,100000):

 x = is_prime(n)

 c += x

print("Total prime numbers in range :", c)

t1 = time.time()

print("Time required :", t1 - t0)  
  
---  
  
 __

 __

 **Output:**

    
    
    Total prime numbers in range: 9592
    Time required: 0.23305177688598633

In the above code, we check all the numbers from 1 to 100000 whether those
numbers are prime or not. It takes comparatively lesser time than all the
previous methods for running the program. It is most efficient and quickest
way to check for the prime number. Therefore, it is most preferred in
competitive programming. Next time while attempting any question in
competitive programming, use this method for best results.  
 **Sieve Method**  
This method prints all the primes smaller than or equal to a given number, n.
For example, if n is 10, the output should be “2, 3, 5, 7”. If n is 20, the
output should be “2, 3, 5, 7, 11, 13, 17, 19”.  
This method is considered to be the most efficient method to generate all the
primes smaller than the given number, n. It is considered as the fastest
method of all to generate a list of prime numbers. This method is not suited
to check for a particular number. This method is preferred for generating the
list of all the prime numbers.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to find prime numbers in a range

import time

def SieveOfEratosthenes(n):

 

 # Create a boolean array "prime[0..n]" and

 # initialize all entries it as true. A value

 # in prime[i] will finally be false if i is

 # Not a prime, else true.

 prime = [True for i in range(n+1)]

 

 p = 2

 while(p * p <= n):

 

 # If prime[p] is not changed, then it is

 # a prime

 if (prime[p] == True):

 

 # Update all multiples of p

 for i in range(p * p, n + 1, p):

 prime[i] = False

 p += 1

 c = 0

 # Print all prime numbers

 for p in range(2, n):

 if prime[p]:

 c += 1

 return c

# Driver function

t0 = time.time()

c = SieveOfEratosthenes(100000)

print("Total prime numbers in range:", c)

t1 = time.time()

print("Time required:", t1 - t0)  
  
---  
  
 __

 __

 **Output:**

    
    
    Total prime numbers in range: 9592
    Time required: 0.0312497615814209

 **Note :** Time required for all the procedures may vary depending on the
compiler but the order of time required by the different methods will remain
same.

 **Reference :**

\https://www.geeksforgeeks.org/sieve-of-eratosthenes/  
http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes  
This article is contributed by **Rishabh Bansal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

