Python program to convert int to exponential



Given a number of int type, the task is to write a Python program to convert
it to exponential.

 **Examples:**

    
    
     **Input:** 19
    **Output:** 1.900000e+01
    
    **Input:** 2002
    **Output:** 2.002000e+03
    
    **Input:** 110102
    **Output:** 1.101020e+05

 **Approach:**

  * We will first declare and initialise an integer number
  * Then we will use formate method to convert the number from integer to exponential type.
  * Then we will print the converted value.

 **Syntax:**

    
    
    String {field_name:conversion} Example.format(value)

 **Errors and Exceptions:**

  

  

> ValueError: Error occurs during type conversion in this method.

More parameters can be included within the curly braces of our syntax. Use the
format code syntax **{field_name: conversion}** , where field_name specifies
the index number of the argument to the **str.format() method** , and
conversion refers to the conversion code of the data type.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert int to exponential

 

# Declaring the integer number

int_number = 110102

 

# Converting the integer number to exponential number

exp_number = "{:e}".format(int_number)

 

# Printing the converted number

print("Integer Number:",int_number)

print("Exponent Number:",exp_number)  
  
---  
  
 __

 __

 **Output:**

    
    
    Integer Number: 110102
    Exponent Number: 1.101020e+05

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

