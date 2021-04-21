What is a modulo operator (%) in Python?



When we see a ‘%’ the first thing that comes to our mind is the “Percentage-
sign”, but when we think of it from the perspective of computer language, this
sign has, in fact, another name and meaning. In computing, the **modulo
operation** (%) finds the **remainder** or **signed remainder** after the
division of one number by another (called the modulus of the operation).

Given two positive numbers, a and n, a modulo n (a % n, abbreviated as a
**mod** n) is the remainder of the **Euclidean division** of a by n, where a
is the dividend and n is the divisor.

Basically, Python modulo operation is used to get the remainder of a division.
The modulo operator( **%** ) is considered an arithmetic operation, along with
**+** , **–** , **/** , ***** , ****** , **//**. In most languages, both
operands of this modulo operator have to be an integer. But Python Modulo is
versatile in this case. The operands can be either **integer** or **float**.

 **Syntax:**

    
    
    a **%** b
    
    

Here, a is divided by b, and the remainder of that division is returned.

  

  

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# inputs

a = 13

b = 5

 

# Stores the remainder obtained 

# when dividing a by b, in c

c = a % b 

print(a, "mod", b, "=",

 c, sep = " ")

 

# inputs

d = 15.0

e = 7.0

 

# Stores the remainder obtained 

# when dividing d by e, in f

f = d % e

print(d, "mod", e, "=", 

 f, sep = " ")  
  
---  
  
 __

 __

 **Output:**

    
    
    13 mod 5 = 3
    15.0 mod 7.0 = 1.0
    

This was a simple example showing the use of the syntax, and a basic operation
performed by the modulo operator. Suppose, we want to calculate the remainder
of every number from 1 to n when divided by a fixed number k.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function is defined for finding out

# the remainder of every number from 1 to n

def findRemainder(n, k):

 

 for i in range(1, n + 1):

 # rem will store the remainder 

 # when i is divided by k.

 rem = i % k 

 

 print(i, "mod", k, "=", 

 rem, sep = " ")

 

# Driver code

if __name__ == "__main__" :

 

 # inputs

 n = 5

 k = 3

 

 # function calling

 findRemainder(n, k)  
  
---  
  
 __

 __

**Output:**

    
    
    1 mod 3 = 1
    2 mod 3 = 2
    3 mod 3 = 0
    4 mod 3 = 1
    5 mod 3 = 2
    

## Exceptions

The only Exception you get with python modulo operation is
**ZeroDivisionError**. This happens if the divider operand of the modulo
operator becomes **zero**. That means the **right operand can’t be zero**.
Let’s see the following code to know about this python exception.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# inputs

a = 14

b = 0

 

# exception handling

try:

 print(a, 'mod', b, '=',

 a % b, sep = " ")

 

except ZeroDivisionError as err:

 print('Cannot divide by zero!' +

 'Change the value of the right operand.')  
  
---  
  
 __

 __

**Output:**

    
    
    Cannot divide by zero! Change the value of the right operand.
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

