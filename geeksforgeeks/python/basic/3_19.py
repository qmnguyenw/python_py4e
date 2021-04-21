What are the allowed characters in Python function names?



The **user-defined** names that are given to Functions or variables are known
as Identifiers. It helps in differentiating one entity from another and also
serves as a definition of the use of that entity sometimes. As in every
programming language, there are some restrictions/ limitations for
Identifiers. So, is the case with Python, we need to take care of the
following points before using an Identifier.

 **Rules for writing Identifiers:**

  * The first and foremost restriction is that Identifiers cannot be the same as Keywords. There are special reserved keywords in every programming language that has its own meaning and these names can’t be used as Identifiers in Python.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# that keywords cant be used as

# identifiers

 

def calculate_sum(a, b):

 return a + b

 

x = 2

y = 5

print(calculate_sum(x,y))

 

# def and if is a keyword, so

# this would give invalid 

# syntax error

def = 12

if = 2

 

print(calculate_sum(def, if))  
  
---  
  
 __

 __

 **Output:**

    
    
     File "/home/9efd6943df820475cf5bc74fc4fcc3aa.py", line 15
        def = 12   
            ^
    SyntaxError: invalid syntax
    

  * An identifier in Python cannot use any special symbols like !, @, #, $, % etc.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demostrate

# that we can't use special

# character like !,@,#,$,%.etc

# as identifier

 

# valid identifier

var1 = 46

var2 = 23

print(var1 * var2)

 

# invalid identifier, 

# will give invalid syntax error

var@ = 12

$var = 55

print(var@ * $var)

 

# even function names can't

# have special characters

def my_function%():

 print('This is a function with invalid identifier')

 

my_function%()  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    File "/home/3ae3b1299ee9c1c04566e45e98b13791.py", line 13
        var@ = 12  
             ^
    SyntaxError: invalid syntax
    

  * Apart from these restrictions, Python allows Identifiers to be a combination of lowercase letters (a to z) or uppercase letters (A to Z) or digits (0 to 9) or an underscore (_). But variable name must not be started with digits. Names like myClass, var_3, and print_to_screen, are valid examples.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demostrate

# some examples of valid identifiers

 

var1 = 101

ABC = "This is a string"

fr12 = 20

x_y = 'GfG'

slp__72 = ' QWERTY'

 

print(var1 * fr12)

 

print(ABC + slp__72)  
  
---  
  
 __

 __

 **Output:**

    
    
    2020
    This is a string QWERTY
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

