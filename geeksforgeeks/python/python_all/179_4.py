Python Program for Find sum of Series with n-th term as n^2 – (n-1)^2



We are given an integer n and n-th term in a series as expressed below:

    
    
    Tn = n2 - (n-1)2

We need to find Sn mod (109 \+ 7), where Sn is the sum of all of the terms of
the given series and,

    
    
    Sn = T1 + T2 + T3 + T4 + ...... + Tn

 **Examples:**

    
    
    **Input :** 229137999
    **Output :** 218194447
    
    **Input :** 344936985
    **Output :** 788019571
    

Let us do some calculations, before writing the program. Tn can be reduced to
give 2n-1 . Let\’s see how:

    
    
    Given, Tn = n2 - (n-1)2
    Or, Tn =  n2 - (1 + n2 - 2n)
    Or, Tn =  n2 - 1 - n2 + 2n
    Or, Tn =  2n - 1. 
    

Now, we need to find ∑Tn.

  

  

∑Tn = ∑(2n – 1)

We can simplify the above formula as,  
∑(2n – 1) = 2*∑n – ∑1  
Or, ∑(2n – 1) = 2*∑n – n.  
Where, ∑n is the sum of first n natural numbers.

We know the sum of n natural number = n(n+1)/2.

Therefore, putting this value in the above equation we will get,

∑Tn = (2*(n)*(n+1)/2)-n = n2

Now the value of n2 can be very large. So instead of direct squaring n and
taking mod of the result. We will use the property of modular multiplication
for calculating squares:

(a*b)%k = ((a%k)*(b%k))%k

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find sum of given

# series.

 

mod = 1000000007

def findSum(n):

 return ((n % mod) * (n % mod)) % mod

 

 

# main()

n = 229137999

print (findSum(n))

 

# Contributed by _omg  
  
---  
  
 __

 __

 **Output:**

    
    
    218194447
    

Please refer complete article on Find sum of Series with n-th term as n^2 –
(n-1)^2 for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

