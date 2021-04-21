How to create an empty class in Python?



A class is a user-defined blueprint or prototype from which objects are
created. Class can be considered as a user-defined data type. Generally, a
class contains data members known as attributes of the class and member
functions that are used to modify the attributes of the class. But have you
ever wondered how to define an empty class i.e a class without members and
member functions?

In Python, if we write something like the following, it would raise a
SyntaxError.

 __

 __  
 __

 __

 __  
 __  
 __

# Incorrect empty class in

# Python

 

class Geeks:  
  
---  
  
 __

 __

 **Output:**

    
    
      File "gfg.py", line 5
    
                    ^
    SyntaxError: unexpected EOF while parsing
    

In Python, to write an empty class pass statement is used. pass is a
special statement in Python that does nothing. It only works as a dummy
statement. However, objects of an empty class can also be created.

 **Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# empty class

 

class Geeks:

 pass

 

# Driver's code

obj = Geeks()

 

print(obj)  
  
---  
  
 __

 __

 **Output:**

    
    
    <__main__.Geeks object at 0x02B4A340>
    

Python also allows us to set the attributes of an object of an empty class. We
can also set different attributes for different objects. See the following
example for better understanding.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# empty class

 

 

class Employee:

 pass

 

 

# Driver's code

# Object 1 details

obj1 = Employee()

obj1.name = 'Nikhil'

obj1.office = 'GeeksforGeeks'

 

# Object 2 details

obj2 = Employee()

obj2.name = 'Abhinav'

obj2.office = 'GeeksforGeeks'

obj2.phone = 1234567889

 

 

# Printing details

print("obj1 Details:")

print("Name:", obj1.name)

print("Office:", obj1.office)

print()

 

print("obj2 Details:")

print("Name:", obj2.name)

print("Office:", obj2.office)

print("Phone:", obj2.phone)

 

 

# Uncommenting this print("Phone:", obj1.phone)

# will raise an AttributeError  
  
---  
  
 __

 __

 **Output:**

    
    
    obj1 Details:
    Name: Nikhil
    Office: GeeksforGeeks
    
    obj2 Details:
    Name: Abhinav
    Office: GeeksforGeeks
    Phone: 1234567889
    
    
    
    Traceback (most recent call last):
      File "gfg.py", line 34, in 
        print("Phone:", obj1.phone)
    AttributeError: 'Employee' object has no attribute 'phone'
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

