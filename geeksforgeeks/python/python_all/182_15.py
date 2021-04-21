Python Program for Common Divisors of Two Numbers



Given two integer numbers, the task is to find count of all common divisors of
given numbers?

    
    
    Input : a = 12, b = 24
    Output: 6
    // all common divisors are 1, 2, 3, 
    // 4, 6 and 12
    
    Input : a = 3, b = 17
    Output: 1
    // all common divisors are 1
    
    Input : a = 20, b = 36
    Output: 3
    // all common divisors are 1, 2, 4
    

__

__  
__

__

__  
__  
__

# Python Program to find

# Common Divisors of Two Numbers

 

a = 12

b = 24

n = 0

 

for i in range(1, min(a, b)+1):

 if a%i==b%i==0:

 n+=1

 

print(n)

 

# Code contributed by Mohit Gupta_OMG  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    

Please refer complete article on Common Divisors of Two Numbers for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

