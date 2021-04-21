Extend Class Method in Python



In Python, when a subclass defines a function that already exists in its
superclass in order to add some other functionality in its own way, the
function in the subclass is said to be an extended method and the mechanism is
known as extending. It is a way by which Python shows Polymorphism. This is
similar to overriding in Java and virtual methods in C++. A call from the
instance of the subclass executes the subclass’s version of the function. To
call superclass’s version super() method is used.

 **Why Extend a Function?**  
The goal of extending a class method in Python can be achieved by Inheritance.
One of the major advantages provided by extending a method is that it makes
the code reusable. Further, multiple subclasses can share the same code and
are even allowed to update it as per the requirement.

We’ll deal with both cases here

 **CASE 1: without extending a class method**

 __

 __  
 __

 __

 __  
 __  
 __

# definition of superclass "Triangles"

class Triangles(object):

 

 count = 0

 

 # Calling Constructor

 def __init__(self, name, s1, s2, s3):

 self.name = name

 self.s1 = s1

 self.s2 = s2

 self.s3 = s3

 Triangles.count+= 1

 

 def setName(self, name):

 self.name = name

 

 def setdim(self, s1, s2, s3):

 self.s1 = s1

 self.s2 = s2

 self.s3 = s3

 

 def getcount(self):

 return Triangles.count

 

 def __str__(self):

 return 'Name: '+self.name+'\nDimensions:
'+str(self.s1)+','+str(self.s2)+','+str(self.s3)

 

 

# describing a subclass 

# inherits from Triangles

class Peri(Triangles):

 

 # function to calculate the area 

 def calculate(self):

 self.pm = 0

 self.pm = self.s1 + self.s2 + self.s3

 

 # function to display just the area 

 # because it is not extended

 def display(self):

 return self.pm

 

 

def main():

 

 # instance of the subclass

 p = Peri('PQR', 2, 3, 4)

 # call to calculate()

 p.calculate()

 # explicit call to __str__()

 print(p.__str__())

 # call to display()

 print(p.display())

 

main()  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Name: PQR
    Dimensions: 2, 3, 4
    9
    

**CASE 2: extending a class method**

 __

 __  
 __

 __

 __  
 __  
 __

# definition of superclass "Triangles"

class Triangles(object):

 

 count = 0

 

 def __init__(self, name, s1, s2, s3):

 self.name = name

 self.s1 = s1

 self.s2 = s2

 self.s3 = s3

 Triangles.count+= 1

 

 def setName(self, name):

 self.name = name

 

 def setdim(self, s1, s2, s3):

 self.s1 = s1

 self.s2 = s2

 self.s3 = s3

 

 def getcount(self):

 return Triangles.count

 

 # superclass's version of display()

 def display(self):

 return 'Name: '+self.name+'\nDimensions:
'+str(self.s1)+', '+str(self.s2)+',
'+str(self.s3)

 

# definition of the subclass

# inherits from "Triangles"

class Peri(Triangles):

 

 def calculate(self):

 self.pm = 0

 self.pm = self.s1 + self.s2 + self.s3

 

 # extended method 

 def display(self):

 

 # calls display() of superclass 

 print (super(Peri, self).display())

 

 # adding its own properties 

 return self.pm

 

 

def main():

 

 # instance of the subclass

 p = Peri('PQR', 2, 3, 4)

 

 # call to calculate

 p.calculate()

 

 # one call is enough 

 print(p.display())

 

main()  
  
---  
  
 __

 __

 **Output:**

    
    
    Name: PQR
    Dimensions: 2, 3, 4
    9
    

The output produced in both cases is the same, the only difference being that
the second case makes it easier for other subclasses to inherit the methods
and “extend” them as required which as mentioned increases code reusability.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

