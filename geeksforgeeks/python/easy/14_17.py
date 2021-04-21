self in Python class



self represents the instance of the class. By using the “self” keyword we can
access the attributes and methods of the class in python. It binds the
attributes with the given arguments.

The reason you need to use self. is because Python does not use the @ syntax
to refer to instance attributes. Python decided to do methods in a way that
makes the instance to which the method belongs be passed automatically, but
not received automatically: the first parameter of methods is the instance the
method is called on

 __

 __  
 __

 __

 __  
 __  
 __

# Write Python3 code here

 

class car():

 

 # init method or constructor

 def __init__(self, model, color):

 self.model = model

 self.color = color

 

 def show(self):

 print("Model is", self.model )

 print("color is", self.color )

 

# both objects have different self which 

# contain their attributes

audi = car("audi a4", "blue")

ferrari = car("ferrari 488", "green")

 

audi.show() # same output as car.show(audi)

ferrari.show() # same output as car.show(ferrari)

 

# Behind the scene, in every instance method 

# call, python sends the instances also with

# that method call like car.show(audi)  
  
---  
  
 __

 __

 **Output:**

    
    
    Model is audi a4
    color is blue
    Model is ferrari 488
    color is green
    

**Self is a convention and not a real python keyword**  
self is parameter in function and user can use another parameter name in place
of it.But it is advisable to use self because it increase the readability of
code.

 __

 __  
 __

 __

 __  
 __  
 __

# Write Python3 code here

 

class this_is_class: 

 def show(in_place_of_self): 

 print("we have used another "

 "parameter name in place of self") 

 

object = this_is_class() 

object.show()   
  
---  
  
__

__

**Output:**

    
    
    we have used another parameter name in place of self
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

