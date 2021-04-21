Python Program for How to check if a given number is Fibonacci number?



Given a number \’n\’, how to check if n is a Fibonacci number. First few
Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 141, ..

Examples :

    
    
    Input : 8
    Output : Yes
    
    Input : 34
    Output : Yes
    
    Input : 41
    Output : No
    

Following is an interesting property about Fibonacci numbers that can also be
used to check if a given number is Fibonacci or not.  
 _A number is Fibonacci if and only if one or both of (5*n 2 \+ 4) or (5*n2 –
4) is a perfect square_ (Source: Wiki).

 __

 __  
 __

 __

 __  
 __  
 __

# python program to check if x is a perfect square

import math

 

# A utility function that returns true if x is perfect square

def isPerfectSquare(x):

 s = int(math.sqrt(x))

 return s*s == x

 

# Returns true if n is a Fibinacci Number, else false

def isFibonacci(n):

 

 # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both

 # is a perferct square

 return isPerfectSquare(5*n*n + 4) or
isPerfectSquare(5*n*n - 4)

 

# A utility function to test above functions

for i in range(1,11):

 if (isFibonacci(i) == True):

 print i,"is a Fibonacci Number"

 else:

 print i,"is a not Fibonacci Number "  
  
---  
  
 __

 __

 **Output:**

    
    
    1 is a Fibonacci Number
    2 is a Fibonacci Number
    3 is a Fibonacci Number
    4 is a not Fibonacci Number 
    5 is a Fibonacci Number
    6 is a not Fibonacci Number 
    7 is a not Fibonacci Number 
    8 is a Fibonacci Number
    9 is a not Fibonacci Number 
    10 is a not Fibonacci Number 
    

Please refer complete article on How to check if a given number is Fibonacci
number? for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

