Python Program for Find largest prime factor of a number



Given a positive integer \’n\'( 1 <= n <= 1015). Find the largest prime factor
of a number.

    
    
    **Input:** 6
    **Output:** 3
    **Explanation**
    Prime factor of 6 are- 2, 3
    Largest of them is \'3\'
    
    **Input:** 15
    **Output:** 5
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to find largest prime

# factor of number

import math

 

# A function to find largest prime factor

def maxPrimeFactors (n):

 

 # Initialize the maximum prime factor

 # variable with the lowest one

 maxPrime = -1

 

 # Print the number of 2s that divide n

 while n % 2 == 0:

 maxPrime = 2

 n >>= 1 # equivalent to n /= 2

 

 # n must be odd at this point, 

 # thus skip the even numbers and 

 # iterate only for odd integers

 for i in range(3, int(math.sqrt(n)) + 1, 2):

 while n % i == 0:

 maxPrime = i

 n = n / i

 

 # This condition is to handle the 

 # case when n is a prime number 

 # greater than 2

 if n > 2:

 maxPrime = n

 

 return int(maxPrime)

 

# Driver code to test above function

n = 15

print(maxPrimeFactors(n))

 

n = 25698751364526

print(maxPrimeFactors(n))

 

# This code is contributed by "Sharad_Bhardwaj".  
  
---  
  
 __

 __

  
 **Output:**

    
    
    5
    328513
    

**Time complexity:**![\\text{O}\(\\sqrt{n}\)
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-4973b3e7306a6726296c98b119742ff5_l3.png)  
 **Auxiliary space:**![\\text{O}\(1\) ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-675ce415c9f2568ad7e2f2f8ff20d967_l3.png)

Please refer complete article on Find largest prime factor of a number for
more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

