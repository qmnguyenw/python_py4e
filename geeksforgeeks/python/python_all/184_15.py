Python Program to Count trailing zeroes in factorial of a number



Given an integer n, write a function that returns count of trailing zeroes in
n!.

 **Examples :**

    
    
    Input: n = 5
    Output: 1 
    Factorial of 5 is 120 which has one trailing 0.
    
    Input: n = 20
    Output: 4
    Factorial of 20 is 2432902008176640000 which has
    4 trailing zeroes.
    
    Input: n = 100
    Output: 24
    
    
    
    Trailing 0s in n! = Count of 5s in prime factors of n!
                      = floor(n/5) + floor(n/25) + floor(n/125) + ....
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to

# count trailing 0s 

# in n !

 

# Function to return 

# trailing 0s in 

# factorial of n

def findTrailingZeros(n):

 

 # Initialize result

 count = 0

 

 # Keep dividing n by

 # powers of 5 and

 # update Count

 i = 5

 while (n / i>= 1):

 count += int(n / i)

 i *= 5

 

 return int(count)

 

# Driver program 

n = 100

print("Count of trailing 0s "+

 "in 100 ! is", findTrailingZeros(n))

 

# This code is contributed by Smitha Dinesh Semwal  
  
---  
  
 __

 __

 **Output:**

    
    
    Count of trailing 0s in 100 ! is 24
    

Please refer complete article on Count trailing zeroes in factorial of a
number for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

