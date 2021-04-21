abs() in Python



The abs() function is used to return the absolute value of a number.  
 **Syntax:**

    
    
    **abs(number)**
    
    **number :** Can be integer, a floating point
    number or a complex number
    

The abs() takes only one argument, a number whose absolute value is to be
returned. The argument can be an integer, a floating point number or a complex
number.

  * If the argument is an integer or floating point number, abs() returns the absolute value in integer or float.
  * In case of complex number, abs() returns only the magnitude part and that can also be a floating point number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate

# abs() built-in function

 

# floating point number

float = -54.26

print('Absolute value of float is:', abs(float))

 

# An integer

int = -94

print('Absolute value of integer is:', abs(int))

 

# A complex number

complex = (3 - 4j)

print('Absolute value or Magnitude of complex is:',
abs(complex))  
  
---  
  
 __

 __

Output:

    
    
    Absolute value of float is: 54.26
    Absolute value of integer is: 94
    Absolute value or Magnitude of complex is: 5.0
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

