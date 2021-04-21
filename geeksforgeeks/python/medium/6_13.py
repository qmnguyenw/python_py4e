Difference between attributes and properties in Python



 **Class Attribute:** Class Attributes are unique to each class. Each instance
of the class will have this attribute.

**Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# declare a class

class Employee: 

 

 # class attribute

 count = 0

 

 # define a method

 def increase(self): 

 Employee.count += 1

 

# create an Employee 

# class object

a1 = Employee() 

 

# calling object's method

a1.increase() 

 

# print value of class attribute

print(a1.count) 

 

a2 = Employee() 

 

a2.increase() 

 

print(a2.count) 

 

print(Employee.count)  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    2
    2
    

In the above example, count variable is a class attribute.

 **Instance Attribute:** Instance Attributes are unique to each instance, (an
instance is another name for an object). Every object/instance has its own
attribute and can be changed without affecting other instances.

  

  

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# create a class

class Employee: 

 

 # constructor

 def __init__(self): 

 

 # instance attribute

 self.name = 'Gfg'

 self.salary = 4000

 

 # define a method

 def show(self): 

 print(self.name) 

 print(self.salary) 

 

# create an object of 

# Employee class

x = Employee()

 

# method calling

x.show()  
  
---  
  
 __

 __

 **Output:**

    
    
    Gfg
    4000
    

Now, Let’s see an example on properties:

1) Create Properties of a class using **property()** function:

> **Syntax:** property(fget, fset, fdel, doc)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# create a class

class gfg: 

 

 # constructor

 def __init__(self, value): 

 self._value = value 

 

 # getting the values 

 def getter(self): 

 print('Getting value') 

 return self._value 

 

 # setting the values 

 def setter(self, value): 

 print('Setting value to ' + value) 

 self._value = value 

 

 # deleting the values 

 def deleter(self): 

 print('Deleting value') 

 del self._value 

 

 # create a properties

 value = property(getter, setter, deleter, ) 

 

# create a gfg class object

x = gfg('Happy Coding!') 

print(x.value) 

 

x.value = 'Hey Coder!'

 

# deleting the value

del x.value  
  
---  
  
 __

 __

 **Output:**

    
    
    Getting value
    Happy Coding!
    Setting value to Hey Coder!
    Deleting value
    

2) **** Create Properties of a class Using **@property** decorator:

  

  

We can apply the property function by using @property decorator. This is one
of the built-in decorators. A decorator is simply a function that takes
another function as an argument and adding to its behavior by wrapping it.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# create a class

class byDeco: 

 

 # constructor

 def __init__(self, value): 

 self._value = value 

 

 # getting the values

 @property

 def value(self): 

 print('Getting value') 

 return self._value 

 

 # setting the values 

 @value.setter 

 def value(self, value): 

 print('Setting value to ' + value) 

 self._value = value 

 

 # deleting the values 

 @value.deleter 

 def value(self): 

 print('Deleting value') 

 del self._value 

 

 

# create an object of class

x = byDeco('happy Coding') 

print(x.value) 

 

x.value = 'Hey Coder!'

 

# deleting the value

del x.value  
  
---  
  
 __

 __

 **Output:**

    
    
    Getting value
    happy Coding
    Setting value to Hey Coder!
    Deleting value

## Table of difference between Attribute V/s Property

 **Attribute**|

 **Property**|  Attributes are described by data variables for example like
name, age, height etc.| Properties are special kind of attributes.|

Two types of attributes:

  * Class attribute
  * Instance attribute

| It has getter, setter and delete methods like __get__, __set__ and
__delete__ methods.|  **Class attributes**are defined in the class body parts
usually at the top.|  We can define getters, setters, and delete methods with
the **property()** **** function.|  **I** **nstance attribute** are defined in
the class body using **self** keyword usually it the **__init__()** method.|
If we just want to the read property, there is also a **@property**decorator
which you can add above your method.  
---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

