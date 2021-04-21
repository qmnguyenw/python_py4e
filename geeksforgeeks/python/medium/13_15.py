__new__ in Python



Python is an Object oriented programming language i.e everything in Python is
an object. There are special kind of methods in Python known as magic methods
or dunder methods (dunder here means “ _Double Underscores_ ”). Dunder or
magic methods in Python are the methods having two prefix and suffix
underscores in the method name. These are commonly used for operator
overloading.  
Few examples for magic methods are: __init__, __add__, __len__,
__repr__ etc.

 **Note:** To know more about Magic methods click here.

#### __new__ method

  
Whenever a class is instantiated __new__ and __init__ methods are called.
__new__ method will be called when an object is created and __init__
method will be called to initialize the object. In the base class object,
the __new__ method is defined as a static method which requires to pass a
parameter cls. cls represents the class that is needed to be instantiated,
and the compiler automatically provides this parameter at the time of
instantiation.

 **Syntax:**

  

  

    
    
    class class_name:
        def __new__(cls, *args, **kwargs):
            statements
            .
            .
            return super(class_name, cls).__new__(cls, *args, **kwargs)
    

**Note:** Instance can be created inside __new__ method either by using
super function or by directly calling __new__ method over object, where if
parent class is object. That is instance = super(MyClass, cls).__new__(cls,
*args, **kwargs) or instance = object.__new__(cls, *args, **kwargs)

If both __init__ method and __new__ method exists in the class, then the
__new__ method is executed first and decides whether to use __init__ method or
not, because other class constructors can be called by __new__ method or it
can simply return other objects as an instance of this class.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate __new__

 

# don't forget the object specified as base

class A(object):

 def __new__(cls):

 print("Creating instance")

 return super(A, cls).__new__(cls)

 

 def __init__(self):

 print("Init is called")

 

A()  
  
---  
  
 __

 __

 **Output:**

    
    
    Creating instance
    Init is called
    

The above example shows that __new__ method is called automatically when
calling the class name, whereas __init__ method is called every time an
instance of the class is returned by __new__ method, passing the returned
instance to __init__ as the self parameter, therefore even if you were to
save the instance somewhere globally/statically and return it every time from
__new__, then __init__ will be called every time you do just that.

This means that if the super is omitted for __new__ method the __init__ method
will not be executed. Let’s see if that is the case.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate __new__

 

class A(object):

 def __new__(cls):

 print("Creating instance")

 

 # It is not called

 def __init__(self):

 print("Init is called")

 

print(A())  
  
---  
  
 __

 __

 **Output:**

    
    
    Creating instance
    None
    

In the above example, it can be seen that **__init__** method is not called
and the instantiation is evaluated to be None because the constructor is not
returning anything. Let’s see what happens if both the __new__ and __init__
methods are returning something.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate __new__

 

class A(object):

 # new method returning a string

 def __new__(cls):

 print("Creating instance")

 return "GeeksforGeeks"

 

class B(object):

 # init method returning a string

 def __init__(self):

 print("Initializing instance")

 return "GeeksforGeeks"

 

print(A())

print(B())  
  
---  
  
 __

 __

 **Output:**

    
    
    Creating instance
    GeeksforGeeks
    Initializing instance
    
    
    
    Traceback (most recent call last):
      File "/home/62216eb30d3856048eff916fb8d4c32d.py", line 17, in 
        print(B())
    TypeError: __init__() should return None, not 'str'
    

This TypeError is raised by the handler that calls __init__ method and it
wouldn’t even make sense to return anything from __init__ method since it’s
purpose is just to alter the fresh state of the newly created instance.

Let’s try an example in which __new__ method returns an instance of a
different class.  
 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate __new__ method

 

# class whose object

# is returned

class GeeksforGeeks(object):

 def __str__(self):

 return "GeeksforGeeks"

 

# class returning object

# of different class

class Geek(object):

 def __new__(cls):

 return GeeksforGeeks()

 

 def __init__(self):

 print("Inside init")

 

print(Geek())  
  
---  
  
 __

 __

 **Output:**

    
    
    GeeksforGeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

