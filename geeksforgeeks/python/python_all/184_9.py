Python Program for factorial of a number



Factorial of a non-negative integer, is multiplication of all integers smaller
than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.

![factorial](https://www.geeksforgeeks.org/wp-content/uploads/factorial.png)

 **Recursive :**

## python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to find

# factorial of given number

def factorial(n):

 

 # single line to find factorial

 return 1 if (n==1 or n==0) else n *
factorial(n - 1);

# Driver Code

num = 5;

print("Factorial of",num,"is",

factorial(num))

# This code is contributed by Smitha Dinesh Semwal  
  
---  
  
 __

 __

 **Iterative:**

## python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to find

# factorial of given number

def factorial(n):

 if n < 0:

 return 0

 elif n == 0 or n == 1:

 return 1

 else:

 fact = 1

 while(n > 1):

 fact *= n

 n -= 1

 return fact

# Driver Code

num = 5;

print("Factorial of",num,"is",

factorial(num))

# This code is contributed by Dharmik Thakkar  
  
---  
  
 __

 __

 **One line Solution (Using Ternary operator):**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to find

# factorial of given number

def factorial(n):

 # single line to find factorial

 return 1 if (n==1 or n==0) else n *
factorial(n - 1)

# Driver Code

num = 5

print ("Factorial of",num,"is",

 factorial(num))

# This code is contributed

# by Smitha Dinesh Semwal.  
  
---  
  
 __

 __

Please refer complete article onProgram for factorial of a number for more
details!

 **By using In-built function:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to find

# factorial of given number

import math

def factorial(n):

 return(math.factorial(n))

# Driver Code

num = 5

print("Factorial of", num, "is",

 factorial(num))

# This code is contributed by Ashutosh Pandit  
  
---  
  
 __

 __

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

