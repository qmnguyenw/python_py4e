Difference between Method and Function in Python



Here, **key differences between Method and Function in Python** are explained.
Java is also an OOP language, but their is no concept of Function in it. But
Python has both concept of Method and Function.

 **Python Method**

  1. Method is called by its name, but it is **associated to an object** (dependent).
  2. A method is **implicitly passed the object** on which it is invoked.
  3. It **may or may not return any data.**
  4. A method **can operate on the data (instance variables) that is contained by the corresponding class**

 **Basic Method Structure in Python :**

 __

 __  
 __

 __

 __  
 __  
 __

# Basic Python method

class class_name

 def method_name () :

 ......

 # method body

 ......   
  
---  
  
__

__

**Python 3 User-Defined Method :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 User-Defined Method

class ABC :

 def method_abc (self):

 print("I am in method_abc of ABC class. ")

 

class_ref = ABC() # object of ABC class

class_ref.method_abc()  
  
---  
  
 __

 __

Output:

  

  

    
    
     I am in method_abc of ABC class

 **Python 3 Inbuilt method :**

 __

 __  
 __

 __

 __  
 __  
 __

import math

 

ceil_val = math.ceil(15.25)

print( "Ceiling value of 15.25 is : ", ceil_val)   
  
---  
  
__

__

Output:

    
    
    Ceiling value of 15.25 is :  16

Know more about Python ceil() and floor() method.

 **Functions**

  1. Function is block of code that is also **called by its name**. (independent)
  2. The function can have different parameters or may not have any at all. If **any data (parameters)** are passed, they are **passed explicitly**.
  3. It **may or may not return any data.**
  4. Function does not deal with Class and its instance concept.

 **Basic Function Structure in Python :**

 __

 __  
 __

 __

 __  
 __  
 __

def function_name ( arg1, arg2, ...) :

 ......

 # function body

 ......   
  
---  
  
__

__

**  
Python 3 User-Defined Function :**

 __

 __  
 __

 __

 __  
 __  
 __

def Subtract (a, b):

 return (a-b)

 

print( Subtract(10, 12) ) # prints -2

 

print( Subtract(15, 6) ) # prints 9  
  
---  
  
 __

 __

Output:

    
    
    -2
    9
    

**Python 3 Inbuilt Function :**

 __

 __  
 __

 __

 __  
 __  
 __

s= sum([5, 15, 2])

print( s ) # prints 22

 

mx = max(15, 6)

print( mx ) # prints 15  
  
---  
  
 __

 __

Output:

    
    
    22
    15
    

Know more about Python sum() function. Know more about Python min() or max()
function.

 **Difference between method and function**

  1. Simply, function and method both look similar as they perform in almost similar way, but the key difference is the concept of ‘ **Class and its Object** ‘.
  2. Functions can be called **only by its name** , as it is defined independently. But methods c **an’t be called by its name** only, we need to invoke the class by a reference of that class in which it is defined, i.e. method is defined within a class and hence they are dependent on that class.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

