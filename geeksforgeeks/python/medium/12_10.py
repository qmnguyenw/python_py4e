Inheritance in Python Inner Class



A class is a user-defined blueprint or prototype from which objects are
created. Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of
that type to be made. Each class instance can have attributes attached to it
for maintaining its state. Class instances can also have methods (defined by
its class) for modifying its state.

An inner class or nested class is defined inside the body of another class. If
an object is created using a class, the object inside the root class can be
used. A class can have one or more than one inner class. Inner class or nested
class helps the user in many ways such as the logical grouping of classes,
more readable and easily maintainable, etc.

For example, consider a situation where a class DOB is inside another class
Person and see the below code snippet.

    
    
    class person:
        def __init__(self):
            self.name = 'AKASH'
            self.db = self.Dob()   #this is Dob object
    

In the preceding code, ’db.’ represent the inner class object. When the outer
class object is created, it contains a subobject that is an inner class
object. Hence, we can refer outer class and inner class members as:

    
    
    p = person()  #create outer class object
    p.display()   #call outer class method
    
    
    x = p.db     #create inner class object
    x.display()    #call inner class method
    

**Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# inner class

 

 

class person:

 def __init__(self):

 self.name = 'AKASH'

 self.db = self.Dob()

 

 def display(self):

 print('NAME = ', self.name)

 

 # this is inner class

 class Dob:

 def __init__(self):

 self.dd = 10

 self.mm = 3

 self.yy = 2000

 def display(self):

 print('DOB = {}/{}/{}'.format(self.dd, self.mm,
self.yy))

 

# creating person class object

p = person()

p.display()

 

# create inner class object

x = p.db

x.display()  
  
---  
  
 __

 __

 **Output:**

    
    
    NAME =  AKASH
    DOB = 10/3/2000
    

#### Inheritance in Inner Class

Inheritance is the capability of one class to derive or inherit the properties
from some another class. The benefits of inheritance are:

  * It represents real-world relationships well.
  * It provides reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
  * It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

To use inheritance in the inner class, consider the below code snippet.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# inheritance in inner class

 

 

class A:

 def __init__(self):

 self.db = self.Inner()

 

 def display(self):

 print('In Parent Class')

 

 # this is inner class

 class Inner:

 

 def display1(self):

 print('Inner Of Parent Class')

 

 

class B(A):

 def __init__(self):

 print('In Child Class')

 super().__init__()

 

 class Inner(A.Inner):

 

 def display2(self):

 print('Inner Of Child Class')

 

# creating child class object

p = B()

p.display()

 

# create inner class object

x = p.db

x.display1()

x.display2()  
  
---  
  
 __

 __

 **Output:**

    
    
    In Child Class
    In Parent Class
    Inner Of Parent Class
    Inner Of Child Class
    

In the above example, Class B inherits from A and the inner class of B
inherits from the inner class of A. Then the class methods of Parent’ Inner
class are called from the child’s inner class object.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

