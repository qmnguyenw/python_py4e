Python Program for Sum the digits of a given number



Given a number and the task is to find sum of digits of this number in Python.

**Examples:**  

> Input : n = 87  
> Output : 15
>
> Input : n = 111  
> Output : 3

  

  

Below are the methods to sum of the digits.  
**Method-1: Using str() and int() methods.** : The str() method is used to
convert the number to string. The int() method is used to convert the string
digit to an integer.

Convert the number to string and iterate over each digit in the string and
after conerting each digit to integer and add to the sum of the digits in each
iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# compute sum of digits in 

# number. 

 

# Function to get sum of digits 

def getSum(n): 

 

 sum = 0

 for digit in str(n): 

 sum += int(digit) 

 return sum

 

n = 12345

print(getSum(n))  
  
---  
  
 __

 __

 **Output:**

    
    
    15

 **Method-2: Using sum() methods.:** The sum() method is used to sum of
numbers in the list.

Convert the number to string using str() and strip the string and convert to
list of number using strip() and map() method resp. Then find the sum using
the sum() method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# compute sum of digits in 

# number. 

 

# Function to get sum of digits 

def getSum(n): 

 

 strr = str(n)

 list_of_number = list(map(int, strr.strip()))

 return sum(list_of_number)

 

n = 12345

print(getSum(n))  
  
---  
  
 __

 __

 **Output:**

    
    
    15

 **Method-3: Using General Approach:**

  * Get the number
  * Declare a variable to store the sum and set it to 0
  * Repeat the next two steps till the number is not 0
  * Get the rightmost digit of the number with help of remainder ‘%’ operator by dividing it with 10 and add it to sum.
  * Divide the number by 10 with help of ‘//’ operator
  * Print or return the sum 

**A. Iterative Approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to

# compute sum of digits in 

# number. 

 

# Function to get sum of digits 

def getSum(n): 

 

 sum = 0

 while (n != 0): 

 

 sum = sum + (n % 10)

 n = n//10

 

 return sum

 

n = 12345

print(getSum(n))  
  
---  
  
 __

 __

 **Output:**

    
    
    15

 **B. Recursive Approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to compute

# sum of digits in number. 

 

def sumDigits(no): 

 return 0 if no == 0 else int(no % 10) +
sumDigits(int(no / 10)) 

 

# Driver code 

n = 12345

print(sumDigits(n))  
  
---  
  
 __

 __

 **Output:**

    
    
    15

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

