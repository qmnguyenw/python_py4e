Python program to add two Octal numbers



Given two octal numbers, the task is to write a Python program to compute
their sum.

 **Examples:**

    
    
     **Input:** a = "123", b = "456"
    **Output:** 601
    
    **Input:** a = "654", b = "321"
    **Output:** 1175

 **Approach:**

To add two octal values in python we will first convert them into decimal
values then add them and then finally again convert them to an octal value. To
convert the numbers we will make use of the **oct()** function. The _oct()_
function is one of the built-in methods in Python3. The _oct()_ method takes
an integer and returns its octal representation in a string format. We will
also use the **int()** function to convert the number to decimal form. The
_int()_ function in Python and Python3 converts a number in the given base to
decimal.

 **Below are the implementations based on the above explanation:**

  

  

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to add two hexadecimal numbers.

 

# Driver code

# Declaring the variables

a = "123"

b = "456"

 

# Calculating octal value using function

sum = oct(int(a, 8) + int(b, 8))

 

# Printing result

print(sum[2:])  
  
---  
  
 __

 __

 **Output:**

    
    
    601

**Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to add two hexadecimal numbers.

 

# Driver code

# Declaring the variables

a = "654"

b = "321"

 

# Calculating octal value using function

sum = oct(int(a, 8) + int(b, 8))

 

# Printing result

print(sum[2:])  
  
---  
  
 __

 __

 **Output:**

    
    
    1175

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

