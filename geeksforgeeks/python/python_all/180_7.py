Python Program for Find sum of even factors of a number



Given a number n, the task is to find the even factor sum of a number.

 **Examples:**

    
    
    **Input :** 30
    **Output :** 48
    Even dividers sum 2 + 6 + 10 + 30 = 48
    
    **Input :** 18
    **Output :** 26
    Even dividers sum 2 + 6 + 18 = 26
    

Let p1, p2, … pk be prime factors of n. Let a1, a2, .. ak be highest powers of
p1, p2, .. pk respectively that divide n, i.e., we can write n as **n = (p1
a1)*(p2a2)* … (pkak)**.

    
    
    Sum of divisors = (1 + p1 + p12 ... p1a1) * 
                      (1 + p2 + p22 ... p2a2) *
                      ...........................
                      (1 + pk + pk2 ... pkak) 
    

If number is odd, then there are no even factors, so we simply return 0.

If number is even, we use above formula. We only need to ignore 20. All other
terms multiply to produce even factor sum. For example, consider n = 18. It
can be written as 2132 and sun of all factors is (20 \+ 21)*(30 \+ 31 \+ 32).
if we remove 20 then we get the  
Sum of even factors (2)*(1+3+32) = 26.

  

  

To remove odd number in even factor, we ignore then 20 whaich is 1. After this
step, we only get even factors. Note that 2 is the only even prime.

 __

 __  
 __

 __

 __  
 __  
 __

# Formula based Python3

# program to find sum 

# of alldivisors of n.

import math

 

# Returns sum of all 

# factors of n.

def sumofFactors(n) :

 

 # If n is odd, then

 # there are no even

 # factors.

 if (n % 2 != 0) :

 return 0

 

 # Traversing through

 # all prime factors.

 res = 1

 for i in range(2, (int)(math.sqrt(n)) + 1) :

 

 # While i divides n

 # print i and divide n

 count = 0

 curr_sum = 1

 curr_term = 1

 while (n % i == 0) :

 count= count + 1

 

 n = n // i

 

 # here we remove the

 # 2^0 that is 1. All

 # other factors

 if (i == 2 and count == 1) :

 curr_sum = 0

 

 curr_term = curr_term * i

 curr_sum = curr_sum + curr_term

 

 res = res * curr_sum

 

 

 # This condition is to

 # handle the case when

 # n is a prime number.

 if (n >= 2) :

 res = res * (1 + n)

 

 return res

 

 

# Driver code

n = 18

print(sumofFactors(n))

 

 

# This code is contributed by Nikita Tiwari.  
  
---  
  
 __

 __

 **Output:**

    
    
    26
    

Please refer complete article on Find sum of even factors of a number for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

