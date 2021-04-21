Python – Access Parent Class Attribute



A class is a user-defined blueprint or prototype from which objects are
created. Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of
that type to be made. Each class instance can have attributes attached to it
for maintaining its state. Class instances can also have methods (defined by
its class) for modifying its state.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# classes and objects

 

 

# Creating a class 

class Student:

 

 # Class Variable

 stream = 'COE'

 

 def __init__(self, name, roll_no):

 

 # Instance Variable

 self.name = name 

 self.roll_no = roll_no 

 

# Objects of Student class 

a = Student('SHIVAM', 3425) 

b = Student('SACHIN', 3624)

 

print(a.stream)

print(b.stream)

print(a.name)

print(b.name)

print(a.roll_no) 

print(b.roll_no)

 

# Class variables can be 

# accessed using class 

# name also 

print(Student.stream)  
  
---  
  
 __

 __

 **Output:**

    
    
    COE
    COE
    SHIVAM
    SACHIN
    3425
    3624
    COE
    

**Note:** For more information, refer to Python Classes and Objects.

#### Accessing Parent Class Functions

When a class inherits from another class it inherits the attributes and
methods of another class. A class that inherits from another class is known as
child class and the class from which the child class inherits is known as
Parent class. But have you ever wondered how to access the parent’s class
methods? This is really simple, you just have to call the constructor of
parent class inside the constructor of child class and then the object of a
child class can access the methods and attributes of the parent class.

  

  

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how parent constructors are called. 

 

# parent class 

class Person( object ): 

 

 # __init__ is known as the constructor 

 def __init__(self, name, idnumber): 

 self.name = name 

 self.idnumber = idnumber 

 

 def display(self): 

 print(self.name) 

 print(self.idnumber) 

 

# child class 

class Employee( Person ): 

 def __init__(self, name, idnumber, salary): 

 self.salary = salary 

 

 # invoking the constructor of 

 # the parent class 

 Person.__init__(self, name, idnumber) 

 

 def show(self):

 print(self.salary)

 

 

# creation of an object

# variable or an instance 

a = Employee('Rahul', 886012, 30000000) 

 

# calling a function of the

# class Person using Employee's

# class instance 

a.display()

a.show()   
  
---  
  
__

__

**Output:**

    
    
    Rahul
    886012
    30000000
    

**Note:** For more information, refer to Inheritance in Python.

#### Accessing Parent class method from inner class

An inner class or nested class is a defined inside the body of another class.
If an object is created using a class, the object inside the root class can be
used. A class can have one or more than one inner classes.

 **Types of Inner Classes:**

  * Multiple Inner Class
  * Multilevel Inner Class

 **Multiple Inner Class:** A class containing more than one inner class.

![MULTIPLE INNER CLASS](https://media.geeksforgeeks.org/wp-
content/uploads/20200125195959/Multilevel1.jpg)

 **Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

class Electronics:

 def __init__(self):

 print('SINGLA ELECTRONICS')

 self.laptop=self.Laptop()

 self.mobile=self.Mobile()

 

 # Inner Class 1

 class Laptop:

 def operation(self):

 print('DELL Inspiron 15')

 

 # Inner Class 2

 class Mobile:

 def operation(self):

 print('Redmi Note 5')

 

# Driver Code

ele = Electronics()

ele.laptop.operation()

ele.mobile.operation()  
  
---  
  
 __

 __

 **Output:**

    
    
    SINGLA ELECTRONICS
    DELL Inspiron 15
    Redmi Note 5
    

**Multilevel Inner Class:** In multilevel inner classes, the inner class
contains another class which is inner classes to the previous one.

![MULTILEVEL INNER CLASS](https://media.geeksforgeeks.org/wp-
content/uploads/20200125214822/MULTILEVEL11.jpg)

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

class Vehicle:

 

 def __init__(self):

 

 # instantiating the 'Inner' class

 self.inner = self.Car()

 

 # instantiating the multilevel

 # 'InnerInner' class

 self.innerinner = self.inner.Maruti()

 

 def show_classes(self):

 print("This is in Outer class that is Vehicle")

 

 

 # inner class

 class Car:

 # First Inner Class

 

 def __init__(self):

 

 # instantiating the 

 # 'InnerInner' class

 self.innerinner = self.Maruti()

 

 def show_classes(self):

 print("This is in Inner class that is Car")

 

 # multilevel inner class

 class Maruti:

 

 def inner_display(self, msg):

 print("This is in multilevel InnerInner\

 class that is Maruti")

 print(msg)

 

 

# Driver Code

outer = Vehicle()

outer.show_classes()

inner = outer.Car()

inner.show_classes()

innerinner = inner.Maruti()

 

# Calling the method inner_display

innerinner.inner_display("Just Print It!")  
  
---  
  
 __

 __

 **Output:**

    
    
    This is in Outer class that is Vehicle
    This is in Inner class that is Car
    This is in multilevel InnerInner class that is Maruti
    Just Print It!
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

