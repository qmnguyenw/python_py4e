Python Program for Find sum of odd factors of a number



Given a number n, the task is to find the odd factor sum.

Examples:

    
    
    Input : n = 30
    Output : 24
    Odd dividers sum 1 + 3 + 5 + 15 = 24 
    
    Input : 18
    Output : 13
    Odd dividers sum 1 + 3 + 9 = 13
    

Let p1, p2, … pk be prime factors of n. Let a1, a2, .. ak be highest powers of
p1, p2, .. pk respectively that divide n, i.e., we can write n as **n = (p
1a1)*(p2a2)* … (pkak)**.

    
    
    Sum of divisors = (1 + p1 + p12 ... p1a1) * 
                      (1 + p2 + p22 ... p2a2) *
                      .............................................
                      (1 + pk + pk2 ... pkak) 

To find sum of odd factors, we simply need to ignore even factors and their
powers. For example, consider n = 18. It can be written as 2132 and sun of all
factors is (1)*(1 + 2)*(1 + 3 + 32). Sum of odd factors (1)*(1+3+32) = 13.

To remove all even factors, we repeatedly divide n while it is divisible by 2.
After this step, we only get odd factors. Note that 2 is the only even prime.  

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Formula based Python3 program

# to find sum of all divisors

# of n.

import math

 

# Returns sum of all factors

# of n.

def sumofoddFactors( n ):

 

 # Traversing through all 

 # prime factors.

 res = 1

 

 # ignore even factors by 

 # of 2

 while n % 2 == 0:

 n = n // 2

 

 for i in range(3, int(math.sqrt(n) + 1)):

 

 # While i divides n, print

 # i and divide n

 count = 0

 curr_sum = 1

 curr_term = 1

 while n % i == 0:

 count+=1

 

 n = n // i

 curr_term *= i

 curr_sum += curr_term

 

 res *= curr_sum

 

 # This condition is to

 # handle the case when

 # n is a prime number.

 if n >= 2:

 res *= (1 + n)

 

 return res

 

# Driver code

n = 30

print(sumofoddFactors(n))

 

# This code is contributed by "Sharad_Bhardwaj".  
  
---  
  
 __

 __

Output:

    
    
    24
    

Please refer complete article on Find sum of odd factors of a number for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

