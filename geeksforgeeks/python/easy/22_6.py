f-strings in Python



PEP 498 introduced a new string formatting mechanism known as _Literal String
Interpolation_ or more commonly as _F-strings_ (because of the leading _f_
character preceding the string literal). The idea behind f-strings is to make
string interpolation simpler.  
To create an f-string, prefix the string with the letter “ f ”. The string
itself can be formatted in much the same way that you would with str.format().
F-strings provide a concise and convenient way to embed python expressions
inside string literals for formatting.  
  
**Code #1 :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program introducing f-string

val = 'Geeks'

print(f"{val}for{val} is a portal for {val}.")

name = 'Tushar'

age = 23

print(f"Hello, My name is {name} and I'm {age} years old.")  
  
---  
  
 __

 __

 **Output :**  

    
    
    GeeksforGeeks is a portal for Geeks.
    Hello, My name is Tushar and I'm 23 years old.

  
**Code #2 :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Prints today's date with help

# of datetime library

import datetime

today = datetime.datetime.today()

print(f"{today:%B %d, %Y}")  
  
---  
  
 __

 __

 **Output :**  

    
    
    April 04, 2018

  
**Note :** F-strings are faster than the two most commonly used string
formatting mechanisms, which are % formatting and str.format().  
  
Let’s see few error examples, which might occur while using f-string :  
 **Code #3 :** Demonstrating Syntax error.  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

answer= 456

f"Your answer is "{answer}""  
  
---  
  
 __

 __

 **Code #4 :** Backslash Cannot be used in format string directly.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

f"newline: {ord('\n')}"  
  
---  
  
 __

 __

 **Output :**  

    
    
    Traceback (most recent call last):
      Python Shell, prompt 29, line 1
    Syntax Error: f-string expression part cannot include a backslash: , line 1, pos 0

  
But the documentation points out that we can put the backslash into a variable
as a workaround though :  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

newline= ord('\n')

f"newline: {newline}"  
  
---  
  
 __

 __

 **Output :**  

    
    
    newline: 10

 **Reference :**PEP 498, Literal String Interpolation  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

