Operator Functions in Python | Set 1



Python has predefined functions for many mathematical, logical, relational,
bitwise etc operations under the module “operator”. Some of the basic
functions are covered in this article.

 **1\. add(a, b)** :- This functions returns **addition** of the given
arguments.  
Operation – **a + b.**

 **2\. sub(a, b)** :- This functions returns **difference** of the given
arguments.  
Operation – **a – b.**

 **3\. mul(a, b)** :- This functions returns **product** of the given
arguments.  
Operation – **a * b.**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# add(), sub(), mul()

 

# importing operator module 

import operator

 

# Initializing variables

a = 4

 

b = 3

 

# using add() to add two numbers

print ("The addition of numbers is :",end="");

print (operator.add(a, b))

 

# using sub() to subtract two numbers

print ("The difference of numbers is :",end="");

print (operator.sub(a, b))

 

# using mul() to multiply two numbers

print ("The product of numbers is :",end="");

print (operator.mul(a, b))  
  
---  
  
 __

 __

Output:

  

  

    
    
    The addition of numbers is :7
    The difference of numbers is :1
    The product of numbers is :12
    

**4\. truediv(a,b)** :- This functions returns **division** of the given
arguments.  
Operation – **a / b.**

 **5\. floordiv(a,b)** :- This functions also returns division of the given
arguments. But the value is floored value i.e. **returns greatest small
integer**.  
Operation – **a // b.**

 **6\. pow(a,b)** :- This functions returns **exponentiation** of the given
arguments.  
Operation – **a ** b.**

 **7\. mod(a,b)** :- This functions returns **modulus** of the given
arguments.  
Operation – **a % b.**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# truediv(), floordiv(), pow(), mod()

 

# importing operator module 

import operator

 

# Initializing variables

a = 5

 

b = 2

 

# using truediv() to divide two numbers

print ("The true division of numbers is : ",end="");

print (operator.truediv(a,b))

 

# using floordiv() to divide two numbers

print ("The floor division of numbers is : ",end="");

print (operator.floordiv(a,b))

 

# using pow() to exponentiate two numbers

print ("The exponentiation of numbers is : ",end="");

print (operator.pow(a,b))

 

# using mod() to take modulus of two numbers

print ("The modulus of numbers is : ",end="");

print (operator.mod(a,b))  
  
---  
  
 __

 __

Output:

    
    
    The true division of numbers is : 2.5
    The floor division of numbers is : 2
    The exponentiation of numbers is : 25
    The modulus of numbers is : 1
    

**8\. lt(a, b)** :- This function is used to **check if a is less than b or
not**. Returns true if a is less than b, else returns false.  
Operation – **a < b**.

 **9\. le(a, b)** :- This function is used to **check if a is less than or
equal to b or not**. Returns true if a is less than or equal to b, else
returns false.  
Operation – **a <= b**.

 **10\. eq(a, b)** :- This function is used to **check if a is equal to b or
not**. Returns true if a is equal to b, else returns false.  
Operation – **a == b**.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# lt(), le() and eq()

 

# importing operator module 

import operator

 

# Initializing variables

a = 3

 

b = 3

 

# using lt() to check if a is less than b

if(operator.lt(a,b)):

 print ("3 is less than 3")

else : print ("3 is not less than 3")

 

# using le() to check if a is less than or equal to b

if(operator.le(a,b)):

 print ("3 is less than or equal to 3")

else : print ("3 is not less than or equal to 3")

 

# using eq() to check if a is equal to b

if (operator.eq(a,b)):

 print ("3 is equal to 3")

else : print ("3 is not equal to 3")  
  
---  
  
 __

 __

Output:

    
    
    3 is not less than 3
    3 is less than or equal to 3
    3 is equal to 3
    

**11\. gt(a,b)** :- This function is used to **check if a is greater than b or
not**. Returns true if a is greater than b, else returns false.  
Operation – **a > b**.

 **12\. ge(a,b)** :- This function is used to **check if a is greater than or
equal to b or not**. Returns true if a is greater than or equal to b, else
returns false.  
Operation – **a >= b**.

 **13\. ne(a,b)** :- This function is used to **check if a is not equal to b
or is equal**. Returns true if a is not equal to b, else returns false.  
Operation – **a != b**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# gt(), ge() and ne()

 

# importing operator module 

import operator

 

# Initializing variables

a = 4

 

b = 3

 

# using gt() to check if a is greater than b

if (operator.gt(a,b)):

 print ("4 is greater than 3")

else : print ("4 is not greater than 3")

 

# using ge() to check if a is greater than or equal to b

if (operator.ge(a,b)):

 print ("4 is greater than or equal to 3")

else : print ("4 is not greater than or equal to 3")

 

# using ne() to check if a is not equal to b

if (operator.ne(a,b)):

 print ("4 is not equal to 3")

else : print ("4 is equal to 3")  
  
---  
  
 __

 __

Output:

    
    
    4 is greater than 3
    4 is greater than or equal to 3
    4 is not equal to 3
    

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

