Python Program for Number of solutions to Modular Equations



Given A and B, the task is to find the number of possible values that X can
take such that the given modular equation **(A mod X) = B** holds good. Here,
X is also called a solution of the modular equation.

 **Examples:**

    
    
    **Input :** A = 26, B = 2
    **Output :** 6
    **Explanation**
    X can be equal to any of {3, 4, 6, 8,
    12, 24} as A modulus any of these values
    equals 2 i. e., **(26 mod 3) = (26 mod 4) 
    = (26 mod 6) = (26 mod 8) =Output:2**
    
    **Input :** 21 5
    **Output :** 2
    **Explanation**
    X can be equal to any of {8, 16} as A modulus 
    any of these values equals 5 i.e. **(21 mod 
    8) = (21 mod 16) = 5**
    

If we carefully analyze the equation A mod X = B its easy to note that if (A =
B) then there are infinitely many values greater than A that X can take. In
the Case when (A < B), there cannot be any possible value of X for which the
modular equation holds. So the only case we are left to investigate is when (A
> B).So now we focus on this case in depth.

Now, in this case we can use a well known relation i.e.

    
    
    Dividend = Divisor * Quotient + Remainder
    

We are looking for all possible X i.e. Divisors given A i.e Dividend and B
i.e., remainder. So,

  

  

    
    
    We can say,
    A = X * Quotient + B
    
    Let Quotient be represented as Y
    ∴ A = X * Y + B
    A - B = X * Y
    
    ∴ To get integral values of Y, 
    we need to take all X such that X divides (A - B)
    
    **∴ X is a divisor of (A - B)**
    

So, the problem reduces to finding the divisors of (A – B) and the number of
such divisors is the possible values X can take.  
But as we know A mod X would result in values from (0 to X – 1) we must take
all such X such that X > B.

Thus, we can conclude by saying that the number of divisors of (A – B) greater
than B, are the all possible values X can take to satisfy A mod X = B

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to find number of possible

# values of X to satisfy A mod X = B 

import math

 

# Returns the number of divisors of (A - B)

# greater than B

def calculateDivisors (A, B):

 N = A - B

 noOfDivisors = 0

 

 a = math.sqrt(N)

 for i in range(1, int(a + 1)):

 # if N is divisible by i

 if ((N % i == 0)):

 # count only the divisors greater than B

 if (i > B):

 noOfDivisors +=1

 

 # checking if a divisor isnt counted twice

 if ((N / i) != i and (N / i) > B):

 noOfDivisors += 1;

 

 return noOfDivisors

 

# Utility function to calculate number of all

# possible values of X for which the modular

# equation holds true 

 

def numberOfPossibleWaysUtil (A, B):

 # if A = B there are infinitely many solutions

 # to equation or we say X can take infinitely

 # many values > A. We return -1 in this case 

 if (A == B):

 return -1

 

 # if A < B, there are no possible values of

 # X satisfying the equation

 if (A < B):

 return 0

 

 # the last case is when A > B, here we calculate

 # the number of divisors of (A - B), which are

 # greater than B 

 

 noOfDivisors = 0

 noOfDivisors = calculateDivisors;

 return noOfDivisors

 

 

# Wrapper function for numberOfPossibleWaysUtil() 

def numberOfPossibleWays(A, B):

 noOfSolutions = numberOfPossibleWaysUtil(A, B)

 

 #if infinitely many solutions available

 if (noOfSolutions == -1):

 print ("For A = " , A , " and B = " , B

 , ", X can take Infinitely many values"

 , " greater than " , A)

 

 else:

 print ("For A = " , A , " and B = " , B

 , ", X can take " , noOfSolutions

 , " values")

# main()

A = 26

B = 2

numberOfPossibleWays(A, B)

 

 

A = 21

B = 5

numberOfPossibleWays(A, B)

 

# Contributed by _omg  
  
---  
  
 __

 __

 **Output:**

    
    
    For A = 26 and B = 2, X can take 6 values
    For A = 21 and B = 5, X can take 2 values
    

Time Complexity of the above approach is nothing but the time complexity of
finding the number of divisors of (A – B) ie O(√(A – B))

Please refer complete article on Number of solutions to Modular Equations for
more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

