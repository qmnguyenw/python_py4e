Python Program for GCD of more than two (or array) numbers



The GCD of three or more numbers equals the product of the prime factors
common to all the numbers, but it can also be calculated by repeatedly taking
the GCDs of pairs of numbers.

    
    
    gcd(a, b, c) = gcd(a, gcd(b, c)) 
                 = gcd(gcd(a, b), c) 
                 = gcd(gcd(a, c), b)
    

__

__  
__

__

__  
__  
__

# GCD of more than two (or array) numbers

# This function implements the Euclidian 

# algorithm to find H.C.F. of two number

 

def find_gcd(x, y):

 while(y):

 x, y = y, x % y

 

 return x

 

 

l = [2, 4, 6, 8, 16]

 

num1=l[0]

num2=l[1]

gcd=find_gcd(num1,num2)

 

for i in range(2,len(l)):

 gcd=find_gcd(gcd,l[i])

 

print(gcd)

 

# Code contributed by Mohit Gupta_OMG  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Please refer complete article on GCD of more than two (or array) numbers for
more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

