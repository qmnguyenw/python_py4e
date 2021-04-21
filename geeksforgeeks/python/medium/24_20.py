vars() function in Python



This is an inbuilt function in Python. The vars() method takes only one
parameter and that too is optional. It takes an object as a parameter which
may be can **a module, a class, an instance, or any object having __dict__
attribute.**  
 **Syntax:**

    
    
     **vars(object)**

The method returns the __dict__ attribute for a module, class, instance, or
any other object if the same has a __dict__ attribute. **If the object fails
to match the attribute, it raises a TypeError exception**. Objects such as
modules and instances have an updateable __dict__ attribute however, other
objects may have written restrictions on their __dict__ attributes. **vars()
acts like locals() method when an empty argument is passed** which implies
that the locals dictionary is only useful for reads since updates to the
locals dictionary are ignored.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# working of vars() method in Python

 

class Geeks:

 def __init__(self, name1 = "Arun", num2 = 46, name3 =
"Rishab"):

 self.name1 = name1

 self.num2 = num2

 self.name3 = name3

 

GeeksforGeeks = Geeks()

print(vars(GeeksforGeeks))  
  
---  
  
 __

 __

Output:

    
    
    {'num2': 46, 'name1': 'Arun', 'name3': 'Rishab'}

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrating

# the use of vars() and locals

# when no argument is passed and 

# how vars() act as locals().

class Geeks(object):

 def __init__(self):

 self.num1 = 20

 self.num2 = "this is returned"

 

 def __repr__(self):

 return "Geeks() is returned"

 

 def loc(self):

 ans = 21

 return locals()

 

 # Works same as locals()

 def code(self):

 ans = 10

 return vars()

 

 def prog(self):

 ans = "this is not printed"

 return vars(self)

 

 

if __name__ == "__main__":

 obj = Geeks()

 print (obj.loc())

 print (obj.code())

 print (obj.prog())  
  
---  
  
 __

 __

Output:

    
    
    {'ans': 21, 'self': Geeks() is returned}
    {'ans': 10, 'self': Geeks() is returned}
    {'num1': 20, 'num2': 'this is returned'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

