Python program to convert exponential to float



Given a number in exponential format, the task is to write a Python program to
convert the number from exponential format to float. The exponential number is
a way of representing a number.

 **Examples:**

    
    
     **Input:** 1.900000e+01
    **Output:** 19.0
    
    **Input:** 2.002000e+03
    **Output:** 2002.0
    
    **Input:** 1.101020e+05
    **Output:** 110102.0

 **Approach:**

  * First, we will declare an exponential number and save it in a variable.
  * Then we will use the **float() function** to convert it to float datatype.
  * Then we will print the converted number.

 **Syntax:**

    
    
    float(x)

The **float() method** is used to return a floating-point number from a number
or a string.

  

  

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert exponential to float

 

# Declaring the exponential number

exp_number = "{:e}".format(110102)

 

# Converting it to float data type

float_number = float(exp_number)

 

# Printing the converted number

print("Exponent Number:",exp_number)

print("Float Number:",float_number)  
  
---  
  
 __

 __

 **Output:**

    
    
    Exponent Number: 1.101020e+05
    Float Number: 110102.0

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

