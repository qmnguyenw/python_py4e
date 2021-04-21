How to remove all decimals from a number using Python?



In python programming, sometimes it is necessary to remove all decimals from a
number to get the required output. These decimals are also called Floating
point numbers in Python. Basically, there are 3 numerical data types in
python. They are integers(int()), floating-point numbers(float()) and
complex(complex()) data types. Type conversion in python helps to convert a
decimal value number(floating number) to an integer. Thus converting
float->int removes all decimals from a number.

There are three methods for removing all decimals from a number using python

 **Methods:**

  1. Using int( ) function
  2. Using trunc( )function
  3. Using split( ) function

 **Method 1: Using int( ) [Type conversion] :**

int( ) is a built-in function used to convert any value into an integer
number.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

Number1= 44.560

Number2 = 856.9785623

Number3 = 9999.99

 

# Type conversion float to int

New_Number1 = int(Number1)

New_Number2 = int(Number2)

New_Number3 = int(Number3)

 

print("Number1 = ", New_Number1)

print("Number2 = ", New_Number2)

print("Number3 = ", New_Number3)

 

# type() function returns the data type

print(type(Number1))

print(type(New_Number1))  
  
---  
  
 __

 __

 **Output :**

    
    
    Number1 =  44
    Number2 =  856
    Number3 =  9999
    <class 'float'>
    <class 'int'>

 **Method 2: Using truncate function(trunc( )) :**

The math( ) module is a standard built-in module in python. There are numerous
mathematical functions defined in math( ) module. To use the truncate
function, first, the math module must be imported, using trunc( ) function
without defining the math( ) module gives an error. By using math.trunc( )
function a number can be truncated in python.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import math function to use trunc( ) function

import math

 

num1 = math.trunc(450.63)

print(num1)

print(math.trunc(999998.99999))

print(math.trunc(-89.99))

print(math.trunc(0.99))  
  
---  
  
 __

 __

 **Output :**

    
    
    450
    999998
    -89
    0

 **Method 3 : Using split( ) function**

The split( ) function only works on strings. Hence, the decimal values are
converted to a string using str( ) function and then split at the decimal
point. The values remain in the string data type after performing split( )
function. Therefore, the values are again converted to the integer data type.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

value1= [998.99, 56.8, 25.6, -52.0]

 

# values are split at decimal point

lst = []

for each in value1:

 lst.append(str(each).split('.')[0])

 

# all values converting to integer data type

final_list = [int(i) for i in lst]

print(final_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    [998, 56, 25, -52]

 **Note:** Using of int() function for removing all the decimal values is easy
and saves time with just a single line of code.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

