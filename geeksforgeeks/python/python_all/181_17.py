Python Program for Largest K digit number divisible by X



Integers X and K are given. The task is to find highest K-digit number
divisible by X.

 **Examples:**

    
    
    **Input :** X = 30, K = 3
    **Output :** 990
    990 is the largest three digit 
    number divisible by 30.
    
    **Input :** X = 7, K = 2
    **Output :** 98
    

An **efficient solution** is to use below formula.

    
    
    ans = MAX - (MAX % X)
    where MAX is the largest K digit 
    number which is  999...K-times

The formula works on simple school method division. We remove remainder to get
the largest divisible number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find highest

# K-digit number divisible by X

 

def answer(X, K):

 

 # Computing MAX

 MAX = pow(10, K) - 1

 

 #returning ans

 return (MAX - (MAX % X))

 

X = 30; 

K = 3; 

 

print(answer(X, K)); 

 

# Code contributes by Mohit Gupta_OMG <(0_o)>  
  
---  
  
 __

 __

 **Output :**

    
    
    990
    

Please refer complete article on Largest K digit number divisible by X for
more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

