ord() function in Python



In Python, the **ord() function** accepts a string of unit length as an
argument and returns the Unicode equivalence of the passed argument. In other
words, given string of length 1, the ord() function returns an integer
representing the Unicode code point of the character when the argument is a
Unicode object, or the value of the byte when the argument is an 8-bit string.

 **Syntax:**

    
    
    ord("string")

For example, ord(‘a’) returns the integer 97, ord(‘€’) (Euro sign) returns
8364. This is the inverse of chr() for 8-bit strings and of unichr() for
Unicode objects. If a Unicode argument is given and Python is built with UCS2
Unicode, then the character’s code point must be in the range [0..65535]
inclusive.

**Note:** If the string length is more then one, and a TypeError will be
raised. The syntax can be ord(“a”) or ord(‘a’), both will give same results.

**Example:**

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# inbuilt function return an

# integer representing the Unicode code

value = ord("A")

# writing in ' ' gives the same result

value1 = ord('A')

# prints the unicode value

print value, value1  
  
---  
  
 __

 __

 **Output:**

    
    
    65 65

#### Error Condition:

A **TypeError** is raised when the length of the string is not equal to 1 as
shown below:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# inbuilt function return an

# integer representing the Unicode code

# demonstrating exception

# Raises Exception

value1 = ord('AB')

# prints the unicode value

print(value1)  
  
---  
  
 __

 __

 **Runtime Error :**

> Traceback (most recent call last):
>
> File “/home/f988dfe667cdc9a8e5658464c87ccd18.py”, line 6, in
>
> value1 = ord(‘AB’)
>
> TypeError: ord() expected a character, but string of length 2 found

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

