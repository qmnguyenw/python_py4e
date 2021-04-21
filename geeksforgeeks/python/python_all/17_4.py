Python Program to add two hexadecimal numbers



Given two hexadecimal numbers, write a Python program to compute their sum.

 **Examples:**

>  **Input:** a = “01B”, b = “378”  
>  **Output:** 393  
>  **Explanation:**  
>  B (11 in decimal) + 8 = 19 (13 in hex), hence addition bit = 3, carry = 1  
> 1 + 7 + 1 (carry) = 9, hence addition bit = 9, carry = 0  
> 0 + 3 + 0 (carry) = 3, hence addition bit = 3, carry = 0  
> 01B + 378 = 393
>
>  **Input:** a = “AD”, b = “1B”  
>  **Output:** C8  
>  **Explanation:**  
>  D(13 in Dec) + B(11 in Dec) = 24(18 in hex), hence addition bit = 8, carry
> = 1  
> A(10 in Dec) + 1 + 1 (carry)= 12 (C in hex), addition bit = C carry = 0  
> AD + 1B = C8

 **Approach:**

  

  

To add two hexadecimal values in python we will first convert them into
decimal values then add them and then finally again convert them to a
hexadecimal value. To convert the numbers we will make use of the
**hex()**function The _hex(_ ) function is one of the built-in functions in
Python3, which is used to convert an integer number into its corresponding
hexadecimal form. We will also use the **int()**function to convert the number
to decimal form. The _int()_ function in Python and Python3 converts a number
in the given base to decimal.

 **Below are the implementations based on the above approach:**

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

a = "01B"

b = "378"

 

# Calculating hexadecimal value using function

sum = hex(int(a, 16) + int(b, 16))

 

# Printing result

print(sum[2:])  
  
---  
  
 __

 __

 **Output:**

    
    
    393

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

a = "B"

b = "C"

 

# Calculating hexadecimal value using function

sum = hex(int(a, 16) + int(b, 16))

 

# Printing result

print(sum[2:])  
  
---  
  
 __

 __

 **Output:**

    
    
    17

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

