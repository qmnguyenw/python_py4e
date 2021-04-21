Python3 Intermediate Level Topics



After going through the basics of python, you would be interested to know more
about further and bit more advance topics of the Python3 programming language.  
This article covers them.  
Please remember that Python completely works on indentation and it is advised
to practice it a bit by running some programs. Use the tab key to provide
indentation to your code.

This article is divided in following five sections:

  1.  **Classes**  
Just like every other Object Oriented Programming language Python supports
classes. Let’s look at some points on Python classes.

    * Classes are created by keyword **class**.
    * Attributes are the variables that belong to class.
    * Attributes are always public and can be accessed using dot (.) operator. Eg.: Myclass.Myattribute

A sample E.g for classes:

 __

 __  
 __

 __

 __  
 __  
 __

# creates a class named MyClass

class MyClass: 

 # assign the values to the MyClass attributes

 number = 0

 name = "noname"

 

def Main():

 # Creating an object of the MyClass. 

 # Here, 'me' is the object

 me = MyClass() 

 

 # Accessing the attributes of MyClass

 # using the dot(.) operator 

 me.number = 1337

 me.name = "Harssh"

 

 # str is an build-in function that 

 # creates an string

 print(me.name + " " + str(me.number))

 

# telling python that there is main in the program.

if __name__=='__main__': 

 Main()  
  
---  
  
 __

 __

Output :

  

  

    
        Harssh 1337
    

  2. **Methods**  
Method is a bunch of code that is intended to perform a particular task in
your Python’s code.

    * Function that belongs to a class is called an Method.
    * All methods require **‘self’** parameter. If you have coded in other OOP language you can think of ‘self’ as the ‘this’ keyword which is used for the current object. It unhides the current instance variable.’self’ mostly work like ‘this’.
    *  **‘def’** keyword is used to create a new method.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate working of class

# methods

 

class Vector2D:

 x = 0.0

 y = 0.0

 

 # Creating a method named Set

 def Set(self, x, y): 

 self.x = x

 self.y = y

 

def Main():

 # vec is an object of class Vector2D

 vec = Vector2D() 

 

 # Passing values to the function Set

 # by using dot(.) operator.

 vec.Set(5, 6) 

 print("X: " + str(vec.x) + ", Y: " + str(vec.y))

 

if __name__=='__main__':

 Main()  
  
---  
  
 __

 __

Output :

    
        X: 5, Y: 6

  3.  **Inheritance**  
Inheritance is defined as a way in which a particular class inherits features
from its base class.Base class is also knows as ‘Superclass’ and the class
which inherits from the Superclass is knows as ‘Subclass’

![Inheritance](https://media.geeksforgeeks.org/wp-
content/uploads/inheritance.jpg)

