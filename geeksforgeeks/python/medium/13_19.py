Floating point error in Python



As it is know that 1.2 - 1.0 = 0.2 . But when you try to the same in python
you will surprised by results:

    
    
    >>> 1.2 - 1.0
    

**Output:**

    
    
    0.199999999999999996

This can be considered as a bug in Python, but it is not. This has little to
do with Python, and much more to do with how the underlying platform handles
floating-point numbers. It’s a normal case encountered when handling floating-
point numbers internally in a system. It’s a problem caused when the internal
representation of floating-point numbers, which uses a fixed number of binary
digits to represent a decimal number. It is difficult to represent some
decimal number in binary, so in many cases, it leads to small roundoff errors.

We know similar cases in decimal math, there are many results that can’t be
represented with a fixed number of decimal digits,  
 **Example**

    
    
    10 / 3 = 3.33333333.......

In this case, taking 1.2 as an example, the representation of 0.2 in binary
is 0.00110011001100110011001100...... and so on.  
It is difficult to store this infinite decimal number internally. Normally a
float object’s value is stored in binary floating-point with a fixed precision
( **typically 53 bits** ).

  

  

So we represent **1.2** internally as,

    
    
    1.0011001100110011001100110011001100110011001100110011  

Which is exactly equal to :

    
    
    1.1999999999999999555910790149937383830547332763671875

Still, you thinking why **python is not solving this issue** , actually it has
nothing to do with python. It happens because it is the way the underlying c
platform handles floating-point numbers and ultimately with the inaccuracy,
we’ll always have been writing down numbers as a string of fixed number of
digits.

Note that this is in the very nature of binary floating-point: this is not a
bug either in **Python** or **C** , and it is not a bug in your code either.
You’ll see the same kind of behaviors in all languages that support our
hardware’s floating-point arithmetic although some languages may not display
the difference by default, or in all output modes). We have to consider this
behavior when we do care about math problems with needs exact precisions or
using it inside conditional statements.  
Check floating point section in python documentation for more such behaviours.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

