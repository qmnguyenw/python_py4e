How to generate Large Prime numbers for RSA Algorithm



The security of the **RSA algorithm** is based on the difficulty of
factorizing very large numbers. The setup of an RSA cryptosystem involves the
generation of two large primes, say **p** and **q** , from which, the RSA
modulus is calculated as **n = p * q**. The greater the modulus size, the
higher is the security level of the RSA system. The recommended RSA modulus
size for most settings is _2048_ bits to _4096_ bits. Thus, the primes to be
generated need to be _1024_ bit to _2048_ bit long. For the synthesis of such
large primes, instead of depending on deterministic methods, we rely on
finding numbers that are prime with a satisfactorily high level of
probability.

## Large Prime Generation Procedure:

  * The goal is to efficiently compute very large random prime numbers with a specified bit-size. The standard method of manually implementing a random prime number generator which can generate prime values with a satisfactory level of accuracy is given as follows:
    1. Preselect a random number with the desired bit-size
    2. Ensure the chosen number is not divisible by the first few hundred primes (these are pre-generated)
    3. Apply a certain number of **Rabin Miller Primality Test** iterations, based on acceptable error rate, to get a number which is probably a prime

![Large Prime Generation Process](https://media.geeksforgeeks.org/wp-
content/uploads/20200515202847/flow6-1.png)

 **Fig 1:** Steps involved in Generation of Large Primes for RSA

