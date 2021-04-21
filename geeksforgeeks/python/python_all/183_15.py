Python Program to Count ways to reach the n’th stair



There are n stairs, a person standing at the bottom wants to reach the top.
The person can climb either 1 stair or 2 stairs at a time. Count the number of
ways, the person can reach the top.

![stairs](https://media.geeksforgeeks.org/wp-content/uploads/nth-stair.png)

Consider the example shown in diagram. The value of n is 3. There are 3 ways
to reach the top. The diagram is taken from Easier Fibonacci puzzles  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A program to count the number of ways to reach n'th stair

 

# Recurssive program to find n'th fibonacci number

def fib(n):

 if n <= 1:

 return n

 return fib(n-1) + fib(n-2)

 

# returns no. of ways to reach s'th stair

def countWays(s):

 return fib(s + 1)

 

# Driver program

 

s = 4

print "Number of ways = ",

print countWays(s)

 

# Contributed by Harshit Agrawal  
  
---  
  
 __

 __

 **Output:**

    
    
    Number of ways =  5
    

The time complexity of the above implementation is exponential (golden ratio
raised to power n). It can be optimized to work in O(Logn) time using the
previously discussed Fibonacci function optimizations.  

## Python

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# A program to count the number of ways to reach n'th stair

 

# Recursive function used by countWays

def countWaysUtil(n, m):

 if n <= 1:

 return n

 res = 0

 i = 1

 while i<= m and i<= n:

 res = res + countWaysUtil(n-i, m)

 i = i + 1

 return res

 

# Returns number of ways to reach s'th stair 

def countWays(s, m):

 return countWaysUtil(s + 1, m)

 

 

# Driver program

s, m = 4, 2

print "Number of ways =", countWays(s, m)

 

# Contributed by Harshit Agrawal  
  
---  
  
 __

 __

