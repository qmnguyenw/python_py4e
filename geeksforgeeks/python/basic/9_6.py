Types of inheritance Python



Inheritance is defined as the capability of one class to derive or inherit the
properties from some other class and use it whenever needed. Inheritance
provides the following properties:  

  * It represents real-world relationships well. 
  * It provides reusability of code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it. 
  * It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.   

**Example:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate

# inheritance 

# Base class or Parent class

class Child:

 # Constructor

 def __init__(self, name):

 self.name = name

 # To get name

 def getName(self):

 return self.name

 # To check if this person is student

 def isStudent(self):

 return False

# Derived class or Child class

class Student(Child):

 # True is returned

 def isStudent(self):

 return True

 

# Driver code

# An Object of Child

std = Child("Ram")

print(std.getName(), std.isStudent())

# An Object of Student

std = Student("Shivam")

print(std.getName(), std.isStudent())  
  
---  
  
 __

 __

 **Output:**  

    
    
    Ram False
    Shivam True
    
    
    

## Types of Inheritance in Python

Types of Inheritance depends upon the number of child and parent classes
involved. There are four types of inheritance in Python:  

  

  

**Single Inheritance:** Single inheritance enables a derived class to inherit
properties from a single parent class, thus enabling code reusability and the
addition of new features to existing code.  

![single-inheritance](https://media.geeksforgeeks.org/wp-
content/uploads/20200108135809/inheritance11.png)

**Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# single inheritance

# Base class

class Parent:

 def func1(self):

 print("This function is in parent class.")

# Derived class

class Child(Parent):

 def func2(self):

 print("This function is in child class.")

# Driver's code

object = Child()

object.func1()

object.func2()  
  
---  
  
 __

 __

 **Output:**

    
    
    
    This function is in parent class.
    This function is in child class.
    

**Multiple Inheritance:** When a class can be derived from more than one base
class this type of inheritance is called multiple inheritance. In multiple
inheritance, all the features of the base classes are inherited into the
derived class.  

![multiple-inheritance1](https://media.geeksforgeeks.org/wp-
content/uploads/20200108144424/multiple-inheritance1.png)

**Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# multiple inheritance

# Base class1

class Mother:

 mothername = ""

 def mother(self):

 print(self.mothername)

# Base class2

class Father:

 fathername = ""

 def father(self):

 print(self.fathername)

# Derived class

class Son(Mother, Father):

 def parents(self):

 print("Father :", self.fathername)

 print("Mother :", self.mothername)

# Driver's code

s1 = Son()

s1.fathername = "RAM"

s1.mothername = "SITA"

s1.parents()  
  
---  
  
 __

 __

 **Output:**

    
    
    Father : RAM
    Mother : SITA
    

**Multilevel Inheritance**  
In multilevel inheritance, features of the base class and the derived class
are further inherited into the new derived class. This is similar to a
relationship representing a child and grandfather.  

![Multilevel-inheritance1](https://media.geeksforgeeks.org/wp-
content/uploads/20200108144705/Multilevel-inheritance1.png)

**Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# multilevel inheritance

# Base class

class Grandfather:

 def __init__(self, grandfathername):

 self.grandfathername = grandfathername

# Intermediate class

class Father(Grandfather):

 def __init__(self, fathername, grandfathername):

 self.fathername = fathername

 # invoking constructor of Grandfather class

 Grandfather.__init__(self, grandfathername)

# Derived class

class Son(Father):

 def __init__(self,sonname, fathername, grandfathername):

 self.sonname = sonname

 # invoking constructor of Father class

 Father.__init__(self, fathername, grandfathername)

 def print_name(self):

 print('Grandfather name :', self.grandfathername)

 print("Father name :", self.fathername)

 print("Son name :", self.sonname)

# Driver code

s1 = Son('Prince', 'Rampal', 'Lal mani')

print(s1.grandfathername)

s1.print_name()  
  
---  
  
 __

 __

 **Output:**

    
    
    Lal mani
    Grandfather name : Lal mani
    Father name : Rampal
    Son name : Prince
    

**Hierarchical Inheritance:** When more than one derived classes are created
from a single base this type of inheritance is called hierarchical
inheritance. In this program, we have a parent (base) class and two child
(derived) classes.  

![Hierarchical-inheritance1](https://media.geeksforgeeks.org/wp-
content/uploads/20200108144949/Hierarchical-inheritance1.png)

**Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# Hierarchical inheritance

# Base class

class Parent:

 def func1(self):

 print("This function is in parent class.")

# Derived class1

class Child1(Parent):

 def func2(self):

 print("This function is in child 1.")

# Derivied class2

class Child2(Parent):

 def func3(self):

 print("This function is in child 2.")

 

# Driver's code

object1 = Child1()

object2 = Child2()

object1.func1()

object1.func2()

object2.func1()

object2.func3()  
  
---  
  
 __

 __

 **Output:**

    
    
    This function is in parent class.
    This function is in child 1.
    This function is in parent class.
    This function is in child 2.
    
    
    

**Hybrid Inheritance:** Inheritance consisting of multiple types of
inheritance is called hybrid inheritance.  

**Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# hybrid inheritance

class School:

 def func1(self):

 print("This function is in school.")

 

class Student1(School):

 def func2(self):

 print("This function is in student 1. ")

 

class Student2(School):

 def func3(self):

 print("This function is in student 2.")

 

class Student3(Student1, School):

 def func4(self):

 print("This function is in student 3.")

 

# Driver's code

object = Student3()

object.func1()

object.func2()  
  
---  
  
 __

 __

**Output:**

    
    
    This function is in school.
    This function is in student 1.
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

