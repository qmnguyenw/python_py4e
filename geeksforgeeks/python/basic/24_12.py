float() in Python



The float() method is used to return a floating point number from a number or
a string.  
 **Syntax:**

    
    
     **float(x)**

The method only accepts one parameter and that is also optional to use. Let us
look at the various types of argument, the method accepts:

  1.  **A number :** Can be an Integer or a floating point number.
  2.  **A String :**
    * Must contain numbers of any type.
    * Any left or right whitespaces or a new line is ignored by the method.
    * Mathematical Operators can be used.
    * Can contain NaN, Infinity or inf (any cases)

 **Values that the float() method can return depending upon the argument
passed**

  * If an argument is passed, then the equivalent floating point number is returned.
  * If no argument is passed then the method returns 0.0 .
  * If any string is passed that is not a decimal point number or does not match to any cases mentioned above then an error will be raised.
  * If a number is passed outside the range of Python float then OverflowError is generated.

Now let us look at various examples and the working of float() method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# Various examples and working of float()

# for integers

print(float(21.89))

 

# for floating point numbers

print(float(8))

 

# for integer type strings

print(float("23"))

 

# for floating type strings

print(float("-16.54"))

 

# for string floats with whitespaces

print(float(" -24.45 \n"))

 

# for inf/infinity

print(float("InF"))

print(float("InFiNiTy"))

 

# for NaN

print(float("nan"))

print(float("NaN"))

 

# Error is generated at last

print(float("Geeks"))  
  
---  
  
 __

 __

Output:

  

  

    
    
    21.89
    8.0
    23.0
    -16.54
    -24.45
    inf
    inf
    nan
    nan
    

All lines are executed properly but the last one which will return an error:

    
    
    Traceback (most recent call last):
      File "/home/21499f1e9ca207f0052f13d64cb6be31.py", line 25, in 
        print(float("Geeks"))
    ValueError: could not convert string to float: 'Geeks'

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

