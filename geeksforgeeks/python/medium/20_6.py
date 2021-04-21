classmethod() in Python



The **classmethod()** is an inbuilt function in Python, which returns a
class method for a given function.

>  **Syntax:** classmethod(function)
>
>  **Parameter :** This function accepts the function name as a parameter.
>
>  **Return Type:** This function returns the converted class method.

classmethod() methods are bound to a class rather than an object. Class
methods can be called by both class and object. These methods can be called
with a class or with an object. The examples below clearly illustrate this.

  

  

 **Example #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to understand the classmethod

 

class Student:

 

 # create a variable

 name = "Geeksforgeeks"

 

 # create a function

 def print_name(obj):

 print("The name is : ", obj.name)

 

# create print_name classmethod

# before creating this line print_name()

# It can be called only with object not with class

Student.print_name = classmethod(Student.print_name)

 

# now this method can be called as classmethod

# print_name() method is called a class method

Student.print_name()  
  
---  
  
 __

 __

 **Output:**

    
    
    The name is :  Geeksforgeeks
    

  
**Example #2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to understand the classmethod

 

class Subject:

 

 # create a variable

 favorite_subject = "Networking"

 

 # create a function

 def favorite_subject_name(obj):

 print("My favorite_subject_name is : ",

 obj.favorite_subject)

 

# create favorite_subject_name classmethod

# before creating this line favorite_subject_name()

# It can be called only with object not with class

Subject.favorite_subject_name =
classmethod(Subject.favorite_subject_name)

 

# now this method can be called as classmethod

# favorite_subject_name() method is called as class method

Subject.favorite_subject_name()  
  
---  
  
 __

 __

 **Output:**

    
    
    My favorite_subject_name is :  Networking
    

**Uses of classmethod()** classmethod() function is used in factory design
patterns where we want to call many functions with the class name rather than
object.

  
**The@classmethod Decorator:**

The @classmethod decorator, is a built-in function decorator which is an
expression that gets evaluated after your function is defined. The result of
that evaluation shadows your function definition.  
A class method receives the class as the implicit first argument, just like an
instance method receives the instance.

 **Syntax:**

    
    
     **class C(object):
        @classmethod
        def fun(cls, arg1, arg2, ...):**
           ....
    
    **fun:** the function that needs to be converted into a class method
    **returns:** a class method for function.
    

  * A class method is a method which is bound to the class and not the object of the class.
  * They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
  * It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that would be applicable to all the instances.

In the below example we use a staticmethod() and classmethod() to check if
a person is an adult or not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# use of a class method and static method.

from datetime import date

 

class Person:

 def __init__(self, name, age):

 self.name = name

 self.age = age

 

 # a class method to create a 

 # Person object by birth year.

 @classmethod

 def fromBirthYear(cls, name, year):

 return cls(name, date.today().year - year)

 

 # a static method to check if a

 # Person is adult or not.

 @staticmethod

 def isAdult(age):

 return age > 18

 

person1 = Person('mayank', 21)

person2 = Person.fromBirthYear('mayank', 1996)

 

print (person1.age)

print (person2.age)

 

# print the result

print (Person.isAdult(22))  
  
---  
  
 __

 __

 **Output:**

    
    
    21
    22
    True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