### Below are the steps to implement the above procedure:

  1.  **Picking a Random Prime Candidate**
    * The generation of a random number with n-bits means the random number is in the range 0 and ![\(2^n-1\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f3fddbaa499b0a964f3a95c8660b8752_l3.png). Some considerations when generating the random number are:
      1. Picking of small primes, such as 3, 5, 7…, must be avoided as the factorization of RSA modulus would become trivial. Thus, care must be taken to not have too many leading zeroes. This may be done by always making the highest order bit = 1
      2. Since all primes (> 2) are odd, for better performace, just odd number may be picked
    * Thus, we pick any random number in the range ![\(2^{n-1} + 1, 2^n - 1\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-e14fd30ae4aa9fff780c6248094b5326_l3.png)

__

__  
__

__

__  
__  
__

def nBitRandom(n):

 

 # Returns a random number

 # between 2**(n-1)+1 and 2**n-1'''

 return(random.randrange(2**(n-1)+1,
2**n-1))  
  
---  
  
 __

 __

  2.  **Division with First Primes _(Low-Level Primality Test)_**
    * This step is a a low level primality test which requires the pre-calculation of the first few hundred primes (using **Sieve of Eratosthenes**).
    * The prime candidate is divided by the pre-generated primes to check for divisibility. If the prime candidate is perfectly divisible by any of these pre-generated primes, the test fails and a new prime candidate must be picked and tested. This is repeated as long as a value which is coprime to all the primes in our generated primes list is found

 __

 __  
 __

 __

 __  
 __  
 __

def getLowLevelPrime(n):

 '''Generate a prime candidate divisible

 by first primes'''

 

 # Repeat until a number satisfying

 # the test isn't found

 while True: 

 

 # Obtain a random number

 prime_candidate = nBitRandom(n) 

 

 for divisor in first_primes_list: 

 if prime_candidate % divisor == 0

 and divisor**2 <= prime_candidate:

 break

 # If no divisor found, return value

 else: return prime_candidate   
  
---  
  
__

__

  3. **Rabin Miller Primality Test _(High-Level Primality Test)_**
    * A prime candidate passing the low-level test is then tested again using the Rabin Miller Primality Test.
    * For extremely large numbers, such as ones used in RSA, deterministic testing of whether the chosen value is prime or not is highly impractical as it requires an unreasonable amount of computing resources.
    * A probabilistic approach is preferred as such. If an inputted value passes a single iteration of the Rabin Miller test, the probability of the number being prime is **75%**.
    * Thus, a candidate passing the test, an adequate number of times, can be considered to be a prime with a satisfactory level of probability.
    * Usually, in commercial applications, we require error probabilities to be less than ![{1/2}^{128}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-5061526741b23b87741541350bf61f52_l3.png).

 __

 __  
 __

 __

 __  
 __  
 __

def isMillerRabinPassed(miller_rabin_candidate):

 '''Run 20 iterations of Rabin Miller Primality test'''

 

 maxDivisionsByTwo = 0

 evenComponent = miller_rabin_candidate-1

 

 while evenComponent % 2 == 0:

 evenComponent >>= 1

 maxDivisionsByTwo += 1

 assert(2**maxDivisionsByTwo * evenComponent ==
miller_rabin_candidate-1)

 

 def trialComposite(round_tester):

 if pow(round_tester, evenComponent, 

 miller_rabin_candidate) == 1:

 return False

 for i in range(maxDivisionsByTwo):

 if pow(round_tester, 2**i * evenComponent,

 miller_rabin_candidate) 

 == miller_rabin_candidate-1:

 return False

 return True

 

 # Set number of trials here

 numberOfRabinTrials = 20

 for i in range(numberOfRabinTrials):

 round_tester = random.randrange(2,

 miller_rabin_candidate)

 if trialComposite(round_tester):

 return False

 return True  
  
---  
  
 __

 __

  4.  **Combining the above steps to generate the code**
    * Finally, we can combine the above functions to create a three-step process to generate large primes. The steps would be
      1. Random number generation by calling **nBitRandom(** _bitsize_ **)**
      2. Basic division test by calling **getLowLevelPrime(** _prime_candidate_ **)**
      3. Rabin Miller Test by calling **isMillerRabinPassed(** _prime_candidate_ **)**
    * If the chosen random value passes all primality tests, it is returned as the n-bit prime number. Otherwise, in the case of test-failure, a new random value is picked and tested for primality. The process is repeated until the desired prime is found.

### Below is the complete implementation of the above approach

 __

 __  
 __

 __

 __  
 __  
 __

# Large Prime Generation for RSA

import random

 

# Pre generated primes

first_primes_list = [2, 3, 5, 7, 11, 13, 17,
19, 23, 29,

 31, 37, 41, 43, 47, 53, 59, 61, 67, 

 71, 73, 79, 83, 89, 97, 101, 103, 

 107, 109, 113, 127, 131, 137, 139, 

 149, 151, 157, 163, 167, 173, 179, 

 181, 191, 193, 197, 199, 211, 223,

 227, 229, 233, 239, 241, 251, 257,

 263, 269, 271, 277, 281, 283, 293,

 307, 311, 313, 317, 331, 337, 347, 349]

 

def nBitRandom(n):

 return random.randrange(2**(n-1)+1, 2**n
- 1)

 

def getLowLevelPrime(n):

 '''Generate a prime candidate divisible 

 by first primes'''

 while True:

 # Obtain a random number

 pc = nBitRandom(n) 

 

 # Test divisibility by pre-generated 

 # primes

 for divisor in first_primes_list:

 if pc % divisor == 0 and divisor**2 <= pc:

 break

 else: return pc

 

def isMillerRabinPassed(mrc):

 '''Run 20 iterations of Rabin Miller Primality test'''

 maxDivisionsByTwo = 0

 ec = mrc-1

 while ec % 2 == 0:

 ec >>= 1

 maxDivisionsByTwo += 1

 assert(2**maxDivisionsByTwo * ec == mrc-1)

 

 def trialComposite(round_tester):

 if pow(round_tester, ec, mrc) == 1:

 return False

 for i in range(maxDivisionsByTwo):

 if pow(round_tester, 2**i * ec, mrc) ==
mrc-1:

 return False

 return True

 

 # Set number of trials here

 numberOfRabinTrials = 20

 for i in range(numberOfRabinTrials):

 round_tester = random.randrange(2, mrc)

 if trialComposite(round_tester):

 return False

 return True

 

if __name__ == '__main__':

 while True:

 n = 1024

 prime_candidate = getLowLevelPrime(n)

 if not isMillerRabinPassed(prime_candidate):

 continue

 else:

 print(n, "bit prime is: \n", prime_candidate)

 break  
  
---  
  
 __

 __

 **Output:**

