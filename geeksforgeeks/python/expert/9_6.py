oct() function in Python



 ** _oct()_** function is one of the built-in methods in Python3. The oct()
method takes an integer and returns it’s octal representation in a string
format.

>  **Syntax :** **oct(x)**
>
>  **Parameters :**
>
>  **x** – Must be an integer number and can be in either binary, decimal or
> hexadecimal format.
>
>  **Returns :** octal representation of the value.
>
>  
>
>
>  
>
>
>  **Errors and Exceptions :**  
>  **TypeError :** Returns TypeError when anything other than integer type
> constants are passed as parameters.

  
**Code #1 :** Illustrates the use of **oct()** function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate

# the use of oct() function

 

print("The octal representation of 23 is " + oct(23))

 

print("The octal representation of the"

 " ascii value of 'z' is " + oct(ord('z')))

 

# Binary representation of a number

# can be passed as a parameter

 

# For 23, Binary is 0b10111

print("The octal representation of the binary"

 " of 23 is " + oct(0b10111))

 

# For 23, Hexadecimal is 0x17

print("The octal representation of the binary"

 " of 23 is " + oct(0x17))  
  
---  
  
 __

 __

 **Output :**

    
    
    The octal representation of 23 is 0o27
    The octal representation of the ascii value of 'z' is 0o172
    The octal representation of the binary of 23 is 0o27
    The octal representation of the binary of 23 is 0o27
    

  
**Code #2 :** Demonstrate TypeError

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program demonstrating TypeError

 

print("The Octal representation of 29.5 is " + oct(29.5))

 

'''

# Python doesn't have anything like float.oct()

# to directly convert a floating type constant

# to its octal representation. Conversion of a

# floating-point value to it's octal is done manually.

'''  
  
---  
  
 __

 __

 **Output :**

    
    
    Traceback (most recent call last):
      File "/home/5bf02b72de26687389763e9133669972.py", line 3, in 
        print("The Octal representation of 29.5 is "+oct(29.5))
    TypeError: 'float' object cannot be interpreted as an integer
    

  
**Applications :**  
oct() is used in all types of **standard conversion**. For example, Conversion
from decimal to octal, binary to octal, hexadecimal to octal forms
respectively.  
 **Code #3 :**

 __

 __  
 __

 __

 __  
 __  
 __

# TypeConversions from decimal and binary

# to their respective octal representations

 

# The choices present to the user

print("a. Hexadecimal to Octal ")

print("b. Decimal to Octal")

print("c. Binary to Octal")

 

# Function generates octal representation 

# from it's binary from

def bin_to_oct():

 

 print("Enter your input in BIN format :-")

 

 # taking user input as binary string and 

 # then using int() to convert it into it's

 # respective decimal format

 x = int(input(), 2)

 print("Octal form of " + str(x) + " is " + oct(x) )

 

 

# Function generates octal representation

# of it's hexadecimal form passed as value.

def hex_to_oct():

 print("Enter your input in HEX format :-")

 

 # taking user input as hexadecimal string and 

 # then using int() to convert it into it's

 # respective decimal format

 x = int(input(), 16)

 print("Octal form of " + str(x) + " is " + oct(x))

 

 

# Function converts decimal form to it's 

# respective octal representation

def decimal_to_oct():

 

 print("Enter a number with base-10 format :-")

 

 # taking a simple user input and 

 # converting it to an integer

 x = int(input())

 print("Octal form of " + str(x) + " is " + oct(x))

 

 

# Driver Code

ch = input("Enter your choice :-\n")

 

if ch is 'a':

 hex_to_oct()

elif ch is 'b':

 decimal_to_oct()

elif ch is 'c':

 bin_to_oct()  
  
---  
  
 __

 __

 **Output :**

    
    
    a. Hexadecimal to Octal 
    b. Decimal to Octal
    c. Binary to Octal
    Enter your choice :-
    a
    Enter your input in HEX format :-
    0x13
    Octal form of 19 is 0o23
    
    
    
    a. Hexadecimal to Octal 
    b. Decimal to Octal
    c. Binary to Octal
    Enter your choice :-
    b
    Enter a number with base-10 format :-
    123
    Octal form of 123 is 0o173
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

