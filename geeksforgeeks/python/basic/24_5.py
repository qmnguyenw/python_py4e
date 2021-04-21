round() function in Python



Python provides an inbuilt function **round()** which rounds off to the given
number of digits and returns the floating point number, if no number of digits
is provided for round off , it rounds off the number to the nearest integer.  
 **Syntax:**  

    
    
    round(number, number of digits)
    
    

**round() parameters:**  

    
    
    ..1) number - number to be rounded
    ..2) number of digits (Optional) - number of digits 
         up to which the given number is to be rounded.
    
    

If the second parameter is **missing** , then round() function **returns** :  
..a) if only an integer is given , as 15 , then it will round off to 15.  
..b) if a decimal number is given , then it will round off to the **ceil**
integer after that if decimal value has >=5 , and it will round off to the
**floor** integer if decimal is <5.  
 _Below is the python implementation of the round() function if the second
parameter is missing._  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# for integers

print(round(15))

# for floating point

print(round(51.6))

print(round(51.5)) 

print(round(51.4))  
  
---  
  
 __

 __

 **Output:**  

    
    
    15
    52
    52
    51
    
    

When the second parameter is **present** , then it **returns:**  
The last decimal digit till which it is rounded is increased by 1 when
(ndigit+1)th digit is >=5 , else it stays the same.  
 _Below is the python implementation of the round() function if the second
parameter is present_  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# when the (ndigit+1)th digit is =5

print(round(2.665, 2))

# when the (ndigit+1)th digit is >=5

print(round(2.676, 2)) 

# when the (ndigit+1)th digit is <5

print(round(2.673, 2))   
  
---  
  
__

__

**Output:**  

    
    
    2.67
    2.68
    2.67
    
    

**Error and Exceptions**  
TypeError : This error is raised in the case when there is anything other than
numbers in the parameters.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

print(round("a", 2))   
  
---  
  
__

__

**Output:**  

    
    
    **Runtime Errors:**
    Traceback (most recent call last):
      File "/home/ccdcfc451ab046030492e0e758d42461.py", line 1, in 
        print(round("a", 2))  
    TypeError: type str doesn't define __round__ method
    
    

**Practical Applications:**  
One of the common uses of rounding of functions is Handling the mismatch
between fractions and decimal .  
One use of rounding numbers is shorten all the three’s to the right of the
decimal point in converting 1/3 to decimal. Most of the time, you will use the
rounded numbers 0.33 or 0.333 when you need to work with 1/3 in decimal. In
fact, you usually work with just two or three digits to the right of the
decimal point when there is no exact equivalent to the fraction in decimal.
How would you show 1/6 in decimal? Remember to round up!  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# practical application

b = 1/3

print(b)

print(round(b, 2))  
  
---  
  
 __

 __

 **Output:**  

    
    
    0.3333333333333333
    0.33
    
    

**Note:** In python if we round of numbers to floor or ceil without giving the
second parameter , it will return 15.0 for example and in Python 3 it returns
15 , so to avoid this we can use (int) type conversion in python.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

