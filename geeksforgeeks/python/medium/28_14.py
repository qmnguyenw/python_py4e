OOP in Python | Set 3 (Inheritance, examples of object, issubclass and super)



We have discussed following topics on Object Oriented Programming in Python

  * Object Oriented Programming in Python | set-1
  * Object Oriented Programming in Python | Set 2 (Data Hiding and Object Printing)

In this article, Inheritance is introduced.

One of the major advantages of Object Oriented Programming is re-use.
Inheritance is one of the mechanisms to achieve the same. In inheritance, a
class (usually called superclass) is inherited by another class (usually
called subclass). The subclass adds some attributes to superclass.

Below is a sample Python program to show how inheritance is implemented in
Python.

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

 

 # To check if this person is employee

 def isEmployee(self):

 return False

 

 

# Inherited or Sub class (Note Person in bracket)

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

  

  

    
    
    ('Geek1', False)
    ('Geek2', True)
    

