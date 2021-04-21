Python Program for Product of unique prime factors of a number



Given a number n, we need to find the product of all of its unique prime
factors. Prime factors: It is basically a factor of the number that is a prime
number itself.

 **Examples:**

    
    
    **Input:** num = 10
    **Output:** Product is 10
    **Explanation:**
    Here, the input number is 10 having only 2 prime factors and they are 5 and 2.
    And hence their product is 10.
    
    **Input :** num = 25
    **Output:** Product is 5
    **Explanation:**
    Here, for the input to be 25  we have only one unique prime factor i.e 5.
    And hence the required product is 5.
    

**Method 1 (Simple)**  
Using a loop from i = 2 to n and check if i is a factor of n then check if i
is prime number itself if yes then store product in product variable and
continue this process till i = n.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find sum of given

# series.

 

def productPrimeFactors(n):

 product = 1

 

 for i in range(2, n+1):

 if (n % i == 0):

 isPrime = 1

 

 for j in range(2, int(i/2 + 1)):

 if (i % j == 0):

 isPrime = 0

 break

 

 # condition if \'i\' is Prime number

 # as well as factor of num

 if (isPrime):

 product = product * i

 

 return product 

 

 

 

# main()

n = 44

print (productPrimeFactors(n))

 

# Contributed by _omg  
  
---  
  
 __

 __

 **Output:**

    
    
    22
    

**Method 2 (Efficient) :**  
The idea is based on Efficient program to print all prime factors of a given
number

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find product of

# unique prime factors of a number

 

import math

 

def productPrimeFactors(n):

 product = 1

 

 # Handle prime factor 2 explicitly so that

 # can optimally handle other prime factors.

 if (n % 2 == 0):

 product *= 2

 while (n%2 == 0):

 n = n/2

 

 # n must be odd at this point. So we can

 # skip one element (Note i = i +2)

 for i in range (3, int(math.sqrt(n)), 2):

 # While i divides n, print i and

 # divide n

 if (n % i == 0):

 product = product * i

 while (n%i == 0):

 n = n/i

 

 # This condition is to handle the case when n

 # is a prime number greater than 2

 if (n > 2):

 product = product * n

 

 return product 

 

# main()

n = 44

print (int(productPrimeFactors(n)))

 

# Contributed by _omg  
  
---  
  
 __

 __

 **Output:**

    
    
    22
    

Please refer complete article on Product of unique prime factors of a number
for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

