How to find the int value of a string in Python?



In Python, we can represent an integer value in the form of string. Int value
of a string can be obtained by using inbuilt function in python called as
**int()**. Here we can pass string as argument to this function which
returns int value of a string.

## int()

>  **Syntax :** int(string, base)  
>  **Parameters :**
>
>   *  **string :** consists of 1’s and 0’s
>   *  **base :** (integer value) base of the number.
>

>
>  **Returns :** an integer value, which is equivalent of binary string in the
> given base.  
>  **TypeError :** Returns TypeError when any data type other  
> than string or integer is passed in its equivalent position.

By default, int() assumes the number to be in decimal notation. If we want a
string representation of int which belongs to other number systems like
binary, hexadecimal, octal. We need to pass an extra argument to this function
specifying the base value. The base values are :

  * binary : 2
  * octal : 8
  * hexadecimal : 16

 **Examples :**

  

  

    
    
    **Input :** "A"  (for base 16)
    **Output :** 10
    
    **Input :** "510"
    **Output :** 510
    

__

__  
__

__

__  
__  
__

# using base 16

s1 = "A"

print(int(s1, 16))

 

# using the default base

s2 = "510"

print(int(s2))  
  
---  
  
 __

 __

 **Output :**

    
    
    10
    510
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

