Python Program for Zeckendorf\’s Theorem (Non-Neighbouring Fibonacci
Representation)



Given a number, find a representation of number as sum of non-consecutive
Fibonacci numbers.

Examples:

    
    
    Input:  n = 10
    Output: 8 2
    8 and 2 are two non-consecutive Fibonacci Numbers
    and sum of them is 10.
    
    Input:  n = 30
    Output: 21 8 1
    21, 8 and 1 are non-consecutive Fibonacci Numbers
    and sum of them is 30.
    

The idea is to use Greedy Algorithm.

    
    
    1) Let n be input number
    
    2) While n >= 0
         a) Find the greatest Fibonacci Number smaller than n.
            Let this number be 'f'.  Print 'f'
         b) n = n - f 

__

__  
__

__

__  
__  
__

# Python program for Zeckendorf's theorem. It finds representation

# of n as sum of non-neighbouring Fibonacci Numbers.

 

# Returns the greatest Fibonacci Numberr smaller than

# or equal to n.

def nearestSmallerEqFib(n):

 

 # Corner cases

 if (n == 0 or n == 1):

 return n

 

 # Finds the greatest Fibonacci Number smaller

 # than n.

 f1, f2, f3 = 0, 1, 1

 while (f3 <= n):

 f1 = f2;

 f2 = f3;

 f3 = f1 + f2;

 return f2;

 

 

# Prints Fibonacci Representation of n using

# greedy algorithm

def printFibRepresntation(n):

 

 while (n>0):

 

 # Find the greates Fibonacci Number smaller

 # than or equal to n

 f = nearestSmallerEqFib(n);

 

 # Print the found fibonacci number

 print f,

 

 # Reduce n

 n = n-f

 

# Driver code test above functions

n = 30

print "Non-neighbouring Fibonacci Representation of", n, "is"

printFibRepresntation(n)  
  
---  
  
 __

 __

 **Output:**

    
    
    Non-neighbouring Fibonacci Representation of 30 is
    21 8 1
    

Please refer complete article on Zeckendorf’s Theorem (Non-Neighbouring
Fibonacci Representation) for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

