Create Classes Dynamically in Python



A class defines a collection of instance variables and methods to specify an
object type. A class can be used to make as many object instances of the type
of object as needed. An object is an identified entity with certain attributes
(data members) and behaviours (member functions). Group of objects having
similar characteristics and behaviour are the instance of the same class.

Python is a dynamic programming language and due to its flexibility Python has
a significant advantage over statically typed languages. Python Code can be
dynamically imported and classes can be dynamically created at run-time.

Classes can be dynamically created using the type() function in Python. The
type() function is used to return the type of the object.

 **Syntax:**

    
    
    type(object)
    

The above syntax returns the type of object.

  

  

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# program to illustrate the use of type()

 

print(type("Geeks4Geeks !")) 

print(type(1706256))  
  
---  
  
 __

 __

 **Output:**

    
    
    class 'str'
    class 'int'
    

## Creating Dynamic Classes in Python

Classes can be created dynamically using the below syntax:  
 **Syntax:**

    
    
    type(name, bases, attributes) 
    
    **Parameters:**
    **name:** The user defined name of the class
    **bases:** A list of base classes, and its type is tuple
    **attributes:** the data members and methods contained in the class
    

The above Syntax returns a new type of object.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# program to create class dynamically

 

# constructor

def constructor(self, arg):

 self.constructor_arg = arg

 

# method

def displayMethod(self, arg):

 print(arg)

 

# class method

@classmethod

def classMethod(cls, arg):

 print(arg)

 

# creating class dynamically

Geeks = type("Geeks", (object, ), {

 # constructor

 "__init__": constructor,

 

 # data members

 "string_attribute": "Geeks 4 geeks !",

 "int_attribute": 1706256,

 

 # member functions

 "func_arg": displayMethod,

 "class_func": classMethod

})

 

# creating objects

obj = Geeks("constructor argument")

print(obj.constructor_arg)

print(obj.string_attribute)

print(obj.int_attribute)

obj.func_arg("Geeks for Geeks")

Geeks.class_func("Class Dynamically Created !")  
  
---  
  
 __

 __

 **Output:**

    
    
    constructor argument
    Geeks 4 geeks!
    1706256
    Geeks for GeeksClass Dynamically Created!
    

In the above program, class Geeks is dynamically created which has a
constructor. The data members of Geeks are string_attribute and
int_attribute and member functions of Geeks are displayMethod() and
classMethod(). An object obj of class Geeks is created and all the data
members are assigned and displayed, all the member functions of Geeks are
also called.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

