Python Program for Smallest K digit number divisible by X



Integers X and K are given. The task is to find smallest K-digit number
divisible by X.

 **Examples:**

    
    
    **Input :** X = 83, K = 5
    **Output :** 10043
    10040 is the smallest 5 digit
    number that is multiple of 83.
    
    **Input :** X = 5, K = 2
    **Output :** 10

An **efficient solution** would be :

    
    
    Compute MIN : smallest K-digit number (1000...K-times)
    If, MIN % X is 0, ans = MIN
    else, ans = (MIN + X) - ((MIN + X) % X))
    This is because there will be a number in 
    range [MIN...MIN+X] divisible by X.
    

__

__  
__

__

__  
__  
__

# Python code to find smallest K-digit

# number divisible by X

 

def answer(X, K):

 

 # Computing MAX

 MIN = pow(10, K-1)

 

 if(MIN%X == 0):

 return (MIN)

 

 else:

 return ((MIN + X) - ((MIN + X) % X))

 

 

X = 83; 

K = 5; 

 

print(answer(X, K)); 

 

# Code contributed by Mohit Gupta_OMG <(0_o)>  
  
---  
  
 __

 __

 **Output :**

    
    
    10043

Please refer complete article on Smallest K digit number divisible by X for
more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

