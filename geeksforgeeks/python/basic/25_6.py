Prime functions in Python SymPy



How to get prime numbers quickly in python using library functions?  
Library functions always make our code easy so here we are going to discuss
some library function in python to work upon prime numbers. **SymPy** is a
python module which contains some really cool prime number related library
functions. Given below is the list of these functions :

  1. **isprime(n):** It tests if n is a prime number (True) or not (False).
  2.  **primerange(a, b):** It generates a list of all prime numbers in the range [a, b).
  3.  **randprime(a, b):** It returns a random prime number in the range [a, b).
  4.  **primepi(n):** It returns the number of prime numbers less than or equal to n.
  5.  **prime(nth) :** It returns the nth prime, with the primes indexed as prime(1) = 2. The nth prime is approximately n*log(n) and can never be larger than 2**n.
  6.  **prevprime(n):** It returns the prev prime smaller than n.
  7.  **nextprime(n):** It returns the next greater prime than n.
  8.  **sieve.primerange(a, b):** It generates all prime numbers in the range [a, b), implemented as a dynamically growing sieve of Eratosthenes.

 **Example:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Library functions for prime

import sympy

# Output : True

print(sympy.isprime(5)) 

# Output : [2, 3, 5, 7, 11, 13, 17, 19, 23,

# 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,

# 73, 79, 83, 89, 97]

print(list(sympy.primerange(0, 100))) 

 

print(sympy.randprime(0, 100)) # Output : 83

print(sympy.randprime(0, 100)) # Output : 41

print(sympy.prime(3)) # Output : 5

print(sympy.prevprime(50)) # Output : 47

print(sympy.nextprime(50)) # Output : 53

# Output : [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,

# 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,

# 79, 83, 89, 97]

print list(sympy.sieve.primerange(0, 100))  
  
---  
  
 __

 __

 **Reference :**  
https://stackoverflow.com/questions/13326673/is-there-a-python-library-to-
list-primes  
This article is contributed by **Shashank Mishra (Gullu)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

