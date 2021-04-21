Convert Decimal to String in Python



Python defines type conversion functions to directly convert one data type to
another. This article is aimed at providing the information about converting
decimal to string.

## Converting Decimal to String

str() method can be used to convert decimal to string in Python.

>  **Syntax:** str(object, encoding=’utf-8?, errors=’strict’)
>
>  **Parameters:**
>
>  **object:** The object whose string representation is to be returned.
>
>  
>
>
>  
>
>
>  **encoding:** Encoding of the given object.
>
>  **errors:** Response when decoding fails.

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from decimal import Decimal

 

dec = Decimal(10)

print(dec, type(dec))

 

# Converting to string

dec = str(dec)

print(dec, type(dec))  
  
---  
  
 __

 __

 **Output:**

    
    
    10 <class 'decimal.Decimal'>
    10 <class 'str'>

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from decimal import Decimal

 

 

dec = Decimal("0.01")

print(dec, type(dec))

 

# Converting decimal to string

s = str(dec)

print(s, type(dec))  
  
---  
  
 __

 __

 **Output:**

    
    
    0.01 <class 'decimal.Decimal'>
    0.01 <class 'decimal.Decimal'>

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

