Getter and Setter in Python



  
In Python, getters and setters are not the same as those in other object-
oriented programming languages. Basically, the main purpose of using getters
and setters in object-oriented programs is to ensure data encapsulation.
Private variables in python are not actually hidden fields like in other
object oriented languages. Getters and Setters in python are often used when:

  * We use getters & setters to add validation logic around getting and setting a value.
  * To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

 **Using normal function to achieve getters and setters behaviour**

To achieve getters & setters property, if we define normal get() and set()
methods it will not reflect any special implementation. For Example

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing a use

# of get() and set() method in

# normal function

 

class Geek:

 def __init__(self, age = 0):

 self._age = age

 

 # getter method

 def get_age(self):

 return self._age

 

 # setter method

 def set_age(self, x):

 self._age = x

 

raj = Geek()

 

# setting the age using setter

raj.set_age(21)

 

# retrieving age using getter

print(raj.get_age())

 

print(raj._age)  
  
---  
  
 __

 __

 **Output:**

    
    
    21
    21
    

In above code functions get_age() and set_age() acts as normal functions
and doesn’t play any impact as getters and setters, to achieve such
functionality Python has a special function property().

  

  

 **Using property() function to achieve getters and setters behaviour**

In Python property()is a built-in function that creates and returns a
property object. A property object has three methods, getter(), setter(), and
delete(). property() function in Python has four arguments property(fget,
fset, fdel, doc), fget is a function for retrieving an attribute value.
fset is a function for setting an attribute value. fdel is a function for
deleting an attribute value. doc creates a docstring for attribute. A
property object has three methods, getter(), setter(), and delete() to
specify fget, fset and fdel individually. For Example

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing a

# use of property() function

 

class Geeks:

 def __init__(self):

 self._age = 0

 

 # function to get value of _age

 def get_age(self):

 print("getter method called")

 return self._age

 

 # function to set value of _age

 def set_age(self, a):

 print("setter method called")

 self._age = a

 

 # function to delete _age attribute

 def del_age(self):

 del self._age

 

 age = property(get_age, set_age, del_age) 

 

mark = Geeks()

 

mark.age = 10

 

print(mark.age)  
  
---  
  
 __

 __

 **Output:**

    
    
    setter method called
    getter method called
    10
    

In above code there is only one print statement at line #25 but output
consists of three lines due to setter method set_age() called in line #23
and getter method get_age() called in line #25. Hence age is a property
object that helps to keep the access of private variable safe.

 **Using @property decorators to achieve getters and setters behaviour**

In previous method we used property() function in order to achieve getters
and setters behaviour. However as mentioned earlier in this post getters and
setters are also used for validating the getting and setting of attributes
value. There is one more way to implement property function i.e. by using
decorator. Python @property is one of the built-in decorators. The main
purpose of any decorator is to change your class methods or attributes in such
a way so that the user of your class no need to make any change in their code.
For Example

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing the use of

# @property

 

class Geeks:

 def __init__(self):

 self._age = 0

 

 # using property decorator

 # a getter function

 @property

 def age(self):

 print("getter method called")

 return self._age

 

 # a setter function

 @age.setter

 def age(self, a):

 if(a < 18):

 raise ValueError("Sorry you age is below eligibility criteria")

 print("setter method called")

 self._age = a

 

mark = Geeks()

 

mark.age = 19

 

print(mark.age)  
  
---  
  
 __

 __

 **Output:**

    
    
    setter method called
    getter method called
    19
    

In above code it is clear that how to use @property decorator to create
getters & setters in pythonic way. Line 15-16 acts as a validation code that
raises a ValueError if we try to initialize age with value less than 18, In
this way any kind of validation can be applied in getter or setter functions .

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

