Decimal Functions in Python | Set 2 (logical_and(), normalize(), quantize(),
rotate() … )



Some of the Decimal functions have been discussed in Set 1 below

Decimal Functions in Python | Set 1

More functions are discussed in this article.

 **1\. logical_and()** :- This function computes digit-wise **logical “and”**
operation of the number. Digits can only have the values **0 or 1**.

 **2\. logical_or()** :- This function computes digit-wise **logical “or”**
operation of the number. Digits can only have the values **0 or 1**.

  

  

 **3\. logical_xor()** :- This function computes digit-wise **logical “xor”**
operation of the number. Digits can only have the values **0 or 1**.

 **4\. logical_invert()** :- This function computes digit-wise **logical
“invert”** operation of the number. Digits can only have the values **0 or
1**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# logical_and(), logical_or(), logical_xor()

# and logical_invert()

 

# importing "decimal" module to use decimal functions

import decimal

 

# Initializing decimal number

a = decimal.Decimal(1000)

 

# Initializing decimal number

b = decimal.Decimal(1110)

 

# printing logical_and of two numbers

print ("The logical_and() of two numbers is : ",end="")

print (a.logical_and(b))

 

# printing logical_or of two numbers

print ("The logical_or() of two numbers is : ",end="")

print (a.logical_or(b))

 

# printing exclusive or of two numbers

print ("The exclusive or of two numbers is : ",end="")

print (a.logical_xor(b))

 

# printing logical inversion of number

print ("The logical inversion of number is : ",end="")

print (a.logical_invert())  
  
---  
  
 __

 __

Output:

    
    
    The logical_and() of two numbers is : 1000
    The logical_or() of two numbers is : 1110
    The exclusive or of two numbers is : 110
    The logical inversion of number is : 1111111111111111111111110111
    

**5\. next_plus()** :- This function returns the **smallest number** that can
be represented, **larger than the given number.**

 **6\. next_minus()** :- This function returns the **largest number** that can
be represented, **smaller than the given number.**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# next_plus() and next_minus()

 

# importing "decimal" module to use decimal functions

import decimal

 

# Initializing decimal number

a = decimal.Decimal(101.34)

 

# printing the actual decimal number

print ("The original number is : ",end="")

print (a)

 

# printing number after using next_plus()

print ("The smallest number larger than current number : ",end="")

print (a.next_plus())

 

# printing number after using next_minus()

print ("The largest number smaller than current number : ",end="")

print (a.next_minus())  
  
---  
  
 __

 __

Output:

    
    
    The original number is : 101.340000000000003410605131648480892181396484375
    The smallest number larger than current number : 101.3400000000000034106051317
    The largest number smaller than current number : 101.3400000000000034106051316
    

**7\. next_toward()** :- This function returns the **number nearest to the 1st
argument in the direction of the second** argument. In case Both the numbers
are equal, returns the **2nd number with the sign of first** number.

 **8\. normalize()** :- This function prints the number after **erasing all
the rightmost trailing zeroes** in the number.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# next_toward() and normalize()

 

# importing "decimal" module to use decimal functions

import decimal

 

# Initializing decimal number

a = decimal.Decimal(101.34)

 

# Initializing decimal number

b = decimal.Decimal(-101.34)

 

# Initializing decimal number

c = decimal.Decimal(-58.68)

 

# Initializing decimal number

d = decimal.Decimal(14.010000000)

 

# printing the number using next_toward()

print ("The number closest to 1st number in direction of second number :
")

print (a.next_toward(c))

 

# printing the number using next_toward()

# when equal

print ("The second number with sign of first number is : ",end="")

print (b.next_toward(a))

 

# printing number after erasing rightmost trailing zeroes

print ("Number after erasing rightmost trailing zeroes : ",end="")

print (d.normalize())  
  
---  
  
 __

 __

Output:

    
    
    The number closest to 1st number in direction of second number : 
    101.3400000000000034106051316
    The second number with sign of first number is : -101.3400000000000034106051316
    Number after erasing rightmost trailing zeroes : 14.01
    

**9\. quantize()** :- This function returns the 1st argument with the number
of **digits in decimal part(exponent) shortened** by the **number of digits**
in **decimal part(exponent) of 2nd argument.**

 **10\. same_quantum()** :- This function **returns 0 if both the numbers have
different exponent and 1 if both numbers have same exponent.**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# quantize() and same_quantum()

 

# importing "decimal" module to use decimal functions

import decimal

 

# Initializing decimal number

a = decimal.Decimal(20.76548)

 

# Initializing decimal number

b = decimal.Decimal(12.25)

 

# Initializing decimal number

c = decimal.Decimal(6.25)

 

# printing quantized first number

print ("The quantized first number is : ",end="")

print (a.quantize(b))

 

# checking if both number have same exponent

if (b.same_quantum(c)):

 print ("Both the numbers have same exponent")

else : print ("Both numbers have different exponent")   
  
---  
  
__

__

Output:

    
    
    The quantized first number is : 20.77
    Both the numbers have same exponent
    

**11\. rotate()** :- This function **rotates** the first argument by the
**amount mentioned in the second argument**. If the sign of second argument is
**positive, rotation is towards left** , **else the rotation is towards
right**. The sign of first argument is unchanged.

 **12\. shift()** :- This function **shifts** the first argument by the
**amount mentioned in the second argument**. If the sign of second argument is
**positive, shifting is towards left,** **else the shifting is towards
right**. The sign of first argument is unchanged. Digit shifted are **replaced
by 0**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# rotate() and shift()

 

# importing "decimal" module to use decimal functions

import decimal

 

# Initializing decimal number

a = decimal.Decimal(2343509394029424234334563465)

 

# using rotate() to rotate the first argument

# rotates to right by 2 positions

print ("The rotated value is : ",end="")

print (a.rotate(-2))

 

# using shift() to shift the first argument

# rotates to left by 2 positions

print ("The shifted value is : ",end="")

print (a.shift(2))  
  
---  
  
 __

 __

Output:

    
    
    The rotated value is : 6523435093940294242343345634
    The shifted value is : 4350939402942423433456346500
    

**13\. remainder_near()** :- Returns the value “ **1st – (n*2nd)** ” where **n
is the integer value nearest to the result of 1st/2nd**. If 2 integers have
**exactly similar proximity, even one is choosen.**

 **14\. scaleb()** :- This function **shifts the exponent** of 1st number by
the **value of second argument**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# remainder_near() and scaleb()

 

# importing "decimal" module to use decimal functions

import decimal

 

# Initializing decimal number

a = decimal.Decimal(23.765)

 

# Initializing decimal number

b = decimal.Decimal(12)

 

# Initializing decimal number

c = decimal.Decimal(8)

 

# using remainder_near to compute value

print ("The computed value using remainder_near() is : ",end="")

print (b.remainder_near(c))

 

# using scaleb() to shift exponont

print ("The value after shifting exponent : ",end="")

print (a.scaleb(2))  
  
---  
  
 __

 __

Output:

    
    
    The computed value using remainder_near() is : -4
    The value after shifting exponent : 2376.500000000000056843418861
    

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

