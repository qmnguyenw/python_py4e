Python program to convert float to exponential



Given a float number, the task is to write a Python program to convert float
to exponential.

 **Examples:**

    
    
     **Input:** 19.0
    **Output:** 1.900000e+01
    
    **Input:** 200.2
    **Output:** 2.002000e+02
    
    **Input:** 1101.02
    **Output:** 1.101020e+03

 **Approach:**

  * We will first declare and initialise a float number.
  * Then we will use formate method to convert the number from integer to exponential type.
  * Then we will print the converted value.

 **Syntax:**

> String {field_name:conversion} Example.format(value)
>
>  
>
>
>  
>

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

# Python program to convert float to exponential

 

# Declaring the float number

float_number = 1101.02

 

# Converting the float number to exponential number

exp_number = "{:e}".format(float_number)

 

# Printing the converted number

print("Float Number:",float_number)

print("Exponent Number:",exp_number)  
  
---  
  
 __

 __

 **Output:**

    
    
    Float Number: 1101.02
    Exponent Number: 1.101020e+03

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

