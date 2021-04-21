Inheritance and Composition in Python



 **Prerequisite –** **Classes and Objects in Python**

This article will compare and highlight the features of **is-a relation** and
**has-a relation** in Python.

##  **What is Inheritance (Is-A Relation)?**

It is a concept of Object-Oriented **** Programming. Inheritance is a
mechanism that allows us to inherit all the properties from another class. The
class from which the properties and functionalities are utilized is called the
**parent class (** also called as **Base Class)**. The class which uses the
properties from another class is called as **Child Class (** also known as
**Derived class)**. Inheritance is also called an **Is-A Relation**.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200916122044/Inheritance.jpeg)

Inheritance – diagrammatic representation

In the figure above, classes are represented as boxes. The inheritance
relationship is represented by an arrow pointing from **Derived Class(Child
Class)** to **Base Class(Parent Class)**. The extends keyword denotes that the
**Child Class** is inherited or derived from **Parent Class**.

**Syntax :**

  

  

    
    
    # Parent class
    class Parent :        
               # Constructor
               # Variables of Parent class
    
               # Methods
               ...
    
               ...
    
    
    # Child class inheriting Parent class 
    class Child(Parent) :  
               # constructor of child class
               # variables of child class
               # methods of child class
    
               ...
    
               ... 
    

**Example :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# parent class

class Parent:

 

 # parent class method

 def m1(self):

 print('Parent Class Method called...')

 

# child class inheriting parent class

class Child(Parent):

 

 # child class constructor

 def __init__(self):

 print('Child Class object created...')

 

 # child class method

 def m2(self):

 print('Child Class Method called...')

 

 

# creating object of child class

obj = Child()

 

# calling parent class m1() method

obj.m1()

 

# calling child class m2() method

obj.m2()  
  
---  
  
 __

 __

 **Output**

    
    
    Child Class object created...
    Parent Class Method called...
    Child Class Method called...
    
    

## **What is Composition (Has-A Relation)?**

It is one of the fundamental concepts of Object-Oriented **** Programming. In
this concept, we will describe a class that references to one or more objects
of other classes as an Instance variable. Here, by using the class name or by
creating the object we can access the members of one class inside another
class. It enables creating complex types by combining objects of different
classes. It means that a class Composite can contain an object of another
class Component. This type of relationship is known as **Has-A Relation**.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200916122520/composition.JPG)

composition – diagrammatic representation

In the above figure Classes are represented as boxes with the class name
**Composite** and **Component** representing Has-A relation between both of
them.

    
    
    class A :
    
          # variables of class A
          # methods of class A
          ...
          ...
    
    class B : 
          # by using "obj" we can access member's of class A.
          obj = A()
    
          # variables of class B
          # methods of class B
          
          ...
          ...
    

**Example :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

class Component:

 

 # composite class constructor

 def __init__(self):

 print('Component class object created...')

 

 # composite class instance method

 def m1(self):

 print('Component class m1() method executed...')

 

 

class Composite:

 

 # composite class constructor

 def __init__(self):

 

 # creating object of component class

 self.obj1 = Component()

 

 print('Composite class object also created...')

 

 # composite class instance method

 def m2(self):

 

 print('Composite class m2() method executed...')

 

 # calling m1() method of component class

 self.obj1.m1()

 

 

# creating object of composite class

obj2 = Composite()

 

# calling m2() method of composite class

obj2.m2()  
  
---  
  
 __

 __

 **Output**

    
    
    Component class object created...
    Composite class object also created...
    Composite class m2() method executed...
    Component class m1() method executed...
    
    

**Explanation:**

  * In the above example, we created two classes **Composite** and **Component** to show the **Has-A Relation** among them.
  * In the **Component class** , we have one constructor and an instance method **m1()**.
  * Similarly, in **Composite class** , we have one constructor in which we created an object of **Component Class.** Whenever we create an object of **Composite Class** , the object of **** the **Component class** is **** automatically created.
  * Now in **m2()** method of **Composite class** we are calling **m1()** method of **Component Class** using instance variable **obj1** in which reference of **Component Class** is stored.
  * Now, whenever we call **m2()** method of **Composite Class,** automatically **m1()** method of **Component Class** will be called.

##  **Composition vs Inheritance**

It’s big confusing among most of the people that both the concepts are
pointing to **Code Reusability** then **what is** the **difference b/w
Inheritance and Composition and when to use Inheritance and when to use
Composition?**

 **Inheritance** is used where a class wants to derive the nature of parent
class and then modify or extend the functionality of it. **Inheritance** will
extend the functionality with extra features allows **overriding of methods**,
but in the case of **Composition** , we can only use that class we can not
modify or extend the functionality of it. It will not provide extra features.
Thus, when one needs to use the class as it without any modification, the
composition is recommended and when one needs to change the behavior of the
method in another class, then inheritance is recommended.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

