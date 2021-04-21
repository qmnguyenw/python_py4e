Inheritance in Python



Inheritance is the capability of one class to derive or inherit the properties
from another class. The benefits of inheritance are:  

  1. It represents real-world relationships well.
  2. It provides **reusability** of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
  3. It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

Below is a simple example of inheritance in Python  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate inheritance

 

# Base or Super class. Note object in bracket.

# (Generally, object is made ancestor of all classes)

# In Python 3.x "class Person" is 

# equivalent to "class Person(object)"

class Person(object):

 

 # Constructor

 def __init__(self, name):

 self.name = name

 

 # To get name

 def getName(self):

 return self.name

 

 # To check if this person is an employee

 def isEmployee(self):

 return False

 

 

# Inherited or Subclass (Note Person in bracket)

class Employee(Person):

 

 # Here we return true

 def isEmployee(self):

 return True

 

# Driver code

emp = Person("Geek1") # An Object of Person

print(emp.getName(), emp.isEmployee())

 

emp = Employee("Geek2") # An Object of Employee

print(emp.getName(), emp.isEmployee())  
  
---  
  
 __

 __

 **Output:**

    
    
    Geek1 False
    Geek2 True
    
    

**What is object class?**  
Like Java Object class, in Python (from version 3.x), object is root of all
classes.  
In Python 3.x, “class Test(object)” and “class Test” are same.  
In Python 2.x, “class Test(object)” creates a class with object as parent
(called new style class) and “class Test” creates old style class (without
object parent). Refer this for more details.

 **Subclassing (Calling constructor of parent class)**  
A child class needs to identify which class is its parent class. This can be
done by mentioning the parent class name in the definition of the child class.  
Eg: class **subclass_name (superclass_name)** :  
_ _ _  
_ _ _  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate how parent constructors

# are called.

 

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

 def __init__(self, name, idnumber, salary, post):

 self.salary = salary

 self.post = post

 

 # invoking the __init__ of the parent class 

 Person.__init__(self, name, idnumber) 

 

 

# creation of an object variable or an instance

a = Employee('Rahul', 886012, 200000, "Intern") 

 

# calling a function of the class Person using its instance

a.display()   
  
---  
  
__

__

**Output:**

    
    
    Rahul
    886012
    
    

‘a’ is the instance created for the class Person. It invokes the __init__() of
the referred class. You can see ‘object’ written in the declaration of the
class Person. In Python, every class inherits from a built-in basic class
called ‘object’. The constructor i.e. the ‘__init__’ function of a class is
invoked when we create an object variable or an instance of the class.

The variables defined within __init__() are called as the instance variables
or objects. Hence, ‘name’ and ‘idnumber’ are the objects of the class Person.
Similarly, ‘salary’ and ‘post’ are the objects of the class Employee. Since
the class Employee inherits from class Person, ‘name’ and ‘idnumber’ are also
the objects of class Employee.  
If you forget to invoke the __init__() of the parent class then its instance
variables would not be available to the child class.

The following code produces an error for the same reason.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate error if we

# forget to invoke __init__() of the parent.

 

class A:

 def __init__(self, n = 'Rahul'):

 self.name = n

class B(A):

 def __init__(self, roll):

 self.roll = roll

 

object = B(23)

print (object.name)  
  
---  
  
 __

 __

Output :

    
    
    Traceback (most recent call last):
      File "/home/de4570cca20263ac2c4149f435dba22c.py", line 12, in 
        print (object.name)
    AttributeError: 'B' object has no attribute 'name'
    

**Different forms of Inheritance:**  
**1\. Single inheritance** : When a child class inherits from only one parent
class, it is called single inheritance. We saw an example above.  
 **2\. Multiple inheritance** : When a child class inherits from multiple
parent classes, it is called multiple inheritance.  
Unlike Java and like C++, Python supports multiple inheritance. We specify all
parent classes as a comma-separated list in the bracket.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python example to show the working of multiple

# inheritance

class Base1(object):

 def __init__(self):

 self.str1 = "Geek1"

 print("Base1")

 

class Base2(object):

 def __init__(self):

 self.str2 = "Geek2"

 print("Base2")

 

class Derived(Base1, Base2):

 def __init__(self):

 

 # Calling constructors of Base1

 # and Base2 classes

 Base1.__init__(self)

 Base2.__init__(self)

 print("Derived")

 

 def printStrs(self):

 print(self.str1, self.str2)

 

 

ob = Derived()

ob.printStrs()  
  
---  
  
 __

 __

 **Output:**

    
    
    Base1
    Base2
    Derived
    Geek1 Geek2
    

**3\. Multilevel inheritance** : When we have a child and grandchild
relationship.  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate inheritance

 

# Base or Super class. Note object in bracket.

# (Generally, object is made ancestor of all classes)

# In Python 3.x "class Person" is 

# equivalent to "class Person(object)"

class Base(object):

 

 # Constructor

 def __init__(self, name):

 self.name = name

 

 # To get name

 def getName(self):

 return self.name

 

 

# Inherited or Sub class (Note Person in bracket)

class Child(Base):

 

 # Constructor

 def __init__(self, name, age):

 Base.__init__(self, name)

 self.age = age

 

 # To get name

 def getAge(self):

 return self.age

 

# Inherited or Sub class (Note Person in bracket)

class GrandChild(Child):

 

 # Constructor

 def __init__(self, name, age, address):

 Child.__init__(self, name, age)

 self.address = address

 

 # To get address

 def getAddress(self):

 return self.address 

 

# Driver code

g = GrandChild("Geek1", 23, "Noida") 

print(g.getName(), g.getAge(), g.getAddress())  
  
---  
  
 __

 __

 **Output:**

    
    
    Geek1 23 Noida
    
    

**4\. Hierarchical inheritance** More than one derived classes are created
from a single base.  
  
 **5\. Hybrid inheritance** : This form combines more than one form of
inheritance. Basically, it is a blend of more than one type of inheritance.

 **Private members of parent class**  
We don’t always want the instance variables of the parent class to be
inherited by the child class i.e. we can make some of the instance variables
of the parent class private, which won’t be available to the child class.  
We can make an instance variable by adding double underscores before its name.
For example,  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate private members

# of the parent class

class C(object):

 def __init__(self):

 self.c = 21

 

 # d is private instance variable 

 self.__d = 42

class D(C):

 def __init__(self):

 self.e = 84

 C.__init__(self)

object1 = D()

 

# produces an error as d is private instance variable

print(object1.d)   
  
---  
  
__

__

Output :

    
    
      File "/home/993bb61c3e76cda5bb67bd9ea05956a1.py", line 16, in 
        print (object1.d)                     
    AttributeError: type object 'D' has no attribute 'd'
    
    

Since ‘d’ is made private by those underscores, it is not available to the
child class ‘D’ and hence the error.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

