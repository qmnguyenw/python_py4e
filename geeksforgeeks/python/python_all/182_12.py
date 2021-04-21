Python Program for n\’th multiple of a number in Fibonacci Series



Given two integers n and k. Find position the n\’th multiple of K in the
Fibonacci series.  
 **Examples:**

    
    
    **Input :** k = 2, n = 3
    **Output :** 9
    3\'rd multiple of 2 in Fibonacci Series is 34 
    which appears at position 9.
    
    **Input  :** k = 4, n = 5 
    **Output :** 30
    5\'th multiple of 5 in Fibonacci Series is 832040 
    which appears at position 30.

An **Efficient Solution** is based on below interesting property.  
Fibonacci series is always periodic under modular representation. Below are
examples.

    
    
    F (mod 2) = 1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,
                1,1,0,1,1,0,1,1,0,1,1,0,1,1,0 
    Here 0 is repeating at every 3rd index and 
    the cycle repeats at every 3rd index. 
    
    F (mod 3) = 1,1,2,0,2,2,1,0,1,1,2,0,2,2,1,0
                ,1,1,2,0,2,2,1,0,1,1,2,0,2,2
    Here 0 is repeating at every 4th index and 
    the cycle repeats at every 8th index.
    
    F (mod 4) = 1,1,2,3,1,0,1,1,2,3,1,0,1,1,2,3,
               1,0,1,1,2,3,1,0,1,1,2,3,1,0 
    Here 0 is repeating at every 6th index and 
    the cycle repeats at every 6th index.
    
    F (mod 5) = 1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,
                2,2,4,1,0,1,1,2,3,0,3,3,1,4,0
    Here 0 is repeating at every 5th index and
    the cycle repeats at every 20th index.
    
    F (mod 6) = 1,1,2,3,5,2,1,3,4,1,5,0,5,5,4,
                3,1,4,5,3,2,5,1,0,1,1,2,3,5,2
    Here 0 is repeating at every 12th index and 
    the cycle repeats at every 24th index.
    
    F (mod 7) = 1,1,2,3,5,1,6,0,6,6,5,4,2,6,1,
                0,1,1,2,3,5,1,6,0,6,6,5,4,2,6 
    Here 0 is repeating at every 8th index and 
    the cycle repeats at every 16th index.
    
    F (mod 8) = 1,1,2,3,5,0,5,5,2,7,1,0,1,1,2,
                3,5,0,5,5,2,7,1,0,1,1,2,3,5,0 
    Here 0 is repeating at every 6th index and 
    the cycle repeats at every 12th index.
    
    F (mod 9) = 1,1,2,3,5,8,4,3,7,1,8,0,8,8,7,
                6,4,1,5,6,2,8,1,0,1,1,2,3,5,8 
    Here 0 is repeating at every 12th index and 
    the cycle repeats at every 24th index.
    
    F (mod 10) = 1,1,2,3,5,8,3,1,4,5,9,4,3,7,0,
                 7,7,4,1,5,6,1,7,8,5,3,8,1,9,0.
    Here 0 is repeating at every 15th index and
    the cycle repeats at every 60th index.
    

__

__  
__

__

__  
__  
__

# Python Program to find position of n\'th multiple

# of a mumber k in Fibonacci Series

 

def findPosition(k, n):

 f1 = 0

 f2 = 1

 i =2; 

 while i!=0:

 f3 = f1 + f2;

 f1 = f2;

 f2 = f3;

 

 if f2%k == 0:

 return n*i

 

 i+=1

 

 return

 

 

# Multiple no.

n = 5;

# Number of whose multiple we are finding

k = 4;

 

print("Position of n\'th multiple of k in"

 "Fibonacci Seires is", findPosition(k,n));

 

# Code contributed by Mohit Gupta_OMG  
  
---  
  
 __

 __

 **Output:**

    
    
    Position of n'th multiple of k inFibonacci Seires is 30
    

Please refer complete article on n’th multiple of a number in Fibonacci Series
for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

