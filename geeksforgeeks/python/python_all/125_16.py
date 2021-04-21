Python | Use of __slots__



When we create objects for classes, it requires memory and the attribute are
stored in the form of a dictionary. In case if we need to allocate thousands
of objects, it will take a lot of memory space.  
 **slots** provide a special mechanism to reduce the size of objects.It is a
concept of memory optimisation on objects.

 **Example of python object without slots :**

 __

 __  
 __

 __

 __  
 __  
 __

class GFG(object):

 def __init__(self, *args, **kwargs):

 self.a = 1

 self.b = 2

 

if __name__ == "__main__":

 instance = GFG()

 print(instance.__dict__)  
  
---  
  
 __

 __

 **Output :**

    
    
    {'a': 1, 'b': 2}

As every object in Python contains a dynamic dictionary that allows adding
attributes. For every instance object, we will have an instance of a
dictionary that consumes more space and wastes a lot of RAM. In Python, there
is no default functionality to allocate a static amount of memory while
creating the object to store all its attributes.  
Usage of __slots__ reduce the wastage of space and speed up the program by
allocating space for a fixed amount of attributes.

 **Example of python object with slots :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

class GFG(object):

 __slots__=['a', 'b']

 def __init__(self, *args, **kwargs):

 self.a = 1

 self.b = 2

 

if __name__ == "__main__":

 instance = GFG()

 print(instance.__slots__)  
  
---  
  
 __

 __

 **Output :**

    
    
    ['a', 'b']

 **Example of python if we use dict :**

 __

 __  
 __

 __

 __  
 __  
 __

class GFG(object):

 __slots__=['a', 'b']

 def __init__(self, *args, **kwargs):

 self.a = 1

 self.b = 2

 

if __name__ == "__main__":

 instance = GFG()

 print(instance.__dict__)  
  
---  
  
 __

 __

 **Output :**

    
    
    AttributeError: 'GFG' object has no attribute '__dict__'

This error will be caused.

 **Result of using __slots__:**

  1. Fast access to attributes
  2. Saves memory space

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

