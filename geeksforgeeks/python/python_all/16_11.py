Python program to print Pascal’s Triangle



Pascal’s triangle is a pattern of the triangle which is based on _nCr_ , below
is the pictorial representation of Pascal’s triangle.

 **Example:**

    
    
     **Input** : N = 5
    **Output:**
          1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
    

**Method 1:** Using _nCr_ formula i.e. n!/(n-r)!r!

After using nCr formula, the pictorial representation becomes:

    
    
              0C0
           1C0   1C1
        2C0   2C1   2C2
     3C0   3C1   3C2    3C3
    

**Algorithm:**

  

  

  * Take a number of rows to be printed, lets assume it to be n
  * Make outer iteration i from 0 to n times to print the rows.
  * Make inner iteration for j from 0 to (N – 1).
  * Print single blank space ” “.
  * Close inner loop (j loop) //its needed for left spacing.
  * Make inner iteration for j from 0 to i.
  * Print _nCr_ of i and j.
  * Close inner loop.
  * Print newline character (\n) after each inner iteration.

 **Implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Print Pascal's Triangle in Java

from math import factorial

 

# input n

n = 5

for i in range(n):

 for j in range(n-i+1):

 

 # for left spacing

 print(end=" ")

 

 for j in range(i+1):

 

 # nCr = n!/((n-r)!*r!)

 print(factorial(i)//(factorial(j)*factorial(i-j)),
end=" ")

 

 # for new line

 print()  
  
---  
  
 __

 __

 **Output:**

    
    
          1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
    

**Time complexity:** O(N2)

 **Method 2:** We can optimize the above code by the following concept of a
Binomial Coefficient, the i’th entry in a line number _line_ is Binomial
Coefficient _C(line, i)_ and all lines start with value 1. The idea is to
calculate _C(line, i)_ using _C(line, i-1)_.

    
    
    C(line, i) = C(line, i-1) * (line - i + 1) / i
    

**Implementations:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Print Pascal's Triangle in Java

 

# input n

n = 5

 

for i in range(1, n+1):

 for j in range(0, n-i+1):

 print(' ', end='')

 

 # first element is always 1

 C = 1

 for j in range(1, i+1):

 

 # first value in a line is always 1

 print(' ', C, sep='', end='')

 

 # using Binomial Coefficient

 C = C * (i - j) // j

 print()  
  
---  
  
 __

 __

 **Output:**

    
    
          1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
    

**Time complexity:** O(N2)

 **Method 3:** This is the most optimized approach to print Pascal’s triangle,
this approach is based on powers of 11.

    
    
    11**0 = 1
    11**1 = 11
    11**2 = 121
    11**3 = 1331
    

**Implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Print Pascal's Triangle in Python

 

# input n

n = 5

 

# iterarte upto n

for i in range(n):

 # adjust space

 print(' '*(n-i), end='')

 

 # compute power of 11

 print(' '.join(map(str, str(11**i))))  
  
---  
  
 __

 __

 **Output:**

    
    
          1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
    

**Time Complexity:** O(N)

However, this approach is applicable up to n=5 only.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

