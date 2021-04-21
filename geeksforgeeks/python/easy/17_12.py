Operator Overloading in Python



Operator Overloading means giving extended meaning beyond their predefined
operational meaning. For example operator + is used to add two integers as
well as join two strings and merge two lists. It is achievable because ‘+’
operator is overloaded by int class and str class. You might have noticed that
the same built-in operator or function shows different behavior for objects of
different classes, this is called _Operator Overloading_.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show use of

# + operator for different purposes.

 

print(1 + 2)

 

# concatenate two strings

print("Geeks"+"For") 

 

# Product two numbers

print(3 * 4)

 

# Repeat the String

print("Geeks"*4)  
  
---  
  
 __

 __

 **Output:**  

    
    
    3
    GeeksFor
    12
    GeeksGeeksGeeksGeeks
    
    
    

**How to overload the operators in Python?**  
Consider that we have two objects which are a physical representation of a
class (user-defined data type) and we have to add two objects with binary ‘+’
operator it throws an error, because compiler don’t know how to add two
objects. So we define a method for an operator and that process is called
operator overloading. We can overload all existing operators but we can’t
create a new operator. To perform operator overloading, Python provides some
special function or magic function that is automatically invoked when it is
associated with that particular operator. For example, when we use + operator,
the magic method __add__ is automatically invoked in which the operation for +
operator is defined.  
 **Overloading binary + operator in Python :**  
When we use an operator on user defined data types then automatically a
special function or magic function associated with that operator is invoked.
Changing the behavior of operator is as simple as changing the behavior of
method or function. You define methods in your class and operators work
according to that behavior defined in methods. When we use + operator, the
magic method __add__ is automatically invoked in which the operation for +
operator is defined. There by changing this magic method’s code, we can give
extra meaning to the + operator.  
**Code 1:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrate how

# to overload an binary + operator

 

class A:

 def __init__(self, a):

 self.a = a

 

 # adding two objects 

 def __add__(self, o):

 return self.a + o.a 

ob1 = A(1)

ob2 = A(2)

ob3 = A("Geeks")

ob4 = A("For")

 

print(ob1 + ob2)

print(ob3 + ob4)  
  
---  
  
 __

 __

 **Output :**  

    
    
    3
    GeeksFor
    
    
    

**Code 2:**  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to perform addition

# of two complex numbers using binary 

# + operator overloading.

 

class complex:

 def __init__(self, a, b):

 self.a = a

 self.b = b

 

 # adding two objects 

 def __add__(self, other):

 return self.a + other.a, self.b + other.b

 

 def __str__(self):

 return self.a, self.b

 

Ob1 = complex(1, 2)

Ob2 = complex(2, 3)

Ob3 = Ob1 + Ob2

print(Ob3)  
  
---  
  
 __

 __

 **Output :**  

    
    
    (3, 5)
    

**Overloading comparison operators in Python :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to overload

# a comparison operators 

 

class A:

 def __init__(self, a):

 self.a = a

 def __gt__(self, other):

 if(self.a>other.a):

 return True

 else:

 return False

ob1 = A(2)

ob2 = A(3)

if(ob1>ob2):

 print("ob1 is greater than ob2")

else:

 print("ob2 is greater than ob1")  
  
---  
  
 __

 __

 **Output :**  

    
    
    ob2 is greater than ob1
    

**Overloading equality and less than operators :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to overload equality

# and less than operators

 

class A:

 def __init__(self, a):

 self.a = a

 def __lt__(self, other):

 if(self.a<other.a):

 return "ob1 is lessthan ob2"

 else:

 return "ob2 is less than ob1"

 def __eq__(self, other):

 if(self.a == other.a):

 return "Both are equal"

 else:

 return "Not equal"

 

ob1 = A(2)

ob2 = A(3)

print(ob1 < ob2)

 

ob3 = A(4)

ob4 = A(4)

print(ob1 == ob2)  
  
---  
  
 __

 __

 **Output :**  

    
    
    ob1 is lessthan ob2
    Not equal
    

#### Python magic methods or special functions for operator overloading

#### Binary Operators:

Operator| Magic Method|  **+**|  __add__(self, other)|  **–**|  __sub__(self,
other)|  *****|  __mul__(self, other)|  **/**|  __truediv__(self, other)|
**//**|  __floordiv__(self, other)|  **%**|  __mod__(self, other)|  ******|
__pow__(self, other)| >>| __rshift__(self, other)| <<| __lshift__(self,
other)| &| __and__(self, other)| || __or__(self, other)| ^| __xor__(self,
other)  
---|---  
  
#### Comparison Operators :

Operator| Magic Method|  **<**|  __LT__(SELF, OTHER)|  **>**|  __GT__(SELF,
OTHER)|  **< =**| __LE__(SELF, OTHER)|  **> =**| __GE__(SELF, OTHER)|  **==**|
__EQ__(SELF, OTHER)|  **!=**|  __NE__(SELF, OTHER)  
---|---  
  
#### Assignment Operators :

Operator| Magic Method|  **-=**|  __ISUB__(SELF, OTHER)|  **+=**|
__IADD__(SELF, OTHER)|  ***=**|  __IMUL__(SELF, OTHER)|  **/=**|
__IDIV__(SELF, OTHER)|  **//=**|  __IFLOORDIV__(SELF, OTHER)|  **%=**|
__IMOD__(SELF, OTHER)|  ****=**|  __IPOW__(SELF, OTHER)|  **> >=**|
__IRSHIFT__(SELF, OTHER)|  **< <=**| __ILSHIFT__(SELF, OTHER)|  **& =**|
__IAND__(SELF, OTHER)|  **|=**|  __IOR__(SELF, OTHER)|  **^=**|
__IXOR__(SELF, OTHER)  
---|---  
  
#### Unary Operators :

Operator| Magic Method|  **–**|  __NEG__(SELF, OTHER)|  **+**|  __POS__(SELF,
OTHER)|  **~**|  __INVERT__(SELF, OTHER)  
---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

