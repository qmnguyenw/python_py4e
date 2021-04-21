Decimal Functions in Python | Set 1



Python in its definition provides certain methods to perform faster decimal
floating point arithmetic using the module “decimal”.

 **Important operations on Decimals**

 **1\. sqrt()** :- This function computes the **square root** of the decimal
number.

 **2\. exp()** :- This function returns the **e^x (exponent)** of the decimal
number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# sqrt() and exp()

 

# importing "decimal" module to use decimal functions

import decimal

 

# using exp() to compute the exponent of decimal number

a = decimal.Decimal(4.5).exp()

 

# using sqrt() to compute the square root of decimal number

b = decimal.Decimal(4.5).sqrt()

 

# printing the exponent

print ("The exponent of decimal number is : ",end="")

print (a)

 

# printing the square root

print ("The square root of decimal number is : ",end="")

print (b)  
  
---  
  
 __

 __

Output:

  

  

    
    
    The exponent of decimal number is : 90.01713130052181355011545675
    The square root of decimal number is : 2.121320343559642573202533086
    

**3\. ln()** :- This function is used to compute **natural logarithm** of the
decimal number.

 **4\. log10()** :- This function is used to compute **log(base 10)** of a
decimal number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# ln() and log10()

 

# importing "decimal" module to use decimal functions

import decimal

 

# using ln() to compute the natural log of decimal number

a = decimal.Decimal(4.5).ln()

 

# using sqrt() to compute the log10 of decimal number

b = decimal.Decimal(4.5).log10()

 

# printing the natural logarithm

print ("The natural logarithm of decimal number is : ",end="")

print (a)

 

# printing the log10

print ("The log(base 10) of decimal number is : ",end="")

print (b)  
  
---  
  
 __

 __

Output:

    
    
    The natural logarithm of decimal number is : 1.504077396776274073373258352
    The log(base 10) of decimal number is : 0.6532125137753436793763169118
    

**5\. as_tuple()** :- Returns the decimal number as tuple containing **3
arguments, sign(0 for +, 1 for -), digits and exponent value**.

 **6\. fma(a,b)** :- This “fma” stands for **fused multiply and add**. It
computes **(num*a)+b** from the numbers in argument. **No rounding of
(num*a)** takes place in this function.

 **Example :**

    
    
    decimal.Decimal(5).fma(2,3) --> (5*2)+3 = 13
    

__

__  
__

__

__  
__  
__

# Python code to demonstrate the working of

# as_tuple() and fma()

 

# importing "decimal" module to use decimal functions

import decimal

 

# using as_tuple() to return decimal number as tuple

a = decimal.Decimal(-4.5).as_tuple()

 

# using fma() to compute fused multiply and addition

b = decimal.Decimal(5).fma(2,3)

 

# printing the tuple

print ("The tuple form of decimal number is : ",end="")

print (a)

 

# printing the fused multiple and addition

print ("The fused multiply and addition of decimal number is :
",end="")

print (b)  
  
---  
  
 __

 __

Output:

    
    
    The tuple form of decimal number is : DecimalTuple(sign=1, digits=(4, 5), exponent=-1)
    The fused multiply and addition of decimal number is : 13
    

**7\. compare()** :- This function is used to compare decimal numbers.
**Returns 1 if 1st Decimal argument is greater than 2nd, -1 if 1st Decimal
argument is smaller than 2nd and 0 if both are equal.**

  

  

 **8\. compare_total_mag()** :- Compares the total magnitute of decimal
numbers. **Returns 1 if 1st Decimal argument is greater than 2nd(ignoring
sign), -1 if 1st Decimal argument is smaller than 2nd(ignoring sign) and 0 if
both are equal(ignoring sign).**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# compare() and compare_total_mag()

 

# importing "decimal" module to use decimal functions

import decimal

 

# Initializing decimal number

a = decimal.Decimal(9.53)

 

# Initializing decimal number

b = decimal.Decimal(-9.56)

 

# comparing decimal numbers using compare()

print ("The result of comparison using compare() is : ",end="")

print (a.compare(b))

 

# comparing decimal numbers using compare_total_mag()

print ("The result of comparison using compare_total_mag() is :
",end="")

print (a.compare_total_mag(b))  
  
---  
  
 __

 __

Output:

    
    
    The result of comparison using compare() is : 1
    The result of comparison using compare_total_mag() is : -1
    

**9\. copy_abs()** :- This function prints the **absolute** value of decimal
argument.

 **10\. copy_negate()** :- This function prints the **negation** of decimal
argument.

 **11\. copy_sign()** :- This function prints the **first argument by copying
the sign from 2nd argument**.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# copy_abs(),copy_sign() and copy_negate()

 

# importing "decimal" module to use decimal functions

import decimal

 

# Initializing decimal number

a = decimal.Decimal(9.53)

 

# Initializing decimal number

b = decimal.Decimal(-9.56)

 

# printing absolute value using copy_abs()

print ("The absolute value using copy_abs() is : ",end="")

print (b.copy_abs())

 

# printing negated value using copy_negate()

print ("The negated value using copy_negate() is : ",end="")

print (b.copy_negate())

 

# printing sign effected value using copy_sign()

print ("The sign effected value using copy_sign() is : ",end="")

print (a.copy_sign(b))  
  
---  
  
 __

 __

Output:

    
    
    The absolute value using copy_abs() is : 9.5600000000000004973799150320701301097869873046875
    The negated value using copy_negate() is : 9.5600000000000004973799150320701301097869873046875
    The sign effected value using copy_sign() is : -9.5299999999999993605115378159098327159881591796875
    

**12\. max()** :- This function computes the **maximum** of two decimal
numbers.

 **13\. min()** :- This function computes the **minimum** of two decimal
numbers.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# min() and max()

 

# importing "decimal" module to use decimal functions

import decimal

 

# Initializing decimal number

a = decimal.Decimal(9.53)

 

# Initializing decimal number

b = decimal.Decimal(7.43)

 

# printing minimum of both values

print ("The minimum of two numbers is : ",end="")

print (a.min(b))

 

# printing maximum of both values

print ("The maximum of two numbers is : ",end="")

print (a.max(b))  
  
---  
  
 __

 __

Output:

    
    
    The minimum of two numbers is : 7.429999999999999715782905696
    The maximum of two numbers is : 9.529999999999999360511537816
    

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

