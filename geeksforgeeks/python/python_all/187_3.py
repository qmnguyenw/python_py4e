Python Program for Fibonacci numbers



The Fibonacci numbers are the numbers in the following integer sequence.  
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..  
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the
recurrence relation

    
    
        Fn = Fn-1 + Fn-2

with seed values

    
    
       F0 = 0 and F1 = 1.

 **Method 1 ( Use recursion ) :**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Function for nth Fibonacci number

def Fibonacci(n):

 

 # Check if input is 0 then it will

 # print incorrect input

 if n < 0:

 print("Incorrect input")

 # Check if n is 0

 # then it will return 0

 elif n == 0:

 return 0

 # Check if n is 1,2

 # it will return 1

 elif n == 1 or n == 2:

 return 1

 else:

 return Fibonacci(n-1) + Fibonacci(n-2)

# Driver Program

print(Fibonacci(9))

# This code is contributed by Saket Modi

# then corrected and improved by Himanshu Kanojiya  
  
---  
  
 __

 __

 **Output**

    
    
    34
    

**Method 2 ( Use Dynamic Programming ) :**

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Function for nth fibonacci

# number - Dynamic Programing

# Taking 1st two fibonacci nubers as 0 and 1

FibArray = [0, 1]

def fibonacci(n):

 

 # Check is n is less

 # than 0

 if n <= 0:

 print("Incorrect input")

 

 # Check is n is less

 # than len(FibArray)

 elif n <= len(FibArray):

 return FibArray[n - 1]

 else:

 temp_fib = fibonacci(n - 1) +

 fibonacci(n - 2)

 FibArray.append(temp_fib)

 return temp_fib

# Driver Program

print(fibonacci(9))

# This code is contributed by Saket Modi  
  
---  
  
 __

 __

 **Output**

    
    
    21
    

**Method 3 ( Space Optimized):**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Function for nth fibonacci

# number - Space Optimisataion

# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):

 a = 0

 b = 1

 

 # Check is n is less

 # than 0

 if n < 0:

 print("Incorrect input")

 

 # Check is n is equal

 # to 0

 elif n == 0:

 return 0

 

 # Check if n is equal to 1

 elif n == 1:

 return b

 else:

 for i in range(1, n):

 c = a + b

 a = b

 b = c

 return b

# Driver Program

print(fibonacci(9))

# This code is contributed by Saket Modi

# Then corrected and improved by Himanshu Kanojiya  
  
---  
  
 __

 __

 **Output**

    
    
    34
    

Please refer complete article on Program for Fibonacci numbers for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

