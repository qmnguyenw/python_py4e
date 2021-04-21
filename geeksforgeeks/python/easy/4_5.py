What is the meaning of invalid literal for int() with base = ‘ ‘?



 **ValueError** is encountered when we pass an inappropriate argument type.
Here, we are talking about the ValueError caused by passing an incorrect
argument to the int() function. When we pass a string representation of a
float or any string representation other than that of int, it gives a
ValueError.

 **Example 1 :** ValueError with base 10.

 __

 __  
 __

 __

 __  
 __  
 __

# ValueError caused by conversion of

# String representation of float to int

int('23.5')  
  
---  
  
 __

 __

Output :

    
    
    ValueError: invalid literal for int() with base 10: '23.5'

One can think that while executing the above code, the decimal part ‘.5’
should be truncated and the code should give output as 23 only. But the point
to be noted is that the int( ) function uses the decimal number system as its
base for conversion ie. base = 10 is the default value for conversion. And in
the decimal number system, we have numbers from 0 to 9 excluding the decimal
(.) and other characters(alphabets and special chars). Therefore, int() with
base = 10 can only convert a string representation of int and not floats or
chars.

We can first convert the string representation of float into float using
float() function and then convert it into an integer using int().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

print(int(float('23.5')))  
  
---  
  
 __

 __

 **Output :**

    
    
    23

 **Example 2 :** Passing alphabets in int().

 __

 __  
 __

 __

 __  
 __  
 __

int('abc')  
  
---  
  
 __

 __

 **Output :**

    
    
    invalid literal for int() with base 10: 'abc'

The chars a, b, c, d, e, and f are present in the base =16 system and
therefore only these chars along with digits 0 to 9 can be converted from
their string representation to integer in hexadecimal form. We have to pass an
parameter base with value 16.

 __

 __  
 __

 __

 __  
 __  
 __

print(int('abc', base = 16))  
  
---  
  
 __

 __

 **Output :**

    
    
    2748

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

