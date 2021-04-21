Python Program for cube sum of first n natural numbers



Print the sum of series 13 \+ 23 \+ 33 \+ 43 \+ …….+ n3 till n-th term.

Examples:

    
    
    Input : n = 5
    Output : 225
    13 + 23 + 33 + 43 + 53 = 225
    
    Input : n = 7
    Output : 784
    13 + 23 + 33 + 43 + 53 + 
    63 + 73 = 784
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Simple Python program to find sum of series

# with cubes of first n natural numbers

 

# Returns the sum of series 

def sumOfSeries(n):

 sum = 0

 for i in range(1, n+1):

 sum +=i*i*i

 

 return sum

 

 

# Driver Function

n = 5

print(sumOfSeries(n))

 

# Code Contributed by Mohit Gupta_OMG <(0_o)>  
  
---  
  
 __

 __

 **Output :**

    
    
    225
    

Time Complexity : O(n)  
An **efficient solution** is to use direct mathematical formula which is **(n
( n + 1 ) / 2) ^ 2**

    
    
    For n = 5 sum by formula is
           (5*(5 + 1 ) / 2)) ^ 2
              = (5*6/2) ^ 2
              = (15) ^ 2
              = 225
    
    For n = 7, sum by formula is
           (7*(7 + 1 ) / 2)) ^ 2
              = (7*8/2) ^ 2
              = (28) ^ 2
              = 784
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A formula based Python program to find sum

# of series with cubes of first n natural 

# numbers

 

# Returns the sum of series 

def sumOfSeries(n):

 x = (n * (n + 1) / 2)

 return (int)(x * x)

 

 

 

# Driver Function

n = 5

print(sumOfSeries(n))

 

# Code Contributed by Mohit Gupta_OMG <(0_o)>  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    225
    

Time Complexity : O(1)  
 **How does this formula work?**  
We can prove the formula using mathematical induction. We can easily see that
the formula holds true for n = 1 and n = 2. Let this be true for n = k-1.

    
    
    Let the formula be true for n = k-1.
    Sum of first (k-1) natural numbers = 
                [((k - 1) * k)/2]2
    
    Sum of first k natural numbers = 
              = Sum of (k-1) numbers + k3
              = [((k - 1) * k)/2]2 + k3
              = [k2(k2 - 2k + 1) + 4k3]/4
              = [k4 + 2k3 + k2]/4
              = k2(k2 + 2k + 1)/4
              = [k*(k+1)/2]2

 **The above program causes overflow, even if result is not beyond integer
limit.** Like previous post, we can avoid overflow upto some extent by doing
division first.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Efficient Python program to find sum of cubes

# of first n natural numbers that avoids 

# overflow if result is going to be withing 

# limits.

 

# Returns the sum of series 

def sumOfSeries(n):

 x = 0

 if n % 2 == 0 : 

 x = (n/2) * (n+1)

 else:

 x = ((n + 1) / 2) * n

 

 return (int)(x * x)

 

 

# Driver Function

n = 5

print(sumOfSeries(n))

 

# Code Contributed by Mohit Gupta_OMG <(0_o)>  
  
---  
  
 __

 __

 **Output:**

    
    
    225
    

Please refer complete article on Program for cube sum of first n natural
numbers for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

