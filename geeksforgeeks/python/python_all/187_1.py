Python Program for n-th Fibonacci number



In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the
recurrence relation

    
    
    Fn = Fn-1 + Fn-2
    

With seed values  

    
    
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

 if n<0:

 print("Incorrect input")

 # First Fibonacci number is 0

 elif n==1:

 return 0

 # Second Fibonacci number is 1

 elif n==2:

 return 1

 else:

 return Fibonacci(n-1)+Fibonacci(n-2)

 

# Driver Program

 

print(Fibonacci(9))

 

#This code is contributed by Saket Modi  
  
---  
  
 __

 __

 **Output:**

    
    
    21
    

**Method 2 ( Use Dynamic Programming ) :**  

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Function for nth fibonacci number - Dynamic Programing

# Taking 1st two fibonacci nubers as 0 and 1

 

FibArray = [0,1]

 

def fibonacci(n):

 if n<0:

 print("Incorrect input")

 elif n<=len(FibArray):

 return FibArray[n-1]

 else:

 temp_fib = fibonacci(n-1)+fibonacci(n-2)

 FibArray.append(temp_fib)

 return temp_fib

 

# Driver Program

 

print(fibonacci(9))

 

#This code is contributed by Saket Modi  
  
---  
  
 __

 __

 **Output:**

    
    
    21
    

**Method 3 ( Use Dynamic Programming with Space Optimization) :**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Function for nth fibonacci number - Space Optimisataion

# Taking 1st two fibonacci numbers as 0 and 1

 

def fibonacci(n):

 a = 0

 b = 1

 if n < 0:

 print("Incorrect input")

 elif n == 0:

 return a

 elif n == 1:

 return b

 else:

 for i in range(2,n):

 c = a + b

 a = b

 b = c

 return b

 

# Driver Program

 

print(fibonacci(9))

 

#This code is contributed by Saket Modi  
  
---  
  
 __

 __

 **Output:**

    
    
    21
    
    

**Method 4 ( Using Arrays ) :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#creating an array in the function to find the nth number in fibonacci
series. [0,1,1,...]

 

def fibonacci (n):

 

 arr = [0] * (n+1)

 

 arr[1] = 1

 

 for i in range (2,n+1):

 

 arr[i] = arr[i-1] + arr[i-2]

 

 return arr[n]

 

#Driver Program

 

if __name__ == "__main__":

 

 print(fibonacci (int (input ("Enter the term :" ) ) ) )
#lets assume the input as 12

 

# This Code is contributed by Prasun Parate (prasun_parate)  
  
---  
  
 __

 __

 **Output :**

    
    
    144
    

**Explanation:**

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]  
As we know that the Fibonacci series is the sum of the previous two terms, so
if we enter 12 as the input in the program, so we should get 144 as the
output. And that is what is the result.

Please refer complete article on Program for Fibonacci numbers for more
details!  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

